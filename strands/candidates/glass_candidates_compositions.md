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

# Glass compositions of candidate c. 1700–1900 deposits (desk tephra comparison for the 1808/09 eruption)

Compiled 2026-10-22. CSV: `data/glass_candidates.csv`. Raw downloads are in the session scratchpad (`.../scratchpad/vglass/`: `neallS1.xlsx`, `neallS1.txt`).

**Verification levels:**
- "suppl. xlsx": I downloaded the authors' supplementary data file and computed the means myself.
- "journal table (text fetch)": a published table read through an HTML-to-text fetch, not checked against the PDF.
- "secondary": abstract or summary text only.

No numbers here are estimated or invented. Blank cells mean the source does not give a value.

**Access notes:**
- From Claude's cloud container, curl could reach only S3. Massey, figshare API, HAL, archimer, GEOROC, Zenodo and archive.org all returned 403.
- GEOROC (georoc.eu) is a JavaScript application and could not be queried with text tools. **No GEOROC data were retrieved.**
- The following are paywalled and not read: Machida et al. 1996, *Quaternary International* 34–36: 65–78; Samaniego et al. 2015, *Bulletin of Volcanology* 77: 51; Manrique et al. 2020, *Bulletin of Volcanology* 82: 6. The archimer author draft of Manrique et al. 2020 gave only 2.8 kB of text.

---

## 1. Witori / Pago (W New Britain, PNG): the W-H tephra series

- **Rock type:** Pago dacite. W-H glass is low-K rhyolite: SiO2 about 72, K2O about 1.2, FeOt about 3.6–4.1, CaO about 3.5.
- **Dating, two sources:**
  - **GVP (eruption list):**
    - W-H6 = "1800 Jul 2 (?) ± 182 days", tephrochronology, VEI 4, "explosion, phreatomagmatic".
    - W-H5 = 1730 ± 25.
    - W-H4 = 1550 (?), VEI 4.
    - W-H3 = 1450 (?).
    - W-H2 = 1050 ± 100.
    - Reported eruptions 1911–1918 (VEI 3) and 1933 (VEI 2).
    - Source: volcano.si.edu, vn 252080.
  - **Neall et al. 2021, Table 1 (p. 6):** gives broader ages based on radiocarbon:
    - **W-H6: "post-1426 cal. AD"** (95% calibrated range).
    - W-H5: 1318–1636 cal AD.
    - W-H4: 1305–1450 cal AD.
    - **W-H7: "1914 AD?"**, probably the 1911–18 eruption.
  - The GVP "1800" is therefore a tephrochronological estimate from Machida et al. 1996, which I have not read. No direct date ties W-H6 to c. 1800. The only firm constraints are that it is younger than about 1426 CE and older than W-H7 (?1914).
