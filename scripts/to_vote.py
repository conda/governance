from pathlib import Path

import sync_steering_members

print(sync_steering_members.build_checklist(Path("teams/steering-council.yml")))
