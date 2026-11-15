# Human/AI collab to identify the missing 1808/9 volcano

**A crowd-sourced research collaboration between people and AI systems, looking for the unidentified volcanic eruption of 1808/09.**

Some time around the end of 1808, a large volcanic eruption put about twice as much sulfur into the stratosphere as Pinatubo did in 1991. Its sulfate lies in the ice of both Greenland and Antarctica, it helped start the cold decade that Tambora finished in 1815, and nobody knows where it was. No eyewitness of the eruption itself has ever been found.

This repository is an open evidence trail for finding it. It holds what has been searched, what came up empty, the leads that might be worth a second look, and the data and scripts behind every calculation. Anyone can add a source, check a reading, argue for a candidate volcano or tell us we are wrong.

**This project claims no discovery.** Nothing here has been peer reviewed. Several of the leads will probably turn out to be weather, dust or coincidence.

## How the work is done

The project was started in October 2026 by [William John Suk](https://williamsuk.ai), an anthropologist with archival experience, working with Claude (an AI model made by Anthropic). Claude ran most of the searches, readings and calculations under William's direction. William chose the questions, obtained the documents that needed human hands, and decides what enters the findings table.

In the research files themselves, every AI-written note, finding and check is marked as AI-generated, and every claim carries a verification level (`page-image`, `ocr`, `computed` or `inferred`). Each source and finding can be re-checked independently by any number of human, AI or mixed teams, and every check is recorded. The rules are in [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Negative results are phrased "we found no report of ... in these sources", never "there was no ...".

## What is known so far

The detail is in [`findings/findings.csv`](findings/findings.csv) (one row per observation) and [`findings/why_unidentified.md`](findings/why_unidentified.md). In short:

- **When.** The first dated sighting of the veil is in Bogotá on 11 December 1808 (Caldas: a whitish sky and a silvery sun; `page-image`). Lima saw glowing evening skies from mid-December (Unanue; `ocr`), and Edo in Japan saw very red sunrises and sunsets from 9 January 1809 (`page-image`). Sulfate reaches the NEEM core in Greenland only around October 1809 (`computed`). Together these suggest an eruption between mid-November and early December 1808 (`inferred`).
- **Where, roughly.** The even fall of sulfate at both poles says "tropical" and little more. The volcanic glass found in the 1809 ice is an iron-rich island-arc andesite (published analyses). Compared with nearly 9,000 published analyses from the candidate arcs, it rules out low-potassium arcs such as Tonga but matches many others about equally well (`computed`).
- **Leading candidates** (none confirmed): Dakataua (New Britain, Papua New Guinea), Gaua (Vanuatu) and Cabalían (Leyte, Philippines), with Agung, Dukono, Todoko-Ranu, Teon, Nila and northern Sulawesi as possibles. Etna, Vesuvius, Hekla and Long Island are ruled out. See [`strands/candidates/`](strands/candidates/).
- **Where we looked and found nothing.** We found no report of the eruption in the Iberian, Latin American, Dutch, German and British newspapers we read; in about sixty European, American and missionary sources; in the East India Company, Royal Navy, Hudson's Bay Company and whaling logs we read; or in the Chinese, Korean, Ryukyuan, Vietnamese, Japanese and Dutch-Japanese (Deshima) records we read. Each search and its limits are in the strand notes.
- **What would settle it.** A trace-element analysis of the ice glass, a dated proximal ash layer near a candidate, or a ship's log or diary from the eastern islands for November-December 1808. See [`strands/method/evidence_that_would_settle_it_2026-11-02.md`](strands/method/evidence_that_would_settle_it_2026-11-02.md).

## How to help

You do not need to know git. Pick whichever path suits you.

**1. Report a source (no git needed).** Know of a diary, ship's log, missionary letter, chronicle, newspaper or core sample that covers late 1808 to 1810? Open a [**Report a source**](../../issues/new?template=report-a-source.yml) issue. A title and a link are enough; we will check it against the [source register](sources/register.md).

**2. Join the discussion and vote.** Every candidate volcano, contested reading and open question has a thread in [**Discussions**](../../discussions). Upvote the arguments you find strongest, answer the polls, and say what you would check next. Votes guide what we work on; they do not decide what counts as evidence (see [GOVERNANCE.md](GOVERNANCE.md)).

**3. Submit a finding or a correction.** If you have read a source, open a [**Submit a finding**](../../issues/new?template=submit-a-finding.yml) issue, or, if you use git, a pull request that adds a row to the register or the findings table. Say which verification level applies and how you read it.

Other ways in:
- [**Propose a candidate volcano**](../../issues/new?template=propose-a-candidate-volcano.yml) with the reason it fits.
- [**Request a document retrieval**](../../issues/new?template=request-a-document-retrieval.yml): many decisive records need someone at an archive or library. They are listed in [`access/unavailable_sources.md`](access/unavailable_sources.md) (U-numbers). If you live near one of them, you can help more than anyone.
- **Pick an open task** from [`access/open_tasks.md`](access/open_tasks.md) (T-numbers).
- **Languages.** We need readers of Dutch, Spanish, Portuguese, classical Chinese, Japanese (kanbun and sōrōbun), Vietnamese (chữ Hán), Malay/Jawi and Tok Pisin.

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Everyone taking part agrees to the [Code of Conduct](CODE_OF_CONDUCT.md).

## Credit

Credit is collective, in the spirit of the [Polymath Project](https://polymathprojects.org/): small contributions are as welcome as large ones, no part of the problem is "owned" by anyone, and anything that comes out of the project (a blog post, a paper, a dataset) is credited to the project, with every contributor listed in [CONTRIBUTORS.md](CONTRIBUTORS.md). AI contributions are credited as AI contributions, never as a person's. How authorship of any publication is handled is set out in [GOVERNANCE.md](GOVERNANCE.md).

## Layout

| Folder | Contents |
|---|---|
| `findings/` | `findings.csv` (one row per observation, with its verification level, status and provenance), `checks.csv` (independent re-checks), `why_unidentified.md`, `archive/` (superseded summaries) |
| `sources/` | `register.md`: every source consulted or identified, with its URL, coverage and whether it was reached; `scans/`: hosted page images of cited public-domain records |
| `strands/` | Working notes, one folder per region or source type: `colombia_caldas`, `peru_south`, `mexico_caribbean_spain`, `portuguese_world`, `asia_pacific_arabic`, `north_america`, `ship_logs`, `europe_press`, `science_alternatives`, `candidates`, `melanesia_oral`, `method` |
| `access/` | How to reach each archive and digitized newspaper, the sources that need human hands (`unavailable_sources.md`) and the open tasks (`open_tasks.md`) |
| `data/`, `figures/` | Derived tables, plots and maps (`data/cc-by-sa/` holds the share-alike tables) |
| `scripts/` | Analysis and download scripts |
| `community/` | Labels, the Discussions plan and the human-verification log |
| `.github/` | Issue forms, the pull-request template and code owners |

The notes keep their original round-by-round structure and repeat each other in places. Page images of public-domain records that the project cites are hosted in `sources/scans/` with their source and licence; anything we may not host is linked to the archive that holds it.

## Licences

Text, notes and derived tables: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Scripts: MIT. One exception: the share-alike tables in [`data/cc-by-sa/`](data/cc-by-sa/LICENSE.md) are CC BY-SA 4.0. See [LICENSE.md](LICENSE.md). Third-party datasets keep their own licences; cite the original datasets (CLIWOC 2.1, the oldweather/EEIC keyed logs, NEEM-2011-S1 (PANGAEA 940553), San Fernando (Zenodo 7104289), GEOROC, the Smithsonian Global Volcanism Program and the others named in each data note). By contributing you agree that your contribution is released under the same licences.

**Takedown.** We host historical material we believe is in the public domain or openly licensed, each item with its source and licence stated. If you hold rights in, or believe we should not host, any item here, email william@williamsuk.ai and it will be taken down promptly while we look into it.
