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

# Dutch newspapers (IA mirror of Delpher), round 2: searches of 1808–1811 issues, the Lamongan line on p. 327, and Bosch (TITLV 1858)

Worker: round 2, strand "dutch_papers". Date: 2026-10-16.

**Verification level for everything below:** the text is OCR obtained through WebFetch, from three places: the archive.org full-text search (fts), the in-book search (`fulltext/inside.php`, which also returns word bounding boxes), and the per-issue `_djvu.txt` files. **No page images were viewed.** The WebFetch summariser limits quotes to about 125 characters, so longer passages are given as consecutive fragments. Dutch OCR renders the long s as "f" (for example "uitbarfting" or "fchok").

---

## 0. Summary

1. **Lamongan line (NTNI vols 80–82, p. 327; IA `mobot31753002490180`).** The word bounding boxes and the full line of the paragraph show a running-text list. In almost every item the date comes before the year ("22/11 1815 Soerabaja", "23/1 '17 Idjen", "8/11 '17 heel Java", "25/9 '21 Djapara", "Mei 1824 Kedoe", "Maart 1830 Lamongan", "15/12 1830 Bromo"). Read that way, the string is "1808, | 5 Dec. 1810, 24/3 1814, 10/3 1815 …". This gives **"5 Dec. 1810"**, and **"1808" stands alone as a bare year**. "1808, 5 Dec." cannot be ruled out, because the very first item is in year-first form ("1806. Loemadjang. Uitbarsting van de Lamongan"). On balance, the internal evidence favours **5 Dec 1810**, so this page should *not* be counted as a third witness for a Lamongan eruption on 5 Dec 1808. Settling it fully needs the page image. Details in §3.
2. **Bosch, "Uitbarstingen der vulkanen Idjin en Raun (Banjoewangi)", TITLV [vol. 7, 1858]. Found on IA as `tijdschriftvoor38unkngoog`, article pp. 283–304 in IA pagination.** The Raung eruption in Wikkerman's time is **undated within 1800–1808 and "of little importance"**: "De vierde uitbarsting had plaats toen de heer J. C. von Wikkerman … als kommandant civiel en militair zich hier bevond (van 1800-1808) doch was van weinig beteekenis." The next dated events are a small Raung eruption with much ash in **1812**, with earth tremors and thunder-like noises until 1814, then the Raung eruption of 1815–16 and the Ijen eruption of 1817. The article gives **no 1806–1810 eruption date**. Details in §4.
3. **Dutch home papers, Dec 1808 – Jun 1809: no report of a pale or red sun, dry fog, haze or abnormal twilight was found.** The weather and sky items in this window are ordinary winter phenomena:
   - snowfall and avalanches in the Alps and Italy (night of about 12 Dec 1808);
   - snow at Nice and Florence (Dec 1808);
   - the ice-jam floods of the Rhine and Waal in Feb 1809, which people at Gorinchem mistook for an earthquake shock.
   
   The OCR is poor, so this negative result is weak.
4. **News from the East Indies is almost absent from the home papers in 1809.** In 1809 "Java" appears only in estate notices. The capture of Amboina on 19 Feb 1810 reached the Dutch papers only on 5–19 Oct 1810, which is a lag of about 7.5 months, and it came via English papers. The home papers therefore cannot be expected to carry Dec 1808 Javanese events before about late 1809, and the British blockade suppressed even that. The *Bataviasche koloniale courant* (from Jan 1810) carries no eruption, earthquake or ash report from Java in the issues sampled (14 and 21 Dec 1810). Its only "aardbeving" hit for 1810–11 is the Cape earthquake of 4 Dec 1809, already noted in pass 3.
5. **Volcanic news actually printed, 1808–1810.** All of it is European or Atlantic and well known: Vesuvius (Aug 1808; Jan–Feb 1809; Sep 1809; late 1810), **Etna (Mar–Apr 1809; ash 2–3 fingers deep on Calabria)**, and São Jorge in the Azores (1808; "NEW VOLCANO", Dabney letter, reprinted in US papers in Feb–Mar 1809). None of it points to a tropical eruption in Dec 1808.

---

## 1. Method (how the IA mirror was searched)

