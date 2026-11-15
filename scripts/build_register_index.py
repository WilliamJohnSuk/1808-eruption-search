#!/usr/bin/env python3
"""Build a compact index of sources/register.md.

The register is a single large Markdown file (about 400 KB) made of lettered
and numbered sections (A, B1 ... B80, C, D, E, E2, F), each with a table of
sources. This script writes one line per section, so that a person or an AI
agent can find the right section without loading the whole register:

    sources/register_index.csv   machine-readable
    sources/register_index.md    the same, as a Markdown table

Columns: id, line (where the section starts in register.md), title (the
section heading, shortened), date (first date in the heading), strand
(folder under strands/ of the notes file the section cites), notes_files
(notes cited in the heading or the section's first lines, resolved to their
path in this repository), other_files (data, script and figure paths cited),
rows (table rows in the section), rows_not_reached (rows whose text contains
a phrase such as "not reached", "blocked" or "catalogue only").

rows_not_reached is a rough keyword count, not a reading of each row: use it
to spot sections with many unreached sources, then read the rows themselves.

Usage, from the repository root (plain Python 3, no dependencies):

    python3 scripts/build_register_index.py

Re-run it after any change to sources/register.md and commit the two outputs
with that change.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTER = os.path.join(ROOT, "sources", "register.md")
OUT_CSV = os.path.join(ROOT, "sources", "register_index.csv")
OUT_MD = os.path.join(ROOT, "sources", "register_index.md")

HEADING = re.compile(r"^(#{2,4})\s+(.*\S)\s*$")
SECTION_ID = re.compile(r"^([A-Z]\d{0,3})(?=[.\s:(]|$)")
DATE = re.compile(
    r"\b(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]* 20\d\d"
    r"|20\d\d-\d\d-\d\d)\b"
)
PATH = re.compile(
    r"(?<![\w/])((?:notes|data|scripts|figures|strands|access|findings)/[\w.\-]+(?:/[\w.\-]+)*"
    r"|[\w\-]+_[\w\-]*\.md)"
)
NOT_REACHED = re.compile(
    r"not reached|blocked|not read\b|not searched|not located|catalogue[ -]only"
    r"|not digiti[sz]ed|not online|not downloaded|digitized-but-not-reached",
    re.I,
)
# Body lines scanned for the section's notes file (e.g. "From `notes/caldas.md`.").
BODY_LINES_SCANNED = 4


def index_repo_files():
    """Map each Markdown basename in the repo to its repository path(s)."""
    by_name = {}
    for top in ("strands", "access", "findings", "sources", "community"):
        for dirpath, _, files in os.walk(os.path.join(ROOT, top)):
            for f in files:
                rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                by_name.setdefault(f, []).append(rel)
    return by_name


def resolve(path, by_name):
    """Turn a path as the register cites it into a path in this repository."""
    path = path.rstrip(".,;:)_*`")
    if os.path.exists(os.path.join(ROOT, path)):
        return path
    base = os.path.basename(path)
    hits = by_name.get(base, [])
    if len(hits) == 1:
        return hits[0]
    if hits:
        return hits[0]
    return path + " (not in repo)"


def short_title(text):
    # Drop parentheses that hold a date or file paths (provenance, not topic).
    t = re.sub(r"\s*\((?=[^()]*(?:20\d\d|notes/|data/))[^()]*\)", "", text)
    t = t.strip(" .")
    if ": " in t and len(t.split(": ", 1)[0]) >= 15:
        t = t.split(": ", 1)[0]
    if len(t) > 110:
        t = t[:107].rsplit(" ", 1)[0] + " ..."
    return t.replace("|", "/")


def parse(lines, by_name):
    sections = []
    seen = {}
    cur = None
    for n, line in enumerate(lines, 1):
        m = HEADING.match(line)
        if m:
            text = m.group(2)
            idm = SECTION_ID.match(text)
            if not idm:
                continue
            sid = idm.group(1)
            rest = text[idm.end():].lstrip(". ")
            if len(m.group(1)) == 4 or "(continued)" in rest[:20]:
                sid = sid + " (cont.)"
                rest = re.sub(r"^\(continued\)\.?\s*", "", rest)
            seen[sid] = seen.get(sid, 0) + 1
            if seen[sid] > 1:
                sid = f"{sid} #{seen[sid]}"
            cur = {
                "id": sid,
                "line": n,
                "heading": rest,
                "body": [],
                "rows": 0,
                "rows_not_reached": 0,
            }
            sections.append(cur)
            continue
        if cur is None:
            continue
        s = line.strip()
        if s.startswith("|"):
            cells = s.strip("|").split("|")
            if all(re.fullmatch(r"\s*:?-{2,}:?\s*", c) for c in cells):
                cur["rows"] -= 1  # the line above was the header row
                if NOT_REACHED.search(cur.get("_last", "")):
                    cur["rows_not_reached"] -= 1
                continue
            cur["rows"] += 1
            if NOT_REACHED.search(s):
                cur["rows_not_reached"] += 1
            cur["_last"] = s
        elif s and len(cur["body"]) < BODY_LINES_SCANNED:
            cur["body"].append(s)

    out = []
    for sec in sections:
        cited = PATH.findall(sec["heading"])
        if not any(p.endswith(".md") for p in cited):
            for b in sec["body"]:
                cited += PATH.findall(b)
        notes, other = [], []
        for p in cited:
            r = resolve(p, by_name)
            bucket = notes if r.split(" ")[0].endswith(".md") else other
            if r not in bucket:
                bucket.append(r)
        strands = []
        for p in notes:
            parts = p.split("/")
            if parts[0] == "strands" and len(parts) > 2 and parts[1] not in strands:
                strands.append(parts[1])
            elif parts[0] == "access" and "access" not in strands:
                strands.append("access")
        d = DATE.search(sec["heading"])
        out.append({
            "id": sec["id"],
            "line": sec["line"],
            "title": short_title(sec["heading"]),
            "date": d.group(1) if d else "",
            "strand": "; ".join(strands),
            "notes_files": "; ".join(notes),
            "other_files": "; ".join(other),
            "rows": max(sec["rows"], 0),
            "rows_not_reached": max(sec["rows_not_reached"], 0),
        })
    return out


def next_free_b(rows):
    nums = [int(m.group(1)) for r in rows if (m := re.fullmatch(r"B(\d+)", r["id"]))]
    return f"B{max(nums) + 1}" if nums else "B1"


def main():
    with open(REGISTER, encoding="utf-8") as f:
        lines = f.read().splitlines()
    rows = parse(lines, index_repo_files())
    fields = ["id", "line", "title", "date", "strand", "notes_files",
              "other_files", "rows", "rows_not_reached"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    nb = next_free_b(rows)
    md = [
        "# Source register index",
        "",
        "Generated by `scripts/build_register_index.py` from "
        "[`register.md`](register.md); do not edit by hand. Regenerate with "
        "`python3 scripts/build_register_index.py` after changing the register. "
        "The same table is in [`register_index.csv`](register_index.csv).",
        "",
        "One line per register section. `Line` is where the section starts in "
        "`register.md`. `Not reached` is a rough keyword count of rows marked "
        "not reached, blocked, catalogue only and similar; read the rows "
        "before relying on it.",
        "",
        f"Sections: {len(rows)}. Table rows: {sum(r['rows'] for r in rows)}. "
        f"Next free section number: **{nb}**.",
        "",
        "| ID | Line | Title | Date | Strand | Notes file | Rows | Not reached |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        notes = ", ".join(f"`{p}`" for p in r["notes_files"].split("; ") if p)
        md.append(
            f"| {r['id']} | {r['line']} | {r['title']} | {r['date']} | "
            f"{r['strand']} | {notes} | {r['rows']} | {r['rows_not_reached']} |"
        )
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print(f"{len(rows)} sections written to {os.path.relpath(OUT_CSV, ROOT)} "
          f"and {os.path.relpath(OUT_MD, ROOT)}; next free {nb}", file=sys.stderr)


if __name__ == "__main__":
    main()
