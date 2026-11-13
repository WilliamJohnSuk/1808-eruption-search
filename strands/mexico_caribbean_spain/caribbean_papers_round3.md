---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: mexico_caribbean_spain
date: undated
---

# Caribbean and circum-Caribbean newspapers and registers, Nov 1808 – Jun 1809 (round 3, strand "caribbean_papers")

Status: complete for this session (16 Oct 2026). Strand: Caribbean and circum-Caribbean newspapers, Nov 1808 – Jun 1809.

**Bottom line:** none of the five Caribbean and Guianas newspapers reachable here (Barbados, Nassau, Tobago, Demerara, Paramaribo) reports a dim, pale or silver sun, haze, unusual twilights, ash, pumice, detonations, a local earthquake, or a ship report of sky or sea anomalies from the Spanish Main or the Pacific, Dec 1808 – Jun 1809. Two caveats: the reading was of OCR text, and there are gaps (listed below). The same Barbados paper reported the St Vincent ash and haze of May 1812 in detail, which makes its silence in 1809 a meaningful though weak negative for the eastern Caribbean. Jamaica, the most important target (Kingston *Royal Gazette*, vol. 31 = 1809), is digitised only behind a subscription (AM Digital *Eighteenth Century Journals*); it is not in dLOC.

## Findings so far

