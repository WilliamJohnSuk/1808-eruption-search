---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: science_alternatives
date: 2026-10-27
---

# Coral and tree-ring fingerprints of 1809: Timmreck 2021, later work, and ENSO 1808-1810 (27 Oct 2026)

Thread "Test 1809 climate fingerprints in corals and tree rings". Register B58. Data: data/coral_enso_1804-1814_2026-10-27.csv. Script: scripts/coral_enso_2026-10-27/coral_enso.py.

Verification levels used here: **[text]** = paper or data file read through the web fetch tool (summaries plus short quotations returned by that tool, no page images); **[calc]** = Claude's own calculation from published proxy values; **[inference]** = Claude's interpretation, not stated by any source.

## 1. Short answer

- **Timmreck et al. 2021 did not test eruption latitude.** All 40 runs put the eruption at the Equator on 1 Jan 1809. Their only hemispheric test, removing the aerosol north of the tropics ("nNHP"), matched the tree rings better but they call it "an unlikely" explanation because the ice cores show sulfate at both poles. Their explanation for the weak and patchy 1810 tree-ring cooling is internal variability, or a smaller sulfur load (Low run, about 12 Tg S, fits best). [text]
- **Later work does not change this.** No post-2021 tree-ring or model study found here names a hemisphere or latitude for 1809. Marshall et al. 2025 again find that all models cool the Northern Hemisphere too much in 1810 and suggest the SO2 amount is overestimated. Wilson et al. 2026 (preprint) date the event to 1808 from Patagonian tree rings and ice-core timing. [text]
- **ENSO 1808-1810: the sources disagree, and none supports an El Niño in the 1809 Java dry season.**
  - Tree rings (Li et al. 2013) and the multiproxy list (Gergis and Fowler 2009) say **La Niña** for 1808, 1809 and 1810.
  - The McGregor 2010 unified proxy is **near neutral**.
  - Quinn's Peru chronology lists **no El Niño** between 1806-07 and 1812.
  - Corals point the other way. Freund et al. 2019 and Claude's own composite of 18 Indo-Pacific corals both show **El Niño-like conditions from late 1808 to about May 1809**, already building before the eruption. By 1810 conditions are **neutral to La Niña-like**.
  - The Lombok coral is the nearest record to Batavia. It shows **normal conditions in Jul-Nov 1809**. [text, calc]
