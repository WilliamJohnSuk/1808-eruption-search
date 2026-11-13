---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: science_alternatives
date: undated
---

# Scientific data for the 1808/09 eruption: inventory and reanalysis (round 6, 16 Oct 2026)

Thread: "What kind of scientific data could shed more light on this?" Scripts: `scripts/round6/`. Data written to `data/`.

## 0. Access from Claude's cloud container (tested 16 Oct, 15:20–15:45 UTC)
- **Bash egress:** GitHub (git clone of public repos, but not Git LFS objects of unattached repos), raw.githubusercontent.com, AWS S3 open-data buckets (NOAA GHCN-Daily `noaa-ghcn-pds` works), PyPI. **Refused:** PANGAEA, NCEI/NOAA paleo (also the LTRR mirror), Zenodo, figshare, Kaggle, Hugging Face, Met Office, DWD, CRU/UEA, CEDA, NCAR RDA, Arctic Data Center, media.githubusercontent.com (LFS), historicalclimatology.com. BigQuery's public ICOADS needs credentials, which we don't have.
- **WebFetch:** reads PANGAEA landing pages and the start of data files, but a quote limit makes it useless for numeric tables. NCEI pages return only the app shell.
- **William's Mac (Terminal curl):** all of the above are public. Two download commands were sent in the thread at 15:27 and 15:40 UTC: CLIWOC21.tsv, Recife register, NEEM-2011-S1 2 cm, San Fernando SF1799-1813, CLIWOC zip. Target folder: `~/Downloads/1808-9 Volcano Project/data/`.
- The device VM (`device_bash`) has no internet, but it can read the Downloads folder.

## 1. Reanalyses done now

### R1. East India Company logbooks: monthly tropical marine air temperature (new analysis)
- **Data:** github.com/oldweather/EEIC `imma/` (CDMP-keyed EIC logs 1789–1834, 894 files), cloned here. Noon air temperature, 190,607 obs; 128,144 between 30°S and 30°N.
- **Method:** anomaly against a 10°×10° box × calendar-month climatology built from EEIC itself, excluding 1809–12 and 1815–18. Boxes with fewer than 30 obs are dropped. Output: `data/eic_tropical_air_temp_monthly_1789-1834.csv`, plot `data/eic_tropical_air_temp_monthly_1805-1819.png`.
- **Result.** Tropical anomalies are about 0 to +0.3 °C through Nov 1808: Sep −0.38, Oct −0.05, Nov +0.31 (11 ships), Dec +0.24 (2 ships only). Then they **drop to −1.32 in Jan 1809 (8 ships)** and stay at −0.3 to −0.65 every month from Feb 1809 to Mar 1810 (−0.78). Annual means: 1808 +0.01, 1809 −0.55, 1810 −0.24, 1816 −0.46 (consistent with Brohan et al. 2012).
- **Within-voyage test.** This removes thermometer and exposure bias between ships. For each voyage with ≥10 tropical obs both in Aug–Nov 1808 and in Jan–Apr 1809, the mean change is **−0.65 °C (17 voyages)**. The same test for every other year 1789–1833, excluding volcanic years, gives a null of +0.08 ± 0.28 (39 years, most negative −0.39). Without the outlier Lord Keith (−3.1, Bay of Bengal) the change is still about −0.49, colder than any null year.
- **Sliding 3-month step test** (within-voyage, null from 415 non-volcanic months: mean +0.02, sd 0.28, 1st percentile −0.61). The step is largest when the split falls at **1 Dec 1808 (−0.82; −0.69 without Lord Keith)** or **1 Jan 1809 (−1.00; −0.60)**. Splits from Jul to Nov 1808 show no step. For calibration, Tambora (eruption 10 Apr 1815) gives its largest step at a split of **1 Nov 1815 (−0.59)**, about 7 months after the eruption.
- **Where.** The Jan 1809 cold anomalies come from ships at 80–90°E in the Bay of Bengal and eastern equatorial Indian Ocean (Ocean, Sir Stephen Lushington, Union, Lord Keith, Sir William Bensley, Harriet). Ships off SE Africa and in the S Atlantic were near normal.
- **Interpretation (inference; revised after R4, see below: the NEEM core argues against a mid-1808 eruption).**
  - Tropical ocean-surface cooling began in Dec 1808–Jan 1809. That is consistent with a veil present by late 1808.
  - If the lag between eruption and step were the same as Tambora's (about 7 months), the eruption would fall around **May–Jun 1808**. That matches Chenoweth's (2001) Mar–Jun 1808 from "Malaysian" temperatures and argues for an earlier eruption than the conventional 4 Dec 1808.
  - Three cautions limit this. The lag is calibrated on one event, and Tambora's step is itself barely significant. Only 8 ships sample Jan 1809, concentrated in one region. And an abrupt one-month drop of 1.3 °C looks more like regional weather (NE-monsoon or Indian Ocean Dipole) than a radiative response.
  - Supporting point: Camelia et al. (EGU26-20293, abstract) find "pronounced" cooling in monthly coral Sr/Ca from the NE Indian Ocean starting about 1809, the same region.