### F1. Edwards, *History … of the West Indies*, vol. 5 (1819): the "impenetrable haze" is St Vincent 1812, not 1808. Open item now CLOSED.
- IA item b33287417_0005 (https://archive.org/details/b33287417_0005), searched with IA full-text search (inside.php on ia600101).
- "impenetrable haze": one hit, p. 102: "the sea and the island being wrapped in sulphureous clouds and impenetrable haze" (OCR: "‘thesea and the island being wrapped in sulphureous clouds and impenetrable haze.")
- The same section (pp. 98–102) covers West Indian volcanoes and an ash fall: p. 98 "Those in Guadaloupe and St. Lucia occasionally, though faintly, emit flames, and throw out ashes"; p. 100 "covered the woods, ridges and cane-pieces, with light grey ashes, resembling snow thinly strewed with dust" and "the ground bore a wintry appearance from the thick crust of fallen ashes"; p. 102 "the throwing up of a quantity of stones and ashes, which fell back into the abyss whence they came." This is the well-known account of the **Soufrière St Vincent eruption of 30 Apr – 1 May 1812** (Barbados ash fall). The wording is the standard 1812 narrative. The 1812 date itself was not confirmed by a direct snippet, because the WebFetch budget ran out first.
- All "31st December, 1808" hits (pp. 331, 340, 341) are dates of Acts of Parliament (trade acts, Turks Islands). They have nothing to do with the haze.
- p. 105: a town "threatened with destruction by the hostile element" in "June 1808" is a fire.
- **Verdict:** this is not an 1808–09 observation. Verification level: OCR text via WebFetch.

## Tool discovery: dLOC full-text search API WORKS through WebFetch (key method)
- The dloc.com and ufdc.ufl.edu web front ends are JavaScript shells, so WebFetch sees no results.
- The back-end API answers JSON: **https://api.dloc.patron.uflib.ufl.edu/** (root: https://api.dloc.patron.uflib.ufl.edu/?format=api). Useful endpoints:
  - `exactsearch?<field>=<value>&<field>=<value>`: fields include `fulltext`, `bibid`, `vid`, `title`, `publication_date` (a string, matched as a substring, e.g. "1809" or "January 1809"), `country`, `city`. Several fields can be combined, which ANDs them.
    - Example: https://api.dloc.patron.uflib.ufl.edu/exactsearch?fulltext=Carthagena&publication_date=1809 returned 3 hits.
  - `<BIBID>/<VID>/citation?format=api`: issue metadata, page-image names (0001.jpg …), page-text files (0001.txt) and the issue PDF name.
- Permanent issue link pattern: https://ufdc.ufl.edu/<BIBID>/<VID> (also https://dloc.com/<BIBID>/<VID>).
- Relevant bibids found:
  - **AA00047511**: *Barbados Mercury, and Bridge-town Gazette* (Bridgetown, 13.1°N). **104 issues dated 1809** (twice weekly), e.g. vid 00464 = 7 Jan 1809, 00474 = 11 Feb 1809, 00475 = 14 Feb 1809, 00484 = 18 Mar 1809, 00508 = 10 Jun 1809, 00509 = 13 Jun 1809. The same run, with page images, is the BL Endangered Archives project EAP1086: https://eap.bl.uk/collection/EAP1086-1-7 (1808) and https://eap.bl.uk/collection/EAP1086-1-8 (1809), monthly sub-collections such as EAP1086/1/8/6 = June 1809.
  - **AA00079433**: *The Royal Gazette, and Bahama Advertiser* (Nassau, 25.1°N). Has issues for 1809, e.g. vid 03644 = 21 Jan 1809.
  - AA00083639: *St. Croix Avis*. The issue seen (vid 02565) is from 1919; whether it covers 1808–09 is unknown.

- Notes on the API:
  - The `pagetext?term=<word>&bibid=<B>[&vid=<V>]` endpoint returns page-level hits with the OCR page text. Only the first ~6–7 hits are readable through WebFetch, and no pagination parameter was found (`page`, `format=json` and `conv_date=1809` fail). For a page-level quote, restrict by `vid`.
  - `exactsearch?fulltext=<word>&publication_date=1809` covers **all** of dLOC, so it searches the Barbados Mercury, the Bahama Gazette and every other title at once, at issue level.
  - Barbados Mercury vids for the window run from 00445 (1 Nov 1808) and 00454 (3 Dec 1808) to about 00512 (late Jun 1809). Bahama Gazette vids: Jan 1808 = 03534, 14 Sep 1808 = 03607, 18 Jan 1809 = 03643, so Dec 1808 is probably about 03630–03642.
  - The OCR is mediocre (18th/19th-century long s; garbled lines), so a nil return is a weak negative.
  - WebFetch quotes are limited to about 125 characters per quote by the summariser.

## Searches and hits in dLOC (exactsearch, all titles)
| # | Query | Hits | Assessment |
|---|---|---|---|
| 1 | fulltext=Carthagena, publication_date=1809 | 3: Bahama Gazette 21 Jan 1809 (vid 03644); Barbados Mercury 25 Nov 1809 (00556), 12 Dec 1809 (00561) | 03644 p. [1] is a reprinted Glasgow/Athenaeum commercial report ("Purchases … for Vera Cruz, Carthagena, and the Caraccas"). The Nov/Dec 1809 issues fall outside the window. No sky content. |
| 2 | fulltext=hazy, 1809 | 2: Henderson, *Account of the British Settlement of Honduras* (1809, UF00095343); Bahama Gazette 1 May 1809 (03673) | 03673 p. 3 is a reprinted British item: an earthquake at **Whitehaven** (Cumberland), "the atmosphere being very thick and hazy" after the shock. A British local quake, irrelevant. Henderson is a general description of Belize: see below. |
| 3 | fulltext=volcano, 1809 | 3: Bahama Gazette 18 Jan (03643), 8 Feb (03649), 29 Apr 1809 (03672) | 03649 p. [1] "NEW VOLCANO." reprints the US Consul at Fayal's letter (June 1808) on the **São Jorge, Azores eruption of May 1808** (already known). 03643: "the Africa, during the contest, was like a perfect volcano" (naval metaphor). 03672 not yet read. |
| 4 | fulltext=earthquake, 1809 | 3: Bahama Gazette 18 Jan (03643), 1 May (03673), 29 Jul 1809 (03698) | 03643 is a satirical "Political Catechism" on the Embargo ("O grab me … like an earthquake"). 03673 is Whitehaven. 03698 is Cobbett quoted in London news. All irrelevant. |
| 5 | fulltext=haze, 1809 | 0 | — |
| 6 | pagetext term=haze, Barbados Mercury (all years) | 7 | None in the window. **Calibration:** vid 00807 (12 May 1812) "an impenetrable haze hung over the sea", the St Vincent eruption of 30 Apr–1 May 1812, reported by the same paper. This shows the Barbados Mercury did report an ash or haze event when one reached Barbados. |
| 7 | pagetext term=hazy, Barbados Mercury (all years) | 25 (6 visible) | Visible: 1784, 1812-11-17 (sea weather), 1814, 1823, 1835. Combined with query 2 (no Barbados hit in 1809), there is **no "hazy" in any 1809 Barbados Mercury issue**. |
| 8 | fulltext=phenomenon, 1809 | 6: Henderson 1809; Bahama Gazette 8 Feb (03649, Azores), 31 May (03681), 12 Aug (03702), 16 Sep (03712); Barbados Mercury 16 Dec 1809 (00562) | 03681: a Bordeaux letter (Mar 1809) on plague among Spanish prisoners. 03702: the Bottineau "nauscopie" story (Réunion, 1784). Both irrelevant. |
| 9 | fulltext=ashes, 1809 | 13 (Barbados Mercury 22 Apr, 6 Jun; Bahama Gazette 15 Apr, 24 May, 17 Jun, plus later 1809) | Checked: Barbados 00494 "camp was reduced to ashes" (war); 00507 "Ashes (pot)" in a list of goods under a Napoleonic decree. These are fire and commodity senses; the other in-window hits are probably similar but were not all opened. |
| 10 | fulltext=eruption, 1809 | 1: Bahama Gazette 4 Nov 1809 (03726) | **Etna**, eruption of 27 Mar 1809, in an officer's letter dated Melazzo, 25 Apr 1809 (already known; N. hemisphere, small). |
| 11 | fulltext=darkness, 1809 | 10 | Read: 03653 (Finland front, Nov 1808: "darkness of the weather", the polar night); 03656 (night off Montserrat); 03660 (political metaphor); 03663 (poem); 03688 (Basque Roads, night). **03678 (Bahama Gazette 20 May 1809), p. 2**: the French squadron's escape from **Les Saintes, Guadeloupe, on the night of 14 [April] 1809**: "as in consequence of the darkness and haziness of the night our vessels had no idea of the enemy's intention" (OCR: "as m consequence of the darkness and haziness of the eight our vessels had no ideaot the ene enemy's my's enemy's intention"). See F2. |
| 12 | fulltext=atmosphere, 1809 | 4 | 00507 is an agricultural essay; 03702 is Bottineau; 03673 is Whitehaven. Irrelevant. |
| 13 | fulltext=Santa Martha (phrase) / Martha, 1809 | 0 / 3 | 03646 is a land sale (Martha Kempanu, Eleuthera). The rest are Dec 1809. Irrelevant. |
| 14 | fulltext=earthquake, 1808 | 4 (Bahama Gazette Mar, Aug 1808; Crusoe) | Before the window. |
| 15 | fulltext=hazy, 1808 | 6 (Surinaamsche Courant 23 Mar 1808; Bahama 16 Jul; Barbados 7 Jun, 5 Jul, 6 Sep 1808) | All before the window. Not opened. |
| 16 | fulltext=phenomenon, 1808 | 8, incl. Barbados Mercury 5, 12, 19, 22 Nov and 3 Dec 1808 | 00454 (3 Dec 1808) p. 3 is "this phenomenon" = Miss Byfield, the limbless artist in Lancashire. Irrelevant. The other Nov issues were not opened. |
| 17 | fulltext=aardbeving, 1809; nevel, 1809 | 0; 0 | Dutch terms; the Surinaamsche Courant OCR is poor. |
| 18 | fulltext=zon, Surinaamsche Courant, 1809 | 10 | 00277 (11 Mar 1809): "zon" is an OCR fragment of "zoals" in a legal notice. The paper is bilingual (Dutch and English). The other hits were not opened (low value). |
| 19 | country=Jamaica, 1809; country=Bermuda, 1809 | 0; 0 | **dLOC has no Jamaican or Bermudian newspaper for 1809.** |
| 20 | language=French, 1809 | 2 (Lettres édifiantes, Manioc) | No French Caribbean papers in dLOC for 1809. |

- **Surinaamsche Courant** (Paramaribo, 5.8°N; British-occupied 1804–16; bilingual Dutch/English), bibids AA00098217 (1809: **94 issues**, e.g. vid 00277 = 11 Mar 1809, 00290 = 29 Apr 1809, 00298 = 31 May 1809, 00305 = 24 Jun 1809) and AA00098218 (1808 issues, e.g. vid 00029 = 12 Apr 1808). This route gets round the Delpher block noted in dutch_papers_round2.md. **It is reachable from here.**

### F2. Night of 14–15 April 1809, Les Saintes (15.9°N, 61.6°W): "darkness and haziness of the night"
- Source: *The Royal Gazette, and Bahama Advertiser* (Nassau), 20 May 1809, p. [2] (pageorder 1), reprinting a naval letter on the escape of the French squadron (Troude) from the Saintes and the chase to the capture of the *d'Hautpoult* (17 Apr 1809). URL: https://ufdc.ufl.edu/AA00079433/03678 . Verification level: OCR text via the dLOC API, read through WebFetch; page image not seen.
- Excerpt (OCR, cleaned): "on the night of the 14th inst. at ten o'clock, the whole squadron cut their cables … one of them fired a broadside into the Neptune, which killed one man and wounded five … as in consequence of the darkness and haziness of the night our vessels had no idea of the enemy's intention."
- The month is "inst." in the original letter (April). The escape is well documented for 14 Apr 1809. Independent of Caldas and Unanue.
- **Assessment:** this is ordinary tropical night weather, the kind any naval narrative cites. It is not evidence of a stratospheric veil. It gives a check point: the logs of HMS *Neptune* (TNA ADM 51/1948) and of *Pompée* (ADM 51/1894; both in catalogue_sweep) should record the weather for 14 Apr 1809.

### F3. Henderson, *An Account of the British Settlement of Honduras* (London 1809), dLOC UF00095343
- Contains a **daily weather log for April 1806** (p. 199, e.g. "Morning cool and hazy; noon fine"). This predates the eruption and gives baseline only. URL: https://ufdc.ufl.edu/UF00095343/00001 .

## Issue-by-issue reading (whole-issue OCR text files)
**Method:** each issue's OCR is a plain-text file on the UFDC image server, `https://ufdcimages.uflib.ufl.edu/<AA/00/04/75/11>/<VID>/<BIBID>_<VID>.txt`. The bibid is split into pairs of characters to make the path. For older items the name is `<YYYYMMDD>01_pdf.txt`, e.g. https://ufdcimages.uflib.ufl.edu/AA/00/09/81/75/00104/1808121701_pdf.txt . The file names come from `<BIBID>/<VID>/citation?format=api`. Each file was read through WebFetch with a fixed prompt asking for weather, sky, sun, moon, haze, fog, smoke, rain, drought, crops, earthquake, volcano, ashes, dust, explosions, sea state, and arrivals from the Spanish Main or the Pacific. The summariser read every file, but the OCR is noisy, so a nil result is a weak negative. Verification level: OCR text via WebFetch.

### Barbados Mercury, and Bridge-town Gazette (AA00047511), Bridgetown, 13.1°N 59.6°W
| vid | Date | Result |
|---|---|---|
| 00458 | Sat 17 Dec 1808 | Nil. Arrivals from Grenada, St Lucia, Cork, Madeira. A plantation advert: "The present crop is likely to nett from …" |
| 00459 | Tue 20 Dec 1808 | Nil. "heavy sea" in a naval chase off Martinique. Seahorse vs Turkish frigate (Jul 1808) and Corunna news reprinted. Arrivals: Neptune; schooner Patty from Boston. |
| 00460 | Sat 24 Dec 1808 | **No usable OCR**: the text files contain only the Tiffen colour target. Page images needed (dLOC or EAP1086). |
| 00461 | Tue 27 Dec 1808 (inferred) | OCR is garbled, with no masthead. Nil; "eclipsed" appears only in a figurative sense. |
| 00462 | Sat 31 Dec 1808 (inferred) | **No usable OCR** (colour target only). |
| 00463 | Tue 3 Jan 1809 | Nil. Martinique and Spain news, the US Embargo debate. Arrivals from New York, Demerara, Dominica. |
| 00464 | Sat 7 Jan 1809 | Nil. French reinforcements at Martinique; the Embargo. |
| 00465 | Tue 10 Jan 1809 | Nil. Garrison contracts; Canning–Pinckney correspondence. |
| 00466 | Sat 14 Jan 1809 | Nil. Castaños's defeat; the Cintra inquiry; arrivals from Liverpool. |
| 00467 | Tue 17 Jan 1809 | Nil, apart from a West India fleet "dispersed by a heavy gale on the 19th" (in the Atlantic, reprinted). |
| 00468 | Sat 21 Jan 1809 | Nil. The Assembly v. Gen. Carmichael (Fort Augusta mutiny). |
| 00469 | Tue 24 Jan 1809 | Nil for the sky. Surf at Antigua (a wreck); *Terpsichore* action off Ceylon "dark and squally"; Finland "dampness of the weather" (10 Nov 1808). A Havana schooner is mentioned. |
| 00470 | Sat 28 Jan 1809 | Nil. Capri; a London pro-Spanish meeting. |
| 00471 | Tue 31 Jan 1809 | Nil for the sky. The Martinique expedition "sailed with so favouring a breeze, that before sun-set the whole were entirely clear of the land", and "Since the sailing of the Expedition the wind has been rather squally, chiefly from the Southward and S.E." (Barbados, ~28–31 Jan 1809). |
| 00472 | Sat 4 Feb 1809 | Nil. Martinique attack. "sporting in the sun … the damps of evening" is a figurative passage about the French. |
| 00473 | Tue 7 Feb 1809 | Nil. Cayenne capitulation; Martinique. |
| 00474 | Sat 11 Feb 1809 | Nil. |
| 00475 | Tue 14 Feb 1809 | Nil. |
| 00476 | Sat 18 Feb 1809 | Nil. Siege artillery at Fort Bourbon, Martinique, "constantly kept up both by night and day". This is a gunfire source for any reports of "explosions" in the Windward Islands in Feb 1809. |
- Barbados Mercury, Mar–Jun 1809: checked only by issue-level keyword search (queries 1–13). Not read issue by issue. **Gap.**

### Royal Gazette, and Bahama Advertiser (AA00079433), Nassau, 25.1°N 77.3°W
Read with `pagetext?term=the&bibid=AA00079433&vid=<V>`, which returns the OCR text of all 4 pages.
| vid | Date | Result |
|---|---|---|
| 03635 | 21 Dec 1808 | Nil. Death of Ferrand at Santo Domingo; capture of the brig *Maria* off Barbados. HMS *Variable* arrived at Jamaica on 20 [Nov]. |
| 03636 | 24 Dec 1808 | Nil (Cevallos exposition; Dalrymple/Vimeiro). A French transport "got into" Carthagena (Spain? context unclear), escaping a British squadron. |
| 03637 | 28 Dec 1808 | Nil. "burst forth like a sudden explosion" (the Aranjuez riot, figurative). |
| 03638 | 31 Dec 1808 | Nil. |
| 03639 | 4 Jan 1809 | Nil. Arrivals from Crooked Island, Charleston, Jamaica. |
| 03640 | 7 Jan 1809 | Nil. Bill for rebuilding Falmouth (Jamaica), "burnt in May last". |
| 03641 | 11 Jan 1809 | Nil. |
| 03642 | 14 Jan 1809 | Nil. A vessel from Porto Rico. |
| 03643 | 18 Jan 1809 | Keyword hits only, all irrelevant (see queries 3–4). |
| 03644 | 21 Jan 1809 | Nil. "the neighbouring Spanish colonies of Cuba and the Main" (trade). |
| 03645 | 25 Jan 1809 | Nil. "inclemency of the season" (Gulf of Finland). |
| 03646 | 28 Jan 1809 | Nil (land sale; "dark clouds" used figuratively). |
| 03647 | 1 Feb 1809 | Nil (Masonic ode: "the sun has declined"). |
| 03648 | 4 Feb 1809 | "meteor course" (a poem on Napoleon). Nil. |
| 03649 | 8 Feb 1809 | "NEW VOLCANO": São Jorge, Azores, May 1808 (reprint). |
| 03650 | 11 Feb 1809 | The schooner *William* (Capt. Spalding, of Halifax) left Jérémie in Dec 1808 with coffee, met "the extreme violence of the weather", the vessel "covered with ice", and put into Nassau. This is ordinary winter weather north of the Bahamas, not an anomaly. |
| 03651 | 15 Feb 1809 | Nil. A gale at San Salvador (the *Snow Ranger* aground). |
| 03652 | 18 Feb 1809 | Nil (rains at Rosas, Spain; a moon in a poem). |
| 03654 | 25 Feb 1809 | Nil. |
| 03655 | 1 Mar 1809 | Nil. A vessel "driven out to sea in a heavy squall". |
- vids 03653 (22 Feb) and 03656–03688 were checked only by keyword search (queries 1–13). **Gap:** Mar–Jun 1809 were not read issue by issue.

### The Tobago Gazette (AA00084163), Scarborough, 11.2°N 60.7°W
- dLOC run for 1808: 48 issues, 29 Jan – **16 Dec 1808** (vid 01041 is the last). **There are no 1809 issues in dLOC.**
- 01041 (16 Dec 1808): Nil. The only "moon" is in a reprinted Baltic gun-boat action of 3 Sep 1808 ("in the evening the moon … obscured"). Irrelevant.
- (vid 01042 is a 1895 issue: dLOC vids are not in date order.)

### The Essequebo & Demerary Royal Gazette (AA00098175), Georgetown/Stabroek, 6.8°N 58.2°W
- dLOC run for 1808: 53 issues, to **31 Dec 1808**. **There are no 1809 issues in dLOC.**
- 00104 (17 Dec 1808), whole-issue text read: Nil. Arrivals from New Brunswick and Liverpool; a subscription for the Trinidad fire; the "Plugged Joes" currency notice.
- 00105 (24 Dec 1808): Nil. Arrivals from Glasgow, Liverpool, Cork, Halifax.
- 00106 (31 Dec 1808): Nil. "famine and Cold Winter are likely" (Spanish war news).
- 00103 (10 Dec 1808): not read; it falls before the onset.

### Surinaamsche Courant (AA00098218 for 1808; AA00098217 for 1809), Paramaribo, 5.8°N 55.2°W
- Dec 1808: vids 00093 (2 Dec), 00094 (9), 00095 (13), 00096 (16), 00097 (20), 00098 (23), 00099 (27), 00100 (30 Dec 1808). 1809: 94 issues (AA00098217).
- 00097 (20 Dec 1808), whole-issue text read: **OCR poor** (page 2 is partly legible; pages 3–4 are noise). Nil in what is legible: an address to the inhabitants of Santo Domingo credited to the *Barbados Mercury*, a departure notice, and deaths.
- **Conclusion:** the Surinaamsche Courant needs page images (dLOC JPEGs, e.g. https://ufdc.ufl.edu/AA00098218/00097). OCR keyword searches on this title are unreliable.

## Other leads checked (not newspapers in dLOC)
- **Royal Gazette (Kingston, Jamaica), vol. 31 (1809)**, British Library copy, digitised in AM Digital *Eighteenth Century Journals*: https://www.18thcjournals.amdigital.co.uk/Documents/Details/Royal-Gazette--volume-31/Royal Gazette, Volume 31 . The page states: "The full content of this document is only available to subscribing institutions." Vol. 30 (1808) is presumably the same; not verified. **Highest-priority inaccessible source of this strand.** It is weekly, with supplements, and it carries Kingston shipping news from Cartagena, Santa Marta, Portobelo and Chagres; Jamaica traded heavily with the Spanish Main in 1808–09.
- CRL Digital Collections, *Royal Gazette* (Kingston): digitised holdings are only "v.4 (1781/2) … v.43-44 (1821-1822)" (https://digitalcollections.crl.edu/record/463192). **They do not cover 1808–09.**
- National Library of Jamaica: holds "The Royal Gazette 1780 – 1837, 1844" and the "St. Jago de la Vega Gazette 1791 – 1837" (https://nlj.gov.jm/newspapers/). Format and digitisation are not stated; probably microfilm or on-site only.
- **Danish West Indies:** KB (Royal Danish Library) lists **"The St. Croix Gazette (1808-1813)"** and **"The Saint Thomas Gazette (1809-1815)"** (British-occupation era) as digitised in Mediestream: https://www.kb.dk/en/inspiration/newspapers-danish-west-indies ; St Croix Gazette list: http://www2.statsbiblioteket.dk/mediestream/avis/list/doms_newspaperAuthority:uuid:0ca7a727-bb38-482c-946b-44cc119e87a4 ; St Thomas Gazette list: http://www2.statsbiblioteket.dk/mediestream/avis/list/doms_newspaperAuthority:uuid:14f4fede-8487-415e-a066-7b21d5af61b3 . Fetching these failed here (robots-disallowed). The KB Labs API (https://labs.statsbiblioteket.dk/labsapi/api/aviser/export/fields?…) answered, but returned empty CSVs even for a trivial query (probably IP-restricted or limited to content over 140 years old). **A human can open these freely in Mediestream** (papers over 100 years old are open online). **Strong lead:** St Croix is at 17.7°N, a free port in direct contact with La Guaira and Cartagena.
- **Barbados Mercury page images:** BL Endangered Archives EAP1086 (free): 1808 at https://eap.bl.uk/collection/EAP1086-1-7 (104 issues; "extremely brittle, badly worm damaged"), 1809 at https://eap.bl.uk/collection/EAP1086-1-8 (monthly sub-collections, e.g. https://eap.bl.uk/collection/EAP1086-1-8-6 = June 1809). Use these for 24 and 31 Dec 1808, which have no OCR in dLOC.
- **Bermuda Gazette:** AM Digital has only 1785. There is no dLOC copy for 1809. The Bermuda National Library Bermudiana collection (https://www.bnl.bm/colmgt/colmgt-bermudiana/) has unknown digitisation.
- *Gaceta de Puerto Rico*: UFDC/dLOC run AA00023800 starts 1837 or later in the API. **There are no 1809 issues online here.**
- **Readex *Caribbean Newspapers, Series 1, 1718–1876*** (subscription; >140 titles from 22 islands plus Bermuda): the likely home of the *Jamaica Courant*, *Kingston Chronicle*, *St George's Chronicle* (Grenada), *Antigua Journal*, *St Christopher Gazette* and *Trinidad Weekly Courant* for 1808–09. A title list was not obtained. Library access only (e.g. https://libguides.bodleian.ox.ac.uk/caribbean_newspapers).
- **Simon Taylor (Jamaica planter) letters**, Taylor family papers 1770–1835, Institute of Commonwealth Studies, Senate House Library (ICS 120). Over a quarter of the letters are in letterbooks. Catalogue: https://archiveshub.ac.uk/search/archives/09aa7a0c-b553-379a-ac53-250b9a070353 and https://archives.libraries.london.ac.uk/Details/archive/110024489 (not opened: budget). Microfilmed in AMP *Plantation Life in the Caribbean, Pt 1: Jamaica c.1765–1848* (https://www.ampltd.co.uk/digital_guides/plantation_life_in_the_carribean_part_1/Contents.aspx ; CRL https://crl.edu/node/12440). Taylor wrote frequent letters with weather and crop remarks until he died in 1813. **Catalogue-only lead for Dec 1808 – Feb 1809.**
- TNA Discovery N13730401, "meteorological journals kept in Jamaica" (Edinburgh University Library, Dc 6 96), covers **1785–92**. Not relevant.
- Jamaican diaries already in catalogue_sweep_1808-09.md (Pinnock, BL Add MSS 33316–7; NML DX/2416; Bluett) are not repeated here.

## Assessment and what this constrains
1. **Eastern Caribbean and Guianas (Barbados 13°N, Tobago 11°N, Demerara 7°N, Paramaribo 6°N), Dec 1808 – Feb 1809:** no printed report of a dimmed or coloured sun, haze, ash or detonations. In the Barbados and Bahamas papers, local news is a small share of each issue; most space is European reprints. A thin stratospheric veil (Caldas's "silver" sun) might not have struck island editors as news at all. Compare 1812, when ash actually fell on Barbados (Barbados Mercury, 12 May 1812: "an impenetrable haze hung over the sea"). So the negative rules out only a *conspicuous* local event (ash fall, darkness, audible explosions) in the eastern Caribbean. It does not rule out a subtle veil.
2. **The ships seen are uninformative.** No arrival from Cartagena, Santa Marta, La Guaira, Portobelo or Chagres was found in the issues read. The Spanish Main trade ran through Jamaica, Curaçao and St Thomas, so the gap lies in the Kingston and St Thomas/St Croix papers, which cannot be reached here.
3. **The noise sources in this window are documented.** These include the Martinique siege (30 Jan – 24 Feb 1809; continuous artillery at Fort Bourbon), the Les Saintes action (14–17 Apr 1809), and gales. Any "explosions heard" in the Windward Islands in Feb 1809 must be checked against the siege.
4. **Old open items closed:** the Edwards 1819 "impenetrable haze" is St Vincent 1812 (F1).

## Recommended next steps (for a human)
1. Kingston *Royal Gazette* vol. 30 (Nov–Dec 1808) and vol. 31 (Jan–Jun 1809) through an institution subscribing to AM Digital *Eighteenth Century Journals*, or the BL/NLJ originals. Look in the "Kingston" local column and the shipping list for arrivals from Carthagena, St Martha, Chagres and Porto Bello.
2. Mediestream: *The St. Croix Gazette* (1808–13) and *The Saint Thomas Gazette* (1809–15). Open the issues for Dec 1808 – Mar 1809.
3. Page images for Barbados Mercury 24 and 31 Dec 1808 (EAP1086/1/7) and the Surinaamsche Courant Dec 1808 – Feb 1809 (dLOC JPEGs).
4. Bahama Gazette and Barbados Mercury, Mar–Jun 1809, issue by issue. The method in this file works for both titles.
5. Simon Taylor letterbook entries for Dec 1808 – Mar 1809 (ICS 120; AMP microfilm).

## Search log (additional to the tables above)
| Repository / tool | Query | Result |
|---|---|---|
| dloc.com/search?q=… | Royal Gazette Jamaica 1809 | JS shell; no results (blocked in effect) |
| archive.org advancedsearch + FTS | Edwards, History of the West Indies vol. 5: "impenetrable haze", 1808, ashes, hostile element, sulphureous OR volcano | Resolved (F1). `OR` queries return 0 in IA FTS. |
| WebSearch | dloc Royal Gazette Jamaica 1809 | AM Digital vol. 31 (subscription); CRL (1782, 1821–22 only) |
| WebSearch | Barbados Mercury 1809 dloc | BL EAP1086 |
| WebSearch | Royal Danish American Gazette / St Croix Gazette 1809 | KB DWI list; dLOC API URL discovered |
| dLOC API exactsearch | publication_date=1809 & mediatype=newspaper | 0 (mediatype value differs) |
| dLOC API exactsearch | genre=newspaper & 1809 | 300 (capped; only the Bahama Gazette visible) |
| dLOC API exactsearch | country=Jamaica / Bermuda & 1809 | 0 / 0 |
| dLOC API exactsearch | language=Spanish & 1809 | 8 (maps, pamphlets; no periodicals) |
| dLOC API exactsearch | title=Chronicle & 1809; title=Courant & 1809 | 0; 94 (Surinaamsche only) |
| dLOC API exactsearch | fulltext=Carthagena & 1808 | 19 (Barbados, Bahama, Tobago, Demerara, all Jan–Oct 1808) |
| dLOC API exactsearch | fulltext=meteor & 1809; smoky & 1809; thermometer & 1809 | 2 (poem on Napoleon; 03682 not read); 0; 2 (Henderson; Bahama Sep 1809, outside the window) |
| dLOC API exactsearch | fulltext=sun & Barbados & 1809 | 21. In-window hits read (00467, 00471, 00476, 00501) are all "Sunday", "sunset", "sundry" or "under the sun". |
| dLOC API exactsearch | fulltext=volcano & 1808 | 1 (Bahama Gazette, 27 Jan 1808) |
| api.patron.uflib.ufl.edu | same API, wider UFDC | same results for volcano 1809 |
| KB labsapi | several queries | empty CSV (not usable) |
| TNA Discovery API | N13730401 | Jamaica met journals 1785–92 (not relevant) |
| WebSearch | Simon Taylor 1809; Plantation Life in the Caribbean | catalogue-level only |
| WebFetch budget | — | The shared 400/h proxy budget was hit repeatedly. Several planned reads were deferred: Barbados Mercury Mar–Jun issue by issue; Bahama Gazette Mar–Jun; Bahama 03682 "meteor"; Cambridge ArchiveSearch Vanneck items. |

## Source register
| Source/edition | Region/lang | Type | Covers 1808–09? | Digitized (URL) | Access from here | Opened from here? |
|---|---|---|---|---|---|---|
| Barbados Mercury, and Bridge-town Gazette (dLOC AA00047511) | Barbados / EN | newspaper, twice weekly | yes (104 issues 1808, 104 issues 1809) | https://ufdc.ufl.edu/AA00047511/00464 (pattern /AA00047511/<vid>) ; API https://api.dloc.patron.uflib.ufl.edu/exactsearch?bibid=AA00047511&publication_date=1809 | OCR full text via API + text files | yes |
| Barbados Mercury (BL EAP1086 images) | Barbados / EN | newspaper images | yes | https://eap.bl.uk/collection/EAP1086-1-7 ; https://eap.bl.uk/collection/EAP1086-1-8 | catalogue pages only; images not tried | yes (catalogue) |
| Royal Gazette, and Bahama Advertiser (dLOC AA00079433) | Bahamas / EN | newspaper, twice weekly | yes (105 issues 1808; 1809 run) | https://ufdc.ufl.edu/AA00079433/03644 | OCR via API | yes |
| The Tobago Gazette (dLOC AA00084163) | Tobago / EN | weekly | 1808 to 16 Dec 1808 only | https://ufdc.ufl.edu/AA00084163/01041 | OCR via API | yes |
| Essequebo & Demerary Royal Gazette (dLOC AA00098175) | Demerara / EN | weekly | 1808 to 31 Dec 1808 only | https://ufdc.ufl.edu/AA00098175/00104 | OCR via API | yes |
| Surinaamsche Courant (dLOC AA00098218 for 1808; AA00098217 for 1809) | Suriname / NL+EN | twice weekly | yes | https://ufdc.ufl.edu/AA00098218/00097 ; https://ufdc.ufl.edu/AA00098217/00277 | OCR poor; images needed | yes |
| Henderson, Account of the British Settlement of Honduras (1809) (dLOC UF00095343) | Belize / EN | book with 1806 weather log | baseline only | https://ufdc.ufl.edu/UF00095343/00001 | OCR via API | yes |
| Edwards, History … of the West Indies vol. 5 (1819) | Caribbean / EN | history | St Vincent 1812 | https://archive.org/details/b33287417_0005 | IA FTS | yes |
| Royal Gazette (Kingston, Jamaica) vol. 31, 1809 (BL copy) | Jamaica / EN | weekly newspaper | yes | https://www.18thcjournals.amdigital.co.uk/Documents/Details/Royal-Gazette--volume-31/Royal Gazette, Volume 31 | subscription only | yes (record only) |
| Royal Gazette (Kingston), CRL digital | Jamaica / EN | newspaper | no (1781–82, 1821–22) | https://digitalcollections.crl.edu/record/463192 | open record | yes |
| NLJ newspaper holdings (Royal Gazette 1780–1837; St Jago de la Vega Gazette 1791–1837) | Jamaica / EN | newspapers (format unknown) | yes | https://nlj.gov.jm/newspapers/ | on-site/unknown | yes |
| The St. Croix Gazette (1808–1813), Mediestream | St Croix / EN | newspaper | yes | http://www2.statsbiblioteket.dk/mediestream/avis/list/doms_newspaperAuthority:uuid:0ca7a727-bb38-482c-946b-44cc119e87a4 | robots-blocked here; open to humans | blocked |
| The Saint Thomas Gazette (1809–1815), Mediestream | St Thomas / EN | newspaper | 1809 on | http://www2.statsbiblioteket.dk/mediestream/avis/list/doms_newspaperAuthority:uuid:14f4fede-8487-415e-a066-7b21d5af61b3 | robots-blocked here | blocked |
| KB list of DWI newspapers | DWI | finding aid | — | https://www.kb.dk/en/inspiration/newspapers-danish-west-indies | open | yes |
| KB Labs API (aviser export) | Denmark/DWI | API | ? | https://labs.statsbiblioteket.dk/labsapi/api/aviser/export/fields | returns empty | yes (empty) |
| Bermuda Gazette (AM Digital) | Bermuda / EN | newspaper | no (1785 only) | https://www.18thcjournals.amdigital.co.uk/Documents/Details/Bermuda-Gazette-and-Weekly-Advertiser/Bermuda Gazette and Weekly Advertiser | subscription | yes (record) |
| Bermuda National Library, Bermudiana | Bermuda | library | unknown | https://www.bnl.bm/colmgt/colmgt-bermudiana/ | not tried | not tried |
| Gaceta de Puerto Rico (UFDC AA00023800) | Puerto Rico / ES | newspaper | no (from 1837 in API) | https://api.dloc.patron.uflib.ufl.edu/exactsearch?bibid=AA00023800&publication_date=1809 | open | yes |
| Readex Caribbean Newspapers Series 1, 1718–1876 | 22 islands + Bermuda | newspaper database | probably | https://libguides.bodleian.ox.ac.uk/caribbean_newspapers | subscription | not tried |
| Pactor, Colonial British Caribbean Newspapers (1990) | Caribbean | bibliography | yes | https://solo.bodleian.ox.ac.uk/permalink/44OXF_INST/35n82s/alma990106343790107026 | print | not tried |
| Bodleian Caribbean newspapers guide | Caribbean | finding aid | — | https://libguides.bodleian.ox.ac.uk/newspapers/caribbean | open | yes |
| Taylor family papers (Simon Taylor letterbooks), ICS 120 | Jamaica / EN | MS letters | yes (to 1813) | https://archiveshub.ac.uk/search/archives/09aa7a0c-b553-379a-ac53-250b9a070353 | catalogue only | yes (Archives Hub) |
| AMP Plantation Life in the Caribbean Pt 1 (Jamaica) microfilm | Jamaica | microfilm | yes | https://www.ampltd.co.uk/digital_guides/plantation_life_in_the_carribean_part_1/Contents.aspx ; https://crl.edu/node/12440 | library | yes (guide) |
| Edinburgh UL Dc 6 96, Jamaica meteorological journals | Jamaica | MS | no (1785–92) | https://discovery.nationalarchives.gov.uk/details/r/N13730401 | catalogue | yes |
| Penrhyn papers (Jamaica estates), Bangor | Jamaica | MS letters | possibly | https://calmview.bangor.ac.uk/CalmView/rdf/catalog/PENRH/4/3/1490-1504/1493 | not opened (budget) | blocked (budget) |
| Cambridge ArchiveSearch (Vanneck/Arcedeckne) | Jamaica | MS | unknown | https://archivesearch.lib.cam.ac.uk/repositories/2/archival_objects/644507 | not opened (budget) | blocked (budget) |

## Round 3b: Mar–Jun 1809 issue-by-issue
*(Added 16 Oct 2026, 09:27–09:46 UTC. Method: whole-issue OCR read through WebFetch. Barbados Mercury: `https://ufdcimages.uflib.ufl.edu/AA/00/04/75/11/<vid>/AA00047511_<vid>.txt`. Bahama Gazette: `https://api.dloc.patron.uflib.ufl.edu/pagetext?term=the&bibid=AA00079433&vid=<vid>`. Surinaamsche Courant: `https://ufdcimages.uflib.ufl.edu/AA/00/09/82/1[7|8]/<vid>/<YYYYMMDD>01_pdf.txt`. The same fixed prompt was used throughout, asking for weather, sky, sun, moon, twilight, haze, fog, smoke, rain, drought, cold, earthquake, volcano, ash, pumice, dust, non-battle detonations, sea state, and arrivals from the Spanish Main or the Pacific. Verification level: OCR text via the WebFetch summariser. Page images were not seen. Quotes are OCR-level.)*

### Result
**No issue of either paper, 1 Mar – 30 Jun 1809, reports a dim, red or pale sun, haze, unusual twilights, ash, pumice, unexplained detonations, a local earthquake, or a ship report from the Spanish Main or the Pacific with sky or sea anomalies.** The same holds for the Surinaamsche Courant, 13 Dec 1808 – 25 Feb 1809, though that OCR is poor. Every weather item found is either a European or US reprint or ordinary local weather (rain, gales, squalls).

### Barbados Mercury (AA00047511), 21 Feb – 27 Jun 1809 (vids 00477–00513; 37 issues)
| vid | Date (issue) | Result |
|---|---|---|
| 00477 | Tue 21 Feb | Martinique siege (early Feb 1809): "the inclemency of the weather, and almost incessant rains" (OCR partly reconstructed by the summariser). Local rain, not haze. |
| 00478 | Sat 25 Feb | Nil locally. Reprints: Bath (Maine), Savannah and New York winter items (Jan 1809). A Cape of Good Hope paragraph names the homebound ship *Flora* "from New South Wales" with news of the Bligh affair; no weather. |
| 00479 | Tue 28 Feb | Nil (the Fort Bourbon siege). |
| 00480 | ~Sat 4 Mar | Nil. |
| 00481 | Tue 7 Mar | Celebrations of the capture of Martinique: rockets "Posting off in the clouds", "peals thro' the land" (celebratory guns). Nil otherwise. |
| 00482 | Sat 11 Mar | Atlantic fleets "dispersed on the 24th in a heavy gale that lasted for several weeks" (European reprint). Nil locally. |
| 00483 | Tue 14 Mar | European weather only (Moore's dispatch: snow and cold; ice at Leith). Nil locally. |
| 00484 | Sat 18 Mar | Nil. |
| 00485 | ~Tue 21 Mar | Nil. |
| 00486 | Sat 25 Mar | Nil locally (Galicia floods; the *San Justo* from Vera Cruz). |
| 00487 | Tue 28 Mar | Nil. |
| 00488 | ~1 Apr | Nil (French Brest squadron near Guadeloupe). |
| 00489 | ~4 Apr | Nil. |
| 00490 | ~8 Apr (date illegible) | Nil (the *Berwick* driven ashore near Martinique; cause not stated). |
| 00491 | ~8–11 Apr | Nil. |
| 00492 | Sat 15 Apr | Nil. |
| 00493 | Tue 18 Apr | Nil. |
| 00494 | Sat 22 Apr | Nil (capture of the Saintes). |
| 00495 | Tue 25 Apr | Nil. |
| 00496 | Sat 29 Apr | Nil. Arrivals: *Fleetwood* from Liverpool, HMS *Blonde* from Cayenne. |
| 00497 | ~2–6 May | Nil. |
| 00498 | Sat 6 May | Nil. |
| 00499 | ~9 May (garbled) | Nil. |
| 00500 | ~13–16 May | Nil. |
| 00501 | Tue 16 May | Nil. |
| 00502 | ~Sat 20 May | Gen. Beckwith's dispatch from Martinique (Feb 1809): "notwithstanding heavy rains and most unfavourable weather" (OCR: "heavy rains'and most uafayourable weather"). Ordinary weather. |
| 00503 | ~23 May | Nil. |
| 00504 | ~27 May | Nil. |
| 00505 | ~30 May | Nil (garbled). |
| 00506 | ~3 Jun | **No usable OCR** (colour target only). |
| 00507 | ~6 Jun | Royal salutes for the King's birthday (4 Jun) at Barbados: a known source of gunfire reports. Nil otherwise. |
| 00508 | Sat 10 Jun | Nil. |
| 00509 | ~13 Jun | Nil. |
| 00510 | ~17 Jun | Nil. |
| 00511 | ~20 Jun | Nil (garbled date). |
| 00512 | ~24 Jun | Nil (garbled; only a sailing-wind fragment). |
| 00513 | Tue 27 Jun | Nil. An American ship spoken on 8 Jun at 36°N 56°W, "with a fair wind, all well". |

### Royal Gazette, and Bahama Advertiser (AA00079433), 1 Mar – 28 Jun 1809 (vids 03655–03689)
| vid | Date | Result |
|---|---|---|
| 03655 | 1 Mar | Nil (vessel "driven out to sea in a heavy squall"). |
| 03656 | 4 Mar | Nil locally. A squall in the *Amphitrite* account; a "heavy sea" in a chase off Trinidad; Glasgow synod harvest and wet weather (1808 Scotland). |
| 03657 | 8 Mar | "a gale from the N. W." (naval). Nil. |
| 03658 | 11 Mar | A ship cut through ice (northern harbour reprint). Nil. |
| 03659 | 15 Mar | Nil. |
| 03660 | 18 Mar | US report of the 4 March (Madison inauguration) celebrations: "But the clouds soon dispersed and the sun shone upon one of the finest days that we have witnessed for many weeks." Ordinary weather, US East Coast. Nil. |
| 03661 | 22 Mar | **Only Spanish Main arrival found:** "Margaret, nine days from the Main", reporting "a Spanish packet in 22 days from Cadiz" (item dated 9 Mar). Political news only; no sky or sea remarks. |
| 03662 | 25 Mar | Nil. |
| 03663 | 29 Mar | Nil locally (Salamanca rains; Corunna winds; poem). |
| 03664 | 1 Apr | Nil. |
| 03665 | 5 Apr | Nil (Pye's New Year ode). |
| 03666 | 8 Apr | London "sudden thaw" floods (Jan 1809 reprint). Nil locally. |
| 03667 | 11 Apr | Nil locally. |
| 03668 | 15 Apr | Nil. |
| 03669 | 19 Apr | Transports for Jamaica turned back to Nassau by "adverse winds" (Apr 1809). The schooner *Messenger*, 20 days from Curaçao to Halifax, brought no news. Nil. |
| 03670 | 22 Apr | Nil. |
| 03671 | 26 Apr | Nil ("blowing fresh" at sea, mid-March, ship *Diana*). |
| 03672 | 29 Apr | Keyword-checked in round 3 (the Burke "volcano" metaphor). Not read in full. |
| 03673 | 1 May | Keyword-checked in round 3 (Whitehaven earthquake, "very thick and hazy", England). Not read in full. |
| 03674 | 3 May | Drury Lane fire, London, 24/25 Feb 1809 ("The night was uncommonly fine"; explosions; "a shock like an earthquake"). A reprint, irrelevant. |
| 03675 | 6 May | Nil locally (Sleaford church window blown in, 29 Jan; Montego Bay item on a schooner from Vera Cruz to Maracaibo). |
| 03676 | 13 May | Nil. |
| 03677 | 17 May | Nil. |
| 03678 | 20 May | (Round 3) Les Saintes, night of 14 Apr: "darkness and haziness of the night" (see F2). |
| 03679 | 24 May | Nil locally (European sea and ice items). |
| 03680 | 27 May | Nil. |
| 03681 | 31 May | Nil (poem; Bordeaux plague letter). |
| 03682 | 3 Jun | Nil locally (Paris balloon duel, 3 May). |
| 03683 | 7 Jun | Nil locally (English snow; the Bath "predicted earthquake" hoax of 31 Mar). |
| 03684 | 10 Jun | Nil. |
| 03685 | 14 Jun | Nil. |
| 03686 | 17 Jun | Nil. |
| 03687 | 21 Jun | Nil. |
| 03688 | 24 Jun | Nil locally (night darkness at Ushant and Basque Roads, Apr 1809). |
| 03689 | 28 Jun | Nil locally (Basque Roads gale). |
| 03653 | 22 Feb | Not read in full (keyword hit only: Finland, "darkness of the weather"). |

### Surinaamsche Courant, 13 Dec 1808 – 25 Feb 1809 (AA00098218 vids 00095–00100; AA00098217 vids 00260–00274)
- Dates read: 13, 16, 20, 23, 27 and 30 Dec 1808; 7, 11, 14, 18, 21, 25 and ~28 Jan 1809; 1, ~4, ~8, 11, 15, 18 and ~22 Feb 1809, plus vid 00274 (date illegible). 21 issues in all.
- **All nil.** The only marginal items are a curfew notice "before sun-rise" (23 Dec), "contrary winds" at Capri (a reprint, ~11 Feb), and a frigate arrival of unreadable origin (~22 Feb).
- **The OCR is poor or very poor throughout** (Dutch and English columns interleaved, many words garbled). These nil results are weak, and the page images (https://ufdc.ufl.edu/AA00098217/<vid>) still need checking by eye.
- The whole-issue file name pattern `<YYYYMMDD>01_pdf.txt` works for both Surinaamsche bibids. The Feb 1809 vids were matched to dates by inference (00267 = 1 Feb, …, 00273 = 22 Feb), and the files resolved under those names.

### Assessment for Round 3b
- With the round 3 reading, Barbados and Nassau are now covered issue by issue from mid-Dec 1808 to end-Jun 1809. Exceptions: Barbados 24 and 31 Dec 1808 and ~3 Jun 1809 (no OCR), and Bahama 22 Feb, 29 Apr and 1 May (keyword-checked only).
- Neither paper shows any sign of a conspicuous optical or volcanic phenomenon at 13°N or 25°N across the whole Feb 1809 ±4 months ice-core window. Local weather notes are ordinary: Feb rains on Martinique, gales, squalls.
- Detonation-type noise sources in the window are documented: the Martinique siege (Feb), the Martinique victory celebrations (early Mar), the Saintes action (14–17 Apr), and the King's birthday salutes (4 Jun).
- Caveats:
  1. The OCR is noisy and the summariser may miss short local paragraphs.
  2. Most column space is European reprints.
  3. A thin veil like the one Caldas reported would probably not have been news to island editors.
  4. The only Spanish Main arrival found (*Margaret*, "nine days from the Main", Bahama Gazette 22 Mar 1809) carries political news only.
- The Kingston *Royal Gazette* (subscription) and the St Croix and St Thomas Gazettes (Mediestream) remain the key unread Caribbean sources for ship reports from Cartagena and La Guaira.