- **Batavia drought (Claude's inference):** the 1809 dry-season drought is not explained by a developing El Niño, since none appears in any source for mid-1809. Two readings remain open. (a) The coral El Niño of 1808/09 weakened the 1808/09 rains, so the early-1809 harvest was poor and rice was scarce from March 1809. (b) The 1809 dry season failed locally or for a non-ENSO reason, which could include the eruption's effect on the monsoon or Daendels's labour levies. The corals cannot tell these apart.

## 2. Timmreck, Toohey, Zanchettin, Brönnimann, Lundstad and Wilson 2021, Clim. Past 17:1455-1482 [text]

- **Model and ensembles.** MPI-ESM1.2-LR (ECHAM6.3 at T63, 47 levels), with aerosol from the EVA generator. Four forcing experiments of 10 members each, 40 runs in all:
  - **Best:** eVolv2k, 19.3 Tg S.
  - **High** and **Low:** ±2σ around Best (σ = 3.54 Tg S).
  - **nNHP ("no NH plume"):** the Best forcing with the aerosol north of the tropics removed. The authors call it an unlikely end-member.
  - Every run starts 1 Jan 1800 and includes Tambora from 1815. Peak global SAOD ranges from 0.17 (Low) to 0.33 (High), and is 0.21 in nNHP.
- **Latitude and season.** The eruption is placed "1 January 1809 located at the Equator" in every run. **No alternative latitude or season was simulated.** The paper says the season "has an impact on the climate response" and that Chenoweth's March-June 1808 date "should be addressed in further studies". It argues for a tropical source because cooling in the tropics after 1809 resembles that after Tambora.
- **Tree rings versus model.** Reconstructed NH summer 1810 anomalies are N-TREND(S) −0.87 °C, NVOLC −0.77, N-TREND(N) −0.21 and SCH15 −0.15. NH cooling persists until 1815 in all four, which the model does not reproduce (except partly in nNHP). N-TREND(S) shows a zonal "wave-2" pattern in 1809-10, unlike the even cooling after Tambora. The paper's finding is that "The NH mean summer temperature response to the 1809 eruption is smaller in tree-ring reconstructions" than in the simulations. Low and nNHP agree best. The spatial correlation with N-TREND is weak for the ensemble mean, but individual runs match North America and Europe well. Hence the abstract's line that the patchy 1810 cooling "could be due to internal climate variability".
- **Hemispheric asymmetry.** The nNHP run gives almost no NH extratropical cooling in the first four years, apart from Finland, Kola and western Alaska. The authors judge nNHP "an unlikely reason" for the muted NH response, because the ice cores show the aerosol spread to both poles. In all experiments, significant cooling south of 30°S appears only in austral spring 1809.
- **Tropics and corals.** The Low run fits the EEIC ship temperatures best for 1810-1812. The paper compares four regions with the Tierney et al. 2015 coral reconstructions:
  - **Eastern Pacific:** "not inconsistent" with the models, with high ENSO variability.
  - **Western Pacific:** only a weak signal.
  - **Western Atlantic:** warm, opposite to the models.
  - **Indian Ocean:** "no large cooling after 1809".
  - The D'Arrigo 2006 warm-pool record shows the clearest 1809 cooling.
- **ENSO.** Section 3 says the tropical SST records show "neutral to La Niña-like conditions in 1810" (citing Li 2013 and McGregor 2010). It attributes the delayed tropical cooling to an "overlaying El Niño signal" (D'Arrigo 2009). In the simulations, only High shows a significant El Niño-type anomaly in summer 1810. Using the relative-SST method of Khodri et al., all four experiments show one. In winter 1809/10, every experiment except Best has central Pacific warming.
- **Recommended future work.** Further modelling to narrow the forcing; more tree-ring density records in poorly sampled regions, including the Southern Hemisphere; transient CMIP6 runs. The source "remains unidentified".

## 3. Later work on the 1809 cooling pattern [text]

| Work | What it says about 1809 |
|---|---|
| Marshall et al. 2025, Clim. Past 21:161 (multi-model, SO2-based forcing) | "All models show a strong immediate NH summer cooling following the 1809 eruption, which is not reflected in the hemispheric-mean tree-ring reconstructions"; suggests SO2 for 1809 overestimated, or timing/identity. UKESM1 and CESM2 put the eruption in October, not January. Endorses Timmreck's point that removing NH-extratropical aerosol improves the fit. No latitude given. |
| Sanchez, Hakim and Saenger 2021, J. Climate 34:1863 (coral data assimilation, 1809-1830) | Most of 39 corals cool after 1809/1815. SW Pacific (SPCZ) corals give a warm, El Niño-like Niño-3.4 only because the model prior links SPCZ cooling to Niño-3.4 warming. Without them, "all proxy subregions, including the eastern Pacific, provide evidence for cool conditions in the Niño-3.4 region". Their conclusion is that it is "still not clear" that the eruptions caused an El Niño-like response. Urvina Bay (Galápagos) and Secas (Panama) are the eastern Pacific corals that span 1809; Palmyra is not used. |
| Wilson, Mundo, Marshall, Reid, Sigl et al. 2026, EGUsphere-2026-4785 (preprint, Northern Patagonia tree rings) | Treats the event as "Unknown", **actual year 1808**, VSSI 19.26 Tg S at 0° latitude. Superposed epoch analysis of the six largest events gives about −1 °C at T+1. Shifting 1808 to 1809 moves the peak cooling to T+0, which they call incompatible with the transport lag. This supports an 1808 eruption. Southern Hemisphere cooling is greatest at 25-30°S. Nothing specific to 1808 on asymmetry. |
| Leland et al. 2023, Paleoceanogr. Paleoclimatol. (already in B38) | Extreme 1810 cold centred on NW North America. |
| Burke et al. 2023, PNAS 120(47) | 1809 appears only as a point on its Fig. 2 (tree-ring cooling against stratospheric sulfur); no sulfur-isotope or latitude statement. |
| Higgins et al. 2022, Clim. Past 18:1169 (New Zealand tree rings) | Does not mention 1808/1809. |
| "A re-appraisal of the ENSO response to volcanism with paleoclimate data assimilation", Nat. Commun. 2022, doi:10.1038/s41467-022-28210-1 (authors not recorded here) | Mentions 1809 only via Sanchez: corals in SPCZ and Niño-3.4 regions cool after 1809 and 1815. |

No Guillet, Büntgen, Schneider or Esper paper after 2021 with a 1809-specific hemispheric result was found in these searches (WebSearch, standard and extended modes). This is a weak negative.

## 4. ENSO reconstructions for 1808-1810

Conventions differ, so years are given as each source labels them.

| Source | 1808 | 1809 | 1810 | Level |
|---|---|---|---|---|
| Gergis and Fowler 2009, Clim. Change 92, Table 9 (multiproxy, 1525-2002) | La Niña, very strong (7/10 proxies) | La Niña, strong (5/10) | La Niña, strong (5/10); 1811 also La Niña strong | text (PDF on author's site; table columns re-checked in a second extraction) |
| Li et al. 2013, Nat. Clim. Change (tree rings, Niño3.4 for NDJ before the labelled year, °C vs 1971-2000) | −1.16 (NDJ 1807/08) | −1.04 (NDJ 1808/09) | −2.14 (NDJ 1809/10) | text (data file enso-li2013.txt, LTRR mirror) |
| McGregor et al. 2010, Clim. Past (Unified ENSO Proxy, scaled) | −0.43 | −0.11 | 0.00 | text (NCEI data file) |
| Freund et al. 2019, Nat. Geosci. (27 corals; Niño Cold Tongue index NCT, seasonal) | MAM 0.13, JJA 0.31, SON 0.33, **DJF 1808/09 0.51** | **MAM 0.55**, JJA 0.37, SON 0.13, DJF 1809/10 0.15 | MAM 0.27, JJA −0.05, SON −0.16 | text (NCEI data file). For scale: DJF 1982/83 1.00, 1972/73 0.76, 1997/98 0.42 |
| Quinn and Neal 1992 (Peru documents) | no event (1806-07 M, conf. 3) | no event | no event (1812 M+, 1814 S) | text (Bradley 1992 database copy) |
| García-Herrera et al. 2008, J. Climate 21:1948 (N Peru documents) | year table is in suppl. Table S1, not read | – | the 1810s are among "the most active" decades | text (main article only) |
| Dätwyler et al. 2019, Int. J. Climatol. (multiproxy PC1) | not read: the fetch tool truncates the file at 1794 | – | – | – |

The Freund season convention was checked: DJF of year Y means Dec Y to Feb Y+1, which matches the 1982/83 and 1972/73 peaks.

## 5. Claude's coral composite (PAGES2k v2 corals) [calc]

- **Source.** PAGES2k v2 values as packaged in github.com/fzhu2e/cfr-data (`pages2kv2.json`). For the modern sign check: Bunge and Clarke 2009 monthly Niño3.4 from 1873 (`BC09_NINO34.csv`). NOAA Paleo is blocked from Claude's cloud container, so this mirror was used.
- **Coverage.** 18 Indo-Pacific coral series span 1804-1814:
  - Fiji: Savusavu 1F d18O and Sr/Ca, Savusavu AB, and Bagnato.
  - Tonga: Hafera Sr/Ca.
  - Rarotonga: Sr/Ca and d18O.
  - New Caledonia: Amédée Sr/Ca.
  - Vanuatu: Quinn 1996.
  - Palau, Guam (Double Reef), Lombok and Galápagos (Urvina Bay).
  - Great Barrier Reef: Abraham Reef.
  - Indian Ocean: Malindi, Ifaty, and Houtman Abrolhos (two series).
- **Gaps.** **Palmyra (Cobb/Emile-Geay 2013, Nurhati 2011) has no data for 1780-1840**, so Palmyra cannot answer the question. Kiritimati, Maiana, Nauru and Mentawai do not reach back to 1809 in this database. The GBR luminescence (Lough) series is not in it.
- **Method.**
  - Season series: Nov-Apr means for sub-annual records, labelled by the January year, so "1809" means Nov 1808 to Apr 1809. Annual records use the coral year as published.
  - The sign of each record's El Niño response comes from its correlation with NDJ Niño3.4 over 1873-1995 (r between −0.37 and +0.46).
  - High-pass anomaly: deviation from the 7-year centred mean, in SD units of the 1780-1840 residuals, signed so that + means El Niño-like.
- **Composite check.** Over 1874-1990 the composite correlates with NDJ Niño3.4 at r = 0.66. This is in-sample, because the signs were chosen on the same period.
- **Result.** Composite means by labelled year:

  | Year | Mean | Records > +0.5 | Records < −0.5 |
  |---|---|---|---|
  | 1806 | −0.40 | – | – |
  | 1807 | −0.35 | – | – |
  | 1808 | 0.00 | – | – |
  | **1809** | **+0.56** | 12 | 1 |
  | 1810 | +0.12 | – | – |
  | 1811 | +0.02 | – | – |
  | 1812 | −0.34 | – | – |

  1809 ranks 8th of 206 years in 1785-1990, about 2 SD on the pre-1870 spread. It holds without the SW Pacific corals: non-SW-Pacific mean +0.50 in 1809, then −0.24 in 1810 and −0.26 in 1811. The SW Pacific corals alone stay positive (+0.48) in 1810, which is the pattern Sanchez et al. explain as volcanic cooling, not ENSO.
- **Caveat.** The composite fails for the documented El Niño years. 1806-07 (Gergis and Fowler very strong and strong, Quinn moderate) comes out negative, and 1812 (Quinn M+) negative. So the early-1800s coral composite is not a dependable year-by-year classifier.
- **Lombok** (8.2°S 115.6°E, Charles et al. 2003). It is the closest coral to Java, about 1,000 km east of Batavia. Its Jul-Nov d18O tracks Niño3.4 (r = +0.41), and it shows the known El Niño or positive-IOD dry seasons of 1877, 1902, 1914, 1941, 1963 and 1972 as +1.1 to +2.2 SD. **Jul-Nov 1808 is −0.2 SD and Jul-Nov 1809 is 0.0 SD, both normal.** Jul-Nov 1812 is the largest anomaly in the record (+3.3 SD vs 1780-1840; +3.4 SD over the full record).

## 6. What this means for the Batavia drought [inference]

- The 5 Oct 1809 edict (Plakaatboek vol. 15 p. 912, page image) blames "the unusual drought of the season". Java's dry season runs about Jun to Oct. An ENSO-driven Java drought normally comes in the dry season of a *developing* El Niño. No source shows El Niño developing in mid-1809. The corals and Freund show one *decaying* through 1809, and the tree rings and Gergis show La Niña. Lombok is normal in Jul-Nov 1809. So **El Niño is an unlikely cause of the 1809 dry-season drought.**
- An 1808 El Niño, as the corals indicate, could instead explain **rice scarcity from March 1809**, through a late or weak 1808/09 rainy season and a poor first-crop harvest. Our Java sources do not settle this.
- A volcanic cause for the 1809 drought stays possible but untested. Large tropical eruptions weaken the Asian-Australian monsoon in the following year. This record cannot separate that from local variability or Daendels's labour levies.
- The coral El Niño-like signal starts by mid-1808 (Freund NCT JJA 1808 0.31). That is before the inferred Nov-Dec 1808 eruption, so the eruption did not trigger it.

## 7. Search log

| # | Source / query | Tool | Result |
|---|---|---|---|
| 1 | cp.copernicus.org/articles/17/1455/2021/ (HTML, two offsets) and PDF | WebFetch | Abstract, Sects. 2-4, Discussion, Conclusions summarised; HTML truncates at about 89k characters, PDF read for the rest |
| 2 | "1809 eruption tree-ring cooling hemisphere ..." (extended); "1809 El Niño reconstruction coral ..." (extended); "1809 ... Guillet OR Büntgen ..." (extended) | WebSearch | Wilson 2026 preprint, Higgins 2022, Marshall 2025, Nat. Commun. 2022 ENSO paper, Leland 2023 |
| 3 | Gergis and Fowler 2009 PDF (joellegergiscom.wordpress.com) | WebFetch | Table 9, two extractions |
| 4 | enso-li2013.txt (LTRR mirror), mcgregor2010uep-noaa.txt, freund2019enso.txt (NCEI, three reads) | WebFetch | values above |
| 5 | Quinn and Neal 1992 (paleo.ltrr.arizona.edu bradley1992/ch32.txt) | WebFetch | events 1795-1820 |
| 6 | García-Herrera 2008 (eprints.ucm.es, docta.ucm.es) | WebFetch | main text only; Table S1 not reached |
| 7 | Dätwyler 2019 RunningPC1.txt (LTRR and NCEI) | WebFetch | truncated at 1794; not read |
| 8 | Sanchez 2021 (repository.library.noaa.gov/view/noaa/44720 PDF) | WebFetch | read |
| 9 | Burke 2023 (par.nsf.gov 10566113); Marshall 2025 (cp 21:161); Wilson 2026 (egusphere-2026-4785) | WebFetch | read |
| 10 | git clone github.com/fzhu2e/cfr-data (pages2kv2.json, BC09_NINO34.csv) | Bash | 18 coral series analysed |
| 11 | Direct curl to NOAA, PANGAEA, Zenodo, Copernicus, figshare from Claude's cloud container | Bash | all refused by proxy (GitHub and PyPI only) |

## 8. Open items (optional, not essential)

- Dätwyler 2019 values for 1808-1810, and García-Herrera 2008 Table S1 entries for 1806-1812 (AMS supplement). Both are on William's Mac if wanted. See the curl block in the thread reply. NOAA reachability from the Mac is untested.
- The GBR luminescence (Lough 2011) and the D'Arrigo 2006 warm-pool series are not in PAGES2k. They would need NOAA.
- A Java-specific test: monthly rainfall-sensitive coral from Java or Bali for 1808-1809. None was found in PAGES2k besides Lombok.
- Archival route for the drought cause: register B57 (another thread, same day) lists Nationaal Archief 2.01.27.03 inv. 96, a 1809 report on the rice supply of Java. Its stated cause of the 1809 shortfall would test the readings in section 6 directly.
