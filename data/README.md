# Data files: provenance and licence

Written 4 Nov 2026 (tasks T31 and T38). One line per file: what it is, the source dataset it was built from, that source's licence, and the script or note that made it. Licences come from the hosting audit (`data/hosting_licence_audit_2026-11-04.csv`, `strands/method/hosting_licence_audit_2026-11-04.md`). Where the audit says **check**, the item-level licence has not yet been read on the provider's own page (tasks T36, T40; terms pages U179-U194).

**Licence of these files.** Tables, figures and JSON made by this project are released under **CC BY 4.0** (see `LICENSE.md` at the top of the repository), except the files in `data/cc-by-sa/`, which are **CC BY-SA 4.0** because they adapt share-alike data (see `data/cc-by-sa/LICENSE.md`). The source datasets keep their own licences, given below; please cite them as well as this project when you reuse a file.

**If an item should not be here.** We host only tables we derived ourselves and short extracts we believe the source's licence allows. If you hold rights in, or believe we should not host, any file in this folder, email **1808@williamsuk.ai** and it will be taken down promptly while we look into it.

**How the files were made.** Every file was produced by Claude (an AI model) working for the project maintainer; none has yet been checked by a second person (`verified_by: none`). Counts from manuscripts (parish books) were made by reading page images once. Scripts are in `scripts/` (MIT licence). "Script: none" means the table was built by hand or in a one-off session from the note named; the note gives the method.

Verification levels: `page-image` (read from an image of the original), `ocr`, `computed`, `inferred`, as in CONTRIBUTING.md.

## Ice cores and volcanic forcing

| File | What | Source dataset and licence | Made by |
|---|---|---|---|
| `neem2011s1_2cm_1804-1819.csv` | NEEM-2011-S1 sulfur at 2 cm resolution, 1804-1819 extract | Sigl et al., PANGAEA doi:10.1594/PANGAEA.940553, **CC BY 4.0** | extract; note `strands/science_alternatives/scientific_data_round6.md` |
| `neem2011s1_sulfur_1809_vs_tambora.png` | Figure of the above | as above | `scripts/round6/fig.py` |
| `antarctic_sulfate_1809_vs_tambora.csv`, `_map.png` | 1809/Tambora sulfate ratio for 15+ Antarctic cores | Values from 17 published core papers (tables cited per row); facts, cite the papers | `scripts/antarctic_sulfate_2026-10-26/build.py`, `fig.py` |
| `bipolar_lag_1809_2026-10-27.csv` | Greenland-Antarctic onset lag, 1809, Tambora, Krakatau | Sigl et al. 2013; Plummer et al. 2012; Gao et al. 2007 (published tables; cite the papers) | `scripts/bipolar_lag_2026-10-27/lag.py` |
| `evolv2k_v2.1_events_2026-10-28.csv` | 271 eVolv2k v2.1 events (dump of the netCDF) | Toohey & Sigl 2017, ESSD 9:809, **CC BY 4.0** | note `deposition_ratio_validation_2026-10-28.md` |
| `deposition_ratio_validation_2026-10-28.csv`, `deposition_ratio_of_ratios_vs_tambora_2026-10-28.csv` | Emulator vs observed Greenland/Antarctic ratios, eleven eruptions | eVolv2k (CC BY 4.0); Crowley & Unterman 2013 (NOAA, **check**); Marshall et al. 2021 emulator grid (GitHub cemac/volcanic-forcing-deposition, licence **check**) | `scripts/deposition_validation_2026-10-28/validate_emulator.py` |
| `deposition_emulator_ratio_by_latitude_2026-10-28.csv` | Emulator ratio by latitude (the withdrawn band, F30) | Marshall et al. 2021 emulator (**check**) | `scripts/creative_next_steps_2026-10-28/invert.py`, `calib.py` |
| `evah_deposition_ratio_grid_2026-10-28.csv`, `evah_saod_timing_2026-10-28.csv` | EVA_H model runs | Our runs of EVA_H (Aubry et al. 2020, GitHub thomasaubry/EVA_H; licence **check**) | `scripts/deposition_validation_2026-10-28/run_evah.py`, `grid_evah.py`, `timing_evah.py` |
| `everest_samples_1795-1830_efc_2026-10-28.csv`, `himalaya_bismuth_1795-1830_2026-10-28.png` | East Rongbuk samples 1795-1830 with bismuth enrichment | Kaspari et al. 2009, NOAA NCEI rongbuk2009.txt (US federal archive; contributed data, **check**) | `scripts/tibet_icecores_2026-10-28/everest_close.py`, `himalaya_fig.py` |

