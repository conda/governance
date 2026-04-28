"""Replace content between STEERING-MEMBERS markers with the current steering.csv list.

Scans .yml, .yaml, and .md files under the repo root for
<!-- STEERING-MEMBERS --> / <!-- END-OF-STEERING-MEMBERS --> marker pairs and
regenerates the vote checklist between them, preserving the surrounding indentation.

Usage:
    python scripts/sync_steering_members.py          # update files in-place
    python scripts/sync_steering_members.py --check   # exit 1 if any file would change (for CI)
"""

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
STEERING_CSV = REPO_ROOT / "steering.csv"

EXTENSIONS = {".yml", ".yaml", ".md"}

START_MARKER = "<!-- STEERING-MEMBERS -->"
END_MARKER = "<!-- END-OF-STEERING-MEMBERS -->"

MARKER_RE = re.compile(
    rf"^(?P<indent>[ \t]*){re.escape(START_MARKER)}\n"
    rf"(?P<body>.*?)"
    rf"^(?P=indent){re.escape(END_MARKER)}",
    re.MULTILINE | re.DOTALL,
)


def build_checklist(csv_path: Path) -> str:
    """Return the bare checklist lines (no leading indent, no markers)."""
    lines: list[str] = []
    with csv_path.open(newline="") as f:
        for row in csv.DictReader(f):
            username = row["github_username"]
            name = row["name"]
            lines.append(f"@{username} ({name})")
            lines.append("- [ ]  yes")
            lines.append("- [ ]  no")
            lines.append("- [ ]  abstain")
            lines.append("")
    return "\n".join(lines)


def sync_file(path: Path, checklist: str, *, check: bool) -> bool:
    """Sync one file. Returns True if the file was (or would be) changed."""
    text = path.read_text()
    if START_MARKER not in text:
        return False

    def _replace(m: re.Match) -> str:
        indent = m.group("indent")
        indented = "\n".join(
            f"{indent}{line}" if line else "" for line in checklist.splitlines()
        )
        return f"{indent}{START_MARKER}\n{indented}\n{indent}{END_MARKER}"

    new_text = MARKER_RE.sub(_replace, text)
    if new_text == text:
        return False

    if not check:
        path.write_text(new_text)
    return True


def main() -> int:
    check = "--check" in sys.argv
    checklist = build_checklist(STEERING_CSV)

    changed: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if ".git" in path.parts:
            continue
        if sync_file(path, checklist, check=check):
            changed.append(path)

    if changed:
        verb = "would change" if check else "updated"
        for p in changed:
            print(f"{verb}: {p.relative_to(REPO_ROOT)}")
        if check:
            print("\nRun 'python scripts/sync_steering_members.py' to fix.")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
