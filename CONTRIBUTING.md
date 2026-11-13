# Contributing

Thank you for helping look for the 1808/09 volcano. Historians, archivists, volcanologists, ice-core and coral scientists, sailors, genealogists, translators and curious readers are all useful here, and so are AI agents run by people who stand behind them.

## The short version
1. **Check the register first.** Search [`sources/register.md`](sources/register.md) and [`access/unavailable_sources.md`](access/unavailable_sources.md) for your source. If it is there, say what you can add (a reading, a page image, a better link).
2. **Open an issue** with one of the forms. No git is needed, and a link plus one sentence is a fine start.
3. **Label what you did.** Say how you read the source (verification level) and whether an AI tool wrote any of your text.
4. **Phrase negatives carefully.** "We found no report of ash in the *Gazeta de Lisboa*, Nov 1808 to Mar 1809 (issues read: ...)", never "there was no ash".

## Ways to contribute

| You have | Do this |
|---|---|
| A source nobody has listed | [Report a source](../../issues/new?template=report-a-source.yml) |
| A reading of a source (a quotation, a date, a null result) | [Submit a finding](../../issues/new?template=submit-a-finding.yml), or a pull request (below) |
| A volcano you think fits | [Propose a candidate volcano](../../issues/new?template=propose-a-candidate-volcano.yml) |
| Access to an archive, library or dataset we cannot reach | Take a U-number from `access/unavailable_sources.md` and [request or offer a retrieval](../../issues/new?template=request-a-document-retrieval.yml) |
| Time to check something we already have | [Re-check a source or finding](../../issues/new?template=recheck-a-source-or-finding.yml): independent checks by people, AI systems or mixed teams are all recorded |
| An opinion, an objection, a hunch | Post in [Discussions](../../discussions) and vote |
| An afternoon and an internet connection | Pick a free task from `access/open_tasks.md` |

## Verification levels

Every claim you add needs one of these. If in doubt, choose the weaker one.

| Level | Use it when |
|---|---|
| `page-image` | You read the words on an image of the original page or manuscript. Give the image reference (archive, item, image or page number). |
| `ocr` | You read machine-transcribed text and have not checked the image. |
| `computed` | You calculated it. Include or point to the script and the input data. |
| `inferred` | It is your interpretation. Say what it rests on. |

A transcription you made yourself from a page image is `page-image`. A transcription someone else made is `ocr` (or `page-image` if you checked it against the image).

## AI-generated work

AI help is welcome and must be visible.
- If an AI system wrote or substantially drafted your issue, comment, note or pull request, tick the AI box on the form (or add the `ai-generated` label) and name the system and version if you know it.
- New Markdown notes start with the front-matter block below. `verified-by` stays `none` until a person other than the AI has checked the content against the source; then it names that person (their GitHub handle).

```yaml
---
ai-generated: true            # false if a person wrote it unaided
author: Claude (Anthropic AI model)   # or your name / handle
model: name-and-version        # the AI model and version, if AI
directed-by: your-handle       # the person who ran the AI
verified-by: none              # or the handle of the person who checked it
verification: mixed (see the label on each item)
strand: candidates
date: 2026-11-04
---
```

- An AI agent may open issues and pull requests only through an account whose human operator answers for it. Do not run agents that post in bulk.
- Do not paste AI output about a historical document you have not seen. An AI summary of a source counts as `inferred` until someone has read the source.

The existing notes were all written by Claude under William's direction; the script `scripts/add_frontmatter.py` stamps them. When you check one, record it in [`community/verification_overrides.csv`](community/verification_overrides.csv) (path, your handle, the level you confirmed, a one-line note) in the same pull request.

## Pull requests (for git users)

- Add rows; do not delete them. If a row is wrong, change its status and say why, so the trail stays complete.
- Source register: add a new row with the next free number shown at the foot of the section. Unavailable sources: next free U-number. Open tasks: next free T-number.
- Findings: propose rows for `findings/findings.csv` in a pull request; the maintainer reviews every change there (see [GOVERNANCE.md](GOVERNANCE.md)).
- Notes go in the right `strands/<region>/` folder, one file per strand, named with a date (`topic_YYYY-MM-DD.md`).
- Scripts: plain Python 3 with few dependencies; put the date in the folder name and say what data they read.
- Fill in the pull-request template.

## Documents and copyright

We host what we made and link to what others scanned.
- **Do not upload scans or PDFs** unless the holding archive's terms allow redistribution. Many do not (FamilySearch, purchased record copies, most paywalled papers). When unsure, link to the archive's own page and give the item reference.
- Short quotations for verification are fine. Your own transcription of a pre-1900 text is fine.
- Data derived from other datasets must name the source dataset and its licence. Share-alike data (CC BY-SA) is flagged in the data notes.

## Licence of contributions

By submitting a contribution you agree that it is released under CC BY 4.0 (text, notes, data) or MIT (code), as described in [LICENSE.md](LICENSE.md), and that you have the right to release it.

## Credit

Add yourself to [CONTRIBUTORS.md](CONTRIBUTORS.md) in your first pull request, or ask in your issue and we will add you. Credit is collective; see the README.
