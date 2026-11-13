---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: candidates
date: 2026-10-28
---

# Existing sediment, coral and speleothem archives within 300 km of the candidate volcanoes (option 8 of B62)

28 October 2026. Register entry B69. Companion file: `data/existing_cores_near_candidates_2026-10-28.csv` (58 rows, same columns as the tables below). Verification labels as in the register: [text] = catalogue metadata, abstract or open data file read as text; [calc] = Claude's calculation; [inference] = Claude's reading between the lines; "not captured" = the field exists in the source but was not fetched. Yield ratings and everything under "Suggestions" are Claude's suggestions.

## 1. Question and method

Option 8 of `creative_next_steps_2026-10-28.md` asked: search PANGAEA metadata for lake, marine and coral cores within 300 km of each top candidate with sub-decadal resolution through 1800-1820, check the other catalogues reachable from Claude's cloud container, and report which cores already have 1809-era tephra or geochemistry measured.

Candidate summit coordinates (GVP, as in `candidate_priority_list_2026-10-26.md`): Dakataua 5.056°S 150.108°E; Gaua 14.27°S 167.5°E; Cabalían 10.287°N 125.221°E; Agung 8.343°S 115.508°E; Todoko-Ranu 1.25°N 127.47°E and Dukono 1.693°N 127.894°E; Teon 6.92°S 129.125°E and Nila 6.738°S 129.5°E; Mahawu/Lokon 1.36°N 124.8°E. Each was searched in a box of ±2.7° latitude (300 km) and a slightly wider longitude band; distances in the tables are great-circle distances from the nearest candidate in the group [calc]. Archives just outside 300 km that matter for context are kept and flagged.

Catalogue routes that worked from Claude's cloud container [text]: (a) the PANGAEA holdings through the DataONE Solr index (bounding-box fields plus title terms core, coral, lake, tephra, ash), with PANGAEA landing pages for details; (b) the DataCite API for PANGAEA DOIs by core name and for NOAA World Data Service for Paleoclimatology DOIs (prefix 10.25921) by place name; (c) the NOAA paleo search API by bounding box and study id, and the NOAA data files themselves. Routes that failed: PANGAEA's own search (script shell, search endpoints disallowed to robots), B2FIND (robots), Neotoma (location filter ignored in WKT form, server error in GeoJSON form), OpenAlex (client error), IMLGS, the US Index to Marine and Lacustrine Geological Samples (every API and map-service address returned 404 or a client error), EarthChem/MGDS (navigation and bathymetry only in these boxes). PAGES2k corals were already covered in B62 sec. 2.3 and the coral footprint note. The sweep therefore covers what PANGAEA, NOAA and DataCite index; cores held only in US repositories (Lamont Vema and Conrad cruises, Scripps Monsoon and Lusiad cruises other than the one PANGAEA lists) are not covered until IMLGS is queried on the Mac (U132).

## 2. Headline results