- **fts endpoint.** `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=QUERY&filter_map=…`
  - Year filter: `{"year":{"1809":"gte","1810":"lt"}}`. **Do not use the same year as both keys.** The JSON then has a duplicate key and the filter silently fails, returning all years. `lt` on the next year works.
  - **New: a collection filter works.** Add `"collection":{"newspapers":"inc"}` to `filter_map` to restrict results to newspapers. This covers the ddd_ Dutch papers plus US papers (Alexandria Gazette, Kentucky Gazette, Pittsburgh Gazette, Newport Mercury) and Italian ones (Giornale del Campidoglio).
  - Full URL that worked: `…&user_query=aardbeeving&filter_map=%7B%22year%22%3A%7B%221808%22%3A%22gte%22%2C%221811%22%3A%22lte%22%7D%2C%22collection%22%3A%7B%22newspapers%22%3A%22inc%22%7D%7D`
  - **Limits.** The WebFetch proxy rejects URLs above a certain length, so drop `hits_per_page` when combining filters. `OR` does not appear to work. Two-word queries behave roughly as AND. Recall looks low: only 12 hits for "nevel" across all 1809 newspapers, so the OCR or index is patchy.
- **Issue text.** `https://archive.org/download/<id>/<id>_djvu.txt` returns a 302 to a datanode; fetch the redirect URL. Some fetches fail with a client error.
- **In-book search.** `https://<d1>/fulltext/inside.php?item_id=X&doc=X&path=<dir>&q=…` (d1 and dir come from `/metadata/X`). The response includes **word bounding boxes**, which allow line layout to be reconstructed without the image. A rate limit (HTTP 429) was hit once on ia601907 and cleared after a few minutes.

---

## 2. Findings from the newspapers (event date ≠ paper date)

