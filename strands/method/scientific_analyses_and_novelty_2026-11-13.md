---
ai-generated: true
author: Claude (Anthropic AI model)
directed-by: William John Suk (project lead)
verified-by: none
verification: summary of earlier notes; each item keeps the level given in its source note
strand: method
date: 2026-11-13
---
# The project's quantitative analyses: methods, datasets, results and novelty (13 Nov 2026)

William asked (13 Nov 2026): "explain what scientific analyses and datasets Claude used for scientific assessments. Include the novelty."

This note gathers, in one place, every numerical analysis Claude ran for the project between 16 Oct and 12 Nov 2026. It adds no new calculation. Each entry gives the question, the method, the dataset and its licence (from `data/README.md` and the hosting audit), the result, the verification level, and a novelty rating. The detail stays in the source notes, which are named on each entry.

**How to read the novelty ratings.** They are **Claude's assessment**, made against the literature the project has read (register B1-B79, `strands/science_alternatives/literature.md`, the novelty check of 16 Oct, the wide search of 4 Nov and the scholarship check of 12 Nov). They are not the result of a systematic review. "Not found in the literature reviewed" is the honest form of every claim below; a specialist may know of prior work we missed.

- **New**: we found no published analysis of this question for 1809.
- **New combination**: published data and standard methods, put together in a way we did not find published for 1809.
- **Replication**: repeats or extends a published result, with our own numbers.
- **Withdrawn**: the result was tested and failed; kept here so nobody reuses it.

