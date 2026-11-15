---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: science_alternatives
date: 2026-10-28
---

# Does the Greenland/Antarctic sulfate ratio give a latitude band? Validation of the B62 emulator band, and EVA_H runs (28 Oct 2026)

Thread "Finish the ice-deposition latitude band" (option 1 of notes/creative_next_steps_2026-10-28.md, B62). Register section B66. Scripts: `scripts/deposition_validation_2026-10-28/`. Data: `data/deposition_ratio_validation_2026-10-28.csv`, `data/deposition_ratio_of_ratios_vs_tambora_2026-10-28.csv`, `data/evah_deposition_ratio_grid_2026-10-28.csv`, `data/evah_saod_timing_2026-10-28.csv`, `data/evolv2k_v2.1_events_2026-10-28.csv`. Labels as in B62: **[calc]** Claude's calculation from downloaded published data; **[text]** fetched text of a paper or data file, not checked against a page image; **[memory]** from training, not verified; **[speculation]** an idea. Every number below is Claude's calculation unless a source is named.

## 1. Result in six lines

1. **The provisional band of B62 (about 12°S-3°N for a November-December eruption) is withdrawn.** Tested against eleven eruptions of known latitude and month, the Marshall et al. 2021 deposition emulator predicts their Greenland/Antarctic ratios with a root-mean-square error of a factor 3.0 (factor 2.1 after removing its mean bias of ×2.3 towards Greenland), and its predictions do not correlate with the observed ratios (Spearman 0.20, p = 0.55; Pearson 0.35, p = 0.29) [calc]. The contrast it predicts across the whole B62 band (×1.7 between 10°S and 2°N for a December eruption) is smaller than its own error.
2. By the test B62 itself set ("if the calibrated emulator reproduces the ratio-of-ratios of Huaynaputina, Parker, Cosigüina and Krakatau within a factor of 1.5, the band stands; if not, it falls"), one of the four passes (Parker, 1.04) and three fail (Krakatau 2.1, Cosigüina 3.2, Huaynaputina 3.4) [calc].
3. **The observed ratios show no latitude dependence inside the tropics.** Across the eleven eruptions between 16.6°S and 15.1°N the fitted slope is ×1.13 per 10° of latitude northward (p = 0.5), or ×1.06 (p = 0.7) once season is allowed for; the scatter between eruptions is a factor 1.8 [calc]. Cosigüina (13°N, January 1835) and Huaynaputina (16.6°S, February 1600) have the same ratio, 2.0, on the eVolv2k basis.
4. **What the ratio does carry is season.** Eruptions of October-February put about twice as much sulfate on Greenland, relative to Antarctica, as eruptions of March-June (fitted amplitude ×2.0 about the mean, peak in late October-November, p = 0.04 for the sine term, n = 11) [calc]. The emulator has the sign right (January/July factor 2.5 at 8°S) but places the latitude gradient on top of it, and that gradient is not in the ice cores.
5. **EVA_H cannot arbitrate.** With its default parameters, and with its optional seasonal mixing switched on, it gives a NH/SH deposition ratio of 1.00 ± 0.01 for any eruption between 15°S and 15°N in any month and at any injection height, because it treats the tropics as a single well-mixed reservoir; its sensitivity begins at ±20° (0.79 at 20°S, 1.27 at 20°N) [calc].
6. **Consequences.** The quantitative argument against Cabalían (10°N) in B62 is withdrawn; the hemispheric ratio excludes only extratropical sources (|latitude| above about 20°), which B55 had already said. The B53 priority list is unchanged by this thread. One loose end survives (section 6): the 1809 ratio (1.3 on the eVolv2k basis, 0.9-1.3 across four bases) is the lowest of the five October-February eruptions on record (the others: 2.0, 2.0, 2.4, 2.8), which with four analogues and factor-1.6 residual scatter is not significant.

## 2. What was asked and what was done