| # | Paper (IA id) | Paper date | Dateline / event date | What it says (OCR, verbatim fragments) | Relevance |
|---|---|---|---|---|---|
| N1 | Vriesche courant (`ddd_010180406_mpeg21`) | 27 Jan 1809 | Leeuwarden 26 Jan; Zurich news of 29 Dec 1808; event night of "1/ December" (probably 12 Dec, see N2) 1808 | "Opmerkelyk is het, dat de meeste Lavinen in den nacht op den 1/ Pecember neder vielen." / "Zou veelligteen Aardbeving of eenige andere elekcriekt Be neging daarvan de oorzaak zyn?" / "De (tand des Barrometers was in den nacht zeef aag." | Alpine avalanches (Grisons, Bernese Oberland, Forest Cantons) after about 14 days of snow and very low pressure. **Meteorological, not volcanic.** Shows a deep cyclone over the Alps about 11–12 Dec 1808. |
| N2 | Utrechtsche courant (`ddd_010813658_mpeg21`) | 11 Jan 1809 | Nice "den aa [?] December"; Florence; Altorf "15 December"; Bern "19 December" [1808] | Nice: "By Menfchen geheugen heeft men vus Land door geen zulk eene meenigte Sneeuw bedekt gezien" … "dat men genoegfaam een Luchtverfchynfel kan noemen". Florence: "dat dit verfchynfel, flechts eenmaal in de laarsleedene Eeuw heèft plaats gehad" (compared with 1708/1709). Bern: "In den nacht van den 12," (avalanches). | Exceptional snow in Mediterranean France and Italy, Dec 1808. Weather context for the cold Dec 1808 – Jan 1809. **No haze or sun anomaly mentioned.** |
| N3 | Ommelander courant (`ddd_010216234_mpeg21`), 9 Dec 1808; Rotterdamse courant (`ddd_010123214_mpeg21`), 6 Dec 1808 | 6–9 Dec 1808 | Spanish campaign, late Nov 1808 | "eén dikke nevel heerscht" … "nog ongunftigèr toor de inboors" | Ordinary fog in Spain (the Somosierra–Madrid campaign, ~30 Nov 1808). This **predates** the proposed ~4 Dec eruption. Not relevant. Rotterdam djvu.txt could not be fetched. |
| N4 | Ommelander courant (`ddd_010216288_mpeg21`) | 17 Feb 1809 | Gorinchem, early Feb 1809 | "Vele geloofwaardige lieden meenen des nachts," "tusfchen een en twee uren, een fchok van aardbeving" "gevoeld te hebben." Also floods: "Waar wy onze oogen wenden, is water." | Ice-dam and dyke-breach floods of Feb 1809 on the Rhine and Waal. The "shock" is almost certainly ice or dyke failure. **Not relevant.** The same story is in Leeuwarder 14 Feb, Vriesche 15 Feb and Rotterdamse 9 Feb 1809 ("dat er eene Aardbeving plaats had"). |
| N5 | Utrechtsche courant (`ddd_010813555_mpeg21`) 3 Mar 1809; Koninklijke courant (`ddd_010239704_mpeg21`) 4 Mar 1809; Vriesche courant (`ddd_010180422_mpeg21`) 8 Mar 1809 | 3–8 Mar 1809 | Naples, "Sprokkelmaand" (Feb) 1809 | "uitbarstingen vam den Vefuvius, die ovlangs, kort: op 'elikaaderen plaats hadden" … a new vent about 15 paces east of the old crater … "de Vulkaan eene zoo groote meenigte feenen heeft uitgebraakt". The summariser read the stronger outburst as 28 Jan; the date is not verified. | Small Vesuvius activity, about Jan–Feb 1809. European, minor, not a sulfate source. |
| N6 | Utrechtsche courant (`ddd_010813588_mpeg21`) | 31 May 1809 | "NAPELS den 16. April" [1809] | "de tegenswoordige uitbarfting van den ZErme [=Etna]" "eene der vreeslykfte is die federt Reuwen plaats gehad heeft" … Calabria "twee à drie vingeren hoog met ftuifasch bedekt" … "boven zynen Crater verheft sich eene Vuaur- Colom" "die 2 à 9 maalen hooger dan de Berg zelve is" | **Etna, Mar–Apr 1809 (GVP: 27 Mar 1809 onward).** Ash fell 2–3 fingers deep on Calabria and the eruption column stood several times the mountain's height. A European eruption in spring 1809. Any European haze or twilight reports from Apr–May 1809 must consider Etna as the source. |
| N7 | Vriesche courant (`ddd_010180244_mpeg21`), 10 Sep 1808; Rotterdamse (`ddd_010123174_mpeg21`), 6 Sep 1808 | Sep 1808 | Naples, "den 16 dezer" (Aug 1808) | "Pmerklyk is het, dat wy fterke uitbarftingen uit de Vefuvius hebben gehoord;" "de nok, welke uit den Crater kwam, was zo dik, dat de lucht er donker van was;" | Vesuvius, Aug 1808. Minor, and before the window. |
| N8 | Amsterdamse courant (`ddd_010720480_mpeg21`), 9 Sep 1809; Koninklijke courant 28 Sep 1809; Vriesche 2 Oct 1809 | Sep–Oct 1809 | Naples, early Sep 1809 | "Gisteren avond zyn wy getuigen geweest van eene uitbarfting van des Veluvius" | Vesuvius, Sep 1809. Minor. |
| N9 | Ommelander courant (`ddd_010216387_mpeg21`) | 21 Dec 1810 | Naples, late 1810 | "De lava, welke de Vefurius by de laate uitbarfting heeft uitgeworpen, begins reeds te verkoelen" | Vesuvius, autumn 1810. Minor. |
| N10 | Haagsche courant (`ddd_010249848_mpeg21`), 24 Sep 1810; Leydse 24 Sep 1810 | Sep 1810 | Almeida, Aug 1810 | "Het was de uitbarfting vaa eenen vulkaan." | **Simile only**: the explosion of the powder magazine at the siege of Almeida (26 Aug 1810). Not volcanic. |
| N11 | Vriesche courant (`ddd_010180460_mpeg21`) | 5 Jun 1809 | Turin, 12 May; event 30 Apr 1809 at Cavour (Pinerolo) | "eene geweldige Aardbeving heeft ge- Veeld" | Piedmont earthquake. Tectonic. |
| N12 | Groninger courant (`ddd_010170678_mpeg21`), 18 Aug 1809; Koninklijke courant (`ddd_010239837_mpeg21`), 10 Aug 1809 | Aug 1809 | Gulf of Spezia, 9 Jul 1809, and elsewhere in Italy | "by eene ftille Zee ên heldere Lucht, een zeer buitengewoon verfchynfel" (sudden rise of the sea), "eene aardbeving ter zee" | A Mediterranean seiche or meteotsunami ("marrobbio"). Not volcanic. |
| N13 | Alexandria Daily Gazette (`per_alexandria-gazette-packet_…_1809-02-25_9_2420`) and Kentucky Gazette (`xt7h9w08x041`), 21 Mar 1809 | Feb–Mar 1809 | Azores (Fayal / São Jorge), May 1808 | "NEW VOLCANO. … A letter from J. B. Dabney, esq." … "the large volcano that had lain dormant for nine day[s] burst forth" | São Jorge, May–Jun 1808 (known, VEI 2–3). Published ~9 months after the event. Before the window. |
| N14 | Haagsche courant (`ddd_010249896_mpeg21`) | 17 Dec 1810 | Travancore letter of 4 Apr [1810]; West Indies | Earthquake at Travancore that "collapsed buildings" (summariser); West Indies text is a description of extinct volcanoes only | Off-window. Indian earthquake of Apr 1810; worth noting for the Indian-Ocean strand. |
| N15 | Vriesche courant (`ddd_010180626_mpeg21`) 29 Jun 1810; Amboina items Oct 1810 | 1810 | Batavia letters; Amboina taken 19 Feb 1810 | "Brieven van Batavia roemen de ftandvastigkid … Daendels"; Amboina news printed 5–19 Oct 1810 | **News lag Batavia → NL of about 4–8 months, routed via English papers.** No natural-event content. |