- **Verification level:** computed result, reproducible (scripts `eeic_at.py`, `eeic_onset.py`, `eeic_slide.py`). Its *meaning* is a weak-to-moderate inference. Not peer reviewed. Novelty: Brohan et al. (2012) published annual values only. No monthly onset analysis was found in the literature reviewed.

### R2. Diurnal temperature range, Milan and Prague (GHCN-Daily, S3)
- Only four GHCN-Daily stations cover 1808–09: Milan (ITE00100554, Tmax/Tmin), Prague-Klementinum (EZE00100082, Tmax/Tmin), Hohenpeissenberg (precipitation only) and Palermo (precipitation only). A veil should lower the diurnal range (DTR) by cutting daytime sunshine.
- **Result: no signal.**
  - Milan DTR anomaly: Dec 1808 +0.77, Jan 1809 −0.32, Feb −0.22, Mar +0.93.
  - Prague: Dec 1808 +0.77, Jan 1809 +1.10, Feb +0.58.
  - Tambora control: Milan 1816 −0.19, Prague −0.51, so even Tambora barely registers. The test has little power: winter DTR is dominated by cloud, and these are fixed-hour readings rather than true max/min.
- Output: `data/milan_prague_diurnal_range_monthly_1785-1830.csv`. **Verification: computed. Negative, low power.**

### R3. CLIWOC weather text, Sept 1808 – Jun 1809 (cleaned copy)
- Source: github.com/jburnford/CLIWOC_work `cleaned/cliwoc_cleaned.parquet` (all 287,113 CLIWOC 2.1 records). It includes `Weather` and `StateSea`, but **not** `OtherRem`, `Clearness`, `ShapeClouds` or `LifeOnBoard`, which need the full TSV.
- **Coverage 1 Sept 1808 – 30 Jun 1810:** about 20 voyages and 2,000 daily records. British (EIC and RN): Penelope, Tigris, Townsend, Earl Spencer, Neptune, Swiftsure, Perseverence, Dover Castle, Glatton, Windham, Acasta, Nisus. Spanish: Mercurio (Cádiz–Rio, Jul 1809–Feb 1810). Dutch: Havick (Batavia–Europe, Nov 1809–Feb 1810).
- **Result: nothing.** In 799 records Sept 1808–Jun 1809, 508 have an empty weather field. The rest are FINE, PLEASANT, CLOUDY, UNSETTLED, THICK (2), SULTRY and CLOSE. There is no haze, smoke, dark, red, dim or ash wording. Text dump: `data/cliwoc_cleaned_weather_text_1808-09_1809-06.txt`.
- **Ships covering the key windows:**
  - HMS Penelope, off New England 1–9 Nov 1808 (36.8–42.8°N, 70°W): 1 Nov "AM FINE", heavy sea 4–5 Nov, other days blank. This is the coordinator's York Factory / Salem darkness window: **no darkness is keyed**, but the remarks field is still unread.
  - Tigris, Madras to England: Bay of Bengal 1 Nov 1808, crossing 0°S on 11 Nov, at 18–24°S, 63–79°E on 1–10 Dec, at the Cape Jan 1809. Weather mostly blank or fine. "Immense seas" on 21 Nov at 9.6°S 90.7°E.
  - Townsend, Rio to Falmouth: crossed the equatorial Atlantic 2–31 Dec 1808 at about 30°W, "fine pleasant weather" throughout; "climate much cooler" on 22 Dec at 12.8°N, which is ordinary.
