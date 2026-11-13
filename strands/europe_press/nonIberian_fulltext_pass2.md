---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: europe_press
date: undated
---

# Non-Iberian full-text sweep, pass 2 (periodicals, ship news, voyages): 1808/1809 eruption

Worker: non-Iberian full-text pass 2. Date: 2026-10-16. Status: done (budget-limited; see 'not reached').

Method: WebFetch on archive.org metadata API, advancedsearch and the in-book full-text endpoint
(`https://<d1>/fulltext/inside.php?item_id=..&doc=..&path=<dir>&q=..`). All quotes are OCR via
WebFetch (summariser caps quotes at ~125 chars, so long snippets were pulled out in consecutive chunks).
No page images were viewed. "p." = IA page index returned by the search API.
Constraint met during the session: WebFetch proxy budget (400 calls/hour shared by all agents) ran out
once; work was paced afterwards.

## SUMMARY OF STRONGEST RESULTS
1. **London "rose-coloured haze" re-dated to ~31 Mar and ~1 Apr 1809.** Source: Howard, *Athenaeum* 1 May 1809 p. 55. The notes are lettered and keyed to a table running from New Moon 16 Mar to 13 Apr 1809.
   This is the basis of Lamb's "early April 1809" sunset colouring. The evidence is weak and non-diagnostic: it fell in a cold, showery, hail-and-snow northerly spell. Howard's London notes for Dec 1808 – Mar 1809 contain **no** dry fog, dim or red sun, or unusual twilight.
2. **Etna, 27 March 1809: a flank eruption with heavy black-ash fall ~50 miles away**, probably at Messina ("several cart loads might have been collected";
   *Naval Chronicle* vol. 23, 1810, pp. 45–46). This is a dated NH eruption in the window, 4–5 days before the London haze. The timing is probably a coincidence; no transport to London has been shown.
3. **Paris Observatory, Dec 1808 and Jan 1809: 20 fog-days each** (*J. de physique* t. 68, p. 117, p. 182). These were wet fogs. The baseline is unknown, so this is not diagnostic.
4. **Cotte's multi-country chronicles of phenomena** for 1807–08 (t. 68 pp. 343–348) and 1809 (t. 70 pp. 205–212, 490) exist and list eruptions and earthquakes.
   Their OCR splits the columns, so entries cannot be dated from the text. Reading the page images is a high priority.
5. Tectonic negatives: Labrador earthquake **21 Jan 1809** (Moravian *Periodical Accounts* 4: 451); Namaqualand tremors **early Feb [1809]** (LMS); Cape Town
   earthquake 4 Dec 1809 (several sources; "serene sky ... stars shone bright"); Dunning (Perthshire) 18 Jan [1809].
6. Pacific negatives: Campbell (Hawaii Jan 1809 – Mar 1810) saw no smoke or fire at Mauna Loa. Mariner (Tonga 1806–10) describes Tofua's persistent
   small activity but no large eruption. Patterson (Fiji 1808–09) makes no sky remarks. The Azores São Jorge eruption of 1 May 1808 (*Naval Chronicle* 21) is earlier than the window.

## 1. Howard / Athenaeum: London sky notes Dec 1808 – Sept 1809 (resolved dates)

Key discovery: the original monthly *Athenaeum* (Aikin) issues Jan–Jun 1809 are on IA (SIM microfilm,
`sim_athenaeum-magazine_1809-0X-01_5_2X`), with Howard's lunar-period table AND lettered notes. The notes
are keyed by letters (a, b, c ...) to rows of the table, not by day numbers, which is why the 1818
*Climate of London* OCR looked like garbled day numbers. The 1833 2nd ed. vol. 2 (Wellcome scan IA
`b29350529_0002`) has much cleaner OCR of the same notes (pp. 79–109 cover Dec 1808–Dec 1809).

### 1A. Rose-coloured haze on an "opaque twilight", London (Plaistow), ~31 Mar and ~1 Apr 1809
- Observer: Luke Howard, Plaistow, Essex. Writing date: notes signed "L. H., Plaistow, 20th of 4th mo, 1809".
  Published *Athenaeum* vol. 5 no. 29 (1 May 1809), p. 55 (IA page index); reprinted Howard,
  *Climate of London* 1st ed. vol. 1 (1818) leaf 118 (IA `climatelondon00howagoog`) and 2nd ed. vol. 2 (1833) p. 85 (IA `b29350529_0002`).
- Verbatim (Athenaeum 1 May 1809, p. 55, OCR): "l. Showers, mixed with hail p.m. At sun-set an extensive blush of
  rose-coloured haze, spreading on the face of an opaque twilight, the clouds beneath (mostly cirro-stratus)
  at the same time rapidly dis- persing." / "m. Showers of hail, or rather of those hard snow-balls which form its
  basis. A huge Nimbus, affording these balls, mixed with snow, passed over about sun-set: after which the haze,
  &c. of last evening were repeated." / "o. Hail has appeared occasionally in the showers for the last few days.
  Stormy night." (1833 ed. p. 85 has identical wording.)
- Dating: the table on p. 54 runs "New Moon Mar. 16" to Apr. 13, 1809. In the OCR of the table rows the letter
  "k" sits at Mar 27, an unclear mark ("t.6." = probably "l.") at Mar 31, "m." at Apr 1, "n." at Apr 2 and 3
  (note "n. n. Showers of the kind last mentioned"), "o." at Apr 12. Hence: **l = 31 March 1809 (prob.),
  m = 1 April 1809** (±1 day; OCR of the table, not page image). Supported by the independent note of
  "Fourth Month, 6, 1809": "Some snow and hail had fallen at intervals, but no rain, for a week past" (1833 ed. p. 82).
