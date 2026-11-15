# AGENTS.md: a guide for AI agents

This file is for AI agents (Claude, Codex, Cursor, Copilot and others) that a person has pointed at this repository, and for the people who run them. It tells you what the project is, where things are, what to work on and the rules every contribution must follow. Where a rule is set out in full elsewhere, this file links to it: [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md) are the authority, and if this file ever disagrees with them, they win.

## What the project is, and is not

- **It is** an open evidence trail for identifying the unidentified volcanic eruption of about late 1808, whose sulfate is in both Greenland and Antarctic ice. It records what has been searched, what was found, what came up empty and the data and scripts behind every calculation. See [README.md](README.md) for the state of the evidence and [`findings/why_unidentified.md`](findings/why_unidentified.md) for why the eruption is still unknown.
- **It is not** a claim of discovery. Nothing here is peer reviewed, and no candidate volcano is confirmed. Do not write, in any file, issue or comment, that the eruption has been found or that a candidate is "the" source.
- It was started by William John Suk, working with Claude (Anthropic). Most existing notes were written by Claude under his direction and are labelled as AI-generated. William is the maintainer and decides what enters the findings table.

## The person behind the agent

**A person must stand behind every AI contribution.** AI agents are treated as tools of the person who runs them (GOVERNANCE.md, "Roles").
- Post only through an account whose human operator answers for what it posts. Do not post in bulk or open many issues or pull requests at once.
- Your operator is named in the `directed-by` field and on the issue or PR form. Do not leave it blank.
- AI work never counts as human verification, even when it is right. Only a person who has read the source can be named in `verified-by`.
- Do not contact archives, libraries, researchers or other people on the project's behalf. If a source needs a request or a letter, raise it in an issue or Discussion; whether and who writes is a project decision (GOVERNANCE.md, "Project decisions").

## Repository layout

| Path | What it holds | Notes for agents |
|---|---|---|
| [`findings/findings.csv`](findings/findings.csv) | One row per observation (F-numbers), with verification level, status and provenance | Maintainer-only. Propose rows in a PR or a [Submit a finding](../../issues/new?template=submit-a-finding.yml) issue. |
| [`findings/checks.csv`](findings/checks.csv), [`findings/CHECKS_README.md`](findings/CHECKS_README.md) | Independent re-checks (C-numbers) of findings, register rows and notes | Read CHECKS_README before adding a check. |
| [`sources/register.md`](sources/register.md) | Every source consulted or identified, in sections B1, B2, ... (about 400 KB) | **Start from [`sources/register_index.md`](sources/register_index.md)** (or the [CSV](sources/register_index.csv)): one line per section with its line number, strand and notes file. |
| [`access/open_tasks.md`](access/open_tasks.md) | Work offered but not done (T-numbers) and who has to do it | Next free number at the foot. |
| [`access/unavailable_sources.md`](access/unavailable_sources.md) | Sources that need human hands: offline, paywalled, captcha, archive visit (U-numbers) | Status vocabulary in the file header; next free number at the foot. |
| `access/` (other files) | How to reach each archive and digitised newspaper; catalogue sweeps | |
| `strands/<strand>/` | Working notes, one folder per region or source type, one dated file per strand | Each folder has a README. Notes repeat each other in places. |
| `data/`, `figures/` | Derived tables, plots and maps | `data/cc-by-sa/` is share-alike; see [`data/README.md`](data/README.md). |
| `scripts/` | Analysis and download scripts (plain Python 3) | Dated folders; each says what data it reads. |
| `community/` | Labels, Discussions plan, human-verification log (`verification_overrides.csv`) | Maintainer-only. |

Notes written before the repository was set up cite paths such as `notes/caldas.md` or `source_register.md`. These now live under `strands/<strand>/` and `sources/register.md`; the register index resolves them.

## Where to start

1. Read [README.md](README.md) (ten minutes), then [`strands/method/evidence_that_would_settle_it_2026-11-02.md`](strands/method/evidence_that_would_settle_it_2026-11-02.md) for what would actually help.
2. Pick one item and say you are taking it before you start, in its issue or a new one, so two agents do not do the same work:
   - **A free task.** Rows in [`access/open_tasks.md`](access/open_tasks.md) section 1 with status `open (free)` need no special access. Issues labelled `good-first-task` are small and self-contained. Rows marked `project decision` are settled in a Discussion or poll (GOVERNANCE.md, "Project decisions"): join it rather than acting alone. Only `maintainer` rows (merging, repository settings) are the maintainer's.
   - **A U-item your environment can reach.** Many rows in [`access/unavailable_sources.md`](access/unavailable_sources.md) are marked `needs Mac download` or `needs Safari or captcha` only because the project's own AI environment was blocked (HathiTrust, Gallica, Delpher, Google Books, the Hemeroteca Digital Brasileira and others). If you can read the source, read it, and report what you read with its exact reference. Do not get around captchas, paywalls or terms of use.
   - **A re-check.** Pick a finding or a register row and check it against the source. Independent checks are wanted for everything (see [`findings/CHECKS_README.md`](findings/CHECKS_README.md)), and the human checks so far have caught real errors in the AI-made record.
3. Before you add a source, search the register index and `access/unavailable_sources.md` for it. If it is already there, add what is new (a reading, a better link, a page image reference) rather than a second row.

The project's search window is September 1808 to mid-1810 for newspapers, and March 1808 to mid-1810 for logs and Asian sources, since news took months to reach print. Search terms by language are in [`strands/method/eruption_clue_search_terms.md`](strands/method/eruption_clue_search_terms.md).

## Hard rules

These come from CONTRIBUTING.md and GOVERNANCE.md. A contribution that breaks one will be sent back.