**Verification levels** (as in CONTRIBUTING.md): `page-image`, `ocr`, `computed` (Claude's code on downloaded data), `text` (numbers read from a paper or file through a web text reader, not checked against a page image), `inferred`. No analysis below has been checked by a second person (`verified_by: none`). All scripts are in `scripts/` (MIT licence) and all derived tables in `data/` (CC BY 4.0, except `data/cc-by-sa/`).

**A general limit.** Claude's cloud container could not reach most scientific data portals (PANGAEA, NOAA, Zenodo, GEOROC and others: see project memory, "Environment limits"). Many datasets were therefore downloaded by William on his Mac, read from GitHub mirrors, or read as published tables through a text reader. Where a number was read as text, not computed from a file, the entry says so.

---

## Summary table

| # | Analysis | Main dataset | Result in one line | Verification | Novelty (Claude's assessment) |
|---|---|---|---|---|---|
| 1 | EIC marine air temperature step | oldWeather EEIC logs | Tropical Indian Ocean cools about 0.65 °C within voyages from Dec 1808-Jan 1809 | computed | New (monthly onset) |
| 2 | NEEM 2 cm sulfur timing | NEEM-2011-S1 (PANGAEA) | Winter 1808/09 clean; sulfate arrives Aug-Oct 1809, so eruption about Dec 1808-Mar 1809 | computed | Replication plus new reading |
| 3 | Antarctic per-core 1809/Tambora map | 17 published core papers | Uniform across Antarctica except Talos Dome (about 5 sd high) | computed; Talos page-image | Average = replication; Talos anomaly new |
| 4 | Bipolar onset lag and hemispheric split | Sigl 2013, Plummer 2012, Gao 2007 tables | Synchronous at both poles (tropical); about 55 % of sulfate in the north | text, computed | Replication, extended to four cores |
| 5 | Latitude band from the Greenland/Antarctic ratio | Marshall 2021 emulator, eVolv2k, Crowley 2013, EVA_H | Band 12°S-3°N **withdrawn**; ratio carries season, not latitude | computed | Withdrawn; the validation itself is new |
| 6 | Glass major-element scoring | GEOROC, Gill (EarthChem), published ice glass | Many medium-K arc andesites match equally (0.90-0.95); low-K arcs out | computed | New combination |
| 7 | Trace-element lookup (pre-registered) | GEOROC arc files | Zr/Nb would separate Dakataua (66), Gaua (43), Leyte (28) | computed | New (as a pre-registration) |
| 8 | Coral ENSO state 1808-10 | PAGES2k v2 corals | El Niño-like Dec 1808-May 1809, then neutral; not El Niño in Java's 1809 dry season | computed | Replication (Freund 2019) plus new inference |
| 9 | Coral footprint 1809-12 | PAGES2k v2, NOAA coral files | Lombok and Palau jump Dec 1808; Lombok's most extreme 4-yr window 1809-13 | computed | Footprint = replication; Dec 1808 onset new |
| 10 | Himalayan ice bismuth | Kaspari 2009 East Rongbuk (NOAA) | No 1809-11 bismuth peak; Tambora clear | computed | New (small negative) |
| 11 | Chinese gazetteers by database | REACHES v3.1 (CC0) | South China drought-famine 1809 at a 24-year high; no sky or ash coded | computed (coded rows) | New application |
| 12 | Milan/Prague diurnal range | GHCN-Daily | No veil signal; even Tambora barely shows | computed | New test, low power |
| 13 | Ships' haze counts | CLIWOC 2.1 | Townsend packet hazy 10 Dec 1808-9 Jan 1809 (weak, one observer); nothing else | computed | New |
| 14 | Parish burial counts, Bohol | FamilySearch images | No excess after Nov 1808; crisis 1810-11 | page-image (one pass) | New |
| 15 | Existing cores near candidates | PANGAEA/DataCite/NOAA catalogues | No dated 1809 tephra within 300 km; Kau Bay the one usable basin | text, computed distances | New compilation |
| 16 | Detection-floor distances | project's own read records | Melanesian candidates are more than 1,200-2,100 km from any read record | computed, inferred | New framing |
| 17 | Unidentified ice events vs GVP, 1760-1850 | eVolv2k v2.1, GVP 4.6.7 | No tropical VEI ≥3 eruption in GVP for 1807-10; side leads Makian 1760, Hekla 1845-46 | computed | New combination |
| 18 | Royal Navy fleet map | Steel's Navy List 1809; TNA Discovery | No RN ship east of Malacca Nov 1808-Mar 1809 | text, transcription | New (archival inventory, not a physical analysis) |

Smaller items are listed at the end (section 19).

---

## 1. East India Company logs: tropical marine air temperature (16 Oct)

- **Question.** Did the tropical ocean cool before or after the date the veil was seen (Bogotá, 11 Dec 1808)?
- **Method.** Noon air temperatures from 894 keyed EIC voyages (1789-1834; 128,144 tropical observations). Anomalies against a 10°×10° box and calendar-month climatology built from the same logs, with volcanic years left out. Two tests that remove differences between ships' thermometers: a within-voyage change (Aug-Nov 1808 against Jan-Apr 1809), and a sliding three-month step test with a null distribution from 415 non-volcanic months.
- **Dataset and licence.** oldWeather / EEIC keyed logs (Brohan et al. 2012), GitHub `oldweather/EEIC`; NOAA, licence **check**.
- **Result.** Within-voyage change −0.65 °C (17 voyages), colder than all 39 null years (null +0.08 ± 0.28). The step is largest at a split of 1 Dec 1808 or 1 Jan 1809; splits from Jul to Nov 1808 show nothing. The cold ships were in the Bay of Bengal and eastern equatorial Indian Ocean. Annual means agree with Brohan et al. 2012.
- **Limits.** Only 8 ships in Jan 1809, and one outlier (*Lord Keith*, −3.1 °C). A first reading by analogy with Tambora's 7-month lag put the eruption in May-June 1808; the NEEM timing (section 2) contradicts that, so the analogy was dropped.
- **Verification.** computed (`scripts/round6/eeic_at.py`, `eeic_onset.py`, `eeic_slide.py`). Finding F07.
- **Novelty.** **New** for the monthly onset. Brohan et al. 2012 published annual values only; we found no monthly or within-voyage analysis of 1808-09.
- **Source note.** `strands/science_alternatives/scientific_data_round6.md` R1.

## 2. NEEM-2011-S1 sulfur at 2 cm: when the 1809 sulfate reached Greenland (16 Oct)

- **Method.** Read the sub-annual series from 1795 to 1819, compare 1808-09 with the 1795-1808 background (mean 14.4 µg/kg, 95th percentile 25), and date the rise and peak. Tambora on the same core gives the eruption-to-arrival lag.
- **Dataset and licence.** Sigl et al., PANGAEA doi:10.1594/PANGAEA.940553, **CC BY 4.0** (downloaded by William).
- **Result.** Winter 1808/09 is at background. The 1809 sulfate rises about Aug-Oct 1809 and peaks in spring 1810. With Tambora's lag of 7-8 months, the eruption falls about Dec 1808-Mar 1809. This rules out a mid-1808 eruption (inference).
- **Limits.** One core; the dating error is about ±3 months.
- **Verification.** computed (`scripts/round6/fig.py`). Finding F08.
- **Novelty.** **Replication plus a new reading.** Sigl et al. 2013 already published the NEEM-S1 onset (1809.7); our reading of the raw series gives the same onset. Using the clean winter of 1808/09 to argue against a mid-1808 date is, as far as we found, not published.

## 3. Antarctic sulfate map: 1809 against Tambora, core by core (26 Oct)

- **Question.** Is the 1809 sulfate in Antarctica even (far-travelled), or is there extra near a local volcano?
- **Method.** For each core, divide its 1809 flux by its own Tambora flux. The ratio cancels most site effects (snowfall, laboratory). Compare the ratios across the continent and by distance from Mt Melbourne and the Pleiades.
- **Dataset and licence.** Published flux tables from 17 core papers (cited per row); these are facts, cite the papers.
- **Result.** Fifteen cores away from Victoria Land give 0.26-0.76 (mean 0.48, sd 0.12), matching the published averages (0.45 Cole-Dai 2009; 0.44 Gao composite). The two Talos Dome cores give 1.05 and 1.11, about 5 sd high; GV7 at 450 km is normal. This fits a small local Victoria Land eruption around 1809-10 on top of the main signal (inference), the same one whose glass Kurbatov et al. 2006 found at Siple Dome.
- **Limits.** Talos values come from one paper (Nardin et al. 2020); the two Talos cores disagree badly on some other events.
- **Verification.** computed; Talos input values page-image checked. Finding F19.
- **Novelty.** The continental average is **replication**. The Talos Dome excess for 1809 is **new**: we found no paper that points it out.
- **Source note.** `strands/science_alternatives/antarctic_sulfate_map_2026-10-26.md` (register B46).

## 4. Bipolar onset lag and hemispheric split (27 Oct)

- **Method.** Greenland-minus-Antarctica onset lag from four sub-annually dated cores (WDC06A, Law Dome DSS, NEEM-S1, NGRIP), with Tambora and Krakatau as controls. The north/south deposition ratio relative to Tambora across five bases. A Tambora-analogue eruption date (each core's Tambora delay applied to its 1809 onset).
- **Dataset and licence.** Sigl et al. 2013 Table 1; Plummer et al. 2012 Table 2; Gao et al. 2007; Cole-Dai et al. 2009 (published tables; cite the papers). Read as text, not page images.
- **Result.** Lag −0.05 yr (range −0.4 to +0.3): synchronous, so tropical. But Tambora and Krakatau show no consistent sign either, so the lag cannot say north or south of the equator. About 55 % of the deposited sulfate fell in the north (45-65 %). Tambora-analogue date 1809.07 ± 0.41 (Claude's calculation).
- **Verification.** text, computed (`scripts/bipolar_lag_2026-10-27/lag.py`). Finding F29.
- **Novelty.** **Replication**, extended. Cole-Dai et al. 2009 showed bipolar synchrony from three cores; this uses four independently dated cores and adds controls. It does not tighten latitude beyond Cole-Dai.
- **Source note.** `strands/science_alternatives/bipolar_sulfate_lag_2026-10-27.md` (B55).

## 5. Latitude band from the Greenland/Antarctic ratio: tested and **withdrawn** (28 Oct)

- **What was tried first (B62).** The Marshall et al. 2021 deposition emulator (UM-UKCA, Gaussian-process grid on GitHub `cemac/volcanic-forcing-deposition`) was inverted for the 1809 ratio after calibration with Tambora. It gave a provisional band of about 12°S-3°N for a Nov-Dec eruption, which would have weighed against Cabalían (10°N).
- **The test.** Eleven tropical eruptions of known latitude and month (Huaynaputina to Pinatubo), with observed ratios from eVolv2k v2.1 (variable `hemi`), Crowley & Unterman 2013, Sigl 2013 and Gao 2007. EVA_H (Aubry et al. 2020) was also run: 264 deposition runs and 7 timing runs.
- **Datasets and licences.** eVolv2k v2.1, Toohey & Sigl 2017, **CC BY 4.0**; Crowley & Unterman 2013 (NOAA, **check**); Marshall 2021 emulator grid (**check**); EVA_H code (GitHub `thomasaubry/EVA_H`, **check**).
- **Result.** The emulator predicts the eleven ratios with an rms error of a factor 3.0 and no correlation (Spearman 0.20, p 0.55). Only one of four pre-set test eruptions passed. Observed ratios show **no latitude slope** inside ±17° but a **season** signal: Oct-Feb eruptions put about twice as much on Greenland as Mar-Jun ones (p 0.04, n 11). EVA_H gives a ratio of 1.00 for any source within ±15°, by design. So the ratio says only "tropical". **The 12°S-3°N band is withdrawn and Cabalían is not excluded by latitude.**
- **Verification.** computed (`scripts/deposition_validation_2026-10-28/`, `scripts/creative_next_steps_2026-10-28/`). Finding F30.
- **Novelty.** The band is **withdrawn** and must not be cited. The validation of the emulator against eleven eruptions, and the season-not-latitude pattern, we did not find published. Marshall et al. 2021 already showed that their own blind inversion of Tambora misplaces it (22-56°S), so the emulator's weakness is partly **replication**. The season effect was predicted in models (Toohey et al. 2013); the observed-ratio fit is **new combination**. With n = 11 it is suggestive only.
- **Source note.** `strands/science_alternatives/deposition_ratio_validation_2026-10-28.md` (B66).

## 6. Ice-core glass against candidate volcanoes: major-element scoring (22 Oct-2 Nov)

- **Method.** Borchardt similarity coefficient on seven oxides (TiO2 left out), using means of the published 1809 ice glass (Dome C, South Pole; also Eclipse Icefield and Siple Dome). Control: South Pole 1816 glass against Tambora scores 0.92, so the method recognises a known match. Applied first to published papers, then to 8,740 GEOROC analyses and 248 Gill whole-rock analyses, then per volcano for Vanuatu and the Solomons.
- **Datasets and licences.** Ice glass: Plunkett et al. 2023, Kurbatov et al. 2006, Yalcin et al. 2006 and others (`data/glass_ice_1809.csv`, cited per row). GEOROC precompiled arc files, version 2026-09 (treated as **CC BY**; item licence to confirm, U192). Gill, EarthChem Library 1499/1502/1503, **CC BY-SA 4.0** (output in `data/cc-by-sa/`).
- **Result.** The Antarctic 1809 glass is an iron-rich medium-K arc andesite (about 60 % SiO2). Many unrelated arc andesites score 0.90-0.95, which is the same-source range: Dakataua Makalia 0.92, SW Luzon and Vanuatu marine glass 0.92-0.95, and across Vanuatu Tanna, Ambrym, Gaua and Kuwae all 0.91-0.97. Low-K arcs (Tonga, the New Britain arc front, Witori, northern Banda) score 0.83 or less and are unlikely. Andean dacites and Witori's rhyolite do not fit.
- **Limits.** 6-13 shards per ice population, mostly 1990s SEM-EDS; GEOROC is mostly whole rock, not glass; most candidates have no glass data at all (untested, not excluded). Major elements cannot name the volcano.
- **Verification.** computed (`scripts/glass_similarity_2026-10-26.py`, `score_georoc_2026-10-26.py`, `score_gill_ecl_2026-10-26.py`, `glass_vanuatu_solomons_2026-11-02/`). Findings F20, F34.
- **Novelty.** **New combination.** Plunkett et al. 2023 already called the South Pole glass comparable to Indonesian tephra. The systematic scoring against whole arc databases, with a Tambora control, is not published as far as we found. Its main value is negative: it shows how unspecific the existing ice glass is, and that a Gaua match is not specific to Gaua. A side observation: Plunkett's comparison sample (Faral et al. 2022 "Telaga Group F") is a bulk tephra, not glass (inference from page images).
- **Source notes.** `strands/candidates/glass_comparison_2026-10-22.md`, `glass_candidates_compilation_2026-10-26.md`, `strands/method/free_checks_T5-T10_2026-11-02.md`.

## 7. Trace-element lookup, fixed in advance (2 Nov)

- **Method.** For each candidate group, medians and quartiles of 14 trace-element ratios in GEOROC samples with 55-68 % SiO2, written down before any ice-glass trace data exist, so that a future measurement cannot be fitted after the fact.
- **Dataset and licence.** GEOROC arc files 2026-09 (as section 6).
- **Result.** Zr/Nb separates the top three: Dakataua about 66, Gaua about 43, Leyte about 28 (La/Nb 6.6, 8.2, 4.4). Agung is missing (Sunda file not downloaded, U154); Cabalían has no separately labelled samples.
- **Verification.** computed (`scripts/trace_lookup_2026-11-02/trace_ratios.py`).
- **Novelty.** **New** as a pre-registered comparison for 1809. It is a tool, not a result: it only becomes evidence when someone measures trace elements in the ice glass (held by the Hutchison, Plunkett and McConnell groups, U90-U92).
- **Source note.** `strands/candidates/trace_element_lookup_2026-11-02.md`.

## 8. Coral composite and the ENSO state, 1808-10 (27 Oct)

- **Method.** 18 Indo-Pacific coral series from PAGES2k v2, sign-adjusted to ENSO using the modern Niño3.4 relation (Bunge & Clarke 2009), composited monthly; compared with tree-ring and multiproxy ENSO lists.
- **Dataset and licence.** PAGES2k v2 via GitHub `fzhu2e/cfr-data` (open; licence **check**); Bunge & Clarke 2009 Niño3.4.
- **Result.** Corals show El Niño-like conditions from late 1808 to about May 1809, then neutral; tree rings and the multiproxy lists say La Niña 1808-10. The Lombok coral is normal in Jul-Nov 1809, so a developing El Niño is unlikely to explain the 1809 Java dry-season drought (inference).
- **Verification.** computed; the literature as text. Finding F23.
- **Novelty.** **Replication**: Freund et al. 2019 already show DJF 1808/09 El Niño-like (0.51). Linking the coral state to the 1809 Batavia rice failure is a **new inference**, not a test. The note also records, from the text of Timmreck et al. 2021, that every one of their 40 runs placed the eruption at the equator on 1 Jan 1809, so no published model run has tested latitude.

## 9. Coral footprint of 1809-12 (28 Oct)

- **Method.** 34 coral records, yearly and monthly anomalies 1800-1820, window statistics and a map; comparison with published reconstructions.
- **Dataset and licence.** PAGES2k v2 and NOAA NCEI coral files (**check**); published reconstructions transcribed for comparison (D'Arrigo 2006, Tierney 2015, Lough 2007 and others; cite the papers).
- **Result.** Lombok (13 km from Agung) and Palau both jump in Dec 1808 (+2.1 and +2.2 sd). Lombok is normal in the 1809 dry season, then has its most extreme four-year window of 1782-1990 (Jul 1809-Jun 1813). Fiji, the Great Barrier Reef, Malindi and Galápagos are cool or dry 1809-12; the Vanuatu coral (Espiritu Santo, 98 km from Gaua) is not. The pattern is not ENSO-like (inference). It does not locate the eruption.
- **Verification.** computed (`scripts/coral_footprint_2026-10-28/`). Finding F22.
- **Novelty.** The 1809-12 warm-pool cooling is **published** (D'Arrigo et al. 2006 called it the greater impact of 1809 and Tambora; Tierney et al. 2015). The **Dec 1808 onset month** at Lombok and Palau and the Vanuatu null we did not find published (**new**).
- **Source note.** `strands/science_alternatives/coral_footprint_1809-12_2026-10-28.md` (B65).

## 10. Himalayan ice: bismuth enrichment at East Rongbuk (28 Oct)

- **Method.** Crustal enrichment factor of bismuth (a volcanic tracer used by Xu et al. 2009) for each East Rongbuk sample 1795-1830, against the threshold from that method.
- **Dataset and licence.** Kaspari et al. 2009, NOAA NCEI `rongbuk2009.txt` (US federal archive; contributed data, **check**); Dasuopu decadal file (Gabrielli et al. 2020).
- **Result.** Sixteen samples 1808-1811 show no enrichment (EFc 1.7-27, threshold 371); Tambora is one sample at 3,882. A weak negative; it does not locate the source.
- **Verification.** computed (`scripts/tibet_icecores_2026-10-28/`). Finding F28.
- **Novelty.** **New**, small. Xu et al. 2009 listed nine events and 1809 was not among them, but we found no sample-level look at 1808-11.

## 11. Chinese local gazetteers through REACHES (27 Oct)

- **Method.** All REACHES rows Jul 1808-Jun 1810 decoded (646 rows); counts of drought, famine, frost and optical events for South China against a 1780-1840 baseline.
- **Dataset and licence.** REACHES v3.1 (Wang et al. 2018; coding of Zhang De'er 2004), NOAA study 23410, **CC0**.
- **Result.** Frost on the Guangxi coast in Nov-Dec 1808; drought-famine in 1809 at 26 sites, the highest count of 1796-1819. We found no red sky, dim sun, haze, ash or sea surge coded for Nov 1808-Mar 1809 in these rows (weak negative: Tambora's optics are not coded either).
- **Limits.** The database has coded categories, not the quoted text; Gregorian months are its conversion. A pirate blockade is an alternative cause of famine.
- **Verification.** coded database rows; counts computed (`scripts/reaches_2026-10-27/`). Finding F25.
- **Novelty.** **New application** of a published database; we found no paper linking the 1809 South China drought to the eruption.

## 12. Milan and Prague diurnal temperature range (16 Oct)

- **Method.** A veil should cut daytime sunshine and narrow the daily range. Monthly anomalies 1785-1830, Tambora as a control.
- **Dataset and licence.** GHCN-Daily (NOAA, AWS open data); station series **check**.
- **Result.** No signal in Dec 1808-Mar 1809, and Tambora barely registers either (Milan 1816 −0.19, Prague −0.51). The test has little power: winter range is dominated by cloud, and readings were at fixed hours.
- **Verification.** computed (`scripts/round6/dtr.py`).
- **Novelty.** **New test**, negative and low power. Not worth citing as evidence against a veil.

## 13. Ships' haze counts, CLIWOC 2.1 (16 Oct)

- **Method.** Count "hazy" in the Clearness and Weather fields by voyage, against a baseline of the same calendar month and region in all other years 1750-1854. Full-text search of all remark fields for volcanic wording.
- **Dataset and licence.** CLIWOC 2.1 (García-Herrera et al. 2005; EU project, freely released, **check**); cleaned copy GitHub `jburnford/CLIWOC_work`.
- **Result.** We found no volcano, ash, pumice, red-sun or dim-sun remark in 1,765 records (Sept 1808-Jun 1810). The packet *Townsend* logs haze almost daily from 10 Dec 1808 to 9 Jan 1809 along 30°W, against about 10 % normally, but this observer wrote "hazy" on 58 % of all days (weak). *Penelope* and *Tigris* are weaker still. The San Fernando "calimoso" days of winter 1809 all came with south-east winds (probably Saharan dust); the dataset's authors had already set the volcanic reading aside, so that part is **replication**.
- **Verification.** computed (`scripts/round6/cliwoc_*.py`, `sf.py`). Findings F06, F11, F12, F14.
- **Novelty.** **New** for the 1808-09 haze screen.

## 14. Parish burial counts, Bohol (28 Oct)

- **Question.** Would a large eruption of Cabalían (Leyte) show as extra deaths 150-180 km away?
- **Method.** Monthly burial counts from page images of three parish burial books 1806-1811 (Baclayon, Tagbilaran, Loon), read once by Claude, with any marginal notes. No Leyte register for 1808-10 survives in the FamilySearch catalogue.
- **Dataset and licence.** FamilySearch images (DGS 7768815, 7769534, 5382642); no images hosted; counts are facts.
- **Result.** We found no excess of burials after Nov 1808 and no note of sky, ash, noise, earthquake, hunger or sickness. All three parishes show a mortality crisis in 1810-11, with a children's wave Jan-Apr 1811.
- **Verification.** page-image, one pass, not double-counted. Finding F27.
- **Novelty.** **New** counts. A weak negative for a very large eruption near Bohol; silent on distant candidates. The 1810-11 crisis is unexplained.

## 15. Existing sediment, coral and cave archives near the candidates (28 Oct)

- **Method.** Catalogue search (PANGAEA via DataONE, DataCite, NOAA paleo) in a 300 km box around each candidate; great-circle distances; record of which archives have a dated 1800-1820 section.
- **Dataset and licence.** Catalogue metadata (facts); compilation CC BY 4.0.
- **Result.** 58 archives; none has a published tephra layer dated to about 1809. Kau Bay (Halmahera) is the only basin with cores that could resolve 1809. No core exists for Lake Dakataua or Lake Letas (Gaua). The Espiritu Santo coral and Taurius Cave stalagmite near Gaua show no 1809-11 cooling.
- **Verification.** text (catalogue), computed (distances). Finding F35.
- **Novelty.** **New compilation**. Coverage gaps remain (IMLGS not queried).

## 16. Detection-floor distances (4 Nov)

- **Method.** Great-circle distance from 14 candidate volcanoes to every 1808-10 written record the project has read or located (280 rows), with the kind of record noted.
- **Dataset and licence.** The project's own list; coordinates approximate; CC BY 4.0.
- **Result.** Every Melanesian candidate (Dakataua, Rabaul, Bougainville, Lamington, Victory) is more than about 2,100 km from any read record, so documentary silence there is close to no evidence. Gaua's nearest is a secondary account from Tanna (614 km, Jul 1809). Agung's nearest is the Bima court record at 353 km, which did record Tambora, so Agung's silence carries more weight. Cabalían has the only read source within 50 km, and it is weak (the *Ramoncita* track charts).
- **Verification.** computed; the reading is inference. The weighted ranking (second half of T11) was not attempted because its weights would be Claude's judgement.
- **Novelty.** **New framing.** Simple arithmetic, but we found no published attempt to measure how close the written record gets to each candidate.

## 17. Unidentified ice-core events 1760-1850 against GVP (4 Nov)

- **Method.** Each unidentified eVolv2k v2.1 event matched to GVP eruptions of VEI 3 or more in a year and latitude window.
- **Datasets and licences.** eVolv2k v2.1 (CC BY 4.0); GVP Volcanoes of the World 4.6.7, snapshot of 8 May 2018 in pyvolcans 1.3.3 (terms **check**, U193).
- **Result.** GVP has no tropical VEI ≥3 eruption in 1807-1810 apart from a small Cameroon event: the 1809 source is either unrecorded or recorded too vaguely to date. Side leads: Makian 1760 for the 1762 event, Hekla 1845-46 for 1846; 1821 has no candidate at all.
- **Limits.** The GVP snapshot is stale: the live GVP now lists a Karthala 1808 eruption (F39; re-screen is T59). Karthala is basaltic, so a poor fit for the andesitic glass (inference).
- **Verification.** computed (`scripts/related_mysteries_2026-11-04/match_unidentified.py`).
- **Novelty.** **New combination**; we found no published attempt on 1762, 1821 or 1846.

## 18. Royal Navy fleet map (2 Nov)

- **Method.** Transcription of 233 ships on distant stations from Steel's Navy List of 1 Jan 1809; one TNA Discovery lookup per ship for surviving logs; map.
- **Datasets and licences.** Steel's List (public domain, archive.org); TNA Discovery catalogue (Open Government Licence).
- **Result.** No Royal Navy ship east of Malacca from Nov 1808 to Mar 1809; none in the Pacific. 86 of 145 Atlantic-station ships have logs at Kew.
- **Verification.** text and transcription.
- **Novelty.** **New** as an inventory. It is archival planning rather than a physical analysis, included because it set the limits of the ship-log search.

## 19. Smaller calculations

- **Hiroshima summer 1809** (F21): values digitised by Claude from a figure in Hirano et al. 2018; no 1809 summer cooling at one site. inferred; reuse of published data.
- **Two-eruption case file** (wide search s. 11): glass differences between the Eclipse Icefield and Antarctic 1809 glass computed at 2-5 times the spread; onset dates from Wilson et al. 2026 give 1809.12 (Greenland) and 1808.98 (Antarctica), a difference within error. Yalcin et al. 2006 and Meuer et al. 2024 already raised a second eruption, so this is **replication** and synthesis, not a new result.
- **Dome C Δ33S** (wide search s. 9.9): a small positive value in the sample before the 1809 peak in Gautier et al. 2019 data; noted, not interpreted. computed from published data.

---

## What is new, in plain terms (Claude's assessment)

1. **New and potentially useful to specialists**: the Dec 1808-Jan 1809 cooling step in EIC logs (1), the Talos Dome 1809 excess (3), the Dec 1808 onset in the Lombok and Palau corals (9), the validation showing the hemispheric ratio carries season rather than latitude (5), and the pre-registered trace-element table (7). Each is a modest, single-dataset result that a specialist should check.
2. **New combinations of standard methods**: systematic glass scoring against whole arc databases (6), REACHES for South China (11), the existing-cores compilation (15), detection-floor distances (16) and the GVP screen of unidentified events (17). Their main contribution is to show where the evidence is thin, not to point to a volcano.
3. **Replications**: the bipolar synchrony (4), the Antarctic average ratio (3), the NEEM onset (2), the coral ENSO state (8) and the 1809-12 warm-pool cooling (9). These agree with the published work, which is a check on our numbers.
4. **Withdrawn**: the 12°S-3°N latitude band (5). Do not cite it.
5. **Negatives with little power**: Milan/Prague range (12), Himalayan bismuth (10), Bohol burials (14). We found no signal in these; that is weak evidence of absence.

**What none of this does.** No analysis names the volcano. The physical evidence that could settle it (trace elements in the ice glass, a Lake Dakataua core, Gaua's youngest tephra, the H15 and Talos Dome ash) is held by other groups or not yet collected (`strands/method/evidence_that_would_settle_it_2026-11-02.md`).

**Unavailable sources.** This note adds no new source, so no U-number was taken.
