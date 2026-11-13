---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: candidates
date: 2026-11-02
---

# Trace-element lookup table for the 1809 candidates (T12 = creative option 7), 2 Nov 2026

**Purpose.** The major elements of the 1809 ice glass (B50, B52) fit several arc andesites about equally well. They do not name the volcano. Glass in the ice that is measured for trace elements by LA-ICP-MS (U90-U92; nobody has published such data) would compare against the table below. We fix the comparison in advance so that a future measurement cannot be fitted after the fact.

**Data.** GEOROC precompiled arc files downloaded Sept 2026, on the Mac in `data/georoc/`: Bismarck/New Britain, New Hebrides/Vanuatu, Luzon (which includes Leyte and Camiguin), Halmahera, Banda, Sulawesi and Solomons. Samples are mostly whole rock. Selection: each group's samples with SiO2 55-68 wt%, which brackets the ice glass at c. 59-65 wt%; if fewer than 3 such samples exist, all of them. Script: `scripts/trace_lookup_2026-11-02/trace_ratios.py`. Output: `data/trace_ratio_lookup_2026-11-02.csv` (median and 25-75 % range of 14 ratios per group) and `data/trace_ratio_separation_2026-11-02.csv` (ratios whose 25-75 % ranges do not overlap, for each pair of candidates). All numbers are [calc] from GEOROC [text].

## 1. The lookup (medians; the full ranges are in the CSV)

| Candidate group | n (selected) | SiO2 | Zr/Nb | La/Nb | Ba/La | Th/La | La/Yb | Sr/Y |
|---|---|---|---|---|---|---|---|---|
| **Dakataua/Makalia (Willaumez, New Britain)** | 5 | 60.3 | **66** | 6.6 | 24 | 0.80? | 8.1 | 13 |
| Witori/Pago (New Britain) | 10 | 64.2 | 70 | 6.6 | 24 | – | – | 16 |
| **Gaua (Vanuatu)** | 24 | 57.2 | **43** | **8.2** | 30 | 0.18 | 9.2 | 24 |
| Ambrym (Vanuatu) | 12 | 60.1 | 33 | 4.1 | 40 | – | 5.4 | 12 |
| Kuwae/Tongoa/Epi (Vanuatu) | 17 | 60.7 | 38 | 4.5 | 39 | 0.17 | 5.9 | 12 |
| Tanna/Yasur (Vanuatu) | 80 | 58.0 | 70 | 9.6 | 39 | 0.16 | 5.4 | 17 |
| **Leyte (as a whole; Cabalían not separately sampled)** | 10 | 57.0 | **28** | 4.4 | 28 | – | 5.4 | 20 |
| Camiguin/Hibok-Hibok (N Mindanao) | 40 | 58.6 | 17 | 3.5 | 17 | 0.30 | 14.9 | 56 |
| Dukono/Todoko (Halmahera) | 3 | 59.3 | 67 | 7.4 | 32 | 0.15 | 3.9 | 30 |
| Ibu/Gamkonora (Halmahera) | 9 | 61.1 | 35 | 4.0 | 35 | 0.25 | 3.6 | 12 |
| Nila/Teon/Serua (Banda) | 65 | 57.6 | 19 | 4.4 | 20 | 0.37 | 7.5 | 20 |
| N Sulawesi (Lokon, Soputan, Mahawu, Klabat, Tongkoko) | 26 | 60.4 | 40 | 3.4 | 19 | 0.35 | 2.9 | 9.5 |
| Bagana (Bougainville) | 11 | 57.0 | 20 | 2.5 | 25 | 0.11 | 6.1 | 49 |
| Savo (Solomons) | 34 | 63.0 | 34 | 2.6 | 70 | 0.65 | 11.4 | 146 |

(The Dakataua Th/La rests on very few values; treat it with caution.)

## 2. What separates the top three [calc]

- **Zr/Nb is the single best discriminator.** Dakataua is about 66, Gaua about 43 and Leyte about 28, and their 25-75 % ranges do not overlap pairwise.
- **La/Nb** separates Dakataua (6.6) and Gaua (8.2) from Leyte (4.4).
- **Ba/La and Sr/Y** separate Dakataua from Gaua as well.
- **A pre-registered reading [suggestion]** for 1809 ice glass at c. 60 % SiO2:
  - Zr/Nb ≥ 55 with La/Nb 6-7 points to New Britain (Dakataua or Witori) or Halmahera (Dukono). These two are then split by Sr/Y (13 vs 30).
  - Zr/Nb 38-50 with La/Nb ≥ 7 points to Gaua.
  - Zr/Nb ≤ 32 with La/Nb ≤ 5 points to Leyte/Cabalían, the Banda arc or Bougainville. These are split by Zr/Y and Sr/Y, but weakly.
  - Tanna stands apart with very high La/Nb (9.6) and Zr/Nb (70).
- **Pairs the table cannot split** with the incompatible ratios: Leyte vs Banda (Zr/Y only) and Leyte vs N Sulawesi (Sr/Y only). Both rest on ratios that crystallisation shifts.

## 3. Caveats

1. **Whole rock vs glass [inference].** Ratios of highly incompatible elements (Zr/Nb, La/Nb, Th/Nb, Ba/La, Th/La) carry over from whole rock to matrix glass within roughly ±10-20 % at these silica contents. Sr/Y, Zr/Y, La/Yb and Ce/Pb shift with plagioclase, amphibole and sulphide, so they are a second rank.
2. **Thin samples.** Dakataua/Makalia has 5 samples (with Talasea) and Dukono/Todoko has 3. "Leyte" is the island as a whole: no GEOROC sample is labelled Cabalían. Agung (Sunda arc) is not in the downloaded files. A Sunda-arc file download would add it: new item **U154** (Mac/Safari, GEOROC precompiled "SUNDA ARC").
3. **Measurement.** Nb in these andesites is about 1-3 ppm. On 10-30 µm ice shards, LA-ICP-MS gives perhaps ±20-30 % on Nb per shard [inference]. That still separates 66 from 43 from 28 if several shards are averaged.
4. This table ranks candidates. It does not prove a match, because a shard set could come from an unsampled volcano.

## 4. Next steps

- (William, Mac) U154: download the GEOROC precompiled Sunda-arc file into `data/georoc/`, then rerun the script (T27).
- (free, later) Add any published Cabalían or southern Leyte analyses (literature search; none in GEOROC) (T28).
- When ice-glass trace data appear (U90-U92), compare them using exactly the rules in section 2.
