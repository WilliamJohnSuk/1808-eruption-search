---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: ship_logs
date: 2026-11-02
---

# Royal Navy logs worldwide for the eruption window: what survives at Kew and where the ships were (started 2 Nov 2026)

Thread: Decide on the Kew logbook order. William (2 Nov 2026, 05:35 UTC) asked whether Claude could research the availability of records "from the entire fleet during that period", "everywhere in the world", for example ships near Lima and Colombia where the veil was seen (Caldas, Bogotá, 11 Dec 1808).

**Verification:** every catalogue statement below is TNA Discovery API catalogue text fetched 2 Nov 2026 through Claude's cloud container's web fetch (summarised by the fetch tool, so short descriptions only) [text]. Fleet-history statements are web text [text, web] unless marked [inference]. Bash has no route to Discovery or archive.org in this session (proxy 403); only the web fetch tool works.

## 1. How the Kew logs are catalogued (what limits a fleet-wide inventory)

- ADM 51 (captains' logs) and ADM 52 (masters' logs) pieces are composite volumes catalogued by **ship name and date range only** ("Captains' logs, including: COMUS (1808 May 17-1809 June 30). JAMAICA (1808 June 1-1809 June 30)...", ADM 51/1952). No station, captain or position is given. A fleet-wide inventory therefore needs (a) a list of ships in commission by station for winter 1808/09 and (b) one catalogue lookup per ship.
- Station lists: Steel's *Original and Correct List of the Royal Navy*, 1 Jan 1809, is on archive.org (steelslistroyalnavy1809jan), with a station column, but its OCR is too garbled to read station by station through the fetch tool [text, OCR, checked 2 Nov]. Page images could not be fetched from Claude's cloud container.
- Positions: item-level ADM 1 letter descriptions (place and date of each captain's letter) remain the free way to place a ship, as in B73.
- Earlier sweep (catalogue_sweep_1808-09.md part 1, 16 Oct) already lists logs for the South America (Rio/Plate), Leeward Islands, Cape and East Indies stations.

## 2. Pacific coast of South America (Lima, Guayaquil, Pacific New Granada)

- Discovery, ADM department, Sep 1808-Jun 1810: "Callao" returns only charts (ADM 352/591, /593, /596; SVY A/t34); "Lima" returns no letter from the Pacific coast (24 hits, none an RN ship on that coast); "Carthagena" returns no RN letter from Cartagena de Indias in the window [text].
- Wikipedia, *British Pacific Squadron*: "It was formed in 1813 during the War of 1812" [text, web]. Wikipedia, *South America Station* (formed 1808 at Rio): no Pacific deployment before 1812 mentioned [text, web].
- Reading: **no Royal Navy log is likely to exist for the Pacific coast of South America in Dec 1808-1810** [inference from the absence above; not proven]. The St Andrews thesis by Ortiz-Sotelo (1998), *Peru and the British naval station (1808-1839)*, would settle it; its PDF is refused by the site's robots rule (U147).
- Alternatives near Lima and Bogotá: Spanish Navy (Real Armada) ships of the Callao and Cartagena stations (logs, if they survive, would be in Spanish naval archives; not checked); British and American whalers off Peru and Chile (catalogue sweep part 2; American whaling logs already negative in the register); the Caribbean side, below.

## 3. Caribbean coast of New Granada (Jamaica station)

- The Jamaica station ships worked the Spanish Main; Bogotá is c. 650 km inland of Cartagena [inference, geography]. Admiralty letters from Port Royal, Jamaica in Jan-Apr 1809 name HMS Avon, Shark, Garland (ADM 1/2609/76-77), Bacchus, Pelican (ADM 1/2705/15) and Meleager (ADM 354/235/110) [text]. Logs exist for e.g. HMS Jamaica (ADM 51/1952, 1 Jun 1808-30 Jun 1809; ADM 51/2506, 1 Jul 1809-19 Nov 1810) [text]; the others not yet looked up.
- **Correction (2 Nov, same day):** HMS *Jamaica* (24) is listed in Steel's Navy List of 1 Jan 1809 at **Newfoundland**, not on the Jamaica station, and a letter of 23 Jan 1809 has her at Plymouth with a convoy (ADM 1/2078/145). Her logs are not a Caribbean source. Jamaica-station ships are in section 6.
- A Caribbean log would be a veil check (did the sky haze reach 10-18°N in Dec 1808-Feb 1809?), like Phaeton's for the South China Sea, not a source check [Claude's judgement].

