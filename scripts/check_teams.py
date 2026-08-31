"""
Checks whether the members defined in the teams/*.yaml files correspond to their Github definitions.
It also makes sure that all teams in conda and conda-incubator are collected here.

We need one fine-grained token per organization (CONDA_ORG_WIDE_TOKEN,
CONDA_INCUBATOR_ORG_WIDE_TOKEN), with permissions:

- All repositories, metadata (read-only)
- Organization, metadata (read-only)
"""

# /// script
# dependencies = [
#   "requests",
#   "ruamel.yaml",
# ]
# ///

import os
import sys
from difflib import unified_diff
from functools import cache
from itertools import chain
from pathlib import Path

import requests
from ruamel.yaml import YAML

HERE = Path(__file__).parent
ROOT = HERE.parent
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def eprint(*args, indent=0, **kwargs):
    # kwargs.setdefault("file", sys.stderr)
    if indent:
        print(indent * " ", *args, **kwargs)
    else:
        print(*args, **kwargs)


def report_diff(
    field: str, indent: int = 2, warning: bool = False, **entries: str | list[str]
):
    if len(entries) != 2:
        raise ValueError("Must pass exactly two keyword arguments")
    names = list(entries.keys())
    values = list(entries.values())
    eprint(
        f"::{'warning' if warning else 'error'}::"
        f"Contents for {field} in {names[0]} do not match {names[1]}:",
        indent=indent,
    )
    values0 = (
        [str(val) for val in values[0]]
        if isinstance(values[0], (list, tuple))
        else [values[0] or ""]
    )
    values1 = (
        [str(val) for val in values[1]]
        if isinstance(values[1], (list, tuple))
        else [values[1] or ""]
    )
    eprint(f"{names[0]}:", values0, indent=indent)
    eprint(f"{names[1]}:", values1, indent=indent)
    for line in unified_diff(
        values0,
        values1,
        fromfile=names[0],
        tofile=names[1],
    ):
        eprint(line, indent=indent)
    eprint()


def gh(org, apipath):
    api_url = f"https://api.github.com/{apipath}"

    if org == "conda":
        token = os.environ.get("CONDA_ORG_WIDE_TOKEN")
    elif org == "conda-incubator":
        token = os.environ.get("CONDA_INCUBATOR_ORG_WIDE_TOKEN")
    else:
        token = None
    token = token or os.environ.get("GITHUB_TOKEN") or ""

    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(api_url, headers=headers, params={"per_page": 100})
    r.raise_for_status()
    return r.json()


@cache
def team_details(org: str, team: str) -> list[str]:
    return gh(org, f"orgs/{org}/teams/{team}")


@cache
def team_members(org: str, team: str) -> dict[str, bool]:
    result = gh(org, f"orgs/{org}/teams/{team}/members")
    return {member["login"]: member.get("inherited", False) for member in result}


@cache
def teams_in_org(org):
    result = gh(org, f"orgs/{org}/teams")
    return [f"{org}/{team['slug']}" for team in result]


@cache
def repos_in_org(org):
    result = gh(org, f"orgs/{org}/repos")
    return [repo["full_name"] for repo in result]


@cache
def access_to_repos(org, team):
    result = gh(org, f"orgs/{org}/teams/{team}/repos")
    return [
        repo["full_name"]
        for repo in result
        if (repo["permissions"]["admin"] or repo["permissions"]["push"])
        and "-ghsa-" not in repo["name"]
    ]


@cache
def teams_with_access_to_repo(org, repo):
    result = gh(org, f"repos/{org}/{repo}/teams")
    return [team["slug"] for team in result]


@cache
def collaborators(org, repo):
    result = gh(org, f"repos/{org}/{repo}/collaborators?affiliation=direct")
    return {user["login"]: user["role_name"] for user in result}


@cache
def all_yamls() -> list[Path]:
    return sorted(
        yml
        for yml in chain(ROOT.glob("teams/**/*.yml"), ROOT.glob("teams/**/*.yaml"))
        if not yml.name.startswith("__")
    )