- Period summary (p. 56): "The dense, fair, and dry weather which characterised the close of the last month,
  introduced the present, and continued, with little variation, to the 23d. The 24th and three succeeding days
  were wet and windy; and on the 28th a rapid and considerable decrease of Temperature took place, which, together
  with squalls from the North, and occasional smart showers of rain, hail, and sleet terminated the period."
  "Character, fair and warm to the first quarter: then cold, cloudy, and unfavourable to vegetation".
- Same period, note "fg" (≈21–22 Mar 1809): "A.M. very clear atmosphere below: Cirrus cloud only above. This soon
  became Cirro-cumulus, and p.m. came down, as before thunder, with a dull red halo round the Moon."
- Verification: OCR via WebFetch (two independent OCRs agree on the wording). Row-letter dating is inferred from OCR of the table.
- Independence: independent of Caldas/Unanue. This is almost certainly Lamb's (1970) "sunset colouration over London in early April 1809" cited by Guevara-Murua et al. 2014.
- Alternatives: occurs in a cold showery northerly outbreak with hail/snow; "rose-coloured haze" after showers with dispersing Cirrostratus is meteorologically ordinary. Howard records comparable coloured twilights in other years (e.g. 1806–07, and many in 1811–1813). Weak, non-diagnostic.
- Constrains: no more than "possible aerosol enhancement over London by ~1 Apr 1809".

### 1B. Other dated optical notes, London 1809 (OCR, 1833 ed. vol. 2 / 1818 vol. 1)
| Date | Text (OCR) | Source |
|---|---|---|
| 1 Dec 1808 (letter of John Capper, Stoke Newington) | "On the 1st of 12th month (Dec) 1808, a little after 5 o'clock a.m. I observed a Lunar Rainbow ..." | Athenaeum 1 Apr 1809 p. 56; 1818 leaf 106 |
| Dec 1808 – mid Jan 1809 notes | cloudy, frosty, snow; "Wild geese migrate in large flocks"; no haze/red-sky notes found (searched snow, sun, Barometer in Athenaeum Feb 1809) | Athenaeum 1 Feb 1809 p. 55–56 |
| 15–16 Jan 1809 | "On this and the preceding day the snow exhibited its beautiful blue and pink shades at sun-set" | Athenaeum 1 Mar 1809 p. 58 |
| 17 Jan 1809 | "The New Moon was very conspicuous on the 17th, the whole disk appearing, well defined." (earthshine) | same |
| 18 Jan 1809 | "though the Moon was still conspicuous, the Horns of the Crescent were obtuse" | same |
| 28 Jan 1809 | "a Lunar Halo of the largest diameter" | same |
| Feb–Mar 1809 (lunar period from New Moon 14 Feb; letter "c") | "a.m. much dew. At sunset the Cirrus cloud, highly coloured, with a strong pink tinge in the horizon. Some wind in the night." Period character: "Barometer remarkably high and steady ... frequent mists, dews, and hoar-frost" | 1818 leaf 113 / 1833 p. 80; Athenaeum Apr 1809 p. 56 |
| Feb–Mar 1809 | "Still misty weather: coloured halo, as also the following night." | 1818 leaf 114 |
| ~21–22 Mar 1809 | "dull red halo round the Moon" | Athenaeum May 1809 p. 55 |
| ~31 Mar & 1 Apr 1809 | rose-coloured haze, opaque twilight (1A) | |
| Apr–May 1809 | "A faint red blush on the evening twilight, followed by hoar frost." ; "A strong but not clear twilight; very calm nights of late, with much dew." | 1833 p. 87 |
| 19–20 June 1809 | "A blush on the evening twilight." | 1833 p. 94 |
| 18–20 Sept 1809 | "18. A blush on the evening twilight: windy. 19, 20. The same." | 1833 p. 100 |
| 24 Sept 1809 | "The moon rose clear, but with a red recess (as it were) round it" | same |
| 28 Sept 1809 | "much redness, as if from elevated Cirri, at sun set." | same |
| early Oct 1809 | "At sunset a dewy haze highly coloured in the E succeeded by much red in the W." | 1818 leaf 134 |
| Jan/Feb 1810 | "About 11 a. m. a pinky haze appeared in a snow storm under the sun, as before under the moon." | 1818 leaf 146 |
- Negative: no "dry fog", dimmed/pale/red sun, or persistent haze is recorded at London Dec 1808–Sept 1809.
  The pink/blue snow at sunset on 15–16 Jan 1809 is normal.

### 1C. "Cape of Good Hope, Dec. 8, 1809": earthquake of 4 Dec 1809 (not volcanic)
- Howard 1818 leaf 141 / 1833 vol. 2 p. 108, quoting a letter printed in *The Times*. OCR (1818): "Cape of Good Hope,
  Dec. 8, 1809. — On the 5th instant we were still in a state of alarm, on account of the earthquake the night before
  at half-past ten: we had three successive shocks of a tremendous nature, accompanied by a most awful sound. The
  whole lasted about three minutes, with an interval of hardly two seconds between each shock. During all the time
  there was a serene sky: the stars shone bright, but we observed [OCR illegible: '0fi fiacaffimoa fiamiflr ^ ifait/af/tRg' —
  probably 'an uncommon flashing of lightning' or similar] — (Times)."
- This is the well-known Cape Town (Milnerton/Blaauwberg) earthquake of 4 Dec 1809, 22:30 local. Tectonic; not volcanic.
  Irrelevant to the eruption except as a negative (no haze noted: "serene sky ... stars shone bright").