## 4. Status (superseded by sections 5-7)

Partial. Not yet done: station lists for Jamaica, Leeward Islands and East Indies/China in Dec 1808; per-ship ADM 51/52 lookups beyond those in the 16 Oct sweep; positions from ADM 1 letters.

## 5. Steel's Navy List, 1 January 1809: ships by station (read from page images, 2 Nov 2026)

Source: *Steel's Original and Correct List of the Royal Navy*, 1 Jan 1809 (archive.org steelslistroyalnavy1809jan; PDF downloaded by William to books/navy_lists/ on his Mac, 2 Nov 2026; U148). Ship pages 3-20 of the list (PDF pages 5-22) were read as page images at 150-250 dpi [page image]. Only ships marked C (in commission) were taken. For William's "priority ones" first, ships on home, European, Baltic and Mediterranean stations were left out except on the first four pages. The result is in `data/rn_stations_steel_1809-01-01.csv`: **233 ships on distant stations**.

| Region | Ships (this transcription) | Steel's own "Statement of the distribution" (p. 21 of list) |
|---|---|---|
| East Indies (incl. Bombay, and 3 ships at Spithead/Plymouth "for East Indies") | 38 | 34 "East Indies, and on the Passage" |
| Jamaica station (incl. Melpomene "Vera Cruz") | 36 | 34 |
| Leeward Islands / West Indies (incl. convoys to the West Indies) | 80 | 114 "At the West India Islands, and on the Passage" |
| Brazil / South America (incl. Elizabeth "with sealed orders", Olympia off the River Plate) | 18 | in 24 "North & South America & Newfoundland" |
| North America, Bermuda, Newfoundland | 39 | (same line) |
| Cape of Good Hope | 13 | 15 "Cape of Good Hope and southward" |
| Coast of Africa, St Helena, Madeira | 5 | 5 "Coast of Africa" |
| New South Wales | 3 | (not separate) |

Steel counts 565 ships at sea in all and 831 in commission. The West Indies shortfall (80 against 114) means some rows were missed or are counted by Steel among convoys; the East Indies, Jamaica and Cape counts agree within 2-4 [comparison, Claude].

