---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: method
date: 2026-11-02
---

# Free checks T5, T6, T7, T8, T10 from open_tasks.md (2 Nov 2026)

Asked by William (2 Nov 2026, 16:05 UTC): "Please do these free ones T8 T7 T6 T5 T10". Thread "Survey Royal Navy logs 1808-10 at Kew". Verification labels: [catalogue text] read through the fetch tool; [OCR snippet] archive.org full-text search snippets, not page images; [calc] Claude's calculation from data already in data/.

## T5. Kew CO 77: a sequel to the 1807 Canton/Macao meteorological journal? (done)

TNA Discovery, series CO 77, all records dated 1806-1812 (11 hits) and keyword searches "meteorological", "journal", "Canton" [catalogue text]. The only meteorological item is **CO 77/64, "Meteorological Journal: Canton and Macao", 1807**. No 1808, 1809 or 1810 journal is catalogued in CO 77. The general volumes for the window (CO 77/27 Secretary of State 1793-1813; 77/34 Bengal 1809-16; 77/37 1809-16; 77/58 despatches 1795-1810; 77/60 domestic 1810-13) are not itemised, so a later journal could be bound inside one of them unseen. **Result: we found no catalogued sequel.** The 1809 Canton/Macao weather record remains Kerr's journal, BL Add MS 8964 (pacific_china_pass3.md 5.1).

## T6. Deshima day register 1808-09 (done: inventory numbers found, scans exist)

Nationaal Archief 1.04.21 (Nederlandse Factorij Japan), per-item inventory page [catalogue text]. The inventory number left unresolved since 16 Oct (U11) is now known:
- **inv. 221**: dagregister 4 Nov 1807 - 8 Nov 1808, DIGITALIZED
- **inv. 222**: dagregister **9 Nov 1808 - 22 Nov 1809**, DIGITALIZED (the core window, with the Edo red skies from 9 Jan 1809)
- **inv. 223**: dagregister 22 Nov 1809 - 18 Oct 1810, with duplicate, DIGITALIZED
- **inv. 256**: secret dagregister 16 Nov 1807 - 8 Nov 1808, DIGITALIZED
- **inv. 257**: **secret dagregister 11 Nov 1808 - 19 Oct 1809, with enclosures**, DIGITALIZED
Opperhoofd Hendrik Doeff (1804-17). Viewer links follow the pattern nationaalarchief.nl/onderzoeken/archievenoverzicht/1.04.21/invnr/@222/file/NL-HaNA_1.04.21_222_0001. Claude's cloud container cannot reach the EAD XML for the METS identifiers (403), so the download goes through William's Mac: `scripts/fetch_unavailable.py deshima` (inv. 222 and 257) and `deshima-extra` (221, 223), added 2 Nov and copied to the Mac's scripts/ folder (md5 checked). Scans land in archives/Nationaal_Archief/1.04.21_inv222/ etc. Reading needs the Dutch daily weather and sky entries for Dec 1808-Mar 1809. A published Japanese translation also exists (長崎オランダ商館日記 vol. 3, 1991; asian_arabic_round4.md). U11 status changed to "needs Mac download".

## T7. HRNSW vol. 7 p. 104, "We have had very dry weather since you left" (partly done)

archive.org in-item search of historicalrecor03walegoog (HRNSW vol. 7, 1901) [OCR snippet]. The phrase is on page 104, between a document dated "18th February, 1809" (p. 103) and a dispatch dated Sydney, 20 Feb 1809 (p. 105). The same letter, or one next to it, has: "I have been obliged to build a new timber carriage compleat ... for which I paid the tradesmen" (p. 104), "The woman who lived with McLaughlin has been mad ever since you left" and "Inclosed I send the bearings of my farm, and hope you will be pleased to put your hand to it, that I may begin to improve" (p. 105). Reading [inference]: a settler's or employee's private letter of about 18-20 February 1809, written to someone in authority who had left the colony and could sign a land grant. The writer and recipient were not in the snippets; later queries hit archive.org errors. **Climate value: low.** "Very dry weather" in the Sydney summer of 1808-09 is one private remark, with no date for the start of the dry spell. Finishing T7 needs the page image (p. 103-105) or the djvu text through a working archive.org connection.