Option 1 said: run EVA_H for the December 1808 scenarios; when the eVolv2k supplement (U36) is on the Mac, validate the calibrated emulator with Huaynaputina, Parker, Cosigüina and Krakatau; publish the band with its uncertainty.

- **EVA_H** (Aubry et al. 2020, JGR 125, e2019JD031303 [memory for the reference]; Python port in GitHub thomasaubry/EVA_H) was re-cloned and run in Claude's cloud container: 264 deposition-proxy runs (11 latitudes × 4 heights × 3 eruption months × 2 mixing variants) and 7 SAOD-timing runs (section 7).
- **The eVolv2k supplement does not contain what B62 said it did.** Both the preprint supplement (essd-2017-31-supplement.pdf) and the final one (essd-9-809-2017-supplement.pdf, 13 pages) were read as text on 28 Oct: Table S1 is ice-core metadata, Tables S2-S4 match event years between eVolv2k, ICI and IVI2; there are no per-event fluxes and no ratios [text]. The B62 sentence "Tables S2/S4 list composite Greenland and Antarctic fluxes for every event" came from memory and was wrong. The paper itself (p. 814) says the per-event ratio R of Greenland to Antarctic deposited sulfate is part of the database, and the WDCC entry for `eVolv2k_v3_ds` lists the variable "hemispheric asymmetry of aerosol spread (NH/SH)" with year, month, day, latitude and VSSI [text]. The v3 file needs a free WDCC login (now U125). A copy of **v2.1** (`eVolv2k_v2.1_ds_1.nc`, 271 events, committed 2 Nov 2017) sits in the Easy Volcanic Aerosol repository on GitHub (matthew2e/easy-volcanic-aerosol), which Claude's cloud container can clone; its `hemi` variable is defined as "hemispheric asymmetry (NH/SH) of aerosol spread for tropical eruptions based on ratio of Greenland to Antarctic flux". The v3 change notes list only minor events (1654, 1414, 1381, 688, 379, 430 BCE, 1463, 190 BCE), none used here. So the validation did not have to wait for human hands, and U36 is superseded.
- **Three further bases for the observed ratios** were fetched as text, to see how much a single eruption's ratio depends on which cores are used: Crowley & Unterman 2013 (ESSD 5:187) 30-90°N and 30-90°S composites, per event, from the NOAA files `crowley2013so4-nh.txt` and `-sh.txt`; Sigl et al. 2013 (JGR 118:1151) Table 1, the single-core pair NEEM-2011-S1 / WDC06A; Gao et al. 2007 (JGR 112, D09109) Table 2 hemispheric means (only 1259, 1452, 1809, 1815, 1883, and 1963 and 1991 for Antarctica alone).
- **Marshall et al. 2021** (JGR 126, e2020JD033578) was read in full as text from the White Rose eprint. Two facts matter here. Their design: 82 UM-UKCA runs (41 starting 1 January, 41 starting 1 July), SO2 10-100 Tg, latitude 80°S-80°N, plume base 15-25 km, easterly QBO, year-2000 background, Gaussian-process emulators with noise terms of 10 (Greenland) and 2.5 (Antarctica) kg/km². Their own blind inversion of Tambora: January solutions lie at 22-56°S, July solutions at 6-62°S; "if restricted to Tambora's latitude (8°S), only July eruptions fit, with SO2 above about 97 Tg" [text]. In other words the published emulator cannot recover Tambora's latitude and season from its deposition; this is the bias B62 found independently.
- **The emulator's ratio depends on mass, and its Greenland values go negative for small July eruptions** (for 10-20 Tg SO2 at 10°S in July the mean Greenland deposition is −4.8 kg/km²) [calc]. At 10.5°S in January the median ratio is 0.35 for 10-20 Tg, 1.8 for 20-35, 2.2 for 35-60 and 2.8 for 60-100 Tg. Six of the eleven test eruptions (9-19 Tg SO2 in eVolv2k) fall below the range where the emulator is usable, so all predictions below are made at a fixed 35-60 Tg window, the range of 1809 (38.5 Tg SO2 from 19.3 Tg S) and Tambora (56 Tg); predictions at each event's own mass are given in the CSV where the mass is 20 Tg or more and differ by less than 10 %. Month weighting: log-linear between the January and July emulators with weight (1 + cos 2π(m−1)/12)/2, so 1 December carries 0.93 of January; this is a convention, not something the emulator provides.