**Searched for and not found in Dec 1808 – Jun 1809 issues:** any red or pale sun, dry fog ("drooge nevel", "heirook"), haze ("damp" in a sky sense), "roode lucht", "roode zon", unusual twilight, or a "Noorderlicht" report. The only "nevel" hits in this window are battle fog. Given how weak the fts recall is (§1), this is **not proof of absence**. A page-image read of selected issues from Dec 1808 – Feb 1809 on Delpher is still the proper test. Best candidates: *Oprechte Haarlemse Courant*, *Leydse courant*, *Amsterdamse courant*.

---

## 3. Lamongan / Java list, NTNI vols 80–82 (1920–22), p. 327: "1808, 5 Dec." or "5 Dec. 1810"?

- Item: IA `mobot31753002490180` (*Natuurkundig Tijdschrift voor Nederlandsch-Indië*, vols 80–82, 1920–22). https://archive.org/details/mobot31753002490180 . The in-book search URL that worked: `https://ia601507.us.archive.org/fulltext/inside.php?item_id=mobot31753002490180&doc=mobot31753002490180&path=/10/items/mobot31753002490180&q=Soerabaja`
- **Full paragraph (OCR), consecutive fragments:**
  1. "1806. Loemadjang. Uitbarsting van de Lamongan. 1808, 5 Dec. 1810, 24/3 1814, 10/3"
  2. "1815 Rembang, Solo, Banjoewangi, 22/11 1815 Soerabaja, 23/1 '17 Idjen, 1817 aardbeving Jogya,"
  3. "8/11 '17 heel Java, uitb. Lamongan, 25/9 '21 Djapara, Oct. '22 Galoenggoeng, Merapi."
  4. "Mei 1824 Kedoe, Oct. 1826 uitb. Pakoewadja (Dijeng). Maart 1830 Liamongan. 15/12 1830 Bromo."
  5. "Jan. 1833 Batavia. 1834 sterk in West Java. Jan. 1840 Java. 1842, 1845."
- **Word boxes on p. 327 (page 1786 × 2868 px):**
  - "Loemadjang": l 305, t 2160, at the left margin.
  - "1808": l 1494–r 1620, t 2156, at the **right end of the same line**.
  - "Dec.": l 308–415, t 2230, at the **start of the next line**.
  - "1810": l 465–591, t 2233, on the same line as "Dec.".
  - "Soerabaja": l 944, t 2298, one line lower.
  - So the "5" sits at the end of line 1, after "1808,", and "Dec. 1810," opens line 2. This is justified running text, so the line break settles nothing.
