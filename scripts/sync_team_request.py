"""Create or update a draft team record from a new-team issue form."""

import base64
import io
import json
import os
import re
from pathlib import Path

import requests
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
from schemas import CondaSubTeam, Resources

REPOSITORY = "conda/governance"
BOT = "github-actions[bot]"
TYPES = {
    "Sub-team (Dynamic Charter)": "dynamic-subteam",
    "Sub-team (Static Charter)": "static-subteam",
    "Project Team": "unknown",
}
FIELDS = (
    "Type of Team",
    "Team Name",
    "Team Handle",
    "Members",
    "Charter",
    "Responsibilities",
    "Scope",
    "Checklist",
)


def form_fields(body):
    fields = {}
    duplicates = []
    current = None
    fence = None
    for line in body.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, rest = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not rest.strip():
                fence = None
        elif fence is None and line.startswith("### "):
            label = line[4:].strip()
            if label in FIELDS:
                if label in fields:
                    duplicates.append(label)
                current = label
                fields[label] = []
                continue
        if current is not None:
            fields[current].append(line)
    if len(set(fields).intersection(FIELDS[:3])) < 2:
        return {}
    if duplicates:
        raise ValueError(f"The form contains more than one {duplicates[0]} section.")
    return {
        key: "" if (text := "\n".join(lines).strip()) == "_No response_" else text
        for key, lines in fields.items()
    }


def render_team(body: str, issue_url: str) -> tuple[str, str] | None:
    fields = form_fields(body)
    if not fields:
        return None
    for key in FIELDS[:5]:
        if not fields.get(key):
            raise ValueError(
                f"Complete the {key} field before generating a team record."
            )
    if fields["Type of Team"] not in TYPES:
        raise ValueError("Choose one of the supported Type of Team options.")
    name = fields["Team Name"]
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,127}", name):
        raise ValueError(
            "Team Name must be a lowercase slug, starting with a letter or number."
        )
    handle = fields["Team Handle"].removeprefix("@")
    if not re.fullmatch(
        r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?/[A-Za-z0-9_-]{1,128}",
        handle,
    ):
        raise ValueError("Team Handle must use the organization/team format.")
    members = {}
    for line in re.split(r"[,\n]", fields["Members"]):
        if not line.strip():
            continue
        match = re.fullmatch(
            r"(?:[-*] )?@?([A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?)",
            line.strip(),
        )
        if not match:
            raise ValueError(
                "Members must contain only GitHub usernames, separated by lines or commas."
            )
        members[match[1].lower()] = None
    if not members:
        raise ValueError("List at least one proposed member.")
    details = "\n\n".join(
        f"## {heading}\n\n{fields[field]}"
        for field, heading in (
            ("Charter", "Role"),
            ("Responsibilities", "Responsibility"),
            ("Scope", "Scope"),
        )
        if fields.get(field)
    )
    team = CondaSubTeam(
        name=name,
        description=f"The {name} team",
        charter=TYPES[fields["Type of Team"]],
        details=details or None,
        resources=Resources(teams=[handle], repos=None, other=None),
        links=[issue_url],
        members=dict(sorted(members.items())),
        emeritus=None,
    )
    data = team.model_dump(mode="json", exclude_defaults=True)
    if details:
        data["details"] = LiteralScalarString(details + "\n")
    yaml = YAML()
    yaml.width = 10000
    yaml.indent(mapping=2, sequence=4, offset=2)
    output = io.StringIO()
    output.write("# yaml-language-server: $schema=./teams.schema.json\n")
    yaml.dump(data, output)
    return f"teams/{name}.yml", output.getvalue()


class GitHub:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )

    def request(self, method, endpoint, *, missing_ok=False, **kwargs):
        response = self.session.request(
            method,
            f"https://api.github.com/repos/{REPOSITORY}/{endpoint}".rstrip("/"),
            timeout=30,
            **kwargs,
        )
        if missing_ok and response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, *, missing_ok=False, **params):
        return self.request("GET", endpoint, missing_ok=missing_ok, params=params)

    def post(self, endpoint, **data):
        return self.request("POST", endpoint, json=data)

    def patch(self, endpoint, **data):
        return self.request("PATCH", endpoint, json=data)

    def list(self, endpoint, **params):
        page = 1
        while True:
            items = self.get(endpoint, per_page=100, page=page, **params)
            yield from items
            if len(items) < 100:
                break
            page += 1


def file_content(api, path, ref):
    data = api.get(f"contents/{path}", ref=ref, missing_ok=True)
    if data is None:
        return None
    if data.get("type") != "file" or data.get("encoding") != "base64":
        raise ValueError("The team record must be a regular text file.")
    return base64.b64decode(data["content"]).decode("utf-8")


def check_branch(api, head, base, path, number):
    comparison = api.get(f"compare/{base}...{head}")
    files = comparison["files"]
    if len(files) != 1 or files[0]["filename"] != path or files[0]["status"] != "added":
        raise ValueError(
            "Sync paused: the branch changes other files or the team name changed."
        )
    message = f"Sync team record from issue #{number}"
    last_generated = next(
        (
            commit["sha"]
            for commit in api.list("commits", sha=head, path=path)
            if (commit.get("committer") or {}).get("login") == BOT
            and commit["commit"]["message"] == message
        ),
        None,
    )
    if last_generated is None:
        raise ValueError("Sync paused: the branch was not created by this workflow.")
    current = file_content(api, path, head)
    if current != file_content(api, path, last_generated):
        raise ValueError(
            "Sync paused: the team record has human edits. Complete the PR manually."
        )
    return current


