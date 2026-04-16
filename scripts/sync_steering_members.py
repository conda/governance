"""Sync steering council data from CSV files into marker-delimited sections.

Scans .yml, .yaml, and .md files under the repo root for marker pairs and
regenerates content between them, preserving the surrounding indentation.

Supported markers:
    <!-- STEERING-CHECKLIST --> / <!-- END-OF-STEERING-CHECKLIST -->
        Vote checklist (yes/no/abstain per member) from steering.csv
    <!-- STEERING-TABLE --> / <!-- END-OF-STEERING-TABLE -->
        Markdown table of current members from steering.csv
    <!-- EMERITUS-TABLE --> / <!-- END-OF-EMERITUS-TABLE -->
        Markdown table of emeritus members from emeritus.csv

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
EMERITUS_CSV = REPO_ROOT / "emeritus.csv"

EXTENSIONS = {".yml", ".yaml", ".md"}

MARKER_RE = re.compile(
    r"^(?P<indent>[ \t]*)<!-- (?P<name>[A-Z-]+) -->\n"
    r"(?P<body>.*?)"
    r"^(?P=indent)<!-- END-OF-(?P=name) -->",
    re.MULTILINE | re.DOTALL,
)


def build_checklist(csv_path: Path) -> str:
    """Return per-member vote checklist lines (yes/no/abstain)."""
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


def build_table(csv_path: Path) -> str:
    """Return a markdown table of members sorted alphabetically by first name."""
    with csv_path.open(newline="") as f:
        rows = sorted(csv.DictReader(f), key=lambda r: r["name"].lower())

    lines = ["| Name | GitHub | Funder | Pronouns |", "| --- | --- | --- | --- |"]
    for row in rows:
        name = row["name"]
        username = row["github_username"]
        funder = row.get("funder", "") or ""
        pronouns = row.get("pronouns", "") or ""
        lines.append(
            f"| {name} | [@{username}](https://github.com/{username}) | {funder} | {pronouns} |"
        )
    return "\n".join(lines)


def sync_file(path: Path, contents: dict[str, str], *, check: bool) -> bool:
    """Sync one file. Returns True if the file was (or would be) changed."""
    text = path.read_text()

    def _replace(m: re.Match) -> str:
        name = m.group("name")
        if name not in contents:
            return m.group(0)
        indent = m.group("indent")
        indented = "\n".join(
            f"{indent}{line}" if line else "" for line in contents[name].splitlines()
        )
        return f"{indent}<!-- {name} -->\n{indented}\n{indent}<!-- END-OF-{name} -->"

    new_text = MARKER_RE.sub(_replace, text)
    if new_text == text:
        return False

    if not check:
        path.write_text(new_text)
    return True


def main() -> int:
    check = "--check" in sys.argv
    contents = {
        "STEERING-CHECKLIST": build_checklist(STEERING_CSV),
        "STEERING-TABLE": build_table(STEERING_CSV),
        "EMERITUS-TABLE": build_table(EMERITUS_CSV),
    }

    changed: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if ".git" in path.parts:
            continue
        if sync_file(path, contents, check=check):
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
