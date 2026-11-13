---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: europe_press
date: undated
---

# Newspapers 1809 (US / Italian / Spanish on Internet Archive) — round 2

Strand: newspapers_1809. Worker draft, 16 Oct 2026. Written incrementally.

**Verification level for everything below:** OCR text obtained through WebFetch (IA fts snippets, `_djvu.txt` files, `fulltext/inside.php`). **No page images viewed.** Quotes are OCR, garbled where marked; long s appears as "f" in Newport Mercury and Kentucky Gazette OCR.

## 0. Corpus actually searchable on IA

IA advancedsearch `collection:newspapers AND date:[1808-12-01 TO 1809-12-31] AND NOT identifier:ddd*` → 714 items:
- *Alexandria Daily Gazette, Commercial & Political* (Alexandria, VA; daily port paper with Baltimore/Norfolk/NY ship news), ~326 issues
- *Diario de Mallorca* (Palma), ~213 issues
- *Pittsburgh Weekly Gazette*, ~56 issues
- *Newport Mercury* (RI port), ~54 issues
- *Kentucky Gazette* (Lexington; ExploreUK `xt…` identifiers), ~60 issues
- *Giornale del Campidoglio* (Rome, monthly volumes), *Corriere delle Dame* (Milan), 1 misc.

**No Salem, Boston, New York, Philadelphia, Baltimore, Charleston or Savannah papers for the window are in this IA collection.** So printed weather registers of Salem/Philadelphia/Charleston cannot be checked here.

Tool behaviour noted: multi-word queries (`smoke sun`, `atmosphere sun`, `"sun appeared"`, `"dark day"`, `"Indian summer"`) return 0 even when the single words hit — the fts appears to treat them as adjacent phrases or fails; single words work. `"shower of ashes"` URL rejected as too long. inside.php URLs for Alexandria items exceed the WebFetch URL length limit; the `_djvu.txt` URL works. IA returned HTTP 429 after ~20 calls in this session (shared budget).

## 1. Findings (event date ≠ paper date)