- **Verification: computed, negative for the keyed weather text. The remarks fields are pending the full TSV.**


## 1b. Reanalyses after William's downloads (16 Oct, 16:00–16:25 UTC)
Files are in `~/Downloads/1808-9 Volcano Project/data/` and were staged: CLIWOC21.tsv, cliwoc21-data.zip, neem2011s1_2cm_PANGAEA_940553.tab, SF1799-1813_1.txt, recife_PANGAEA_872369.tab.

### R4. NEEM-2011-S1, 2 cm (sub-annual): when the 1809 sulfate reached Greenland
- Output: `data/neem2011s1_2cm_1804-1819.csv`; plot `data/neem2011s1_sulfur_1809_vs_tambora.png`.
- Background S 1795–1808: mean 14.4 µg/kg, sd 5.6, 95th percentile 25.
- **Winter 1808/09 is normal.** S was 11–14 from Nov 1808 to Mar 1809, and the spring 1809 maximum of 19.7 matches the spring 1808 maximum (21.4). There is no excess before about Aug 1809.
- **The 1809 sulfate starts rising at about 1809.6–1809.7.** It crosses the 95th percentile at **1809.82 (about late Oct 1809, 28.6)**. It peaks at 69 in **spring–summer 1810** (1810.36–1810.43), with a second winter maximum of 51 at 1810.96.
- **Tambora (10 Apr 1815) at the same core:** the threshold is crossed at 1815.87–1815.96 (Nov–Dec 1815), about **7–8 months after the eruption**, and the peak (100) comes at 1816.26.
- **Seasonal position:** the 1809 sulfate arrives about 2–4 months earlier relative to the Na winter maximum than Tambora's does.
- **Inference.** By the Tambora analogy, the 1809 eruption falls around **Jan–Mar 1809 (±a few months)**. A December eruption would reach Greenland faster, because NH-winter stratospheric transport is strongest, so a Dec 1808 date also fits. **An eruption in May–Jun 1808 does not fit**: its sulfate would have reached NEEM in winter 1808/09, and that winter is clean.
- So this **contradicts the mid-1808 reading of R1** and agrees with Cole-Dai's Feb 1809 ±4 mo and with a veil in Bogotá by 11 Dec 1808.
- Black carbon in Nov 1808 is low (0.4–0.6 µg/kg), so NW Greenland shows no large smoke pulse. That says little about Salem or York Factory, which are far away.
- Ce and Mn show no shard-like spike in 1809–10 beyond the dust season.
- The double peak (spring 1810, then winter 1810/11) has the same shape as Tambora's (spring 1816, then winter 1816/17). **It is a deposition pattern, not evidence of a second eruption.**
- **Verification:** computed from the published dataset on its published layer-counted age scale, where sub-annual ages are interpolated between annual markers. One core only. Inference moderate.

### R5. CLIWOC full file (OtherRem, Clearness, EncRem): Sept 1808 – Jun 1810
- In the window there are 1,765 records from 14 voyages: 12 British, plus Mercurio (Spanish) and Havick (Dutch). Filled fields: Clearness 880, Weather 599, Precipitation 417, EncRem 851 (all "convoy/fleet in company"), and OtherRem only 13 (navigation and anchoring notes).
- **No volcano, ash, pumice, earthquake, bang, red-sun, dim-sun or smoke remark in any field.** Mercurio (Jul 1809) has "horizontes calimosos" off Cape Verde, which is ordinary.
- **Haze test on English Clearness entries.** The baseline is the same calendar month, the same region, and all other years 1750–1854.
  - Tropics 30°S–30°N, Dec 1808 – Feb 1809: **14 of 38 hazy (37%) against 12.7% expected (P≈1e-4)**.
  - Tropics, Sept–Nov 1808: 3 of 81 hazy (4%, below normal).
