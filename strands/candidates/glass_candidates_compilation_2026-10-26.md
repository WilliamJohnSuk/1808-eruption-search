---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: candidates
date: 2026-10-26
---

# Glass and rock compositions for the unrecorded-eruption candidates, scored against the 1809 ice glass (26 Oct 2026)

Thread "Compile glass compositions for candidate volcanoes". Asked: compile every published glass composition (whole-rock where glass is absent, flagged) for the 64 tier-B unrecorded-eruption candidates (notes/gvp_candidates_and_volcanocafe_2026-10-22.md), New Britain, Halmahera and the Banda arc first, and score them with the 22 Oct method (notes/glass_comparison_2026-10-22.md).

Files: data/glass_candidates.csv (14 rows added, same columns), data/glass_similarity_2026-10-26.csv (scores), scripts/glass_similarity_2026-10-26.py, data/glass_ice_1809.csv (H15 row added). William's download filed as `~/Downloads/1808-9 Volcano Project/papers/Faral_2022_JVGR_Ternate_Tidore_tephras.pdf`, key pages rendered to `faral_2022_pages/faral2022_pNN.png`.

**Verification levels.** *page image* = read from the rendered page; *text fetch* = an HTML or PDF text layer read through a fetch tool, numbers not checked against the page (a fetch tool can mis-transcribe a table); *range only* = a summary range in prose. **All similarity scores are Claude's calculation; all conclusions are inference.**

## 1. Access (what blocked the compilation)

- GEOROC, the EarthChem Portal and Library downloads, Göttingen Research Online (GEOROC precompiled files), HAL (bot wall), figshare downloads and Zenodo are all unreachable from Claude's cloud container and from the shell on William's Mac (that shell has no internet). GEOROC's web pages are a JavaScript app. **No GEOROC data were retrieved.** That is the main gap: GEOROC holds the whole-rock and glass analyses for nearly every candidate.
- What works: text fetches of open-access articles, PANGAEA data tables, and PDFs William saves.

## 2. What was found, by region

### Halmahera (tier B: Ibu, Jailolo, Tobaru, Todoko-Ranu, Mare, Moti, Tidore, Tigalalu, Amasing, Bibinoi)
- **Bani et al. 2021**, JVGR 418:107342, Table 4 (text fetch of the author copy): whole-rock analyses of Dukono, Ibu, Gamkonora, Gamalama and Makian, the only multi-volcano Halmahera major-element table found.
  - Dukono: SiO2 58.0–59.5, Fe2O3T 8.4–10.5, K2O 2.5–3.7 (medium- to high-K andesite).
  - Ibu (tier B): dacite, SiO2 66.6–67.1, K2O 3.2.
  - Gamkonora, Gamalama: basaltic andesite, SiO2 56.6–57.7, K2O 1.5–1.6.
  - Makian: SiO2 50.0–55.8, K2O 0.8–1.2.
