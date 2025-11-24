"""
Checks whether the members defined in the teams/*.yaml files correspond to their Github definitions.
It also makes sure that all teams in conda and conda-incubator are collected here.
"""

import os
import sys
from itertools import chain
from difflib import unified_diff
from pathlib import Path

import requests
from ruamel.yaml import YAML

HERE = Path(__file__).parent
ROOT = HERE.parent
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def eprint(*args, **kwargs):
    kwargs.setdefault("file", sys.stderr)
    print(*args, **kwargs)


def report_diff(field: str, **entries: list[str]):
    if len(entries) != 2:
        raise ValueError("Must pass exactly two keyword arguments")
    names = list(entries.keys())
    values = list([value or "" for value in entries.values()])
    eprint(f"Contents for {field} in {names[0]} do not match {names[1]}:")
    values0 = sorted(values[0], key=str.lower)
    values1 = sorted(values[1], key=str.lower)
    eprint(f"{names[0]}:", values0)
    eprint(f"{names[1]}:", values1)
    eprint(
        "Diff:",
        *unified_diff(
            values0,
            values1,
            fromfile=names[0],
            tofile=names[1],
        ),
        sep="\n",
    )
    eprint("----")


def gh(org, apipath):
    api_url = f"https://api.github.com/{apipath}"

    if org == "conda":
        token = os.environ.get("CONDA_ORG_WIDE_TOKEN")
    if org == "conda-incubator":
        token = os.environ.get("CONDA_INCUBATOR_ORG_WIDE_TOKEN")
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


def team_details(org: str, team: str) -> list[str]:
    return gh(org, f"orgs/{org}/teams/{team}")


def team_members(org: str, team: str) -> list[str]:
    result = gh(org, f"orgs/{org}/teams/{team}/members")
    return [member["login"] for member in result]


def teams_in_org(org):
    result = gh(org, f"orgs/{org}/teams")
    return [f"{org}/{team['slug']}" for team in result]


def repos_in_org(org):
    result = gh(org, f"orgs/{org}/repos")
    return [repo["full_name"] for repo in result]


def access_to_repos(org, team):
    result = gh(org, f"orgs/{org}/teams/{team}/repos")
    return [
        repo["full_name"]
        for repo in result
        if (repo["permissions"]["admin"] or repo["permissions"]["push"])
        and "-ghsa-" not in repo["name"]
    ]


def all_yamls() -> list[Path]:
    return sorted(chain(ROOT.glob("teams/**/*.yml"), ROOT.glob("teams/**/*.yaml")))


def check_teams() -> int:
    exit_code = 0
    teams_in_github = [*teams_in_org("conda"), *teams_in_org("conda-incubator")]
    seen_teams = []

    for path in all_yamls():
        eprint("Checking", path.relative_to(ROOT))
        with open(path) as f:
            team = yaml.load(f)

        # 0. Validate team name
        name_components = team["name"].split("/")
        if len(name_components) == 2:
            org, name = name_components
        elif len(name_components) == 1:
            org = "conda"
            name = name_components[0]
        else:
            eprint(f"Name {team['name']} must be '<team_name>' or '<org>/<team_name>'")
            exit_code = 1
            continue
        if org not in ("conda", "conda-incubator"):
            eprint("Team must belong to the `conda` or `conda-incubator` orgs.")
            exit_code = 1
            continue

        details = team_details(org, name)

        # 1. Validate descriptions
        if team["description"] != details["description"]:
            report_diff(
                "descriptions",
                file=[team["description"]],
                github=[details["description"]],
            )
            exit_code = 1

        # 2. Validate team members
        try:
            members = team_members(org, name)
        except Exception as exc:
            eprint(type(exc).__name__, "-", exc)
            eprint("----")
            exit_code = 1
            continue
        seen_teams.append(f"{org}/{name}")
        if set(members) != set(team["members"]):
            members_in_file = sorted(team["members"], key=str.lower)
            members_in_gh = sorted(members, key=str.lower)
            report_diff("members", file=members_in_file, github=members_in_gh)
            exit_code = 1

        # 3. Validate access to repositories
        repos_in_file = sorted(team["scopes"]["codeowners"] or [], key=str.lower)
        repos_in_gh = sorted(access_to_repos(org, name), key=str.lower)
        if set(repos_in_file) != set(repos_in_gh):
            report_diff("repositories", file=repos_in_file, github=repos_in_gh)
            exit_code = 1

    # 4. Check all teams are described
    if set(seen_teams) != set(teams_in_github):
        teams_in_repo = sorted(seen_teams, key=str.lower)
        teams_in_gh = sorted(teams_in_github, key=str.lower)
        report_diff("teams", repo=teams_in_repo, github=teams_in_gh)
        exit_code = 1

    # # 5. Check no individuals are granted access directly (everything must be a team)
    # for repo in chain(repos_in_org("conda"), repos_in_org("conda-incubator")):
    #     access = repo_access(*repo.split("/"))
    #     if access["usernames"]:
    #         eprint(f"Some users have direct access to `{repo}`:", access["usernames"])
    #         eprint("Repository access must be granted through teams only!")
    #         exit_code = 1

    return exit_code


def generate():
    team_to_fn = {}
    for path in all_yamls():
        with open(path) as f:
            team = yaml.load(f)
            team_to_fn[team["name"]] = path

    for team in chain(teams_in_org("conda"), teams_in_org("conda-incubator")):
        if team in team_to_fn:
            continue
        org, team_name = team.split("/")
        details = team_details(org, team_name)
        data = {
            "name": team,
            "description": details["description"],
            "charter": None,
            "requirements": None,
            "scopes": {"codeowners": access_to_repos(*team.split("/")), "other": None},
            "links": None,
            "members": {member: None for member in team_members(*team.split("/"))},
            "emeritus": None,
        }
        Path("teams", org).mkdir(parents=True, exist_ok=True)
        output_path = Path("teams", org, f"{team_name.replace('.', '-')}.yml")
        output_path.write_text("# yaml-language-server: $schema=../teams.schema.json\n")
        with open(output_path, "a") as f:
            yaml.dump(data, f)


if __name__ == "__main__":
    if sys.argv[1:] and sys.argv[1] == "generate":
        sys.exit(generate())
    sys.exit(check_teams())