- **Reading.** From "1815" onward, every item is in date-then-year order. The paragraph appears to be a terse list of dated earthquakes or events (it includes "1817 aardbeving Jogya" and "1834 sterk in West Java"). Read in that format, the entries are "5 Dec. 1810", "24/3 1814" and "10/3 1815 Rembang, Solo, Banjoewangi". The last could be a misprint or OCR error for 10/4 1815, the Tambora detonations heard across Java, which would support date-before-year. **"1808" is then a bare year** (as are "1842, 1845" at the end). The alternative year-first reading ("1808, 5 Dec.", "1810, 24/3", "1814, 10/3", "1815 Rembang…") fits only the very first item.
- **Conclusion.** The more probable reading is "1808" (undated) followed by "5 Dec. 1810". Do not treat p. 327 as independent support for a Lamongan event on 5 Dec 1808. The page lies in or near the article "Oud-Javaansche gegevens omtrent de vulkanologie van Java" (heading found on p. 157, list on p. 327). Its compiler and sources were not identified. **Open item:** view the page image (IA BookReader page 327) to check punctuation and the "10/3" digit. Not done: page images could not be retrieved here.
- **Cross-check attempted.** The *Bataviasche koloniale courant* of 14 Dec 1810 (`ddd_010522000_mpeg21`) and the following issue (`ddd_010522001_mpeg21`, with a Samarang item of 13 Dec 1810) contain **no earthquake or eruption report**. This weakly argues against a notable event on 5 Dec 1810 in central Java, but these issues are not exhaustive.

---

## 4. Bosch 1858: "Uitbarstingen der vulkanen Idjin en Raun (Banjoewangi)"

- Found on IA as **`tijdschriftvoor38unkngoog`** (*Tijdschrift voor Indische Taal-, Land- en Volkenkunde*, Google scan of the University of Michigan copy; IA metadata says "1853", which is wrong). https://archive.org/details/tijdschriftvoor38unkngoog
  - The table of contents (p. 11) reads "Uitbarstingen der vulkanen Idjin en Raun (Banjoewangi), door C. J. Bosch."
  - The volume contains 1858 material (for example "Riouw, 6 April 1858. H. von Dewall"), which is consistent with **Deel VII (1858)**.
  - The article runs **pp. 283–304 in IA pagination**. Sapper cites "p. 265 ff."; the difference is unresolved (IA page labels or a different issue).
  - In-book search URL: `https://ia601907.us.archive.org/fulltext/inside.php?item_id=tijdschriftvoor38unkngoog&doc=tijdschriftvoor38unkngoog&path=/34/items/tijdschriftvoor38unkngoog&q=uitbarsting`
- **Chronology of Raung and Ijen in the article (OCR):**
  - p. 297: "Eene vroegere uitbarsting van den Idjin moet hebben plaats gehad in het jaar 1796 (2)." Also: "het schijnt dat de eruptie van 1817 vooreerst zijne krachten heeft uitgeput". The first eruption mentioned dates from the time of "pangeran Tawangaloen".
  - p. 298: "Van eene tweede uitbarsting wordt gesproken gedurende de regering van pangeran Danoeredjo …"
  - p. 299: "Ook toen (1720-1750) zonden groote overstroomingen hebben plaats gehad, zoude veel asch zijn gevallen …"
  - p. 299: "Eene derde uitbarsting moet men hebben waargenomen, gedurende het bestuur van dit gewest onder den kommandaut C. de Harris (1787-1799); de gewone verschijnselen deden zich voor, namelijk: het gedonder van den berg en een sterke aschregen, ten gevolge waarvan eene groote ziekte onder het vee ontstond en vele beesten omkwamen."
  - **p. 299: "De vierde uitbarsting had plaats toen de heer J. C. von Wikkerman (1) als kommandant civiel en militair zich hier bevond (van 1800-1808) doch was van weinig beteekenis. De vijfde maal, dat de Raun sterk gewerkt heeft, moet zijn waargenomen onder het bestuur van den resident A. Macleod (1815 & 1816)."**
  - Footnote (1), p. 299: "Deze heer von Wikkerman heeft den Idjin met den heer Leschenault bestegen." This was in 1805 (p. 297: "in 1805 den Idjin beklom").
  - Footnote (2), p. 299: Crawfurd's chronological table, "1586. Aan het oostelijk einde van Java heeft eene hevige uitbarsting plaats …"
  - p. 300: "In 1812 moet ook eene kleine eruptie van den Raun hebben plaats gehad, die veel asch uitwierp, terwijl men aardschuddingen waarnam en tot 1814 geluiden, uit dezen berg komende, werden gehoord, die veel gelijkenis hadden aan die van donder (1)."
