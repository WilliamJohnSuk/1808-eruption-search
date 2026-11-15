---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: findings
date: undated
---

# Independent checks

Any source or finding in this repository can be checked again by anyone: a person, an AI system run by a person, or a mixed team. We want **several independent checks of every source**, and we record each one, including checks that disagree.

Each check is one row in [`checks.csv`](checks.csv):

| Column | What goes in it |
|---|---|
| `check_id` | `C` plus the next free number (C001, C002, ...) |
| `target` | What was checked: a finding (`F04`), a register row (`B53`), an unavailable source (`U151`) or a note path |
| `checked_by` | GitHub handle(s) of the person or people responsible |
| `team_type` | `human`, `ai` (an AI system run by the named person, output not checked by them against the source) or `human+ai` |
| `ai_systems` | Name and version of any AI system used, or `none` |
| `date` | YYYY-MM-DD |
| `source_reference_read` | Exactly what was read: archive, item, page or image, edition, URL |
| `verification_level_achieved` | `page-image`, `ocr`, `computed` or `inferred` |
| `result` | `confirms`, `partly confirms`, `contradicts`, `could not reach source` |
| `notes` | Short: what differed, a corrected reading, a better link |

How it feeds the findings table:
- `findings.csv` has three columns for this: `ai_generated` (who produced the row), `verified_by` (handles of the people whose `human` or `human+ai` checks confirmed it, or `none`) and `independent_checks` (the number of rows in `checks.csv` for that finding, whatever their result).
- A check by the same team that produced the item does not count as independent.
- An `ai`-only check is recorded and counted but does not make an item `human-verified`.
- A `contradicts` result is never deleted. The maintainer reviews it and either changes the finding's status or explains in the pull request why the finding stands.

To add a check without git, use the issue form [Re-check a source or finding](../../../issues/new?template=recheck-a-source-or-finding.yml).

## Corrections caught by human checks

These are errors in the AI-produced record that a person found by reading the source. Each is kept here, as well as being corrected where it occurred, because it shows what the human checks are for.

### 1. F15: a corona dated to the wrong day (found 15 Nov 2026, check C002)

- **What the AI record said.** Caldas's Bogotá weather table for February 1808 logged a thin veil with a solar corona ("S ve. cla. cor. S.") on **14 Feb 1808**. It cited this as *Semanario* núm. 7.
- **What the source says.** William John Suk read the table on the page image (JCB copy, archive.org `semanariodelnuev01unse`, PDF p. 105, printed p. 83). For day 14 he read "C. cal. nieb." and found the corona entry on the next line.
- **Why the AI got it wrong.** The "Estado del Cielo" (state of the sky) column is printed about half a row higher than the day numbers. The OCR text and the AI subagent that read it paired each sky entry with the row beside it, which put every entry one day early.
- **How it was settled.** The 29 sky entries were counted from the top (entry 1 = day 1) and from the bottom (entry 29 = day 29), on the image, by both William and Claude. Both counts put "S ve. cla. cor. S." on **15 Feb** and "C. cal. nieb." on 14 Feb. Veils ("ve.") appear on 9, 15 and 29 Feb; a corona with a veil only on 15 Feb.
- **A second slip found at the same time.** The February table is not in núm. 7 (14 Feb 1808), which holds only the definition of "velo" and the key to the codes. It is in **núm. 10 (6 Mar 1808)**.
- **Does it change the finding?** No. The point of F15 holds: "velo" was a routine category in Caldas's log and could carry a corona. The date and the citation were wrong and are corrected in `findings.csv`, the notes and the seed posts.
- **Lesson for checkers.** In printed tables, do not trust the alignment of a text column with the day numbers. Count the entries from both ends.