- **No archive within 300 km of any candidate has a published tephra layer dated to c. 1809, and none of the catalogued marine cores has an age model for the last few centuries.** Where marine cores exist, PANGAEA holds only physical-property (MSCL) and colour scans or long-period proxy records.
- **Halmahera is the one place where existing cores could plausibly resolve 1809.** Kau Bay, 45-135 km from Todoko-Ranu and Dukono, holds the dated 4.25-m core BJ8-03-102GGC (377 m water depth; -1550 to 1950 CE; about 8 yr/cm in the upper part but sampled only every 8 cm, roughly 60 yr), the 19.6-m IMAGES core MD98-2180 (415 m; MSCL and colour only) and twelve Snellius-II piston cores of 1985 (not laminated, no tephra described, storage not stated). MD98-2179 (18.97 m) lies 41 km from Dukono on the Pacific side.
- **Agung has the richest set of dated, sub-decadal archives:** three East Java crater lakes 237-244 km west (Lading: Ca/Ti every 1.6-1.9 yr across 1800-1820; Logung: magnetic susceptibility yearly, geochemistry every 5-8 yr; Ranu Lamongan: sub-annually laminated), the Lombok Strait coral 10 km away (monthly from 1782, already analysed in B62) and the Kangean teak chronology (1760-2000, 165 km). The lake chronologies are 14C and U/Th with about ±30 yr at 1810; no tephra marker is mentioned in the open files, and the Rodysill et al. 2013 abstract itself invokes "large volcanic eruptions that occurred in 1809, 1815 and 1835 CE" as a cause of the drought it dates to 1790 ± 20 with a peak c. 1810 ± 30 [text].
- **Gaua:** no lake core exists for Lake Letas (19 km², 119 m deep; only a 1995 ORSTOM bathymetry) and none for any Banks Islands lake. The nearest cores are ODP Leg 134 Sites 832 and 833 in the North Aoba Basin (59 and 79 km; 1990; top-core resolution unknown). The Espiritu Santo coral (annual δ18O from 1806; 97 km on NOAA's rounded coordinates, consistent with the 98 km in U124) and the Taurius Cave stalagmite (3-month resolution, 1557-2003; 150 km) are the only dated archives spanning 1809; both were read (sec. 5).
- **Dakataua:** nothing closer than 230 km. MD97-2136 and MD97-2137 (Bismarck Sea, 18 and 28 m long, MSCL only) and GeoB17434-3 (Solomon Sea, 4208 m) are undated; the New Ireland Basin cores have Late Quaternary ash beds only (Horz 2004); the Kavieng and Rabaul corals begin in 1823 and 1867. No Lake Dakataua core exists. IODP Sites U1486/U1487 (Manus Basin, 660 km) accumulate c. 3.5 cm/kyr and cannot resolve a year.
- **Cabalían:** only the SO228 gravity and multicores off eastern Mindanao (294-307 km; 210Pb-dated tops, one 18-kyr record) and corals from 1859. One new lead: an approximately 800-year sediment core from a reef hole near Bohol with benthic-foraminifera δ18O and XRF (Monica 2025 dissertation, c. 127 km; the PDF is bot-blocked from Claude's cloud container, U130).
- **Southern Banda:** nothing within 200 km of Teon, Nila or Serua. The Timor Sea (SO185, MD98-2171/2172, LSDA-152P) and northern Banda Sea (MD01-2380, MD98-2173/2174) cores at 205-288 km are long-period records with no late-Holocene age control published. The Snellius-II Banda Sea cores of 1984-85 are described in the Situmorang 1992 thesis (U131).
- **North Sulawesi:** only the Bunaken coral (1860-1990); no sediment core in any catalogue.

## 3. Catalogue routes tried

| Catalogue | Route | Result |
|---|---|---|
| PANGAEA | DataONE Solr index of urn:node:PANGAEA, bounding box + title term | works; 7 boxes swept; landing pages for details [text] |
| PANGAEA | own search, Elasticsearch endpoint, advanced search | script shell; robots-disallowed |
| DataCite | api.datacite.org, client pangaea.repository, titles.title by core name | works (GeoB17434-3, 17402, 17409 found) |
| NOAA WDS Paleoclimatology | DataCite prefix 10.25921 by place name; NOAA paleo search API by bounding box (headersOnly, skip) and NOAAStudyId; pub/data/paleo files | works; corals, lakes, speleothem, tree rings found; files read [text] |
| B2FIND (EUDAT) | search page | robots-disallowed |
| Neotoma | api.neotomadb.org sites with loc= WKT / GeoJSON | WKT filter ignored (global list); GeoJSON server error |
| IMLGS (NCEI/NGDC geosamples) | geosamples-api (samples, repositories, api-docs), ArcGIS Sample_Index service, product page | 404 / client error on every address; needs Safari (U132) |
| EarthChem / IEDA / MGDS | DataONE nodes IEDA_MGDL, MGDS search | no sediment cores in the boxes (bathymetry, dredge geochemistry only) |
| ODP/IODP | PANGAEA ODP mirror; iodp.tamu.edu site summaries | Leg 134 Sites 832/833, Leg 193 (hydrothermal), Exp. 363 U1486/U1487 read |
| OpenAlex | works?search= | client error |
| Literature | web search; VLIZ, Cambridge, Copernicus, core.ac.uk, aquila.usm.edu, Utrecht repository | Snellius-II Kau Bay report read in full; SO228 cruise report first 80k characters; theses blocked (U130, U131) |

## 4. Archives by candidate

Columns: position (decimal degrees; coordinate quality in brackets), water depth or elevation, distance to the nearest candidate of the group [calc], cruise or collection, length, resolution and age control, whether 1800-1820 is covered by a dated record, whether a tephra of c. 1809 has been measured, whether any geochemistry spanning 1800-1820 exists, data location, access route, verification.

#### Dakataua/Makalia (New Britain)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MD97-2136 | marine Calypso piston core, Bismarck Sea | -4.697, 148.045 (exact) | not given | 232 (Dakataua) | MD106 IMAGES III, 1997 | 18.15 m | MSCL and colour scans only; no age model found | unknown | none reported | no | PANGAEA.124278 (physical properties); colour reflectance | IMAGES core; repository not verified (MNHN Paris curates 980 MD cores) | text (PANGAEA metadata) |
| MD97-2137 | marine Calypso piston core, Bismarck Sea | -2.989, 149.585 (exact) | not given | 237 (Dakataua) | MD106 IMAGES III, 1997 | 28.48 m | MSCL (4243 points) and colour only; no age model found | unknown | none reported | no | PANGAEA.124279 | IMAGES core; repository not verified | text (PANGAEA metadata) |
| GeoB17434-3 | gravity core, Solomon Sea | -6.5953, 148.2712 (exact) | 4208 m (CTD at station) | 266 (Dakataua) | RV Sonne SO228 EISPAC, 2013 | not captured | no published data found | unknown | none reported | no | PANGAEA.818962 (documentation) | MARUM Bremen core repository [inference] | text (DataCite, cruise report) |
| GIK16998-1 (and -2) | sediment core, New Ireland Basin W of New Ireland | -3.69166, 151.74432 (exact) | not captured | 236 (Dakataua) | RV Sonne SO94, 1994 | not captured | age model, bulk sedimentology, magnetic susceptibility in PANGAEA; Late Quaternary | unknown (coarse) | ash beds Late Quaternary (Horz 2004); nothing dated to 1809 | no | PANGAEA (Horz et al. 2013 series) | GEOMAR/Kiel [inference] | text (PANGAEA metadata) |
| New Ireland Basin set GIK16986-16994 (1994), GIK17674-17684 (1998) | box and gravity cores | -3.3, 152.5 (centroid approx) | 1000-2500 m (not captured per core) | 329 (Dakataua) | SO94 1994, SO133 1998 | various | tephra occurrence tables and glass chemistry (Horz et al. 2004 JVGR 132:73); ages Late Quaternary | unknown | Late Quaternary ash beds, glass major elements published; none historical | no | PANGAEA.824489 and children | GEOMAR/Kiel [inference] | text (PANGAEA metadata; glass rows read 26 Oct, B50) |
| Kavieng coral core NEP | Porites coral core | -2.5, 150.5 (rounded (NOAA)) | reef | 288 (Dakataua) | collected Apr 1997 | 2.1 m | monthly Sr/Ca, Ba/Ca | no (1823-1997) | n/a | no (starts 1823) | NOAA study 8604, alibert2008_noaa.txt | data open | text (NOAA metadata) |
| Rabaul coral core 95 | Porites coral core | -4.18, 151.98 (exact (4°11.49′S 151°58.63′E)) | reef | 229 (Dakataua) | c. 1995 | 2 m | monthly d18O, Sr/Ca | no (1867-1997) | n/a | no (starts 1867) | NOAA study 6116, quinn2006_noaa.txt | data open | text (NOAA metadata) |
| Lake Dakataua (caldera lake) | NO CORE FOUND | -5.06, 150.1 (lake approx) | - | 1 (Dakataua) | - | - | - | - | - | - | searched PANGAEA (DataONE), NOAA, DataCite, web; Neotoma route failed | a new core remains the test proposed in B53 | text (absence) |
| IODP 363 Sites U1486/U1487 (Manus Basin) | drill cores, OUTSIDE 300 km | -2.3333, 144.8195 (exact (U1487)) | 874 m (U1487) | 660 (Dakataua) | IODP Exp. 363, 2016 | 144 m (U1487) | Pleistocene average c. 3.5 cm/kyr; rare ash in upper 21 m | no usable resolution (1 cm = c. 30 yr) | tephra layers common but undated at top | no | IODP Proceedings 363 ch. 107-108 | IODP Kochi/College Station repository c. 690 km from Dakataua | text (site summary) |
| SO228 GeoB17426/17427 (N of New Ireland) | gravity cores + MUC, OUTSIDE 300 km | -2.1867, 150.8617 (CTD position of 17426) | 1350 m / c. 950 m | 330 (Dakataua) | SO228, 2013 | not captured | no published data found | unknown | none reported | no | cruise report (MARUM Berichte 295) | MARUM [inference] c. 330 km | text (cruise report) |
| SO228 GeoB17435/17436 (Huon Gulf) | gravity cores + MUC, OUTSIDE 300 km | -7.89, 148.2017 (CTD position of 17436) | 845 m (17436); 1000 m (17435, up to 70 m undisturbed sediment) | 379 (Dakataua) | SO228, 2013 | not captured | no published data found | unknown | none reported | no | cruise report (MARUM Berichte 295) | MARUM [inference] c. 380 km | text (cruise report) |
| SO228 GeoB17432 (S of Long Island) | gravity core + MUC, OUTSIDE 300 km | -5.345, 146.2 (CTD position) | 1388 m | 434 (Dakataua) | SO228, 2013 | not captured | no published data found | unknown | none reported | no | cruise report | MARUM [inference] c. 430 km; Long Island is itself ruled out (B53) | text (cruise report) |

#### Gaua (Banks Is., Vanuatu)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ODP Site 134-832 (Holes A, B) | drill holes, North Aoba Basin | -14.796, 167.573 (exact) | not retrieved | 59 (Gaua) | ODP Leg 134, Nov 1990 | deep penetration (not retrieved) | VCDs, MSCL, P-wave in PANGAEA; top-core resolution unknown | unknown | ash layers in VCDs (Pleistocene); nothing dated to 1809 | no | PANGAEA ODP mirror | IODP sample request (Pacific legs: Kochi Core Center) [inference] | text (PANGAEA metadata) |
| ODP Site 134-833 (Holes A, B) | drill holes, North Aoba Basin | -14.876, 167.88 (exact) | not retrieved | 79 (Gaua) | ODP Leg 134, Dec 1990 | not retrieved | as 832 | unknown | as 832 | no | PANGAEA ODP mirror | as 832 | text (PANGAEA metadata) |
| Espiritu Santo coral core 001 (Platygyra lamellina) | coral core | -15.0, 167.0 (rounded to 1° (NOAA)) | reef | 97 (Gaua) | c. 1980 (Quinn 1993) | not given | annual d18O, d13C (2- and 4-sample means) | YES 1806-1979 | n/a | yes: annual d18O/d13C from 1806 | NOAA study 1839, quinn1996_noaa.txt | data open and read (this note, sec. 5) U124/U68 hold the papers | text + calc |
| Taurius Cave stalagmite | speleothem | -15.5333, 167.0167 (exact) | 230 m elev. | 150 (Gaua) | Partin et al. 2013 Geology 41 | 250 mm to 1800 CE | c. 3 months/sample; 31 U/Th dates; 2-sigma age error c. 3 yr at 1800 | YES 1557-2003 | n/a | yes: d18O, d13C | NOAA study 14988, taurius2013.txt | data open and read (sec. 5) | text + calc |
| Malo Channel coral | Porites coral core | -15.7, 167.2 (NOAA) | reef | 162 (Gaua) | Kilbourne 2004 | - | monthly d18O, Sr/Ca | no (1928-1992) | n/a | no | NOAA study 1925 | data open | text |
| Sabine Bank coral | coral core | -15.9, 166.0 (approx) | reef | 242 (Gaua) | Gorman et al. 2012 | - | monthly/seasonal d18O | no (1842-2007) | n/a | no | NOAA DOI 10.25921/c417-zb83 | data open | text (title only) |
| Vanuatu modern and fossil coral Sr/Ca | coral | - | reef | - | - | - | monthly | no (1049-1152 and 1894-2006) | n/a | no | NOAA DOI 10.25921/dx12-km22 | data open | text (title only) |
| Lake Letas (crater lake around Mt Gharat) | NO CORE FOUND | -14.283, 167.533 (lake) | 418 m elev.; 119 m max depth; 19 km2 | 4 (Gaua) | - | - | - | - | - | - | bathymetry only: Laurent et al. 1995 (ORSTOM); Ramsar 2023 | a new core would be the test (B53) | text (Wikipedia; absence in PANGAEA/NOAA/web) |

#### Cabalian (S Leyte)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GeoB17402-2 | gravity core, off E Mindanao | 8.00117, 126.57567 (exact) | 555 m | 294 (Cabalian) | SO228, May 2013 | not captured | 18 kyr foraminiferal isotope record (Shao et al. 2021 Clim. Past 17:1507); resolution not stated | probably (record reaches 0 BP) but coarse | none reported | isotopes only, coarse | NOAA study 33094 shao2021.txt; PANGAEA.818932 | data open; core MARUM [inference] | text |
| GeoB17402-1 (multicorer) | short core | 7.99966, 126.57483 (exact) | c. 555 m | 295 (Cabalian) | SO228, 2013 | short | 210Pb/137Cs, organic geochemistry (2017) | last c. 100-150 yr only | none reported | no | PANGAEA.877436 | data open | text |
| GeoB17409-1 | short core | 7.85833, 126.55467 (exact) | not captured | 307 (Cabalian) | SO228, 2013 | short | 210Pb/137Cs; natural and anthropogenic U isotopes (2021) | last c. 100-150 yr only | none reported | no | PANGAEA.877437, 932255 | data open | text |
| GeoB17405-3, 17408-1, 17411-1 | gravity cores, off E Mindanao | 7.9, 126.63 (centroid) | not captured | 307 (Cabalian) | SO228, 2013 | not captured | documentation only | unknown | none reported | no | PANGAEA documentation | MARUM [inference] | text |
| Reef-hole sediment core near Bohol (Monica 2025 dissertation, ch. 3) | reef-hole core | 9.85, 124.15 (island centroid approx (site unread)) | not read | 127 (Cabalian) | USM dissertation Dec 2025 (Wallace lab) | not read | c. 800-yr record; benthic foraminifera d18O, XRF; resolution not read | probably (800 yr to present) | not read | XRF and d18O exist | aquila.usm.edu/dissertations/2414 (PDF article=3579) | PDF blocked from container: U130 (Safari) only sub-centennial archive found within 150 km of Cabalian | abstract only |
| Western Bohol Sea deep-sea core (Buen, Siringan, Lloren, EGU2020-13383) | marine core | 8.9, 123.8 (approx (position not given)) | not given | 219 (Cabalian) | UP Marine Science Institute, c. 2019 | not given | LGM to present on five 14C dates; low resolution | probably, coarse | not mentioned | XRF elements, coarse | EGU2020-13383 abstract | unpublished; held by UP-MSI: U142 | abstract only |
| Olango (Cebu) coral Olango_XXV | Porites lobata coral | 10.217, 124.01 (exact) | reef | 133 (Cabalian) | Pfeiffer et al. | - | monthly d18O | no (1859-1980) | n/a | no | PANGAEA | data open | text |

#### Agung (Bali)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lake Lading | crater-lake sediment cores | -8.0088, 113.3125 (exact) | elev. not retrieved | 244 (Agung) | Brown Univ. (Russell lab), 2000s | not retrieved | Ca/Ti 1.6-1.9 yr/sample through 1800-1820 [calc from file]; dDwax c. 8.5 yr (Konecky 2013); grain size/flood index (Rodysill 2019); 14C + U/Th, age error ±30 yr at 1810 | YES (c. 800-2009 CE) | none reported in NOAA metadata (papers unread: U133) | yes: Ca/Ti, Mg/Ca etc. 1.6-1.9 yr; Ca/Ti high (drought) c. 1804-1825 | NOAA studies 33192, 33193, 14129, 32133; lading2013ca-ti.txt | data open; core material Brown Univ. [inference]: U139 Rodysill 2013 abstract names eruptions of 1809, 1815, 1835 as a cause of the drought | text + calc |
| Lake Logung | crater-lake sediment core | -8.0418, 113.3075 (exact) | 215 m elev.; 7 m water depth | 244 (Agung) | Brown Univ., c. 2009 | not stated | magnetic susceptibility c. 1 sample/yr (43 samples 1800-1820); TOC/TN/isotopes/opal every 5-8 yr (2-3 samples 1800-1820) [calc from file] | YES (614-2009 CE) | not mentioned in file | yes: MS yearly; TOC, TIC, C/N, d13C, d15N, BSi 5-8 yr | NOAA study 13177, logung2012.txt | data open; core Brown Univ. [inference]: U139 | text + calc |
| Ranu Lamongan | crater-lake sediment core, sub-annually laminated | -7.9833, 113.3833 (exact) | 240 m elev. | 237 (Agung) | collected 1998 (Crausbay 2006) | 9.82 m | laminated (c. 1 cm dry-season, 1-10 cm wet-season); drought index mol% MgCO3 by depth; NOAA file has no calibrated age column | YES (1145-1950 CE per NOAA) | not mentioned in file | yes: carbonate mineralogy | NOAA study 22409, lamongan2006di.txt | data open; age model in paper (U135); core Brown Univ. [inference]: U139 | text |
| Lombok Strait coral (Padang Bai) | Porites coral core | -8.25, 115.5 (NOAA) | reef | 10 (Agung) | collected 1990 (Charles 2003) | - | monthly d18O | YES 1782-1990 | n/a | yes: monthly d18O (read in B62: Dec 1808 +2.5 sd; 1810-12 extreme) | NOAA study 1903, charles2003-lom_noaa.txt | data open, already analysed | text |
| Kangean (Sepanjang) teak INDO008 | tree-ring widths, Tectona grandis | -6.8667, 115.3833 (exact) | 120 m elev. | 165 (Agung) | D'Arrigo, Krusic, Palmer | - | annual ring width | YES 1760-2000 | n/a | ring width only | NOAA study 12631, indo008.rwl | data open | text |
| Nusa Penida coral (Murty et al. 2018) | coral core | -8.73, 115.55 (approx) | reef | 43 (Agung) | - | - | monthly Sr/Ca | no (193 yr from 1824) | n/a | no | NOAA (not retrieved) | data open | text (earlier sweep) |
| Gili Selang coral | coral core | -8.4, 115.7 (approx) | reef | 22 (Agung) | - | - | monthly | no (c. 110 yr) | n/a | no | NOAA (not retrieved) | data open | text (earlier sweep) |
| GIK18534-3 | sediment core, Bali/Flores Sea | -7.51065, 116.26273 (exact) | not captured | 124 (Agung) | Aug 2011 | not captured | documentation only | unknown | none reported | no | PANGAEA documentation | GEOMAR/Kiel [inference] | text |
| MD98-2158 | Calypso piston core, Bali/Flores Sea | -7.49, 116.27 (exact) | not given | 127 (Agung) | IMAGES IV, 1998 | not captured | physical properties and colour only | unknown | none reported | no | PANGAEA | IMAGES core; repository not verified | text |
| MD98-2157 | Calypso piston core, Indian Ocean S of Bali | -10.56, 114.89 (exact) | not given | 256 (Agung) | IMAGES IV, 1998 | not captured | physical properties and colour only | unknown | none reported | no | PANGAEA | IMAGES core | text |
| MD98-2159 | Calypso piston core, Java Sea | -6.15, 114.83 (exact) | not given | 255 (Agung) | IMAGES IV, 1998 | not captured | physical properties and colour only | unknown | none reported | no | PANGAEA | IMAGES core | text |
| GeoB10053-7 | gravity core, Indian Ocean S of E Java | -8.6765, 112.8725 (exact) | not captured | 292 (Agung) | SO184 PABESIA, Aug 2005 | not captured | 22-kyr multiproxy (Mg/Ca SST, pollen, leaf wax, fire proxies); a 5000-yr multi-proxy dataset exists; resolution not checked | probably, coarse | none reported | yes, coarse | PANGAEA (many datasets) | data open; core MARUM [inference] | text |

#### Halmahera (Todoko-Ranu, Dukono)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MD98-2180 | Calypso piston core, Kau Bay (position and 415 m depth imply inside the bay) [inference] | 0.95, 127.74 (exact) | 415 m | 45 (Todoko-Ranu) | IMAGES IV, 1998 | 19.6 m | MSCL and colour only; no age model found | unknown | none reported | no | PANGAEA.59619, 59023 | IMAGES core; repository not verified: U138 | text (PANGAEA metadata) |
| MD98-2179 | Calypso piston core, off NE Halmahera (Tobelo side) [inference] | 1.45, 128.17 (exact) | 385 m | 41 (Dukono) | IMAGES IV, 1998 | 18.97 m | MSCL and colour only; no age model found | unknown | none reported | no | PANGAEA.59618, 59022 | IMAGES core: U138 | text (PANGAEA metadata) |
| BJ8-03-102GGC | giant gravity core, Kau Bay | 0.5, 127.717 (exact (0°30′N 127°43′E)) | 377 m | 88 (Todoko-Ranu) | RV Baruna Jaya VIII, 2003 (Langton et al. 2008 Geology 36:795) | 4.25 m | sampled every 8 cm = c. 60 yr; upper core c. 8 yr/cm, so 1-cm resampling could give sub-decadal resolution [calc] | YES (-1550 to 1950 CE) | none mentioned in NOAA file | yes, coarse: Mg/Ca SST and d18O of G. ruber at c. 60-yr steps | NOAA langton2008.txt | data open; core material Linsley/LDEO [inference]: U99 | text + calc |
| Snellius-II Kau Bay cores (12 piston, 13 box: stations K3, K4, K8-K11) | piston and box cores, Kau Bay | 0.9, 127.8 (approx (positions not given in report)) | 437 m at K4 | 53 (Todoko-Ranu) | Snellius-II cruise G4, Apr 1985 | K8P1 target 9 m; others not given | not laminated ("varves are remarkably absent"); c. 10 ka at 5-10 m depth; no sedimentation rate stated | probably (surface cores) | none described | pore-water and sulphide chemistry only | van der Linden et al. 1986 progress report (VLIZ 360517.pdf); Barmawidjaja et al. 1989 Radiocarbon 31:948 | storage not stated (Utrecht/NIOZ?) [inference]: U141 | text (report read in full) |
| MD01-2386 | Calypso piston core, W Pacific E of Halmahera | 1.13, 129.793 (exact) | not captured | 220 (Dukono) | MD122 WEPAMA, May 2001 | not captured | 14C ages and physical properties in PANGAEA | unknown | none reported | no | PANGAEA | IMAGES core | text |
| MD10-3340 | piston core, Halmahera Sea | -0.52, 128.72 (exact) | not captured | 241 (Todoko-Ranu) | MD10, 2010 | not captured | 360-kyr record (XRF, ICP-MS, Mg/Ca, benthic isotopes); long-period | coarse | none reported | coarse | PANGAEA.924044 etc. | data open | text |

#### S Banda (Teon, Nila)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MD98-2172 and MD98-2171 | Calypso piston cores, Timor Sea | -8.52, 128.16 (exact) | not given | 207 (Teon) | IMAGES IV, 1998 | not captured | physical properties and colour only | unknown | none reported | no | PANGAEA | IMAGES cores | text |
| GIK18459-3 | gravity core, Timor Sea | -8.49965, 128.16711 (exact) | not captured | 205 (Teon) | SO185 VITAL, Sep 2005 | not captured | documentation only | unknown | none reported | no | PANGAEA | GEOMAR/Kiel [inference] | text |
| GIK18460-3 | gravity core, Timor Sea | -8.78977, 128.64142 (exact) | not captured | 215 (Teon) | SO185, 2005 | not captured | age determinations (Suppl. Table 2) | unknown | none reported | no | PANGAEA | GEOMAR/Kiel [inference] | text |
| GIK18471 (SO18471) | piston core, Timor Sea | -9.36645, 129.98305 (exact) | not captured | 288 (Teon) | SO185, 2005 | not captured | multi-proxy MIS 1-2; Mg/Ca at 5-cm steps; tie points and sedimentation rates published | probably, coarse | none reported | yes, coarse | PANGAEA (several) | data open | text |
| Other SO185 Timor Sea cores GIK18456-3, 18457-3, 18458-5, 18461-1, 18462-3, 18468-3, 18470-2 | gravity cores | -9.2, 129.6 (centroid) | not captured | 259 (Teon) | SO185, 2005 | not captured | documentation only | unknown | none reported | no | PANGAEA | GEOMAR/Kiel [inference] | text |
| MD01-2380 | Calypso piston core, N Banda Sea | -5.7607, 126.904 (exact) | not captured | 277 (Teon) | MD122 WEPAMA, May 2001 | not captured | planktic d18O, d15N, alkenones, opal; long record | probably, coarse | none reported | yes, coarse | PANGAEA | IMAGES core | text |
| MD98-2173 and MD98-2174 | Calypso piston cores, N Banda Sea | -5.77, 126.9 (exact) | not given | 277 (Teon) | IMAGES IV, 1998 | not captured | physical properties and colour only | unknown | none reported | no | PANGAEA | IMAGES cores | text |
| LSDA-152P | piston core, Timor Trough | -8.733, 127.483 (exact) | not captured | 271 (Teon) | Lusiad expedition (Scripps), 1963 | not captured | 14C age determinations | unknown | none reported | no | PANGAEA | Scripps [inference] | text |
| SHI 9016 | piston core east of Timor (Spooner et al. 2015) | - | 1805 m | - | c. 1990 | - | 80-kyr record; resolution not stated | coarse | none mentioned | coarse | ANU thesis / Elsevier 2015 | ANU [inference] | abstract only |
| Snellius-II Banda Sea cores (Situmorang 1992 thesis) | piston and box cores | - | - | - | Snellius-II 1984-85 | - | sedimentology, geotechnics; tephra not mentioned in abstract | unknown | not read | no | Utrecht thesis PDF 9.66 MB | needs Mac download: U131 | abstract only |
| Banda Sea within 150 km of Teon/Nila/Serua | NO CORE FOUND | -6.8, 129.3 (region) | - | 23 (Nila) | - | - | - | - | - | - | PANGAEA (DataONE), NOAA, DataCite: nothing | Snellius-II 1984 Teon charcoal (B52) remains the only on-island sample | text (absence) |

#### N Sulawesi (Mahawu/Lokon)

| Archive | Type | Position | Depth / elev. | km to nearest candidate [calc] | Cruise / year | Length | Resolution and age control | Covers 1800-1820? | Tephra c. 1809? | Geochemistry 1800-1820? | Data | Access route | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bunaken Island coral | Porites coral core | 1.5, 124.83 (NOAA) | 3 m | 16 (Mahawu-Lokon) | collected Aug 1990 (Charles 2003) | 2.65 m | monthly d18O | no (1860-1990) | n/a | no | NOAA study 1903, charles2003-bun_noaa.txt | data open | text |
| Celebes Sea / Molucca Sea / Lake Tondano within 300 km | NO CORE FOUND | 1.36, 124.8 (region) | - | 0 (Mahawu-Lokon) | - | - | - | - | - | - | PANGAEA (DataONE), NOAA, DataCite: nothing | - | text (absence) |

## 5. Which archives already have 1809-era tephra or geochemistry

**Tephra:** none. No core in any box has a tephra layer dated to c. 1809, and the only cores with tephra data at all (New Ireland Basin GIK16986-16994 and GIK17674-17684; Horz et al. 2004) carry Late Quaternary ash beds whose glass was already compared in B50 [text]. ODP 832/833 visual core descriptions list Pleistocene ash. The Kau Bay Snellius-II report of 1986 describes no ash in any core and says the sediments hold no seasonal laminations ("varves are remarkably absent") [text, report read in full].

**Geochemistry spanning 1800-1820 at usable resolution** (all data open at NOAA and already readable from Claude's cloud container):

| Archive | What exists across 1800-1820 | Resolution | Chronology at 1809 |
|---|---|---|---|
| Lake Lading | Ca/Ti, Mg/Ca and other XRF ratios (Rodysill 2013); grain size and flood index (Rodysill 2019); leaf-wax δD (Konecky 2013) | 1.6-1.9 yr per sample [calc]; δD c. 8.5 yr | 14C + U/Th, ±30 yr |
| Lake Logung | magnetic susceptibility; TOC, TIC, C/N, δ13C, δ15N, biogenic silica | MS c. 1 yr (43 samples 1800-1820); geochemistry 5-8 yr (2-3 samples) [calc from file] | file gives years only; method in paper (U136) |
| Ranu Lamongan | carbonate mineralogy drought index on laminated sediment | sub-annual laminations; NOAA file lacks calibrated ages | 14C and U-series in paper (U135) |
| Lombok Strait coral | δ18O | monthly | annual bands (read in B62: Dec 1808 +2.5 sd, 1810-12 extreme) |
| Kangean teak INDO008 | ring widths | annual | ring counting |
| Espiritu Santo coral | δ18O, δ13C | annual | density bands |
| Taurius Cave stalagmite | δ18O, δ13C | c. 3 months | 31 U/Th dates, 2σ c. 3 yr at 1800 |
| Kau Bay BJ8-03-102GGC | Mg/Ca sea-surface temperature, δ18O of *G. ruber* | c. 60 yr (8-cm samples); c. 8 yr/cm available | 14C |
| Western Bohol Sea core; GeoB17402-2; GIK18471; MD01-2380; GeoB10053-7 | XRF or isotope series reaching the present | decadal to centennial | 14C, coarse |

**Readings made this turn (Claude's calculations on the open files; interpretive direction follows the authors):**

- *Espiritu Santo coral (Quinn et al. 1996; quinn1996_noaa.txt).* Annual δ18O (2-sample mean) 1806-1822, in ‰: 1806 -4.91, 1807 -4.79, 1808 -4.73, 1809 -4.92, 1810 -5.04, 1811 -5.22, 1812 -4.91, 1813 -5.03, 1814 -4.86, 1815 -5.02, 1816 -4.70, 1817 -4.91, 1818 -4.79, 1819 -4.84, 1820 -4.42, 1821 -4.47, 1822 -4.84. Whole-record mean -4.98, sd 0.25 (174 years; computed by the fetch tool, window rows checked by hand). Higher δ18O means cooler or more saline water. 1809-1815 lie at or below the mean (slightly warm or wet); the only departures beyond one sd in the window are positive: 1816 (+1.1 sd), 1820 (+2.2 sd) and 1821 (+2.0 sd), after Tambora. 1808 (+0.98 sd) is borderline. So this coral shows no cool excursion in 1809-1811; the first-draft blog rule applies: "we found no 1809 cooling in this record".
- *Taurius Cave stalagmite (Partin et al. 2013; taurius2013.txt).* Seventy-seven samples dated 1800.0-1821.9 CE: mean δ18O -5.86‰, sd 0.25‰ [calc]. The 1801-1814 mean is -6.00‰; the run 1809.2-1810.4 CE (four samples, -6.11 to -6.18‰, mean -6.14‰) is the most negative stretch after 1800-1801; from 1815 the values rise steadily to -5.3 to -5.5‰ by 1820-1821 (1815-1821.9 mean -5.58‰). Partin et al. read lower δ18O as more rainfall under the South Pacific Convergence Zone, so the record shows a wet 1809-10 and a drying trend after 1815 at 15.5°S, with ±3 yr dating. It is one record and a small excursion; it is noted, not weighed.
- *Lake Logung (logung2012.txt).* Between 1800 and 1820 the file holds 43 magnetic-susceptibility samples but only 2-3 geochemical samples (1804.3, 1810.1, 1815.5 CE), so the Logung geochemistry cannot see a single year; the susceptibility series could. Ages in the file differ by up to 8 yr between proxy tables at the same depth [text].

## 6. Suggestions (Claude's; William decides)

1. **Kau Bay is the cheapest existing-core test for the Halmahera candidates.** BJ8-03-102GGC has about 8 yr/cm in its upper part; the 1780-1830 interval is a few centimetres that could be resampled at 1 cm and screened for glass shards and for XRF or sulphur spikes. MD98-2180 (19.6 m) would give the same interval with more material. Both need the holders (U99, U138); the Snellius-II cores (U141) are a third copy of the same basin. A hit would be the first physical 1809 deposit anywhere.
2. **East Java lakes:** a cryptotephra scan of the 1790-1830 interval in the Lading, Logung or Lamongan cores (U139) would find the Tambora 1815 ash, which fell on East Java, as a fixed point, and any 1809 layer would sit a few centimetres below it. The Ca/Ti drought that Rodysill et al. date to c. 1804-1825 could then be tied to the ash positions. Reading Rodysill 2013 and Crausbay 2006 in full (U133, U135) comes first; the authors may already have looked.
3. **Gaua:** no existing archive can date the caldera tephra; Lake Letas remains uncored and the Santo coral and stalagmite show no 1809 cooling. The B53 recommendation (date the youngest caldera tephra, or core Lake Letas) stands.
4. **Dakataua:** the Bismarck Sea IMAGES cores (U140) have no age model and lie 230 km away; a thin 1809 ash in their top metre is possible but unlikely to be found without a dated framework. A Lake Dakataua core remains the test.
5. **Cabalían:** read the Bohol reef-hole chapter (U130) for the core's position, resolution and any XRF spike near 1809 or 1815; it is the only sub-centennial archive within 150 km.
6. **Catalogue gap:** run the IMLGS box queries on the Mac (U132) to see whether Lamont or Scripps hold pre-1990 cores in the Banda and Bismarck Seas; export each box as CSV into data/.
7. **Side result for the climate strand:** the Santo coral and Taurius stalagmite add two tropical South Pacific records with no 1809-11 cooling, consistent with the weak Southern Hemisphere response in B58; worth one line in the coral footprint note when it is next revised.

## 7. Added to unavailable_sources.md this turn

A (Mac or Safari): U130 Monica 2025 dissertation PDF; U131 Situmorang 1992 thesis PDF; U132 IMLGS queries. B (paywalled): U133 Rodysill 2013; U134 Langton 2008; U135 Crausbay 2006; U136 Rodysill 2012; U137 Horz 2004. D (held by researchers or repositories): U99 BJ8-03-102GGC material; U138 MD98-2180/2179; U139 East Java lake cores; U140 MD97-2136/2137; U141 Snellius-II Kau Bay cores; U142 western Bohol Sea core; U143 ODP 832/833 top sections.

## 8. Sources consulted (all read as text unless stated)

- DataONE Solr index: https://cn.dataone.org/cn/v2/query/solr/ (q=southBoundCoord:[S TO N] AND westBoundCoord:[W TO E] AND title:core, fq datasource "urn:node:PANGAEA"); DataCite: https://api.datacite.org/dois (client-id pangaea.repository; prefix 10.25921); NOAA: https://www.ncei.noaa.gov/access/paleo-search/study/search.json (minLat/maxLat/minLon/maxLon, headersOnly, skip, NOAAStudyId, dataTypeId=4 corals).
- PANGAEA landing pages: doi.pangaea.de/10.1594/PANGAEA.59619, 59023, 59618, 59022 (MD98-2180, -2179); 124278, 124279 (MD97-2136, -2137); 818962 (GeoB17434-3); 818932, 877436, 877437, 932255 (GeoB17402, 17409); 824489 (Horz 2013 series); 801457 (ODP 193-1191A).
- NOAA studies and files: 1839 quinn1996_noaa.txt; 14988 taurius2013.txt; 1925; 8604 alibert2008_noaa.txt; 6116 quinn2006_noaa.txt; 1903 charles2003-lom/-bun_noaa.txt; 13177 logung2012.txt; 22409 lamongan2006di.txt; 33192, 33193, 14129, 32133 (Lading); 12631 indo008.rwl; 33094 shao2021.txt; langton2008.txt.
- Van der Linden, Hartosukohardjo, Zachariasse & de Lange 1986, Snellius-II progress report cruise G4 (Kau Bay), https://www.vliz.be/imisdocs/publications/360517.pdf (read in full); Barmawidjaja et al. 1989 Radiocarbon 31:948-956 (abstract); Rodysill et al. 2013 QSR 80:102-111 (abstract via experts.umn.edu); Mohtadi et al. 2013 SO228 cruise report, MARUM Berichte 295, https://core.ac.uk/download/19669116.pdf (first 80,752 characters; station list not included); IODP Exp. 363 Site U1487 summary, https://web.iodp.tamu.edu/scienceops/sitesumm/363/363_ss1487.html; Buen, Siringan & Lloren EGU2020-13383 (abstract); Monica 2025, https://aquila.usm.edu/dissertations/2414 (abstract; PDF blocked); Situmorang 1992, https://dspace.library.uu.nl/handle/1874/238553 (record; PDF failed); Spooner et al. 2015 (openpolar record, abstract); MNHN Oceanic Collection page https://www.mnhn.fr/en/ocean-sediment-and-rock-collection; Wikipedia, Lake Letas; Bani et al. 2021 JVGR 418:107342 (IRD record, no sediment content).