- **Volume and sulfur:** none found. GVP gives VEI 4.
- **Source:** Neall, McGee, Turner, O'Neill, Zernack & Athens 2021, "Geochemical fingerprinting of Holocene tephras in the Willaumez Isthmus District of West New Britain", *Technical Reports of the Australian Museum Online* 34: 5–24.
  - Glass was analysed by EDS microprobe (Auckland), 20 µm beam.
  - The data file is Table S1, doi:10.6084/m9.figshare.14502618 ("Appendix 1 … .xlsx").
  - The authors' own text (p. 19–21) gives the correlations:
    - Tili site: tephras 1–3 = W-H7, W-H6, W-H5 (these labels are the authors').
    - Garu 1 and 2 are "highly likely" W-H6 and W-H7.
    - Post-W-K4 glasses "show considerable compositional overlap".
- **How the means were computed:** from the raw per-shard values, renormalised by me to 100% on the 11 oxides listed (SO3, Cr2O3 and NiO dropped; the authors say they lack standards). SD is 1σ.

| Deposit (site, depth) | Age / method | Type | n | SiO2 | TiO2 | Al2O3 | FeOt | MnO | MgO | CaO | Na2O | K2O | P2O5 | Cl | Raw total | Source | Verif. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **W-H7** (Tili 1, 122–124 cm) | "1914 AD?" | glass | 10 | 71.34 | 0.46 | 13.86 | 4.14 | 0.09 | 0.98 | 3.80 | 3.96 | 1.19 | 0.11 | 0.07 | 97.8 | Neall 2021 Table S1, sheet 4 | suppl. xlsx |
| SD | | | | 0.31 | 0.08 | 0.22 | 0.09 | 0.07 | 0.10 | 0.17 | 0.19 | 0.08 | 0.10 | 0.02 | | | |
| **W-H6** (Tili 2, 137–150 cm) | post-1426 cal AD (14C); GVP "1800?" | glass | 12 | 71.97 | 0.41 | 13.64 | 3.80 | 0.07 | 0.90 | 3.57 | 4.19 | 1.22 | 0.13 | 0.10 | 96.8 | Table S1, sheet 4 | suppl. xlsx |
| SD | | | | 0.42 | 0.08 | 0.14 | 0.17 | 0.08 | 0.09 | 0.13 | 0.09 | 0.05 | 0.08 | 0.04 | | | |
| **W-H5** (Tili 3, 263–268 cm) | 1318–1636 cal AD; GVP 1730±25 | glass | 10 | 72.97 | 0.38 | 13.47 | 3.45 | 0.06 | 0.79 | 3.28 | 4.14 | 1.29 | 0.10 | 0.08 | 97.4 | Table S1, sheet 4 | suppl. xlsx |
| SD | | | | 0.32 | 0.09 | 0.18 | 0.17 | 0.07 | 0.06 | 0.15 | 0.11 | 0.08 | 0.06 | 0.05 | | | |
| Garu 1 (23–24 cm; W-H7 or W-H6) | — | glass | 10 | 72.13 | 0.40 | 13.80 | 3.72 | 0.05 | 0.77 | 3.52 | 4.14 | 1.23 | 0.17 | 0.07 | 98.0 | Table S1, sheet 5 | suppl. xlsx |
| Garu 2 (35–36 cm; W-H6 or W-H7) | — | glass | 9 | 71.69 | 0.42 | 13.76 | 3.89 | 0.09 | 0.97 | 3.68 | 4.11 | 1.18 | 0.14 | 0.08 | 98.0 | Table S1, sheet 5 | suppl. xlsx |
| W-H6 (Kulu 1/1, 36–45 cm) | correlated | glass | 11 | 71.85 | 0.42 | 13.53 | 3.86 | 0.13 | 0.94 | 3.60 | 4.12 | 1.14 | 0.04 | 0.38 | 98.8 | Table S1, sheet 6 | suppl. xlsx (SD SiO2 0.77; Cl high in this session) |
| W-H6 (Kulu 2/1 "XX11", 8–15 cm) | correlated | glass | 11 | 72.41 | 0.40 | 13.78 | 3.60 | 0.07 | 0.73 | 3.47 | 4.09 | 1.21 | 0.15 | 0.08 | 97.3 | Table S1, sheet 6 | suppl. xlsx (SD SiO2 0.93) |
| *Ref: Dakataua Dk (Buludava)* | c. 1300 cal BP | glass | 13 | 66.53 | 0.75 | 14.66 | 5.03 | 0.20 | 1.39 | 4.02 | 4.58 | 2.15 | 0.40 | 0.28 | 97.0 | Table S1, sheet 1 | suppl. xlsx |
| *Ref: Dakataua Dk (Volupai)* | c. 1400 14C BP | glass | 12 | 66.47 | 0.71 | 14.75 | 5.18 | 0.17 | 1.46 | 4.16 | 4.41 | 2.08 | 0.33 | 0.27 | 97.2 | Table S1, sheet 1 | suppl. xlsx |

**Fingerprint (inference from the table):**
- W-H7, W-H6 and W-H5 form a tight, low-K (K2O 1.2–1.3), high-Ca (CaO 3.3–3.8), Na-rich rhyolitic glass. They are hard to tell apart.
- At Tili, SiO2 falls and FeO and CaO rise upwards, from W-H5 to W-H7.
- **Dakataua glass is different:** dacitic, with K2O about 2.1 and TiO2 about 0.7. Dakataua is not a 1700–1900 candidate here.
- I found no published Machida et al. 1996 glass table online (it may give refractive indices only). Petrie & Torrence 2008 give radiocarbon ages only.

## 2. Tutupaca (S Peru): the 218 ± 14 aBP eruption

- **Rock type:** dacite. Tutupaca Reciente domes: whole-rock 63.2–68.0 wt% SiO2 and 2.9–3.7 wt% K2O, by ICP-AES on 55 samples. These ranges cover the whole young edifice, not only the 1802 products. Interstitial glass is "essentially rhyolitic"; **no glass numbers were found.**
  - Source: Manrique, Samaniego, Médard, Mariño, Valderrama & Liorzou, INGEMMET congress abstract CPG17-079 (secondary).
- **Dating:**
  - 14C 220 ± 30 aBP on charred material at the top of the Zuripujo PDC sequence (Valderrama et al., CPG17-133).
  - Bulletin of Volcanology abstract: 218 ± 14 aBP, "probably between 1787 and 1802 AD" from chronicles plus radiometric data. The authors link it to the 1802 eruption.
  - Mariño et al. 2016 hazard map (CPG18-124): "possibly between 1731 and 1802".
- **Size:**
  - Debris avalanche: <1 km³.
  - Associated pyroclastic deposits: 6.5–7.5 × 10⁷ m³ bulk.
  - "At least VEI 3" (CPG18-124). This is a small eruption.
- **Pre-eruptive conditions** (Manrique et al. 2020, *Bulletin of Volcanology* 82: 6, abstract): 735 ± 23 °C, about 8.8 km depth; recharge raised rims to 840 °C.
- **Sulfur:** none given.
- **Paywalled sources that may hold glass tables:** Samaniego et al. 2015 (doi 10.1007/s00445-015-0937-8) and Manrique et al. 2020 (doi 10.1007/s00445-019-1335-4; author draft at archimer.ifremer.fr/doc/00687/79870/82742.pdf, which failed to extract).

## 3. Ticsani (S Peru)

- **Youngest explosive deposit:** "Ticsani pardusco", a brownish pumice-fall deposit.
  - It lies above the 1600 CE Huaynaputina ash and below the last dome D3, so it is less than 400 years old.
  - Volume 0.015 km³, column about 10 km, VEI 2–3, with bread-crust bombs (phreatomagmatic phase).
  - Source: Mariño & Thouret, *Geología, historia eruptiva y evaluación de peligros del volcán Ticsani*, no date (references run to 2002), via the sigrid.cenepred.gob.pe document 150; citing Mariño 2002.
- **Rock type:** "Modern Ticsani" products are high-K dacites with 64–66 wt% SiO2 and 7–8 wt% total alkalis (whole-rock; their Tables 3–4 not seen). **No glass data found.**
- **Dating:** the GVP date of "1800" is not supported by a radiometric date in this source. Lavallée et al. 2009 was not reached.

## 4. Putana (Chile/Bolivia)

- GVP gives "1810 ± 10", described as "a major one". Other sources (Stebel et al. 2015) put the last eruption in the late 19th century, or doubt any historical eruption.
- Rocks: basaltic andesite, andesite and dacite.
- **No deposit, glass or whole-rock data found for a c. 1810 event.**

## 5. Other named candidates and references

| Volcano | Youngest event, dating | Rock type | Glass data |
|---|---|---|---|
| Victory (Cape Nelson, PNG) | GVP "1810 ± 10" (per earlier notes); Wikipedia: dome activity c. 1890–1935 | Andesite (high Cr–Ni) | **None found** |
| Cabalían (Leyte) | 1820 ± 30, 14C on a pyroclastic-flow deposit (GVP/PHIVOLCS) | Andesite | **None found** |
| Tambo Quemado (Bolivia) | Unknown | Rhyolite (GVP) | **None found**; rhyolite is a poor fit |
| Huaynaputina 1600 (reference) | 1600 CE, historical; bulk tephra 13–14 km³, VEI 6 (Prival et al. 2020, *Bulletin of Volcanology* 82: 7, abstract) | Dacite | Not retrieved: Prival 2020 and Adams et al. 2001 are paywalled. Check ice-glass work. |
| **Long Island / Tibito (reference)** | 1665–1668 CE (Firth et al. Table 4, after Blong & Kurbatov 2020) | Basaltic andesite (Matapun Beds) | Yes, see below |

**Tibito Tephra glass:**
- Source: Firth, Blong, Haberle et al., *The Holocene* 35: 234–248, open access. Table 3, anhydrous-normalised means, read via text fetch. P2O5 and Cl are not reported.
- 22 site means. SiO2 ranges from 54.6 to 58.1. Three representative rows:

| Site / sample | n | SiO2 | TiO2 | Al2O3 | FeOt | MnO | MgO | CaO | Na2O | K2O |
|---|---|---|---|---|---|---|---|---|---|---|
| Kuk RB-87 | 25 | 55.07 | 1.04 | 14.93 | 12.08 | 0.29 | 3.97 | 7.33 | 3.24 | 1.97 |
| Kutubu KTB-7/17–20 | 16 | 56.38 | 0.87 | 15.15 | 11.13 | 0.26 | 3.53 | 7.41 | 3.24 | 1.91 |
| Ambra A1 | 21 | 56.70 | 0.81 | 15.18 | 10.90 | 0.28 | 3.10 | 7.08 | 3.39 | 2.11 |

Tibito is a high-Fe basaltic-andesite glass, quite unlike Witori W-H glass.

## 6. Quick scan of other young (<300 yr) arc deposits

This was a quick web search only, a few minutes per region. "None found" means no published glass analysis of a young deposit turned up. It does not mean none exists.

| Region | Volcanoes | Result |
|---|---|---|
| Halmahera | Gamalama, Makian, Gamkonora, Ibu, Dukono, Jailolo | None found |
| New Britain (other) | Hargy, Lolo, Bola, Garbuna | None found. Dakataua: Dk tephra glass above, but c. 1300 BP. GVP lists later Dakataua activity (1895) without glass data. |
| Bougainville | Balbi, Loloru | None found |
| Bougainville | Bagana | Whole-rock only: "Andesites of Bagana volcano … reference andesite composition" (Bultitude et al., data.gov.au). Not glass, not checked. |
| SE PNG | Lamington, Victory, Waiowa | None found (Lamington 1951 is outside the window) |
| Tonga | Hunga (pre-2022), Home Reef, Metis Shoal, Fonuafo'ou | None found for pre-1900 deposits. Only 2009, 2014–15 and 2022 eruption products are analysed. |
| Sangihe / Sulawesi | Awu, Ruang, Banua Wuhu, Soputan | None found |
| Banda | Gunung Api/Banda Api, Teon, Nila, Serua, Manuk | None found. An EarthChem Banda Arc compilation is whole-rock only (ecl.earthchem.org id 1499). |
| PNG highlands | — | Firth et al. 2024: no tephra younger than Tibito at 17 sites. Blong 1982 Upper Wage post-Tibito ash: XRF trace elements only (see oral_history_melanesia.md). |

## Bottom line

**Witori W-H6 is the only candidate with published glass data.**
- Composition: low-K rhyolitic glass, SiO2 about 72.0, K2O about 1.2, CaO about 3.6, FeOt about 3.8, Na2O about 4.2.
- Its age is only bracketed: post-1426 cal AD and older than W-H7 (?1914). The GVP "1800" is a tephrochronological guess, and VEI 4 suggests a modest sulfur yield.
- **Tutupaca 1802:** whole-rock is high-K dacite (K2O 2.9–3.7) and the glass is described only as "rhyolitic", with no numbers. It was a small eruption (≥VEI 3, about 0.07 km³ of pyroclastic deposits).
- **Ticsani:** the youngest pumice fall is VEI 2–3, 0.015 km³, high-K dacite.
- **Putana, Victory, Cabalían, Tambo Quemado:** no compositional data.