## T8. *Natuurkundig tijdschrift voor Nederlandsch-Indië*: eruptions remembered "in 1808" or "1809" (attempted, not finished)

archive.org's full-text search (fts) returned server errors on every query on 2 Nov. In-item searches: vol. 14 (1857) no hit for "1808"; vol. 59 (1900) failed mid-read; vol. 7 (1854) hOCR read: no "1808" or "1809" [OCR, partial page text]. BHL blocks robots. Earlier coverage stands: the 26 Oct Banda/Halmahera strand's fts queries ("1809" aardbeving Banda; "1809" uitbarsting Ternate) included NTNI hits and found no 1808-10 event; Wichmann's catalogue and the NTNI vols 80-82 earthquake list were read in October. **Result: not finished; retry when archive.org's fts answers.** T8 stays open.

## T10. Glass filter extended to Vanuatu and the Solomons (done) [calc]

Per-volcano summary of the 26 Oct GEOROC scores (7-oxide similarity to the 1809 Dome C and South Pole glass; same-source glasses usually ≥0.92-0.95; Tambora control 0.92). Script `scripts/glass_vanuatu_solomons_2026-11-02/summarise.py`; table `data/glass_vanuatu_solomons_by_volcano_2026-11-02.csv`. Almost all analyses are whole rock, which runs a little less silicic than glass, so a whole-rock score is a family match, not a source match (glass note section 9).

Vanuatu (best Dome C / best South Pole; analyses ≥0.92):
- Yasur and Tanna: 0.93 / 0.97; 32 of 104 analyses ≥0.92. High-K (K2O median 3.0). Yasur's persistent small eruptions cannot make a VEI 6; the older Siwi caldera is the only big-eruption source on Tanna.
- Ambrym: 0.92 / 0.95; 2 of 116. Mostly basalt (SiO2 median 51); its 1913 glass scores 0.86.
- Gaua: 0.91 / 0.94; 9 of 68 (as on 26 Oct).
- Epi and Kuwae (incl. Tongoa): 0.92 / 0.91; none ≥0.92. Lower K2O (median 1.0).
- Ambae (Aoba): 0.91 / 0.90; none. Basaltic (median 49).
- Below 0.87: Futuna, Ureparapara, Vanikoro, Matthew, Vanua Lava, Erromango, Hunter, Mota Lava, Efate, Lopevi, Mere Lava, Aneityum.
Solomons (all whole rock):
- No volcano with known young activity reaches 0.92. Savo 0.88 / 0.83; Bagana 0.87; Kolombangara 0.86; Tinakula 0.83; Simbo 0.75. One Rendova sample (old island, no known Holocene activity) scores 0.94 against South Pole.
- Bougainville's calderas (Billy Mitchell, Loloru, Takuan; Balbi has one analysis, 26 Oct) are not in the GEOROC files we hold. Added as U153.

**What this changes [inference].** Vanuatu's central and southern volcanoes belong to the same medium- to high-K andesite family as the 1809 glass, so Gaua is not unique within its own arc on major elements. Ambrym (basaltic) and Ambae fit worse, and Tanna's match comes from high-K lavas of a volcano without a known large caldera eruption in the last centuries. The Solomons and Bagana (Bougainville) fit worse than Vanuatu, Halmahera or New Britain; Bougainville's calderas are untested. This supports B53's ranking (Gaua top in Vanuatu, the Solomons not listed) and does not add a candidate. As before, only trace elements or a dated proximal tephra can choose.