## 3. The validation set

Eruptions with a known source latitude and month that appear in both ice sheets, taken from the eVolv2k event list (dates and latitudes [text]). R = Greenland/Antarctic ratio. "geomean" = geometric mean of the available bases. Emulator R = Marshall 2021, fixed 35-60 Tg SO2, month-weighted, medians over injection height.

| Eruption | Date | Lat | SO2 Tg (eVolv2k ×2) | R eVolv2k | R Crowley | R Sigl13 pair | R Gao07 | R geomean | Emulator R | Emulator ÷ observed |
|---|---|---|---|---|---|---|---|---|---|---|
| Huaynaputina | 17 Feb 1600 | 16.6°S | 38 | 2.0 | 3.27 | 1.27 | – | 2.02 | 1.29 | 0.64 |
| Ruiz | Mar 1595 | 4.9°N | 18 | 0.8 | – | – | – | 0.80 | 5.12 | 6.4 |
| Parker | 26 Dec 1640 | 6.1°N | 37 | 2.8 | (SH composite has no signal) | 3.77 | – | 3.25 | 7.36 | 2.3 |
| Gamkonora | 20 May 1673 | 1.4°N | 9 | 0.7 | 1.96 | 0.56 | – | 0.91 | 2.04 | 2.2 |
| Tambora | 10 Apr 1815 | 8.25°S | 56 | 0.8 | 0.62 | 0.44 | 1.16 | 0.71 | 1.54 | 2.2 |
| Cosigüina | 20 Jan 1835 | 13.0°N | 19 | 2.0 | 1.70 | 0.87 | – | 1.43 | 10.0 | 7.0 |
| Makian | 28 Dec 1861 | 0.3°N | 9 | 2.4 | 0.88 | 2.72 | – | 1.79 | 4.95 | 2.8 |
| Krakatau | 27 Aug 1883 | 6.1°S | 19 | 1.7 | 1.48 | 1.65 | 1.00 | 1.43 | 1.46 | 1.0 |
| Samalas | Jul 1257 (May-Oct) | 8.4°S | 119 | 1.4 | 1.36 | 1.03 | 1.30 | 1.27 | 1.05 | 0.83 |
| Agung | 17 Mar 1963 | 8.3°S | – | – | – | 0.44 | – | 0.44 | 1.84 | 4.2 |
| Pinatubo (+ Hudson) | 15 Jun 1991 | 15.1°N | – | – | – | 1.46 | – | 1.46 | 3.89 | 2.7 |
| Colima (outside ±17°) | 10 Jan 1585 | 19.5°N | 17 | 10.6 | – | – | – | 10.6 | 12.1 | 1.1 |
| **Unknown 1809** | assigned 1 Jan 1809 | ? | 38 | 1.3 | 1.21 | 0.91 | 1.08 | 1.12 | – | – |

Notes on the rows. Crowley's 1595 and 1861 matches are uncertain (his NH and SH event ages differ by one to three years); his SH composite has no 1641 signal at all. The Sigl 2013 Agung value for NEEM is 7.2 ± 7.6 kg/km², at noise level and overlapping Surtsey; the 1991 Antarctic value includes Cerro Hudson (August 1991, 46°S), so the true Pinatubo ratio is higher than 1.46. The eVolv2k `hemi` values are given to one decimal. The Sigl 2013 values were read through a text extractor; the 1809, 1815 and 1883 rows match what B55 read, and the Huaynaputina, Parker, Cosigüina, Krakatau and Samalas rows were returned twice identically, but the column assignment of the modern rows (Agung, Pinatubo) is the extractor's reading and should be checked against the page.