### 1D. Ball lightning on an (East India?) ship, newspaper dated ~14 Feb 1809
- 1818 leaf 115 (Athenaeum extract): "...The third ball came in contact with a Chinese, killed him, and wounded the main-mast
  in several places; the force of the air ... knocked down Mr. Lucas, the Chief Mate ... For some time after the storm
  subsided, a nauseous, sulphoreous smell continued on board the ship. (Apparent date by the Papers, Feb. 14.—Athenaeum.)"
  Lightning, not volcanic. Ship and place not identified in snippet.


## 2. Paris Observatory tables (Bouvard), *Journal de physique* t. 68 (1809), IA `journaldephysiqu68pari`
- Monthly "Observations météorologiques par M. Bouvard" with an "état du ciel" column (matin/midi/soir) and monthly counts
  ("Jours ... de brouillard"). Table for "DÉCEMBRE 1808." at IA p. 117; subsequent tables at pp. 182–183 (Jan 1809),
  264–265 (Feb), 349 (Mar?), 392–393 (Apr?), 456–457 (May?) (month assignment of the later tables inferred from order).
- OCR (inside.php "brouillard"): p. 117 (Dec 1808) has ten "état du ciel" entries such as "Brouillard épais.", "Couvert, brouillard.",
  "Pluie fine, brouillard." and the summary "[Jours] de brouillard ..... 20". Jan 1809 (p. 182): "de brouillard ......... 20";
  Feb (p. 264): 8; p. 392: 9; p. 456: 6. "Vapeurs" entries: p. 265 "Vapeurs, gelée à gla[ce]", p. 349 "Vapeurs, gelée bl[anche]",
  p. 393 "Vapeurs à l'horizon."
- Interpretation: 20 fog-days in each of Dec 1808 and Jan 1809 at Paris. That is high but winter radiation/advection fog in Paris
  is common; the entries are wet-weather fogs ("pluie fine, brouillard", "couvert") — no "brouillard sec", no red/pale sun
  in the snippets seen. NOT diagnostic without a baseline (Dec 1807/Dec 1809 counts not yet extracted).
- Also in t. 68: p. 82, fireball at Weston, Connecticut, 14 Dec 1807 (meteorite; irrelevant); Cotte, p. 334 (cited by Howard),
  hail storms 21 May 1808 in Loire and Lot.
- Verification: OCR via WebFetch. Page images not viewed.

## 3. Philosophical Magazine (Tilloch)
- IA has vols 33 (Jan–May 1809, `philosophicalmag33lond`), 35 and 36 (1810). Vols 32 and 34 not found on IA under the
  `philosophicalmag3Xlond` pattern (other copies may exist under Google ids; not located).
- Vol. 33: "volcano" 0 hits; "volcanic" 0; "hazy" 1 (astronomical, p. 75); "earthquake": p. 105 "earthquake felt at Dunning, in
  Perthshire, on the 18th of January, about two o'clock A.M." (year not in snippet; vol. 33 is 1809 so prob. 18 Jan 1809).
  Ordinary British tremor; not volcanic.
- Vol. 35 (1810): "earthquake" 0; "volcano" only geological theory (p. 378).
- Vol. 36 (1810): Vesuvius eruption narrative pp. 325–327 (dated "the 13th", month not in snippet; likely the Sept 1810 Vesuvius
  eruption); "Extract of a letter, dated St. Michael (Azores), August 24.— ... On the 11th of August, at ten P.M. slight shocks of an
  earthquake ... On the 12th at mid-day ... the village of Gozas ... was swallowed up, and in the spot where it stood a lake of
  boiling water gushed forth" (p. 409; 1810 São Miguel earthquake story, outside window; the "Gozas" detail is suspect).
- The monthly London meteorological table (Carey, Strand) has only a one-word weather column (Fair/Cloudy/Rain); not searched further.

## 4. Naval Chronicle
- IA: vol. 21 (Jan–Jun 1809) `navalchronicleco21londiala`; vol. 22 (Jul–Dec 1809) `navalchronicleco22lond`; vol. 23 `navalchronicleco23lond`;
  vol. 24 `navalchronicleco24londiala`; also vol. 20 (Jul–Dec 1808) `navalchronicleco20londiala` (IA metadata date "1799" is wrong).
- Vol. 21, IA p. 121 (printed p. 105): "NEW VOLCANO AT THE AZORES." Eyewitness letter: on Sunday 1 May [1808] about 1 p.m., from
  St. Anthonio [Pico], smoke from St. George [São Jorge], "a volcano had burst out about the centre of that island"; p. 122:
  "the large volcano, that had lain dormant for nine days, burst forth again like a roaring lion" (~11 May to 5 June). Crater ~4 miles
  from the sea, lava visible from Fayal. = the known São Jorge (Urzelina) eruption of 1 May 1808. Effusive/strombolian; 7 months
  before the window; cannot explain a bipolar signal. OCR via WebFetch (summarised, not fully verbatim).
- Vol. 21 "earthquake": p. 369 "During this tremendous gale, a shock of an earthquake was felt in several parts of the kingdom." (date not in snippet).
  "ashes": only Saragossa ("two thirds of the city is now in ashes") and rhetoric.
