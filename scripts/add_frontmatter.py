#!/usr/bin/env python3
"""Add an AI-provenance front-matter block to every Markdown note.

Usage:  python3 scripts/add_frontmatter.py [REPO_ROOT] [--dry-run]

Targets every *.md under strands/ and findings/ of REPO_ROOT (default: the
folder above this script). Each note gets a YAML block like:

    ---
    ai-generated: true
    author: Claude (Anthropic AI model)
    model: not recorded
    directed-by: William John Suk (project lead)
    verified-by: none
    verification: mixed (see the label on each item)
    strand: candidates
    date: 2026-10-26
    ---

Rules
- Idempotent: a file whose first line is '---' and whose block already holds
  'ai-generated:' is left alone. A file with some other front matter is left
  alone too and reported, so nothing is overwritten.
- verified-by is 'none' unless community/verification_overrides.csv lists the
  file (columns: path,verified-by,verification,note). That CSV is how a human
  check is recorded later; re-running the script does not change files that
  already have a block, so edit the block by hand (or delete it and re-run)
  when a note is verified.
- 'model: not recorded' is deliberate: the working notes were written by
  several Claude models over Oct-Nov 2026 and the model behind each file was
  not logged. New AI-written notes should name the model.
- date comes from a YYYY-MM-DD in the file name; otherwise 'undated'.

Licence: MIT (see LICENSE.md).
"""
import csv
import re
import sys
from pathlib import Path

TARGET_DIRS = ("strands", "findings")
OVERRIDES = Path("community") / "verification_overrides.csv"
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def load_overrides(root):
    path = root / OVERRIDES
    out = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("path"):
                    out[row["path"].strip()] = row
    return out


def block_for(rel, override):
    parts = rel.parts
    strand = parts[1] if parts[0] == "strands" and len(parts) > 2 else parts[0]
    m = DATE_RE.search(rel.name)
    verified_by = (override or {}).get("verified-by") or "none"
    verification = (override or {}).get("verification") or "mixed (see the label on each item)"
    lines = [
        "---",
        "ai-generated: true",
        "author: Claude (Anthropic AI model)",
        "model: not recorded",
        "directed-by: William John Suk (project lead)",
        f"verified-by: {verified_by}",
        f"verification: {verification}",
        f"strand: {strand}",
        f"date: {m.group(1) if m else 'undated'}",
        "---",
        "",
    ]
    return "\n".join(lines) + "\n"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    root = Path(args[0]) if args else Path(__file__).resolve().parent.parent
    overrides = load_overrides(root)
    counts = {"added": 0, "already": 0, "other_frontmatter": 0, "verified": 0}
    per_dir = {}
    for d in TARGET_DIRS:
        for path in sorted((root / d).rglob("*.md")):
            rel = path.relative_to(root)
            text = path.read_text(encoding="utf-8")
            top = rel.parts[1] if rel.parts[0] == "strands" and len(rel.parts) > 2 else rel.parts[0]
            if text.startswith("---\n") or text.startswith("---\r\n"):
                end = text.find("\n---", 3)
                head = text[: end if end > 0 else 0]
                if "ai-generated:" in head:
                    counts["already"] += 1
                else:
                    counts["other_frontmatter"] += 1
                    print(f"SKIPPED (other front matter): {rel}")
                continue
            ov = overrides.get(str(rel))
            if ov and (ov.get("verified-by") or "none") != "none":
                counts["verified"] += 1
            if not dry:
                path.write_text(block_for(rel, ov) + text, encoding="utf-8")
            counts["added"] += 1
            per_dir[top] = per_dir.get(top, 0) + 1
    label = "would add" if dry else "added"
    print(f"{label}: {counts['added']}  already had block: {counts['already']}  "
          f"skipped (other front matter): {counts['other_frontmatter']}  "
          f"marked human-verified via overrides: {counts['verified']}")
    for k in sorted(per_dir):
        print(f"  {k}: {per_dir[k]}")


if __name__ == "__main__":
    main()