- **Stöhr 1874** (*Abh. Senckenb. Naturf. Ges.* 9; IA `mobot31753003649065`, p. 121) repeats Bosch: "Dann ein kleiner, weniger bedeutend, als van Wilker Commandant war, um 1800 bis 1808. 1812 wieder eine kleine Eruption mit viel Aschenregen und Erderschütterungen, und 1815/16 eine grössere …". Stöhr calls Bosch's article the one "welcher die amtlichen Daten erschöpfend zusammengestellt". Stöhr adds nothing to the dating.
- **Implications.**
  - The Wikkerman-era Raung eruption is **undated (1800–1808) and minor**, and Bosch gives no month or year. It therefore cannot be tied to Dec 1808.
  - Wikkerman's term may have ended in 1808, which is when Daendels reorganised the government. Even so, "until 1808" is the end of his term, not the date of the eruption.
  - A Raung event in 1812 with much ash, tremors and noises until 1814 is a better-dated East Java event. It might feed later confusion such as "seven years ago" counted back from 1815, but it lies outside the 1808–09 window.
  - **No dated 1806–1810 eruption of Ijen or Raung.**
  - The archival originals would be the Banyuwangi residency reports. Bosch says he used local "verhalen" (accounts) and official data. The relevant files would be Arsip Nasional RI, Banyuwangi / Oosthoek residency archives; not checked.

---

## 5. Search log

| # | Tool | Query / filter | Coverage | Result |
|---|---|---|---|---|
| 1 | IA fts | vulkaan, year 1808–1811 | all IA | 18 hits. Vesuvius (Feb–Mar 1809 papers), Almeida simile, books |
| 2 | IA fts | aardbeving, 1808–1810 | all IA | 134 hits (57 seen). European quakes; Cape 4 Dec 1809 (BKC) |
| 3 | IA fts | aardbeving, 1809 only (gte 1809, lt 1810) | all IA | 29 hits. Alps avalanches; Feb 1809 floods; Cavour 30 Apr 1809; Lisbon Dec 1809; Spezia seiche |
| 4 | IA fts | "drooge nevel", 1807–1811 | all IA | 0 |
| 5 | IA fts | nevel zon, 1808–1809 | all IA | 47 hits, all fog in battles or literature |
| 6 | IA fts | "dikke nevel", 1808–1809 | all IA | 4 hits, war fog (Spain Nov 1808) |
| 7 | IA fts | Barometer Thermometer Wind, 1808–1809 | all IA | 6 hits, 0 newspapers. **No printed weather registers found** |
| 8 | IA fts | zon rood nevel | all IA | 1 ddd hit, irrelevant |
| 9 | IA fts | verfchynfel lucht; verfchynfel (1809, newspapers) | IA / newspapers | Nice and Florence snow (Dec 1808); Spezia seiche (Jul 1809) |
| 10 | IA fts | Batavia Daendels, 1809–1810 | all IA | BKC 1810 admin. notices; Vriesche 29 Jun 1810 |
| 11 | IA fts | uitbarfting, 1808–1810 | all IA | 41 ddd hits. Vesuvius ×3, Etna (Utrechtsche 31 May 1809), rest war or other |
| 12 | IA fts | afch OR asch regen; afch Berg | all IA | 0 / noise |
| 13 | IA fts | vuurberg, 1808–1811 | all IA | 25 hits. Vesuvius, Hecla prize-essay topic, West Indies description |
| 14 | IA fts | Manilla, 1809–1811 | all IA → newspapers | Ship and trade news only |
| 15 | IA fts | volcano, 1809, newspapers | newspapers | 7 hits. Azores "NEW VOLCANO" (Feb–Mar 1809); rest metaphor |
| 16 | IA fts | aardbeeving, 1808–1811, newspapers | newspapers | 10 hits, all European (Moor/Hungary 1810, Crete 1810, Piedmont 1808) |
| 17 | IA fts | Amboina, 1808–1811, newspapers | newspapers | 18 hits; fall of Amboina 19 Feb 1810 reported Oct 1810 (lag) |
| 18 | IA fts | Java, 1809, newspapers | newspapers | 19 hits; estate notices and US coffee ads only. **No Java news in NL papers in 1809** |
| 19 | IA fts | Goenong, 1808–1811 | newspapers | 2 hits (garden for sale, BKC) |
| 20 | IA fts | aardbeving, 1811–1812, newspapers | newspapers | 36 hits; no Java/Indies items; Caracas 1812, Guadeloupe 1812, Portsmouth NH 1810/11 |
| 21 | IA fts | Noorderlicht; "roode lucht"; "roode zon"; heirook; damp lucht zon; haze sun; smoky (1808–1809) | various | 0 or irrelevant |
| 22 | IA fts | nevel, 1808 and 1809 separately, newspapers | newspapers | 16 and 12 hits, all battle fog |
| 23 | IA fts | Bogota, 1809–1810, newspapers | newspapers | 1 irrelevant |
| 24 | IA fts | aardschudding / aardfchudding, 1808–1811 | newspapers | 0 |
| 25 | IA inside | `mobot31753002490180`: Loemadjang, Rembang, Lamongan, 1808, Dec, 1810, Soerabaja | NTNI 80–82 | p. 327 paragraph and word boxes (§3) |
| 26 | IA fts | "Idjen en Raun" | all IA | Stöhr 1874 (Senckenberg) and Sapper |
| 27 | IA inside | `mobot31753003649065`: Wikkerman (0), Bosch, years, "bis 1808", Raun Ausbruch | Stöhr 1874 | p. 121 chronology |
| 28 | IA fts | Wikkerman Raun | all IA | **Found the Bosch article in `tijdschriftvoor38unkngoog`** |
| 29 | IA inside | `tijdschriftvoor38unkngoog`: Wikkerman, Raun, commandant (0), asch, "vrij wat asch", "zoude veel asch", Harris, uitbarsting, 1858, years, eruptie | TITLV [7] | §4 (one HTTP 429, cleared on retry) |
| 30 | djvu.txt | BKC 14 Dec 1810 and next issue | BKC | No natural events |
| 31 | djvu.txt | Rotterdamse 6 Dec 1808; Oprechte Haarlemse 14 Jan 1809 | — | **Fetch failed** (client error) |

