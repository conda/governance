"""
Checks whether the members defined in the teams/*.yaml files correspond to their Github definitions.
It also can check that all teams in the passed organizations are collected here, among others.

We need one organization-wide, read-only token per organization, passed as a JSON object in the
`GITHUB_TOKENS_PER_ORG` environment variable. For example:

    GITHUB_TOKENS_PER_ORG='{"conda": "xxx", "conda-incubator": "yyy"}'

We recommend using a GitHub App installed on each organization. The app needs:

- Repository permissions: Metadata (read-only, implicit), Administration (read-only)
- Organization permissions: Members (read-only)

Each installation must cover all repositories of its organization.

Then you can use:

```yaml
- uses: actions/create-github-app-token@64ab729a6294000f5aa4a4bc0b73d1f32bc45510 # v3.3.0
  id: token-for-org-name
  with:
      client-id: ${{ vars.CLIENT_ID }}
      private-key: ${{ secrets.PRIVATE_KEY }}
      owner: ORG-NAME # zizmor: ignore[github-app] auditing every team and repository is the point
      permission-administration: read
      permission-members: read
```

Fine-grained PATs also work (one per organization, with the organization as resource owner).
They need the same permissions as the app, with access to all repositories.
"""

# /// script
# dependencies = [
#   "requests",
#   "ruamel.yaml",
# ]
# requires-python = ">=3.11"
# ///

import json
import os
import sys
from collections.abc import Iterable
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
OPTIONAL_CHECKS = (
    "team-details",  # 'details' section in some charters must conform to a certain schema
    "descriptions-match",  # github team description is checked
    "inherited-members",  # no inherited access in this team from parent teams
    "all-teams-described",  # checks all teams in the org(s) are described by YAML
    "all-repos-described",  # checks all repos in the org(s) are described by YAML
    "direct-access",  # checks no repo has direct access from individuals
    "all-orgs-checked",  # teams/repos in YAMLs from orgs not being checked are errors, not warnings
    "org-owners",  # org owners match the members of the teams listing the org in resources.orgs
)


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


@cache
def gh_tokens():
    if tokens := os.environ.get("GITHUB_TOKENS_PER_ORG"):
        return json.loads(tokens)
    return {}