- **The excess is almost entirely one ship.** The Falmouth packet **Townsend** (Capt. Cock; NMM Greenwich NAI/3/17) sailed from Rio to Falmouth along about 30°W. She logged "hazy" on 10 Dec 1808 at 16°S, then on 17, 18, 19, 20, 21, 22, 24, 25 and 29 Dec between 3°N and 28°N, and again on 6–9 Jan 1809. In her box (0–30°N, 40–20°W) in December, other years are 9.5% hazy (358 obs, 44 ships). Without Townsend, the tropical Dec–Feb excess disappears (3 of 21, P = 0.5).
- Two cautions:
  - Townsend's keeper wrote "hazy" freely: 58% of all her days, including off Rio on 2 Dec and off Portugal in January, and she has no other CLIWOC voyage to calibrate against.
  - Her Dec–Jan track runs through the Harmattan/Saharan-dust belt. That belt is part of the regional baseline, but 1808–09 could simply have been a dusty winter.
- **The timing is striking but not evidence:** her first tropical haze entry (10 Dec) is one day before Caldas's 11 Dec.
- **Tigris** (EIC; BL IOR/L/MAR/B/219D) logged "hazy" or "thick hazy" on 16, 17 and 20 Dec 1808 at 27–30°S, 41–51°E, SE of Madagascar: 3 of 6 days against 15% (P = 0.05). She also logged "gloomy" on 28 Nov 1808 (14°S 87°E) and 13 Jan 1809 at the Cape. Weak.
- **HMS Penelope** (Capt. John Dick; NMM SPN/9), NW Atlantic 35–45°N, 75–60°W. "Hazy" on **3, 5, 6 and 9 Nov 1808** at 38.6–42.8°N, 64–70°W, which is the window of McNab's darkest day (4 Nov, York Factory) and Bentley's darkness (8–12 Nov, Salem). That is 4 of 8 days, against 22% for November in that box (P = 0.08). Penelope's keeper used "hazy" for 36% of days in 1809, so this is **weak**. No darkness, smoke or red sun is written.
- Output: `data/cliwoc21_full_text_1808-09_1810-06.csv`.
- **Verification:** computed. Negative for explicit volcanic phenomena. The haze excess is a single-observer effect, so weak. The original logs (NMM NAI/3/17 Townsend; BL IOR/L/MAR/B/219D Tigris; NMM SPN/9 Penelope) could be checked for fuller remarks.

### R6. San Fernando (Cádiz) observatory, 1799–1813: baseline for "calimoso"
- One reading a day at 14h from 1809 (8h and 14h in 1805–08; 1802–04 missing). In winter (Nov–Mar), calimoso days by winter: 1800: 4, 1805: 2, 1807: 1, **1809: 10**, 1813: 7, all others 0.
  - Jan 1809 (3 days) and Feb 1809 (6 days) rank first among all Januaries and Februaries.
  - **Every one of the 10 days had ESE/SE wind** and a warm afternoon (17–19 °C in Jan–Feb).
  - In summer, calimoso is common (July 1808: 18 days).
- **Reading:** this is Saharan-dust calima brought by levante/SE winds. It is unusual in frequency for winter 1809, but the wind pattern fits dust, as the dataset's authors concluded. **Not a veil signal.** Verification: computed; probably negative.

### R7. Recife register 1808–10 (indoor, three readings a day)
- Dec 1808 – May 1809 is about 0.3 °C cooler than the same months of 1808. The afternoon-minus-morning range is *larger* (+0.4 to +0.9), the opposite of veil dimming.
- There are only two years of baseline, a gap from Nov 1809 to Apr 1810 (instruments moved), and an indoor exposure. **Inconclusive.**

