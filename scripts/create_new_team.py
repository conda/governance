import sys
from pathlib import Path

import schemas
from ruamel.yaml import YAML

TEAMS = Path(__file__).parent.parent / "teams"

team_name = sys.argv[1] if sys.argv[1:] else "REPLACE-ME"
team = schemas.CondaSubTeam(
    name=team_name,
    description=f"The {team_name} team",
    charter="unknown",
    details="Please fill this in",
    resources=schemas.Resources(repos=None, teams=None, other=None),
    links=[],
    members={"REPLACE-ME": None},
    emeritus=None,
)
yml_file = TEAMS.joinpath(f"{team_name}.yml")
yml_file.write_text("# yaml-language-server: $schema=./teams.schema.json\n")
with yml_file.open("a") as f:
    YAML().dump(team.model_dump(), f)