- Vol. 22 "volcano": p. 113 Ischia (geography); p. 114 figurative (gunfire); p. 353 a waterspout description ("assumed the resemblance
  of the crater of a volcano, with this exception, that it threw out nothing but large streams of cloud and spouts of sea-water").
  Not volcanic.

## 5. Asiatic Annual Register (AAR)
- Volume mapping (from IA titles): vol. 10 = 1808 (IA `in.ernet.dli.2015.85846`), vol. 11 = 1809 (`in.ernet.dli.2015.21987`,
  `in.ernet.dli.2015.109827`, `dli.bengal.10689.23498`), vol. 12 = 1810–11 (`in.ernet.dli.2015.68540`, `dli.bengal.10689.23446`).
- Access: the DLI scans have no page-level full-text index (inside.php returns page_count 1, no hits for "volcano"); the djvu.txt exists
  but has poor OCR ("tlie") and is ~1.5 M chars, readable only in 100k chunks by WebFetch. The first chunk of vol. 11 has no
  earthquake/volcano/haze/hurricane. **Not systematically searched: access barrier (budget).** Google-scanned
  `asiaticannualreNNunkngoog` items have unreliable dates; `asiaticannualre11unkngoog` is not vol. 11 (no "1809" hits).

## 6. Voyages and travellers
### Archibald Campbell, *A Voyage Round the World, from 1806 to 1812* (Edinburgh 1816; IA `avoyageroundwor00campgoog`, 1817 ed.; also Gutenberg #46468)
- p. 39 (Kamchatka, Petropavlovsk, 1807): "One of them is a volcano; and when we could see the top, which was seldom free from clouds, it was
  constantly smoking, and at night sparks were frequently [to] be seen. An eruption took place some time before our arrival, by which the
  whole town was covered with ashes." (Avachinsky or Koryaksky; arrival in 1807; outside window.)
- p. 56 (Sannak/Halibut Island, Alaska Peninsula, wintering after the wreck of Jan 1808, i.e. ~Feb–Apr 1808): "the remarkable volcano
  mentioned by Captain Cook, bore n. n. w. from our tent. It was constantly smoking during the day, and at night we could frequently see
  the flames." (Probably Shishaldin or Pavlof/Isanotski; persistent activity early 1808; small.)
- p. 97 (Hawaii, he arrived Jan 1809 and stayed to Mar 1810): "Mouna-roa, one of the mountains in the interior is a volcano; a few years
  before this time a violent eruption took place, when it sent forth a stream of lava which ran into the sea. ... We did not see any flame
  or smoke issuing from the crater." (The "few years before" flow is probably Hualalai 1801.) **Negative for Hawaii 1809.**
- "earthquake": 0 hits.
- Verification: OCR via WebFetch. Independence: independent eyewitness.

## 7. Moravian *Periodical Accounts* vol. 4 (1806–1810), IA `periodicalaccoun04mora`
- Labrador: IA p. 459 (printed p. 451; index p. 517 "Earthquakes, in Labrador, 451. At the Cape, 4[8]6."). Letter of Aug/Sept 1809 from a Labrador
  station (Nain/Okkak/Hopedale letters are on pp. 453–463): "January 21, 1809, and for some days after, we perceived some shocks of
  earthquakes, which seemed to be felt, as far as we could learn, all down the coast." OCR via WebFetch, verbatim.
  Event date 21 Jan 1809 (+ some days). Tectonic (Labrador Sea intraplate seismicity); independent. Not volcanic; no sky effects reported.
- Cape: IA p. 483–484, Gnadenthal letter dated Oct 13, 1809 and the Gruenekloof diary: "terrible earthquake" Monday [4 Dec 1809]
  about 10 p.m., ~13 shocks; on the 5th fissures and new springs throwing up white sand between Gruenekloof and Cape Town; Cape Town
  5 shocks, cracked walls, rent in castle vault, people camped in tents. Same event as Howard's "Cape of Good Hope, Dec. 8, 1809".
- Sky search ("sun", pp. 380–515): only Niagara rainbows (p. 502). No haze/red-sun notes in 1808–09 mission diaries via this term.
- Coverage: Greenland, Labrador, Cape (Gnadenthal, Gruenekloof), Antigua, Danish West Indies, Surinam, North America (Gracedale etc.).

## 8. London Missionary Society, *Transactions of the Missionary Society* vols 2–3 (IA `transactionsmis00socigoog`, NYPL copy)
- Covers Tahiti (letter "Matavai, Otaheite, Feb. 3, 1809", IA p. 160; "We embarked at Huaheine, October 26, 1809; and arrived at
  Port Jackson, February 17", p. 411), the Cape/Bethelsdorp ("Annual Report of Bethelsdorp for the Year 1809", p. 379), Namaqualand
  (C. Albrecht, "November 7, 1809", p. 406), India (p. 422).
- "earthquake": p. 388, Cape Town, letter of Mrs Smith: "an alarming earthquake" (shocks began on the 4th [Dec 1809]); p. 390 "The
  earthquake continues to be heard and felt from time to time at the Cape"; **p. 406, Namaqualand (Albrecht's report, closing Nov 7, 1809):
  "February.—In the beginning of this month, two shocks of an earthquake were felt at a place where some Kaminquas reside"** — probably
  early Feb 1809 (year inferred from the report; ±1 yr). Tectonic, interpreted by locals as divine anger. Not volcanic.
- "volcano" 0; "atmosphere" 0. No Tahiti sky notes found by these terms (note: index flags leaf0 missing; "sun" not searched — too many "Sunday" hits).

## 9. William Mariner / John Martin, *An Account of the Natives of the Tonga Islands* (London 1817), vol. 1 (Wellcome IA `b29335784_0001`)
- Mariner lived in Tonga Nov/Dec 1806 – 1810. IA p. 322, chap. VIII (events c. 1807–08, under Finow): "On the island of Tofooa there is a
  small volcano, situated near the northern extremity, from which smoke almost constantly issues, and pumice-stones are very frequently
  thrown out. An eruption of flame takes place, sometimes twice or thrice a week, and at other times scarcely once in two months, and
  generally lasts from one to two or three days. There was at this time no eruption of flame, which had ceased a few hours before, after
  having lasted three days ... smoke there was, however, in abundance".
- Constrains: Tofua (Tonga, 19.75°S) was in persistent strombolian activity c. 1807–08 with frequent pumice; Mariner, resident to 1810,
  reports no major Tongan eruption. Negative evidence for a large Tongan eruption 1808–09 (weak: the book is not a diary).
- "earthquake": p. 395, figurative ("shaken as if by an earthquake").

## 10. V. M. Golovnin, *Puteshestvie ... shliupa Diany ... v 1807, 1808 i 1809 godakh* (St Petersburg 1819), IA `Puteshestvierossijskagoimperatorskagoshl58`
- Diana was detained at Simon's Bay (Cape) Apr 1808 – May 1809, then crossed the Indian Ocean south of Australia to Tanna (New Hebrides;
  Yasur volcano) late July–Aug 1809, then Kamchatka (Sept 1809). A first-rank observer of SH skies Dec 1808–1809.
- Access: OCR is very poor (pre-reform Cyrillic, garbled). "огнедышущ", "волкан": 0 hits (probably OCR failure, not absence).
  "1809": 5 hits: p. 297 "[3]о Генваря 1809 года поймали мы сию рыбу" (fish caught 30 Jan 1809), p. 347 (frigates Cornelia and
  Iphigenia at the Cape in 1809), p. 360 (Feb–Mar 1809 heaving down a 64-gun ship), p. 364 (winds at Simon's Bay, "Мы въ Генварѣ 1809 года
  долго имѣли вѣтры ..."), p. 412 ("Іюля 26 го дня 1809 го года", Tanna). **Not usable for systematic search here.** Lead: the Tanna chapter
  (Yasur activity, July–Aug 1809) and the Cape weather journal should be read in a clean edition (Golovnin, Sochineniia, Moscow 1949/1961;
  English: *Detained in Simon's Bay*, Van Riebeeck Soc./Friends of SA Library 1964).

## 11. Etna eruption of 27 March 1809, with heavy ash fall ~50 miles away (Naval Chronicle vol. 23, 1810)
- Source: *Naval Chronicle* vol. 23 (Jan–Jun 1810), IA `navalchronicleco23lond`, IA pp. 45–46: "ERUPTION OF MOUNT ETNA. The following copy of a letter,
  from a British officer in Sicily, furnishes a more picturesque and circumstantial account of the late eruption of Mount Etna, than any other that has appeared".
- Verbatim (OCR): "On the morning of the [2]7th of March, about seven o'clock, advices of an eruption of Etna were conveyed hither, by a very swift courser, a cloud
  of black ashes from the mountain top, which is 50 miles distant in a straight line. These ashes, borne on a hard gale of wind, showered into the town
  in such quantities, that several cart loads might have been collected from the streets and house-tops. They resembled gunpowder; so much so, indeed,
  that an Irish soldier, in the citadel, called out, 'Blood and turf! the wind has forced open the magazine doors, and here's all the powder blowing about
  the barracks.'" ... "On the evening of the same day, an eruption of lava took place at a short distance below ... another broke out next day, with
  greater fury than the former, about five miles lower down, at a place called Monte Negro. The latter displayed three vast columns of flame and smoke ...
  one which broke out two hours after the first alarm, about twelve miles below Monte Negro, and eight west of Lingua Grossa ... This eruption has formed
  a row of craters ... running in a North-East direction from the top of the mountain."
- Observer: unnamed British officer, a garrison town with a citadel ~50 miles from the summit (almost certainly Messina). Event date: 27 March [1809]
  (year from context: "the late eruption", vol. for 1810; matches the known Etna NE-flank eruption of 27 Mar 1809). Writing date: spring 1809. Publication 1810.
- Verification: OCR via WebFetch ("?7th" read as 27th). Independent of Caldas/Unanue.
- Significance: a well-dated, ash-producing NH eruption in the window. Small (flank fissure, VEI ~2); tropospheric. Cannot produce a bipolar sulfate
  signal. **Timing coincidence**: Howard's London rose-coloured haze (~31 Mar–1 Apr 1809, sect. 1A) came 4–5 days after; transport of Etna ash/SO2 to London
  in that time is conceivable but unproven and the London weather was a cold northerly outbreak (unfavourable trajectory from Sicily). Note as alternative.
- Vol. 23 also, IA p. 266: "In the island of St. George, a volcano burst forth during the year 1808." (Azores, cf. sect. 4).
- Vol. 23, IA p. 209: "EARTHQUAKE, AND DISAPPEARANCE OF AN ISLAND, AT THE CAPE OF GOOD HOPE ... In December an earthquake was felt at Cape Town" — the Dec 1809
  Cape quake with a (false) rumour that Robben/Penguin Island had sunk.
- Vol. 21 "pumice": p. 121, São Jorge 1808: "In two days it had thrown out cinders or small pumice stones"; p. 238 "nor did I ever observe any pumice-stone or lava in these islands" (context not identified).

## 12. Other periodicals sampled
- *Belfast Monthly Magazine* (SIM, 1809 issues on IA) — naturalist's diary/meteorological report (J. Templeton?) Dec 20 1808 – Jan 20 1809 (issue of
  31 Jan 1809, IA `sim_belfast-monthly-magazine_1809-01-31_2_6`, pp. 77–78): entries like "Dec. 31. A mild day. Common Wren singing.", "Dark calm warmish day",
  "Cold dark day with a slight shower", "Pleasant, bright, frosty day". ("Dark day" = overcast in this diarist's usage.) No haze/red sky. Negative.
- *Gentleman's Magazine* (SIM monthly issues 1809 on IA): Meteorological Diary in Feb 1809 issue (IA p. 1; Jan 1809 days): "clear, evening foggy", "cloudy,
  considerable fall of snow in the morning"; no "hazy". Negative (sampled one issue only).
- *Monthly Magazine* (London) 1809 SIM issues exist on IA (`sim_monthly-magazine_1809-0X-01_27_18X`) — not searched (budget).
- *Gilbert's Annalen der Physik* Bd. 31 (1809), IA `sim_annalen-der-physik_1809_31` (long-s OCR as "f"): "Höhenrauch" 0; "Vulkan" 1 (Teide, 1791); "Erdbeben" 1 (generic).
  Bd. 32–36 exist on IA (`sim_annalen-der-physik_1809_32`, `_33`, `sim_annalen-der-physik_1810_34`…) — not searched.
- *Athenaeum* 1 June 1809 (IA `sim_athenaeum-magazine_1809-06-01_5_30`, p. 57): notes "o. A faint red blush on the evening twilight, followed by hoar frost."
  and "p. A strong but not clear twilight: very calm nights of late, with much dew." — lunar period ~14 Apr–13 May 1809; table OCR too poor to date the letters
  (probably early May 1809).

## 13. Cotte's "Tableau chronologique des phénomènes météorologiques observés en différens pays" (*Journal de physique*) — HIGH-PRIORITY LEAD
- t. 68 (1809), IA `journaldephysiqu68pari`, pp. 343–348, heading "ANNÉES 1807 — 1808": a multi-country chronicle (earthquakes, storms, snow) with the Paris
  weather alongside, e.g. "Tr. de terre considér. à Lisbonne", "Tr. de terre à Cahors, Brioude, Mende, Nismes, Montpellier, Saumur, Clermont en Auv., etc.",
  "Tr. de terre à Gênes, dans le Piémont ...", "Trembl. de terre à Pignerol" (= Pinerolo, 2 Apr 1808), "Nouvelle secousse ... à Pignerol". It seems to end
  in spring 1808 here; the continuation for the rest of 1808 is probably in t. 69 (not searched).
- t. 70 (1810), IA `journaldephysiqu70pari`, pp. 205–212 (+ "Suite du Tableau" p. 490): "Des Phénomènes météorologiques observés en différens pays", from
  Cotte's "Paris. Année 1809". Entries include p. 208 "... abondante à Tarbes, départem. des Hautes-Pyrénées, éruption violente de l'Etna." and
  "éruption du Vésuve et de l'Etna"; p. 210 "Grêle désastreuse près de Bâle. Éruption du Vésuve."; p. 211 "Septembre. ... 4 Éruption du Vésuve, orage et chute
  de la foudre à Bonn. ... Octobre. 26 Trembl. de terre à Lisbonne. Novembre. Froid très-vif dans le nord de l'Europe. Décembre, ..." (year presumably 1809).
- The IA OCR splits the table columns, so dates for each line cannot be recovered via the snippet API; no "brouillard sec"/haze lines were found in these pages
  by "brouillard" or "brouillards" searches (t. 70 "brouillards": only p. 16, an analogy with the 1783 fog). **Read these pages as images (IA or Gallica) to
  obtain the Dec 1808–1809 entries.** These tables are the most likely place in the French literature for a 1809 "brouillard sec" or coloured-sky report.

## 14. Books/voyages enumerated and NOT searched or out of window (for the register)
- Krusenstern (voyage 1803–06), Lisiansky (1803–06), Langsdorff (1803–07), Turnbull (1800–04), Lichtenstein (Cape 1803–06), Delano 1817 (voyages to 1807):
  their voyages end before Sept 1808 — not searched.
- Fanning, *Voyages round the World* (1833): IA copy `voyagesroundworl0000fann` (1970 reprint) is access-restricted; inside.php failed. BSB copy `10469325bsb` not checked.
- Samuel Patterson, *Narrative of the Adventures and Sufferings* (Palmer, Mass. 1817), IA `narrativeofadven00pattrich`: wrecked on a reef in Fiji
  20 June 1808 ("S. lat. 17, 40; E. long. 179"), in Fiji into 1809 (to the consul "in July, 1809"). "sun": no sky-appearance remarks; no volcano/earthquake/ash. Negative.
- Golovnin *Diana* (sect. 10): poor OCR.
- Not reached (budget): Henry Salt, *Voyage to Abyssinia* (1814; Mozambique and Red Sea 1809–10); John Mawe, *Travels in the Interior of Brazil* (1812);
  James Prior, *Voyage along the Eastern Coast of Africa* (1819; Nisus 1810–11); W. Lockerby, *Journal ... Fijian Islands 1808–1809* (Hakluyt 1925);
  Asiatic Annual Register vols 10–12 chronicle sections; Monthly Magazine 1809; Nicholson's Journal vols 21–26; Annales de chimie; Moniteur;
  Mémoires d'Arcueil; Annals of Philosophy; Bibliothèque britannique 1809 (not found on IA; Gallica/Google blocked); Cape Town Gazette (not online here);
  Lloyd's List 1808–10 (digitised by HathiTrust/Google — blocked here); American ship news (Salem Gazette, Boston Columbian Centinel — not on IA in searchable form).

---

## SEARCH LOG (all via WebFetch on archive.org; inside.php = in-book full-text search)
| Item (IA id) | Queries | Coverage | Result |
|---|---|---|---|
| climatelondon00howagoog (Howard 1818 v.1) | twilight, haze, sun, Cape, 1810, pinky, Mo., sunset, Fourth, hail, Third, Tab., ball, ship, lightning, coloured, misty, dew | 1806–1818 | hits (1A–1D); notes are letter-keyed |
| b29350529_0002 (Howard 1833 v.2) | twilight, hail, 1809 | 1806–1819 | clean OCR of 1809 notes (pp. 79–109) |
| b29350529_0002 djvu.txt; climatelondon00howagoog djvu.txt | offset reads | – | WebFetch returns only first ~70–80k chars: unusable for deep pages |
| sim_athenaeum-magazine_1809-01…06 | haze, hail, Plaistow, Moon, a.m., cloud, Barometer, snow, sun, twilight | Nov 1808–May 1809 | hits; Apr issue "sun" query rate-limited (429) |
| philosophicalmag33lond / 35 / 36 | volcano, volcanic, earthquake, hazy | 1809–1810 | Dunning quake; Vesuvius 1810; Azores 1810 |
| journaldephysiqu68pari | brouillard, vapeurs, OBSERVATIONS MÉTÉOROLOGIQUES, décembre, volcan, 1808, Trembl., terre, Marche | 1809 | Dec 1808 table p.117 (20 fog days); Cotte 1807–08 tableau pp.343–348 |
| journaldephysiqu69natr | terre | 1809 | Humboldt/Jorullo only |
| journaldephysiqu70pari | brouillards, 1809, tremblement, Vésuve, éruption, Etna, Tarbes, Mars, Brouillard, Janvier | 1810 | Cotte 1809 tableau pp.205–212 (columns split) |
| asiaticannualre11unkngoog | volcano, 1809 | ? | 0 (not the 1809 vol.) |
| in.ernet.dli.2015.21987 (AAR vol. 11, 1809) | volcano; djvu.txt first chunk | 1809 | no page index; poor OCR; barrier |
| navalchronicleco21londiala | volcano, earthquake, ashes, Azores, pumice | Jan–Jun 1809 | São Jorge 1808 |
| navalchronicleco22lond | volcano, crater, earthquake | Jul–Dec 1809 | negative (waterspout) |
| navalchronicleco23lond | volcano, Etna, earthquake | Jan–Jun 1810 | **Etna 27 Mar 1809 ashfall**; Cape quake |
| avoyageroundwor00campgoog (Campbell) | volcano, earthquake | 1806–12 | Kamchatka 1807, Alaska 1808, Hawaii 1809 negative |
| voyagesroundworl0000fann (Fanning) | 1809 | – | fetch error (restricted) |
| periodicalaccoun04mora (Moravian) | 1809, earthquake, January 21, earthquakes, sun | 1806–10 | Labrador quake 21 Jan 1809; Cape Dec 1809 |
| transactionsmis00socigoog (LMS) | 1809, earthquake, Kaminquas, volcano, atmosphere | 1806–12 | Namaqualand quake Feb [1809]; Cape Dec 1809 |
| b29335784_0001 (Mariner) | volcano, Tofooa, earthquake | 1806–10 | Tofua persistent activity |
| Puteshestvierossijskagoimperatorskagoshl58 (Golovnin) | огнедышущ, волкан, 1809, Генварь | 1807–09 | poor OCR |
| narrativeofadven00pattrich (Patterson) | 1808, 1809, sun | Fiji 1808–09 | negative |
| sim_belfast-monthly-magazine_1809-01-31_2_6 | sun, Dec., day | Dec 1808–Jan 1809 | negative |
| sim_gentlemans-magazine_1809-02_79 | hazy, METEOROLOGICAL, foggy, morning | Jan 1809 | negative |
| sim_annalen-der-physik_1809_31 | Vulkan, Höhenrauch, Erdbeben | 1809 | negative |
| IA search APIs | advancedsearch / scrape for Phil. Mag., J. de physique, Asiatic Annual Register, Naval Chronicle, Athenaeum, Gentleman's Mag., Monthly Mag., Bibliothèque britannique, Annalen der Physik, Periodical Accounts, Transactions of the Missionary Society, Campbell, Fanning, Mariner, Golovnin, Patterson | – | identifiers in register |
| Bibliothèque britannique 1809 | IA advancedsearch/scrape | – | not on IA with usable metadata |
| WebFetch budget | – | – | proxy budget (400/h shared) exhausted 5 times; paced with waits |

## Source register
| Source/edition | Region/lang | Type | Covers 1808–09? | Digitized (URL) | Access from here |
|---|---|---|---|---|---|
| *Athenaeum* (Aikin) vol. 5, Jan–Jun 1809 monthly issues (Howard's register) | London; EN | magazine, met. register | yes (Nov 1808–May 1809) | https://archive.org/details/sim_athenaeum-magazine_1809-05-01_5_29 (and _01_5_25, _02_5_26, _03_5_27, _04_5_28, _06_5_30) | OCR search works |
| Howard, *Climate of London* 1st ed. vol. 1 (1818) | London; EN | met. diary | yes | https://archive.org/details/climatelondon00howagoog | OCR search |
| Howard, *Climate of London* 2nd ed. vol. 2 (1833), Wellcome | London; EN | met. diary | yes | https://archive.org/details/b29350529_0002 | OCR search (clean) |
| *Philosophical Magazine* vol. 33 (1809), 35–36 (1810) | UK; EN | journal | yes | https://archive.org/details/philosophicalmag33lond | OCR search |
| *Philosophical Magazine* vols 32, 34 | UK; EN | journal | yes | not found on IA | not reached |
| *Journal de physique* t. 68 (1809), 69 (1809), 70 (1810) | FR | journal, Paris obs. tables, Cotte chronicles | yes | https://archive.org/details/journaldephysiqu68pari ; …69natr ; …70pari | OCR search; tables column-split (need images) |
| *Naval Chronicle* vols 20–24 (1808–10) | UK; EN | naval periodical | yes | https://archive.org/details/navalchronicleco21londiala ; …22lond ; …23lond | OCR search (21–23 searched) |
| *Asiatic Annual Register* vol. 10 (1808), 11 (1809), 12 (1810–11) | India; EN | annual | yes | https://archive.org/details/in.ernet.dli.2015.21987 (vol. 11) ; in.ernet.dli.2015.85846 (vol. 10) ; in.ernet.dli.2015.68540 (vol. 12) | digitised, poor OCR, no page index: not searched |
| *Gentleman's Magazine* 1809 (monthly SIM issues) | UK; EN | magazine, met. diary | yes | https://archive.org/details/sim_gentlemans-magazine_1809-02_79 | OCR search (1 issue sampled) |
| *Monthly Magazine* 1809 (SIM issues) | UK; EN | magazine | yes | https://archive.org/details/sim_monthly-magazine_1809-03-01_27_182 | digitised; not searched |
| *Belfast Monthly Magazine* 1809 (SIM) | Ireland; EN | magazine, naturalist's diary | yes | https://archive.org/details/sim_belfast-monthly-magazine_1809-01-31_2_6 | OCR search (1 issue) |
| Gilbert's *Annalen der Physik* Bd. 31–36 (1809–10) (SIM) | DE | journal | yes | https://archive.org/details/sim_annalen-der-physik_1809_31 | OCR search (Bd. 31 only) |
| *Bibliothèque britannique* (Geneva), Sciences et arts 1809 | CH; FR | journal, Geneva tables | yes | Gallica/Google (blocked); not found on IA | not reached |
| Nicholson's *Journal of Natural Philosophy* vols 21–26 | UK; EN | journal | yes | probably IA/BHL | not reached (budget) |
| *Annales de chimie*, *Moniteur universel*, *Mémoires d'Arcueil*, *Annals of Philosophy* | FR/UK | journals/newspaper | yes/retro | Gallica/IA | not reached |
| *Periodical Accounts ... United Brethren* vol. 4 (1806–10) | Labrador, Greenland, Cape, W. Indies; EN | mission reports | yes | https://archive.org/details/periodicalaccoun04mora | OCR search |
| *Transactions of the Missionary Society* vols 2–3 | Tahiti, Cape, Namaqualand, India; EN | mission reports | yes | https://archive.org/details/transactionsmis00socigoog | OCR search |
| A. Campbell, *A Voyage Round the World, from 1806 to 1812* (1816/1817) | Kamchatka, Alaska, Hawaii; EN | travel | yes | https://archive.org/details/avoyageroundwor00campgoog | OCR search |
| W. Mariner / J. Martin, *Account of the Natives of the Tonga Islands* (1817) | Tonga; EN | ethnography/narrative | yes (1806–10) | https://archive.org/details/b29335784_0001 | OCR search |
| S. Patterson, *Narrative of the Adventures and Sufferings* (1817) | Fiji; EN | narrative | yes (1808–09) | https://archive.org/details/narrativeofadven00pattrich | OCR search |
| V. M. Golovnin, *Puteshestvie ... shliupa Diany* (1819) | Cape, Indian Ocean, Tanna, Kamchatka; RU | voyage | yes (1807–09) | https://archive.org/details/Puteshestvierossijskagoimperatorskagoshl58 | OCR poor; needs clean edition |
| Golovnin, *Detained in Simon's Bay* (English tr., 1964) | Cape; EN | voyage (tr.) | yes | not online | not reached |
| E. Fanning, *Voyages round the World* (1833) | Pacific; EN | voyages | partly | IA `voyagesroundworl0000fann` (restricted), `10469325bsb` | not reached |
| A. Delano, *Narrative of Voyages* (1817) | Pacific; EN | voyages | no (to 1807) | IA | not searched (out of window) |
| Krusenstern, Lisiansky, Langsdorff, Turnbull, Lichtenstein | various | voyages/travel | no (end ≤1807) | IA | not searched (out of window) |
| W. Lockerby, *Journal ... Fijian Islands 1808–1809* (Hakluyt Soc. 1925) | Fiji; EN | journal | yes | not on IA (in copyright) | not reached |
| H. Salt, *A Voyage to Abyssinia* (1814) | Mozambique, Red Sea; EN | travel | yes (1809–10) | IA (ids not looked up) | not reached |
| J. Mawe, *Travels in the Interior of Brazil* (1812) | Brazil; EN | travel | yes (1807–11) | IA (ids not looked up) | not reached |
| J. Prior, *Voyage along the Eastern Coast of Africa* (1819) | E. Africa; EN | voyage | 1810–11 | IA | not reached |
| *Cape Town Gazette and African Advertiser* 1808–10 | ZA; EN/NL | newspaper | yes | NLSA? | not reached |
| *Lloyd's List* 1808–10 | world shipping; EN | shipping list | yes | HathiTrust/Google (blocked) | not reached |
| Salem Gazette / Columbian Centinel / American ship news 1809 | US; EN | newspapers | yes | Readex/Chronicling America (pre-1836 sparse) | not reached |
| *The Times* (London) 1809 | UK; EN | newspaper | yes | not free | not reached (quoted second-hand by Howard) |