## Glass and rock chemistry

| File | What | Source dataset and licence | Made by |
|---|---|---|---|
| `glass_ice_1809.csv` | Published major-element analyses of the 1809 ice glass | Plunkett et al. 2023, Kurbatov et al. 2006 and others (measured values; source paper and table on each row) | note `glass_candidates_compilation_2026-10-26.md` |
| `unsourced_ice_glass_1750-1850_2026-11-04.csv` | Ice-core glass occurrences 1750-1850 with no proximal source (plus the solved 1831 case and the Siple Dome Pleiades attribution), 9 rows | compiled from published papers (reference on each row); this compilation CC BY 4.0 | note `wide_source_search_2026-11-04.md` 12.14 |
| `glass_candidates.csv` | Published glass and rock analyses of candidate volcanoes | Published papers, cited per row | same note |
| `glass_similarity_2026-10-26.csv` | Similarity scores, ice glass vs candidates | derived from the two files above | `scripts/glass_similarity_2026-10-26.py` |
| `georoc_scored_2026-10-26.csv` | 8,740 GEOROC analyses scored against the ice glass | GEOROC precompiled arc files, version 2026-09 (DIGIS, Univ. Göttingen; GRO.data); the maintainer's decision of 4 Nov treats it as **CC BY**, item-level licence still to confirm (U192) | `scripts/score_georoc_2026-10-26.py` |
| `glass_vanuatu_solomons_by_volcano_2026-11-02.csv` | Per-volcano summary for Vanuatu and the Solomons (F34) | GEOROC as above | `scripts/glass_vanuatu_solomons_2026-11-02/summarise.py` |
| `trace_ratio_lookup_2026-11-02.csv`, `trace_ratio_separation_2026-11-02.csv` | Pre-registered trace-element ratio lookup | GEOROC as above | `scripts/trace_lookup_2026-11-02/trace_ratios.py` |
| `cc-by-sa/gill_ecl_wholerock_scored_2026-10-26.csv` | Gill whole-rock analyses scored against the ice glass | Gill, EarthChem Library 1499, 1502, 1503, **CC BY-SA 4.0** (U194 to confirm); this file is CC BY-SA | `scripts/score_gill_ecl_2026-10-26.py` |
| `gvp_tropical_candidates_1808.csv` | Tropical volcanoes with Holocene eruptions, from GVP | Smithsonian Global Volcanism Program, Volcanoes of the World 4.6.7 (via the pyvolcans package); terms **check** (U193) | `scripts/gvp_candidates.py` |

## Corals, tree rings and climate

