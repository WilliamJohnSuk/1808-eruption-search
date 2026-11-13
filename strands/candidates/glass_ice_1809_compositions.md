---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: candidates
date: undated
---

# Ice-core volcanic glass for the 1809 sulfate event (c. 1808–1811): published compositions

Compiled 22 Oct 2026 (desk search, subagent). CSV: `data/glass_ice_1809.csv`.
All values are wt%, mean (1 SD). n.r. = not reported; "not found" = the paper has a value but I could not read it from here.

**How the numbers were read.** Claude's cloud container network access was blocked, so I read the PDFs through a web-fetch tool that summarises them. Where a table came back, I checked it by arithmetic:
- Yalcin 2006 Table 1 rows each sum to 100.00.
- Palais 1990 is a scanned PDF, and its OCR scrambles the column order in some rows. I only accepted its numbers where they agree with Yalcin's renormalised copy (Palais × 0.991).

"PDF table" below means read from the publication's table in this way. "Secondary" means taken from a project note, an abstract or a web page.

## 1. Glass populations

| # | Core / layer | Depth, age | n (analyses / particles) | SiO2 | TiO2 | Al2O3 | FeOt | MnO | MgO | CaO | Na2O | K2O | P2O5 | Cl | Normalised? | Class | Source, table | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | **Eclipse Icefield, Yukon** (2002 core) | depth not given; 1809 by layer counting (Laki/Tambora sulfate control) | 10 / 10 | 64.86 (1.10) | 1.15 (0.20) | 16.13 (0.66) | 3.84 (0.71) | n.r. | 1.12 (0.49) | 3.56 (0.73) | 6.64 (0.77) | 2.70 (0.26) | n.r. | n.r. | yes, 8 oxides to 100 | trachyte on TAS in the text ("dacitic" in the abstract) | Yalcin et al. 2006 GRL 33:L14706, **Table 1, p. 2 of 4** | PDF table (sum 100.00) |
| B | **South Pole PS1809** (Yalcin's recalculation) | 27.50–27.99 m, 1809–13 | 8 / 6 | 60.28 (1.41) | 0.84 (0.16) | 15.80 (1.77) | 7.91 (1.86) | n.r. | 2.35 (0.93) | 5.45 (0.92) | 4.26 (0.75) | 3.11 (1.38) | n.r. | n.r. | yes, 8 oxides to 100 | andesite–trachyandesite | Yalcin 2006 Table 1 (data of Palais 1990) | PDF table (sum 100.00) |
| B′ | **South Pole PS1809** (as Palais printed it) | same | 8 analyses on 6 particles | 59.74 (1.40) | 0.83 (0.16)* | 15.66 (1.75) | 7.84 (1.84) | ~0.16?† | 2.33 (0.92) | 5.40 (0.91) | 4.22 (0.74) | 3.08 (1.37) | ~0.06?† | 0.47 (0.21)‡; SO3 0.28 (0.13) | EDAX "calculated to 100%" (Table II note), probably with SO3 and Cl included | andesitic; Table I says "Local?" | Palais, Kirchner & Delmas 1990 Ann. Glaciol. 14:216–220, **Table III col. 3, p. 218**; sample in Table I, p. 216 | PDF table (scanned OCR; see notes) |
| C | **Dome C** layer (first dated 1815, redated to 1809) | depth not read; 1809 | 13 / n.r. | 59.44 (1.63) | 0.67 (0.24) | 16.43 (0.51) | 9.00 (0.72) | n.r. | 2.83 (0.73) | 5.44 (0.82) | 4.14 (0.52) | 2.05 (0.40) | n.r. | n.r. | yes | andesite–trachyandesite | De Angelis et al. 1985 Nature 317:52, via Yalcin 2006 Table 1 and Palais 1990 Table III col. 4 (SiO2 59.45; other values the same) | PDF table of the secondary compilations; the 1985 original was not read |
| D | **Siple Dome A, SDMA-166** | 33.75 m, 1810 CE | 8 shards | 63.4 | not found | 16.77 | 6.3 | not found | not found | 1.21 | 5.99 | 4.91 | not found | not found | unknown (the 6 oxides sum to 98.58) | trachyte | Kurbatov et al. 2006 JGR 111:D12307, **Table 4**; Table 1 and §27 | PDF table as transcribed in the project note of 22 Oct (William's copy); full row **not** re-verified |
| E | Siple Dome A | 33.61 m, 1811 CE | n.r. | **not found** | | | | | | | | | | | | basanite | Kurbatov 2006 Table 4 | secondary |
| F | Siple Dome A | 34.60 m, 1804 CE | n.r. | **not found** | | | | | | | | | | | | basanite | Kurbatov 2006 Table 4 | secondary |
| G | TUNU2013, NE Greenland (QUB-1950) | 39.68–39.60 m, 1810 ± 1 | 3 shards, not analysed | — | | | | | | | | | | | | brown microlitic shards, 8–15 µm | Plunkett et al. 2023 QSR 301:107936, §2.2.5 p. 5, Table 1 p. 6 | PDF text |
| H | WAIS Divide WDC06A | 1809 sulfate interval | 0 | — | | | | | | | | | | | | dust only; "no population of tephra shards" matching | Dunbar, NMT research web page (unpublished) | secondary |

\* TiO2 in B′ is inferred. The OCR gives the TiO2 row as "0.72 (0.15), 0.83 (0.16), 0.67 (0.24), …" with a cell missing. Yalcin's renormalised SP value of 0.84 (0.16) works only if Palais printed 0.83 (0.16) for PS1809: the 8-oxide sum is then 99.10, and 59.74/99.10 = 60.28. So 0.67 (0.24) is the Dome C value, as Yalcin also gives it.
† MnO and P2O5 cannot be placed in columns reliably from the OCR.
‡ Cl is probably in this column, but that is not certain.

### Tambora 1815 controls in the same cores and papers
| Core / layer | Depth, age | n | SiO2 | TiO2 | Al2O3 | FeO | MgO | CaO | Na2O | K2O | Other | Source | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| South Pole PS1816 | 26.4–27.1 m, 1816–21 | 16 analyses / 5 particles (1–3 µm) | 57.83 (1.42) | 0.72 (0.15)? | 18.53 (0.74) | 5.53 (0.84) | 1.48 (0.36) | 3.19 (0.67) | 5.61 (0.47) | 6.02 (0.54) | SO3 0.34 (0.13), Cl 0.47 (0.12)? | Palais 1990 Table III col. 1, p. 218 | PDF table (OCR); TiO2, MnO and P2O5 columns uncertain |
| Tambora plinian matrix glass (reference) | proximal | 93 | 57.63 (0.97) | ? | 19.62 (0.36) | 4.47 (0.32) | 1.29 (0.13) | 3.12 (0.30) | 6.49 (1.05) | 6.36 (0.33) | – | Sigurdsson & Carey, cited in Palais 1990 Table III col. 2 | PDF table (OCR) |
| TUNU2013 1815 buffer (QUB-1949) | 38.97–38.91 m | 1 shard | rhyolite; values only in Suppl. Dataset 1 | | | | | | | | | Plunkett 2023 §2.2.4 | not Tambora ("Katla?"); 1816 ice had no tephra |
| Siple Dome | – | – | Tambora interval missed (fractured ice) | | | | | | | | | Kurbatov 2006 | – |
| Eclipse | – | – | no Tambora glass reported; Tambora used only for sulfate dating and flux (1809/Tambora flux 0.52) | | | | | | | | | Yalcin 2006 Table 3 | – |

The control works. The South Pole 1816–21 glass is high-K trachyandesite (K2O ~6, Al2O3 ~18.5) and matches Tambora matrix glass. **The South Pole 1809 glass does not**: it has K2O ~3.1, FeO ~7.9 and CaO ~5.4. So the South Pole 1809 layer is not reworked Tambora glass or a Tambora-type magma.

## 2. Comparison (inference)
- The record holds at least **three distinct 1809–1810 glass populations**:
  - **Yukon:** trachyte/dacite, SiO2 64.9, K2O 2.7, CaO 3.6, FeO 3.8.
  - **East Antarctic plateau (South Pole and Dome C):** andesite–trachyandesite, SiO2 59–60, FeO 8–9, CaO 5.4, K2O 2–3.
  - **Siple Dome:** trachyte, SiO2 63.4, K2O 4.9, CaO 1.2, FeO 6.3, typical of alkaline Antarctic (McMurdo/Pleiades) magmas.
- Yalcin's t-tests (Table 2) find:
  - Eclipse differs from South Pole and from Dome C at p<0.001 in SiO2, FeO, CaO and Na2O.
  - South Pole and Dome C do not differ significantly, so they probably have one source.
- The South Pole/Dome C glass is the only candidate for a far-travelled tropical 1809 component. Plunkett 2023 calls it "comparable to Indonesian tephra (Telaga Group F, Faral et al. 2022)". Palais tentatively suggested Cosigüina 1809, a date Yalcin calls spurious.
- Its analytical basis is weak:
  - The analyses are old SEM-EDAX on 1–5 µm particles.
  - The analyses were normalised, with the Na loss that implies.
  - Only 8 analyses on 6 particles exist at the South Pole.
  - At Dome C there are 13 analyses.
  - There is no WDS microprobe data.
  - There are no trace elements. **No published trace-element (LA-ICP-MS) data exist for any 1809 ice-core glass.**

## 3. What is missing and where to get it
1. **Kurbatov et al. 2006, full Table 4 rows.** The rows needed are SDMA-166 (TiO2, MnO, MgO, P2O5, Cl, total, SD) and the 33.61 m and 34.60 m basanites. Wiley/AGU and the NMT PDF were blocked from here. William's PDF copy has them: transcribe the full rows.
2. **USAP-DC dataset 609110 (NSIDC-0110), "Tephra in Siple and Taylor Dome Ice Cores"**, doi:10.7265/N50P0WXF.
   - Files: `sipleA_tephra.txt` and `.xls`, plus BSE images named sipleA33.4, sipleA33.6 and sipleA34.4.
   - USAP-DC dataset 609126 has `siple_glass_eprobe.xls` and the images sipleA_33.4, 33.6 and 34.4.
   - These are almost certainly the shot-by-shot microprobe data for the ~1804–1811 Siple Dome layers.
   - Download needs a reCAPTCHA, so it must be done in a browser on the Mac. **This is the best route to individual shard analyses.**
   - Caution: Dunbar, Zielinski & Voisin 2003 (JGR 108(B8), doi:10.1029/2002JB002056) dated these shallow Siple A layers to **1776–1805** ("previously unrecognized Antarctic volcanic activity between 1776 and 1805"). Kurbatov 2006 later placed 33.75 m at 1810. Check which age model the data files use.
3. **Palais 1990 Table III.**
   - Read the table from a clean copy, because the OCR misplaces the TiO2, MnO and P2O5 cells. The free Cambridge PDF is: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E1C240F1DD3064BF6EB0BD87D63D5361/S0260305500008612a.pdf/identification-of-some-global-volcanic-horizons-by-major-element-analysis-of-fine-ash-in-antarctic-ice.pdf
   - Fehrenbach 1984 (thesis, Paris) and De Angelis et al. 1985 hold the Dome C raw data.
4. **Yalcin 2006.** The free PDF is at https://scholars.unh.edu/cgi/viewcontent.cgi?article=1538&context=earthsci_facpub.
   - It gives means only.
   - Individual Eclipse shard analyses are probably in Yalcin's PhD thesis (University of New Hampshire, c. 2005–2007; not checked).
   - The AVO geochem database has an Eclipse Icefield station (https://avo.alaska.edu/geochem/station/5969661), but it lists only 20th-century and older events, not 1809.
5. **Plunkett 2023.** The 1810 shards in TUNU were not analysed. Supplementary Dataset 1 holds the 1815 rhyolite shard.
6. **Hutchison et al. (St Andrews).** The abstracts are PAGES VICS 2023 and COT-INTIMATE Sicily 2024 ("Re-evaluating the source, style and impacts of the 1800–1840 eruption cluster…"). They say "ice-core cryptotephra extracted for 1809 corroborate" multiple eruptions. **No numbers are published.** I found no peer-reviewed 1809 tephra paper as of 22 Oct 2026. The 2025 PNAS paper on Zavaritskii 1831 does not cover 1809. Ask Hutchison or Sigl for the data.
7. **Negative or irrelevant checks:**
   - Dai, Mosley-Thompson & Thompson 1991 analysed **no glass**. Their cores were Siple Station (not South Pole), Site T and Site A, and they measured sulfate and dust counts only.
   - Mount Brown South (Harlan et al. 2026, CP 22:1057) covers 1979–2017 only.
   - The DA2009 Dome A preprint (egusphere-2026-769) has sulfate only.
   - Gow & Meese 2007 (Siple Dome) covers deep layers only.
   - Dome Fuji visible layers are deep only.

## Sources
- Yalcin et al. 2006: https://scholars.unh.edu/earthsci_facpub/539 (PDF linked above)
- Palais et al. 1990: https://www.cambridge.org/core/journals/annals-of-glaciology/article/identification-of-some-global-volcanic-horizons-by-major-element-analysis-of-fine-ash-in-antarctic-ice/E1C240F1DD3064BF6EB0BD87D63D5361
- Plunkett et al. 2023: https://avo.alaska.edu/pdfs/cit15909.pdf
- Dai et al. 1991: https://bpcrc.osu.edu/sites/default/files/Dai_et_al_J_Geophys_Res_1991.pdf
- Dunbar, WAIS Divide: https://geoinfo.nmt.edu/staff/dunbar/research/ice_cores.html
- Dunbar et al. 2003 abstract: https://geoinfo.nmt.edu/staff/dunbar/publications/abstracts/dzv2003.html
- USAP-DC: https://www.usap-dc.org/view/dataset/609110 ; https://www.usap-dc.org/view/dataset/609126
- Kurbatov 2005 WAIS workshop slides (slide 19: 1809 event, "Buckle Is., Pleiades"): https://www.waisworkshop.org/sites/waisworkshop.org/files/files/Kurbatov-2005.pdf
- COT 2024 abstracts (Hutchison et al.): https://cot.iavceivolcano.org/content/uploads/sites/2/2024/09/cot_abstractvol_aug29-1.pdf
