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

# Bipolar sulfate lag and hemispheric ratio for 1809 (27 Oct 2026)

Thread "Calculate the bipolar sulfate lag for 1809" (William's lead 1 of 27 Oct 01:58). Register: B55. Script: `scripts/bipolar_lag_2026-10-27/lag.py`; numbers: `data/bipolar_lag_1809_2026-10-27.csv`.

**Access today.** Neither Claude's cloud container nor the Linux VM on William's Mac could download anything: PANGAEA, Copernicus, NOAA, Zenodo, Arctic Data Center and USAP-DC were all refused (the VM has no network at all this session). So no new raw series was downloaded. Everything below comes from published tables read through the web text reader, plus the NEEM 2 cm series William downloaded on 16 Oct. None of it is page-image checked. Values that overlap with the 26 Oct Antarctic sulfate map (Sigl 2013 and Plummer 2012 fluxes) agree exactly with what that thread read.

## Plain-language result

1. **The 1809 sulfate reached both poles at the same time, within the dating error.** Using the onset dates published for four sub-annually dated cores (WAIS Divide WDC06A, Law Dome DSS, NEEM-2011-S1, NGRIP), the Greenland-minus-Antarctica onset lag is **−0.05 yr on average (range −0.4 to +0.3 yr; about −0.6 ± 4 months)**. The same pairings give **+0.25 yr (−0.2 to +0.7) for Tambora** and **−0.7 yr (−1.0 to −0.4) for Krakatau**. Each single onset is uncertain by about ±3 months (Sigl 2013), so each lag by about ±4 months (Claude's calculation).
2. **What the lag says about latitude: only "tropical".** An extratropical eruption puts sulfate on its own ice sheet months to a year before the other one, or not at all. 1809 shows no such lead. That agrees with the Δ33S evidence that the sulfur was stratospheric (below) and with the standard view. But Tambora (8°S) and Krakatau (6°S) do not show a consistent sign either, so the lag cannot tell whether the source was north or south of the equator. **This does not tighten latitude beyond Cole-Dai 2009.** It does extend his result from three cores to four independently dated ones.
3. **The hemispheric split leans north compared with Tambora.** Greenland received relatively more of the 1809 sulfate than of Tambora's. Relative to Tambora, the north-to-south ratio for 1809 is 2.1 (NEEM/WDC06A), 2.2 (NGRIP/DSS), 1.47 (all 21 cores on the 26 Oct map), 1.36 (Cole-Dai 2009 means) and 0.93 (Gao 2007 means). So about 1.4 times, range 0.9 to 2.2 (Claude's calculation). Taking Tambora's composite ratio of 0.87 (Sigl 2015 via Marshall 2021: Greenland 39.7, Antarctica 45.8 kg/km²), 1809 would have a Greenland/Antarctica ratio of about 1.2 (0.8 to 1.9), with **about 55% of the deposited sulfate in the north (45 to 65%)**.
4. **What the ratio implies (inference).** In the models, more sulfate goes to Greenland when a tropical eruption happens in northern winter (Toohey et al. 2013, as summarised by Toohey 2014 and Marshall 2018). So a ratio somewhat above Tambora's fits **either** a source near or north of the equator **or** a December–January eruption at any tropical latitude. Toohey (2014) said the same about this ratio: possibly "a ∼6 month seasonal difference", but "a difficult argument". A northern-winter date is already independently likely (Bogotá veil by 11 Dec 1808). So the ratio does **not** rule out the southern candidates on our list (Dakataua 5°S, Gaua 14°S, Cabalían 10°N). An extra northern extratropical eruption in 1809-10 (the "several eruptions" hypothesis) would also raise the ratio. The ratio cannot tell these apart without a model run for the right season.
5. **Timing check on the eruption date (Claude's calculation, weak).** Take each core's delay from Tambora's eruption (10 Apr 1815) to its Tambora onset and apply it to its 1809 onset. That puts the eruption at **1809.07 ± 0.41 (about Jan 1809 ± 5 months)**. The Krakatau analogue gives 1809.28 ± 0.40. Cole-Dai's midpoints with the Tambora analogue give 1808.98 (Dec 1808). All three are consistent with an eruption in late 1808 and with the Bogotá veil. One tension: if the eruption was in early December 1808, the 1809 sulfate took about 4-5 months **longer** than Tambora's to reach both WAIS Divide (0.48 vs 0.13 yr) and NEEM (0.78 vs 0.33 yr). That fits a December eruption having to wait for the seasonal transport windows (deposition at both poles is locked to season), or a lower or smaller injection. It is an inference, not a measurement.

## Per-core table (all values from published tables; text read, not page images)

Onset and end are decimal years as published. Duration and peak are Claude's calculation or reading. "–" means not published in a form we could read.

| Core | Hemisphere | Dating | 1809 onset / end / duration | 1809 peak | Tambora onset / end | Krakatau onset / end | Source |
|---|---|---|---|---|---|---|---|
| WDC06A, WAIS Divide | S | annual layers, ~1 cm; tie points Krakatau, Tambora, Huaynaputina; fraction-of-year error ±0.25 | 1809.4 / 1812.1 / 2.7 yr | – | 1815.4 / 1818.4 | 1884.0 / 1886.4 | Sigl 2013 Table 1 |
| DSS, Law Dome | S | annual layers, 2.5 cm (8-10 samples/yr), δ18O summer max = 1 Jan; dated unambiguously to 1807 | 1809.7 / 1811.1 / 1.4 yr | – | 1815.8 / 1819.3 | 1884.5 / 1885.9 | Plummer 2012 Table 2 |
| SP01, South Pole | S | sub-annual layers, ±4 months | midpoint Jun 1810, 21 months long | – | midpoint about Jan 1817 | – | Cole-Dai 2009 Table 2 (William's PDF, text layer) |
| WDC (Cole-Dai) | S | sub-annual layers, ±4 months | midpoint Jul 1810, 22 months | – | midpoint about Oct 1816 | – | same |
| NEEM-2011-S1 | N | annual layers; ±0.25 yr fraction | 1809.7 / 1811.2 / 1.5 yr | – | 1815.6 / 1817.6 | 1883.6 / 1886.3 | Sigl 2013 Table 1 |
| NEEM-2011-S1, 2 cm (our reading of the raw series) | N | same timescale | rise 1809.6-1809.7; crosses 95th percentile 1809.82 | **1810.36-1810.43 (spring 1810)**, second max 1810.96 | crosses 1815.87-1815.96; peak 1816.26 | – | PANGAEA 940553, notes/scientific_data_round6.md R4 (computed from data) |
| NGRIP | N | GICC05 layers (as used by Plummer) | 1809.3 / 1811.8 / 2.5 yr | – | 1816.1 / 1817.9 | 1883.5 / 1886.2 | Plummer 2012 Table 2 |
| SU07, Summit | N | sub-annual layers, ±4 months | midpoint Sep 1810, 17 months | – | midpoint about Sep 1816 | – | Cole-Dai 2009 Table 2 |

The NEEM 2 cm series (onset 1809.6-1809.7) agrees with Sigl's published NEEM-S1 onset of 1809.7. That is a useful cross-check, because it is the same core read two ways.

NGRIP's 1809 onset (1809.3) is earlier than NEEM's (1809.7), although the NEEM 2 cm series shows a clean winter 1808/09. NGRIP's Tambora onset (1816.1) is also the latest of all four cores. NGRIP is probably the coarsest of the four, so the NGRIP pairings are the least reliable (inference).

Durations are not consistent between cores (1809: 1.4 to 2.7 yr; Tambora 1.8 to 3.5 yr). So the "short NEEM deposition" noted in nonvolcanic_alternatives.md is not by itself evidence of a second eruption.

## Lag calculations (Claude's calculation; data/bipolar_lag_1809_2026-10-27.csv)

Greenland minus Antarctica, in years (+ = Greenland later):

| Pair | 1809 | Tambora | Krakatau | 1809 minus Tambora |
|---|---|---|---|---|
| NEEM-S1 − WDC06A (onset) | +0.3 | +0.2 | −0.4 | +0.1 |
| NEEM-S1 − DSS (onset) | 0.0 | −0.2 | −0.9 | +0.2 |
| NGRIP − WDC06A (onset) | −0.1 | +0.7 | −0.5 | −0.8 |
| NGRIP − DSS (onset) | −0.4 | +0.3 | −1.0 | −0.7 |
| **Mean of onset pairs** | **−0.05** | **+0.25** | **−0.70** | |
| SU07 − SP01 (midpoint) | +3 mo | −4 mo | – | +7 mo |
| SU07 − WDC (midpoint) | +2 mo | −1 mo | – | +3 mo |

Uncertainty: ±0.25 yr per onset (Sigl 2013 footnote), so about ±0.35 yr per pair; ±4 months per midpoint, so about ±6 months per midpoint pair. The four onset pairs share cores, so they are not independent. Absolute layer-count errors near 1809 are small for WDC06A and NEEM, which are tied to Tambora 6 years later, and for DSS, which is "unambiguous" to 1807.

Krakatau: NEEM and NGRIP onsets (1883.6, 1883.5) come at or before the eruption (27 Aug 1883 = 1883.65). So for a small signal the published "onset" can be early by a few months. This is a warning against reading too much into any single lag.

## Hemispheric ratio (Claude's calculation)

| Basis | 1809 NH/SH | Tambora NH/SH | Krakatau NH/SH | 1809 relative to Tambora |
|---|---|---|---|---|
| NEEM-S1 / WDC06A (Sigl 2013) | 30.6/33.8 = 0.91 | 39.0/88.6 = 0.44 | 18.5/11.2 = 1.65 | 2.06 |
| NGRIP / DSS (Plummer 2012) | 38.6/24.6 = 1.57 | 40.3/57.2 = 0.70 | 15.4/16.8 = 0.92 | 2.23 |
| Gao 2007 Table 2 hemispheric means (NH 11 cores, SH 17 for 1809) | 28/26 = 1.08 | 59/51 = 1.16 | 11/11 = 1.00 | 0.93 |
| 26 Oct map: Greenland mean 1809/Tambora 0.70 vs Antarctica 0.475 | – | – | – | 1.47 |
| Cole-Dai 2009: 0.61 vs 0.45 | – | – | – | 1.36 |

Gao 2007 is the outlier, partly because its Tambora Greenland mean (59, 22 cores) includes high-accumulation southern Greenland sites such as Dye 3. eVolv2k (Toohey & Sigl 2017) gives 19.3 Tg S for 1809 against 28.1 for Tambora, averaging the two ice sheets equally. It treats 1809 as tropical because the signals are synchronous. It uses no ratio-to-latitude rule (tropical band ±25°), and its supplement gives no per-hemisphere 1809 fluxes in the text we could read. Marshall et al. 2021 (JGR 126, e2020JD033578), the emulator study, did **not** include 1809. Its eight events are 44 BCE to 1458 plus Tambora. So no published emulator constraint on 1809 latitude exists. Lin et al. 2022 (Clim. Past 18:485) classify only into broad bands (>40°N, 40°N-40°S, >40°S).

## Sulfur isotopes (recorded; nothing new published since 16 Oct as far as found)

- **Gautier et al. 2019** (Nat. Commun. 10:466; Dome C; data PANGAEA 895169, rows read 16 Oct through the text tool): Δ33S **+0.19 ± 0.05‰ at 1809.7**, +0.05 ± 0.03 at 1811.9, **−0.23 ± 0.13‰ at 1813.7**. Samples are about 1.5 years each, so they cannot time the arrival. The positive-then-negative sequence is the stratospheric pattern (negative only about 2σ). The ages are Dome C's own and run late. The article text does not discuss 1809 (checked today).
- **Burke et al. 2019** (EPSL 521:113; accepted manuscript read today): **1809 was not measured.** The cores were Tunu2013 (Tambora, Samalas, Katmai) and B40 (Samalas only), at 2-3 cm, "up to bi-monthly resolution". Their test is useful for 1809. In tropical eruptions (Samalas, Tambora) the Δ33S maximum comes "at the very start of the sulfate deposition" (about 1.7-1.9‰). In the extratropical Katmai the first sulfate has Δ33S ≈ 0. **A Burke-style profile through 1809 in Tunu or B40 would be the cleanest latitude test available.** It has not been published.
- **Burke et al. 2023** (PNAS 120: e2221810120): covers the 540s, 1450s and 1600s, not 1809.
- **Cole-Dai et al. 2009**: Summit early +0.18‰, late −0.12‰ (stratospheric). Dome C and South Pole bulk samples show no anomaly (+0.10 ± 0.17, 0.003 ± 0.12). Lanciki 2010 (thesis, abstract only): Greenland +0.18/−0.11‰.
- **Hutchison et al. 2023-24** (abstracts only): 1809 Δ33S "more complex time-evolving pattern suggestive of multiple eruptions". Innes et al. EGU25-20238 and Hutchison et al. 2025 (PNAS, Zavaritskii 1831) do not mention 1809. Innes's 2024 thesis data are embargoed to 2029 (see B56).

## Verification levels

- Sigl 2013 Table 1, Plummer 2012 Tables 1-2, Gao 2007 Table 2, Marshall 2018 Table 5, Marshall 2021 Table 1, Burke 2019 text: **fetched text of open PDFs, not page images.** Sigl and Plummer fluxes match the 26 Oct reading exactly.
- Cole-Dai 2009 midpoints: PDF text layer of William's copy (22 Oct). The Tambora midpoints are back-calculated from the stated mean offsets (77 months Antarctica, 72 Greenland) and the per-core lags in notes/papers_downloaded_2026-10-22.md.
- NEEM 2 cm: **computed from the raw data** (16 Oct).
- Dome C Δ33S: PANGAEA rows through the text tool.
- All lags, ratios and analogue dates: **Claude's calculation**, with the uncertainties stated above.

## What needs William's hands (suggestions)

The Mac's own Terminal or Safari is needed. This session's VM had no network.

1. **WDC06A sub-annual sulfate 1800-1820** (Sigl et al. 2013). Look for it at the Arctic Data Center (doi:10.18739/A2TH15, as noted 16 Oct) or the USAP-DC search for "WDC06A sulfur". This would let us read the 1809 onset month and peak in Antarctica the same way as NEEM, instead of using the ±3 month table value. It is the most useful single download for this question.
2. **Law Dome DSS 2.5 cm sulfate** (Plummer 2012): NOAA Paleo, search "Law Dome volcanic sulfate Plummer". Same purpose, second Antarctic core.
3. **Cole-Dai et al. 2009 supporting information** (Text S1, Table S1; free on the AGU/Wiley article page): onset months for SP01, WDC and SU07.
4. **Sigl et al. 2015 Nature, Extended Data Table 4 / source data** (free on nature.com): NH and SH composite fluxes for 1809 and Tambora, the inputs the eVolv2k split rests on.
5. **Marshall et al. 2018 ACP supplement Table S1** (acp.copernicus.org/articles/18/2307/2018/): monthly D4 (Greenland) and DIV2010 (WAIS Divide) Tambora timing. It is the best published monthly analogue.
6. **Toohey, Krüger & Timmreck 2013, JGR 118:4788** (paywalled; Le Moyne ILL): model Greenland/Antarctic ratio for January vs July eruptions. Needed before the ratio argument in point 4 can be made quantitative.
7. Optional: Lanciki 2010 thesis full text (SDSU), for the Greenland Δ33S sample depths and dates.

## Suggested next steps (suggestions)

- With items 1-2, compute the onset month in WDC06A and DSS from raw data, using the same 95th-percentile rule as NEEM. That would reduce the lag uncertainty from about ±4 to about ±2 months.
- A Δ33S profile through 1809 at bi-monthly resolution (Tunu2013/B40, Burke method) would settle tropical vs extratropical. It exists only as unpublished St Andrews work. William decides whether to contact anyone; no letter has been drafted.
