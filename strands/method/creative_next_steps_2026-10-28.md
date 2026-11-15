---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: method
date: 2026-10-28
---

# Creative next steps: options, unusual sources and side mysteries (28 Oct 2026)

Thread "Think creatively about next steps". Written for William to pick from by number (options 1-25, side problems M1-M13). Everything below is either a result of this thread's own checks, with the verification level in square brackets, or a suggestion. Labels: **[page image]** read from a scan; **[text]** fetched text of a published paper or catalogue, not checked against a page image; **[calc]** Claude's calculation from downloaded published data; **[memory]** from Claude's training, not verified this session; **[speculation]** an idea, not a finding. Scripts and data for sections 2.1 and 2.3: `scripts/creative_next_steps_2026-10-28/`, `data/deposition_emulator_ratio_by_latitude_2026-10-28.csv`, `data/coral_footprint_1806-1816_2026-10-28.csv`. Register section B62.

## 1. Where the search stands (five lines, from the register and notes)

- About 19 Tg S reached both ice sheets at the same time, from the stratosphere (Δ33S). The Bogotá veil (11 Dec 1808) and Edo's red skies (from 9 Jan 1809), both page-image, date the eruption to about mid-November to early December 1808. We know of no account of the eruption itself.
- The 1809 ice glass is an iron-rich medium-K andesite (~60% SiO2). Major elements alone cannot pick the arc; low-K arcs (Tonga, the New Britain front, northern Banda) are out. No trace elements have been published for any 1805-12 ice glass.
- Priority list (B53): Dakataua/Makalia, Gaua, Cabalían; possible Agung, Todoko-Ranu, Dukono, Teon, Nila, northern Sulawesi.
- The documentary net is now very wide (Iberian, Dutch, German, British and American papers; EIC, Royal Navy, HBC and whaling logs; China, Korea, Ryukyu, Japan; Dutch Indies archives inv. 19, 20, 22) and almost wholly negative. The positive non-veil signals are the Java drought and rice failure of 1809, the Guangdong-Guangxi drought of 1809, the EIC marine air-temperature step of Dec 1808-Jan 1809, and now the corals (2.3).
- The physical evidence that could settle the question (ice-glass trace elements, a Lake Dakataua core, Gaua's youngest rim tephra, the H15 and Talos Dome ash) is in other people's hands.

## 2. New results from this thread's viability checks

### 2.1 The Greenland/Antarctic deposition ratio can be turned into a latitude band, once calibrated [calc]

**What was done.** Marshall et al. 2021 (JGR 126, e2020JD033578) published a statistical emulator of UM-UKCA simulations that gives the mean sulfate deposition on Greenland and on Antarctica for an eruption of any SO2 mass (10-100 Tg), latitude (26 values from 80°S to 80°N), injection height (16.5-26.5 km) and season (1 January or 1 July). The emulator grid (17,576 points per season) is on GitHub (cemac/volcanic-forcing-deposition, the release archived as Zenodo 10.5281/zenodo.4038013) and was downloaded and inverted here. The bipolar-lag note of 27 Oct (B55) could only quote the qualitative season effect from Toohey 2013; this is the first time the project has had numbers for it.

**Result 1: the raw emulator must not be used as it stands.** Taken at face value, the 1809 deposition (Greenland 25.9, Antarctica 25.1 kg/km², Sigl 2013 composites, ratio 1.03) is reproduced only by a January eruption at 17-30°S or a July eruption at 4-36°S. But the same emulator predicts that a Tambora-like eruption (8°S, 53-64 Tg SO2) put 1.3 (July) to 2.7 (January) times more sulfate on Greenland than on Antarctica, whereas the ice cores give 0.87 (Greenland 39.7, Antarctica 45.8 kg/km², Sigl 2015 via Marshall 2021 Table 1 [text, from B55]). The full UM-UKCA Tambora run in Marshall et al. 2018 (ACP 18:2307, Table 5 [text]) shows the same bias: Greenland 31, Antarctica 19 kg/km², ratio 1.6. So this model family puts about twice too much of a tropical eruption's sulfate on Greenland, and the raw inversion is pushed 15-20° too far south. Anyone who applies the published emulator to 1809 without this check will get the wrong hemisphere.

**Result 2: calibrated with Tambora.** Dividing the emulator's ratio by its own Tambora-like ratio (April approximated as the geometric mean of January and July, 1.90) and comparing with the observed 1809/Tambora ratio-of-ratios (1.2, range 0.9-2.2 across the core pairs and composites in B55) gives, for SO2 loads above 20 Tg (medians over injection height):

| Eruption latitude | January eruption: predicted 1809/Tambora ratio-of-ratios | July eruption |
|---|---|---|
| 23°S | 0.51 | 0.40 |
| 17°S | 0.77 | 0.50 |
| 10.5°S | 1.21 | 0.66 |
| 4°S | 1.99 | 0.88 |
| 2.4°N | 3.3 | 1.14 |
| 8.9°N | 5.0 | 1.52 |
| 15.4°N | 6.5 | 2.09 |
| 21.8°N | 7.6 | 2.9 |

The observed 1.2 (0.9-2.2) is matched by a January eruption between about 14°S and 3°S (best fit near 10°S), or a July eruption between about 4°S and 16°N (best fit near 5°N). For a late-November to early-December eruption, our date, the answer lies between the two columns but nearer the January one: roughly **12°S to 3°N, centre of mass near 5-8°S**.

**What it would mean for the candidates, if it holds.** Dakataua (5°S), the Banda arc (Teon, Nila, Serua, Banda Api, Gunungapi Wetar: 4.5-7°S), Agung (8°S), northern Sulawesi (1°N) and Halmahera (1-2°N) all sit in the band. Gaua (14°S) is at its southern edge. Cabalían (10°N) is outside it for any eruption between October and February, and fits only if the eruption happened in the middle of the year, which the Bogotá and Edo dates make unlikely. This is the first quantitative argument the project has had against the Philippine candidate and in favour of the Tambora-latitude belt.

**Why it is not yet a finding.** (a) One calibration point. The emulator's seasonal factor (Greenland share about twice as large for a January eruption as for a July one) has not been checked against any other eruption. The single-core pairs for Krakatau (August 1883, 6°S) point both ways: NEEM/WDC06A says Krakatau put relatively more on Greenland than Tambora did, NGRIP/DSS and the Gao 2007 means say about the same (data/bipolar_lag_1809_2026-10-27.csv), and single pairs scatter by ±50%. (b) The 1809 composites carry large uncertainties (±15.2 and ±13.3 kg/km²). (c) Injection height and QBO phase, which the emulator averages over, change the split. (d) The April proxy is crude; if the emulator's true April value is nearer its July value the band shifts about 5° south, if nearer January about 5° north. The test that settles (a) is cheap: the eVolv2k supplement (Toohey & Sigl 2017, ESSD 9:809, Tables S2/S4) lists composite Greenland and Antarctic fluxes for every event, and four eruptions of known latitude and month bracket our case: Huaynaputina (Feb 1600, 16.6°S), Parker (Dec 1640, 6.1°N), Cosigüina (Jan 1835, 13°N) and Krakatau (Aug 1883, 6.1°S) [dates and latitudes from Toohey & Sigl 2017 Table 1, text]. If the calibrated emulator reproduces their ratio-of-ratios within a factor of 1.5, the 1809 band above stands; if not, it falls. The supplement is a zip Claude's cloud container cannot fetch (U36). A second, independent model is ready to run here: EVA_H (Aubry et al. 2020, JGR 125, e2019JD031303 [memory for the reference]), an eight-box stratospheric aerosol model with latitude, height and season dependence, Python version cloned from GitHub (thomasaubry/EVA_H) on 28 Oct; it needs only `pip install scipy netCDF4`.

### 2.2 Base rate: where a VEI 6 goes unrecorded [calc]

From GVP VOTW 4.6.7 (the eruption list in the pyvolcans wheel): 30 eruptions of VEI 5 or more between 1500 and 1900. Dating evidence: 26 "Historical Observations"; 3 radiocarbon (Billy Mitchell, Bougainville, c. 1580, VEI 6; Sheveluch 1652; Long Island, PNG, c. 1660, VEI 6); 1 dendrochronology (St Helens 1800). Six at VEI 6 or more: Billy Mitchell, Huaynaputina, Long Island, "Unknown Source" 1808, Tambora, Krakatau. Two of the six have no written record at all, and both are Melanesian; the third (ours) is "historical" only through veils seen 15,000 km away. The catalogue is itself biased, since an unrecorded VEI 5 in Melanesia stays unrecorded until someone dates a tephra, and that strengthens the point: between Halmahera and Vanuatu, large eruptions of this period are found by coring, not by reading. Taken with 2.1, the prior moves towards New Britain, Bougainville, the Solomons, Vanuatu and the Banda arc, and away from the Philippines.

Gap noticed on the way: Bougainville appears in data/georoc_scored_2026-10-26.csv only as Bagana (12 rows). Billy Mitchell, Loloru and Takuan are absent, so the glass filter has never been applied to Bougainville's calderas. Billy Mitchell's products are probably too silicic for a 60% SiO2 glass [memory], but the check was never made (option 5).

### 2.3 Corals: the Indo-Pacific felt 1809-1812 at least as hard as Tambora [calc]

PAGES2k v2 (Emile-Geay et al. 2017; pages2kv2.json from the GitHub mirror fzhu2e/cfr-data of the NOAA dataset) has 28 coral records that cover 1806-1816. Anomalies were computed against a 1790-1830 climatology in standard-deviation units (file in the header). Raw proxy sign: higher δ18O or Sr/Ca = cooler and/or saltier (drier).

The Lombok Strait coral (Charles et al. 2003; 8.25°S 115.58°E, which is 13 km from Agung's summit [calc]): December 1808 is +2.5 sd (14th highest of 492 months in 1790-1830), after a normal October and a +1.0 November; January-May 1809 run +0.5 to +1.2; then the July-June years 1809/10 +1.0, 1810/11 +1.2, 1811/12 +1.75, 1812/13 +1.45. Seven of the twelve most extreme months in the whole 209-year record (1782-1990) fall in 1810-1812. The Tambora years are milder at this site (1815/16 +0.7, 1816/17 +1.5).

Elsewhere (July-June yearly anomalies, sd): Fiji, Savusavu Bay (17°S), three records: 1809 +1.0, +0.8, -0.2; 1810 +1.8, +1.5, +0.5; 1811 +0.9, +1.1, +1.95. Abraham Reef, Coral Sea (22°S): 1809 +2.1, 1811 +1.9. New Caledonia, Amédée (22.5°S), Sr/Ca: 1810 +0.6, 1811 +1.1. Galápagos, Urvina Bay: 1810 +1.65, 1811 +2.3. Malindi, Kenya (3°S): 1810 +1.7, 1811 +1.2. Palau (7°N): 1808 +0.7, 1811 +1.1. Guam (13.6°N): 1808 +1.45, 1809 +0.8. Rarotonga (21°S), Sr/Ca 1810-12: -0.5 to -0.8 (warmer). Houtman Abrolhos (28°S): nothing. Caribbean and Red Sea: mixed, no pattern.

Reading (inference, not a finding): a cool and dry excursion over the western Pacific and Indian Ocean tropics in 1809-1812, strongest in the southern tropics and at Lombok, weak in the north (Palau, Guam). It is the natural-archive twin of the documentary Java drought of 1809 and the Guangdong drought, and it says the eruption's tropical-ocean footprint was at least as large as Tambora's. Caveats: coral chronologies can slip by a year; δ18O mixes temperature and rainfall; ENSO overlaps (the Galápagos record looks La Niña-like in 1810-11). The Lombok December 1808 spike sits one month after our inferred eruption date; a local cause (ash or dimming from a volcano 13 km away) is possible but [speculation]; the excursion peaks in 1811-12, which is a climate signal, not a local one.

### 2.4 A court chronicle nobody has read for this: the Đại Nam thực lục [text; page images checked]

The Nguyễn court's Veritable Records cover Gia Long 7-9 (1808-10) day by day, with omens (sun and moon, "red vapour", earthquakes), droughts, famine relief and rice prices for Huế (16.5°N), Gia Định (Saigon, 10.8°N) and Bắc Thành (Hanoi, 21°N). The register (line 1162) listed the Chinese text as a cross-strand lead but found the Wikisource mirror empty. The 2002 Vietnamese translation (Viện Sử học, tập 1, 1079 pp.) is online as an image-only scan (vietsu.org, file Dai-Nam-thuc-luc-T.01-Quoc-su-quan-trieu-Nguyen-2002.pdf on the site's S3 bucket; 44 MB; a copy is now in Claude's cloud container). Page map [page image]: scan 700 = printed p. 697, Gia Long 6 (1807), summer, Quyển XXXII; scan 790 = p. 787, Quyển XL, Gia Long 9 (1810), 6th month (the death of Nguyễn Văn Trương [memory for the year]); so November 1808 to mid-1810 is roughly scans 735-790, about 55 pages, readable at 70 dpi. No OCR engine is installed here; the pages can be read visually. Yield M: a dated sky phenomenon at 11-21°N would bound the veil's spread; silence is a weak negative, since the chronicle records omens selectively.

### 2.5 Ready-to-run model code obtained

EVA_H (see 2.1) is cloned and runnable after two pip installs. It gives monthly stratospheric aerosol optical depth in three latitude bands for a given eruption latitude, height, mass and month, calibrated on 1979-2015 satellite data. Runs for a 1 December 1808 injection at 15°N, 5°N, 5°S, 10°S and 15°S can be compared with (a) the hemispheric deposition split and (b) the arrival dates at Bogotá, Lima and Edo and the European silence.

## 3. Options, numbered for picking

### A. Can start now in Claude's cloud container

1. **Finish the latitude band (2.1).** Run EVA_H for the December 1808 scenarios now; when the eVolv2k supplement (U36) is on the Mac, validate the calibrated emulator with Huaynaputina, Parker, Cosigüina and Krakatau; then publish the band with its uncertainty as a note and CSV. Yield H: it bears directly on Cabalían versus the Tambora belt. About a day.
2. **Read the Đại Nam thực lục** for Gia Long 7 (10th-12th months), 8 and 9 (scans c. 735-790): every sky, earthquake, drought, famine, price and epidemic entry with its date (lunar to Gregorian [calc]). Yield M. A few hours.
3. **Krakatau-1883 spread analogue.** Build the table of first appearance of the 1883 twilights by latitude from the Royal Society report (pp. 263 and 334-337; needs the archive.org PDF, U37) and align it with Bogotá 11 Dec, Lima mid-Dec, Edo 9 Jan, Tottori 5 Feb and the European silence. Krakatau's veil reached the tropical belt in days, 20°N-30°S within about three weeks, and Europe and the northern United States after about three months [memory]. Predictions to test: an eruption date in the last week of November 1808 ± 10 days from the Bogotá date alone; a European twilight window of February-March 1809; and whether a source south of the equator in northern winter fits Lima being as early as Bogotá. Then re-search the downloaded 1809 newspapers (on the Mac) for February-March 1809 twilight language specifically. Yield M-H.
4. **Coral footprint note (2.3).** Read Charles et al. 2003, Linsley et al. 2006 and Bagnato et al. 2005 for their own treatment of 1808-12; add the Vanuatu annual record (Quinn 1996, begins 1807, 300 km from Gaua) and write the footprint up as a side finding with a map. Yield M for the search, H as a side result (M13).
5. **Extend the glass filter** to Bougainville and the Solomons (Billy Mitchell, Loloru, Takuan, Savo, New Georgia) and to Vanuatu's other calderas. Vanuatu (1,264 rows) and the Solomons (420) are already in the GEOROC file; Bougainville's calderas need a GEOROC download on the Mac. Yield M.
6. **A detection-floor table.** For every candidate, the distance to the nearest observer whose written 1808-10 record survives and we have actually read (Batavia, Ambon, Ternate, Banda, Kupang, Manila, Guam, Sydney, Canton, Macau, the LMS and Tongan sources) and the kind of record (daily, monthly, none). Combine it with the latitude band, the glass score and the base rate into one weighted ranking with the weights stated (all [speculation]). It replaces B53's judgement ranking with an auditable one. Yield M.
7. **Pre-register the trace-element discriminators.** From GEOROC (if trace columns are in the downloaded CSVs; otherwise a Mac download), compute which ratios (Ba/La, Nb/Zr, Sr/Y, Th/Nb, La/Yb) separate Dakataua, Gaua, the Banda arc, Halmahera, northern Sulawesi and Cabalían, so that the day someone measures the ice glass there is a lookup table. Yield M now, H later; publishable as a short methods note.
8. **PANGAEA sweep for archives that already exist.** Search PANGAEA metadata (reachable from here) for lake, marine and coral cores within 300 km of each top candidate with sub-decadal resolution through 1800-1820 (Banda Sea, Bismarck Sea, Halmahera, Vanuatu lakes). A core that already exists is cheaper than a new one. Yield M-H.

### B. Needs William's hands first

9. **BL Add MS 12350, Bugis diary, 1808 to 9 July 1809** (also July-August 1812), apparently a copy of the diary of the king of Bone, Aḥmad aṣ-Ṣāliḥ, cross-referenced to Add MS 12354-12357, captured from the palace of Bone in 1814 [text, BL catalogue]. The only indigenous day-by-day record from Sulawesi for the window; Bone is 700 km from the Banda arc, 1,000 km from northern Sulawesi and Halmahera, 2,000 km from New Britain. Bugis court diaries record eclipses, earthquakes, strange skies, epidemics and prices [memory]. Needs Safari for the viewer (if digitised; the catalogue text read here did not say) and a reader of Bugis script; contacting anyone is William's decision. U34. Yield H if anything, L-M if nothing.
10. **FamilySearch "Philippines, Eastern Visayas, Church Records, 1716-2014" (collection 5000329)**: browse the images by parish for Cabalían (now San Juan), Sogod, Liloan, Hinunangan and Maasin, 1808-10, looking for burial spikes and marginal notes. Free account plus Safari. The cheapest test of U84, even if 2.1 lowers Cabalían's odds. U35. Yield H for that question.
11. **Two Mac downloads that unlock options 1 and 3:** the eVolv2k supplement zip (U36) and the Krakatoa report PDF (U37).
12. **Thai dynastic chronicle** (Thiphakorawong), First Reign (1935 Thai edition, PDF on Wikimedia Commons, Safari; Flood's English translation, library) and the Second Reign from September 1809: omens listed before Rama I's death on 7 Sep 1809 and the Burmese attack on Phuket in late 1809 [memory for the dates]. U38, U65. Yield L-M.
13. **TNA HCA 32 prize papers**: ships from Batavia, Banda, Manila and Île de France taken by British cruisers in 1809-10. Daendels sent only six letters home in 1809 and the Dutch letters we read are thin because the mail was intercepted; intercepted mail sits in HCA 30 and HCA 32 (the Prize Papers portal's 1808-10 material is not yet online). Search Discovery by year and ship, then paid copying. U85. Yield M, on the [speculation] that the missing 1809 Batavia and Banda letters are there.
14. **Zerefos painting-based aerosol optical depth for 1809 and 1810** (red/green ratios 1.137 and 1.021, AOD 0.30 and 0.22, from a 2022 conference slide deck [text]; the 2014 ACP paper's Table D1 is blank for 1808-10). Held by the researcher; U98. Yield L.
15. **Prince of Wales Island Gazette 1808-10** (Penang, 5°N): BL microfilm; the NLS holds manuscript copies of three 1809 issues (register lines 221, 618). U66. Yield L.
16. **Sydney Gazette via Trove** (key pending): shipping columns for vessels through St George's Channel and Dampier Strait in 1809-10, and the word "pumice". Yield M: a pumice raft is the one clue a New Britain source should have left.

### C. Reframings

17. **Treat it as a sampling problem, not a reading problem.** Sixty-odd negative sources say the eruption was not seen by anyone who wrote. The remaining effort should go to deposits: ice-glass trace elements, existing cores (option 8), the H15 and Talos Dome ash. A one-page "evidence that would settle it" table, with owner, cost and lead time, is a better basis for William's decisions on contacting researchers than another newspaper run.
18. **Two problems, not one.** Separate "which volcano" from "what did the eruption do". The second is answerable now (corals, Java rice, the Guangdong drought, EIC temperatures, Edo's skies, Bogotá) and is the material of a paper whatever happens to the first.
19. **Invert the ENSO disagreement (B58).** Tree rings say La Niña 1808-10, corals say El Niño-like from December 1808 to May 1809. The Lombok December 1808 spike shows how volcanic cooling at a western-Pacific coral site mimics El Niño in δ18O. A short note arguing that the coral classifier is contaminated by the eruption would resolve a published disagreement [speculation until tested against the Galápagos and Palau records].
20. **Hemisphere from the veil's own timing** rather than from the ice (option 3): the veil reached Bogotá (4.6°N) and Lima (12°S) within days of each other, Edo (36°N) a month later, and Europe never, in the literature reviewed. With the Krakatau table this becomes a formal test of the source hemisphere.

### D. Needs other people, a field season or a laboratory (William's decisions)

21. Ice-glass trace elements (U90-92: Hutchison, Plunkett, McConnell): unchanged as the top physical test.
22. A Lake Dakataua core, and Machida 1996 for the Dakataua tephra chemistry (U47).
23. Gaua: date the youngest caldera-rim tephra; Lake Letas sediments (no published core known [memory]).
24. Cabalían parish records on site (U84), if option 10 finds no digitised books.
25. The H15 and Talos Dome ash (NIPR; Italian PNRA): the only tephra from the 1809 layer that is not Greenlandic or South Polar, and the H15 "ash-like material" has never been analysed.

## 4. Side problems and mysteries our research can illuminate, even if the volcano stays hidden

- **M1. The Kii tsunami of 4 December 1808 (Tsuji 2025).** Our date inference puts the eruption within days of it. A volcanic wave of 2-3 m at Kii from any candidate 4,000 km or more away is physically implausible (Krakatau's 1883 wave was decimetres at trans-Pacific tide gauges [memory]), and our Pacific negatives (no wave at Sydney, Hawaiʻi, Tonga or Lima) support Tsuji's reading of a local "tsunami earthquake". We can say so.
- **M2. The 1809 Java food crisis.** Dutch historiography blames Daendels's corvée and the Great Post Road. The decree of 14 July 1809, the 5 October 1809 "unusual drought" order and now the Lombok coral show a climatic component. A note for colonial Java history.
- **M3. The 1809 Guangdong-Guangxi famine: pirate blockade or drought?** REACHES shows drought at 26 sites in 1809, the most in 1796-1819; the corals and Java add a regional drought. Zheng Yi Sao's fleet was not the only cause.
- **M4. Why did Europe not notice?** A 19 Tg S eruption in northern winter left no red skies in the literature we reviewed and only weak instrumental signals (Milan and Prague diurnal range: negative, low power). Option 3 can say whether the veil's geometry explains the silence, or whether February-March 1809 simply was never searched for twilight language.
- **M5. The ice-core "1809" horizon.** Many cores date the layer 1809.0 or 1809/10. With a November-December 1808 eruption, polar deposition begins in mid-1809 (WDC06A 1809.4, NEEM 1809.7). A one-paragraph note would help every core that uses the layer as a tie point.
- **M6. An unknown Antarctic eruption c. 1810.** Talos Dome's 1809 excess (ratio 1.05-1.11 against 0.48 elsewhere) and the Siple Dome trachyte point to a Victoria Land eruption (Mt Melbourne, the Pleiades or Rittmann) that no catalogue lists. Our sulfate map is the evidence.
- **M7. A second northern eruption in 1808-09** (the Yukon dacitic tephra): Aleutian or Kamchatkan. Our North Pacific window searches (Golovnin, the Russian-American Company, HBC) are a ready-made documentary screen for it.
- **M8. Edo's red skies of January-February 1809** have a cultural history in Japan (diaries, perhaps verse) that never links them to a volcano (B43). Our result gives them a cause.
- **M9. Caldas and the Semanario.** The Bogotá veil of December 1808 is the earliest instrumental-era description of a stratospheric veil in the Americas: history of science in New Granada.
- **M10. Paleo-ENSO method.** Volcanic cooling can be misclassified as El Niño by western-Pacific coral δ18O (option 19).
- **M11. How large eruptions escape the record.** The GVP base rate (2.2) and our sixty negatives quantify a "documentary detection floor" for 1800-1810 by region, relevant to hazard statistics and to the completeness of eruption catalogues.
- **M12. The 1809 mail gap between Batavia and The Hague** (option 13) is a Napoleonic-era communications story that the prize papers could fill.
- **M13. Lombok 1810-1812**: the strongest cool/dry excursion in a 209-year coral record, stronger than Tambora's (2.3). If it survives a chronology check, it changes the account of what the 1809 eruption did to the Australian-Indonesian monsoon, and bears on Timmreck 2021's puzzle of a "weak" 1809 climate response: the response may have been hydrological rather than thermal.

## 5. Recommendation (a suggestion)

In order: **1** (with the two downloads in **11**), **10**, **2**, **8**, **4**. Option 1 is the only item that can change the ranking of the top three candidates from the desk; option 10 is the cheapest direct test of a candidate; option 2 is an untouched primary source that can be read today; options 8 and 4 turn existing archives into evidence.

## 6. Housekeeping done in this thread

Added to unavailable_sources.md: U34 (Bugis diary), U35 (FamilySearch Eastern Visayas), U36 (eVolv2k supplement), U37 (Krakatoa report pages), U38 (Thai chronicle 1935 edition), U39 (Đại Nam thực lục scan, for the Mac copy), U65 (Flood translation), U66 (Prince of Wales Island Gazette), U85 (HCA 32 prize papers), U98 (Zerefos painting AOD). Section A's block (U1-U39) is now full; the next A number is U120. Register section B62 summarises this note. Scripts and data as in the header. findings.csv not changed (observations only, as for B53).
