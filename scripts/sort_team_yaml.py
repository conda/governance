# /// script
# dependencies = [
#   "requests",
#   "ruamel.yaml",
#   "pydantic>=2,<3",
#   "email-validator",
# ]
# ///
import sys
from pathlib import Path

from ruamel.yaml import YAML

from schemas import CondaSubTeam

TEAM_KEY_ORDER = list(CondaSubTeam.model_fields.keys())

yaml = YAML(typ="rt")
yaml.preserve_quotes = True
yaml.width = 10000
yaml.indent(mapping=2, sequence=4, offset=2)

for path in sys.argv[1:]:
    path = Path(path)
    with open(path) as f:
        data = yaml.load(f)

    # NOTE: We use reversed pop + insert to preserve comments

    for key in reversed(TEAM_KEY_ORDER):
        # .pop() removes the key/value but RETAINS the comment in 'ca'
        val = data.pop(key, None)
        data.insert(0, key, val)

    for key in "members", "emeritus":
        if members := data.get(key):
            for key in sorted(members.keys(), reverse=True, key=str.lower):
                val = members.pop(key, None)
                members.insert(0, key, val)

    for key in reversed(("teams", "repos", "other")):
        val = data["resources"].pop(key, None)
        data["resources"].insert(0, key, val)

    path.write_text(
        "# NOTE: This file is a work in progress.\n"
        "# The information here reflected is provisional\n"
        "# and must not be interpreted as the ground truth.\n"
    )
    with open(path, "a") as f:
        yaml.dump(data, f)