| File | What | Source dataset and licence | Made by |
|---|---|---|---|
| `coral_enso_1804-1814_2026-10-27.csv` | Indo-Pacific coral anomalies 1804-1814, ENSO sign-adjusted | PAGES2k v2 (via GitHub fzhu2e/cfr-data); PAGES2k data are open, licence **check**; Bunge & Clarke 2009 Niño3.4 | `scripts/coral_enso_2026-10-27/coral_enso.py` |
| `coral_footprint_1806-1816_2026-10-28.csv` | First coral footprint (28 records) | PAGES2k v2 as above | `scripts/creative_next_steps_2026-10-28/` (note `creative_next_steps_2026-10-28.md`) |
| `coral_footprint_1800-1820_2026-10-28.csv`, `coral_footprint_monthly_z_1800-1820_2026-10-28.json`, `coral_footprint_map_1809-12_2026-10-28.png`, `coral_footprint_series_1805-1818_2026-10-28.png` | Coral footprint 1809-12, 34 records (F22) | PAGES2k v2 as above; NOAA NCEI coral files (**check**) | `scripts/coral_footprint_2026-10-28/` |
| `coral_footprint_external_series_2026-10-28.csv` | Published reconstructions transcribed for comparison (D'Arrigo 2006, Tierney 2015, Lough 2007 and others) | NOAA NCEI files and paper tables (**check**; cite the papers) | note `coral_footprint_1809-12_2026-10-28.md` |
| `existing_cores_near_candidates_2026-10-28.csv` | 58 archives within 300 km of the candidates, distances | Catalogue metadata from PANGAEA, DataCite, NOAA paleo (facts) | note `existing_cores_near_candidates_2026-10-28.md` |
| `milan_prague_diurnal_range_monthly_1785-1830.csv` | Monthly diurnal temperature range, Milan and Prague | Published station series (source named in the note; **check**) | `scripts/round6/dtr.py` |
| `mallorca_weather_1808-09_1809-07.csv` | Daily weather from the *Diario de Mallorca* | Our transcription of a pre-1900 newspaper (public domain text; scans on archive.org) | note `newspaper_downloads_round5.md` |
| `reaches_1808-07_1810-06_2026-10-27.tsv`, `reaches_south_china_baseline_1780-1840_2026-10-27.tsv` | REACHES rows Jul 1808-Jun 1810 and South China baseline counts (F25) | REACHES v3.1, Wang et al. 2018, NOAA study 23410, **CC0** | `scripts/reaches_2026-10-27/` |

## Ships' logs and the fleet

| File | What | Source dataset and licence | Made by |
|---|---|---|---|
| `cliwoc21_full_text_1808-09_1810-06.csv`, `cliwoc_cleaned_weather_text_1808-09_1809-06.txt` | CLIWOC 2.1 records for the window, with weather text | CLIWOC 2.1 (García-Herrera et al. 2005; EU project, freely released; **check**) | `scripts/round6/cliwoc_full.py`, `cliwoc_haze.py` |
| `eic_keyed_weather_1808-03_1808-09.csv`, `eic_keyed_weather_1808-10_1809-03.csv`, `eic_unkeyed_port_stays_1808.txt`, `eic_tropical_air_temp_monthly_1789-1834.csv`, `eic_tropical_air_temp_monthly_1805-1819.png` | English East India Company logs, keyed weather and noon air temperature (F07) | oldWeather / EEIC keyed logs (Brohan et al. 2012; NOAA, **check**) | `scripts/round6/eeic_at.py`, `eeic_onset.py`, `eeic_slide.py`, `fig.py` |
| `rn_stations_steel_1809-01-01.csv` | 233 Royal Navy ships on distant stations, 1 Jan 1809 | Our transcription from Steel's Navy List, 1 Jan 1809 (public domain; archive.org steelslistroyalnavy1809jan) | note `fleet_log_inventory_2026-11-02.md` |
| `packets_steel_1809-01-01.csv` | Falmouth packets, Jan 1809 | Same list, p. 22 (public domain) | same note |
| `rn_logs_atlantic_stations_2026-11-02.csv` | Which Atlantic-station ships have a Kew log for the window | TNA Discovery catalogue descriptions (facts; catalogue under the Open Government Licence) | same note |
| `detection_floor_distances_2026-11-04.csv` | Great-circle distances from 14 candidate volcanoes to 20 read or located 1808-10 records (280 rows) | this project, CC BY 4.0 (coordinates approximate) | `scripts/detection_floor_2026-11-04/build.py`; note `wide_source_search_2026-11-04.md` 10, 12.11 |
| `unidentified_ice_events_gvp_matches_1760-1850_2026-11-04.csv` | GVP eruptions (VEI 3+, latitude band, year window) matching each unidentified eVolv2k v2.1 event 1760-1850 (22 rows) | derived from GVP VOTW 4.6.7 (Global Volcanism Program 2013; snapshot in pyvolcans 1.3.3) and eVolv2k v2.1 (Toohey & Sigl 2017, CC BY 4.0) | `scripts/related_mysteries_2026-11-04/match_unidentified.py`; note `wide_source_search_2026-11-04.md` 13 |

## Parish registers

| File | What | Source dataset and licence | Made by |
|---|---|---|---|
| `baclayon_burials_monthly_1806-1810_2026-10-28.csv` | Monthly burial counts, Baclayon, Bohol (F27) | Our counts from FamilySearch images of the parish book (DGS 7768815). No images are hosted; counts are facts | note `cabalian_parish_records_familysearch_2026-10-28.md` (counts by hand, one pass) |
| `bohol_burials_monthly_three_parishes_1806-1812_2026-10-28.csv` | Monthly burials, Baclayon, Tagbilaran, Loon (F27) | Same route (DGS 7768815, 7769534, 5382642) | notes `cabalian_parish_records_familysearch_2026-10-28.md`, `bohol_burial_entries_by_image_2026-10-28.md` |

## Project housekeeping

| File | What | Licence | Made by |
|---|---|---|---|
| `hosting_licence_audit_2026-11-04.csv` | What may be hosted, linked or only transcribed (54 rows) | this project, CC BY 4.0 | note `hosting_licence_audit_2026-11-04.md` |
| `README.md` | This file | CC BY 4.0 | T31 |