## 2. Dataset inventory (one line each)
Columns: what it is / URL / reachable here? / analysed for 1809 by whom / what a reanalysis could add.

### Ice cores
- **eVolv2k** sulfate composite (Toohey & Sigl 2017, ESSD 9:809) / https://doi.org/10.5194/essd-9-809-2017 / text yes, data needs the Mac / basis of the 19.3 Tg S / nothing to add.
- **NEEM-2011-S1, 2 cm continuous aerosol** (S, Na, NO3, NH4, BC, Ce, Mn; Sigl & McConnell 2022) / https://doi.org/10.1594/PANGAEA.940553 / Mac (requested) / annual totals in Sigl 2013/2015; **sub-annual position not published as far as found** / can place the first 1809 sulfate in its season, using the Na winter and NH4/BC summer markers, and compare it with Tambora (eruption Apr 1815). BC and NH4 can test the Nov 1808 smoke hypothesis (Salem, York Factory). Ce and Mn spikes may mark the tephra layer.
- **WAIS Divide WDC06A + NEEM + Humboldt** (Sigl et al. 2013, JGR) / https://doi.org/10.18739/A2TH15 (Arctic Data Center) / Mac / annual / the same seasonal test for Antarctica, showing which hemisphere received sulfate first. That points to the side of the equator the source lies on.
- **WDC monthly nssS** (Sigl et al. 2025, PANGAEA 974948) / covers only 1530–1710 / – / it shows that a monthly WDC product exists; ask Sigl for the 1805–1815 segment.
- **Dome C sulfur isotopes** (Gautier et al. 2019) / PANGAEA 895169 / already read by the project (nonvolcanic_alternatives.md) / Δ33S +0.19 (1809.7), +0.05 (1811.9), −0.23‰ (1813.7) / done.
- **South Pole Δ33S** (Cole-Dai et al. 2009, GRL) and the Feb 1809 ±4 mo timing (Cole-Dai 2010) / literature / used / –.
- **Δ33S time-evolving pattern** (Hutchison et al. 2023, workshop abstract) / data unpublished / – / ask the authors. This is the most direct test of "two eruptions".
- **TUNU2013** (Plunkett et al. 2023) / shards not analysable / – / –.
- B40 (NGT), other Greenland cores: not checked this round.