| # | Paper (IA id) | Paper date | Dateline / event date | OCR excerpt (verbatim fragments) | Assessment |
|---|---|---|---|---|---|
| F1 | Alexandria Daily Gazette `…_1809-02-25_9_2420`; Kentucky Gazette `xt7h9w08x041` (1809-03-21) | 25 Feb 1809; 21 Mar 1809 | Azores (São Jorge), eruption May 1808; letter of J. B. Dabney | "NEW VOLCANO. A letter from J. B. Dabney…"; "the large volcano that had lain dormant for nine days burst forth"; "small pumice stones, that a strong N.E. wind…" | **Known São Jorge 1808 reprint; not chased.** Shows the US reprint lag (~9 months after event). |
| F2 | Pittsburgh Weekly Gazette `…_1809-05-31`; Kentucky Gazette `xt7dfn10pp4m` (1809-06-06) | 31 May 1809; 6 Jun 1809 | "From Providence (R.I.) May 13"; event Cumberland RI "about the beginning of March" 1809, recurring every few days | "In the north part of Cumberland, in this state, near the Atticborough line… about the beginning of March, in the night, the ground for the space of two or three acres began shaking, and continued two or three minutes… there appeared many indications of an earth quake… the next day about 2 in afternoon, the same quivering of the earth was observed. Since every few days, the earth shakes…" (OCR lightly normalised; original garbled e.g. "degan shs aking", "pwo or three") | Local ground tremor/frost-heave-type phenomenon in New England; **not volcanic, no relevance to a tropical eruption.** |
| F3 | Pittsburgh Weekly Gazette `…_1809-03-01` | 1 Mar 1809 | "Portsmouth (N.H.) Feb. 7" — January 1809 | "For ten years, we have not experienced so long a series of uninterrupted cold." / "During the month of January, the Thermometer never rose so high [as 34?] degrees at sunrise, but once." / "So far the winter has passed without a thaw, which is extraordinary." / "it snowed eight times, and the wind was N. W. 25 days during the month of January." | **Climatic**: very cold, thaw-less Jan 1809 at Portsmouth NH (a sunrise-temperature register). No sky/haze remark. Cold NE US winter 1808/09 is consistent with, but not diagnostic of, a volcanic forcing. Constraint: none on timing. |
| F4 | Alexandria Daily Gazette `…_1809-05-18_9_2491` (+ Pittsburgh 31 May, Kentucky 6 Jun reprints) | 18 May 1809 | Ship **Monticello, from Lima**, bound for Philadelphia, fell in with wreck (Acorn) and rescued survivor Moorhead | "We stated in a former paper, that the ship Monticello, from Lima, fell in with the wreck of a vessel at sea" / "When the captain of the Monticello took [him on board]… for Philadelphia" | **Lead, not a finding**: a ship that left Lima probably ~Jan–Feb 1809 (Unanue's afterglow period) and reached Philadelphia ~Apr–May 1809. Its arrival notice/letters would be in Philadelphia papers (Poulson's American Daily Advertiser, Relf's Philadelphia Gazette, Aurora) — not on IA. Nothing about weather/sky in the Alexandria OCR. |
| F5 | Pittsburgh Weekly Gazette `…_1809-11-08` | 8 Nov 1809 | Etna eruption (Mar–Apr 1809) | "ERUPTION OF MOUNT ÆTNA"; "the whole of the lava downwards appeared red and the eruption appeared to double advantage" | Known Etna 1809 eruption; Mediterranean, not candidate. |
| F6 | Alexandria Daily Gazette `…_1809-09-08_9_2590` | 8 Sep 1809 | Baltimore Sept 5 ship news: Carthagena "5th ultimo" (5 Aug 1809) | "Left at Carthagena, 5th ultimo, schooner William and Eliza, for N. York… the only American vessel there, the port shut against neutrals." ("most total darkness; rains and peals of thunder" in the same issue = theatre playbill, not weather) | Explains the scarcity of Cartagena ship news in 1809: port closed to neutrals. |

## 1a. Negative / noise results (IA fts, newspapers, 1808–1809)
See search log. No ship report found mentioning ashes on deck, pumice at sea (other than Azores reprint), a South American/Caribbean/Pacific volcano, a red/pale sun, haze, dry fog or "smoky" weather in Dec 1808 – Mar 1809.


## 1b. Savannah — *The Republican; and Savannah Evening Ledger* (Georgia Historic Newspapers, free)

A free, OCR-searchable US **port** paper that covers the window. It is not on IA. LCCN sn82014388; title page: https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388 (issues 1807-03-10 to 1816-03-02).
- **Gap: there are no issues between 4 Oct 1808 and 3 Jan 1809.** After that, issues run about three a week: 10 in Jan 1809, 12 in Feb, 6 in Mar, 7 in Apr. Example issue URL: https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1809-01-03/ed-1#issue
- **Search method that works:** `https://gahistoricnewspapers.galileo.usg.edu/search/pages/results/?lccn=sn82014388&andtext=WORD+WORD&rows=100`. `ortext=` also works, and the `#words=` fragment on each result shows which OCR word matched. **The date filter is ignored** (both `date1/date2` with `dateFilterType=yearRange` and the `range` form), so 1809 hits have to be picked out by hand. The `ocr.txt` and `ocr.xml` files are blocked by robots, and the IIIF JPG came back with a server error. So **only page-level hits are available here, with no text.**
- Page-level hits, Dec 1808 – Dec 1809 (term located, **text not read**):
  - "earthquake": **10 Jun 1809, p. 3**; 28 Oct 1809, p. 2. Outside the window: 13 Jan 1810, p. 2; 29 Mar 1810, p. 3.
  - "ashes": 10 Jun 1809 p.3; 2 May 1809 p.1; 9 May 1809 p.1; 5 Dec 1809 p.2. Pages 1–2 are probably pot/pearl-ash adverts.
  - **10 Jun 1809, p. 3 has "earthquake", "ashes", "Ash", "city" and "Hazes" on the same page.** It does not match "volcano", "lava", "Etna", "mountain", "Lisbon" or "Cumberland". So it is not the Etna, Azores or Cumberland RI story, as far as OCR shows. **Unidentified. A human should read it:** https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1809-06-10/ed-1/seq-3/
  - "etna": 14 Feb 1809, p. 3 (https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1809-02-14/ed-1/seq-3/). Could be a ship's name; the Etna eruption began only in Mar 1809.
  - "Hazy": 11 Apr 1809, p. 2 (https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1809-04-11/ed-1/seq-2/). Probably the London telegraph/"hazy weather" item also found in Alexandria on 12 Apr (see search log).
  - "smoky": 30 Sep 1809, p. 2. "Phenomenon": 5 Sep 1809, p. 3 and 19 Dec 1809, p. 2. "Pumice": 29 Apr 1809, p. 1 and 12 Sep 1809, p. 1 (front page, probably adverts).
  - "volcano": no hits in 1809. The hits are in 1808-09-15 (probably the Azores), 1810 and 1812.

## 2. Assessment

- **No positive evidence** turned up in this corpus for (a) ships reporting ash on deck, pumice at sea, darkness, or a red or pale sun from South America, the Caribbean, the Pacific, the Indian Ocean or Africa in Dec 1808 – Dec 1809, or (b) local US or Italian/Spanish reports of haze, dry fog, a red sun or odd twilights in Dec 1808 – Mar 1809.
- The weather signal that does show up is **cold**: Portsmouth NH reported January 1809 as the most uninterrupted cold in 10 years, with no thaw (F3). This is consistent with, but not diagnostic of, a volcanic winter.
- Volcanic news printed in the US in 1809 is limited to known events: the São Jorge (Azores) eruption of May 1808, reprinted in Feb–Mar 1809, and Etna in Mar–Apr 1809, reprinted by Nov 1809.
- **Why the absence is weak evidence:** (1) the IA corpus has no Salem, Boston, New York, Philadelphia, Baltimore or Charleston papers, the ports where Pacific, Chilean, Peruvian and Indian Ocean ships arrived; (2) fts recall is low and phrase queries fail; (3) the 1807–09 Embargo cut US foreign shipping until 15 Mar 1809, so few ships arrived from the far south in Dec 1808 – Mar 1809; (4) Cartagena was closed to neutrals in 1809 (F6).
- **Best concrete follow-up:** the arrival of the ship *Monticello* from Lima at Philadelphia, about late April or early May 1809 (F4). She sailed from Lima during Unanue's afterglow months. Check Philadelphia papers (*Poulson's American Daily Advertiser*, *Relf's Philadelphia Gazette*, *Aurora General Advertiser*) for her arrival notice and "news from Lima", using Readex America's Historical Newspapers or GenealogyBank. Also check New York papers (*Mercantile Advertiser*, *New-York Gazette*) and Salem papers (*Salem Gazette*, *Essex Register*) for China and Pacific arrivals in Feb–Jun 1809. Those ships passed the Sunda Strait or Cape Horn about Dec 1808 – Feb 1809, and their arrival reports sometimes printed log extracts.

## 3. Search log

| # | Repository / tool | Query / filter | Coverage | Result |
|---|---|---|---|---|
| 1 | IA fts | `ashes deck`, 1808–09, newspapers | IA newspapers | 11 hits, all pot/pearl ashes trade or unrelated "deck". Nothing |
| 2 | IA fts | `"shower of ashes"` | — | URL rejected as too long |
| 3 | IA fts | `pumice` | 1808–09 newspapers | 4 hits. Alexandria 25 Feb 1809 = Azores reprint (F1); the rest are recipes or adverts |
| 4 | IA fts | `volcano` | " | 7 hits. Azores "NEW VOLCANO" (Alexandria 25 Feb, Kentucky 21 Mar 1809); the rest are metaphors or a racehorse |
| 5 | IA fts | `eruption` | " | 5 hits. Etna (Pittsburgh 8 Nov 1809, F5); the rest medical or metaphor |
| 6 | IA fts | `earthquake`, `earthquakes` | " | 5 + 1 hits. Cumberland RI (Kentucky 6 Jun 1809 = F2); Barbary coast quake (Alexandria 7 Mar 1808); the rest metaphor |
| 7 | IA fts | `haze` | " | 100 hits, all Dutch (place name "Haagsche"/"'s-Hage") — useless |
| 8 | IA fts | `hazy` | " | 3 hits. Alexandria 12 Apr 1809 ("Hazy weather rendering the…", London/Lloyd's column; checked in djvu.txt, not a sky report); Kentucky poem |
| 9 | IA fts | `smoky`, `"Indian summer"`, `"dark day"`, `"atmosphere sun"`, `"smoke sun"`, `"sun appeared"` | " | 0 hits each (multi-word queries fail) |
| 10 | IA fts | `atmosphere` | " | 12 hits. Barometric essays, metaphors, a fire account; none Dec 1808 – Mar 1809 about the sky |
| 11 | IA fts | `phenomenon` | " | 10 hits. Pittsburgh 31 May 1809 "NATURAL PHENOMENON" = Cumberland RI (F2, read in djvu.txt); Pittsburgh 23 Aug 1809 = Scottish item; Newport 11 Nov 1809 = meteor |
| 12 | IA fts | `darkness` | " | 37 hits. 3× Sep 1809 Alexandria "most total darkness" = theatre playbill (checked); the rest metaphor or night |
| 13 | IA fts | `Carthagena` | " | 45 hits (16 relevant). Prisoners from Miranda's expedition; trade; port shut to neutrals (F6). No natural events |
| 14 | IA fts | `Guira` | " | 9 hits. Political news only |
| 15 | IA fts | `Lima` | " | 59 hits. Ship *Monticello* from Lima (F4); Spanish political items; Lima beans |
| 16 | IA fts | `Monticello` (1809) | " | 3 relevant (wreck rescue) |
| 17 | IA fts | `Valparaiso`, `Guayaquil` | " | 0 |
| 18 | IA fts | `Caraccas` | " | 11 hits. Cocoa prices and politics |
| 19 | IA fts | `Janeiro` (1809) | " | 25 hits. Trade, politics, voyages; no natural events |
| 20 | IA fts | `Pacific` (1809) | " | 73 hits. Dispatch ship *Pacific*, Lewis & Clark book adverts, "pacific" in politics. Nothing |
| 21 | IA fts | `thermometer` | " | 57 hits. Pittsburgh glassware adverts; **Portsmouth NH Jan 1809 cold (F3)** |
| 22 | IA fts | `volcanic`, `meteor`, `fog` | " | 1 / 10 / 247 hits. Weston/Connecticut meteorite, Scottish fireball; battle or harbour fog only |
| 23 | IA fts | `volcan`, `ceniza`, `terremoto` | " (Diario de Mallorca, Giornale del Campidoglio) | 3 / 4 / 2 hits. War metaphors; Rome Nov 1809 "La scossa è stata simile a quella di un terremoto; alcune campane suonarono" (an explosion-like shock, not followed up) |
| 24 | IA fts | `afhes` (long s) | " | 1 hit, domestic anecdote (Newport 20 May 1809) |
| 25 | IA fts | `smoke` (1809) | " | 66 hits. Smokehouses, battle, Azores fire column. No weather |
| 26 | IA djvu.txt / inside.php | Pittsburgh 1 Mar 1809 and 31 May 1809; Alexandria 8 Sep 1809, 18 May 1809, 12 Apr 1809; Newport 27 May 1809 | — | Read as described above. inside.php URLs for Alexandria items exceed the WebFetch length limit |
| 27 | IA advancedsearch | `collection:newspapers` Dec 1808–Dec 1809, excluding ddd | — | 714 items (corpus in §0) |
| 28 | Georgia Historic Newspapers | `volcano`, `earthquake`, `ashes`, `etna`, `andtext=earthquake ashes [+city/lava/mountain/Lisbon/Cumberland]`, `ortext=haze hazy smoky smoaky pumice phenomenon` (lccn=sn82014388) | Savannah 1807–1816 | Page-level hits listed in §1b; text not accessible (robots) |
| 29 | Georgia Historic Newspapers | site-wide date filter | — | Not applied by the server |
| 30 | Virginia Chronicle (Veridian) | `volcano` Dec 1808 – Dec 1809 | Richmond/Norfolk papers | **Blocked (robots)** |
| 31 | NYS Historic Newspapers | `volcano` 1808–09 | NY titles | **Blocked (robots)** |
| 32 | CRU (UEA) Holyoke Salem data | readme | Salem 1786–1829 daily | Daily weather-description file exists; I guessed its file name and the fetch failed |
| 33 | IA | Hale 1833, *Memoirs AAAS* n.s. 1 (`sim_american-academy-of-arts-and-sciences-boston-memoirs_1833_1`) | Holyoke journal pp. 107–216 | inside.php: "No hOCR" without the `doc` parameter; with `doc` the URL is too long. Not read |
| 34 | APS | Legaux Spring Mill finding aid | Philadelphia area | Covers 1787–1800 only: **no 1809** |
| 35 | WebSearch | "1809 newspaper ashes fell on deck ship volcano South America" | web | Nothing relevant |

## 4. Source register

| Source / edition | Region / lang | Type | Covers 1808–09? | Digitized (URL) | Opened from here? |
|---|---|---|---|---|---|
| Alexandria Daily Gazette, Commercial & Political (IA) | Virginia; EN | daily port newspaper | yes (~326 issues Dec 1808–Dec 1809) | https://archive.org/details/per_alexandria-gazette-packet_alexandria-daily-gazette-commercial-politica_1809-05-18_9_2491 | yes (fts + djvu.txt) |
| Pittsburgh Weekly Gazette (IA) | Pennsylvania; EN | weekly | yes | https://archive.org/details/per_pittsburgh-weekly-gazette-895_pittsburgh-weekly-gazette_1809-03-01 | yes |
| Newport Mercury (IA) | Rhode Island; EN | weekly port paper | yes | https://archive.org/details/newport-mercury-1809-05-27 | yes |
| Kentucky Gazette (IA / ExploreUK) | Kentucky; EN | weekly | yes | https://archive.org/details/xt7h9w08x041 | yes (fts) |
| Diario de Mallorca (IA) | Spain; ES | daily | yes (~213 issues) | https://archive.org/details/DiarioDeMallorca_18090530 | yes (fts) |
| Giornale del Campidoglio (IA) | Rome; IT | newspaper (monthly volumes) | yes (some months) | https://archive.org/details/giornale-del-campidoglio-1809-11 | yes (fts) |
| Corriere delle Dame (IA) | Milan; IT | periodical | partial | https://archive.org/details/corriere-delle-dame-1809-12 | fts only |
| IA full-text search endpoint | — | search tool | — | https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=pumice | yes |
| The Republican; and Savannah Evening Ledger | Georgia; EN | port newspaper | yes from 3 Jan 1809 (gap 4 Oct 1808 – 3 Jan 1809) | https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388 | yes (search hits only; OCR text and images blocked) |
| Savannah 10 Jun 1809 p. 3 (earthquake + ashes, unidentified) | Georgia; EN | newspaper page | yes | https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1809-06-10/ed-1/seq-3/ | page metadata only |
| DLG Savannah Historic Newspapers collection | Georgia; EN | portal | 1809–1880 | https://dlg.usg.edu/record/dlg_savn | yes |
| Virginia Chronicle (Library of Virginia) | Virginia; EN | newspaper portal (Richmond Enquirer, Norfolk papers, etc.) | yes, likely | https://virginiachronicle.com/ | blocked (robots) |
| NYS Historic Newspapers | New York; EN | newspaper portal | some 1809 titles | https://nyshistoricnewspapers.org/ | blocked (robots) |
| Chronicling America (LoC) | US; EN | newspaper portal | sparse before 1836 | https://chroniclingamerica.loc.gov/ | blocked (loc.gov) |
| Readex, America's Historical Newspapers (Early American Imprints/Newspapers series I) — Salem Gazette, Columbian Centinel, Poulson's, Relf's, NY Mercantile Advertiser, Charleston Courier | US; EN | subscription database | yes, the key US port papers | https://www.readex.com/products/americas-historical-newspapers | not tried (library subscription) |
| GenealogyBank (consumer front end to much of Readex) | US; EN | subscription | yes | https://www.genealogybank.com/ | not tried (subscription) |
| Newspapers.com | US; EN | subscription | partial 1809 | https://www.newspapers.com/ | not tried (subscription) |
| American Antiquarian Society newspaper holdings (originals of most 1809 US papers) | US | library catalogue | yes | https://www.americanantiquarian.org/ | not tried |
| Holyoke (Salem) daily register, CRU UEA data and weather descriptions | Salem MA; EN | instrumental + descriptive diary data | yes (1786–1829) | https://crudata.uea.ac.uk/cru/data/holyoke/ | yes (readme); description file not reached |
| Hale 1833, "A Meteorological Journal 1786–1829" (Holyoke), *Memoirs AAAS* n.s. vol. 1, pp. 107–216 | Salem MA; EN | published register | yes | https://archive.org/details/sim_american-academy-of-arts-and-sciences-boston-memoirs_1833_1 | metadata only; text search failed |
| van der Schrier & Jones 2008, Salem daily series | — | paper | yes | https://ueaeprints.uea.ac.uk/25488/ | not tried |
| Legaux, Spring Mill meteorological observations (APS Mss.551.5.L52) | Philadelphia; FR/EN | manuscript | **no** (1787–1800) | https://search.amphilsoc.org/collections/style/pdfoutput/Mss.551.5.L52-ead.pdf | yes |
| APS digital library, meteorological data | US | digital library | mostly 18th c. | https://diglib-legacy.amphilsoc.org/islandora/search/dc.type:"Meteorological Data" | not tried |
| Philadelphia papers for *Monticello* (from Lima) arrival, ~Apr–May 1809 | Philadelphia; EN | newspapers | yes | no URL found (Readex/GenealogyBank above) | not tried |
