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


def report_diff(**entries: list[str]):
    if len(entries) != 2:
        raise ValueError("Must only pass two keyword arguments")
    names = list(entries.keys())
    values = list(entries.values())
    print(
        f"Contents in {names[0]} do not match {names[1]}:",
        file=sys.stderr,
    )
    values0 = sorted(values[0], key=str.lower)
    values1 = sorted(values[1], key=str.lower)
    print(f"{names[0]}:", values0, file=sys.stderr)
    print(f"{names[1]}:", values1, file=sys.stderr)
    print(
        "Diff:",
        *unified_diff(
            values0,
            values1,
            fromfile=names[0],
            tofile=names[1],
        ),
        sep="\n",
    )
    print("----", file=sys.stderr)


def token(org):
    return os.environ.get("GITHUB_TOKEN")
    if org == "conda":
        return os.environ.get("CONDA_ORG_WIDE_TOKEN", "")
    if org == "conda-incubator":
        return os.environ.get("CONDA_INCUBATOR_ORG_WIDE_TOKEN", "")


def team_members(org: str, team: str) -> list[str]:
    api_url = f"https://api.github.com/orgs/{org}/teams/{team}/members"

    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {token(org)}",
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
        "Authorization": f"Bearer {token(org)}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(api_url, headers=headers, params={"per_page": 100})
    r.raise_for_status()
    return [f"{org}/{team['slug']}" for team in r.json()]


def access_to_repos(org, team):
    api_url = f"https://api.github.com/orgs/{org}/teams/{team}/repos"

    # Headers for authentication and proper API versioning
    headers = {
        "Authorization": f"Bearer {token(org)}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(api_url, headers=headers, params={"per_page": 100})
    r.raise_for_status()
    return [
        repo["full_name"]
        for repo in r.json()
        if repo["permissions"]["admin"] or repo["permissions"]["push"]
    ]


exit_code = 0
teams_in_github = [*teams_in_org("conda"), *teams_in_org("conda-incubator")]
seen_teams = []

for path in chain(ROOT.glob("teams/*.yml"), ROOT.glob("teams/*.yaml")):
    print("Checking", path.name, file=sys.stderr)
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
        exit_code = 1
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
        report_diff(file=members_in_file, github=members_in_gh)
        exit_code = 1
    repos_in_file = sorted(team["scopes"]["codeowners"] or [], key=str.lower)
    repos_in_gh = sorted(access_to_repos(org, name), key=str.lower)
    if set(repos_in_file) != set(repos_in_gh):
        report_diff(file=repos_in_file, github=repos_in_gh)
        exit_code = 1


if set(seen_teams) != set(teams_in_github):
    teams_in_repo = sorted(seen_teams, key=str.lower)
    teams_in_gh = sorted(teams_in_github, key=str.lower)
    report_diff(repo=teams_in_repo, github=teams_in_gh)
    exit_code = 1

sys.exit(exit_code)