- **Faral et al. 2022**, JVGR 423:107474 (William's download; **page image** pp. 12–13, 17, 34):
  - The 52 analyses are **bulk tephra by ICP-AES (lithium-borate fusion), not glass** (methods section, text layer). The oxide values are in Supplementary Material 2, which is not in the author PDF. Figure 6 (K2O–SiO2) is not in the PDF either.
  - Groups: A = Telaga caldera dacite, 22,000–17,500 cal BP; B, D, G = grey pumice falls; C, F, G = Gamalama-type (like the 1907 Batu Angus lava); E = Kie Matubu (Tidore) andesite.
  - **Group F is the Ngade maar phreatomagmatic ash and scoria on Ternate, c. 14,500–13,000 cal BP.** Plunkett et al. 2023 call the 1809 South Pole/Dome C glass "comparable to Indonesian tephra (e.g., Telaga Group F tephra reported by Faral et al., 2022)". In Faral's paper Group F is not Telaga; the phrase mixes the Telaga caldera with Group F (inference from the page images). Plunkett's comparison is therefore with a bulk Gamalama-type basaltic-andesite to andesite tephra, not with glass.
  - Youngest dated deposits: Kie Matubu 2669 ± 77 cal BP (charcoal) and a paleosol above Kie Matubu block-and-ash flows at 740 ± 26 cal BP (c. 1210 CE) (Table 2, p. 34). Kie Matubu has no recorded eruption since the 16th century. **No deposit of c. 1800 is identified** on Ternate, Tidore or Maitara. Fig. 2 caption: Tolire maar (Ternate) formed in a 1775 phreatomagmatic eruption.
- West Halmahera paper (Jailolo, Sahu, Gamkonora, Ibu; JGSM v20 no. 3, doi:10.33332/jgsm.geologi.v20i3.468): trace elements only, by its abstract page.
- Gill, EarthChem Library 1502 (doi:10.26022/IEDA/111502): Smithsonian whole-rock compilation for Halmahera, Ternate, Tidore, Mare, Moti, Makian and others (.xls, 64.5 kB). The download link is not exposed; not read.

### New Britain (tier B: Bola, Dakataua, Garove, Garua Harbour, Hargy, Garbuna, Lolo, Sulu Range, Tavui; tier A: Witori)
- No new glass for any tier-B New Britain volcano. Witori W-H and Dakataua Dk glass (Neall et al. 2021) were already in the CSV.
- Woodhead, Eggins & Johnson 1998 (J. Petrol.): only the front matter is reachable (Russian mirror). Its new data are trace elements and isotopes, focused on the Sulu Range.
- BMR report on Bamus, Lake Hargy and the Sulu Range (data.gov.au; Geoscience Australia catalogue): no download reachable. Johnson et al. 1983 (Geol. Rundschau 72:207) on Bamus is paywalled.
- New Ireland Basin marine tephra glass (Horz et al. 2013 PANGAEA series doi:10.1594/PANGAEA.824489; text fetch, only some rows returned): three groups. A = alkaline, very high K (Tabar–Lihir–Tanga–Feni). B = high-K rhyodacite. C = low-K, including a 60.7% SiO2, FeO 10.1, K2O 0.81 glass. The sources are not assigned in the tables (Horz's 2002 Kiel thesis names Rabaul and "New Britain arc" groups). Ages were not worked out. Reference only.

### Banda arc (tier B: Gunungapi Wetar, Manuk, Nila, Teon)
- **No glass or major-element table found for the four tier-B Banda volcanoes.**
- Banda Besar and Naira calderas (Suhendro et al. 2022, Geosciences 12:428, text fetch): rhyolite 73.1–73.8 and dacite 66.2–67.2 SiO2, prehistoric. Too silicic for the 1809 ice glass.
- Gill, EarthChem Library 1499 (doi:10.26022/IEDA/111499): Banda Api, Banda Neira, Manuk, Serua, Damar, Ambon whole rock (.xlsx). Vroon 1992 thesis (Utrecht; Sr-Nd-Pb on seven Banda islands): the PDF fetch failed.

### Other unrecorded-eruption arcs (quick look)
- **Tonga (Hunga):** 2022 products are low-K basaltic andesite, K2O 0.5–0.6, mean tephra glass SiO2 57.9 (Ukstins et al., EGU22-13585, text fetch). Tonga glass is far below the 1809 glass in K2O (inference).
- **Bougainville:** Bagana lavas are 56–58 SiO2, medium-K, with a calculated groundmass of 63–66 SiO2 (J. Petrol. 2024 egae065, text fetch). No data for Billy Mitchell, Balbi, Loloru or the other tier-B Solomons volcanoes.
- **SE New Guinea:** Lamington 1951 andesite is 58.7–61.2 SiO2 whole rock, and its enclave glass is rhyolitic (Zhang et al. c. 2015, text fetch). Nothing found for Victory, Waiowa or the other D'Entrecasteaux centres.
- **Sangihe and Sulawesi:** Ruang 2024 juvenile SiO2 53.0–54.3 (IJOG article 1333 abstract). Tondano andesites (Dmitrieva et al. 2023, Litosfera 23(3)): the PDF failed to load. Gill ECL 1503 holds Sangihe whole rock.
- **Mindanao, central Philippines, Vanuatu, Fiji, Matthew/Hunter:** nothing found in the time spent.

## 3. Scores (Claude's calculation)

Borchardt similarity on SiO2, Al2O3, FeOt, MgO, CaO, Na2O and K2O. Same-source glasses usually score ≥0.92–0.95. Control: Tambora 0.92. The previous best was Dome C vs Tibito, 0.88.

| Candidate (material) | Dome C 1809 | South Pole 1809 | Eclipse 1809 | Siple Dome 1810 |
|---|---|---|---|---|
| Dukono DK3 (whole rock) | 0.89 | **0.93** | 0.71 | 0.67 |
| Dukono DK2 (whole rock) | **0.90** | 0.91 | 0.70 | 0.67 |
| Gamkonora (whole rock) | 0.88 | 0.82 | 0.61 | 0.63 |
| Long Island Tibito (glass, previous best) | 0.88 | 0.80 | 0.62 | 0.59 |
| Gamalama (whole rock) | 0.86 | 0.79 | 0.59 | 0.61 |
| Dukono DK1 (whole rock) | 0.79 | 0.84 | 0.63 | 0.65 |
| Makian MK3 (whole rock) | 0.81 | 0.77 | 0.59 | 0.62 |
| Dakataua Dk (glass) | 0.78 | 0.77 | 0.83 | 0.69 |
| NIB low-K glass, grp C (glass) | 0.77 | 0.75 | 0.55 | 0.54 |
| Ibu (whole rock) | 0.68 | 0.75 | **0.84** | 0.73 |
| Witori W-H6 (glass) | 0.66 | 0.66 | 0.80 | 0.60 |
| Hunga 2022 (bulk) | 0.67 | 0.63 | 0.48 | 0.48 |

## 4. What the comparison says (inference)

1. **The closest compositional family to the 1809 Antarctic glass found so far is the Halmahera arc,** Dukono in particular. Dukono whole rock (SiO2 about 60, FeOt about 7.7–7.9, K2O 2.5) scores 0.89–0.93 against the Dome C and South Pole glass, above Tibito's 0.88.
2. **This is not a match, and the caveat cuts against Dukono itself.** A whole-rock andesite contains crystals, so its glass is more silicic and lower in Ca, Mg and Al than the bulk rock. A 60% SiO2 whole rock like Dukono's would have glass well above 60%, a worse fit. The rocks whose glass would land near 60% SiO2 are Halmahera's basaltic andesites (Gamkonora, Gamalama: about 57% whole rock). Their K2O (1.6) would rise in the glass toward the Dome C value (2.05). So the result supports "Halmahera-type, medium-K, iron-rich arc andesite" as a family. It does not single out a volcano.
3. **K2O separates the arcs.** The 1809 glass has K2O 2.0 (Dome C) to 3.1 (South Pole). Low-K arcs fit badly on that oxide alone: Tonga (K2O 0.5–0.6), the New Britain arc front (marine glass 0.8; Witori 1.2) and Makian (≤1.2). Medium- to high-K arcs fit: Halmahera's Dukono, Gamkonora and Gamalama; the Bismarck arc's Long Island; Bagana. On present data this lowers New Britain's arc-front volcanoes and Tonga, and keeps Halmahera and the medium-K parts of PNG in play. The Banda arc is untested: its tier-B volcanoes have no major-element data here.
4. **Dukono is a tier-C volcano, not tier B.** In the 2018 GVP snapshot it has one historically observed eruption in 1700–1900, a first historical eruption in 1550, and a last known eruption in 2018. A large eruption in 1808 on northern Halmahera would have gone unrecorded only if the Ternate sultanate's and the Dutch post's records missed it or are lost. The Ternate records strand (B48) found nothing for 1763–1840. This keeps Dukono possible but unsupported.
5. **The Eclipse (Yukon) glass** (64.9 SiO2, Na2O 6.6) is closest to the Ibu dacite (0.84) and Dakataua glass (0.83). Neither is a match, and a northern source for that population remains likely (earlier notes).
6. **Plunkett 2023's Indonesian comparison is weaker than it reads.** Faral's "Group F" is bulk tephra from a 14,000-year-old Ternate maar, not glass and not the Telaga caldera.

## 5. Ice-core addition

Added to data/glass_ice_1809.csv: H15 (Mizuho Plateau) 1809 layer, "fine ash-like materials (~10 µm)", unanalysed (Kohno et al. 1996, p. 50; register B43). Unanalysed particles were also found in the 1816 layer.

## 6. Needs William's hands (all optional; shortest first)

1. **GEOROC precompiled files** (convergent-margin CSVs) for New Britain/Bismarck, Halmahera, Sangihe/Sulawesi, Banda, Bougainville/Solomons and PNG. Download them in a browser from the Göttingen Research Online GEOROC dataverse (https://data.goettingen-research-online.de/dataverse/digis) into `1808-9 volcano research/data/georoc/`. A folder thread can then score every analysis with a GLASS or whole-rock label without internet.
2. **Gill's EarthChem Library sheets:** Halmahera (https://doi.org/10.26022/IEDA/111502), Banda (https://doi.org/10.26022/IEDA/111499), Sangihe (https://ecl.earthchem.org/view.php?id=1503). Use the "Download" button on each page; save to the same folder.
3. **Faral et al. 2022 Supplementary Material 2** (bulk-tephra oxides): on the ScienceDirect article page (https://doi.org/10.1016/j.jvolgeores.2022.107474), "Supplementary data". These files are usually free even when the article is not.
4. Optional, paywalled: Woodhead, Eggins & Johnson 1998, J. Petrol. 39:1641 (New Britain arc); Johnson et al. 1983, Geol. Rundschau 72:207 (Bamus).

## Sources read this session
- Bani et al. 2021 author copy: https://iris.unipa.it/retrieve/8fd50a2e-f5be-42f9-8740-85d20c428a6f/Bani_et_al_Gas_budget_and_source_geochem_Halmahera_Volc.pdf (citation confirmed at https://www.documentation.ird.fr/hor/fdi:010082657)
- Faral et al. 2022 (HAL hal-03680328; William's PDF); listing at https://www.lgp.cnrs.fr/?p=2791
- Plunkett et al. 2023 §2.2.5: https://avo.alaska.edu/pdfs/cit15909.pdf
- Horz et al. 2013 PANGAEA: https://doi.pangaea.de/10.1594/PANGAEA.824489 (child tables 824476–824478); Horz 2002 thesis, Kiel (macau.uni-kiel.de, diss. 623)
- Suhendro et al. 2022: https://www.mdpi.com/2076-3263/12/11/428
- Ukstins et al. EGU22-13585: https://presentations.copernicus.org/EGU22/EGU22-13585_presentation-h362350.pdf
- Bagana, J. Petrol. 2024: https://ueaeprints.uea.ac.uk/99667/1/egae065.pdf
- Lamington: https://durham-repository.worktribe.com/OutputFile/1415607 and /1325221
- Gabriel et al. 2025 (St Andrews PDF): reference glasses are Tarumae, Long Island (Coulter 2009) and Shiveluch only; no 1808/09 mention. Raw glass data at PANGAEA.974359 and 974360.
- EarthChem Library pages 1499, 1502, 1503 (metadata only).

## 7. Update 26 Oct ~21:55 UTC: Gill's EarthChem whole-rock sheets (William's downloads)

**Files.** William's three downloads are filed in `~/Downloads/1808-9 Volcano Project/data/georoc/` as `Gill_ECL1499_Banda_wholerock.xlsx`, `Gill_ECL1502_Halmahera_wholerock.xls` and `Gill_ECL1503_Sangihe_wholerock.xlsx`. They are Smithsonian-collection whole-rock analyses, CC BY-SA 4.0.

**What was scored.** All 248 analyses (Banda 20, Halmahera group 96, Sangihe and N Sulawesi 132), with the same 7-oxide similarity method. Results: data/cc-by-sa/gill_ecl_wholerock_scored_2026-10-26.csv; script: scripts/score_gill_ecl_2026-10-26.py.

**How the data were treated.**
- Fe is given as FeOT (Banda), FeO* (Halmahera) or Fe2O3 (Sangihe, ×0.8998).
- Each analysis was normalised anhydrous on SiO2–P2O5.
- These are whole rock, not glass, so the same caveat as section 4 applies.

**Verification.** The values were read by script from the files themselves, not by a fetch tool.

**Results (Claude's calculation; conclusions inference).**
- **Banda arc: poor fit.** All Banda arc rocks here are low-K, with K2O ≤1.4.
  - Banda Api is a tholeiitic dacite: SiO2 64–68, K2O 0.8–0.9. Best scores 0.79 against Dome C and 0.81 against South Pole.
  - Manuk (tier B) has K2O <1.0, best 0.74. Serua is best at 0.75.
  - No Nila, Teon or Wetar samples are in the file.
  - On K2O alone, the analysed Banda volcanoes are an unlikely source of the 1809 Antarctic glass. Nila, Teon and Wetar are untested.
- **Halmahera: medium- to high-K, the best fits again.**
  - Tarakani lavas: NH69, SiO2 60.1, K2O 2.66, score 0.93 against South Pole. NH67 is from near Gahla and Mamuya. Both are in the Dukono area of north Halmahera, so this repeats the Dukono result from Bani 2021.
  - Todoke lava (NH44, Lake Todoke; GVP tier-B "Todoko-Ranu"): SiO2 60.9, K2O 1.85, score 0.91 against Dome C.
  - Ternate (Gamalama) lavas: up to 0.90.
- **Other tier-B islands of the group score lower.**
  - Tidore: up to 0.83; K2O 1.0–1.7.
  - Mare: 0.83.
  - Moti: 0.79.
  - Jailolo's recent lavas are low-K basaltic andesite, ≤0.73.
- **North Sulawesi: medium-K andesites score just as high as Halmahera.**
  - Lokon–Empung and Tompaluan: Empung PJ135, SiO2 60.0, K2O 1.97, score 0.92 against Dome C.
  - Mahawu: 0.91.
  - Tondano area: Lembeh up to 0.87.
  - Sangihe proper is lower: Awu up to 0.81, Banua Wuhu up to 0.84.
- **Dated lavas.**
  - The only dated lavas near our window are Tangkoko's Batu Angus flows, labelled 1801, 1821 and 1880: basaltic andesite, K2O about 0.9, score ≤0.81.
  - No sample is labelled 1808 or 1809.

**What this changes (inference).**
1. A whole-rock score of about 0.90 turns out to be common: any medium-K andesite of about 60% SiO2 in N Sulawesi or Halmahera reaches it. **Whole-rock similarity therefore cannot pick a volcano within these arcs.** Only glass analyses or trace elements of a dated c. 1808 deposit can.
2. **K2O remains the useful filter.** It lowers the Banda arc front (Banda Api, Manuk, Serua) alongside Tonga and the New Britain arc front. It keeps the medium- to high-K centres of north Halmahera (the Dukono–Tarakani area, Todoko-Ranu), Ternate and N Sulawesi (Lokon–Empung, Mahawu).
3. N Sulawesi's Minahasa volcanoes now join Halmahera as the compositional best fit. That zone was in the 26 Oct records strand (B48), with weak negatives (Bleeker 1856 harvest tables).

## 8. Update 26 Oct ~22:05 UTC: GEOROC Bismarck/New Britain and Solomon files (William's downloads)

**Files.** Filed as `~/Downloads/1808-9 Volcano Project/data/georoc/GEOROC_2026-09_BISMARCK_ARC_NEW_BRITAIN_ARC.csv` and `GEOROC_2026-09_SOLOMON_ISLAND_ARC.csv`. These are the GEOROC precompiled Convergent Margins files, Sep 2026 release.

**What was scored.** 1,878 analyses with full major elements: 201 glass and 1,257 whole rock in the Bismarck file, 420 whole rock in the Solomon file. Same 7-oxide method. Results: data/georoc_scored_2026-10-26.csv; script: scripts/score_georoc_2026-10-26.py.

**Verification.** Values read by script from the GEOROC files. The original papers were not seen.

**Results (Claude's calculation; conclusions inference).**

- **Best glass so far: Dakataua's Makalia cone.**
  - The sample is Lowder 1970's groundmass glass of a Holocene pyroxene-andesite lava (sample 114G): SiO2 61.2, FeOt 9.0, K2O 1.77.
  - Scores: **0.92 against Dome C** (equal to the Tambora self-match), 0.89 against South Pole and 0.67 against Eclipse.
  - The same rock's whole rock (58.6 SiO2) scores 0.89. That is the expected step: glass is more silicic than the whole rock.
  - Makalia is Dakataua's post-caldera cone. The GVP eruption list gives a Makalia VEI 2 eruption in 1895, dated by anthropology, and Dakataua is a tier-B candidate.
  - **Caveats:**
    - It is a single 1970-era analysis.
    - It is lava groundmass, not tephra.
    - It is undated beyond "Holocene".
    - GEOROC's coordinates for Lowder's samples look generic (-5.33/150.02).
    - Dakataua's other glasses do not match: four rhyolitic Makalia-labelled glasses (75–78 SiO2) score ≤0.50, and the c. 1300 BP Dk tephra (66.5 SiO2) scores 0.78.
  - Net: Makalia shows that an andesite magma close to the Dome C glass was erupted at Dakataua in the Holocene. It is not evidence of an eruption in 1808.
- **Rabaul: whole rock fits, glass does not.** Rabaul whole rock (medium-K andesite–dacite) reaches 0.93 against Dome C and 0.95 against South Pole, among them the 2013–14 lavas at 0.92. Rabaul's 22 glasses (median SiO2 69.6, K2O 3.6) score ≤0.69 against Dome C. This is the whole-rock caveat in action.
- **Rabaul's neighbour Tavui (tier B, submarine caldera):** one trachyandesite at 0.92/0.92 (whole rock). The rest are low-K basaltic andesites and dacites, ≤0.85.
- **Other tier-B New Britain centres (whole rock):**
  - Garbuna: 2 analyses, ≤0.84.
  - Lolo and Garove: low-K (K2O about 0.5), ≤0.82.
  - Sulu Range: low-K, ≤0.74.
  - Garua (Harbour): 1 analysis, 0.68.
  - Pago (Witori): ≤0.77.
  - Hargy and Bola: not in the file.
- **Bougainville and Solomons (whole rock):**
  - Balbi: 1 analysis, K2O 3.3; 0.91 against South Pole, 0.84 against Dome C.
  - Takuan: 0.80.
  - Simbo: ≤0.75.
  - Bagana: ≤0.88.
  - Savo: up to 0.88 against Dome C and 0.90 against Eclipse.
  - Billy Mitchell, Loloru, Tore, Kavachi and Gallego are not in either file.
- **SE New Guinea (whole rock):** Lamington 1951 andesite scores 0.88–0.90 against Dome C and Victory 0.85. Its glass is rhyolitic, so the glass would fit worse.
- **Marine glasses from the Manus back-arc and PACMANUS** (deep submarine, excluded as sources) reach 0.86–0.90. They show the same andesite family exists widely in the Bismarck Sea.

**What this changes (inference).**
1. **Dakataua returns to the list as the one tier-B New Britain volcano with a glass analysis close to Dome C.** It has recorded post-caldera activity (Makalia, 1895). This is the strongest glass-to-glass result so far, but it rests on one old analysis of an undated lava.
2. The New Britain arc front stays a poor fit on K2O (Lolo, Garove, Sulu, Ulawun, Bamus).
3. Whole-rock scores of 0.90–0.95 again appear at several volcanoes (Rabaul, Tavui, Halmahera, N Sulawesi). Without glass from dated deposits, whole rock cannot rank them.
4. **The next useful test** would be a dated tephra from Makalia or Dakataua younger than the Dk tephra. Neall et al. 2021 cover the Willaumez Isthmus south of Dakataua. Whether any post-Dk Dakataua tephra has been analysed is not known from these files.

## 9. Update 26 Oct ~22:15 UTC: GEOROC Halmahera, Sulawesi, Banda, Luzon, Vanuatu and Tonga files

**Files.** Filed as `GEOROC_2026-09_<ARC>.csv` in `~/Downloads/1808-9 Volcano Project/data/georoc/` (William's downloads). All eight GEOROC arcs were then scored together: 8,740 analyses, 1,406 of them glass. Results: data/georoc_scored_2026-10-26.csv, which replaces the section-8 file. Script: scripts/score_georoc_2026-10-26.py.

**Verification.** Read by script from the GEOROC files. My name-matching of volcanoes caught two false hits ("NILA" inside "MANILA TRENCH"; "IBU" in the Tonga file), which are ignored below.

**Results (Claude's calculation; conclusions inference).**

- **Marine tephra glasses from other arcs reach the same scores as Makalia.**
  - South China Sea core MD97-2142, off Mindoro (Ku et al. 2009, G-cubed 10, a 2-million-year record of SW Luzon explosive volcanism): glasses with SiO2 58–62, FeOt 7.7–8.8, K2O 1.9–2.4 score **0.92–0.95 against Dome C and up to 0.93 against South Pole**. These layers are tens of thousands of years old or more (1.2–36 m depth).
  - ODP Sites 832–833 (Vanuatu, Baker et al. 1994): Pleistocene ash glasses up to 0.90 against Dome C and 0.93 against South Pole.
  - **So a major-element score of 0.92–0.95 is reached by unrelated arc glasses from the Philippines, Vanuatu and New Britain.** On major elements alone the Dome C/South Pole glass is a common arc andesite composition. It cannot name its source without trace elements or a dated proximal tephra.
- **Whole rock, tier-B and related volcanoes:**
  - Gaua (Vanuatu, tier B): 0.91 against Dome C, 0.94 against South Pole.
  - Awu (Sangihe): 0.92.
  - Ibu: 0.91.
  - Dukono: 0.90/0.93.
  - Teon (Banda, tier B): 0.87, with K2O median 2.0.
  - Nila: 0.84, K2O median 1.9.
  - Wetar: 0.83/0.85, K2O median 2.5.
  - Manuk: 0.84.
  - Banda Api: 0.83.
  - Philippine tier-B volcanoes: Mandalagan and Silay 0.88, Cuernos de Negros 0.87, Apo 0.87.
  - Taal (watched zone): 0.96 whole rock.
- **Correction to section 7.** The *southern* Banda arc (Teon, Nila, Wetar) is medium-K (K2O about 2). Only the northern Banda Api–Manuk–Serua group is low-K. So K2O no longer counts against Teon, Nila and Wetar.
- **Tonga stays out on potassium.**
  - Hunga whole rock: K2O median 0.52, best 0.74.
  - Tofua, Late, Kao, Fonualei: K2O ≤1.1 and scores ≤0.82.
  - All Tonga glass ≤0.73.
- **Halmahera and Sulawesi glass:** only 21 glass analyses. None above 0.70 except Ruang 2024 (0.64) and alkaline Sulawesi glass (0.69).

**What this changes (inference).**
1. **The desk glass comparison has reached its limit.** Major elements put the 1809 Antarctic glass in a widespread medium-K arc andesite family. That family includes Makalia/Dakataua, SW Luzon and Vanuatu tephras, and the rocks of Halmahera, N Sulawesi, the southern Banda arc, Gaua and Rabaul. It rules out low-K arcs (Tonga, the New Britain arc front, Witori) and very high-K ones. It does not choose among the rest.
2. **What would choose:** trace elements (Zr, Y, Nb, rare earths) on the ice shards, which no one has published; or glass from a tephra dated to c. 1808 near a candidate volcano. Both need the ice-core labs or field sampling.
3. The section 8 Makalia result should be read in this light. It is a good match, but not a unique one.