**How much does one eruption's ratio depend on the cores used?** Tambora 0.44-1.16 (×2.6 between bases), Huaynaputina 1.27-3.27 (×2.6), Gamkonora 0.56-1.96 (×3.5), Makian 0.88-2.72 (×3.1), Cosigüina 0.87-2.0 (×2.3), Krakatau 1.0-1.7 (×1.7), Samalas 1.03-1.40 (×1.4), Parker 2.8-3.8 (×1.35), and 1809 itself 0.91-1.30 (×1.4) [calc]. The "measurement" of a ratio is therefore itself uncertain by a factor of about 1.5-3, and the emulator's whole latitude signal across the B62 band (×1.7) is of that size.

## 4. Emulator skill

Eleven eruptions within ±17° (Colima excluded), observed R = geometric mean of bases [calc]:

| Measure | Raw emulator | After removing the mean bias |
|---|---|---|
| Mean error | ×2.27 too much Greenland | – |
| RMS error | ×3.03 | ×2.11 |
| Within ×1.5 / ×2 / ×3 | 2 / 3 / 8 of 11 | 5 / 6 / – of 11 |
| Correlation log(predicted) vs log(observed) | Pearson 0.35 (p 0.29), Spearman 0.20 (p 0.55) | same |

The emulator's own predicted range for these eleven eruptions is ×12 (1.05 for Samalas to 10.0 for Cosigüina); the observed range is ×7 (0.44 to 3.25), and the two orderings do not match. The Tambora-calibrated ratio-of-ratios (the B62 method) fares no better: factors of 1.04 (Parker), 1.03 (Gamkonora), 1.23 (Pinatubo), 1.27 (Makian), 1.9 (Agung), 2.1 (Krakatau), 2.6 (Samalas), 2.95 (Ruiz), 3.2 (Cosigüina), 3.4 (Huaynaputina). The four that pass are the two December eruptions near the equator, the May eruption at 1.4°N and the June eruption at 15°N; the clear failures are the two southern-summer eruptions far from the equator (Huaynaputina, 16.6°S in February, which the emulator makes the most Antarctic-heavy case and the ice cores make Greenland-heavy) and the January eruption at 13°N (Cosigüina, predicted 6.5 times Tambora's ratio, observed 2.0 times).

Where does the emulator go wrong? Not in a single direction that a calibration could fix: it is too Greenland-heavy for Cosigüina (13°N), Parker (6°N), Ruiz (5°N), Makian (0°), Tambora (8°S), Agung (8°S) and Pinatubo (15°N), about right for Krakatau and Samalas (July-August, 6-8°S), and too Antarctic-heavy for Huaynaputina (16.6°S). The latitude gradient it imposes within the tropics (×1.7 per 5° near the equator for a December eruption: 2.1 at 10°S, 3.1 at 5°S, 4.5 at 0°, 6.4 at 5°N, 8.5 at 10°N) is absent from the data. The most likely reasons, in the authors' own description of the design [text]: two seasons only, one QBO phase, a year-2000 background atmosphere, three-year runs, and Gaussian-process noise terms (10 kg/km² for Greenland) comparable to the signals of the smaller eruptions. None of this is a criticism of the emulator for its stated purpose (forcing uncertainty for the largest eruptions); it is simply not accurate enough for the ratio inversion B62 tried.

## 5. The 1809 inversion anyway, for the record