def gh(org, apipath):
    api_url = f"https://api.github.com/{apipath}"
    token = gh_tokens().get(org)
    if not token:
        raise ValueError(
            f"No token could be found for org '{org}'. "
            'Pass it via GITHUB_TOKENS_PER_ORG=\'{"org-name": "token"}\'.'
        )
    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    url, params, results = api_url, {"per_page": 100}, []
    while url:  # paginate
        if not url.startswith("https://api.github.com/"):
            raise RuntimeError(f"Refusing to send token to unexpected URL: {url}")
        r = requests.get(url, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        if not isinstance(data, list):
            return data
        results.extend(data)
        url = r.links.get("next", {}).get("url")
        params = None  # the next URL already carries the query string
    return results


@cache
def team_details(org: str, team: str) -> dict:
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
def org_owners(org) -> list[str]:
    result = gh(org, f"orgs/{org}/members?role=admin")
    return [user["login"] for user in result]


@cache
def all_yamls(teams_dir: str = "teams") -> list[Path]:
    teams_dir = ROOT / teams_dir
    return sorted(
        yml
        for yml in teams_dir.glob("**/*.y*l")
        if not yml.name.startswith("__") and yml.suffix in (".yml", ".yaml")
    )


def check_teams(
    *organizations: str,
    teams_dir: str = "teams",
    optional_checks: Iterable[str] = OPTIONAL_CHECKS,
) -> int:
    seen_teams = set()
    seen_repos = set()
    # teams_dir may live outside this repository (e.g. when used as a GitHub Action)
    display_root = (ROOT / teams_dir).parent
    unchecked: dict[str, str] = {}
    # Repos (in the checked orgs) referenced in the YAMLs, for the direct-access check
    mentioned_repos = set()
    # org -> {expected owner: [YAML files granting ownership]}
    expected_owners: dict[str, dict[str, list[str]]] = {}

    print("======================")
    print("Individual YAML checks")
    print("======================")
    list_of_yamls = all_yamls(teams_dir)
    n_yamls = len(list_of_yamls)
    n_errors = 0
    n_warnings = 0
    for i, path in enumerate(list_of_yamls, 1):
        print(f"{i}/{n_yamls}: Checking", path.relative_to(display_root), "...")
        with open(path) as f:
            team = yaml.load(f)
        if team.get("dissolved"):
            continue

        for org in (team.get("resources") or {}).get("orgs") or ():
            if org not in organizations:
                unchecked.setdefault(org, str(path.relative_to(display_root)))
                continue
            for member in team.get("members") or {}:
                expected_owners.setdefault(org, {}).setdefault(member, []).append(
                    str(path.relative_to(display_root))
                )

        # Governance says:
        #   Proposers must specify the name, role & responsibility, members,
        #   and charter (dynamic or static) of any new sub-teams.
        # Name, charter and members are in the schema. Role and responsibility need to be enforced
        # in the free text field 'details':
        if "team-details" in optional_checks and team["charter"] in (
            "static-subteam",
            "dynamic-subteam",
        ):
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
            if org not in organizations:
                eprint(
                    f"Not checked: '{org}' is not among the checked organizations.",
                    indent=4,
                )
                unchecked.setdefault(team_name, str(path.relative_to(display_root)))
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
            if "descriptions-match" in optional_checks:
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
            if "inherited-members" in optional_checks and inherited_members:
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
        for repo in team.get("resources", {}).get("repos") or ():
            if repo.split("/")[0] not in organizations:
                unchecked.setdefault(repo, str(path.relative_to(display_root)))
            else:
                mentioned_repos.add(repo)
        print("---")

    orphaned_path = ROOT / teams_dir / "__orphaned__.yml"
    with open(orphaned_path) as f:
        orphaned = yaml.load(f)
    for item in chain(orphaned["teams"] or (), orphaned["repos"] or ()):
        if item.split("/")[0] not in organizations:
            unchecked.setdefault(item, str(orphaned_path.relative_to(display_root)))
    mentioned_repos.update(
        repo for repo in orphaned["repos"] or () if repo.split("/")[0] in organizations
    )
    seen_teams.update(orphaned["teams"] or ())
    seen_repos.update(orphaned["repos"] or ())
    # Unchecked entries are reported below; keep them out of the GitHub comparisons
    seen_teams = {t for t in seen_teams if t.split("/")[0] in organizations}

    if unchecked:
        print("==============================================")
        print("Check all referenced organizations are checked")
        print("==============================================")
        strict = "all-orgs-checked" in optional_checks
        unchecked_orgs = sorted({item.split("/")[0] for item in unchecked})
        eprint(
            f"::{'error' if strict else 'warning'}::"
            f"{len(unchecked)} teams/repos/orgs belong to organizations that were not checked "
            f"({', '.join(unchecked_orgs)}). Maybe missing some in the CLI?"
        )
        for item, source in sorted(unchecked.items(), key=lambda kv: kv[0].lower()):
            eprint(f"- {item} (in {source})", indent=2)
        if strict:
            n_errors += len(unchecked)
        else:
            n_warnings += len(unchecked)
        print("---")

    if "org-owners" in optional_checks:
        print("===============================")
        print("Check organization owners match")
        print("===============================")
        for org in organizations:
            if org not in expected_owners:
                eprint(
                    f"::warning::No team lists '{org}' in resources.orgs, "
                    "so its owners can't be checked."
                )
                n_warnings += 1
                continue
            try:
                owners = org_owners(org)
            except requests.HTTPError as exc:
                eprint(f"::error::Could not fetch the owners of {org}: {exc}")
                n_errors += 1
                continue
            expected = expected_owners[org]
            if set(owners) != set(expected):
                report_diff(
                    f"{org} owners",
                    yamls=sorted(expected, key=str.lower),
                    github=sorted(owners, key=str.lower),
                    indent=2,
                )
                for user in sorted(set(owners) - set(expected), key=str.lower):
                    eprint(
                        f"- {user} is an owner of {org}, but not a member of any team "
                        "listing it in resources.orgs",
                        indent=2,
                    )
                for user in sorted(set(expected) - set(owners), key=str.lower):
                    eprint(
                        f"- {user} should be an owner of {org} as a member of "
                        f"{', '.join(expected[user])}",
                        indent=2,
                    )
                n_errors += 1
            print("---")

    if "all-teams-described" in optional_checks:
        # 4. Check all teams are described
        print("=============================")
        print("Check all teams are described")
        print("=============================")
        teams_in_github = {team for org in organizations for team in teams_in_org(org)}

        if seen_teams != teams_in_github:
            teams_in_repo = sorted(seen_teams, key=str.lower)
            teams_in_gh = sorted(teams_in_github, key=str.lower)
            report_diff("teams", yamls=teams_in_repo, github=teams_in_gh, indent=2)
            n_errors += 1
            print("---")

    if "all-repos-described" in optional_checks:
        print("=============================")
        print("Check all repos are annotated")
        print("=============================")
        repos_to_audit = []
        for repo in chain(*(repos_in_org(org) for org in organizations)):
            if "-ghsa-" in repo:
                continue
            repos_to_audit.append(repo)
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
    else:
        # Without the org-wide listing, only audit the repos referenced in the YAMLs.
        # This keeps the number of API calls proportional to the YAMLs, not to the org size.
        repos_to_audit = sorted(mentioned_repos, key=str.lower)

    # 5. Check no individuals are granted access directly (everything must be a team)
    if "direct-access" in optional_checks:
        print("================================================")
        print("Check no individuals are granted access directly")
        print("================================================")
        if "all-repos-described" not in optional_checks:
            print(
                f"Checking the {len(repos_to_audit)} repositories mentioned in the YAMLs "
                "('all-repos-described' is disabled)."
            )
        repos_with_direct_access = {}
        for repo in repos_to_audit:
            try:
                if users := collaborators(*repo.split("/")):
                    repos_with_direct_access[repo] = users
            except requests.HTTPError as exc:
                eprint(
                    f"::error::Could not check collaborators for {repo} (HTTPError: {exc}), skipping...",
                    indent=2,
                )
                n_errors += 1
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


def generate(*organizations: str, teams_dir: str = "teams"):
    team_to_fn = {}
    for path in all_yamls(teams_dir):
        with open(path) as f:
            team = yaml.load(f)
            team_to_fn[team["name"]] = path

    for team in chain(*(teams_in_org(org) for org in organizations)):
        org, team_name = team.split("/")
        if team_name in team_to_fn:
            continue
        output_dir = ROOT / teams_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{team_name.replace('.', '-')}.yml"
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


def cli():
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument(
        "--generate",
        action="store_true",
        help="Instead of checking compliance, create a YAML file for each team in the passed "
        "organizations that is not fully described yet.",
    )
    p.add_argument(
        "--teams-dir",
        help="Directory where the YAML files for each team are stored.",
        default="teams",
    )
    p.add_argument(
        "-x",
        "--exclude-checks",
        help="Comma-separated string of optional checks to skip. Choose 'all' to skip all of them. ",
    )
    p.add_argument(
        "organizations",
        nargs="+",
        help="Github organization(s) to check. Please provide Github tokens for each in "
        "$GITHUB_TOKENS_PER_ORG set to a JSON string mapping org names to tokens",
        metavar="ORG",
    )
    return p


def main() -> int:
    args = cli().parse_args()

    tokens = gh_tokens()
    if not isinstance(tokens, dict):
        raise SystemExit(
            "GITHUB_TOKENS_PER_ORG must be a JSON object mapping org names to tokens."
        )
    if missing := sorted(set(args.organizations) - tokens.keys()):
        raise SystemExit(f"No token in GITHUB_TOKENS_PER_ORG for: {', '.join(missing)}")

    if args.generate:
        generate(*args.organizations, teams_dir=args.teams_dir)
        return 0

    exclude_checks = (args.exclude_checks or "").split(",")
    if exclude_checks == [""]:
        exclude_checks = []
    if invalid := set(exclude_checks).difference({"all", *OPTIONAL_CHECKS}):
        raise ValueError(f"Some exclude-checks values are not recognized: {invalid}")
    if "all" in exclude_checks:
        optional_checks = []
    elif exclude_checks:
        optional_checks = [c for c in OPTIONAL_CHECKS if c not in exclude_checks]
    else:
        optional_checks = OPTIONAL_CHECKS
    n_errors = check_teams(
        *args.organizations, teams_dir=args.teams_dir, optional_checks=optional_checks
    )
    return 1 if n_errors else 0


if __name__ == "__main__":
    sys.exit(main())
