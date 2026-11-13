# Governance

How decisions are made in this project. Short on purpose; it will change as the community grows, and changes to it go through a pull request like anything else.

## Roles

- **Maintainer:** William John Suk (<https://williamsuk.ai>; GitHub `WilliamJohnSuk`), who started the project. He merges pull requests, keeps the findings table, and settles disputes under the Code of Conduct. He may name further maintainers later; their names will be added here.
- **Contributors:** anyone who opens an issue, comments, votes or sends a pull request.
- **AI agents:** treated as tools of the person who runs them. Their work is labelled `ai-generated` and is not counted as human verification, even when it is right.

## What enters the evidence trail

| File | Who may change it | How |
|---|---|---|
| `findings/findings.csv` | Maintainer only | By pull-request review. Each new or changed row needs a source, a verification level and a notes file. |
| `findings/why_unidentified.md`, synthesis files | Maintainer | Pull request; review by the maintainer. |
| `sources/register.md`, `access/*.md` | Anyone | Pull request; rows are added or their status changed, never deleted. |
| `strands/**` notes | Anyone | Pull request; new notes carry the front-matter block. |
| `data/`, `scripts/` | Anyone | Pull request with the script that made the data. |
| `community/`, `.github/`, this file | Maintainer | Pull request. |

Code owners (`.github/CODEOWNERS`) make the maintainer's review required for `findings/`, `sources/` and the governance files.

## How votes are used

Discussions has upvotes and polls. They are **advice**:
- They set priorities: which source to chase, which candidate to test next, which open task to do first.
- They do **not** decide what is true. A finding enters `findings.csv` because of its source and verification level, not because it is popular. A low-voted objection that is right wins over a high-voted claim that is wrong.
- The maintainer will say in the thread when a vote has changed the project's plan.

## Verification levels

`page-image`, `ocr`, `computed`, `inferred`, as defined in CONTRIBUTING.md. Two rules:
1. A claim never moves up a level without someone reading the stronger evidence. Moving from `ocr` to `page-image` requires the image reference.
2. `human-verified` means a named person, not the AI that produced the item, has checked it against the source. It is recorded in the note's `verified-by` field and in `community/verification_overrides.csv`.

## Independent checks (many teams, one record)

We want each source and finding checked by several independent teams: people, AI systems run by people, or both. The schema:
- `findings/findings.csv` carries three provenance columns: `ai_generated` (who produced the row), `verified_by` (handles of people whose `human` or `human+ai` checks confirmed it; `none` until then) and `independent_checks` (how many checks of the row are recorded, whatever their result).
- `findings/checks.csv` holds one row per check: target, who, team type (`human`, `ai`, `human+ai`), AI systems used, date, exactly what was read, verification level achieved, result (`confirms`, `partly confirms`, `contradicts`, `could not reach source`). Rules in `findings/CHECKS_README.md`.
- Register rows and notes are checked the same way; the target column names the B-, U- or T-number or the note path. For notes, a confirmed human check is also recorded in `community/verification_overrides.csv`, which sets the note's `verified-by` field.
- A check by the team that produced the item is not independent. An `ai`-only check is counted but never makes an item `human-verified`. Contradicting checks are kept, never deleted.

## How results are phrased

- Negatives: "we found no report of ... in these sources", with the sources listed. Never "there was no ...".
- Dates computed by the project (calendar conversions, inferred eruption windows) are labelled as the project's calculation.
- Suggestions and interpretations are labelled as such.
- "Not found in literature reviewed" means only that; it is not a priority claim.

## Credit and publication

Credit is collective. Everything the project produces is credited to "the 1808/09 eruption collaboration" with every contributor listed in `CONTRIBUTORS.md`. If a peer-reviewed paper or dataset grows out of the work, the maintainer will invite those whose contributions shaped it to be co-authors or to be acknowledged, and will explain the choice in a Discussion before submission. AI systems are acknowledged as tools in the methods, not listed as authors.

## Disagreements

Argue about evidence in the open, in the issue or Discussion. If two readings of a source cannot be reconciled, both go into the notes with their verification levels. Conduct problems go to the contact route below, not into the thread.

## Contact

For Code of Conduct reports or anything that should not be public: email **widzodev@icloud.com** (read only by the maintainer).
