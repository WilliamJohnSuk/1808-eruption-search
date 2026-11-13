---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: method
date: 2026-11-04
---

# Findings table checked against its notes (release gap 3, task T42), 4 Nov 2026

Checked by Claude (AI) on 4 Nov 2026; this is a consistency check of the table against the project's own notes, **not** a human check against the sources. Every row stays `verified_by: none`.

**Method.** For each row F01-F36 of `findings/findings.csv`: (1) the notes file named in `notes_file` exists; (2) the distinctive names, numbers and page references in the `observation` and `source` columns occur in that notes file [computed, script in this note's history: a token match]; (3) rows whose verification level is OCR or computed say so; (4) the misses were read by hand.

**Results**
- All 36 notes files exist at the paths given.
- No row claims a higher verification level than its notes support. OCR-only rows (F02, F03, F05, F10, F13, F16, F36) are labelled OCR in the table.
- **F13 corrected.** The Raffles quotation is cited from Lady Raffles's *Memoir* (1830) p. 244, but the notes (`strands/asia_pacific_arabic/indonesia_pass2.md` lines 44-52) trace an earlier printing in Raffles's *History of Java* vol. 1 (1817), leaf 85 of the Wellcome copy ("Karang Asam"). The source column now names both; still OCR only.
- **F34 corrected.** Its `notes_file` pointed to the glass compilation of 26 Oct; the Vanuatu and Solomons per-volcano scores are in `strands/method/free_checks_T5-T10_2026-11-02.md`. Path changed.
- **F24.** The table spells the paper "Bataviaasch Vendu-Nieuws"; the notes spell it "Bataviaas Vendu-Nieuws" as printed. Not changed: both forms are in use.
- **F36.** The Connecticut Evangelical Magazine page numbers (pp. 278-279) are in `strands/method/script_downloads_read_2026-10-27.md`, not in the Tonga note named; reader should look in both.
- Other misses were wording only (paraphrase in the table, same facts in the note).

**Still to do (needs a person).** A human check of each row against its source, recorded in `findings/checks.csv`. Highest value first: F01, F04, F09, F15, F17 (page-image rows a reader can recheck from public scans), then the OCR rows F02 and F13.