If one insists on using the emulator, corrected by its mean bias and with its residual scatter (×2.1) and the 1809 ratio's own spread (×1.3) as the error, a December eruption with R = 1.3 gives a most probable latitude of 5°S, a 68 % interval of 16°S-10°N and a 95 % interval of 26°S-26°N; the probability of a source north of 8°N is 0.18 and south of 12°S 0.26. With R = 1.1 (the mean of the four bases) the mode is 8°S, 68 % 19°S-6°N, P(north of 8°N) = 0.13 [calc]. The raw, uncorrected emulator puts the mode at 17-20°S, as B62 found. The model-free view (section 1, point 3) is flat across the tropics. So the most that can be said is a weak lean towards the southern tropics that rests on a model which failed its validation. It should not be used to rank candidates.

## 6. The seasonal signal, and where 1809 sits in it (observation, weak)

Observed ratios (geometric mean of bases) by eruption month [calc]:

| Month of eruption | Eruptions and R |
|---|---|
| December-February | Parker (Dec) 3.25, Makian (Dec) 1.79, Cosigüina (Jan) 1.43, Huaynaputina (Feb) 2.02; also Colima (Jan, 19.5°N) 10.6 |
| March-June | Ruiz (Mar) 0.80, Agung (Mar) 0.44, Tambora (Apr) 0.71, Gamkonora (May) 0.91, Pinatubo (Jun) 1.46 |
| July-August | Samalas (Jul) 1.27, Krakatau (Aug) 1.43 |
| **1809 (assigned 1 Jan; our date late Nov-early Dec 1808)** | **1.12 (0.91-1.30)** |

The fit in section 1 puts the peak of R in late October-November and the trough in late April-May, amplitude ×2 about the mean. Physically this is the expected direction: an eruption in northern autumn or winter injects into a stratosphere whose winter-hemisphere wave-driven transport carries aerosol northward, and Marshall 2021's model has the same sign [text]. On the eVolv2k basis alone the four dated October-February tropical eruptions have R = 2.0, 2.0, 2.4 and 2.8, and 1809 has 1.3. Readings, none of them findings: (a) noise, since the between-basis spread for a single eruption reaches ×2.6 and the residual scatter of the fit is ×1.6; (b) an eruption whose plume rose into a different QBO phase or height than the four analogues; (c) an eruption earlier than late November (September-October 1808 would be at the seasonal peak of R, so that does not help) or, less plausibly against the Bogotá date, later. This is worth keeping as a loose end for the synthesis, not as evidence. A larger test is possible: the eVolv2k file has 16 tropical events between 1500 and 1900 with a `hemi` value, but only the nine dated ones are usable; Sigl 2015's per-event fluxes with uncertainties (U126) would let the fit be weighted properly [suggestion].

## 7. EVA_H runs

**Deposition proxy.** EVA_H's loss terms from boxes 7 (lowermost stratosphere, south of 25°S), 5 (tropical lower stratosphere) and 8 (north of 25°N) are the only fluxes to the troposphere, so their time integrals were used as the extratropical-south, tropical and extratropical-north deposition. Scenarios: 19.3 Tg S (the eVolv2k 1809 VSSI), eruption on the first of December, June or April, latitudes 20°N to 30°S in 5° steps, injection heights 18, 22, 26 and 30 km, default parameters (no seasonal cycle of mixing, as the authors recommend) and the optional 20 % seasonal mixing cycle given in the code comments (southern mixing fastest in July, northern in January). Proxy background injections off, so the ratios are pure eruption signal; the model is linear in mass, so they do not depend on the 19.3 Tg S.

NH/SH extratropical deposition ratio, December eruption, default parameters (18 km / 22-30 km) [calc]: 20°N 1.42 / 1.27; 15°N 1.05 / 1.03; 10°N 1.003 / 1.002; 5°N to 5°S 1.000; 10°S 0.997 / 0.998; 15°S 0.95 / 0.97; 20°S 0.71 / 0.79; 25°S 0.34 / 0.46; 30°S 0.14 / 0.25. June and April eruptions: identical to three decimals. With the seasonal mixing cycle on, December values change by less than 1 % between 10°S and 10°N (0.992-0.997) and April values by up to 3 % (1.02-1.03). The reason is structural: the injection is split between the three latitude bands by a Gaussian of 7° width about the volcano, so anything inside ±15° goes almost entirely into the tropical boxes, which then feed both hemispheres through identical mixing timescales (10.2 months). EVA_H was built to reproduce global and hemispheric optical depth from 1979-2015 satellite data, and in that record it has no eruption whose hemispheric split it needed to resolve.