def check_teams() -> int:
    seen_teams = set()
    seen_repos = set()

    print("======================")
    print("Individual YAML checks")
    print("======================")
    list_of_yamls = all_yamls()
    n_yamls = len(list_of_yamls)
    n_errors = 0
    n_warnings = 0
    for i, path in enumerate(list_of_yamls, 1):
        print(f"{i}/{n_yamls}: Checking", path.relative_to(ROOT), "...")
        with open(path) as f:
            team = yaml.load(f)
        if team.get("dissolved"):
            continue

        # Governance says:
        #   Proposers must specify the name, role & responsibility, members,
        #   and charter (dynamic or static) of any new sub-teams.
        # Name, charter and members are in the schema. Role and responsibility need to be enforced
        # in the free text field 'details':
        if team["charter"] in ("static-subteam", "dynamic-subteam"):
            details_lines = (team.get("details") or "").splitlines()
            for section, is_error in (
                ("Role", False),
                ("Responsibility", False),
                ("Membership", False),
            ):
                if f"## {section}" not in details_lines:
                    eprint(
                        f"{'::error::' if is_error else '::warning::'}"
                        f"'{team['charter']}' teams {'MUST' if is_error else 'SHOULD'} "
                        f"include a '## {section}' section under `details`.",
                        indent=4,
                    )
                    if is_error:
                        n_errors += 1
                    else:
                        n_warnings += 1

        for team_name in team.get("resources", {}).get("teams") or ():
            print("  Checking Github team name", team_name)
            # 0. Validate team names
            org, name = team_name.split("/")
            if org not in ("conda", "conda-incubator"):
                eprint(
                    "::error::Team must belong to the `conda` or `conda-incubator` orgs.",
                    indent=4,
                )
                n_errors += 1
                continue

            try:
                details = team_details(org, name)
            except requests.HTTPError as exc:
                if exc.response.status_code == 404:
                    eprint("::error::Team does not exist!", indent=4)
                else:
                    eprint("::error::Could not fetch team details:", exc, indent=4)
                n_errors += 1
                continue

            # 1. Validate descriptions
            print("  Checking Github team description")
            if (team["description"] or "").strip() != (
                details["description"] or ""
            ).strip():
                report_diff(
                    "descriptions",
                    file=(team["description"] or ""),
                    github=(details["description"] or ""),
                    indent=4,
                )
                n_errors += 1

            # 2. Validate team members
            print("  Checking team members")
            try:
                members = team_members(org, name)
            except Exception as exc:  # noqa
                eprint("::error::", type(exc).__name__, "-", exc, indent=4)
                n_errors += 1
                continue
            seen_teams.add(f"{org}/{name}")
            # Teams can have nested subteams. The member list of the parent team
            # includes the nested ones by default, but those are marked with inherited=true.
            # Separate direct membership from inherited to compare separately. By default,
            # our governance model does not rely on nested teams because it makes permission
            # management more complicated (e.g. emeritus members must be a separate team instead
            # of a nested one to facilitate offboarding permissions-wise).
            direct_members, inherited_members = [], []
            for member, inherited in members.items():
                if inherited:
                    inherited_members.append(member)
                else:
                    direct_members.append(member)
            if set(direct_members) != set(team["members"]):
                members_in_file = sorted(team["members"], key=str.lower)
                members_in_gh = sorted(direct_members, key=str.lower)
                report_diff(
                    "members", file=members_in_file, github=members_in_gh, indent=4
                )
                n_errors += 1
            if inherited_members:
                inherited_members_dashed = [
                    f"  - {m}" for m in sorted(set(inherited_members))
                ]
                eprint(
                    f"::error::Team {org}/{name} has inherited members coming from nested teams:",
                    *inherited_members_dashed,
                    sep="\n",
                    indent=4,
                )
                n_errors += 1
            # 3. Validate access to repositories
            print("  Checking repositories")
            repos_in_file = sorted(
                [
                    repo
                    for repo in team["resources"]["repos"] or []
                    if repo.startswith(f"{org}/")
                ],
                key=str.lower,
            )
            seen_repos.update(repos_in_file)
            repos_in_gh = sorted(access_to_repos(org, name), key=str.lower)
            if set(repos_in_file) != set(repos_in_gh):
                report_diff(
                    "repositories", file=repos_in_file, github=repos_in_gh, indent=4
                )
                n_errors += 1
            print("  ---")
        print("---")

    with open(ROOT / "teams" / "__orphaned__.yml") as f:
        orphaned = yaml.load(f)
    seen_teams.update(orphaned["teams"].keys())
    seen_repos.update(orphaned["repos"].keys())

    # 4. Check all teams are described
    print("=============================")
    print("Check all teams are described")
    print("=============================")
    teams_in_github = {*teams_in_org("conda"), *teams_in_org("conda-incubator")}

    if seen_teams != teams_in_github:
        teams_in_repo = sorted(seen_teams, key=str.lower)
        teams_in_gh = sorted(teams_in_github, key=str.lower)
        report_diff("teams", yamls=teams_in_repo, github=teams_in_gh, indent=2)
        n_errors += 1
        print("---")

    # 5. Check no individuals are granted access directly (everything must be a team)
    print("=============================")
    print("Check all repos are annotated")
    print("=============================")
    repos_with_direct_access = {}
    for repo in chain(repos_in_org("conda"), repos_in_org("conda-incubator")):
        if "-ghsa-" in repo:
            continue
        if repo not in seen_repos:
            eprint(
                f"::error::Repository '{repo}' is not annotated in any local team or orphaned YAMLs."
            )
            try:
                eprint(
                    "These teams have access:",
                    teams_with_access_to_repo(*repo.split("/")),
                    indent=2,
                )
            except requests.HTTPError as exc:
                eprint(
                    f"::error::Could not check teams with access to {repo} (HTTPError: {exc}), skipping...",
                    indent=2,
                )
            n_errors += 1
        try:
            if users := collaborators(*repo.split("/")):
                repos_with_direct_access[repo] = users
        except requests.HTTPError as exc:
            eprint(
                f"::error::Could not check collaborators for {repo} (HTTPError: {exc}), skipping...",
                indent=2,
            )
            continue
    print("================================================")
    print("Check no individuals are granted access directly")
    print("================================================")
    if repos_with_direct_access:
        eprint("::warning::Some users have direct access to repositories.")
        eprint("Direct repository access is reported for review.")
        for repo, users in repos_with_direct_access.items():
            n_warnings += 1
            print(f"- {repo}:")
            for user, level in sorted(users.items()):
                print(f"  - {user}: {level}")

    print("====================", "=" * len(str(max([n_warnings, n_errors]))), sep="")
    print("Number of errors:", n_errors)
    print("Number of warnings:", n_warnings)
    print("====================", "=" * len(str(max([n_warnings, n_errors]))), sep="")

    return n_errors


def generate():
    team_to_fn = {}
    for path in all_yamls():
        with open(path) as f:
            team = yaml.load(f)
            team_to_fn[team["name"]] = path

    for team in chain(teams_in_org("conda"), teams_in_org("conda-incubator")):
        org, team_name = team.split("/")
        if team_name in team_to_fn:
            continue
        Path("teams").mkdir(parents=True, exist_ok=True)
        output_path = Path("teams", f"{team_name.replace('.', '-')}.yml")
        if output_path.exists():
            continue
        details = team_details(org, team_name)
        data = {
            "name": team_name,
            "description": details["description"] or "",
            "charter": "unknown",
            "details": None,
            "resources": {
                "teams": [team],
                "repos": access_to_repos(org, team_name),
                "other": None,
            },
            "links": [],
            "members": {
                member: None
                for member, inherited in team_members(org, team_name).items()
                if not inherited
            },
            "emeritus": None,
        }
        output_path.write_text("# yaml-language-server: $schema=./teams.schema.json\n")
        with open(output_path, "a") as f:
            yaml.dump(data, f)


if __name__ == "__main__":
    if sys.argv[1:] and sys.argv[1] == "generate":
        sys.exit(generate())
    sys.exit(1 if check_teams() else 0)