---

## 6. Source register

| Source / edition | Region / lang | Type | Covers 1808–09? | Digitized (URL) | Opened from here? |
|---|---|---|---|---|---|
| IA mirror of Delpher newspapers (ddd_*_mpeg21), fts with year and collection filters | NL / Dutch | newspaper corpus | yes | https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=aardbeeving | yes (OCR snippets; recall low) |
| Vriesche courant 27 Jan 1809 | NL | newspaper | yes | https://archive.org/details/ddd_010180406_mpeg21 | yes (djvu.txt) |
| Utrechtsche courant 11 Jan 1809 | NL | newspaper | yes | https://archive.org/details/ddd_010813658_mpeg21 | yes (djvu.txt) |
| Ommelander courant 9 Dec 1808 | NL | newspaper | yes | https://archive.org/details/ddd_010216234_mpeg21 | yes (djvu.txt, garbled) |
| Rotterdamse courant 6 Dec 1808 | NL | newspaper | yes | https://archive.org/details/ddd_010123214_mpeg21 | snippet only (djvu fetch failed) |
| Oprechte Haarlemse courant 14 Jan 1809 | NL | newspaper | yes | https://archive.org/details/ddd_010077524_mpeg21 | snippet only (djvu fetch failed) |
| Ommelander courant 17 Feb 1809 | NL | newspaper | yes | https://archive.org/details/ddd_010216288_mpeg21 | yes |
| Utrechtsche courant 3 Mar 1809 (Vesuvius) | NL | newspaper | yes | https://archive.org/details/ddd_010813555_mpeg21 | yes |
| Koninklijke courant 4 Mar 1809 (Vesuvius) | NL | newspaper | yes | https://archive.org/details/ddd_010239704_mpeg21 | yes |
| Utrechtsche courant 31 May 1809 (Etna) | NL | newspaper | yes | https://archive.org/details/ddd_010813588_mpeg21 | yes |
| Vriesche courant 10 Sep 1808 (Vesuvius) | NL | newspaper | 1808 | https://archive.org/details/ddd_010180244_mpeg21 | yes |
| Vriesche courant 5 Jun 1809 (Cavour quake) | NL | newspaper | yes | https://archive.org/details/ddd_010180460_mpeg21 | yes |
| Haagsche courant 24 Sep 1810 (Almeida) | NL | newspaper | 1810 | https://archive.org/details/ddd_010249848_mpeg21 | yes |
| Haagsche courant 17 Dec 1810 (Travancore quake) | NL | newspaper | 1810 | https://archive.org/details/ddd_010249896_mpeg21 | yes |
| Groninger courant 18 Aug 1809 (Spezia sea phenomenon) | NL | newspaper | yes | https://archive.org/details/ddd_010170678_mpeg21 | snippet only |
| Bataviasche koloniale courant 14 Dec 1810 | Java / NL | newspaper | 1810 | https://archive.org/details/ddd_010522000_mpeg21 | yes |
| Bataviasche koloniale courant, Dec 1810 issue (Samarang 13 Dec) | Java / NL | newspaper | 1810 | https://archive.org/details/ddd_010522001_mpeg21 | yes |
| Bataviasche koloniale courant 16 Nov 1810 (Cape quake 4 Dec 1809) | Java / NL | newspaper | reprint | https://archive.org/details/ddd_010521996_mpeg21 | snippet (pass 3 read it) |
| Alexandria Daily Gazette 25 Feb 1809 ("NEW VOLCANO", Azores) | US / EN | newspaper | yes | https://archive.org/details/per_alexandria-gazette-packet_alexandria-daily-gazette-commercial-politica_1809-02-25_9_2420 | snippet only |
| Kentucky Gazette 21 Mar 1809 (same) | US / EN | newspaper | yes | https://archive.org/details/xt7h9w08x041 | snippet only |
| NTNI vols 80–82 (1920–22), p. 327 Java event list | NL | journal | retrospective | https://archive.org/details/mobot31753002490180 | yes (in-book search and word boxes; no image) |
| Bosch, "Uitbarstingen der vulkanen Idjin en Raun", TITLV [Deel 7, 1858] | Java / NL | journal article | retrospective (1800–08 eruption undated) | https://archive.org/details/tijdschriftvoor38unkngoog | yes (in-book search) |
| Stöhr 1874, *Abh. Senckenb. Naturf. Ges.* 9 (Idjen–Raun) | DE | monograph | retrospective | https://archive.org/details/mobot31753003649065 | yes (in-book search) |
| Sapper 1917, *Katalog der geschichtlichen Vulkanausbrüche* | DE | catalogue | retrospective | https://archive.org/details/KatalogDerGeschichtlichenVulkanausbrueche | yes (fts snippet; pass 3) |
| Delpher (original newspaper page images) | NL | newspaper portal | yes | https://www.delpher.nl/nl/kranten | blocked (not tried this round; blocked in earlier passes) |
| Batavia *Vendu-Nieuws* 1808–1809 | Java / NL | newspaper | yes | no URL found | no IA copy (pass 3); Delpher or KITLV holdings unverified |
| Banyuwangi residency reports (source of Bosch) | Java / NL | archive | possibly | no URL found | not tried (ANRI) |

---

## 7. Open items and recommendations for a human

1. **NTNI p. 327 page image.** Open https://archive.org/details/mobot31753002490180 at page 327. Check whether "1808," is followed by "5 Dec." with a separator, and whether "10/3 1815" is actually "10/4 1815".
2. **Delpher page-image reading for Dec 1808 – Feb 1809.** Read the *Oprechte Haarlemse Courant*, *Leydse courant* and *Amsterdamse courant*. Look for weather or sky items ("weêr", "lucht", "zon", "nevel", "mist") and for any letters from the Cape, Suriname or Curaçao mentioning haze. The IA OCR is too degraded for a confident negative.
3. **Bosch's sources.** Read the whole article (IA `tijdschriftvoor38unkngoog`, pp. 283–304) on screen, especially footnote (1) on p. 300 for the 1812 eruption, to see whether Bosch cites dated official letters.