### Cryptotephra
- **Eclipse Icefield, Yukon, dacitic** (Yalcin et al. 2006, GRL 33:L14706); **Antarctic andesitic** shards (Dai et al. 1991; Kurbatov et al. 2006 Siple Dome); **Dome C / South Pole "Indonesian-like"** (as reviewed by Plunkett et al. 2023) / papers mostly paywalled here / analysed only against a few candidates.
- **Possible reanalysis:** compile the shard oxide tables and compare them with GEOROC (https://georoc.eu) and the Kuril/Alaska/Indonesia glass compilations. A discriminant test such as K2O vs SiO2, or FeO/MgO, against every arc with a VEI ≥ 4 candidate. GEOROC needs the Mac. **Not done**, because the shard tables are not in hand. William could download the Yalcin 2006 supporting info and the Kurbatov 2006 tables through Syracuse or Le Moyne.
- **Note (inference):** Leland et al. (2023, Paleoceanogr. Paleoclimatol. 38) put the extreme 1809–10 cold centre over the Gulf of Alaska, Wrangell–St Elias and southern Yukon. That is the same area as the Eclipse dacitic tephra. They explain it by circulation (weak Aleutian Low, negative PDO). A local Alaskan eruption would also fit the overlap. This is worth stating, but it is not evidence.

### Tree rings
- **N-TREND** (Wilson 2016; gridded Anchukaitis et al. 2017) / NOAA study 19743 / Mac / Timmreck et al. 2021: 1810 −0.87 °C (S), "wave-2" pattern already visible in 1809 / little to add except mapping 1809 against 1810.
- **NVOLC v2** (Guillet et al. 2017) / NOAA study 21090 (`guillet2017nhtemp.txt`, `guillet2017nhtempgrid.nc`) / Mac / 1810 −0.77 °C / –.
- **Schneider et al. 2015 MXD** / NOAA / Mac / −0.15 / –.
- **Leland et al. 2023 NW North America network** / St Andrews repository / text yes / extreme cold in the Gulf of Alaska and Yukon / see the tephra note.
- **Frost rings:** no published 1809 or 1810 frost-ring event was found in a quick search; not checked further.
- **What the tree rings say about timing:** NH summer 1809 is already cool in N-TREND (S). So the aerosol was present by Jun–Aug 1809, which fits any eruption up to early 1809. Tree rings cannot date the eruption to the month.

### Corals and speleothems
- **Camelia, Felis, Kölling, Scheffers & Chavanich, EGU26-20293** (https://meetingorganizer.copernicus.org/EGU26/EGU26-20293.html): monthly Sr/Ca and δ18O, NE Indian Ocean, from 1774. "Prolonged cooling and freshening from about 1809". Data probably unpublished. **This is the best target for month-level onset.** Ask Thomas Felis (MARUM) whether the monthly series shows cooling starting in late 1808, and compare it with R1.
- **Bicol, Philippines 228-yr coral** (ESSOAr 10.1002/essoar.10511034.1): its abstract names Tambora and Krakatau only; resolution not stated.
- **D'Arrigo et al. 2006 IPWP; Tierney et al. 2015 compilation; CoralHydro2k** (Walter et al. 2023 ESSD): NCEI, Mac / annual composites used by Timmreck 2021 / a compilation of only the *monthly* coral series spanning 1806–1812 could test the onset month across basins. Not done.
- **Speleothems:** at best annual, usually coarser. They cannot resolve months, so low value here.

### Early instrumental series
- **GHCN-Daily Milan, Prague** (S3, reachable): R2 done, negative.
- **Recife 1808–10, 3 obs a day, indoor T and pressure** (Domínguez-Castro et al. 2017; https://doi.org/10.1594/PANGAEA.872369) / Mac (requested) / published as data rescue, not analysed for the veil / the indoor thermometer limits a DTR test. A pressure or temperature anomaly from Dec 1808 can still be checked. Instruments moved Nov 1809.
- **San Fernando (Cádiz) 1799–1813**, including daily sky state (https://doi.org/10.5281/zenodo.7104289, file SF1799-1813_1.txt) / Mac (requested) / the authors noted "calimoso" days in Jan–Mar 1809 and dropped the volcanic reading / **baseline count of hazy days by month 1799–1813**, the test the interim summary asked for.
- **Mallorca 1808–09** and **EIC keyed weather**: already in `data/`. Haze frequency test done (negative, notes/eic_access.md).
- **HadCET daily mean** (Met Office) / Mac / mean only, no max/min before 1878 / low value.
- **Padua, Stockholm/Uppsala, Hohenpeissenberg temperature, Boston/Holyoke (Salem file at crudata.uea.ac.uk), Madras/Calcutta registers** / Mac or browser / Brönnimann et al. 2019 used station means / sky-state or sunshine remarks would be the useful part, not temperature.
- **Inventory of pre-1850 instrumental records** (Brönnimann et al. 2019, BAMS, "Unlocking pre-1850 instrumental meteorological records: a global inventory") / UB repository / text / it lists every known 1808–09 register, so use it to find tropical registers (Havana, Manila, Batavia, Calcutta, Bombay) with sky remarks.
- **20th Century Reanalysis v3** (starts 1806) and **ModE-RA** (monthly 1421–2008) / NOAA PSL, Mac / reanalysed fields exist for 1808–09 / they give the circulation context (e.g. NE monsoon Jan 1809 for R1), not the source.

### Ship logs
- **CLIWOC 2.1** / full TSV via the Mac (requested); cleaned copy on GitHub (reachable) / Können & Koek 2005 built it, and no 1809 search exists / R3 done for weather words. The **OtherRem, Clearness, ShapeClouds and EncRem** fields are still to search once the TSV arrives. Coverage for 1808–10 is thin, about 20 voyages.
- **ICOADS R3** (CLIWOC deck 730, US Maury, EEIC) / NCAR RDA ds548, Mac / numeric only, no remarks / a marine air temperature check like R1 across all decks.
- **EEIC** / GitHub (reachable) / Brohan et al. 2012, annual / R1 done (monthly).
- **RN logs (TNA ADM 51/52/53), EIC journals (BL IOR/L/MAR/B), whaling logs** / not digitised / the remarks columns are the real prize, but only by reading in person or ordering images.

## 3. Findings and verification levels (this round)
| # | Finding | Level |
|---|---|---|
| S1 | EIC tropical marine air temperature steps down in Dec 1808–Jan 1809, colder than any of 39 other years by the within-voyage test. The cold is concentrated at 80–90°E | Computed from keyed data. The meaning (eruption before Dec 1808, possibly mid-1808 by the Tambora-lag analogy) is an inference, weak to moderate |
| S2 | A Tambora-calibrated lag of about 7 months would put the eruption around May–Jun 1808, which supports Chenoweth 2001 | Inference from one analogue; weak. **Contradicted by S7 (NEEM): treat as unlikely** |
| S3 | Milan and Prague DTR show no veil signal Dec 1808–Mar 1809; Tambora control also weak | Computed; negative, low power |
| S4 | CLIWOC keyed weather text, Sept 1808–Jun 1809: no haze, dim-sun, red-sky, smoke or ash wording; Penelope off New England 1–9 Nov 1808 shows nothing | Computed; negative; remarks fields pending |
| S5 | Monthly coral Sr/Ca from the NE Indian Ocean (Camelia et al. 2026 abstract) shows cooling from about 1809 in the same region as S1 | Literature (abstract only) |
| S6 | The NW North American cold core (Leland et al. 2023) overlaps the Eclipse Icefield dacitic-tephra site | Literature plus inference; not evidence of a source |
| S7 | NEEM 2 cm: winter 1808/09 is clean. 1809 sulfate arrives about Aug–Oct 1809, 2–4 months earlier in the season than Tambora's, which came 7–8 months after the eruption. That implies an eruption around Dec 1808–Mar 1809 and rules against mid-1808 | Computed from published data; moderate inference; one core |
| S8 | CLIWOC full remarks Sept 1808–Jun 1810: no volcanic phenomena in any field | Computed; negative |
| S9 | Packet Townsend logs haze almost daily, 10 Dec 1808 – 9 Jan 1809, in the S and equatorial Atlantic at about 30°W, against a 9.5% regional baseline. Her keeper used "hazy" freely | Computed; single observer; weak; original log NMM NAI/3/17 |
| S10 | HMS Penelope logs haze off New England on 3, 5, 6 and 9 Nov 1808 (the York Factory/Salem dark days); no darkness written | Computed; weak (P = 0.08) |
| S11 | San Fernando calimoso Jan–Feb 1809 is the most of any winter 1799–1813, but every case has SE wind and warmth, so it is Saharan dust | Computed; probably negative |
| S12 | Recife indoor register: no dimming signal | Computed; inconclusive |

## 4. Search log
| Tool | Query / URL | Result |
|---|---|---|
| curl | PANGAEA, NCEI, Zenodo, figshare, Met Office, DWD, CRU, CEDA, RDA, historicalclimatology, media.githubusercontent | proxy-refused |
| curl | noaa-ghcn-pds S3 inventory | 4 stations cover 1808–09 |
| git | stvno/stvno.github.io (CLIWOC21 TSV, LFS) | pointer only; LFS refused |
| git | jburnford/CLIWOC_work | cleaned parquet, 287,113 records |
| git | oldweather/EEIC | 894 IMMA files |
| bq | bigquery-public-data:noaa_icoads | no credentials |
| WebSearch/WebFetch | Timmreck 2021; Leland 2023; EGU26-20293; PANGAEA 940553, 974948, 872369; LTRR readmes ntrend2017grid, guillet2017 | read (metadata) |
