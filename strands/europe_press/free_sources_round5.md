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

# Round 5: freely available 1808–09 sources not checked before (16 Oct 2026)

Thread: "Another pass for free 1808–09 sources". Four strands were searched from Claude's cloud container (WebFetch only, OCR/text only, no page images). Every quotation below is **OCR only**.

## Summary of results
- **No source read this round reports the veil** (dim/silvery sun, red twilights, dry fog, haze) anywhere for Dec 1808 – May 1809. All negatives are weak to moderate: keyword searches through OCR snippets, not page-by-page reading.
- **German-language press (Deutsches Zeitungsportal, ~25 searches, ~20 pages read):** Hamburg, Altona, Berlin, Augsburg, Munich, Stuttgart/Tübingen, Karlsruhe, Innsbruck, Köln. Zero hits for Höhenrauch/Heerrauch, "Sonne bleich/roth", trockener Nebel, Lufterscheinung. Volcano news only Vesuvius (~28 Jan 1809) and Etna. Context: severe N/E European winter 1808/09; Zagreb quake 9 Dec 1808; Västergötland quake 15 Jan 1809; fireball over Bern 29 Dec 1808; Venus–Jupiter conjunction late Jan 1809 reported as a "meteor" (point lights, cannot explain twilights).
- **Salem, Mass. (William Bentley's diary vol. 3):** 8–12 Nov 1808 "great darkness much resembling the Dark day… the sun was very red", hot and dry. A month **before** Bogotá, regional (Martha Ballard in Maine and Leonard Hill in Mass. do not show it), most likely smoke/overcast; recorded so it is not later mistaken for the veil. Bentley has nothing optical Dec 1808 – May 1809. Medical Repository NY winter 1808–9 report: cold, snowy, nothing optical.
- **Giornale italiano (Milan) 1808 – Jun 1809, Moniteur Jul–Dec 1808 + 1799–1814 index, O Telegrafo Portuguez 1809:** nothing; only Etna 1809 (ash on Calabrian coast, ~Apr 1809; a "meteora" blamed on Etna, ~Jun 1809) and the 29 Dec 1808 fireball.
- **Missionary and India sources (Baptist Magazine 1809, Methodist Magazine 1809, Henry Martyn's journal, Mrs Sherwood, Mackintosh, Minto):** nothing.
- **Blocked or unreadable from here:** ANNO (Wiener Zeitung), Finnish digi, Swedish tidningar.kb.se (JS), DIGAR Estonia, Mediestream, Polona, Latvian periodika, Russian papers, Founders Online, Canadiana, Holyoke description file, Trove (Sydney Gazette), BMS Periodical Accounts vol. IV (not online), Correo de Tenerife (Jable/Maresía JS/robots), BNE titles.
- **New working routes for later threads:** DDB newspaper Solr index (no key; query format in strand A §0); MDZ/BSB IIIF full-text search per volume (strand C); Europeana API with demo key (catalogue level only); Norwegian api.nb.no (works, OCR poor).

## Best browser downloads for William (exact URLs in the strand sections)
1. Rigasche Zeitung 1802–1888 plain-text dump (one file, search 1808–09 locally): https://dati.lnb.lv/en/dataset/rigaschezeitung
2. ANNO full-text search, 1808-12-01 to 1809-05-31 (Wiener Zeitung etc.): https://anno.onb.ac.at/anno-suche
3. Correo de Tenerife (La Laguna, weekly, from 25 Aug 1808): https://jable.ulpgc.es/correotenerife (e.g. 15 Dec 1808: http://maresia.bbtk.ull.es/viewer.vm?id=0000017797)
4. Holyoke (Salem) daily weather descriptions: https://crudata.uea.ac.uk/cru/data/holyoke/holyoke.descript.dat
5. Finland: https://digi.kansalliskirjasto.fi/search?query=solen&startDate=1808-12-01&endDate=1809-05-31&formats=NEWSPAPER&orderBy=DATE ; Sweden: https://tidningar.kb.se/search?q=solen&from=1808-12-01&to=1809-05-31
6. Sydney Gazette Dec 1808 – May 1809: https://trove.nla.gov.au/newspaper/title/3
7. Diario de Valencia (daily weather notes) Dec 1808 – 1809 at BNE Hemeroteca Digital, e.g. http://hemerotecadigital.bne.es/details.vm?q=id:0004511785

---

# Strand file: A_nordic_central.md
## Strand A: Nordic, Baltic, Central and Eastern European newspapers (round 5)

Worker notes, 16 Oct 2026. About 70 tool calls. **Every quote below is OCR only.** I saw no page images. WebFetch also passes text through a summariser, which limits quotes to about 125 characters, so quotes are short fragments. Long s is often rendered "ſ".

Before starting I checked the project files (source_register.md, notes/*.md, newspaper_access_guide.md). They name ANNO, Finnish digi, tidningar.kb.se, Mediestream and the Deutsches Zeitungsportal only as access-guide entries. None had been searched for Europe. Mediestream was already recorded as robots-blocked (for the Danish West Indies papers). euro_journals_round3 had already found one "Heerrauch" (Berlin, July 1809) in journals, not newspapers.

### 0. Key method finding: the Deutsches Zeitungsportal Solr API works through WebFetch

The DDB web search page is robots-blocked, but its open Solr index answers without an API key:

`https://api.deutsche-digitale-bibliothek.de/search/index/newspaper-issues/select?q=plainpagefulltext:TERM&fq=publication_date:[1808-12-01T00:00:00Z%20TO%201809-06-01T00:00:00Z]&fl=id,publication_date,paper_title&rows=40`

- Get the full page text with `?q=id:<ID>&fl=paper_title,publication_date,plainpagefulltext`.
- Phrase proximity works (`%22Sonne%20bla%C3%9F%22~8`). So do wildcards (`feuerspeiend*`) and OR/AND groups inside `plainpagefulltext:( … )`.
- Highlighting (`hl=`) returns a server error.
- The WebFetch proxy refuses URLs longer than about 250 characters, so queries must be short.
- The index treats ſ as s ("Sonnenſcheibe" was found by "Sonnenscheibe").
- Papers covered for 1808–09 include: *Staats- und gelehrte Zeitung des Hamburgischen unpartheyischen Correspondenten*, *Hamburgische neue Zeitung*, *Altonaischer Mercurius*, *Allgemeine Zeitung* (Tübingen/Augsburg), *Augsburgische Ordinari Postzeitung*, *Münchener politische Zeitung*, *Baierische National-Zeitung*, *Karlsruher Zeitung*, *Schwäbischer Merkur*, *Berlinische Nachrichten (Spenersche)*, *Innsbrucker Zeitung*, *L'Observateur* (Köln), *Morgenblatt*, *Zeitung für die elegante Welt*, *Allgemeiner Anzeiger der Deutschen*, *Hamburgische Adreß-Comtoir-Nachrichten*, *Riedlinger politische Zeitung* and some intelligence sheets.
- Human issue viewer: `https://www.deutsche-digitale-bibliothek.de/newspaper/item/<ITEM-ID>` (the part of the id before `-FILE_…`/`-ALTO…`). I inferred this URL pattern and did not test it here.

### 1. Sources tried

| Source | Place / language | Covers Dec 1808–spring 1809? | Human URL | Digitised | Readable from here | Result |
|---|---|---|---|---|---|---|
| ANNO (Wiener Zeitung, Pressburger Zeitung etc.) and ANNO-Suche | Vienna / German | yes | https://anno.onb.ac.at/anno-suche ; issue e.g. https://anno.onb.ac.at/cgi-content/anno?aid=wrz&datum=18090111 | yes | **blocked** ("Sicherheitsüberprüfung" bot wall on anno and annoshow text view; search UI is a JS app) | not read |
| digi.kansalliskirjasto.fi (Åbo Tidningar, Finlands Allmänna Tidning) | Turku / Swedish | yes | https://digi.kansalliskirjasto.fi/search?query=solen&startDate=1808-12-01&endDate=1809-05-31&formats=NEWSPAPER&orderBy=DATE | yes | **blocked** (ROBOTS_DISALLOWED) | not read |
| Svenska dagstidningar, tidningar.kb.se (Post- och Inrikes Tidningar etc.) | Stockholm / Swedish | yes | https://tidningar.kb.se/search?q=solen&from=1808-12-01&to=1809-05-31 | yes | **no**: the result list is loaded by JavaScript (the page shell has no hits); guessed API endpoints (`/api/search`, `data.kb.se/search`) returned errors | not read |
| Nasjonalbiblioteket, api.nb.no (Danish-Norwegian papers) | Norway / Dano-Norwegian | yes (only 326 issues for 1809: Christiania Intelligentssedler, Bergens Adressecontoirs Efterretninger, Trondhjems Adressecontoirs-Efterretninger, Christiansands Adresse-Contors Efterretninger, Tiden) | https://www.nb.no/search?mediatype=aviser&fromDate=18081201&toDate=18090531 | yes | **partly**: metadata and hit lists work (`q=TERM%20AND%20year:1809`); `filter=year:` and date filters are ignored; fragments come back as single words only | Fraktur OCR is very weak ("Christiania" occurs in only 40 of 326 issues). "Solen": 1 hit (Tiden 31 Oct 1809). "Himmelen": 4 hits (Trondhjem 3 Jan, 31 Jan, 31 Oct 1809; Bergen 30 Sep 1809), with no context returned. "Vulcan/Taage/Aske/Jordskiælv" OR-query: 0. **Inconclusive.** |
| Mediestream (Danish papers) | Copenhagen / Danish | yes | https://www2.statsbiblioteket.dk/mediestream/avis | yes | already recorded as robots-blocked in project notes; not retried | not read |
| **Deutsches Zeitungsportal (DDB), Solr API** | Germany, Austria (Tyrol), Köln (French) / German | **yes** | https://www.deutsche-digitale-bibliothek.de/newspaper | yes | **yes (OCR full text)** | about 25 searches and 20 pages read: see section 2. **No veil, dry fog, pale sun or red twilight found.** |
| BSB digipress | Munich | yes | https://digipress.digitale-sammlungen.de | yes | not tried separately; its titles (Allgemeine Zeitung, Augsburger Postzeitung, Münchener politische Zeitung etc.) are in the DDB index, provider "Bayerische Staatsbibliothek" | covered via DDB |
| e-newspaperarchives.ch | Switzerland | yes | https://www.e-newspaperarchives.ch/?a=q&txq=Sonne | yes | **no** (CLIENT_ERROR on the Veridian query URL) | not read |
| periodika.lv (Rigasche Zeitung) | Riga / German | yes | https://periodika.lv ; the bulk text corpus is listed at https://dati.lnb.lv/en/dataset/rigaschezeitung (TXT, https://dom.lndb.lv/data/obj/1062448) | yes | not tried (JS viewer); the corpus file is too large for WebFetch and Bash has no internet | not read; **good bulk lead** |
| DIGAR, dea.digar.ee (Revalsche Wöchentliche Nachrichten) | Tallinn / German | probably | https://dea.digar.ee/?a=q&txq=Sonne | yes | **blocked** (ROBOTS_DISALLOWED) | not read |
| Polona / Gazeta Warszawska | Warsaw / Polish | images exist (Polona, e-bUW, WBC Poznań) | https://polona.pl/search/?query=Gazeta_Warszawska_1809 ; https://platforma.bk.pan.pl/en/search_results/470686 | yes (images; OCR uncertain) | not tried beyond a web search (JS apps) | not read |
| Sankt-Peterburgskie / Moskovskie vedomosti 1809 | Russia / Russian | holdings exist (NLR, RGB) | https://rusneb.ru/catalog/000199_000009_004837020_92405/ | partial, images | not tried beyond a web search | not read |
| Europeana API (api2demo key) | pan-European | — | https://www.europeana.eu | — | yes, but the newspaper full-text filters returned 0 (newspapers.eanadev.org: 0 for "Sonne" 1809) | useless as configured |

### 2. What the DDB newspapers say (OCR only)

### 2a. Searches and hit counts (window as stated; pages = page-level hits)

| Query | Window | Hits | Outcome |
|---|---|---|---|
| Vulkan | 1 Oct 1808–31 May 1809 | 37 pages | Read samples: the Vesuvius renewal (Allg. Ztg 20 Feb 1809, Naples, early Feb: on ~28 Jan a lava vent opened on the SE rim, "daß dieser Vulkan nächstens auslöschen" [it had been thought the volcano would soon die out]); mythology (Morgenblatt 13 Dec 1808, "Vulkan vom Hefästos"). No American or Pacific volcano. |
| (Vulkan OR Vulcan) minus Vesuv/Aetna | Nov 1808–Aug 1809 | 22 | The exclusion does not work well (the OCR misspells the names). The hits are the same set. |
| feuerspeiend*/feuerspeyend* | Nov 1808–Aug 1809 | 10 | Berlinische Nachrichten 31 Jan and 7 Feb 1809: an advert for a Berlin panorama show, "Einen Ausbruch des feuerſpeienden Berges Veſuv bei Neapel, bei Nacht" [an eruption of the fire-spewing mountain Vesuvius near Naples, by night]. Noise. |
| Heerrauch OR Höhenrauch OR Haarrauch | Oct 1808–May 1809 | **0** | negative |
| "Nebel trocken"~5 | Nov 1808–May 1809 | **0** | negative |
| "Sonne bleich"~8 | Nov 1808–May 1809 | **0** | negative |
| "Sonne blaß"~8 | Nov 1808–May 1809 | 1 | Hallisches patriotisches Wochenblatt 27 May 1809, a moral tale: "Die letzten Strahlen der untergehenden Sonne zuckten auf seinem blassen Gesichte" [the last rays of the setting sun flickered on his pale face]. Fiction. |
| "Sonne roth"~4, "Himmel roth"~4 | Dec 1808–Apr 1809 | **0, 0** | negative |
| "rothe Himmel"~3 | Nov 1808–May 1809 | 1 | Zeitung f. d. elegante Welt 17 Jan 1809, description of a painting ("Rothe Streifen, die ihn überzogen, verkündigten die nahe Ankunft des Tages" [red streaks across it announced the coming day]). Art criticism. |
| Abendröthe OR Morgenröthe | Oct 1808–May 1809 | 25 | 3 Jan–Feb hits read (Morgenblatt 4 Jan and 3 Feb 1809; Allg. Anzeiger 5 Jan 1809): all poetry or metaphor ("In unſrer Dichtung Abend-Morgenröthe"; "Welche heitere Morgenröthe würde für das Glück des Staats aufſtrahlen?"). The rest are unread. |
| Sonnenscheibe | Dec 1808–Apr 1809 | 1 | Morgenblatt 16 Jan 1809, a battle narrative in serial form ("Als die Sonnenſcheibe uber der Alpe ſich wies"). Literary. |
| "Nebel Sonne"~6 | 5 Dec 1808–15 Mar 1809 | 1 | Zeitung f. d. elegante Welt 17 Feb 1809, an undated Alpine travel account ("Die Sonne ſiegte über den Nebel"). Irrelevant. |
| Nordlicht OR Nordschein | Dec 1808–mid-Apr 1809 | 3 | An anecdote (Voigtländischer Anzeiger 11 Mar 1809) and Siberian aurora as background in a piece on sea luminescence (Morgenblatt 14 Apr 1809). There was no aurora or "red sky" sighting report. |
| Lufterscheinung* OR Himmelserscheinung* | Dec 1808–May 1809 | **0** | negative |
| Meteor OR Feuerkugel | Dec 1808–Apr 1809 | 12 | Read 2. (a) Münchener politische Ztg 20 Jan 1809: a fireball seen in **Bern on 29 Dec [1808], 5–6 a.m.**, NE to SW, "ein feuriges Meteor … Vielleicht fiel dabey wieder ein Aerolith" [a fiery meteor … perhaps another aerolite fell]. A bolide, not a veil. (b) Allgemeine Zeitung 9 Feb 1809: the Venus–Jupiter conjunction in the evening sky, which "das Volk … hielt sie für ein Meteor" [the people took for a meteor]. Weather "very unsettled": spring sunshine in the mornings, autumn storms with rain, warm moonlit evenings. |
| Bimsstein* OR Aschenregen | Dec 1808–Aug 1809 | 7 | Read 2: a wood-stain recipe (Allg. Anzeiger 6 Jan 1809) and a simile ("Trocken, wie ein Bimsſtein", Morgenblatt 29 Mar 1809). Noise. |
| Bogota OR Popayan OR Quito | Dec 1808–Sep 1809 | 2 | Morgenblatt 20 Dec 1808, a review of Humboldt's *Essai politique* (no natural events). The other is 3 Jul 1809, unread. |
| Lima AND Peru | Jan–Sep 1809 | 5 | Not read (mostly Hamburg Adreß-Comtoir-Nachrichten, probably trade or book notices). |
| Erdbeben | Dec 1808–Jun 1809 | 63 | Read 4 Hamburgischer Correspondent pages; see 2b. |

### 2b. Hamburgischer Correspondent: foreign-news pages read (OCR only)

- **28 Jan 1809, p. 2**, Preßburg, 13 Jan: an earthquake at Agram (Zagreb) "am 9ten v. M." (= **9 Dec 1808**), "sehr heftiges Erdbeben … Es stürzten mehrere Schornsteine davon ein" [a very violent earthquake … several chimneys collapsed]. Same page: unusually heavy snow delaying the mails; wolves in the Banat during "the great cold"; Danube and Theiss low the previous summer. No sky remark. *Not volcanic. Note only as an exact-date coincidence: a regional Croatian quake on 9 Dec 1808.*
- **10 Feb 1809, p. 2**, Augsburg, 2 Feb: a popular prophecy that Augsburg would be destroyed by an earthquake in January because of the Jupiter–Venus conjunction; "…Januar kam, und Augsburg steht noch" [… January came, and Augsburg still stands]. Amsterdam, 4 Feb: worst floods for years after a hurricane-force storm. No sky remark.
- **17 Mar 1809, p. 4**: a strong earthquake, "daß die Einwohner aufs Feld flohen" [so that the inhabitants fled to the fields]; the place is garbled ("St. Germans"?). St Petersburg, 1 Mar: cold of 26 degrees on 25 Feb.
- **22 Mar 1809, p. 4**, Stockholm, 9 Mar: an earthquake felt in **Västergötland (Kinnekulle?) on the night of 15 Jan 1809, 1–2 a.m.**, beginning "mit einem unterirdischen Getöse" [with an underground roar], running N to SW, no damage; "Unter fortdauernder Kälte von 27 Grad" [during continuing cold of 27 degrees]; Baltic full of drift ice; a frigate frozen in between Møn and Bornholm all winter.

**Pattern across these pages:** a very severe winter of 1808/09 in Scandinavia, the Baltic, Russia and the Danube lands (−26 to −27 degrees, presumably Réaumur; frozen Baltic). The Dutch floods were storm-driven. No paper describes a dimmed, pale or silvery sun, coloured twilights or dry fog.

### 3. Findings: positive, suggestive, negative

- **Positive veil evidence: none found.** In the German-language press indexed by the DDB (Hamburg, Altona, Berlin, Augsburg, Munich, Stuttgart/Tübingen, Karlsruhe, Innsbruck, Köln), Dec 1808 – May 1809, I found **no report of a pale, dim or silvery sun, red or unusual twilights, Höhenrauch/Heerrauch or dry fog, or an unexplained sky phenomenon**, using the terms listed in 2a. Limits on this negative: Fraktur OCR quality is unknown, only about 20 pages were read, and 22 "Abendröthe/Morgenröthe" and about 59 "Erdbeben" hits remain unread. Hit counts were checked in full; their contents were sampled.
- **No news of an American, Pacific or Asian eruption** reached these papers by Sep 1809 under "Vulkan/Vulcan/feuerspeiend/Bimsstein/Aschenregen". The only volcanic news is the Vesuvius renewal of late Jan 1809 (news from Naples, early Feb) and Etna (spring 1809), which is known.
- **Context (weak, non-diagnostic):** an exceptionally cold winter of 1808/09 in N and E Europe (Stockholm −27°, St Petersburg −26° on 25 Feb 1809, Baltic ice, Danube-land snow and wolves). This is consistent with, but not evidence for, volcanic cooling. Its timing (Dec–Feb) is too early for a forced response to an eruption at the start of Dec 1808.
- **Coincidences to note so they are not re-chased:** the Zagreb earthquake of 9 Dec 1808; the Västergötland earthquake of 15 Jan 1809; the Bern fireball of 29 Dec 1808; the Venus–Jupiter conjunction of late Jan/early Feb 1809, which caused "meteor" and earthquake-prophecy talk in Augsburg. The conjunction is a **possible confounder** for reports of "strange lights" in the evening sky in Jan–Feb 1809. It cannot explain diffuse red twilights such as the Edo report, because it is a pair of point lights, not a coloured sky.
- **Nordic, Baltic, Polish and Russian papers: not read.** Access failed (see table). Norway's 1809 OCR is too poor for keyword work.

### 4. Browser-only leads for William

1. **ANNO, Wiener Zeitung** (has a "Witterung"/meteorological table and foreign news). Open the full-text search https://anno.onb.ac.at/anno-suche with a date range of 1808-12-01 to 1809-05-31 and search for: Höhenrauch, Sonne, Abendröthe, Nebel, Vulkan. Daily issue pattern: https://anno.onb.ac.at/cgi-content/anno?aid=wrz&datum=18090111 (change the date). Also *Pressburger Zeitung* (aid=pre) and *Brünner Zeitung* (aid=bzt).
2. **Finland**: https://digi.kansalliskirjasto.fi/search?query=solen&startDate=1808-12-01&endDate=1809-05-31&formats=NEWSPAPER&orderBy=DATE. Then try: rök, töcken, dimma, aftonrodnad, vulkan, "eldsprutande". Åbo was under Russian occupation from early 1808, so its paper is thin but daily weather notes are possible.
3. **Sweden**: https://tidningar.kb.se/search?q=solen&from=1808-12-01&to=1809-05-31 (Post- och Inrikes Tidningar, Stockholms-Posten). Also search "rök", "dimma", "solen blek", "aftonrodnad", "eldsprutande berg", "jordbäfning" (to find the 15 Jan 1809 Västergötland quake report and its column).
4. **Norway**: the 4 "Himmelen" hits (Trondhjems Adressecontoirs-Efterretninger 3 Jan and 31 Jan 1809, p. 4) are quick to eyeball: https://www.nb.no/items/URN:NBN:no-nb_digavis_trondhjemsborgerligerealskole_null_null_18090131_0_9_1-1 (and the _18090103_ equivalent; URN pattern from the API; not tested in a browser).
5. **Latvia**: download the Rigasche Zeitung text corpus (TXT) from https://dati.lnb.lv/en/dataset/rigaschezeitung (file https://dom.lndb.lv/data/obj/1062448) and grep the 1808–09 part locally for Sonne, Nebel, Höhenrauch, Abendröthe, Vulkan. This is a cheap, complete test.
6. **Estonia**: https://dea.digar.ee (Revalsche Wöchentliche Nachrichten 1808–09), browser search.
7. **Denmark**: Mediestream https://www2.statsbiblioteket.dk/mediestream/avis (Berlingske Tidende, Kiøbenhavns Adresse-Contoirs Efterretninger, Dec 1808–Mar 1809).
8. **DDB remainder**: the human search is https://www.deutsche-digitale-bibliothek.de/search/newspaper?query=Abendr%C3%B6the&fromYear=1808&toYear=1809. The unread "Erdbeben" Hamburg Correspondent pages are 13 Dec 1808, 3 Jun and 27 Jun 1809. The unread Bogota hit is 3 Jul 1809 (id CRWDSPD4BNQ4SLA6IGZZF7XZJ3EHU4HP).
9. **Poland/Russia**: Gazeta Warszawska 1809 (Polona / e-bUW) and Sankt-Peterburgskie vedomosti 1809 (NLR/RNB) are page images. They are low priority unless a specific date is to be checked.

# Strand file: B_north_america.md
## Strand B: North American sources (English and French), round 5

Worker notes, 2026-10-16. Tools: WebFetch/WebSearch only. All quotations come from OCR text (archive.org full-text search snippets or dohistory transcriptions). I saw no page images. The WebFetch summariser caps each verbatim quote at about 125 characters, so some long passages are given as consecutive fragments.

Access note: WebFetch truncates any download at roughly 50–80k characters. Long `_djvu.txt` files (Hale 1833, Bentley vol. 3) therefore cannot be paged with `offset` past that point. The workable method was archive.org's per-item search: `https://{d1}/fulltext/inside.php?item_id=ID&doc=ID&path={dir}&q=TERM`. It returns page ids and snippets. Short item ids only: the long `sim_` id for Hale makes the URL too long, and the proxy rejects it. One archive.org call was rate-limited (429) once and worked again a few minutes later.

### 1. Sources tried

| # | Source | Place / language | Covers Dec 1808–spring 1809? | URL | Digitized | Readable here | Result |
|---|---|---|---|---|---|---|---|
| 1 | Holyoke daily register, CRU UEA, weather-descriptions file `holyoke.descript.dat` | Salem MA; EN | yes (1786–1829) | https://crudata.uea.ac.uk/cru/data/holyoke/holyoke.descript.dat (file name confirmed in https://crudata.uea.ac.uk/cru/data/holyoke/holyoke.readme.txt) | yes | **no**: fetch error; the `.dat` files come back as "binary" | The file name is now known; it was guessed wrongly last round. Not read. |
| 2 | Hale 1833, "A Meteorological Journal 1786–1829" (Holyoke), *Memoirs AAAS* n.s. 1, pp. 107ff | Salem MA; EN | yes | https://archive.org/details/jstor-25057915 (JSTOR Early Journal Content copy, short id) and https://archive.org/details/sim_american-academy-of-arts-and-sciences-boston-memoirs_1833_1 | yes | partly: fetch truncation stops at about 1790 | Tables use F/C/R/H/S codes plus a sunset column. 1808–09 not reached. |
| 3 | **William Bentley, *Diary* vol. 3 (1803–1810), Salem MA, publ. 1905–14** | Salem MA; EN | **yes** | https://archive.org/details/diaryofwilliambe03bent | yes | **yes** (keyword search, page ids 440–500) | **Dark red-sun episode 8–12 Nov 1808. Nothing for Dec 1808–May 1809.** See §2. |
| 4 | *Medical Repository* (NY), Nov 1808–Jan 1809 issue (vol. 12): Ricketson, "Observations on the Weather and Diseases, in the Winter of 1808-9, in the City of New-York" | New York; EN | yes (Dec 1808–winter) | https://archive.org/details/sim_medical-repository_november-1808-january-1809_6 (p. 73 of scan) | yes | yes (snippets) | Cold, snowy winter with few rains and little south wind; colds and catarrh. **No optical remarks.** |
| 5 | *Medical Repository* Feb–Apr 1809 issue (end of vol. 12) | NY, Demerara, etc.; EN | partly | https://archive.org/details/sim_medical-repository_february-april-1809_6 | yes | yes | "Hazy" entries are in Arnell's table for June–Oct 1808, outside the window. "sun" hits are irrelevant. Nothing for the window. |
| 6 | *Medical Repository* May–Jul 1809 issue (vol. 13 no. 1) | US; EN | partly | https://archive.org/details/sim_medical-repository_may-july-1809_1 | yes | yes | "winter" and "atmosphere" hits are a naval surgeon's New England station and miasma theory. Nothing optical. |
| 7 | Leonard Hill, *Meteorological and Chronological Register* (East Bridgewater MA, daily from 1806; publ. Plymouth 1869) | E. Bridgewater MA, about 35 km S of Boston; EN | **yes** (pp. 23–34 of scan = 1808–1809) | https://archive.org/details/meteorologicalch00hill | yes | yes (search plus a partial text read) | No "red", "smoky", "hazy" or "dark" in the 1808–09 pages, except "Dark, with showers" on p. 24, an earlier 1808 month. Hill uses "sun red" often in later years (pp. 43–392). See §2. |
| 8 | Martha Ballard diary (Hallowell, Maine), dohistory transcription | Maine; EN | yes (to 1812) | https://dohistory.org/diary/1808/11/18081102_print.html ; https://dohistory.org/diary/1808/11/18081112_print.html ; https://dohistory.org/diary/1808/12/18081203_print.html | yes | yes | 2–16 Nov and 3–10 Dec 1808 read: terse weather words only, mostly "Clear", with "Thunder at night" on 9 Nov. No darkness or red sun. |
| 9 | Thomas Robbins *Diary* vol. 1 (Connecticut, 1796–1825; publ. 1886) | CT; EN | yes (1808–09 ≈ page ids 390–440) | https://archive.org/details/diaryofthomasrob01robb | yes | yes (search) | No "dark", "sun" or "smoky" hits in the 1808/09 pages ("smoky" only on p. 239 and p. 1037). Nothing found. |
| 10 | Isaiah Thomas *Diary* 1805–1828 (Worcester MA; AAS Trans. 9) | MA; EN | **no** | https://archive.org/details/diaryofisaiahtho09hillrich | yes | yes | The editor states there are **no entries for 1808**. |
| 11 | *Monthly Anthology and Boston Review*, Feb 1809 issue | Boston; EN | yes | https://archive.org/details/sim_monthly-anthology-and-boston-review_1809-02_6_2 | yes | yes | No "weather" hits and no meteorological journal. Nothing. |
| 12 | Founders Online search (Jefferson, Madison, Adams) | US; EN | yes | https://founders.archives.gov/?q=… | yes | **blocked** (robots) | Not read. Web-search proxies found nothing relevant. |
| 13 | Jefferson Weather & Climate Records (Jefferson's weather memorandum book, transcribed) | Washington/Monticello; EN | probably yes (record runs 1776–1826 "intermittently") | https://jefferson-weather-records.org (described at https://jeffersonpapers.princeton.edu/welcome/the-jefferson-weather-and-climate-records/) | yes | **no** (fetch error) | Browser lead. |
| 14 | Canadiana.ca (Quebec Gazette, Halifax papers) | Canada; EN/FR | yes | https://www.canadiana.ca/search?q=Quebec+Gazette&df=1809&dt=1809 | yes | **blocked** (robots) | Not read. |
| 15 | BAnQ numérique (Gazette de Québec / Quebec Gazette) | Quebec; FR/EN | probably | https://numerique.banq.qc.ca/collections/revues-journaux-quebecois-archives | yes | detail pages fetch with OCR; search did not | Web search returned only 1909 *Gazette officielle* records. No 1809 issue found. |
| 16 | *Moniteur de la Louisiane* / *Louisiana Courier* 1808–09 | New Orleans; FR/EN | ? | https://liblegacy.lsu.edu/sites/all/files/sc/lnp/chronindex.pdf (LSU holdings index) | no open scans found | — | No open digitization located. Probably microfilm or Readex. |
| 17 | archive.org full-text search: "sun was very red" 1808; "smoky" "sun" 1809 January; "sun" "singular appearance" 1809; "dark day" November 1808 smoke | various | — | https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=… | — | yes | Turned up Bentley vol. 3 and Hill's register (above) and Elizabeth Drinker's diary, which is irrelevant because she died in Nov 1807. No 1808–09 sky reports otherwise. |
| 18 | Web search: "uncommon/remarkable darkness" Nov 1808 New England | — | — | — | — | — | Nothing corroborating Bentley's Nov 1808 darkness. |

### 2. What the sources actually say

### William Bentley, Diary vol. 3 (Salem MA). OCR only, archive.org item diaryofwilliambe03bent

Page ids are scan leaves. Dating: leaf 453 begins "November 1 [1808]". Leaf 455 reports "The votes of Yesterday in this District are announced" (the Massachusetts congressional election was Monday 7 Nov 1808). Leaf 465 has "18. Sunday" (18 Dec 1808 was a Sunday). Leaf 467 begins "January 1, 1809". So the leaf-456 entries "10." and "12." are **10 and 12 November 1808**. "Tuesday" there is 8 Nov 1808; I checked the weekday by calendar calculation.

- **Leaf 456, entry 10 [Nov 1808]:** "The thunder & lightning of Tuesday was accompanied with great darkness much resembling the Dark day & the appearances in the N. W. were similar. The shower fell perpendicularly without any appearance of a rising cloud & the rain & thunder lasted not one quarter of an hour. Yesterday, almost the whole day, the sun was very red & for a few moments seemed to break out, but the weather continued dark & is in that state till the present moment."
- **Leaf 456, entry 12 [Nov 1808]:** "The weather for the past week has been uniformly dark with heat at times & with little moisture of the Atmosphere. Such has been the weather since Tuesday when the weather began to assume the appearance so memorable on the dark day of 1780."
- Searches of leaves 440–500 (Nov 1808 – mid-1809) for sun, red, dark, hazy (0 hits in the whole volume), smoke, sky, fog, Aurora, Volcano (0 hits in the volume), earthquake, fires and atmosphere returned **nothing else relevant**. The other "sun" hits in range are leaf 480, a 1809 entry: "The wind was S. W. at night but cloudy at sun rise", and leaf 505 (May 1809, summer heat). Weather entries for Dec 1808 – May 1809 concern storms, a "backward" cold spring (leaf 494, May 1809: "Such uniformly backward weather is uncommon in our climate") and wet weather with late vegetation (leaf 496). There is **no red twilight, dimmed sun or haze in Dec 1808 – May 1809**.

### Ricketson, NY winter 1808–9. *Medical Repository* Nov 1808–Jan 1809 issue, scan p. 73. OCR only
"Month (December) began pretty cold, and continued so nearly throughout, though not without some intervals of moderate, pleasant weather. Early in the next month, the cold increased…" / "We have had but few rains this winter, and very little thawing or open weather of long continuance … the season resembled, both in steady cold and snow, the winters of former, more than those of latter years. There was very little southerly wind during the whole winter." The rest concerns catarrh, scarlet fever and smallpox. Nothing optical.

### Leonard Hill, East Bridgewater register. OCR only
The 1808 pages are scan pp. 23–28 and the 1809 pages pp. 29–34. A text read was too garbled for day-by-day transcription. It gave the November 1808 summary as "Month wet" and the December 1808 entries as rain, snow and a thaw. It also returned a January 1809 note, "Coldest January for ten years"; this is a summariser report and I have not verified it. Keyword search found no "red", "smoky" or "hazy" on pp. 20–40. The only "dark" there is p. 24 ("Rain. Dark, with showers…"), an earlier 1808 month. Hill uses "sun red" or "red sun" often from p. 43 on, so a red sun was something he did write down. Its absence on 8–12 Nov 1808 and in the winter of 1808–09 is mild negative evidence. The OCR is poor, so a check against the page images is advisable.

### Martha Ballard, Hallowell ME. dohistory transcription
- 8 Nov 1808: "Clear part of the day." 9 Nov: "Clear part of ye day … Thunder at night." 10 Nov: "Clear part of ye day, raind at night." 11 Nov: "Clear." 12–13 Nov: "Cloudy." 14–15 Nov: rain and snow.
- 3–10 Dec 1808: snow and rain on 3–4 Dec, then "Clear" on most days. No darkness or red sun. Her entries are too terse to rule out optical effects.

### 3. Findings and how well they are verified

1. **Suggestive but probably unrelated: Salem MA, 8–12 Nov 1808.** Bentley describes a week of "uniformly dark" and dry weather. On about 9 Nov the sun was "very red" almost all day, and he compares the scene twice to the 1780 New England Dark Day, which was caused by wildfire smoke.
   - Verification: the OCR text was read in snippets of the same page and is internally consistent. The date is inferred from the diary's sequence and is solid to about ±1 day. I did not view the page image.
   - This is about one month **before** the Bogotá onset (~11 Dec 1808), and it is regional. The heat, dryness and Dark-Day analogy point to **wildfire smoke** (autumn burning in Maine, New Hampshire or Canada) or a thick storm overcast, not a stratospheric veil.
   - Ballard in Maine ("Clear part of the day", thunder on 9 Nov) and Hill in East Bridgewater (no "dark" or "red") do not corroborate it. Treat it as a nonvolcanic regional event. It is worth recording so it is not mistaken later for an early sighting of the veil.
2. **Not found:** no North American source read here reports a dim or silvery sun, red twilights, a "dry fog" or haze between Dec 1808 and May 1809. That covers Bentley (Salem), Ricketson (New York), Hill (E. Bridgewater), Ballard (Maine, sampled), Robbins (Connecticut) and the *Monthly Anthology*. This is weak negative evidence:
   - Bentley is the only observer here attentive to sky phenomena. He did record the November redness, so his silence in Dec–Feb counts for something.
   - A thin veil like the one seen in Bogotá may simply not stand out to a mid-latitude winter observer under frequent overcast.
3. No volcano, eruption or earthquake news from South America or the Caribbean appears in Bentley for the window.

### 4. Leads for someone with a browser

- **Holyoke descriptions:** https://crudata.uea.ac.uk/cru/data/holyoke/holyoke.descript.dat. The file name is confirmed by the readme. Download it in a browser or with curl and read Nov 1808 – Mar 1809, especially 8–12 Nov 1808 to test Bentley's "dark day". The full Hale tables are at https://archive.org/details/jstor-25057915 (PDF `25057915.pdf`).
- **Jefferson weather memorandum book (Washington, winter 1808–09):** https://jefferson-weather-records.org
- **Founders Online search**, with the date filter set to 1808-11-01 – 1809-05-31: https://founders.archives.gov/ (robots-blocked for tools).
- **Canadiana.ca**: Quebec Gazette and Halifax *Nova-Scotia Royal Gazette* 1808–09, https://www.canadiana.ca/ (robots-blocked). **BAnQ** collection: https://numerique.banq.qc.ca/collections/revues-journaux-quebecois-archives
- **Bentley vol. 3 page images, leaf 456**, to confirm the 10 and 12 Nov 1808 wording and dates: https://archive.org/details/diaryofwilliambe03bent/page/n455
- **Hill register page images, pp. 28–30** (Nov 1808 – Feb 1809): https://archive.org/details/meteorologicalch00hill
- **Readex / GenealogyBank** (Salem Gazette, Columbian Centinel, Portsmouth papers) for Nov 1808 darkness reports and for winter sky reports. Library access only.

# Strand file: C_iberian_italian_latam.md
## Strand C: Spanish, Portuguese, Italian and French sources, 1808–09 (round 5)

Worker C. Date: 2026-10-16. About 95 tool calls.

I grepped the project notes first. Already covered and not repeated here: Gazeta de Caracas, El Aviso, Gazeta do Rio, Semanario de Bogotá, Gazeta de Madrid/BOE (the Gazeta del Gobierno is in the same BOE collection), Diario de Mallorca, Giornale del Campidoglio, Corriere delle Dame, Giornale di fisica (Pavia), and the IA Iberian FTS passes.

## New access routes found this round (useful for later workers)

1. **The Europeana Search API works from here:** `https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=...&qf=YEAR:1809&profile=minimal`. It returns item-level records with direct provider links. It only matches metadata, not full text: queries such as "niebla" or "termometro" return 0.
2. **The MDZ (Bayerische Staatsbibliothek) IIIF full-text search works from here, with OCR:** `https://api.digitale-sammlungen.de/iiif/services/search/v1/bsbNNNNNNNN?q=TERM`. It returns hits with canvas number and an OCR snippet. The WebFetch summariser will only quote ≤125 characters at a time; asking for "segments of ≤90–100 characters" sometimes gets around that. The MDZ viewer and resolver themselves are blocked by robots.
3. **IA FTS takes `filter_map`.** A year range `{"year":{"1808":"gte","1810":"lte"}}` and a single-item filter `{"identifier":{"ID":"inc"}}` both work. The proxy rejects URLs longer than about 250 characters, and IA `advancedsearch.php` returned HTTP 429 (rate limited), so I did not retry it.

## (1) Sources tried

| Source | Place / lang | Covers Dec 1808–spring 1809? | URL | Digitized | Readable here | Result |
|---|---|---|---|---|---|---|
| **Giornale italiano** (Milan, official daily) 1809/1 = nos. 1–181 (Jan–Jun 1809) | Milan / it | **yes** | MDZ bsb10506317: https://www.digitale-sammlungen.de/en/view/bsb10506317 | yes | **yes (OCR search API)** | Searched for 14 keywords. No dry fog, pale sun or red twilight found. Etna-related ash and haze in Apr–Jun 1809 (see §2) |
| Giornale italiano 1808 (whole year) | Milan / it | Oct–Dec 1808 | MDZ bsb10506316: https://www.digitale-sammlungen.de/en/view/bsb10506316 | yes | yes (OCR search) | meteora, fenomeno, nebbia, eruzione, caligine: nothing relevant for Oct–Dec 1808 |
| Gazette nationale ou Moniteur universel vol. 41 (Jul–Dec 1808) | Paris / fr | Oct–Dec 1808 | MDZ bsb10487403: https://www.digitale-sammlungen.de/en/view/bsb10487403 | yes | yes (OCR search, poor OCR) | volcan, brouillard, météore: only ordinary items (a Spanish army bulletin reporting thick fog) |
| Moniteur 1809 Jan–Jun at MDZ | Paris / fr | yes | guessed bsb10487404 returned no hits (ID not confirmed) | ? | not confirmed | not found via Europeana |
| Moniteur universel, Table 1799–1814 pt 2 (subject index) | fr | yes (index) | https://archive.org/details/lemoniteuruniver179918142pari | yes | yes (IA FTS on the item) | brouillard: 0 hits. météore/phénomène: fireballs only, incl. "(1809) Apparition d'un météore enflammé" and a Ferentino night phenomenon. No dry fog, sun or haze entry |
| Moniteur Table pt 1 | fr | index | https://archive.org/details/lemoniteuruniver179918141pari | yes | yes | name index; "1809" hits are biographical |
| **Correo de Tenerife** (La Laguna, weekly, 25 Aug 1808 – 3 May 1810) | Canaries / es | **yes** (74 issues to 28 Dec 1809; no. 32 = 23 Mar 1809 missing in the Museo Canario set) | Jable: https://jable.ulpgc.es/correotenerife ; Maresía ULL issue viewers, e.g. 8 Dec 1808 http://maresia.bbtk.ull.es/viewer.vm?id=0000017788 , 15 Dec http://maresia.bbtk.ull.es/viewer.vm?id=0000017797 , 16 Dec …17806, 29 Dec …17820, 5 Jan 1809 …17831, 23 Mar 1809 …17930, 16 Apr 1809 …17974 | **yes** | **no**: Jable issue list is loaded by JavaScript; Maresía blocked by robots; MDC ULPGC behind an Anubis bot wall; Europeana record has no OCR | **BROWSER LEAD** |
| Diario de Barcelona 1808–09 | Barcelona / es | yes (e.g. 2 Apr 1809 held) | Memoria de Madrid (Hemeroteca Municipal Madrid): https://www.europeana.eu/item/2022711/14241 → http://www.memoriademadrid.es/buscador.php?accion=VerFicha&id=14241 ; viewer pattern https://www.memoriademadrid.es/view/NNNNNN | yes (images, PDF download) | no (images only, no OCR; one view page opened, 1812 issue) | **BROWSER LEAD** |
| Diario de Valencia (1790–), has "notas meteorológicas" | Valencia / es | yes (1808: 15 issues listed, incl. 23 Nov, 2 Dec, 11 Dec 1808; 1809 issues Jan–Jun) | BNE HD, e.g. 11 Dec 1808 http://hemerotecadigital.bne.es/details.vm?q=id:0004511785 ; 2 Dec 1808 …id:0004511761 ; 23 Nov 1808 …id:0004511752 | yes | blocked (BNE) | **BROWSER LEAD**: daily weather notes in a Mediterranean city |
| Gazeta de Valencia, Gazeta de Murcia, Correo de Murcia, Correo de Jaén, Gazeta del comercio de Cádiz, Gazeta del Gobierno (Sevilla), Diario de Sevilla (1809) | Spain / es | 1809 (partial runs) | BNE HD via Europeana records (e.g. Diario de Sevilla 1809 http://hemerotecadigital.bne.es/details.vm?q=id:0005506485) | yes | blocked (BNE) | not read |
| Gazeta de Lisboa 27 Dec 1808 | Lisbon / pt | one issue | http://hemerotecadigital.bne.es/details.vm?q=id:0004474228 (BNE holds a Gazeta de Lisboa run: …id:0004474227) | yes | blocked | BROWSER LEAD (BNE, not BNP) |
| O Telegrafo Portuguez (Dec 1808 – Jun 1809) | Lisbon / pt | yes | https://archive.org/details/otelegrafoportug00unkn_0 ; …00unkn | yes | yes (FTS; 00unkn seems to have no OCR text) | nevoeiro: military fog only. Sol: sunset in a military context. Negative |
| Hemeroteca Digital de Lisboa, "Invasões Francesas" PDF | pt | listing | https://hemerotecadigital.cm-lisboa.pt/EFEMERIDES/InvasoesF/Invasoes.pdf | – | yes | lists Lisbon titles 1808–09 (Gazeta do Rossio, O Lagarde Português 21 Nov–31 Dec 1808, Telegrapho Portuguez Dec 1808–Jun 1809). No digitization links |
| Correio Braziliense vol. II (nos. 8–13, Jan–Jun 1809) | London / pt | yes | IA volumes checked: 02=vol. III (Jul–Dec 1809), 00=vol. IV (1810), 01=vol. XVI (1816), 03=vol. X (1813), bub_gb_QlsPAAAAIAAJ=vol. XII (1814); 04–06 not opened | – | – | **Vol. II not found on IA.** FTS for "Fevereiro, 1809" finds no vol. II |
| Il Regio Dalmata / Kraglski Dalmatin (Zara, weekly) 1809 | Dalmatia / it-hr | yes (nos. 1–40, 1809, e.g. 6, 13, 20, 27 Jan) | http://dnc.nsk.hr/Newspapers/LibraryTitle.aspx?id=ec4bd886-2f50-4747-8582-29436f789de4&y=1809&m=1&d=20 | yes | blocked (robots) | BROWSER LEAD |
| Corriere milanese (IA, Senato "giornali-e-periodici-ottocento") | Milan / it | **no**: IA has 1794–1807 and 1811–14 only | https://archive.org/details/corriere-milanese-il-1811-01 | – | – | gap 1808–1810 |
| IA collection giornali-e-periodici-ottocento, 1808–09 | it | only Giornale del Campidoglio Jul–Dec 1809 | – | – | – | already covered |
| Gazzetta di Genova, Monitore napoletano, Gazzetta di Venezia, Notizie del Mondo, Courrier de Turin | it/fr | – | Europeana: 0 records 1808–09; IA: none found | ? | – | not found online here |
| Journal de l'Empire 1808–09 | fr | – | Europeana: Bodleian single issue 15 Jun 1808 (catalogue); Gallica blocked | – | – | not reached |
| IA FTS, year-filtered 1808–1812: "sole pallido", caligine, "brouillard sec", calina, "niebla seca", "sol opaco" | multi | – | IA FTS | – | yes | No 1808–09 sky reports. "brouillard sec" hits are 1781/1783 retrospectives and dictionaries |
| Prensa Histórica (prensahistorica.mcu.es), Hispana | es | – | – | – | blocked (robots) | – |
| MDC ULPGC PDFs (mdc.ulpgc.es/files/original/…) | Canaries | – | – | – | blocked (Anubis bot wall) | – |
| Jable ULPGC home and publication list | Canaries | – | https://jable.ulpgc.es | – | home yes; issue list no | confirmed Correo de Tenerife record |

Not attempted, for budget: Memoria Chilena chronicles (Chile had no press in 1808–09; prior notes say diaries only), Brasiliana USP, Galiciana, BV Andalucía, BV Defensa (prior notes list BVD naval items), RetroNews.

## (2) What the readable sources say (all OCR only)

### Giornale italiano, Milan, 1809 (MDZ bsb10506317, Jan–Jun 1809; canvas numbering: Milan April datelines about canvas 387, "Milano, Giovedì 1 Giugno" at canvas 567)
- **Canvas 75 (about early Jan 1809):** a fireball ("meteora fulminante") seen on 29 Dec between 5 and 6 a.m., NE→SW, bursting near "Bottigeu" (OCR). There is also an item from Switzerland, credited to the *Journal de l'Empire*: something that "sono accadute la notte del 12 dicembre", with the barometer very low and unsteady (an earthquake suspected). Fireball and seismic items only; no veil.
- **Canvas 428 (about mid–late Apr 1809), Calabria/Naples correspondence:** ash has recently covered the coast between Reggio and Scilla, thought to have been carried from Etna by winds. Quoted in segments: "...quella del vesuvio. Essendo così, bisogna dire che quel vulcano abbia fatto qualche eruzione. Il nostro vesuvio sarebbe allora con esso in una perfetta corrispondenza, essendo vivissime da più giorni le di lui era[zioni]..." ("...it must be said that that volcano has made some eruption. Our Vesuvius would then be in perfect correspondence with it, its eruptions having been very lively for several days"). **This is attributable to Etna, 24–27 Mar 1809. It is not the 1808/09 event.**
- **Canvas 621 (about mid-June 1809 issue):** a "meteora" (the snippet speaks of something seen several times, fleeting and barely noticeable, on "la predetta giornata" and the two following days): "Si crede che questa meteora sia stata prodotta, per consenso, dallo scoppio dell'Etna in Sicilia" ("This meteor is believed to have been produced, by sympathy, by the eruption of Etna in Sicily"). In the days before and after, the barometer was low, the air hazy and the weather completely calm (paraphrase of the OCR snippet). The place and exact date were not visible. **Attributable to Etna, spring 1809.** Worth reading the full page if the project wants Etna haze timing: canvas 621 of bsb10506317.
- Canvas 660: "nuove nebbie che oscurarono il nostro orizzonte" ("new fogs that darkened our horizon"); context not resolved (about mid–late June 1809).
- Canvas 352 (Apr 1809): a balloon ascent report in which the physicist came out above a cloud layer and saw the sun, "hidden for three weeks". Ordinary cloud.
- **Not found** in Jan–Jun 1809: caligine, crepuscolo, pallido, simpatia (0 hits). fenomeno, atmosfera, aurora, nebbie, vapori: nothing sky-related for Dec–Feb.

### Giornale italiano 1808 (bsb10506316)
- meteora: the Stannern meteorite fall (Moravia, 22 May 1808), a Parma/Borgo S. Donnino fall on 19 Apr 1808, and a storm at Monza. fenomeno: an earthquake centred on Piedmont (Apr 1808), a Corriere di Napoli note that natural signs "sono spesso il foriere di qualche eruzione" (Vesuvius), a salt-crust phenomenon, Messier's planetary conjunction. nebbia: fog at Lister fjord, Norway, 23 Mar. **Nothing about the sky or the sun in Oct–Dec 1808.** Caveat: I did not map the canvas numbers for Dec 1808, and keyword search misses words such as "sole".

### Moniteur universel, Jul–Dec 1808 (bsb10487403)
- Canvas 613 (a Spanish campaign bulletin, probably Nov–Dec 1808): "Le tems est humide ; un brouillard épais regne depuis trois jours" ("The weather is damp; a thick fog has prevailed for three days"). Ordinary winter fog in Spain, not a dry fog. Nothing else relevant.

### O Telegrafo Portuguez, 1809 (IA otelegrafoportug00unkn_0)
- Military fog at Amarante, "no dia 2, aproveitando-se do nevoeiro" (spring 1809), and a sunset in a military context. Negative.

## (3) Findings and verification strength
- **No positive evidence of the 1808/09 veil** (dimmed or silvery sun, red twilights, dry fog) in the readable Italian, French and Portuguese sources: the Giornale italiano for Oct 1808 – Jun 1809, the Moniteur for Jul–Dec 1808, the Moniteur subject index for 1799–1814, and O Telegrafo Portuguez. This is a **weak-to-moderate negative**: it rests on OCR keyword searches through summarised snippets, with no page-by-page reading.
- **Etna, spring 1809:** the Giornale italiano reports ash on the Calabrian coast (Reggio–Scilla) attributed to Etna (canvas 428, about Apr 1809) and a hazy, calm atmosphere with a "meteora" attributed to Etna (canvas 621, about Jun 1809). **Moderate:** OCR snippets only. These confirm the existing note that any Italian turbidity from late March 1809 must go to Etna first.
- Fireball of 29 Dec 1808 (Giornale italiano canvas 75) and a 1809 "météore enflammé" (Moniteur index): bolides, irrelevant to the veil.

## (4) Browser-only leads (exact URLs)
1. **Correo de Tenerife**, Dec 1808 – Mar 1809. Mid-Atlantic, and the only Atlantic-island paper of the window. It reprints American news via Cádiz and Havana and would carry ships' reports. Jable: https://jable.ulpgc.es/correotenerife (open the "Ejemplares" tab; 74 issues). Maresía ULL single issues: http://maresia.bbtk.ull.es/viewer.vm?id=0000017788 (8 Dec 1808), …0000017797 (15 Dec), …0000017806 (16 Dec), …0000017820 (29 Dec), …0000017831 (5 Jan 1809), …0000017930 (23 Mar 1809), …0000017974 (16 Apr 1809). Other ids come from the Europeana API query `"Correo de Tenerife"` (272 records). Memoria Digital de Canarias, mdc.ulpgc.es, also seems to hold it.
2. **Diario de Valencia** with daily meteorological notes, Dec 1808 – Feb 1809: BNE HD http://hemerotecadigital.bne.es/details.vm?q=id:0004511785 (11 Dec 1808), id:0004511761 (2 Dec), id:0004511752 (23 Nov). Use the BNE calendar for Jan–Feb 1809.
3. **Diario de Barcelona** 1808–09 (Memoria de Madrid, images and PDF): http://www.memoriademadrid.es/buscador.php?accion=VerFicha&id=14241 (2 Apr 1809). Browse neighbouring ids for Dec 1808 – Feb 1809. It has a daily weather line.
4. **Giornale italiano**, full pages in the MDZ viewer: https://www.digitale-sammlungen.de/en/view/bsb10506317 (1809/1); read canvases 75, 428, 621 and 660, and skim the Milan "Osservazioni meteorologiche" if the paper printed any. 1808: https://www.digitale-sammlungen.de/en/view/bsb10506316.
5. **Il Regio Dalmata** (Zara) 1809: http://dnc.nsk.hr/Newspapers/LibraryTitle.aspx?id=ec4bd886-2f50-4747-8582-29436f789de4&y=1809&m=1&d=6 (change m and d).
6. Gazeta de Lisboa at the BNE: http://hemerotecadigital.bne.es/details.vm?q=id:0004474227 (title) and id:0004474228 (27 Dec 1808).
7. Correio Braziliense vol. II (Jan–Jun 1809): not on IA. Try the Hemeroteca Digital Brasileira or the Brasiliana USP digital.bbm.usp.br.

# Strand file: D_missions_asia_logs.md
## D: Missionary periodicals, Asian/Pacific/African sources, ship logs (worker notes, 16 Oct 2026)

All readings are **OCR only** (IA full-text search snippets or djvu.txt via WebFetch). Nothing was checked against page images.

## Method notes (useful for the next worker)
- Before starting I grepped the project notes. Already covered, so not redone: Salt *Voyage to Abyssinia* (eyewitness_books_pass2 D1), Mawe, Morier, Elphinstone *Caubul*, Maria Graham, Golovnin, the Sydney Gazette suspension (daily_journals_round2), the whalers Cyrus/Hero (catalogue_sweep: manuscript images, no OCR), Sierra Leone Gazette/African Herald (indian_atlantic_pass3), London Evangelical Magazine (not on IA), and LMS Transactions vol. 4 (not on IA).
- **IA FTS with an identifier filter works** and is the efficient route. Example: `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=TERM&filter_map={"identifier":{"ID":"inc"}}` (URL-encode the JSON).
  - Multi-word queries are **AND**, and OR is not supported, so use one term per call.
  - Each call returns at most about 5 snippets per item.
  - The WebFetch proxy rejects URLs longer than about 250 characters, so filter on one identifier per call.
- WebFetch of `_djvu.txt` stops at about 100k characters, and the offset cannot go past that. Full reads are only possible for short items, such as single magazine issues.
- archive.org advancedsearch returned HTTP 429 once (rate limit), on a query for "periodical accounts" plus "baptist". Later calls worked.

### 1. Sources tried

| Source | Place / lang | Covers Dec 1808–spring 1809? | URL | Digitized | Readable here | Result |
|---|---|---|---|---|---|---|
| BMS *Periodical Accounts* vol. IV (London 1810; Ward/Carey journals 1808–09) | Bengal, Burma / EN | yes | catalogue only: https://www.wmcarey.edu/carey/bib/histories_missions.htm ; relbib https://relbib.de/Record/167311735 | not found online (IA has only a 1800 vol. I item) | no | **not located.** IA FTS for "Ward's journal" Serampore 1809 does not hit it |
| *Baptist Magazine* 1809, monthly issues Jan–Dec | London (BMS intelligence) / EN | partly (letters reach London 6–9 months late) | https://archive.org/details/baptist-magazine-1809_1809-12_1 (and _1809-01_1 … _1809-11_1) | yes | yes | Dec 1809 issue read in full: Chater (Rangoon) letters dated 26 Jan, 12 Aug, 5 Sep and 29 Sep 1808, plus a Ward letter of 12 Jan 1809 (Mrs F. Carey's death). **No weather or sky content.** Sep and Nov issues (djvu text, possibly partial) have no mission letters from the window. FTS on single issues was inconclusive because early tests used multi-word AND queries |
| *Methodist Magazine* vol. 32 (1809) | London; Jamaica, W. Indies, missions / EN | yes | https://archive.org/details/methodistmagazin0032john | yes | yes (FTS) | "earthquake" 0 hits; "weather" 5 snippets, all mundane; Jamaica letters (e.g. Kingston, 12 Apr 1809) are about persecution law. **Not found** |
| *Methodist Magazine* vol. 33 (1810) | same | yes (late letters) | https://archive.org/details/methodistmagazin0033unse | yes | not searched (budget) | — |
| *Evangelical Magazine* (London) 1809–10 | EN | yes | — | IA has only US namesakes (Connecticut, Vermont) | no | not located (confirms earlier note) |
| *Missionary Magazine* (Edinburgh) 1809; CMS *Proceedings* 1809–10 | EN | yes | — | not identified on IA | no | not located (advancedsearch failed on URL length; FTS gave no dated hits) |
| LMS *Transactions* vol. 4 (Huahine 1808–09) | Society Is. / EN | yes | — | not on IA (FTS on Huahine/Eimeo/Nott/Pomare 1809 gives only Ellis 1829) | no | not located |
| Danish-Halle *Neuere Geschichte der evangelischen Missionsanstalten … Ost-Indien* (St. 1–95, 1770–1848) | Tranquebar / DE | possibly (later Stücke) | ULB Halle record https://www.opendata.uni-halle.de/handle/1981185920/98574 (doi 10.25673/96617); Francke viewer https://digital.francke-halle.de/mod6a/content/pageview/338007 | yes (ULB Halle 2010) | **blocked** (Francke viewer behind a JS bot check; the ULB record gives no bitstream link); one Francke PDF opened (298623.pdf), but it is the 1863 Festschrift | not read; the Stück number for 1808–09 was not identified |
| Henry Martyn, *Journal and Letters* vol. 2 (1837) | Dinapore→Cawnpore, Bihar/UP / EN | yes | https://archive.org/details/journalandlette02wilbgoog | yes | yes (FTS) | 1809 letters at pp. 239–264 (Apr–Oct 1809). FTS "fog" 0; "weather" and "sun" snippets mundane (hot/cold season, sunstroke). **Not found** |
| *Life of Mrs Sherwood* (1857) | Dinapore, Berhampore, Cawnpore / EN | yes (undated narrative) | https://archive.org/details/lifeofmrssherwoo00sher | yes | yes (FTS) | "fog" 0; "hazy": "It was one of those sickly, hazy, burning evenings, which I have before described" (undated; hot-season context). **Not diagnostic** |
| *Memoirs of Sir James Mackintosh* vol. 2 (1836; Bombay journal from 1809) | Bombay / EN | yes | https://archive.org/details/memoirsoflifeofr02mackuoft | yes | yes (FTS) | "hazy" (Lago Maggiore, later), "sky" (irrelevant). **Not found.** Vol. 1 hits: letter of 29 Mar 1809, no sky content |
| *Lord Minto in India* (1880) | Calcutta / EN | yes | https://archive.org/details/lordmintoinindia00mint | yes | yes (FTS) | "hazy" 0; "fog" only an advertisement; "sunset" = evening walks and breeze. **Not found** |
| Trove *Sydney Gazette* (article and API) | NSW / EN | yes | https://trove.nla.gov.au/newspaper/article/626071 ; api.trove.nla.gov.au | yes | **blocked** (Anubis on the article page; the API is robots-disallowed) | not read |
| William Ward diary / wmcarey.edu site | Serampore / EN | ? | https://www.wmcarey.edu/carey/wmward/Main%20html/contents.html | biography chapters only | yes | no diary transcription found |
| Ship-log datasets (GitHub, oldweather, RN keyed logs) | – | – | WebSearch only | – | – | no openly keyed 1808–09 log text found beyond what the project already has. TNA/RMG catalogue hits only |
| Hagemeister *Neva* journal 1807–10; Metcalfe mission (Punjab) 1808–09; Buchanan Rangpur | – | yes | – | – | not tried (budget) | — |

### 2. What the sources say for the dates (OCR only)
- **Baptist Magazine, Dec 1809:** Rangoon letters from Chater dated before Oct 1808. A letter from Ward to Fuller dated 12 Jan 1809 reads "Sister Felix Carey died a few days ago". It contains no weather or sky remark.
- **Methodist Magazine 1809:** "Chapel House, Kingston, Jamaica, April 12, 1809" (missionary letter about persecution). The FTS "weather" snippets are generic. "earthquake", "hazy", "volcano" and "eruption" were tested only as multi-word AND queries, so the result is uncertain (see method note). A single-term "earthquake" query gave 0 hits.
- **Martyn vol. 2:** "April 3, 1809. I wrote to the Military Board…" and "May 22, 1809. For the last three or four days I have been…". The weather snippets are the usual hot and cold season remarks, e.g. "the sudden increase of heat in the weather, I had a small attack of fever".
- **Mrs Sherwood:** "sickly, hazy, burning evenings" is undated and refers to the Bengal hot season.

### 3. Findings
- **No positive or suggestive evidence** of a dimmed sun, dry fog or red twilights in Dec 1808 – May 1809 in any source read here: Baptist Magazine (Dec issue in full, two other issues partially), Methodist Magazine 1809, Martyn, Sherwood, Mackintosh, or Minto.
- These negatives are **weak**. They rest on keyword FTS with a 5-snippet cap, and on missionary letters that rarely report weather. Bengal's normal cold-season haze would in any case hide a faint veil.

### 4. Browser-only leads (exact URLs)
1. Danish-Halle *Neuere Geschichte* (ULB Halle / Francke Foundations): https://www.opendata.uni-halle.de/handle/1981185920/98574 ("View online"). The Stücke printed c. 1810–1815 should hold Tranquebar diaries for 1808–09, if any were sent. Communications were cut after the British occupied Tranquebar in 1808 (inference).
2. BMS *Periodical Accounts* vol. IV (1810): physical copies at Regent's Park College, Oxford (Angus Library), and Yale Divinity (see https://web.library.yale.edu/sites/default/files/files/fa-bms.pdf). Possibly on Google Books (blocked here).
3. Trove *Sydney Gazette*, Dec 1808 – May 1809: https://trove.nla.gov.au/newspaper/title/3 (open in a browser).
4. The remaining Baptist Magazine 1809 issues (Jul, Aug, Oct): https://archive.org/details/baptist-magazine-1809_1809-08_1 etc. They are short and can be read in full in the browser.

---

# Extension (16 Oct, ~14:00–15:00 UTC): window to Jun 1810, eruption indicators beyond the veil

At William's request, every strand reran its searches over Oct 1808 – Jun 1810 for booms or cannon fire, ash on decks, midday darkness, floating pumice, glow on the horizon, new islands, sea withdrawal or waves, grey rivers, sulfur smell, blood-red twilights, blue or green sun, solar rings, dark lunar eclipses, and later frosts or crop failures, using notes/eruption_clue_search_terms.md plus German/Italian/French equivalents. All OCR only.

## Summary
- **No eruption indicator from Asia, the Pacific, the Indian Ocean or the Americas in any source reached.** Every volcanic item traces to a known European/Atlantic source: Etna Mar 1809 (ash on Calabrian coast ~Apr 1809), Vesuvius (lava 28 Jan 1809; new cone and ash 4–5 Sep 1809), São Jorge 1808 reprints, Azores Sabrina 1811.
- Tectonic events found: Piedmont swarm Nov 1808–Apr 1809 (sulfur smell), Zagreb 9 Dec 1808, San Germano 16–17 Feb 1809, L'Aquila swarm from 1 Aug 1809, Lisbon ~11/26 Oct 1809, Cape Town 4 Dec 1809 ("noise was tremendous", Methodist Magazine 1810 p. 223), Hungary/Vienna 14 Jan 1810, Crete/Malta Feb 1810, São Miguel 11–12 Aug 1810.
- Cold signs only: snow at Warren NY 9 Aug 1809 and northern frosts (Medical Repository Aug–Oct 1809 p. 91); corn injured by frost near Lancaster PA by 19 Sep 1809 (Alexandria Gazette 30 Sep 1809). Cool 1809 summer consistent with, but not specific to, a volcanic cooling.
- Asian news in European/US papers 1809–10 is political or maritime (Madras officers' revolt, Dutch expedition vs "Solou", East India fleet storm losses late 1809, Canton pirates). No volcanic report.
- Untested: 39 "Kanonendonner" pages in German papers (probably battles), ~70 "Vulkan" pages 1809–10, "cannonading" in US papers (rate-limited), Giornale italiano 1810, Moniteur 1809–10, port papers of Salem/Boston/NY/Philadelphia (Readex).
- New resource: ~1,083 free Bombay Courier issues on archive.org (from 5 Jan 1811 only): https://archive.org/search?query=subject%3A%22Bombay+Courier%22
- Savannah Republican 28 Jun 1810 "volcano" hit = political metaphor.


# Extension strand file: A_ext.md
## Strand A, extension: German press Oct 1808 – Jun 1810, eruption indicators beyond the veil

Worker notes, 16 Oct 2026. About 50 tool calls. Same route as in A_nordic_central.md: the open Deutsches Zeitungsportal (DDB) Solr index, read through WebFetch.

**Everything here is OCR only.** I saw no page images. A summariser sits between me and the text, and it caps quotes at about 125 characters, so quotes are short fragments.

The project's term list (notes/eruption_clue_search_terms.md) has no German. I used its Asian and Pacific place names in German spelling (Java, Molukken, Celebes, Manila, Kamtschatka, Japan, Batavia, Ostindien, Bengalen) and added my own German terms.

**Query format.** `https://api.deutsche-digitale-bibliothek.de/search/index/newspaper-issues/select?q=plainpagefulltext:(TERMS)&fq=publication_date:[1808-10-01T00:00:00Z%20TO%201810-07-01T00:00:00Z]&fl=id,publication_date&rows=50`. To read a page: `?q=id:<ID>&fl=paper_title,publication_date,plainpagefulltext`.
- The WebFetch proxy refuses URLs over about 250 characters. That limits OR-lists to about 3 terms.
- The OR-groups must sit inside `plainpagefulltext:( … )`; otherwise the second term searches the wrong field.

**Human viewer.** `https://www.deutsche-digitale-bibliothek.de/newspaper/item/<ITEM-ID>`, using the id prefix before `-FILE`/`-ALTO`/`-fulltext`. I inferred this pattern and did not test it.

**Human search.** https://www.deutsche-digitale-bibliothek.de/search/newspaper?query=Vulkan&fromYear=1808&toYear=1810

## 1. Indicator searches (Oct 1808 – 1 Jul 1810 unless stated)

| Indicator | Query | Hits | Read | Outcome |
|---|---|---|---|---|
| Booms or cannon fire | Kanonendonner AND Schiff | 39 | 0 | Not read. Dates cluster in the war seasons (Oct 1808 Spain; Apr–Aug 1809 Austrian war; Apr–Jun 1810), so these are almost certainly battle reports. **Untested** for unexplained booms. |
| Underground roar | "unterirdisch Getöse"~3 | 0 | – | none. But the Stockholm item of 22 Mar 1809 (Västergötland quake, "mit einem unterirdischen Getöse") is known from round 1, so OCR or phrasing varies. |
| Ash on deck | "Asche Verdeck"~10 | **0** | – | none |
| Midday darkness | Finsterniß AND Mittag AND Asche | 2 | 2 | Both irrelevant. (a) Münchener politische Ztg, 13 Apr 1809: a village fire on Amager (Copenhagen) "Gegen Mittag brach … Feuer aus … lagen 30 Höfe und 11 Häuser in der Asche" [around noon a fire broke out … 30 farms and 11 houses lay in ashes]. (b) Großherzoglich-Bergischer Anzeiger, 3 Jun 1810: a church polemic in which the words are used as metaphors. |
| Pumice | Bimsstein* | 7 (Dec 1808–Aug 1809); 2 (Sep 1809–Jun 1810) | 2 + 0 | The ones read are recipe and simile noise (see round 1). |
| Night glow on the horizon | Feuerschein AND Horizont | **0** | – | none |
| New island | "neue Insel" | **0** | – | none |
| Sea withdrawal or wave | "Meer zurück"~3 OR Fluthwelle | 7 | 3 | All non-events: a British retreat to the sea after Talavera (Münchener politische Ztg, 11 Sep 1809); a squadron returning (Hamb. Correspondent, 11 Oct 1808); a poem (Morgenblatt, 17 Feb 1810). |
| Sulfur smell | Schwefelgeruch | 12 | 2 | (a) Berlinische Nachrichten, 16 Feb 1809: the **1808 Piedmont earthquakes** (Pinerolo valleys, 1808), "man bemerkte überall Schwefelgeruch … Feuer brach zugleich aus der Erde und aus den Wolken hervor" [a smell of sulfur was noticed everywhere … fire broke out at once from the earth and the clouds]. Known European seismic event. (b) Allgemeine Zeitung, 14 Apr 1810: the **Hungarian (Mór / Csóka-hegy) earthquake of 14 Jan 1810**, with aftershocks to 14 Feb. Pest professors found "weder … noch ein Rauch, noch ein Schwefelgeruch" [neither … smoke nor a smell of sulfur]. Not volcanic. |
| Blood-red | blutroth | 5 | 1 | Allg. Anzeiger der Deutschen, 16 Jan 1810: a Braunschweig seed catalogue (red cabbage). Noise. Others unread (poetry and journal titles). |
| Halo round the sun | "Hof um die Sonne"~2 | **0** | – | none (Sonnenring was dropped because of URL length) |
| Lunar eclipse | Mondfinsterniß | 6 | 2 | Both are theatre reviews of Klingemann's *Columbus* (Morgenblatt, 6 May 1809; Elegante Welt, 8 Apr 1809). There was no report of a dark eclipse. |
| Crop failure | Mißwachs OR Mißerndte (Mar 1809–Jun 1810) | 8 | 2 | Generic agricultural essays (Göttingische gel. Anz., 13 Jul 1809; Allg. Anzeiger, 20 Mar 1809). No dated regional failure. |
| Asian/Pacific volcano | (Java OR Molukken OR Celebes) AND Vulkan | **0** | – | none |
| " | (Manila OR Kamtschatka OR Japan) AND Vulkan | – | – | URL too long; not run |
| Asian ash | (Batavia OR Manila) AND Asche | 1 | 1 | Hamburger Relations-Courier, 19 Feb 1810: "Batavia" is a cloth name and "Asche" is American potash at auction. Noise. |
| Asian earthquakes | (Batavia OR Java) AND Erdbeben | 2 | 1 | Morgenblatt, 20 Feb 1810: a review of Valentijn, about the **Amboina earthquake of 1687**. Historical. |
| " | (Ostindien OR Bengalen) AND Erdbeben (Dec 1808–Jun 1810) | 8 | 2 | Berlinische Nachrichten, 12 Dec 1809: India news is military (Madras officers' revolt, Brownrigg); separately, a **Lisbon earthquake felt ~11 Oct 1809, 10 pm**, no damage. Berlinische Nachrichten, 23 Mar 1809: two East Indiamen (*Britannia*, *Admiral Gardner*) wrecked on the Goodwin Sands in storms (London, 14 Feb); **San Germano earthquakes 16–17 Feb 1809**, people fled to the fields. This identifies the garbled "St. Germans" in the Hamb. Correspondent of 17 Mar 1809. |
| American volcanoes | Vulkan AND (Amerika OR Peru OR Chili), Jan 1809–Jun 1810 | 6 | 3 | Hamb. neue Ztg, 1 Mar 1809: Vesuvius, Naples, 3 Feb; lava on the evening of 28 Jan. Karlsruher Ztg, 29 Sep 1809: **Vesuvius, new vent opened to the SW on 4 Sep 1809, and on the night of 5 Sep it threw out ash, dust and stones, building a new cone.** Neue Jugendzeitung, 17 Feb 1810: an educational piece on the Quito volcanoes after Humboldt (Cotopaxi 1738/1744, Antisana "smoking" 1802, Carihuairazo 1698). No contemporary Andean eruption. |
| Any volcano, Jun 1809–Jun 1810 | Vulkan OR Vulcan | 78 | 4 | The Sep–Oct 1809 cluster is the Vesuvius Sep 1809 eruption. Hits read: Hamb. Correspondent, 23 Jan 1810 (Milan fresco, the god Vulcan); Allgemeine Zeitung, 1 Feb 1810 ("Bischof Vulkan" of Grosswardein; also an **earthquake felt in Vienna on the evening of 14 Jan 1810**, stronger at Pressburg); Allgemeine Zeitung, 11 Mar 1810 (Messina, Jan [1810]: Etna had a "starker Ausbruch" [strong eruption] "vorigen Sommer" [last summer, i.e. 1809], with no great devastation); Hamb. neue Ztg, 11 May 1810 (Vulcan on an Antwerp parade float). **No Asian, Pacific or American eruption news.** About 70 hits unread, mostly the Vesuvius 1809 coverage and mythology. |

## 2. Pages requested by the coordinator

- **Hamb. Correspondent, 13 Dec 1808, p. 4** (Erdbeben): Pignerol (Pinerolo), "Am letzten dieses hat man zu Pignerol wieder ein Erdbeben verspürt" [at the end of this month another earthquake was felt at Pignerol], i.e. late Nov 1808. This continues the Piedmont swarm. No shipping or overseas items; no sky remark.
- **Hamb. Correspondent, 3 Jun 1809, p. 2** (Erdbeben): Naples, 9 May. Around midnight there was a loud rumbling and several shocks "die ein Erdbeben fürchten ließen" [that made people fear an earthquake], and a glowing flame was seen on the summit of Vesuvius for some minutes; also a thunderstorm with hail. Shipping: a fire in Naples harbour; an English convoy of ~70 sail; New York ships for Madeira and Fayal held back by the embargo. **No Asia, Pacific, Cape or Île de France news.**
- **Hamb. Correspondent, 27 Jun 1809, p. 6** (Erdbeben): datelined "Lorsu [Corfu?], den ?? May". An earthquake damaged several houses, with shocks on the two following days. Shipping: a Portuguese cartel ship arrived in the Loire "in 54 Tagen von Cayenne" [in 54 days from Cayenne] (no natural phenomena reported). **No Asian or Pacific news.**
- **Abendröthe/Morgenröthe hits for Dec 1808–Feb 1809**, 3 more read (Hamb. Correspondent, 7 Dec 1808; Bildungsblätter, 29 Dec 1808; Schweizer-Bote, 3 Feb 1809). With the 3 from round 1, that makes 6 of the ~10 hits in the window. All are figurative or fiction ("Morgenröthe des Segens" [dawn of blessing]; a hermit's tale; a treasure-ghost story). **No real twilight observations.**

## 3. Bottom line

- **No indicator of a distant eruption was found** in the German press, Oct 1808 – Jun 1810: no unexplained booms tested positive, no ash on decks, no midday darkness, pumice rafts, new islands, sea waves, halos, blood-red or coloured suns, dark eclipses, or Asian, Pacific or American eruption news.
- **Asian news in these papers is political and military** (the 1809 Madras officers' revolt; Lord Minto). It reached Germany about 6–9 months late via London. The **Pacific and Philippines are absent**, and nothing was found from Batavia, the Cape or Île de France apart from noise. This fits the British blockade of Dutch and French Indian Ocean colonies.
- Natural events found, all European and non-diagnostic:
  - Piedmont earthquakes (1808, continuing to late Nov 1808)
  - Zagreb, 9 Dec 1808 (round 1)
  - Västergötland, 15 Jan 1809 (round 1)
  - San Germano, 16–17 Feb 1809
  - Vesuvius renewals (28 Jan 1809; 8–9 May 1809 rumblings; **4–5 Sep 1809 ash eruption**)
  - Etna, summer 1809
  - Lisbon earthquake, ~11 Oct 1809
  - Hungarian (Mór) and Vienna earthquake, 14 Jan 1810
- **Limits on these negatives:**
  - Fraktur OCR quality is unknown.
  - Hits were sampled, not exhausted: Kanonendonner 39 unread; Vulkan 1809–10 about 70 unread; Schwefelgeruch 10 unread.
  - Dano-Norwegian (api.nb.no): "Vulkan AND year:1810" returned 0. The 1809–10 Norwegian OCR is too poor for indicator searches (see round 1), so I did not pursue it.

## 4. Browser leads

1. DDB human search for the untested booms: https://www.deutsche-digitale-bibliothek.de/search/newspaper?query=Kanonendonner&fromYear=1808&toYear=1810 (39 pages). Look for "ohne daß man wußte" or "unbekannt" near the term in Dec 1808 – Mar 1809, and in any sea report.
2. ANNO (Wiener Zeitung), Finland, Sweden, Mediestream, Riga corpus: as listed in A_nordic_central.md section 4. The Riga TXT corpus is the cheapest complete test for all these indicators.
3. Hamburg shipping lists ("Schiffs-Nachrichten" in the Hamburgischer Correspondent / Börsen-Halle) for ships arriving from Batavia, Canton or the Cape in 1809–10. This needs page-by-page reading in the DDB viewer; the OCR keyword route cannot isolate those columns.

# Extension strand file: B_ext.md
## Strand B extension: North American sources, Oct 1808 – Jun 1810, eruption indicators beyond the veil

Worker notes, 2026-10-16. Builds on `B_north_america.md` in this folder. Search terms follow `/mnt/project-files/1808-eruption/notes/eruption_clue_search_terms.md`.

**Everything here is OCR only.** Text comes from archive.org full-text search snippets and per-item search. I viewed no page images. The WebFetch summariser caps each verbatim quote at about 125 characters, so long passages appear as consecutive fragments.

## Method

**Search that worked on archive.org.** I added a year filter, plus a collection filter, to IA full-text search:
`https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=TERM&filter_map={"year":{"1809":"gte","1810":"lte"},"collection":{"newspapers":"inc"}}`
- The URL has to be URL-encoded, and adding `hits_per_page` pushes it over the proxy's length limit.
- It returns US papers on IA for 1809–1810:
  - *Alexandria Daily Gazette* (runs into 1810)
  - *Pittsburgh Weekly Gazette* (runs to Dec 1810)
  - *Newport Mercury*
  - *Kentucky Gazette* (`xt…` ids)
  - Dutch `ddd_` papers (not my strand)
- The same filter with `"pub_monthly-anthology-and-boston-review"` as the collection searches the *Monthly Anthology*.
- Single words only; phrase queries fail, so "dark day", "new island" and "shower of ashes" could not be searched.

**Problems.**
- One query, `cannonading`, was refused with HTTP 429. Per the proxy's instruction I did not retry it, so the "cannonading" term is **untested**. "explosions" was run instead.
- Many archive.org calls overall; one rate-limit hit.

## 1. Sources and queries tried

| Source | Place | Window covered | URL | Readable | Terms run | Result |
|---|---|---|---|---|---|---|
| IA newspapers (Alexandria, Pittsburgh, Newport, Kentucky), 1809–1810 | VA, PA, RI, KY | Jan 1809 – Dec 1810 | https://archive.org/details/newspapers (items listed below) | yes (snippets) | volcano, pumice, ashes, eruption, earthquake, darkness, explosions, sulphur, suffocating, meteor, Manilla, Batavia, Canton, Otaheite, Sandwich, frost | **No eruption indicator from Asia, the Pacific or the Americas.** Details in §2. |
| William Bentley, *Diary* vol. 3 (Salem) | Salem MA | to Dec 1810 (Jun 1810 ≈ leaf 593) | https://archive.org/details/diaryofwilliambe03bent | yes | ashes, pumice, eclipse, Canton, Batavia, explosion, noise, frost, sun, red, dark, plus round-1 terms (volcano, earthquake, smoke, hazy, fog, sky, Aurora) | Nothing for Dec 1808 – Jun 1810. Only the 8–12 Nov 1808 darkness from round 1. |
| *Medical Repository*, Aug–Oct 1809 issue (vol. 13) | New York State | summer and autumn 1809 | https://archive.org/details/sim_medical-repository_august-october-1809_1 | yes | weather, snow, frost | **Cool summer 1809; snow at Warren on 9 Aug 1809** (see §2) |
| *Medical Repository*, Nov 1809–Jan 1810 issue | NY | 1809 | https://archive.org/details/sim_medical-repository_november-1809-january-1810_1 | yes | weather | Nothing relevant: influenza articles that refer back to 1807. |
| *Medical Repository*, Feb–Apr 1810 issue | NY | winter 1809–10 | https://archive.org/details/sim_medical-repository_february-april-1810_1 | **server error** | — | Not read. |
| *Medical Repository*, vol. 12 issues | NY | winter 1808–09 | see `B_north_america.md` | yes | (round 1) | Cold winter; nothing optical. |
| *Monthly Anthology and Boston Review*, 1809–1811 | Boston | yes | https://archive.org/details/pub_monthly-anthology-and-boston-review | yes | volcano, earthquake, ashes | São Jorge 1808 reprint, Cape Town earthquake of Dec 1809, literary uses. Nothing new. |
| *Universal Magazine* (London), Sept 1809 (found through an unfiltered "pumice" search) | Bismarck Sea | voyage in 1803 | https://archive.org/details/sim_new-universal-magazine-or-miscellany_1809-09_12_70 | yes | pumice | Pumice field in 1803; outside the window. See §2. |
| *Republican; and Savannah Evening Ledger* (Georgia Historic Newspapers) | Savannah GA | yes | https://gahistoricnewspapers.galileo.usg.edu/search/pages/results/?lccn=sn82014388&andtext=volcano&rows=100 | page-level hits only; no OCR text (robots) | volcano | 1808–1810 hits: 15 Sep 1808 p. 2, **28 Jun 1810 p. 3**, 15 Dec 1810 p. 2. Text unreadable here; browser lead. |

## 2. What the sources say

### IA newspapers, 1809–1810

**volcano (7 hits).** None is a new eruption.
- The São Jorge (Azores) May 1808 Dabney letter: Alexandria 25 Feb 1809, Kentucky Gazette 21 Mar 1809 (already known, F1 of round 2).
- The rest are figurative: Newport Mercury 30 Sep 1809; Alexandria 14 Jul and 18 Oct 1809. Kentucky Gazette 17 Oct 1809 has "Volcano" as a racehorse's name.

**pumice (22 hits).**
- Mostly Pittsburgh drug-store adverts for "Pumice-stone" (1810), plus apple "pumice" (pomace).
- Pittsburgh 13 Jul 1810: "Pumice is found in abundatce", from a Missouri/Gros Ventres travel account. This is geology, not floating pumice.
- Alexandria 25 Feb 1809: the Azores "small pumice stones" (São Jorge).
- **No floating pumice reported at sea.**

**ashes (134 hits; 49 reviewed).**
- Pot and pearl ash trade, figurative uses, and the Azores letter.
- Pittsburgh 8 Nov 1809 "by the ashes which are discharged" is the Etna 1809 article (round-2 F5).
- **No ashfall on decks or ashfall on land.**

**eruption (10 hits).** Etna (Pittsburgh 8 Nov 1809). The rest are skin eruptions, or "make an eruption into Canada" (Alexandria 9 Jan 1810).

**earthquake (13 hits).** All are Mediterranean or Atlantic, or lists of historical earthquakes:
- Kentucky Gazette 21 Aug 1810 and Pittsburgh 17 Aug 1810: "the same earthquake was felt, in all its terrific force in the island of Candia (the ancient Crete)… felt at Cairo, Alexandria, Malta, Sicily". This is the Crete earthquake of Feb 1810.
- Kentucky Gazette 12 Jun 1810: "Accounts from Malta state, that on the 16th Feb. that island suffered from a severer shock of an earthquake than it ever before experienced". Same event.
- Pittsburgh 3 Aug 1810: Tenerife. Pittsburgh 24 Aug 1810: St. Michael's, Azores. Newport Mercury 11 Aug 1810: an earthquake destroyed a village (place garbled).
- Kentucky Gazette 6 Jun 1809: Cumberland RI ground-shaking (round-2 F2).
- Pittsburgh 29 Jun 1810 and Kentucky Gazette 24 Jul 1810: a list of historical earthquakes.
- **None from Asia, the Pacific or South America in 1808–10.**

**darkness (43 hits).** All are figurative, a theatre playbill (Alexandria 9 and 11 Sep 1809), or "darkness of the night". **No darkness by day.**

**explosions (4 hits).** Magazines blowing up in war news (Alexandria 6 Jan 1810), rhetoric, and torpedoes. **No unexplained booms.**

**sulphur and suffocating.** One natural event:
- Pittsburgh Weekly Gazette 23 Aug 1809: "…of ordnance, and was succeeded by a strong suffocating smell of sulphur, about two minutes continuance. It met the earth…" and "[la]st night, during the storm, a large meteor [ba]ll of fire, supposed to be about two feet in [diam]eter".
- This is a **thunderstorm fireball or ball lightning**, local. Not volcanic.

**meteor.** The Connecticut (Weston) meteorite, a fireball over Glasgow, and figurative uses.

**Manilla, Batavia, Canton, Otaheite, Sandwich (Asia and Pacific shipping news).**
- Canton: 161 hits, of which 12 are arrivals or news. Manilla: 5 English. Batavia: 1 English (a cargo advert). Otaheite: 1. Sandwich Islands: only two book adverts.
- I read two China reports in full:
  - Kentucky Gazette 1 May 1810, reprinting the NY *Mercantile Advertiser*: ship *Chinese*, Capt. Brum, from Canton. The Ladrone pirate fleet of "nearly 300 sail of junks", Portuguese blockade, villages destroyed, East India Company officers at Canton.
  - Kentucky Gazette 24 Jul 1810: "FROM CANTON.—By capt. Dorr", on the Anglo-Chinese dispute and the chop refused to British ships.
- Other China arrivals seen as snippets only: Newport Mercury 18 Feb 1809 (brig *Resort* from Canton, lading at Batavia); Pittsburgh 6 Sep 1809 ("She left Canton 20th March"); Newport Mercury 16 Jun 1810 (shipping "embargoed at Canton from Jan. 27 to Feb. 22"); Pittsburgh 24 Aug 1810 (the *Vancouver*, Whittemore, from Canton, about 3 years absent, i.e. a Northwest Coast voyage).
- **No natural phenomenon (ash, darkness, booms, sea anomaly, pumice) appears in any snippet or in the two reports read in full.**
- Manila items: Drury's squadron capturing US ships off Macao (Alexandria 26 May 1809), a Baltimore ship carried into Manila (Kentucky Gazette 15 May 1810), and a man cast away on the Philippines (Kentucky Gazette 22 May 1810). Nothing natural.

**frost (48 hits).**
- Alexandria Daily Gazette 30 Sep 1809, from "Lancaster, (Pa.), Sept. 19": "We have already had several slight frosts… In some places the corn has been injured", and a single "sharp frost" would be "highly destructive". An early autumn frost of moderate severity.
- Kentucky Gazette 11 Sep 1810: "A frost in Pittsfield, Massachusetts".
- The May 1809 "frost-bitten" hits refer to hands, in a shipwreck story.

### Bentley diary, Salem, to mid-1810

- Leaf numbering: 1809 runs to about leaf 557, Feb 1810 starts at leaf 564, Jun 1810 at leaf 593.
- No hits in the window for ashes, pumice, volcano, eclipse, explosion (except the Portsmouth NH fort powder explosion of 4 Jul 1809, leaf 510), noise, hazy, smoke, fog, sky or Aurora.
- "sun", "red" and "dark" hits after Nov 1808 are irrelevant: a red snapper fish (leaf 553), troops returning after dark (leaf 538).
- Knock-on climate notes: leaf 494, May 1809, "Such uniformly backward weather is uncommon in our climate"; leaf 496, "The Weather wet & vegetation late"; leaf 505, summer heat first reached on 21 May 1809.
- Canton and Batavia hits are all from before 1806.

### Medical Repository, Aug–Oct 1809 issue, p. 91: "State of Weather and Diseases in the Summer and Autumn of 1809" (New York State)

- "that on the 9th of August, snow was observed to fall for several minutes in the town of Warren"
- "It is certain that frost was distinctly noticed, and the inhabitants of that part of the country were…"
- Per the summariser: June cool, July moderate with cool days after the rains of 17–19 July, August "uncomfortably cold weather was felt in the northern parts of the State", September dry, October cool.
- So **a cool summer in New York State in 1809, with an August snow flurry and frost in the north** (Warren, Herkimer County).
- This is a knock-on-type indicator, consistent with the cool 1809 summers reported elsewhere. It is suggestive only, since summer frosts in upstate NY are not unprecedented.

### Monthly Anthology, May 1810, p. 66

"The island of Bossen, or Penguin, sometimes called Seal Island, at the western extremity of Table Bay, has entirely disappeared beneath the waters. An earthquake was felt at Cape Town, in December, only two leagues distant… it is supposed that the convulsion extended to Bossen."

This is the Cape Town (Milnerton) earthquake of 4 Dec 1809 and a false rumour of the island vanishing. Tectonic, not volcanic. It also shows the 5-month news lag from the Cape.

### Universal Magazine, Sept 1809 ("Voyage from Port Jackson to Prince of Wales's Island", a lady's letters)

"At Sea, July 10, 1803", lat. 2°52′S, long. 149°5′E (near the Admiralty Islands and Manus): "pumice-stone floating on the water, as far as the eye" could see. The writer adds "Two volcanic islands are known to exist about one hundred miles from our present situation", and the ship "laboured through them with a crushing noise".

**The event is from 1803, outside the window**, but it shows that this kind of report does reach the periodicals.

## 3. Summary of findings

- **Not found:** across the 1809–1810 IA run of US newspapers (Alexandria, Pittsburgh, Newport, Kentucky), Bentley's Salem diary to Jun 1810, the *Medical Repository* and the *Monthly Anthology*, I found **no unexplained booms, ash on decks, midday darkness, floating pumice, night glow or new island, sea withdrawal, grey rivers, acid fog, unusual twilights, blue or green sun, solar ring, or dark lunar eclipse** reported from Asia, the Pacific, South America or North America for Oct 1808 – Jun 1810.
- **Shipping columns from Canton, Manila and Batavia** that I could see deal only with war, piracy and trade.
- **Weak positive, knock-on only:**
  - A cool New York summer in 1809, with snow at Warren, Herkimer County, on 9 Aug 1809 and frost in the north (*Medical Repository*).
  - A "backward" May 1809 in Salem (Bentley).
  - Light early frosts damaging corn near Lancaster PA by 19 Sep 1809.
  - Verification: OCR snippets only.
- **Limits:**
  - The IA corpus lacks the Salem, Boston, New York and Philadelphia port papers, where East India and China arrivals were first printed. The inland papers reprint only a selection.
  - The fts engine handles only single words. The "cannonading" query was rate-limited and is untested.
  - The *Medical Repository* Feb–Apr 1810 issue gave a server error.

## 4. Browser-only leads

- Savannah *Republican*, 28 Jun 1810, p. 3 ("volcano"): https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1810-06-28/ed-1/seq-3/#words=volcano ; also 15 Sep 1808, p. 2: https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1808-09-15/ed-1/seq-2/#words=volcanoes
- *Medical Repository*, Feb–Apr 1810: https://archive.org/details/sim_medical-repository_february-april-1810_1 (search "weather" for the NY winter 1809–10 report).
- Rerun the fts "cannonading" query above, and try "firing", "reports", "afhes" and "fulphur" (long-s OCR variants).
- Readex *America's Historical Newspapers*: Salem Gazette, Columbian Centinel, NY Mercantile Advertiser and Poulson's marine lists, Oct 1808 – Jul 1810. These are the key East India and China arrival columns.

## Checked by the thread session (16 Oct)
- Savannah *Republican* 28 Jun 1810 p. 3 'volcano' hit: metaphor in a political speech ('from the first burst of the Gallic volcano'). Not relevant. OCR via https://gahistoricnewspapers.galileo.usg.edu/lccn/sn82014388/1810-06-28/ed-1/seq-3/ocr/

# Extension strand file: C_ext.md
## Strand C extension: non-veil eruption clues, Oct 1808 – Jun 1810 (Italian, French, Spanish, Portuguese)

Worker C, second pass, 2026-10-16. About 60 tool calls. All text is **OCR only**, read as search-API snippets summarised by WebFetch, which quotes at most about 125 characters. No page images were seen.

Search terms came from /mnt/project-files/1808-eruption/notes/eruption_clue_search_terms.md (read once), translated into Italian and French for the Milan and Paris papers.

## Sources and routes
| Source | Covers | URL | Route | Readable |
|---|---|---|---|---|
| Giornale italiano 1809/1 (nos. 1–181, Jan–Jun 1809) | yes | https://www.digitale-sammlungen.de/en/view/bsb10506317 | MDZ IIIF search `api.digitale-sammlungen.de/iiif/services/search/v1/bsb10506317?q=` | yes |
| Giornale italiano 1809/2 (nos. 182–365, Jul–Dec 1809) | yes | https://www.digitale-sammlungen.de/en/view/bsb10506318 | same API (bsb10506318) | yes |
| Giornale italiano 1810 | needed for news from Asia | – | **not in MDZ or Europeana**. bsb10506319 is *Il Pungolo* 1860 | no |
| Moniteur universel 1809, 1810 | needed | – | **not at MDZ** (MDZ series ends with vol. 41, Jul–Dec 1808) and **not on IA**. IA has only 1800–04, 1812 Jan–Jun and the index volumes | no |
| Moniteur, Table 1799–1814 pt 1/2 | index | https://archive.org/details/lemoniteuruniver179918142pari | IA FTS with an identifier filter | yes |
| O Telegrafo Portuguez 1809 | Dec 1808 – Jun 1809 | https://archive.org/details/otelegrafoportug00unkn_0 | IA FTS | yes (00unkn has no OCR text) |
| IA full text, year filter 1809–1811 or 1809–1815 | books and serials | IA FTS `filter_map` | one term per call | yes |

## Results by clue

**1. Booms or cannon fire heard with no battle**
- Giornale italiano 1809/1, "detonazione":
  - Canvas 147: French blow up the powder magazines at S. Margherita near A Coruña on the 13th [Jan 1809], heard more than three leagues away. **Military.**
  - Canvas 324 (about Apr 1809): an earthquake "fu preceduta da una vivissima detonazione" ("was preceded by a very sharp detonation"). The district is not named in the snippet; probably Piedmont, since nearby canvases carry the Pinerolo/Luserna swarm. **Local seismic.**
  - Canvas 567: windows broken by artillery at Vienna. **Military.**
- Giornale italiano 1809/2, canvas 137 (about Jul 1809): a sudden blast "like artillery" inside a hill-top church during mass shook the building and shattered the windows. **Probably lightning.**
- IA FTS "détonations entendues" (1809–11): *Archives des découvertes et des inventions nouvelles*. One volume has "deux détonations successives qui furent entendues à plus de dix lieues" (two successive detonations heard more than ten leagues away). Another has "pendant plus de 90 secondes, des détonations semblables à celles du tonnerre" (for more than 90 seconds, detonations like thunder) and "Les épouvantables détonations de la montagne… arrivées jusqu'à la mer" (the mountain's dreadful detonations… reaching the sea). The series runs 1808–1839 and IA's 1809 dates are unreliable, so the event years are unknown. **Unresolved; probably meteorites or other volcanoes.** Items: archivesdesdcou14unkngoog, archivesdesdcou54unkngoog.
- Spanish "cañonazos oyeron mar" and "truenos subterraneos" (1809–15): no relevant hits (only Humboldt on Guanajuato). Portuguese "estrondo" in O Telegrafo Portuguez: 0 hits.
- **No unexplained booms at sea or in Asia found.**

**2. Ashfall or midday darkness**
- Giornale italiano 1809/1, canvas 428 (about Apr 1809): ash covered the Calabrian coast between Reggio and Scilla, attributed to Etna, March 1809 (reported in pass 1). **Etna.**
- Giornale italiano 1809/2, canvas 336 (about Aug–Sep 1809, from the *Corriere di Napoli*): **Vesuvius** opened a new vent to the SW, above the 1807 vent, with a large lava stream. It "gittò un immensa quantità di cenere" (threw out an immense quantity of ash), sand and stones, but weakly, so most fell in or near the crater. The text compares the eruption with that of 12–22 Aug 1682 and describes the "pino" (eruption column). **Vesuvius 1809, local.**
- All other "cenere" hits (9 in 1809/2, 6 in 1809/1) are towns burnt or bombarded.
- IA "pluie de cendres" (1809–11): 14 hits, all retrospective (79 AD, 1785, Sonnini's 1802–06 travels). "lluvia de ceniza": only Solís, *Conquista de México*. "chuva de cinza": 0 hits.
- **Nothing from the sea or from Asia.**

**3. Floating pumice**
- IA "pierre ponce" + mer (1809–11): Morelot 1809 describes pumice floating on the Baltic shores, a general statement. Sage, *Institutions de physique* (1811), describes a sea "couverte de pierre ponce" off the Cape of Good Hope. No ship or date appeared in the item-level search, so it is probably an older observation. **Unresolved.** "piedra pomez" (1809–12): dictionaries only. Giornale italiano "pomice": 0 hits.
- **Not found** for 1808–10.

**4. Night glow, fire or a new island**
- IA "isla nueva" (1809–12): Espinosa y Tello, *Memorias sobre las observaciones astronómicas* (1809). The "Isla Nueva" sits among the Bahamas positions (Providencia/Nassau, 25°N), so it is a charting matter, **not volcanic**.
- IA "nouvelle île" + volcan (1809–11): older events only (Santorini 1707, Terceira, Roggeveen 1722).
- Moniteur index: "new island discovered in the Pacific" (An XI and 1806), before the window.
- "Moluques volcan" and "Manila volcan" (1809–12): only geography books and earlier eruptions, e.g. Amboina 13 May 1784, a garbled *Annales des voyages* 1809 fragment on "Sorca" in the Moluccas, and Sonnini on a Bali volcano. **No Philippine, Moluccan or Javan eruption of 1808–10 found.**

**5. Earthquakes and sea anomalies**
- Giornale italiano 1809/1: a Pinerolo/Luserna (Piedmont) swarm on 27 Jan, the 15th [Mar or Apr] and at Cavour. A Naples astrologer's earthquake scare for 25 Nov [1808]. A quake on the night of the 4th/5th lasting 8–10 s with aftershocks, at canvas 621, about Jun 1809, the same page as the Etna "meteora".
- Giornale italiano 1809/2:
  - Düsseldorf, 5 Jun 1809: two shocks.
  - **L'Aquila / Abruzzo, Aug 1809 (canvas 256):** a slight tremor on 1 Aug at 2 a.m., stronger on the 2nd, then a very violent shock. About 1,500 undulatory shocks were counted at the foot of the Chiarina mountains. The report mentions haze lifting and "several unusual sky phenomena" around the shocks. It recalls 1705. **Local Apennine swarm.**
  - Carlsbad.
  - **Lisbon, letters of 27 Oct 1809:** a tremor the evening before at 9:55 p.m., which alarmed residents who remembered 1755.
  - Canvas 432: speculation that electric fluid produces "the same phenomena at distant points at the same time".
- **No sea withdrawal or tsunami reported.**

**6. Grey rivers:** nothing found (Italian terms not specifically tested beyond the above).

**7. Sulfur smell or acid fog:** not found (pass 1 covered caligine and nebbia; pass 2 "nebbia" in 1809/2 gave military fogs at Tholen, the Finnish coast and the Scheldt).

**8. Optical effects and lunar eclipses**
- Total lunar eclipses fell on 29/30 Apr 1809 and 23 Oct 1809. 1809 almanacs list them only as predictions: *Annuaire du Mont-Tonnerre* 1809 has "Le 29 avril, éclipse de lune, visible en Europe et Afrique". "Invisible à Paris" in *Mémoires … histoire ancienne du globe* t. VIII means below the horizon, not dark.
- Giornale italiano 1809/1 "luna" and "eclisse": no report of how the 30 Apr 1809 eclipse looked.
- **No observed dark-eclipse description found.** Halos and blue or green suns: not found.

**9. Knock-on effects**
- Giornale italiano 1809/2 "carestia": famine in Tyrol, Bohemia/Moravia (army), Turkish frontier and garrisons, all **war-related**. Also "la carestia che soffriva" Iceland (Danish report; the British took the island in 1809), a blockade famine. An editorial (canvas 453, late 1809) says "siamo minacciati dalla carestia" (we are threatened by famine), arguing against a jubilee.
- "gelo" in 1809/1: agricultural advice only.

**News of Asia and the Pacific to mid-1810 (Giornale italiano 1809/2 only; no 1810 volume reachable)**
- Batavia: a Dutch expedition prepared against the Sultan of "Solon/Solou" (Sulu?) (canvas 609, about Nov 1809). Canvas 355 in 1809/1: a Company ship arrived at Batavia.
- "Indie" (31 hits): East India fleet ships scattered or missing after a "terribile tempesta" off an island whose name is cut off (canvases 453 and 502, about Oct–Nov 1809). Bombay papers of 1 June: seven Company ships missing (canvas 686, about Dec 1809). The Madras army–government dispute (Fort St George, order of 1 May 1809). The Company's influence at Peking. **No volcanic, earthquake, darkness or ash report.**
- "Manilla": 0 hits.

## Bottom line
- **No non-veil clue to the 1808/09 eruption was found** in the reachable Italian, French and Portuguese sources for Oct 1808 – Dec 1809. This is a **weak-to-moderate negative**: keyword OCR search, snippet-level reading.
- Volcanic items found are all attributable elsewhere: Etna Mar 1809 (Calabrian ash, haze), Vesuvius Aug–Sep 1809 (new vent, ash near the crater), and the Abruzzo swarm Aug 1809.
- **Gaps:** Giornale italiano 1810 and the Moniteur, Journal de l'Empire and Gazette de France for 1809–1810 are not reachable. These are the columns where Asian and Pacific news of 1809–mid-1810 would appear.

## Browser leads
- Read the Giornale italiano page images, MDZ viewer: bsb10506318 canvases 256 (Abruzzo, with sky phenomena), 336 (Vesuvius), 453/502 (East India fleet storm) and 609 (Batavia); bsb10506317 canvases 324 and 621.
- Giornale italiano 1810: look for another holder (Braidense, Biblioteca digitale lombarda, Internet Culturale).
- Moniteur 1809–1810 and Journal de l'Empire: Gallica or RetroNews, in a browser.
- *Archives des découvertes et des inventions nouvelles*: check which year archivesdesdcou14unkngoog and archivesdesdcou54unkngoog cover, for the "détonations" passages.

# Extension strand file: D_ext.md
## D_ext: wider window (Oct 1808 – Jun 1810), eruption indicators beyond the veil — missions, Asia/Pacific, India, shipping

Worker notes, 16 Oct 2026. Everything is **OCR only**: IA full-text-search (FTS) snippets, the IA "inside.php" in-book search, or djvu.txt read through WebFetch. No page images were checked.

Terms came from notes/eruption_clue_search_terms.md (EN list, place names, long-s variants).

Method:
- The IA FTS endpoint takes `filter_map={"year":{"1809":"gte","1811":"lte"}}` for a year window, or `{"identifier":{ID:"inc"}}` for one item.
- Multi-word queries are AND, and OR does not work.
- The proxy rejects URLs longer than about 250 characters.
- archive.org rate-limited me with HTTP 429 twice: once on an advancedsearch query (first task) and once on the Naval Chronicle vol. 24 query for "ashes" (this task).

(Interim. The sections below are filled in as the work goes on.)

## Notes already in the project (checked first)
- **Naval Chronicle 21–23:** already searched for volcano, earthquake, crater, Etna, Azores and pumice (vol. 21), per nonIberian_fulltext_pass2.md. Known items: Etna ashfall of 27 Mar 1809 (vol. 23, pp. 45–46); the Cape earthquake; the São Jorge eruption of 1808.
- **Asiatic Annual Register vol. 12** (`asiaticannualre02unkngoog`): searched before only for earthquake, volcano and 1809, which found the Calcutta shocks of 1 Apr and 13 May 1810 (pp. 546–547) and the Berhampore fish-kill of 22 May 1810. This task adds the terms below.

## 1. Sources and searches

| Source | Place / lang | Window | Human URL | Readable | Terms / method | Result |
|---|---|---|---|---|---|---|
| Baptist Magazine Jul 1809 | London / EN | letters up to ~Feb 1809 | https://archive.org/details/baptist-magazine-1809_1809-07_1 | djvu fetch failed (server error) | – | not read |
| Baptist Magazine Aug 1809 | " | " | https://archive.org/details/baptist-magazine-1809_1809-08_1 | yes, djvu (seems partial: the "Baptist Mission" section on p. 338 was not in the text) | all indicators | **nothing**; only a thunderstorm in the Timme narrative (undated) |
| Baptist Magazine Oct 1809 | " | " | https://archive.org/details/baptist-magazine-1809_1809-10_1 | yes, djvu (partial) | all indicators | **nothing**; no foreign letters. "Earthquakes" appears only in a piece on the ancient Philadelphia church |
| Baptist Magazine 1810 issues | " | – | – | **not on IA** (the series jumps from 1809 to 1812) | – | not available |
| Methodist Magazine vol. 33 (1810) | London / EN | yes | https://archive.org/details/methodistmagazin0033unse | yes, FTS + inside.php | earthquake, famine, volcano, 1809 | **Cape of Good Hope earthquake, 4 Dec 1809** (p. 223, see §2). "famine" is figurative ("a famine of the word"). volcano: 0 |
| Methodist Magazine vol. 32 (1809) | " | yes | https://archive.org/details/methodistmagazin0032john | FTS | volcano | only the "Account of the New Volcano in the Azore Islands" (São Jorge, May 1808; known) |
| Evangelical Magazine (London) 1809–10 | EN | yes | – | IA "evangelicalmaga…" Google scans checked: vol. 17 = 1839 and "17unkngoog" = 1847 | – | **London 1809–10 volumes still not identified on IA** |
| Missionary Magazine (Edinburgh) 1810 | EN | yes | – | not identified | – | not reached |
| Hagemeister, Neva journal (Hawaii, Jan–Mar 1809) | RU | yes | Tumarkin 1979, https://lir.byuh.edu/index.php/pacific/article/download/2406/2332/4580 | article read | – | the journal is unpublished. Shemelin's book (1816–18) reproduces Hagemeister's 1809 Hawaii data (per Tumarkin), but no online text was found. **not read** |
| Kaye, Life of Metcalfe vol. 1 (1854) | Punjab / EN | yes (Sep 1808–Apr 1809 mission) | https://archive.org/details/lifecorresponden01metcuoft | FTS | weather, earthquake | **nothing**; only routine hot- and cold-weather remarks |
| Buchanan (Martin, Eastern India, 1838) | Bihar/Bengal / EN | survey 1807–14 | https://archive.org/details/b33488320_0001 | FTS | 1809, fogs | generic climate text ("Dew and fogs in winter"); no dated 1809 event |
| Naval Chronicle vol. 24 (Jul–Dec 1810) | UK / EN | yes | https://archive.org/details/navalchronicleco24londiala | FTS + inside.php | volcano, earthquake, pumice, shock, noise; **ashes refused (HTTP 429)** | São Miguel (Azores) earthquake of 11–12 Aug 1810, letter on p. 398–399 ("a subterraneous noise was distinctly heard"). pp. 482–483: a cave or "caverns" narrative, explained in the text, not volcanic. pumice: 0. "bosom of a volcano" is a figure of speech |
| Naval Chronicle vols 22, 23 | UK / EN | Jul 1809–Jun 1810 | https://archive.org/details/navalchronicleco22lond ; https://archive.org/details/navalchronicleco23lond | FTS | pumice, ashes | vol. 22: pumice 0, ashes only in poetry. vol. 23: pumice 0, ashes = the known Etna 1809 account. **Nothing from the Eastern Seas** |
| Asiatic Annual Register vol. 12 | India / EN | 1810–11 | https://archive.org/details/asiaticannualre02unkngoog | FTS | eruption, pumice, explosion, famine; **ashes refused (HTTP 429)** | eruption 0, pumice 0, explosion only figurative or political. "famine": 3 garbled snippets ("apprehensions of famine", "prevalence of famine"), context and date unresolved |
| Asiatic Annual Register vol. 11 (1809) | India / EN | yes | https://archive.org/details/asiaticannualre03samugoog | FTS | pumice, explosion | pumice 0. explosion = fear of a gun-room powder explosion (a ship) |
| Bombay Courier on IA (~1,083 issues, `india.history.resource.*`, subject "Bombay Courier") | Bombay / EN | **starts 5 Jan 1811** (titles run 1811–1842) | e.g. https://archive.org/details/india.history.resource.2647 | yes | advancedsearch | **new free resource, but after the window**. Useful for retrospective 1811 news (Java campaign); not yet listed in the project register |
| IA FTS, all texts, years 1809–1811/12 | – | – | https://archive.org/search?query=pumice&sin=TXT | yes | see §3 | no in-window Asian or Pacific event report |

## 2. What the sources say (OCR only)
- **Methodist Magazine 1810, p. 223.** Heading: "a Letter from a Minister of the Gospel, near the Cape of Good Hope, dated Dec. 23, 1809". Text: "Dec. 4, between 10 and 11 o'clock; there was an Earthquake here. The noise was tremendous; and, by the shaking of the ground, many houses were damaged in the [walls]". This is the known Cape Town earthquake of 4 Dec 1809, and it is tectonic. It is a duplicate of the "Cape quake" in Naval Chronicle 23. **Not an eruption signal.**
- **Naval Chronicle 24, pp. 398–399.** A letter correcting newspaper reports of the earthquake at St Michael's (São Miguel) "on the 11th and 12th of August [1810]". It mentions "a subterraneous noise" and damaged mud cottages. Azores, tectonic or volcanic and local, outside the target region.
- **Global FTS hits that are not new evidence:**
  - Weekly Entertainer, 20 Aug 1810: "shower of ashes and volcanic stones" refers to Vesuvius, 1794.
  - Monthly Magazine, Nov 1811: the Sabrina volcano, Azores, June 1811.
  - Universal Magazine, Apr 1812: a voyage from Manila in 1797.
  - "like the firing of cannon" (1809–11): Valentia's travels of 1802–06, encyclopedias and Wesley.
  - Ternate hits concern the British capture of 31 Aug 1810.
  - Every "Sumbawa"/Tomboro eruption hit in the 1809–12 window is mis-dated metadata for 1815 texts.

## 3. Global FTS runs (years 1809–1811 or 1809–1812)
| Query | Hits | In-window Asian/Pacific event? |
|---|---|---|
| pumice | 766 | no (top 45 are mineralogy, voyages, encyclopedias) |
| "shower of ashes" | 39 | no (Pliny, Vesuvius, Etna, Iceland, Java general) |
| pumice Batavia | 228 | no |
| volcano Amboyna | 161 | no |
| "new island" volcano | 57 | no (Azores Sabrina 1811, Santorini) |
| eruption Ternate | 304 | no (capture of Ternate 1810) |
| volcano Manila | 80 | no (1797 voyage; Sabrina) |
| ashes deck ship 1809 | 0 | – |
| "quantities of pumice" | 38 | no (Iceland, Cook, encyclopedias) |
| Sumbawa | 30 | no (only mis-dated 1815 Tambora texts) |
| "like the firing of cannon" | 16 | no |

Not run, for budget: Celebes, Moluccas, Philippines, "floating pumice", "explosions like cannon", "dark as night", blood-red sky, halo, eclipse, frost, famine 1810.

## 4. Findings and verification strength
- **No eruption indicator from Asia, the Pacific, the Indian Ocean or the missions was found for Oct 1808 – Jun 1810** in anything read here: no booms, ash on decks, pumice rafts, darkness, glow, new island or coloured sun.
- The only geophysical items are known tectonic events, the Cape earthquake of 4 Dec 1809 and São Miguel in Aug 1810. Both are already in the project.
- The negatives are **weak to moderate**: keyword FTS on OCR, 5 snippets per item, some partial djvu texts, two searches refused for rate limiting, and the London Evangelical Magazine and Missionary Magazine not located.

## 5. Browser-only leads
- Asiatic Annual Register vol. 12, "famine" context: https://archive.org/details/asiaticannualre02unkngoog (search "famine" in the BookReader).
- The "ashes" searches refused by rate limiting: Naval Chronicle 24 https://archive.org/details/navalchronicleco24londiala and AAR vol. 12 (above).
- Bombay Courier 1811 issues: https://archive.org/search?query=subject%3A%22Bombay+Courier%22 . Retrospective shipping news; check the Jan–Jun 1811 issues for "pumice", "ashes" and "volcano".
- Shemelin, *Журнал первого путешествия россиян вокруг земного шара* (1816–18), which carries Hagemeister's 1809 Hawaii notes: Russian State Library or NLR in a browser.
- London Evangelical Magazine vols 17–18 (1809–10): Google Books or HathiTrust (blocked here).

---

# Second extension (16 Oct, ~14:30–15:30 UTC): window from 1 Sept 1808, Indian Ocean first

Reason: the veil may have reached Colombia after other places (11 Dec 1808 is only the first Bogotá report). All strands reran for veil and eruption signs 1 Sept – mid-Dec 1808, and for delayed news of that period printed through Aug 1809. All OCR only.

## Summary
- **Nothing found for Sept – mid-Dec 1808 anywhere reachable.** India (Asiatic Annual Register vols 10–11, Seton-Karr pp. 226–230, Henry Martyn, Mrs Sherwood, Baptist Magazine Rangoon/Serampore letters), Cape (Theal vol. 6), NSW (HRA vol. 6), East Indies station (Naval Chronicle 20–21), Mauritius (Flinders letters online, none for Sept–Dec 1808): no dim/red sun, haze, red twilights, ash, pumice or detonations. Weak negative (Seton-Karr is selective; 5-snippet search cap; one rate-limited search).
- **Delayed Asian news in European and US papers Jan–Aug 1809** is naval/political only (Sémillante raids, HMS Laurel taken off Île de France, Drury's Macao expedition, Daendels at Batavia).
- **European skies Sept–Nov 1808** (German papers, Giornale italiano 1808, Moniteur Jul–Dec 1808): nothing; "atmosfera tutta infocata" at Constantinople ~Aug 1808 is a thunderstorm.
- **Bentley, Salem, 8–12 Nov 1808** dark spell with sun "very red" on the 9th: no corroboration (Ballard, Hill, IA papers, Medical Repository), no forest-fire reports found; unexplained regional event, likely smoke or overcast, not the veil. Holyoke descriptions file would test it (fetch fails here).
- **Correction:** the "Manila earthquake" and "détonations" items in *Archives des découvertes et des inventions nouvelles* are from the 1820s (Manila Oct 1824); archive.org's 1809 date for the series is wrong.
- **New source:** Calcutta Monthly Journal on archive.org from vol. 15 (Jul–Oct 1809, dli.bengal.10689.13876; negative); vols 13–14 (Jul 1808–Jun 1809) not found.


# Sept–Dec 1808 strand file: A_sepnov1808.md
## Strand A: Sept–Nov 1808 European sky observations, and delayed Indian Ocean / West Pacific news printed Jan–Aug 1809

Worker notes, 16 Oct 2026. 34 tool calls. Route: the open DDB newspaper Solr index, read through WebFetch (method in A_nordic_central.md §0).

**Everything is OCR only.** I saw no page images. A summariser sits between me and the text, and it caps quotes at about 125 characters.

- Human search: https://www.deutsche-digitale-bibliothek.de/search/newspaper?query=Morgenr%C3%B6the&fromYear=1808&toYear=1808
- Human viewer (pattern inferred, not tested): https://www.deutsche-digitale-bibliothek.de/newspaper/item/<ITEM-ID>, where ITEM-ID is the id before `-FILE`/`-fulltext`.

## (a) Local sky observations in German papers, 1 Sept – 30 Nov 1808

| Query | Hits | Result |
|---|---|---|
| Heerrauch OR Höhenrauch OR Haarrauch | **0** | none |
| "Sonne blaß"~8 | **0** | none |
| "Sonne bleich"~8 | **0** | none |
| "Sonne roth"~4 OR "rothe Himmel"~3 | **0** | none |
| "trockener Nebel"~2 OR Lufterscheinung* | **0** | none |
| Abendröthe OR Morgenröthe | 7 | **All 7 read; all figurative.** Morgenblatt 7 Sep (Krummacher hymn); Baierische National-Ztg 19 Oct and Berlinische Nachrichten 12 Nov (Hetsch's Resurrection painting: "Der Moment dieser Scene ist die Morgenröthe" [the moment of this scene is the dawn]); Altonaischer Mercurius 25 Oct and Münchener politische Ztg 4 Nov ("die kurze Morgenröthe des schönsten Tages … für Preußen" [the brief dawn of the finest day … for Prussia], Berlin, 22 Oct); Morgenblatt 3 Nov (St Gallen speech); Elegante Welt 14 Nov (essay on mysticism). |
| "Nebel Sonne"~6 | 1 | Allgemeine Zeitung 25 Oct 1808, Weimar, hunt of 6 Oct [1808]: "Nach manchen rauhen Nebel- und Regentagen erschien heute die Sonne im vollen Glanz" [after many raw days of fog and rain the sun appeared today in full brightness]. This is a **real observation of an ordinary, clear sun**: autumn fog and rain, then sunshine. No veil. |

**Verdict (a):** No sign of a pale, red or silvery sun, Höhenrauch, dry fog or unusual twilights in the German press for Sept–Nov 1808. Two limits: Fraktur OCR quality is unknown, and the "Sonne blaß OR bleich" OR-query was too long for the proxy, so I ran it as two separate queries.

## (b) Delayed foreign news printed 1 Jan – 1 Sep 1809

| Query | Hits | Read | Result |
|---|---|---|---|
| (Ostindien OR Madras) AND Asche | 8 | 1 | Berlinische Nachrichten 14 Jan 1809: "Ostindien" appears in a reprinted *Times* essay on Spain's colonies, and "Asche" refers to the **fire of the Landschaftshof at Hannover on ~6 Jan 1809**. Noise. 7 unread (mostly fires or potash, judging by the pattern). |
| (Batavia OR Java OR Ceylon) AND Erdbeben | **0** | – | none |
| (Manilla OR Canton) AND Erdbeben | 2 | 2 | Both are the Zürich letter of 29 Dec 1808: **avalanches in Canton Uri and at Lake Lucerne on the night of 12 Dec 1808**, over 50 houses buried. The writer asks "Sollte etwa ein Erdbeben oder irgend eine andere electrische Bewegung dabei zum Grunde liegen?" [Could an earthquake or some other electrical motion be the cause?] and notes a very low barometer. "Canton" here means a Swiss canton. Not Asian. |
| (Ostindien OR Ceylon) AND Vulkan | **0** | – | none |
| (Ostindien OR Bengalen) AND Finsterniß | **0** | – | none |
| (Cap OR Ostindien) AND feuerspei* | **0** | – | none |
| "Isle de France" AND Asche | 2 | 2 | (1) Hamburgische neue Ztg 8 Mar 1809: the cruise of the frigate *Sémillante* (Capt. Motard) from Île de France, including Sept–Oct 1806 events and **a prize taken off Ceylon on 15 Mar 1808**, with raids in the Bay of Bengal. "Asche" occurs only in "Potasche" (potash from Tenerife). (2) Altonaischer Mercurius 3 Apr 1809, London, 11 Mar: Cape dispatches dated **December [1808]** report a frigate action "auf der Höhe von Isle de France" [off Île de France]; HMS *Laurel* (22 guns) was taken by a French frigate (this is the *Canonnière*, Sept 1808), 8 killed and about 20 wounded. In the same issue, "Asche" is the Drury Lane fire (24 Feb 1809). **No natural phenomena in these Indian Ocean naval reports.** |
| Batavia AND Sonne | 1 | 1 | Münchener politische Ztg 18 Jan 1809: "Arrac de Batavia" at a wine auction, and the "Sonne" inn. Noise. |
| ((Mauritius OR "Isle de France") AND Sonne) and (Ostindien OR Bengalen OR Madras) AND Asche | – | – | URL over the proxy limit; replaced by the shorter queries above. |

**Verdict (b):** Indian Ocean news did reach the German papers by Mar–Apr 1809, via London and the Cape: naval actions off Île de France in Sept–Dec 1808. It contains **no report of ash, darkness, a strange sun, detonations or eruptions**. I found nothing from Batavia, Java, Manila or Canton about natural events. Shipping columns proper (arrival lists) cannot be isolated by keyword. This is a browser task: Hamburgischer Correspondent / Börsen-Halle "Schiffs-Nachrichten", Jan–Aug 1809.

## Browser leads

1. The 7 unread "(Ostindien OR Madras) AND Asche" pages, ids in the API at `q=plainpagefulltext:((Ostindien%20OR%20Madras)%20AND%20Asche)&fq=publication_date:[1809-01-01T00:00:00Z%20TO%201809-09-01T00:00:00Z]`. Dates: 5 Jan, 21 Mar, 23 Mar, 28 Mar, 8 Jun, 6 Jul and 14 Jul 1809.
2. London papers reporting the HMS *Laurel* / Île de France action, and the Cape dispatches of Dec 1808. The ships' logs of HMS *Laurel* and other Cape-station ships for Sept–Dec 1808 could hold weather and sky notes from the SW Indian Ocean.

# Sept–Dec 1808 strand file: B_sepnov1808.md
## Strand B: Sept–Nov 1808 recheck (Bentley's November dark days; East Indies news Jan–Aug 1809)

Worker notes, 2026-10-16. **Everything is OCR only.** Sources are archive.org full-text search snippets, per-item `inside.php` search, and dohistory transcriptions. I viewed no page images. Each verbatim quote is capped at about 125 characters by the fetch tool.

**Access limits:**
- IA's year filter accepts `{"year":{"1808":"inc"}}` for a single year.
- Two archive.org calls were rate-limited (HTTP 429) and not retried: the 1808 newspaper query for "sun", and Bentley "heat". Both are **untested**.
- Bentley's full text cannot be read from start to finish here, because WebFetch truncates the 2 MB OCR file. So "read Sept–Dec 1808 in full" was done as a keyword sweep of leaves 439–467 (1 Sep – late Dec 1808). It was not a continuous reading.

## 1. Bentley, Salem: Sept–Dec 1808 (archive.org `diaryofwilliambe03bent`, leaves 439–467)

**Leaf map:**
- "September 1 [1808]" is leaf 439; "October 1, 1808" is leaf 447; "November 1 [1808]" is leaf 453.
- Leaf 455 reports the election "votes of Yesterday"; the Massachusetts election was Monday 7 Nov.
- "18. Sunday" (18 Dec) is leaf 465; "January 1, 1809" is leaf 467.

**Weather and sky entries found:**

| Date (1808) | Leaf | OCR text |
|---|---|---|
| 6 Sep | 440 | "This day I was at Spring pond & a heavy thunder shower came on at sundown. We found the wild grapes ripening." |
| 20 Sep | 443 | "We had great changes in the weather. Sunday was hot & so was Monday… This morning we had several thunder showers, the glass having been 50 hours within doors above summer heat. At noon the wind shifted into the N. E. & we had a cold September storm so that the glass fell 20 degrees. Last evening the lightning burnt a barn in Gloucester." |
| **10 Nov** | 456 | "The thunder & lightning of Tuesday was accompanied with great darkness much resembling the Dark day & the appearances in the N. W. were similar. The shower fell perpendicularly without any appearance of a rising cloud & the rain & thunder lasted not one quarter of an hour. Yesterday, almost the whole day, the sun was very red & for a few moments seemed to break out, but the weather continued dark & is in that state till the present moment." |
| **12 Nov** | 456 | "The weather for the past week has been uniformly dark with heat at times & with little moisture of the Atmosphere. Such has been the weather since Tuesday when the weather began to assume the appearance so memorable on the dark day of 1780." |

So the dark spell ran from Tuesday 8 Nov to at least 12 Nov 1808, with a very red sun on 9 Nov.

**Searched for and not found** in leaves 439–467: smoke and smoky (0 hits in the volume), fires and woods, hazy (0 in the volume), fog, sky, "Indian summer" (0), drought, Aurora, volcano (0), ashes, pumice.

There is no sign of a red sun, haze or darkness again in late Nov or Dec 1808. The volume's other "sun" and "red" hits for those months are unrelated.

## 2. Corroboration, 5–15 Nov 1808

| Source | Place | Result |
|---|---|---|
| Martha Ballard diary (dohistory) https://dohistory.org/diary/1808/11/18081102_print.html , https://dohistory.org/diary/1808/11/18081112_print.html | Hallowell, Maine (≈230 km NNE of Salem) | 8 Nov "Clear part of the day"; 9 Nov "Clear part of ye day… Thunder at night"; 10 Nov "Clear part of ye day, raind at night"; 11 Nov "Clear"; 12–13 Nov "Cloudy"; 14–15 Nov rain and snow. **She records thunder on the night of 9 Nov but no darkness or red sun.** Her entries are terse. |
| Leonard Hill register https://archive.org/details/meteorologicalch00hill | East Bridgewater MA (≈55 km S of Salem) | Nov 1808 summary "Month wet". **No "dark", "red", "smoky" or "hazy"** on the 1808–09 pages (scan pp. 23–34). The OCR is garbled, so day-level reading was not possible. |
| IA newspapers 1808 (Alexandria Daily Gazette; Pittsburgh Weekly Gazette; no 1808 issues of Newport Mercury or Kentucky Gazette appeared in the results) | VA, PA | "smoke" (27 hits): Sep–Dec 1808 hits are smokehouse adverts and battle smoke. "darkness" (15): figurative or garbled. "dark" (120; top 50 reviewed): horse colours and a "dark conspiracy". "atmosphere" (6): figurative. "weather" (66; visible part): European war news, plus 3 Nov 1808 "blight… the state of the weather during the… harvest". "fires" (21): adverts, garbled. "woods" (55): no fire or smoke. **No dark day, red sun, smoke or forest fire reported for Nov 1808.** Query "sun" was rate-limited. |
| *Medical Repository*, Nov 1808–Jan 1809 issue (https://archive.org/details/sim_medical-repository_november-1808-january-1809_6) and Feb–Apr 1809 issue (https://archive.org/details/sim_medical-repository_february-april-1809_6) | New York and elsewhere | "autumn" and "November" searches turned up no report on the weather of autumn 1808. Feb–Apr 1809, p. 49: "The weather through the last season, or 1808, has not been marked by any peculiar changes" (writer's place not identified from the snippet). Ricketson's NY winter report begins with December. **No mention of darkness or smoke.** |
| Web search for New England darkness or forest fires, Oct–Nov 1808 | — | Nothing found. |

## 3. Verdict on 8–12 Nov 1808

**Probably a local or regional weather event, possibly with smoke, and unexplained in detail. Not a stratospheric veil.**

- **For a regional event:**
  - It lasted about 5 days.
  - "heat at times & … little moisture" fits a warm late-autumn spell.
  - Bentley compares it twice to the 1780 Dark Day, which was wildfire smoke.
  - The darkness came with a short thunder shower "without any appearance of a rising cloud".
- **Against a widespread smoke pall or veil:**
  - Ballard in Maine (partly clear on 8–10 Nov) and Hill in E. Bridgewater (no dark or red) do not corroborate it.
  - None of the 1808 papers on IA mention it.
- **Wildfire smoke is plausible but unproven:** no report of forest fires in Maine, New Hampshire, Canada or New York in Oct–Nov 1808 was found in the reachable sources.
- **The timing argues against a link to the eruption veil:** this is ~1 month before the Bogotá onset (11 Dec), and Bentley records nothing similar in Dec 1808 – Feb 1809.
- Classification: **"unexplained, probably regional smoke and/or overcast; not corroborated."**

## 4. US papers printed Jan–Aug 1809: news from the East Indies, India and the Cape about Sept–Dec 1808

**Queries** (IA, newspapers, 1809): Calcutta (25 hits), Bengal (20). From round B_ext (1809–10): Canton (161), Manilla, Batavia, Otaheite, Sandwich, volcano, ashes, pumice, eruption, earthquake, darkness.

**What the Jan–Aug 1809 East Indies items contain:**
- Admiral Drury's expedition from Bengal and Penang to Macao. Alexandria 26 May 1809: "Canton, we learn that an expedition fitted out at Bengal and Penang, under the direction of admiral Drury". Also Newport Mercury 27 May 1809 and Kentucky Gazette 18 Jul 1809.
- Captures of US ships "from Manilla to Canton" (Alexandria 26 May 1809).
- The *Calcutta* (56 guns) naval actions (Alexandria 13–15 Jun 1809; Newport Mercury 17 Jun 1809).
- Bengal cotton and cargo notes (Alexandria 11 Jan and 2 Mar 1809).
- Brig *Resort* from Canton via Batavia (Newport Mercury 18 Feb 1809).
- A ship that "left Canton 20th March" (Pittsburgh 6 Sep 1809).

**Result: not found.** None reports ash, a dim sun, haze, a volcano or darkness in Asia or at sea in Sept–Dec 1808. The only volcano news in 1809 US papers is the São Jorge (Azores) May 1808 letter and Etna 1809.

**Limit:** IA lacks the Salem, Boston, NY and Philadelphia marine lists, where captains' remarks were printed first. These are in Readex / *America's Historical Newspapers* (library access only).

## 5. Browser leads

- Holyoke weather descriptions for 8–12 Nov 1808 at Salem, the best independent check: https://crudata.uea.ac.uk/cru/data/holyoke/holyoke.descript.dat
- Bentley leaf 456, page image: https://archive.org/details/diaryofwilliambe03bent/page/n455
- Readex: Salem Gazette, Salem Register, Essex Register and Columbian Centinel, 9–19 Nov 1808, for any "dark day" or smoke item; marine lists Jan–Aug 1809.
- Rerun the IA fts query `sun` with filter `{"year":{"1808":"inc"},"collection":{"newspapers":"inc"}}` (rate-limited here).

# Sept–Dec 1808 strand file: C_sepnov1808.md
## Strand C: European sky observations 1 Sep – 30 Nov 1808, and delayed news from Asia and the Indian Ocean

Worker C, third pass, 2026-10-16. About 25 calls. All text is **OCR only**, read as search snippets summarised by WebFetch. No page images were seen.

## Routes
- Giornale italiano 1808: MDZ bsb10506316, https://www.digitale-sammlungen.de/en/view/bsb10506316 . Erfurt-congress news (late Sep – Oct 1808) sits at canvases 1125–1132, so Sep–Nov 1808 lies at about canvases 1100–1450.
- Giornale italiano 1809/1: MDZ bsb10506317, for news arriving later.
- Moniteur universel, Jul–Dec 1808: MDZ bsb10487403, https://www.digitale-sammlungen.de/en/view/bsb10487403 . OCR is poor.
- archive.org full-text search with a year filter of 1808–1810.

## 1. European sky observations, Sep–Nov 1808
| Search | Result |
|---|---|
| Giornale italiano 1808: caligine, crepuscolo | 0 hits (caligine also 0 in pass 1) |
| Giornale italiano 1808: pallido | 3 hits: dyes, plant, calendar. Not sky |
| Giornale italiano 1808: atmosfera | 7 hits. Canvas 933 (about Aug 1808, Constantinople): "In vari punti l'atmosfera sembrava tutta infocata, cosicchè a Costantinopoli…" ("in several places the atmosphere seemed all aglow, so that in Constantinople [people thought a great fire had broken out in the suburb]"). The same snippet continues with rain, lightning and thunder, so this is a **thunderstorm, not a twilight glow**. Other hits: balloon physics, Rochefort air, the *Journal de l'Empire* on bird flight |
| Giornale italiano 1808: nebbia, meteora, fenomeno (pass 1) | Lister fjord fog in Mar 1808, meteorite falls, a Monza storm. Nothing for Sep–Nov |
| Moniteur Jul–Dec 1808: crépuscule | 0 |
| Moniteur Jul–Dec 1808: atmosphère | 2 hits, medical and figurative |
| Moniteur Jul–Dec 1808: brume | 1 hit, at sea near the Hebrides (a ship from Batavia) |
| Moniteur Jul–Dec 1808: phénomène | 21 hits: optics (Malus), medicine and other non-sky items |
| Moniteur Jul–Dec 1808: brouillard (pass 1) | Lakes Erie/Ontario climate, Finland war fog, Spanish bulletin "brouillard épais… depuis trois jours" (ordinary wet fog) |
| Moniteur Jul–Dec 1808: tremblement, secousse | La Tour/Pinerolo shocks (July), a shock on 26 Sep 1808 at 3:15 p.m., and a quake toppling chimneys (canvas 538, place not in snippet). All local |
| IA "soleil pâle" 1808–10 | 5 hits: allegory, poetry, burning-glass experiments. No observation |
| IA "soleil rouge" 1808–10 | 4 hits: literature, prism optics, botany. No observation |
| IA "sol rojo" 1808–10 | 0 |
| IA "brouillard sec", calina, "niebla seca", "sol opaco", "sole pallido" (pass 1) | no 1808 observations |

**Result: no European report of a dim or pale sun, red twilight, haze or dry fog for 1 Sep – 30 Nov 1808 was found.** This is a weak-to-moderate negative based on keyword OCR search.

## 2. Delayed foreign news printed to Aug 1809 about Sep–Dec 1808 events in Asia, the Indian Ocean and the Cape
| Search | Result |
|---|---|
| Moniteur Jul–Dec 1808: Manille | 1 hit (canvas 650): the French frigate *Canonnière* arriving from Acapulco with about 4 million piastres. Trade only |
| Moniteur Jul–Dec 1808: Batavia | 15 hits: Daendels arriving at Batavia on 1 Jan 1808, troop morale on Java, Danish Asiatic Company ships reaching Bergen (14 Aug) and Batavia (10 Mar). **No natural events** |
| Giornale italiano 1809/1: Filippine, Manilla | Canvas 258 only: a retrospective on the frigate *Sémillante* (1805–06). Not relevant |
| Giornale italiano 1809/1: "Isola di Francia" | none found on the first result page (656 "Francia" hits; not exhausted) |
| Giornale italiano 1809/1: Batavia (pass 2) | a Company ship arriving at Batavia. 1809/2: an expedition against the Sultan of "Solou" |
| IA "Manille tremblement" 1808–10 | Hits in the *Archives des découvertes et des inventions nouvelles* (IA date 1809): "Tremblement de terre aux îles Philippines… la ville et les faubourgs de Manille éprouvèrent une commotion des plus violentes", "le plus violent… depuis l'année 1796". The item's own text dates it to **October 1824**, so IA's 1809 metadata is wrong for this series. **Not relevant.** This also casts doubt on the series' "détonations" hits from pass 2. Other hits: Manila 1797 (Guignes), Acapulco and Guatemala quakes |
| IA "Filipinas terremoto" 1808–10 | Guatemala quakes, the 1810 Gazeta del Gobierno de México (unnamed quake), dictionaries. No Philippine event |
| IA "Isle de France" cendres 1808–10 | 17 hits: figurative ash, minerals, a comet seen at Port Napoléon (Isle de France) in 1808. **No ash, darkness or volcanic event** |

**Result: no delayed report of an eruption, ashfall, darkness or earthquake in the Philippines, Moluccas, Java, Mauritius or the Cape for Sep–Dec 1808 was found** in these sources. The Moniteur for Jan–Aug 1809 and the Giornale italiano for 1810 are not reachable, which leaves a real gap.

## Browser leads
- Moniteur Jan–Aug 1809 (Gallica or RetroNews), foreign news columns: "Isle de France", "Batavia", "Manille".
- Giornale italiano 1808, canvases about 1100–1450 (Sep–Dec 1808): read for any "Osservazioni meteorologiche". MDZ viewer bsb10506316.

# Sept–Dec 1808 strand file: D_sepdec1808.md
## D_sepdec1808: early veil and eruption signs, 1 Sep – mid-Dec 1808, Indian Ocean / western Pacific (worker notes, 16 Oct 2026)

Everything is **OCR only**: IA full-text search (FTS) snippets with an identifier filter, the IA in-book search (inside.php, which returns every match with a page number), or the RMG/SLNSW web pages. No page images were checked.

Terms came from notes/eruption_clue_search_terms.md. For each item I used veil terms (hazy, haze, fog, smoke, sun, sky, sunset, weather) and eruption terms (volcano, ashes, pumice, explosion, earthquake).

**Reruns.** Several of these sources were searched before for the old window (Dec 1808 – mid 1809) and with old terms:
- Asiatic Annual Register (AAR) vols 10–11 (asiatic_annual_register_scan.md)
- Seton-Karr vol. 4 (volcano, earthquake, atmosphere)
- Theal vol. 6 (earthquake, volcano, atmosphere, smoke, weather, sun, drought)
- HRA vol. 6
- Naval Chronicle vols 20–21 (volcano, earthquake, ashes, Azores, pumice)
- Martyn and Sherwood (my first pass)

They were rerun here with the Sept–Dec 1808 focus and the veil terms.

## 1. Sources and results

| Source | Place | Sept–Dec 1808 coverage | URL | Terms (this pass) | Result |
|---|---|---|---|---|---|
| AAR vol. 10 (for 1808), `asiaticannualre04unkngoog` | India, Penang, at sea | yes (chronicle) | https://archive.org/details/asiaticannualre04unkngoog | hazy, haze, fog, smoke, sun; sunset refused (HTTP 429) | "hazy": 5 snippets, all from the log of the San Fiorenzo–Piémontaise action, **March 1808** (calm and hazy, 8–10 Mar). haze 0, fog 0, smoke 0. "sun": flags at half-mast "until sun-set", "At sun set" (Penang arrival), and similar. **Nothing for Sept–Dec 1808** |
| AAR vol. 11 (for 1809), `asiaticannualre03samugoog` | " | early-1809 news | https://archive.org/details/asiaticannualre03samugoog | hazy | only the known Persian Gulf gale haze of Nov 1809. Negative |
| Seton-Karr, *Selections from Calcutta Gazettes* vol. 4, `selectionsfromca04seto` | Calcutta | yes, but selective: editorial items for 1 Sep – 22 Dec 1808 are only **pp. 226–230** | https://archive.org/details/selectionsfromca04seto | hazy (0); inside.php: weather (32 matches, none on pp. 226–230), sky (6, none in the 1808 pages), 1808 (page map) | **Negative for Sept–Dec 1808.** The 1808 editorial selection is thin: 1 Sep, 8 Dec, 22 Dec |
| Henry Martyn, *Journal and Letters* vol. 2, `journalandlette02wilbgoog` | Dinapore | yes (1808 letters at pp. ~138–235) | https://archive.org/details/journalandlette02wilbgoog | hazy 0, fog 0, sky (one proverb, p. 291); inside.php "weather": pp. 162, 176, 192, 249, 259, 308, 316, 364, 392 | **No weather remark in Sept–Dec 1808.** Out of window: p. 308 (letter of ~1 May 1810, Cawnpore) "I am willing to hope the extraordinary weather is the cause of my pulmonary weakness"; p. 316 (28 May 1810) "The weather dreadfully oppressive, night and day". Both are hot-season remarks, not diagnostic |
| *Life of Mrs Sherwood* (1857), `lifeofmrssherwoo00sher` | Dinapore/Berhampore | yes, but the narrative is undated | https://archive.org/details/lifeofmrssherwoo00sher | fog 0, sunset, sky, hazy, atmosphere | "sickly, hazy, burning evenings" (hot season); "a burning evening in June, when, after sunset…". **Negative** |
| Theal, *Records of the Cape Colony* vol. 6, `recordscapecolo09offigoog` | Cape | yes (to Dec 1808; Dec docs at pp. 423–487) | https://archive.org/details/recordscapecolo09offigoog | hazy 0; fog 1 | "vessels sailed with him and parted in a Fog off the Cape of Good Hope" (undated; ordinary). **Negative** |
| HRA ser. I vol. 6, `historicalrecord00v6aust` | NSW | yes (to Dec 1808) | https://archive.org/details/historicalrecord00v6aust | hazy 0, smoke 0, weather (5 routine snippets) | **Negative** (the snippet cap means late-1808 "weather" lines may be unseen) |
| HRNSW vol. 6 (King and Bligh 1806–08) | NSW | yes | IA id not resolved (`historicalrecor00bladgoog` has 1893 metadata, probably vol. 2) | – | **not searched** |
| Naval Chronicle vol. 20 (Jul–Dec 1808), `navalchronicleco20londiala` | Letters from all stations | East Indies letters of ~Mar–Jul 1808 | https://archive.org/details/navalchronicleco20londiala | volcano 0; hazy 1 | "very hazy weather for several days": HMS Astrea, wrecked on Anegada, West Indies, **May 1808**. Negative for the East |
| Naval Chronicle vol. 21 (Jan–Jun 1809), `navalchronicleco21londiala` | East Indies letters of ~Jul–Dec 1808 | yes | https://archive.org/details/navalchronicleco21londiala | hazy | 5 snippets. p. 100 is de Courcy at Corunna, Jan 1809 ("Hazy weather rendering the Cossack obscure"); the others are European actions. **No East Indies haze** |
| Flinders letters, RMG "Flinders Papers" (Mauritius) | Île de France | 1808 documents | https://flinders.rmg.co.uk/Documents3570.html?Year=1808 | read doc ID 121 (13 Apr 1808, endorsed 19 Sep 1808) and doc 27/41 (20 Jan 1808) | no weather or sky remarks. **No RMG document dated Sept–Dec 1808 is listed.** The private journal (SLNSW Safe 1/58; transcript files a008+) is robots-blocked (daily_journals_round2) |
| Baptist Magazine 1809 (India letters of late 1808) | Rangoon, Serampore | Chater letters of 12 Aug, 5 Sep and 29 Sep 1808; Ward 12 Jan 1809 | https://archive.org/details/baptist-magazine-1809_1809-12_1 | read in full in pass 1 | **no weather or sky content** |
| Methodist Magazine 1809 | (no India mission) | – | https://archive.org/details/methodistmagazin0032john | – | not applicable |
| **Calcutta Monthly Journal**, vol. 15 (Jul–Oct 1809), `dli.bengal.10689.13876` (new to the project) | Calcutta, Madras, Penang | no (vols 13–14 for Jul 1808 – Jun 1809 are not on IA) | https://archive.org/details/dli.bengal.10689.13876 | volcano 0, earthquake 0, hazy 3 (ships separating "in hazy weather near the Line"; routine) | negative. Vols 16–17 (1810) are also on IA: `dli.bengal.10689.11310`, `dli.bengal.10689.16610` |
| Global FTS, years 1808–1810 | – | – | – | "sun was obscured", "hazy Madras 1808", "sun appeared" hazy, "sun appeared" red 1808 | no Asian or Indian Ocean sky report for Sep 1808 – Mar 1809. The hits are Phil. Trans. reprints, European registers, and a dye experiment ("sun appeared of a deeper yellow", J. Nat. Phil. 24) |

## 2. Findings
- **Not found.** In the material reachable here there is no report from India, Burma, Mauritius, the Cape, NSW, the East Indies station or ships of a dim, pale or red sun, haze, dry fog, red twilights, ash, pumice or detonations for 1 Sep – mid-Dec 1808.
- Strength of the negative: **weak**.
  - Seton-Karr prints only about four pages for Sept–Dec 1808.
  - AAR vol. 10's "sunset" search was refused by rate limiting.
  - FTS shows at most 5 snippets per item.
  - Flinders's journal, the Sydney Gazette, HRNSW vol. 6 and the Calcutta Monthly Journal vols 13–14 were not reached.

## 3. Browser-only leads
- *Calcutta Monthly Journal* vols 13–14 (Jul 1808 – Jun 1809). Not on IA; look in the BL or DLI. Other DLI items under the title (https://archive.org/search?query=title%3A%28calcutta+monthly+journal%29) were not dated in the listing; check them for vols 13–14.
- Flinders private journal, Sept–Dec 1808: SLNSW transcript http://acms.sl.nsw.gov.au/_transcript/2013/D17745/a008.html and later files (robots-blocked here).
- AAR vol. 10, search "sunset", "red" and "sky" in the BookReader: https://archive.org/details/asiaticannualre04unkngoog
- HRNSW vol. 6: identify the IA copy, or use the SLNSW/Internet Archive "historicalrecor0Xwalegoog" items, which have no volume metadata.
- Sydney Gazette, Sep–Dec 1808: https://trove.nla.gov.au/newspaper/title/3 (Anubis-blocked here).
