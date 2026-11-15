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

# What the public repo may host, and what it must only link (licence audit, 4 Nov 2026)

AI-generated (Claude, 4 Nov 2026, for the crowd-sourced GitHub redesign). Not legal advice. Every terms statement below carries a verification level:

- **read**: Claude read the portal's terms page today (quotes are from the page as fetched), or read the licence line inside the PDF on William's Mac.
- **inferred**: the page was blocked from Claude's cloud container and William's Mac shell has no network today, so the statement is from Claude's knowledge and **needs checking**. Each one that needs William's Safari is now in `unavailable_sources.md` (U179-U194).

Table: `data/hosting_licence_audit_2026-11-04.csv` (54 rows, one per source or per portal where the portal's terms govern; columns: id, source, holder/portal, where it is held, copyright of the underlying work, terms quote, URL, verification, decision, attribution line, notes).

Decisions used: **HOST** (may go in the repo now, with the attribution line), **HOST-AFTER-CHECK** (probably hostable, terms not yet read or item-level rights unread), **LINK-ONLY** (never put the file in the repo; link it), **TRANSCRIBE-ONLY** (images may not be published; our transcription may).

Count: HOST 12, HOST-AFTER-CHECK 22, LINK-ONLY 17, TRANSCRIBE-ONLY 3.

_Update 14 Nov 2026: BANREP moved from HOST-AFTER-CHECK to HOST. William read the item page for Semanario id 1606 in Safari: "Derechos de autor: Dominio público" (U181 closed). Counts now HOST 13, HOST-AFTER-CHECK 21._

## 1. The rule of thumb, now checked

Host what we made; link to what others scanned; transcribe what we cannot host. Three findings sharpen it:

1. **Non-commercial terms conflict with the repo's CC BY 4.0.** CC BY allows commercial reuse, so a file under a non-commercial licence (Gallica, the HAL copy of Faral 2022 under CC BY-NC 4.0 [read, licence line in PDF], probably HNDM) cannot sit in the repo as if it were CC BY. Either link it, or keep it in a separately labelled folder. Recommendation: link.
2. **Google-digitised public-domain scans** (most of our archive.org books: Plakaatboek, Bleeker, Parkinson, Chladni, Roche, Correio Braziliense) carry Google's front page: "we request that you use these files for personal, non-commercial purposes" and "Maintain attribution ... Please do not remove it" [read, OCR of the Correio Braziliense djvu text on the Mac]. The works are public domain and this is a request, not a licence, but to stay clean: host only the cited page crops, labelled "public domain, scan by Google via Internet Archive" (not CC BY), and link full volumes.
3. **Archive images and archive texts are treated differently.** TNA says so in terms [read]: Discovery images are for "private study or research for a non-commercial purpose", "Publication of images of the documents themselves falls within the scope of Tradable Information", but "written content from a Crown copyright public record may be published by transcription, without charge". FamilySearch is stricter [read]: "You may not post content from this site on another website or on a computer network without our permission." Our counts, dates and transcriptions from these records are our own data and may be hosted.

## 2. Terms read today (from Claude's cloud container)

| Portal | Key clause | Decision |
|---|---|---|
| TNA Kew | images: non-commercial private research only; transcription free (quotes above) | TRANSCRIBE-ONLY |
| FamilySearch | no posting elsewhere without permission; personal, noncommercial use only | LINK-ONLY (images); counts and notes HOST |
| PANGAEA | "published Open Access, preferably under a CC-BY license"; must cite authors | HOST (confirm per dataset, T36) |
| BOE (Gazeta histórica) | commercial and non-commercial reuse allowed; cite "Fuente de los datos: Agencia Estatal Boletín Oficial del Estado" with a link | HOST |
| Copernicus journals | "distributed under the Creative Commons Attribution 4.0 License" | HOST |
| whalinghistory.org | databases "licensed under a Creative Commons Attribution 4.0 International License" | HOST |
| Library of Congress | "we generally do not own the rights"; user must judge copyright | HOST (PD items, with credit) |
| Internet Archive | "does not make guarantees as to the copyright status of items"; rights per item page | HOST-AFTER-CHECK (read item rights) |
| HathiTrust | "Allowable uses for each item are documented via the Access and Use policy linked to from the item" | LINK-ONLY |
| Zenodo | no default licence; "Users ... shall respect applicable license conditions" | HOST-AFTER-CHECK (record licence) |

Licence lines read inside William's PDFs: Plunkett 2023 QSR and Nardin 2020 Geosciences are CC BY 4.0 (may be hosted); Faral 2022 (HAL) CC BY-NC 4.0; Cole-Dai 2009 and Kurbatov 2006 "Copyright ... American Geophysical Union"; Stothers 2005 "All rights reserved"; Hirano 2018, Kohno 1996, Kawano/Kohno 1999, Tsuji 2025, Wichmann 1918 translation (GSL SP441) and Wohlt 1978 show no licence, so they are treated as in copyright.

## 3. Terms not reachable today (inferred, needs check)

Blocked from Claude's cloud container (403 or client error) and not reachable from the Mac shell: Nationaal Archief, GEOROC/GRO.data, GVP/Smithsonian, NOAA NCEI policy text, Trove (bot wall), Gallica, BNE, Delpher, Deutsches Zeitungsportal, ANNO, BVD, QDL, HNDM, BanRep, Kagoshima, Wellcome, HBCA. My expectations, all **inferred**:

- Probably hostable once confirmed: Nationaal Archief scans (public-domain records released without restriction), QDL India Office folios (usage line often OGL or public domain), BNE/Hemeroteca (free reuse of public-domain digitisations with credit), Delpher, Trove, Papers Past, Kagoshima (if CC BY), NOAA NCEI files (US federal or CC BY).
- Probably LINK-ONLY: Gallica (non-commercial), BVD/Museo Naval (publication needs the archive's permission), HBCA (permission to publish images; transcribe instead), HNDM (if non-commercial).
- Data with conditions: GVP (citation required; Smithsonian terms may be non-commercial), GEOROC precompiled files (I believe CC BY-SA 4.0).

Hand items added: U179-U188 and U190-U194 (needs Safari or captcha: export each terms page as PDF into a new `archives/_terms/` folder), U189 (HBCA permission, requires online request, only if William wants HBCA images).

## 4. The Gill CC BY-SA share-alike question

Register B50 records Gill's EarthChem Library files 1499, 1502, 1503 as CC BY-SA [inferred from register; landing pages not re-read, U194]. `data/gill_ecl_wholerock_scored_2026-10-26.csv` reproduces Gill's values row by row with our scores added, which makes it an adaptation. Under CC BY-SA 4.0 an adaptation must be shared under CC BY-SA (or a compatible licence), so this one file cannot be released under the repo's CC BY 4.0.

Two clean options (William's choice, T37):
- (a) Put it, and any GEOROC row-level table if U192 confirms CC BY-SA, in `data/third_party_share_alike/` with its own LICENSE note (CC BY-SA 4.0, credit to Gill/EarthChem and GEOROC) and a line in README. Everything else stays CC BY.
- (b) Drop the row-level tables and publish only per-volcano summaries (counts, medians, best match) plus the script that rebuilds the full table from the downloaded files. My recommendation, because it also avoids a 1.7 MB copy of GEOROC.

Notes that quote a few of Gill's numbers or conclusions are not adaptations of the database and stay CC BY.

## 5. Must never go in the repo

Paywalled or all-rights-reserved papers in `papers/`: Cole-Dai 2009 (AGU), Kurbatov 2006 (AGU), Stothers 2005 (ASP), Hirano 2018, Kohno 1996, Kawano/Kohno 1999, Tsuji 2025 (no licence: link the free PDF), Wichmann 1918 English translation (GSL), Wohlt 1978 thesis, and Faral 2022 (CC BY-NC). The Blong 1982 page screenshots (141 pages from an Internet Archive lending copy of an in-copyright book) must never be hosted; only short quotations. Also never: any FamilySearch image or image list, TNA page-check images, BVD images until permission, the cookie jar `newspapers/script_downloads/.cookies.txt`, and any FS_SESSION value.

## 6. What the public repo must strip or change before a first push

Checked against the repo copy `1808-eruption-repo/` on 4 Nov 2026. It holds **no third-party scans or PDFs** (its only images are our own plots and the fleet map), so the strip list is short:

1. **Remove** `scripts/fs_film_fetch.py`, `scripts/fs_diag.py`, `scripts/fs_diag2.py` from the sync to the repo copy (a FamilySearch bulk fetcher using a signed-in token; publishing it invites terms breaches). Keep them on the Mac.
2. **Move or reduce** `data/gill_ecl_wholerock_scored_2026-10-26.csv` (share-alike, section 4); same for `data/georoc_scored_2026-10-26.csv` if U192 confirms CC BY-SA.
3. **Check, then keep or reduce** `data/gvp_tropical_candidates_1808.csv` (U193).
4. **Add a provenance and licence line** per data file (this audit's CSV feeds T31's `data/README.md`); NEEM, Recife, eVolv2k, whaling are confirmed CC BY 4.0.
5. **Scan notes** for long verbatim passages from modern copyrighted works (Blong, Wohlt, paywalled papers) and cut them to short quotations (T35).
6. **Check** `scripts/fetch_newspapers.py` and other fetch scripts for hard-coded cookies or bot-wall workarounds before push.
7. If William later wants scans in the repo: create a `sources/scans/` folder holding only cited pages from HOST rows, each with its attribution line and "public domain, not covered by the repo's CC BY", never full volumes.

## 6a. William's decisions, 4 Nov 2026 (T37 answered)

- **Share-alike data:** option (a). The Gill-derived table now lives in `data/cc-by-sa/` with its own CC BY-SA 4.0 `LICENSE.md`; the root `LICENSE.md` and README name the exception. GEOROC-derived tables stay in `data/` under CC BY 4.0 (GEOROC is CC BY; U192 confirms the item-level licence).
- **Hudson's Bay Company Archives (row HBCA):** HOST, at William's decision ("let them ask me to take it down"). Cited pages go in `sources/scans/hbca/` with the attribution line; take down on request.
- **Other cited public-domain scans:** host with the source and licence stated and a takedown note, where the audit says HOST or HOST-AFTER-CHECK; LINK-ONLY rows and section 5 stay out. Per-portal confirmation is task T40.
- **Takedown note** (in README, LICENSE.md and `sources/scans/README.md`): "If you hold rights in, or believe we should not host, any item here, email widzodev@icloud.com and it will be taken down promptly while we look into it."
- **Strip list done 4 Nov:** the FamilySearch scripts are out of the repo copy and out of `sync_repo_copy.sh`; no paywalled papers, Blong screenshots or FamilySearch images are in the repo copy (checked: its only images are our own plots and maps).

## 7. Follow-ups

Written into `access/open_tasks.md`: T35 (scan notes for long modern quotations), T36 (confirm item-level licences for NOAA, PANGAEA, Zenodo and archive.org files we would host), T37 (decision: share-alike option a or b; host cited PD scans at launch or link only; seek HBCA/BVD permission or not), T38 (apply the audit to the sync script and repo copy after T37), T39 (William's Safari batch of terms pages U179-U194).
