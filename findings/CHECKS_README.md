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
