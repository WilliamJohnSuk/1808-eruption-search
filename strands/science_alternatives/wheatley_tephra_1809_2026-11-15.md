---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: dataset read in full [data file]; all comparisons are Claude's calculations, not checked by a person
strand: science_alternatives
date: 2026-11-15
---

# Kurbatov 2017 / Wheatley "Antarctic Ice Core Tephra Analysis" (USAP-DC 601038): the 1809 shards (15 Nov 2026)

Register B82. Closes hand item U1. William downloaded the file and uploaded it on 15 Nov 2026.

## 1. What the file is

- **Dataset:** Kurbatov, A. V. (2017), "Antarctic Ice Core Tephra Analysis", U.S. Antarctic Program Data Center, doi:10.15784/601038. File `SDWheatley_tephra-data.xlsx` (8.0 MB; MD5 96cdbe9799c134e770f2b616e37d3587, which matches the MD5 printed on the landing page, so this is the published file unchanged). Created 2 Feb 2017, last saved 3 Aug 2017. The analyst named in the file name is Wheatley (University of Maine MS work in Kurbatov's group; see B56, T2). NSF awards PLR-1142007 (University of Maine), PLR-1142069 (New Mexico Tech), PLR-1042883 (RICE).
- **Licence:** CC0 1.0 (landing page read via WebFetch 15 Nov 2026). Hosting the numbers here is allowed; we credit the dataset anyway.
- **Cores:** WAIS Divide WDC-06A, RICE (Roosevelt Island), SPRESSO (South Pole), SPICE-14 (South Pole). All Antarctic.
- **Intervals:** 1991, 1963, 1815, 1809 and 1257 CE.
- **Method:** Tescan Vega XMU SEM with an Apollo SSD40 EDS detector, 15-20 kV, carbon coat; standards Smithsonian VG-568 rhyolite glass and A99 basalt glass. One spot per particle; particles 5-20 µm. Stated error 2%, detection limit 2%. Eight oxides (SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O) normalised to 100%. **No trace elements** (no Zr, Nb or REE), and no Cl, S, MnO or P2O5.
- **Dating:** layer-counted core timescales (WD2014, Sigl et al. 2016; RICE, Winstrup et al. 2017/2019; SPICE from D. Winski; SPRESSO from E. Korotkikh).
- Each shard has an IGSN (IESDW0001-IESDW0096). The file also holds 10 embedded SEM images, not copied here.

All 96 shard rows are in `data/kurbatov_wheatley_2017_antarctic_tephra_shards.csv` (rounded to 2 decimals). The original xlsx is not committed because of its size; get it from the DOI.

## 2. The "1809" shards [data file]

| Shard | Core | Sample depth | Age the README gives | Size µm | SiO2 | TiO2 | Al2O3 | FeO | MgO | CaO | Na2O | K2O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 316-01 | WDC-06A | 60.12-60.259 m | 1812 | 15 | 75.47 | 0.10 | 12.74 | 1.05 | 0.11 | 0.56 | 7.11 | 2.86 |
| 316-02 | WDC-06A | same | 1812 | 10 | 76.04 | 0.52 | 12.73 | 1.49 | 0.22 | 1.28 | 2.58 | 5.14 |
| 316-03 | WDC-06A | same | 1812 | 20 | 72.32 | 0.39 | 15.08 | 1.86 | 0.39 | 1.69 | 5.85 | 2.41 |
| 316-04 | WDC-06A | same | 1812 | 10 | 74.01 | 0.12 | 14.42 | 1.17 | 0.41 | 1.24 | 6.23 | 2.40 |
| 140-01 | SPRESSO | 29.50-29.55 m | 1811 | 7 | 73.07 | 0.23 | 15.07 | 1.46 | 0.28 | 0.90 | 6.37 | 2.61 |
| 140-02 | SPRESSO | same | 1811 | 5 | 74.85 | 0.07 | 12.89 | 0.97 | 0.24 | 0.79 | 7.43 | 2.77 |
| 140-03 | SPRESSO | same | 1811 | 15 | 75.97 | 0.18 | 13.20 | 1.33 | 0.09 | 0.95 | 5.44 | 2.83 |

Mean of all 7 (Claude's calculation): SiO2 74.5 ± 1.3, Al2O3 13.7, FeO 1.3, MgO 0.25, CaO 1.1, Na2O 5.9 ± 1.5, K2O 3.0. WDC and SPRESSO means agree within 0.2 wt% SiO2.

Reading the table:
- **This is rhyolite, not andesite.** Every shard is 72-76% SiO2 with about 1% FeO. The 1809 glass the project has used so far (Dome C and South Pole PS1809, B50, B52) is iron-rich andesite of about 60% SiO2 and 8-9% FeO. These shards are a different magma.
- **The two cores agree with each other.** Shards from West Antarctica (WAIS Divide) and the South Pole give the same composition. That points to one source for these shards, not two local accidents (Claude's inference).
- **The dates are 1811-1812, not 1809.** The sheet is headed "1809 C.E. Tephra", but the README gives 1812 for the WDC sample and 1811 for the SPRESSO sample. The file does not say whether the samples were cut from the 1809 sulfate peak or from just above it. We found no statement on this in the file or on the landing page.
- **Na2O spread is large** (2.6-7.4%). This is usual for EDS spots on 5-20 µm shards, where sodium moves under the beam. Na2O and K2O are therefore the least reliable oxides here.
- No RICE or SPICE shards are listed for 1809.

## 3. Comparison with the 1809 ice glass and the candidates (Claude's calculation, not checked by a person)

Method: Borchardt similarity coefficient (mean of min/max ratios) on SiO2, Al2O3, FeOt, MgO, CaO, Na2O and K2O, the same method as `scripts/glass_similarity_2026-10-26.py`. Script: `scripts/wheatley_tephra_2026-11-15/compare.py`. Values near 1 mean the same glass; values above about 0.9 are usually needed before tephra people call two glasses a match. Low-MgO rhyolites score low against almost anything, so treat the numbers as a ranking only.

**Control first: the 1815 shards.** The same file's 1815 interval (11 shards, SPICE-14 and SPRESSO) averages SiO2 61.2, Al2O3 20.3, K2O 3.3, and scores **0.83** against the proximal Tambora 1815 glass; the two best SPICE shards score 0.88 and 0.91. So the method picks Tambora out of the 1815 ice in this same lab's data. That makes the low 1809 scores below more likely to be a real difference than an artefact (Claude's inference).

**1809 shards (mean of 7) against:**

| Comparison glass | SC |
|---|---|
| Siple Dome A 33.75 m, 1810 trachyte (no MgO) | 0.72 |
| Eclipse Icefield 1809 | 0.62 |
| New Ireland Basin ash, Group B 0.068 m | 0.62 |
| Witori W-H5 / W-H6 glasses | 0.55-0.59 |
| **Dakataua** Buludava and Volupai tephra glass | 0.56-0.58 |
| South Pole PS1809 andesite | 0.55 |
| Tambora 1815 | 0.53 |
| Dome C 1809 andesite | 0.49 |
| Long Island Tibito glasses | 0.46-0.47 |

No candidate in `data/glass_candidates.csv` scores above 0.62. Per candidate:
- **Dakataua / Makalia:** the published Dakataua tephra glass is 66.5% SiO2; the shards are 74.5%. Not a match (0.58). This neither helps nor hurts Dakataua for the andesite.
- **Gaua:** the project holds only whole-rock data (GEOROC mean about 53% SiO2, maximum about 59%). A basaltic-andesite volcano is an unlikely source for 74% glass, but whole rock and glass are not the same thing (Claude's inference).
- **Cabalían:** no analysed glass or whole-rock major elements in the project files. Cannot be tested.
- **Others:** the high-K2O (about 3%) of these shards is unlike the low-K New Britain glasses (Witori, New Ireland Basin Group C). The Banda Besar caldera rhyolites (73-74% SiO2) are close in silica, but the project has no full oxide analysis to score (see `data/glass_candidates.csv`).

## 4. What this changes (Claude's interpretation)

1. U1 was the best hope for more 1809 andesite shards from the Antarctic. It does not give them. It adds a second, rhyolitic shard population in two Antarctic cores, dated 1811-1812 on those cores' timescales.
2. Helmick et al. 2022 (B56, T1) already reported "subtropical (dacite-rhyolite)" particles in the SPC14 1809 and 1815 intervals. The Wheatley shards fit that description. So rhyolite near the 1809 layer is now seen in three cores (SPC14, SPRESSO, WDC). Whether it comes from the 1809 eruption, a later eruption (1811-1812) or a mix is open.
3. The andesite ranking (F20, F34) does not change: it rests on Dome C and South Pole PS1809, and these new shards do not contradict it, since they are dated later and are a different magma.
4. The trace-element gap stays: this file has no Zr/Nb, so the GEOROC trace comparison still cannot be run on any 1809 shard.

## 5. Open points

- Where 60.12-60.26 m in WDC-06A sits relative to the 1809 sulfate peak on WD2014. The WDC sulfate series (U5) would answer it.
- The file has two identical rows in the 1815 sheet (338-05 and 338-06), and shard 133-17 has 0% TiO2, CaO and K2O (probably a failed spot). Neither affects the 1809 rows.