## Records changed
open_tasks.md T5, T6, T10 done; T7 partly; T8 open. unavailable_sources.md U11 updated; U153 added. source_register.md section B74 rows. scripts/fetch_unavailable.py (deshima modes).

## T6 follow-up: Deshima registers read, 9 Nov 1808 to early April 1809 (2 Nov 2026, 18:30-19:15 UTC)

William ran `fetch_unavailable.py deshima` (inv. 222: 94 scans, 132 MB; inv. 257: 52 scans, 71 MB; on the Mac in archives/Nationaal_Archief/1.04.21_inv222/ and _inv257/). Read as page images [page image], contrast-enhanced halves.

**What kind of record it is.** Inv. 222 is titled "Japans Dagregister gehouden en gesloten door den Opperkoopman & Opperhoofd Hendrik Doeff van het merkwaardigste voorgevallen in dit Ryk, beginnende den 9 November 1808 en eyndigende den 22 November 1809" (scan 0013). It records only *the most remarkable events*, not every day, and has no regular weather column. Scans 0004-0012 are Doeff's "Register der Marginalen", an index of every marginal heading for the whole year with folio numbers; scans 0013-0019 hold the text for Nov 1808 to early April 1809.

**Weather and natural events entered, 9 Nov 1808 - 3 Apr 1809 [page image; my transcription of key words]:**
- 15 Dec 1808 (Thursday): towards evening it began to blow hard from the north-west, rising to a storm, "verzeld van regen en sneeuw" (with rain and snow). Margin: "Storm weeder".
- 16 Dec: hard wind from the west, sometimes north, with snow; a Chinese junk in sight.
- 17 Dec: the junk drifts out of sight again "door de harde noordelyke winden welke deeze daagen met stormvlagen gewaayd hebben, en hier en daar veel schaade veroorzaakten".
- 31 Dec: "Zeedert eenige dagen heeft het aldoor sterk uyt den Noorden met sneeuw en regen buyen gewaayd, somwylen met swaare storm buyen", causing accidents in the town and damage to the Dutch ships *Doorn* and *Lely*.
- 15 Jan 1809: a Chinese junk stranded on the Satsuma coast, 6 drowned. 5 Feb, 9 Feb, 8 and 16 Mar: more Chinese and other vessels wrecked or driven onto the coasts of Gotō, Satsuma and Nagasaki and brought in.
- 22 Mar 1809: a violent storm from the south-south-east, heavy lightning and thunder towards evening, clearing about 9 o'clock; the island's fence on the sea side blown down. 24 Mar: the storm returns as hard, damaging roofs and houses.
- Nothing else on weather. **We found no entry on the sun, sky colour, twilights, haze, darkness, ash, pumice or earthquakes in these pages, nor any heading for one in Doeff's index for the whole year Nov 1808 - Oct 1809** (index scans 0004-0012 read in full).

**Secret register inv. 257** (scans 0003-0008 spot-read, Nov 1808 - Jan 1809) [page image]: political only, the aftermath of the *Phaeton* incident of October 1808 (questions from the Nagasaki governor about Dutch and English ships, flags and signals, the coast defences, rumours at court). No weather. Scans 0009-0052 (Jan-Oct 1809) not read.

**What this means [inference].** A weak negative. Doeff wrote down storms that did damage, wrecks and trade, not the colour of the sky, so silence about the red skies that Edo sources report from 9 Jan 1809 (B43) is expected and does not count against them. The winter of 1808-09 at Nagasaki was stormy, with north winds, snow and a series of wrecked Chinese junks; that is ordinary for the north-east monsoon season and is not by itself evidence of anything volcanic. The register adds no date for the eruption.

**Still unread:** inv. 222 scans 0019-0094 (April - November 1809) and inv. 257 scans 0009-0052; inv. 221 and 223 not downloaded. Scans kept on the Mac for now (bulk-scans rule to be applied when reading is finished: cited pages are 222 scans 0004, 0005, 0013-0018).