**Limits** [Claude's judgement]: the list gives each ship's station as known in London at the end of December 1808. For the East Indies that news was 4-6 months old: Greyhound is still listed though wrecked off Luzon in Oct 1808 (U112), and St Fiorenzo is already back at Sheerness. It gives stations, not positions. **No Royal Navy ship is listed anywhere in the Pacific or on the west coast of the Americas**; the nearest are New South Wales (Porpoise, Lady Nelson, Integrity) and Brazil/River Plate. This supports section 2.

Corrections to the 16 Oct catalogue sweep from the list: Marlborough (74) is on the **Brazils** station (the sweep excluded her as "probably home waters"); Monarch (74) also Brazils; HMS Jamaica is Newfoundland (above).

## 6. East Indies station: surviving captains' logs at Kew (ADM 51) for the window

Discovery catalogue text, searched ship by ship in ADM 51 with dates 1 Jun 1808-30 Jun 1810, 2 Nov 2026 [text]. "Covers core?" = covers some of 1 Nov 1808-31 Mar 1809. Ships already in the 16 Oct sweep or B73 are marked *. Positions are not yet checked except where noted (B73).

| Ship (guns) | Log(s) found | Covers core? | Note |
|---|---|---|---|
| Albion (74)* | ADM 51/1876, 1 Jan 1807-5 Jun 1809 | yes | India, then home 1809 |
| Culloden (74)* | ADM 51/1866 (5 Jul 1808-31 Jul 1809); ADM 52/3738 | yes | Pellew's flagship, Madras/Bengal |
| Russel (74)* | ADM 51/1912, 1808 | to 31 Dec 1808 | Drury's flagship, Macao Sep-Dec 1808 |
| Powerful (74) | last ADM 51 log ends 18 Feb 1808 | no | Drury's flag per Steel; no log found for the window |
| Belliqueux (64)* | ADM 51/2048 (from 6 Nov 1808); ADM 52/4425 | yes | Bombay Jun 1809 (B72) |
| Lion (64) | ADM 51/1997, 19 Feb 1808-18 Feb 1810 | yes | position unknown |
| Piedmontaise (50) | ADM 51/2613 (undated); ADM 51/2638 from 26 Oct 1809 | unclear | check ADM 51/2613 dates |
| Cornwallis (38/44)* | ADM 51/2046 | yes | Arabian Sea side (B72) |
| Dover (38)* | ADM 51/4051, 51/2278 | yes | Macao after Sep 1808 |
| Phaeton (38)* | ADM 51/1952; ADM 52/3853, 52/4229 | yes | Nagasaki-Penang (B73) |
| Sir Francis Drake (38)* | ADM 51/2826 | yes | west of Java (B73) |
| Bombay (38) | ADM 51/1929 (3 Jun 1808-25 May 1809), 51/2033 | yes | may be the 74 of the same name; check |
| Dedaigneuse (36) | none found after 9 May 1808 | no | |
| Doris (36) | ADM 51/1930 (25 Mar 1808-24 Mar 1809); 51/2043 from 25 Jun 1809 | yes | Cole; Penang Apr 1809, then Manila/Macao with Psyche (B73) |
| Caroline (36)* | ADM 51/2242, 29 Jul 1808-21 Jan 1812 | yes | |
| Chiffonne (36) | ADM 51/1865 ends 1 Sep 1808 | no | |
| Psyche (36)* | ADM 51/2666; ADM 52/3787, 52/4576 | yes | Malabar, then Philippines 1809 (B73) |
| Blanche (36) | ADM 51/1898 (18 Jul 1808-3 Feb 1809); 51/2185 (4 Feb 1809-15 Mar 1811) | yes | position unknown |
| Modeste (36)* | ADM 51/2552 | yes | Bay of Bengal Jan 1809 |
| Clorinde (36) | ADM 51/2188, 16 Nov 1808-31 Dec 1811 | yes (on passage) | sailed from Plymouth for the East Indies |
| Fox (32)* | ADM 51/2389, from 15 Nov 1808 | yes | |
| Wilhelmina (32) | ADM 51/1936 (16 Oct 1808-13 Jan 1809; 14 Jan 1809-15 Dec 1812) | yes | position unknown |
| Terpsichore (32) | last log found ends 26 Aug 1808 | no | gap |
| Cornelia (32) | ADM 51/2045, 6 Oct 1808-22 Jun 1813 | yes (on passage) | sailed from Spithead for the East Indies |
| Pitt (28) | ADM 51/4078 "Pitt (Armed)", 27 Nov 1807-15 Dec 1810 | yes | identity with Steel's Pitt (ex Kai Khusroo) to check |
| Samarang (18) | ADM 51/2631, 7 Dec 1808-4 Mar 1812 (and to 23 Nov 1808) | yes | gap 24 Nov-6 Dec 1808 |
| Procris (18) | ADM 51/2854 (from 23 Nov 1808) | yes | |
| Rattlesnake (16) | ADM 51/2763, 7 Jul 1808-26 Mar 1810 | yes | |
| Barracouta (18) | ADM 51/2162, 24 Sep 1807-27 Dec 1811 | yes | |
| Dasher (18) | ADM 51/1859 ends 14 Oct 1808; ADM 51/2268 undated | unclear | |
| Sapphire (18) | ADM 51/2056 (undated); next from 3 Mar 1810 | unclear | |
| Victor (18) | last log found ends 5 Sep 1808 | no | |
| Diana (14, gun-brig) | ADM 51/2418 has "DIANA (Brig) 3 Apr 1807-3 Oct 1809" | probably | identity to check |
| Jaseur (12), Sea Flower (14) | none found | no | |
| Greyhound (32) | lost Oct 1808 (U112) | no | |

**Result:** about 25 East Indies ships have a captain's log at Kew that covers some of Nov 1808-Mar 1809. Which of them were east of Java (the candidate region) is not yet known except for those placed in B73; the next step is the free ADM 1 letter check for Lion, Blanche, Doris, Wilhelmina, Caroline, Fox, Procris, Rattlesnake, Barracouta, Samarang, Pitt and Bombay.

## 7. Next steps (as agreed with William, 2 Nov 2026)

1. Free position checks (ADM 1 letters) for the East Indies ships above; rank by distance from the candidates.
2. Same log lookup for the Cape, Brazil, Jamaica and Leeward Islands ships (`data/rn_stations_steel_1809-01-01.csv`).
3. Home-waters ships for the full world map (blog data).
4. Then William chooses page checks at Kew for the priority areas (£9.92 each).

## 8. East Indies ships placed from Admiralty letters (free check, 2 Nov 2026)

Method: item-level descriptions of ADM 1 captains' letters on TNA Discovery, searched by ship ("HMS X"), captain and place (Madras, Prince of Wales Island, Port Cornwallis, Malacca, Macao, China, Bengal, Drury), letters Sep 1808-Mar 1810 [text, catalogue descriptions as summarised by the fetch tool]. Key letters: **ADM 1/1806/129** (Ferrier, Albion, Table Bay, 21 Jan 1809, with "particulars" of the squadron as of late Oct 1808); **ADM 1/1940/54** (Heathcote, Lion, Penang, 4 Apr 1809); **ADM 1/1654/26** (Campbell, Nassau, Downs, 8 Sep 1809); **ADM 1/1547/245** (Byng, Belliqueux, Bombay, 14 Jun 1809); **ADM 1/1770/9** (Edgell, Cornelia, at sea, 16 Sep 1809); **ADM 1/2335/28** (P. B. Pellew, Plymouth, 4 Oct 1809); **ADM 1/1549/11** (Byng, 24 Feb 1810); **ADM 1/1548/116** (Bremer, Rattlesnake, 10 Mar 1810). Wikipedia for Procris [text, web].

| Ship | What the letters say (dates) | Where in the core window (1 Nov 1808-31 Mar 1809) | Distance to candidates |
|---|---|---|---|
| Russel (Drury's flag) | left Malacca c. 20 Sep 1808 with troops for Macao | Macao/South China Sea Nov-Dec 1808; her ADM 51 log ends 31 Dec 1808 and Jan-Jun 1809 is a gap | far (veil only) |
| Dover | to follow Russel to Macao (letter of Oct 1808 particulars) | probably Macao/South China Sea [inference] | far (veil only) |
| Diana (gun-brig, Lt Kempthorne) | seized the American schooner Topaz at Macao (date not given) | Macao [date unverified] | far |
| Phaeton | Nagasaki Oct 1808; Penang 22 Jan 1809 (B73) | South China Sea Nov-Dec 1808 | far (veil only) |
| Lion | Madras Aug 1808; at Penang 3-4 Apr 1809 with Doris, Blanche, Wilhelmina; crew made "two China voyages in four years" (ADM 1/1940/187); St Helena Jul 1809, home Dec 1809 | possibly escorting the China fleet through the South China Sea early 1809 [inference, not stated]; Penang 4 Apr 1809 | far |
| Doris, Blanche, Wilhelmina | all at Port Cornwallis, Penang, 3 Apr 1809 (scurvy survey); Doris then to Manila and Macao with Psyche (B73) | Doris at Madras 9 Oct 1808; Nov 1808-Mar 1809 not stated; Penang by 3 Apr | Penang is c. 2,500-3,500 km from the eastern candidates |
| Psyche | Malabar coast Dec 1808-Feb 1809; Manila/Macao Apr-Oct 1809; Surigao 1809 (B73) | west of India | in the Philippines Apr-Oct 1809 (extended window): **closest of all** |
| Procris | off Batavia 14 Jul 1809; Indramayu, Java, 30 Jul 1809 (Wikipedia) | not known | Java north coast in Jul 1809 (extended window), c. 700 km W of Agung |
| Culloden (Pellew), Fox | left Madras for Penang 24 Oct 1808 to await the China fleet; Culloden at St Helena 8 May 1809, home Jul 1809 | Penang / Straits of Malacca Nov 1808-early 1809 [inference] | far |
| Modeste | took the Jena in the Bay of Bengal 10-12 Oct 1808; Bay of Bengal Jan 1809; later in China; left Penang 20 Aug 1809 with Cornelia and Clorinde | Bay of Bengal | far |
| Terpsichore | cruising the Bay of Bengal Oct 1808; leaking | Bay of Bengal | far; and no log found for the window |
| Albion, Powerful | left Madras/Bombay Oct 1808; at the Cape Dec 1808-Feb 1809; home May 1809 | southern Indian Ocean, then the Cape | far |
| Caroline, Chiffonne, Cornwallis, Belliqueux | Bombay and the Persian Gulf, 1809 | Arabian Sea / west India | far |
| Cornelia, Clorinde | outward from England (Clorinde at Plymouth 25 Dec 1808); Bombay Jun 1809; Penang-Malacca Strait Aug 1809 | on passage in the Atlantic | far |
| Rattlesnake | Bremer sent a "log of the ship's proceedings, July to December 1808" with his letter of 31 Dec 1808 (ADM 1/1548/8); at Madras Oct 1809 | not stated | note: a copy log sits inside ADM 1/1548/8 |
| Belliqueux, Sir Francis Drake | Nicobars, Andamans and Acheen (Sumatra) Oct-Dec 1809 | Bombay side in the core window | far |

**Reading** [Claude's judgement]: on the free evidence, **no East Indies ship is placed east of the Straits of Malacca and south of the China coast in Nov 1808-Mar 1809**. The squadron was split between Bombay and the Gulf, Madras and the Bay of Bengal, Penang, and Drury's Macao expedition. The ships nearest the candidate region in the core window were those in the South China Sea (Russel, Dover, Phaeton, perhaps Lion and Diana), 1,500-3,000 km from the Philippine and Moluccan candidates: useful for the haze, not for the source. In the extended window, Psyche (and Doris) in the Philippines Apr-Oct 1809 and Procris on the Java coast Jul 1809 come closest.

**Revised ranking of Kew logs for the East Indies** (cost about £9.92 per page check plus £1.52 per image):
1. Psyche master's log ADM 52/4576 (13 Apr-13 Oct 1809), Philippines: unchanged top choice (B73).
2. Doris captain's log ADM 51/2043 (from 25 Jun 1809) and ADM 51/1930 (to 24 Mar 1809): a second ship on the same Manila/Macao cruise, and Nov 1808-Mar 1809 for the core window.
3. Dover ADM 51/4051 or 51/2278 and Russel ADM 51/1912 (to 31 Dec 1808): South China Sea in Nov-Dec 1808, for the veil's onset.
4. Lion ADM 51/1997: only if a China passage in early 1809 is confirmed.
5. Procris ADM 51/2854: Java coast Jul-Aug 1809.

## 9. Post Office packets (asked by William, 2 Nov 2026)

The Falmouth packets were the **British Post Office's** mail ships (179 tons each), not a Portuguese service, though the Lisbon route and the Brazil route (opened 1808, after the Portuguese court moved to Rio) carried much Portuguese mail. Steel's Navy List of 1 Jan 1809, p. 22, "Monthly account of the packets", lists **30 packets** with route and sailing dates [page image]; transcribed to `data/packets_steel_1809-01-01.csv`.

In the core window: **Brazil** Walsingham (sailed 14 Jul 1808), Princess Elizabeth (9 Aug), Townshend (10 Sep), Windsor Castle (10 Dec), Queen Charlotte (30 Dec / 1 Jan 1809); **Jamaica** Carteret (13 Sep), Duke of Kent (12 Oct), Prince of Wales (8 Nov), Mary (18 Dec); **Leeward Islands** Francis Freeling (26 Sep), Prince Adolphus (30 Oct), Princess Mary (8 Dec), Cornwallis (30 Dec); **America** Chesterfield, Manchester, Princess Amelia, Snake; plus Mediterranean, Lisbon and Corunna boats. Arrival and return dates for the Brazil boats from R. Frajola's compilation "1808-1850 Falmouth-Brazil" (rfrajola.com; from Lloyd's List, newspapers and Steel's) [text, web]; e.g. Townshend Rio 1 Dec 1808, Falmouth c. 13-16 Jan 1809; Windsor Castle Rio 1 Mar 1809; the Duke of Marlborough was taken by a French brig-corvette on 18 Nov 1808.

**Logs.** The only packet log for the window known to survive is Townshend's, Rio to Falmouth 1 Dec 1808-13 Jan 1809 (NMM NAI/3/17), already read through CLIWOC (hazy daily 10 Dec 1808-9 Jan 1809 along 30°W; weak, single observer). The Post Office archive at The Postal Museum, London, series POST 43, includes "packet boat log books, voyage record books" (AIM25 description) but is not itemised by year online; POST 39/41 hold the packet reports from 1807. Whether any 1808-09 logs survive there is unknown (U149).

## 10. Portuguese archives equivalent to Kew

Already covered by the lusophone strand (16 Oct; notes/lusophone.md, notes/iberian_logs_round2.md): Arquivo Nacional da Torre do Tombo; Arquivo Histórico Ultramarino (AHU: Timor caixa 4, 1790-1818, catalogue lead not read; Macau papers on the frigate *Ulysses*, Macau 19 Mar 1809 to Rio 25 Nov 1809); Arquivo Histórico da Marinha (Lisbon; its códices index has no *diários náuticos* for 1808-09); Arquivo Nacional and the navy archive in Rio. The AHU items were not on the unavailable list and are now U150.

## 11. Access to ANRI (Jakarta) for U78-U80 (2 Nov 2026)

ANRI public-services page and SOP no. 130/2025 on the LARISSA service, read through the fetch tool [text]: registered users (foreigners verify with a passport) can request a search of static archives by theme and period online at www.larissa.anri.go.id; ANRI assigns an archivist, uploads what is found with a PNBP fee, the user pays the ANRI treasurer account, and the copies are delivered as digital files by download link (download within 7 days). Standard time about 17 days. The request asks for a research permit (*ijin penelitian*); whether a foreign private researcher can satisfy that without an Indonesian research permit is not stated [unverified]. Reproduction requests are also accepted by email, PPID or SIKS with a research form, ID and fee. Reading room Mon-Fri 08:00-15:00. U78 status changed to "requires online request"; U79 and U80 follow U78's route.

## 12. Indonesian-language search for local archive researchers (2 Nov 2026)

Asked by William. Three web searches in Indonesian (jasa penelusuran arsip ANRI; jasa peneliti arsip Belanda VOC / penerjemah arsip kolonial; penerjemah bahasa Belanda kuno / transkripsi paleografi) [text, web]. **We found no advertised paid service for searching or copying ANRI's colonial archives in these.** Leads only (contact is William's decision; nothing drafted):
- Universitas Padjadjaran (Bandung), History programme: course "Bahasa Belanda Arsip I & II" trains students to read and translate VOC and Netherlands-Indies archival Dutch; lecturers Prof. Kunto Sofianto and Budi Gustaman, M.A. [course page, text]. A possible route to a trained student assistant [suggestion].
- ProZ.com profile 1392463: Dutch-Indonesian translator, Universitas Indonesia BA, 16 years, EUR/USD 0.05-0.08 per word, sample from a history dissertation on colonial Batavia; no stated archive-visit or handwriting service [profile, text].
- ANRI itself has in-house transliterators (its own VOC letter transliteration and translation publications) [text], which supports using LARISSA (section 11) rather than a private intermediary.
- DPAD DIY (Yogyakarta regional archive) opinion piece by Hendrikus Franz Josef: few Indonesian researchers read archival Dutch [text]; context for why such services are rare.

## 13. Dutch navy ship journals 1808-09 (free finding-aid check, 2 Nov 2026)

Asked by William. Finding aids read as text through the fetch tool [catalogue text; summarised by the fetch tool, not page images].
- **Nationaal Archief 2.01.29.01**, Departement van Marine 1795-1813 (Hingman 1890): no ship journals listed. Nearest items are inv. 267, fragments of letters from sea officers Nov-Dec 1808, Jan, Mar, May 1809, and inv. 268, Jul-Dec 1809 (mostly European waters, not checked) [catalogue text].
- **NA 2.01.29.03**, Marine 1795-1813 Aanhangsel II (Bonder 1929): holds the period's surviving journals. East Indies journals run 1800-1806 only (Bato, Pluto, Arend, Phoenix, Vrede, Echo; Hartsinck's command journals 1804-06, inv. 124-126). The latest journal of any ship ends 1 Jun 1808 (inv. 131, frigate Gelderland, Norway). **No Dutch navy journal covers Nov 1808-Mar 1809 anywhere** [catalogue text].
- **NA 2.01.30** muster rolls 1795-1813: no East Indies ship after the Batavia depot 1806 (inv. 352); 1808-09 rolls are all home-water ships and flotillas [catalogue text].
- **NA 2.12.03** ship journals of the Ministry of Marine: begins 1813 [catalogue text].
- Why the gap [known history, not checked here]: the Dutch Indies squadron was destroyed or taken by Pellew's ships at Batavia roads (Nov 1806) and Gresik (Dec 1807), so in 1808-09 the Dutch had only small colonial craft in the archipelago, run from Batavia under Daendels.
- **The useful remainder is in Jakarta: ANRI Arsip Marine** (inventory 1695-1930, OCR text garbled): no. 38A harbour reports of ships arrived and departed 1808-1809, 38B idem 1809, 136 sea reports and passes 1809, 7 letters received by the vice-admiral 1809, 203 letters to lieutenant governor-general Buyskes 1808-09, 138-139 navy letters and reports to Daendels 1810, 245 letters 1808, 49 and 287 papers on the Portuguese ship *Madrugada* 1809 [catalogue text]. Harbour reports would give arriving masters' voyage accounts at Batavia in the window. Added as **U152** (LARISSA route as U78).

## 14. Atlantic stations: Kew captains' logs for the Jamaica, Leeward Islands, Brazil and Cape ships (T1, free check, 2 Nov 2026)

Method: TNA Discovery API, series ADM 51, date filter 1 Jun 1808-30 Jun 1810, four ship names per query. The per-ship dates come from the record descriptions [catalogue text]. These were extracted by a summarising fetch tool, so treat single dates as "check before ordering". A name match is not proof that the log is the same ship, because RN names were reused (hired vessels and the several *Elizabeth*s, for example). The table is `data/rn_logs_atlantic_stations_2026-11-02.csv`.

| Station (Steel 1 Jan 1809) | Ships | Log covers all of 1 Nov 1808-31 Mar 1809 | Part | None or undated |
|---|---|---|---|---|
| Jamaica | 36 | 20 | 6 | 10 |
| Leeward Islands (incl. convoys sailing Nov-Dec 1808) | 79 | 44 | 16 | 19 |
| Brazil (incl. Mutine, sailed 5 Nov 1808) | 17 | 14 | 1 | 2 |
| Cape of Good Hope | 13 | 8 | 4 | 1 |
| **Total** | **145** | **86** | **27** | **32** |

**What this means [inference]:** the Atlantic side is well covered. At least 86 ships have a captain's log for the whole core window. For timing the arrival of the veil or twilights on the Atlantic side, a handful of logs placed at known stations is enough:

- **Caribbean coast of New Granada** (nearest the Bogotá veil of 11 Dec 1808). Jamaica-station cruisers off Cartagena and the Main would be best, but positions are not checked. Candidates are *Polyphemus* (flag, ADM 51/1975), *Franchise* (no log found) and the small craft. An ADM 1/259-260-type check (Jamaica admiral's letters) would place them = T4 extension.
- **Rio de Janeiro / South Atlantic:** *Foudroyant* (Sidney Smith's flag; ADM 51/1875 to 24 Jan 1809, then ADM 51/1884) and *London* (ADM 51/1857). Both were at or near Rio [memory: squadron based at Rio 1808-09; not checked here].
- **Mid-Atlantic convoys:** *Gloire* (ADM 51/1875), *Satellite* (ADM 51/2006), *Pelorus* (ADM 51/1984) and *Subtle* (ADM 51/2864) sailed with the West India convoy of 15-16 Dec 1808. They were in mid-ocean at the same time as the packet *Townshend*, which logged haze from 10 Dec 1808. *Mutine* (ADM 51/1956) sailed for Madeira and Brazil on 5 Nov 1808. These are the best Atlantic logs for testing when the haze arrived.
- **Cape:** *Leopard*, *Nereide* (ADM 51/2590) and *Racehorse*. These are of interest for the southern-hemisphere twilight onset.

Masters' logs (ADM 52) were not searched for these stations. The East Indies table (section 6) remains the priority for the eruption region itself.

## 15. Ready-to-use instructions: Kew page check (T17) and ANRI LARISSA request (T20) (2 Nov 2026)

William places both requests and pays for them himself. Nothing here has been submitted. Fees are from TNA's fees page as read on 28 Oct 2026 [text], and the ANRI process is from fleet notes section 11 [text].

### 15.1 Kew page check: Psyche master's log (first choice)

1. Open https://discovery.nationalarchives.gov.uk/details/r/C2533193 (ADM 52/4576, "Masters' logs, including: Prothee ... Psyche (1809 Apr 13-1809 Oct 13) ..."). Sign in with the same TNA account used for RC8585845.
2. Click **"Request a page check"** (wording on the page may differ slightly), then choose **digital copy**.
3. Paste this into the instructions box:

   > Please page-check the master's log of HMS Psyche in ADM 52/4576, entries dated 13 April 1809 to 13 October 1809 only (the volume also holds Prothee, Puissant and Pultusk; please exclude those). I am researching recorded weather, sky and sea conditions in the Philippines and the South China Sea in 1809. Digital images, please. Catalogue: https://discovery.nationalarchives.gov.uk/details/r/C2533193

4. Pay the page-check fee (**£9.92**, non-refundable once it has started). Expect a costed quote in about a week [William, 28 Oct]. At the Cornwallis rate of 2.5 days per A3 image, six months would be about 75 images, roughly **£115** at £1.52 each [calc]. That is a guess, because masters' logs can be denser.
5. When the quote arrives, export the order page as a PDF into `archives/` as before. Claude will then advise whether to buy all of it or only part.

**Optional second page check (Doris, same cruise plus the core window).** Doris ADM 51/1930 (https://discovery.nationalarchives.gov.uk/details/r/C4459986), 1 Nov 1808-24 Mar 1809, and ADM 51/2043 (https://discovery.nationalarchives.gov.uk/details/r/C4459987), 25 Jun-31 Dec 1809. Use the same wording, with "captain's log of HMS Doris" and those dates. Each record needs its own £9.92 check.

### 15.2 ANRI LARISSA request covering U78, U79, U80 and U152

1. Register at https://larissa.anri.go.id. A foreigner verifies identity with a passport scan.
2. Choose the archive search service (*layanan penelusuran arsip statis*). The form asks for a theme, a period and the purpose. It may ask for a research permit (*ijin penelitian*). If it does, state that this is private historical research for a non-commercial publication and ask whether copies can be supplied without a permit. Whether that works is unknown (section 11).
3. Paste this request (English, then Indonesian; the Indonesian is Claude's translation [suggestion]):

   > Request for digital copies, period August 1808 to August 1810, for research on an unidentified volcanic eruption of 1808-09 in eastern Indonesia (records of earthquakes, explosions, ashfall, darkness, pumice at sea, unusual skies or sea waves). Items: (1) Arsip Banda no. 13, day register of Banda and outposts, 1 Aug 1808-Jul 1809. (2) Arsip Ternate no. 59, day register 1809-1810, and nos. 114-116, enclosures Aug 1808-Aug 1810. (3) Arsip Timor, letters received 1808 and 1809 (duplicates), and May-Jun 1810. (4) Arsip Marine nos. 38A and 38B, sea and harbour reports (ships arrived and departed) 1808-1809, and no. 136, sea reports and passes 1809. If the full set is too large, please first send an estimate of the number of pages and the fee for each item.

   > Permohonan salinan digital, periode Agustus 1808 sampai Agustus 1810, untuk penelitian tentang letusan gunung api tahun 1808-09 yang belum teridentifikasi di Indonesia timur (catatan gempa bumi, dentuman, hujan abu, kegelapan, batu apung di laut, langit yang tidak biasa, atau gelombang laut). Arsip yang diminta: (1) Arsip Banda no. 13, dagregister Banda dan pos-pos luar, 1 Agustus 1808-Juli 1809. (2) Arsip Ternate no. 59, dagregister 1809-1810, serta no. 114-116, lampiran Agustus 1808-Agustus 1810. (3) Arsip Timor, surat-surat masuk 1808 dan 1809 (duplikat), serta Mei-Juni 1810. (4) Arsip Marine no. 38A dan 38B, laporan laut dan laporan pelabuhan (kapal datang dan berangkat) 1808-1809, serta no. 136, laporan laut dan pas 1809. Jika jumlahnya terlalu besar, mohon kirimkan terlebih dahulu perkiraan jumlah halaman dan biaya untuk setiap arsip.

4. ANRI assigns an archivist and uploads the result with a PNBP fee. William pays the ANRI treasury account. The files arrive by download link, which must be used **within 7 days**. Standard time is about 17 days (SOP 130/2025).
5. Save the downloads into `archives/ANRI/` and tell Claude. The bulk-scans rule applies afterwards.