**Labelling and provenance**
- New Markdown notes start with the front-matter block in [CONTRIBUTING.md, "AI-generated work"](CONTRIBUTING.md#ai-generated-work): `ai-generated`, `author`, `model` (name and version), `directed-by` (your operator's handle), `verified-by: none`, `verification`, `strand`, `date`.
- Tick the AI box on issue forms, or use the `ai-generated` label, and name the system and version.

**Verification levels.** Every claim carries one, as defined in [CONTRIBUTING.md](CONTRIBUTING.md#verification-levels). If in doubt, choose the weaker.
- `page-image`: you read the words on an image of the original page, and you give the image reference. An AI model reading a page image counts, but the reading stays AI-generated until a person checks it.
- `ocr`: you read machine-transcribed text without checking the image.
- `computed`: you calculated it; point to the script and its input data.
- `inferred`: your interpretation; say what it rests on.
- An AI summary of a source you have not read is `inferred`. Never paste AI output about a document nobody has seen.
- Older notes use a shorter internal set ([page image], [text], [calc], [memory], [suggestion]); map them onto the four levels above when you cite them.

**How results are phrased** (GOVERNANCE.md, "How results are phrased")
- Negatives: "we found no report of ... in these sources", with the sources and what was read listed. Never "there was no ...", never "nobody saw it".
- Label your inferences and suggestions as such. Dates the project calculated (calendar conversions, inferred eruption windows) are labelled as the project's calculation.
- "Not found in the literature reviewed" means only that; it is not a priority claim.

**Language and worldview.** Be careful not to adopt a colonial worldview. Many of the sources here were written by colonial officials, missionaries and traders, and AI models tend to repeat their framing.
- Never refer to Indigenous people as "natives", "savages", "primitive", "tribesmen" or in any other derogatory way. The only exception is an exact quotation from a source, in quotation marks and attributed. Name people as they name themselves, or by place ("people of Tanna", "Tolai communities"), in your own words.
- Describe local and Indigenous people and their records neutrally. Oral histories, genealogies and local chronicles are sources, not "legends" or "folklore" to be ranked below colonial paperwork.
- Never describe a place as empty or devoid of observers, or use any wording that hides the people who lived there: "empty", "uninhabited", "remote", "isolated", "no witnesses", "no observers", "nobody saw it", "nobody was writing". Say instead what is true of the records: "we know of no written account from ... in 1808", "no record has been found in the sources searched". What is missing is a surviving record in the archives searched so far, which is a statement about the archives, not about the people. (Exact, attributed quotations from sources stay as written.)
- Do not treat a colonial post, mission or parish as the mark of where people or knowledge begin.
- See [`strands/method/language_corrections_log.md`](strands/method/language_corrections_log.md), which records this bias in the AI-drafted notes; watch for it in your own output, and fix it when you find it in existing notes (log the change there).

**Numbers and rows**
- Take the next free number: a new register section `B` (shown in [`sources/register_index.md`](sources/register_index.md)), `U` and `T` (at the foot of their files), `C` for checks. Numbers are never reused.
- Never delete a row. If a row is wrong, done or superseded, change its status and say why and when, so the trail stays complete.
- Other contributors may edit the same files; base your change on the current `main` and keep edits small.
- After changing `sources/register.md`, regenerate the index: `python3 scripts/build_register_index.py`, and commit both.

**Copyright**
- Do not add scans, PDFs or long quotations unless the holding archive's terms allow it. Link to the archive's page and give the item reference. Short quotations for verification and your own transcriptions of pre-1900 texts are fine.
- Hosting follows the licence audit, [`strands/method/hosting_licence_audit_2026-11-04.md`](strands/method/hosting_licence_audit_2026-11-04.md): host only what it marks HOST, with source and licence stated; everything else is link-only.
- Derived data names its source dataset and licence. Contributions are released under CC BY 4.0 (text, data) or MIT (code) ([LICENSE.md](LICENSE.md)).

**Privacy and conduct.** Do not put personal contact details in any file. Follow the [Code of Conduct](CODE_OF_CONDUCT.md). The public contact for the project is 1808@williamsuk.ai.

## How to submit

- **No git:** use an issue form: [Report a source](../../issues/new?template=report-a-source.yml), [Submit a finding](../../issues/new?template=submit-a-finding.yml), [Propose a candidate volcano](../../issues/new?template=propose-a-candidate-volcano.yml), [Re-check a source or finding](../../issues/new?template=recheck-a-source-or-finding.yml) or [Request a document retrieval](../../issues/new?template=request-a-document-retrieval.yml). Arguments and hunches go in [Discussions](../../discussions).
- **Git:** open a pull request from a branch and fill in the [pull-request template](.github/PULL_REQUEST_TEMPLATE.md) completely, including the AI-use section. One topic per pull request. Changes to `findings/`, `sources/` and the governance files need the maintainer's review.
- Put notes in the right `strands/<strand>/` folder, named `topic_YYYY-MM-DD.md`, and record the source in the register in the same pull request.
- Add your operator to [CONTRIBUTORS.md](CONTRIBUTORS.md) in their first pull request. AI systems are credited as tools, not as authors.

## Checklist before you submit

- [ ] I checked the register index and `access/unavailable_sources.md` for this source.
- [ ] Every claim has a verification level, and inferences are labelled.
- [ ] Negatives say "we found no report of ... in these sources" and list them.
- [ ] New notes have the front-matter block, with `directed-by` naming my operator.
- [ ] I used the next free number, and changed statuses instead of deleting rows.
- [ ] No scans, PDFs or long quotations the licence audit does not allow.
- [ ] Neutral language about local and Indigenous people: no "natives" or other derogatory terms outside exact, attributed quotations; no colonial framing.
- [ ] If I changed `sources/register.md`, I re-ran `scripts/build_register_index.py`.
