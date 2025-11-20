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
yaml = YAML(typ="safe")
GH_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def team_members(org: str, name: str) -> list[str]:
    api_url = f"https://api.github.com/orgs/{org}/teams/{name}/members"

    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(api_url, headers=headers, params={"per_page": 100})
    r.raise_for_status()
    return [member["login"] for member in r.json()]


def teams_in_org(org):
    api_url = f"https://api.github.com/orgs/{org}/teams"

    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(api_url, headers=headers, params={"per_page": 100})
    r.raise_for_status()
    return [f"{org}/{team['slug']}" for team in r.json()]


exit_code = 0
teams_in_github = [*teams_in_org("conda"), *teams_in_org("conda-incubator")]
seen_teams = []

for path in chain(ROOT.glob("teams/*.yml"), ROOT.glob("teams/*.yaml")):
    with open(path) as f:
        team = yaml.load(path)
    name_components = team["name"].split("/")
    if len(name_components) == 2:
        org, name = name_components
    elif len(name_components) == 1:
        org = "conda"
        name = name_components[0]
    else:
        print(
            f"Name {team['name']} must be '<team_name>' or '<org>/<team_name>'",
            file=sys.stderr,
        )
    try:
        members = team_members(org, name)
    except Exception as exc:
        print(type(exc).__name__, "-", exc, file=sys.stderr)
        print("----", file=sys.stderr)
        exit_code = 1
        continue
    seen_teams.append(f"{org}/{name}")
    if set(members) != set(team["members"]):
        members_in_file = sorted(team["members"], key=str.lower)
        members_in_gh = sorted(members, key=str.lower)
        print(
            f"Members in '{path.name}' are not in sync with team '@{org}/{name}':",
            file=sys.stderr,
        )
        print("File:", members_in_file, file=sys.stderr)
        print("Github:", members_in_gh, file=sys.stderr)
        print(
            "Diff:",
            *unified_diff(
                members_in_file, members_in_gh, fromfile=path.name, tofile="Github"
            ),
            sep="\n",
        )
        print("----", file=sys.stderr)
        exit_code = 1

if set(seen_teams) != set(teams_in_github):
    teams_in_repo = sorted(seen_teams, key=str.lower)
    teams_in_gh = sorted(teams_in_github, key=str.lower)
    print("Teams in repo do not match Github teams:", file=sys.stderr)
    print("Repo:", teams_in_repo, file=sys.stderr)
    print("Github:", teams_in_gh, file=sys.stderr)
    print(
        "Diff:",
        *unified_diff(teams_in_repo, teams_in_gh, fromfile="Repo", tofile="Github",),
        sep="\n",
    )

    print("----", file=sys.stderr)
    exit_code = 1

sys.exit(exit_code)