def record_pr_body(number):
    template = (
        Path(__file__).resolve().parents[1]
        / ".github/PULL_REQUEST_TEMPLATE/add-team.md"
    ).read_text()
    template = "\n".join(
        line for line in template.splitlines() if line != "- [ ] CI is passing"
    )
    for completed in (
        "I have started this PR from a branch, not a fork",
        "I have used `pixi run create_new_team <name>` or equivalent",
    ):
        template = template.replace(f"- [ ] {completed}", f"- [x] {completed}")
    return (
        f"<!-- team-request:{number} -->\n\nCloses #{number}.\n\n"
        "This draft records the proposal in the issue body.\n\n"
        "- Updates pause while the issue or PR is closed, the PR is ready for review, or the generated YAML has human edits.\n"
        "- Updates can resume on the next issue-body edit or issue reopening once both the issue and PR are open, "
        "the PR is a draft, and the YAML matches the bot's last version. Complete the PR manually if you want to keep human edits to the YAML.\n"
        "- Merging the PR ends synchronization.\n\n"
        "Before marking this PR ready, complete the team record and confirm that it matches the approved proposal. "
        "For project teams, replace `unknown` with the agreed project type. Add repository assignments and the approval link.\n\n"
        f"{template}\n"
    )


def sync_issue(api, number):
    issue = api.get(f"issues/{number}")
    if issue["state"] != "open" or "pull_request" in issue:
        return "The issue is closed or is a pull request. No changes made."
    issue_url = f"https://github.com/{REPOSITORY}/issues/{number}"
    generated = render_team(issue.get("body") or "", issue_url)
    if generated is None:
        return "This is not a new-team issue. No changes made."
    path, content = generated
    branch = f"fix/team-request-{number}"
    marker = f"<!-- team-request:{number} -->"
    prs = list(api.list("pulls", state="all", head=f"conda:{branch}"))
    if len(prs) > 1:
        raise ValueError("Sync paused: multiple PRs use the team-request branch.")
    pr = prs[0] if prs else None
    if pr and pr.get("merged_at"):
        return "The record PR has merged. Synchronization has ended."
    if pr and (pr["state"] != "open" or not pr["draft"]):
        return "Sync paused: the record PR is closed or ready for review."
    default_branch = api.get("")["default_branch"]
    if pr and (
        marker not in (pr.get("body") or "")
        or pr["user"]["login"] != BOT
        or pr["head"]["repo"]["full_name"] != REPOSITORY
        or pr["head"]["ref"] != branch
        or pr["base"]["ref"] != default_branch
    ):
        raise ValueError(
            "Sync paused: the existing PR does not belong to this workflow."
        )
    base = api.get(f"git/ref/heads/{default_branch}")["object"]["sha"]
    if file_content(api, path, base) is not None:
        raise ValueError(
            "A team record with this name already exists. No changes made."
        )
    ref = api.get(f"git/ref/heads/{branch}", missing_ok=True)
    if pr and ref is None:
        raise ValueError("Sync paused: the record PR branch is missing.")
    head = ref["object"]["sha"] if ref else base
    current = check_branch(api, head, base, path, number) if ref else None
    if content != current:
        parent = api.get(f"git/commits/{head}")
        tree = api.post(
            "git/trees",
            base_tree=parent["tree"]["sha"],
            tree=[{"path": path, "mode": "100644", "type": "blob", "content": content}],
        )
        commit = api.post(
            "git/commits",
            message=f"Sync team record from issue #{number}",
            tree=tree["sha"],
            parents=[head],
        )
        # A non-fast-forward update fails if somebody changed the branch meanwhile.
        if ref:
            if pr:
                latest = api.get(f"pulls/{pr['number']}")
                if (
                    latest["state"] != "open"
                    or latest.get("merged_at")
                    or not latest["draft"]
                ):
                    return (
                        "The record PR is no longer an open draft. No update published."
                    )
                if latest["head"]["sha"] != head:
                    raise ValueError(
                        "Sync paused: the PR branch changed during this run."
                    )
            api.patch(f"git/refs/heads/{branch}", sha=commit["sha"], force=False)
        else:
            api.post("git/refs", ref=f"refs/heads/{branch}", sha=commit["sha"])
    if pr:
        return f"{'Updated' if content != current else 'No changes needed for'} {pr['html_url']}"
    # The branch may already exist after an interrupted run. Reuse it and create the missing PR.
    pr = api.post(
        "pulls",
        head=branch,
        base=default_branch,
        draft=True,
        title=f"Add {Path(path).stem} team",
        body=record_pr_body(number),
    )
    return f"Created {pr['html_url']}"


def main():
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise ValueError("This workflow only supports conda/governance.")
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    if event.get("repository", {}).get("full_name") != REPOSITORY:
        raise ValueError("Unexpected event repository.")
    if event.get("action") not in {"opened", "edited", "reopened"}:
        return
    if event["action"] == "edited" and "body" not in event.get("changes", {}):
        return
    number = event["issue"]["number"]
    if type(number) is not int or number < 1:
        raise ValueError("Invalid issue number.")
    result = sync_issue(GitHub(os.environ["GH_TOKEN"]), number)
    print(result)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a") as output:
            output.write(result + "\n")


if __name__ == "__main__":
    main()