**SAOD timing.** For a 1 December eruption of 19.3 Tg S at 26 km the model's peak global SAOD at 550 nm is 0.21 (0.19 at 20 km), reached ten months after the eruption; Tambora (28.1 Tg S) gives 0.26 and Krakatau (9.5 Tg S) 0.11. SAOD at the latitude of Edo (37.5°N grid point) reaches 10 % of its peak in the first month and half of it in month 4, Europe (52.5°N) in months 2 and 5; the outputs for sources at 5°S, 10°N and 10°S are identical. The model's extratropical peak SAOD is 11 % higher in the north than in the south for every scenario, including Tambora, which comes from its climatological shape functions rather than from the eruption. Because the model has no transport delay within a box and the shape functions spread the tropical boxes' aerosol into the subtropics instantly, it cannot be used for the first-appearance timing that option 3 (Krakatau analogue) addresses. Full tables in `data/evah_saod_timing_2026-10-28.csv`.

## 8. Verification levels and caveats

- Observed ratios: all from fetched text (data files and PDFs), none from page images. eVolv2k values are from the v2.1 file, rounded to one decimal; v3 not seen (U125). Sigl 2013 extraction caveat as in section 3. Crowley matches for 1595 and 1861 are uncertain. Gao 2007 covers only three of the test eruptions.
- Emulator: used exactly as published (JSON grid of the GitHub release); the 35-60 Tg window, the month weighting and the use of medians over injection height are this thread's conventions. The emulator's authors never claimed sub-tropical latitude resolution; their own Tambora inversion shows the same problem.
- Statistics: eleven points, several of them with a single noisy basis; the latitude slope's confidence interval (±0.03 per degree) still admits a factor of up to 1.7 per 10° in either direction. The claim is not "there is no latitude effect" but "no latitude effect is detectable at the precision of the ice cores, and the emulator's steep effect is contradicted".
- EVA_H: the proxy integrates fluxes to the troposphere over 72 months with background off; the 25° box boundary and the 7° plume width are the published defaults.

## 9. Housekeeping

- unavailable_sources.md: U36 set to superseded (reason above; data obtained from the GitHub copy); U125 added (eVolv2k v3 file at WDCC, free login, yield L); U126 added (Sigl 2015 Supplementary Information and Source Data on nature.com, Safari, yield M). U37 (Krakatoa report PDF for option 3) unchanged; a Terminal block for it, for the ESSD supplement PDF and for a Mac copy of the eVolv2k v2.1 file was posted in the thread.
- Register B66 summarises this note. findings.csv not changed (this note removes a provisional argument rather than adding a finding; if William wants the withdrawal recorded there, a one-line entry "F22: hemispheric sulfate ratio does not resolve latitude within the tropics" is the suggestion).
- The B62 note is left as written; its section 2.1 should be read with this note. The synthesis and candidate list (B53) need no change beyond deleting any use of the "12°S-3°N" band and the sentence excluding Cabalían.

## 10. Suggestions (labelled as such)

1. Drop the deposition ratio from the latitude argument in the write-up; keep "tropical, |lat| below about 20°" from the bipolar synchrony (B55) and from the EVA_H and emulator edges, which agree on that much.
2. The only ice-core route left to latitude is tephra chemistry (B56: unanalysed glass in the Japanese H15 core, SPICEcore particles below 2 µm, researcher-held glass U90-U92).
3. If the seasonal signal of section 6 interests William, the test is cheap once U126 is on the Mac: weighted fit of ln R on season for all dated tropical eruptions in Sigl 2015, then where 1809 sits.
