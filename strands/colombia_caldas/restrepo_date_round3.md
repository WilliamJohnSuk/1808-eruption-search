---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: colombia_caldas
date: undated
---

# Round 3: dating Restrepo's "sol opaco" note (strand "restrepo_date")

Written 16 Oct 2026.

**Method.** archive.org in-book search (inside.php) and per-page OCR (BookReaderGetTextWrapper), plus a few WebSearch and WebFetch calls. No page images were read, so every Restrepo wording below is OCR-level text. WebFetch summaries cut quotations to 125 characters, so long passages were recovered as token lists.

**Rate limits.** The proxy refused 5 requests with HTTP 429, and 1 request failed with a server error. All six are listed in the search log.

## Verdict
- **What is observed belongs to Oct–Nov 1807. Restrepo's own dating, in both editions, is 1808, and that is a one-year mis-dating.**
- **Confidence:**
  - About 90% that the comet in the note is C/1807 R1.
  - About 75% that the dim-sun observation belongs to the same autumn of 1807.
  - About 25% that Restrepo merged a genuine 1808 dim-sun memory with the 1807 comet. If so, the dates in the note cannot be used.
- **Consequence.** The note should **not** be used as evidence that the veil began in Oct–Nov 1808, before Caldas's 11 Dec 1808. At most it is weak, OCR-only, retrospective (c. 1825) evidence of a dim low sun in the northern Andes in Oct–Nov 1807. That fits Portilla's (2017) speculation, and Caldas's own description of the 1807 comet ("luz rojiza, débil, y como dentro de nieblas").

## 1. Correction to round 2: the 1827 edition is dated 1808 by Restrepo, not 1807
Round 2 read the 1827 footnote as belonging to 1807 because of the "Año de 1807" at the top of the page. The coordinate data shows that this is not secure.

**What the coordinate data shows**
- In the 1827 edition the "Año de 18xx." labels are **marginal year notes in the outer margin**, not running heads.
  - In the `historiadelarevo02rest_0` scan (page 2684 px wide), "Año de 1807." on the footnote page (inside.php p. 84 = printed p. 82) has box l=1002, t=926. A second label, "Año de 1808.", sits in the same margin column further down, at box l=1011, t=1253.
  - On a recto page the label is in the right margin (p. 91: l=1927).
- Page OCR of printed p. 82 (`historiadelarevo00rest_0`, BookReader index 81) gives this body sequence, as a token list (OCR, my line joins):
  - "Año de 1807. noticias y variedades, también semanal, que dirigía el bibliotecario Socorro, y que titulaba el Redactor americano, **Año de 1808.** duró cerca de tres años. Por el mismo tiempo varios jóvenes literatos deseosos de promover la ilustración … se asociaron teniendo á su frente á Don Francisco José de Caldas, … y dieron á luz el semanario de la Nueva-Granada *."
- So the footnote mark (*) hangs on the founding of Caldas's *Semanario* (first number Jan 1808), in the passage the margin marks as **1808**. "En los meses de octubre y noviembre **de este año**" therefore means 1808 in Restrepo's 1827 intention. The 1858 edition says the same thing explicitly.

**The 1827 footnote**
- Both 1827 copies were checked: `historiadelarevo00rest_0` and `historiadelarevo02rest_0`.
- The footnote **ends at "…dejó de ser visible en Antioquia el 12 de noviembre"**. The OCR shows no year after it.
  - 00rest_0: "noviembre" is the last token on the page.
  - 02rest_0: only noise follows ("i 1 _ .Q..Q").
  - In-book searches for "1807" and "1808" in both copies show no hit in the footnote zone. The only 1808 hit is the marginal note at t=1253 of 4176.
  - The "180S" reading given in the task brief was **not found in any 1827 copy checked**. The year in "12 de noviembre de 1808" comes from the **1858** edition.
- Full 1827 footnote, page OCR (00rest_0 index 81). It is public domain; OCR "a5" stands for 25:
  > "* En los meses de octubre y noviembre de este año se vió el sol opaco y visible el disco á la simple vista, lo que acaecía por la mañana y por la tarde cuando estaba próximo al orizonte: este fenómeno se observó diariamente en Santafé, en Antioquia y en Quito á un mismo tiempo. Desde el a5 de setiembre se vió también un cometa que apareció en la constelación de libra, y su cola se dirigia un poco al sur; su curso fué al N. E. y dejó de ser visible en Antioquia el 12 de noviembre"

**The 1858 edition, t. 1**
- Copies: `historiadelarevo01rest` (inside.php p. 621) and `historiadelarev00restgoog` (inside.php p. 620). Printed p. 579, in the notes, as part of the biographical note on Caldas.
- OCR tokens: "En los meses de octubre y noviembre de **1808**" (both copies), and "déjó de ser visible en Antióquia el 12de noviembre de **1808**" (01rest).
- Plus, from round 2: "observó Cáldas, lo mismo que los demas ciudadanos", "y por algunos meses, sin que se pudiese dar una explicación satis[factoria]", and "un hermoso cometa que apareció en la constelación de Libra".

## 2. Comets: only 1807 fits
**C/1807 R1, the Great Comet of 1807**
- First seen 9 Sep 1807 by Parisi at Castrogiovanni, Sicily, low in twilight near Spica, which is in Virgo near the Libra border.
- Perihelion 19 Sep. Closest to Earth 26 Sep. Magnitude about 1–2 around 20 Sep. Naked-eye through October.
- Seen by the naked eye in Europe until mid-December. No naked-eye observations from Jan 1808. Last telescopic observation 27 Mar 1808 (Wisniewski).
- Source: Wikipedia, "Great Comet of 1807".

**Caldas's own record of the 1807 comet** (via Portilla 2017; Caldas's text not seen directly)
- *Semanario* "número cero", dated 4 Oct 1807 per Portilla: "Desde el 23 de setiembre se advirtió al fin de la constelación de la Virgen un cometa, y se comenzó a observar el 25 en el Observatorio astronómico de esta Capital." The end of Virgo borders Libra.
- **Restrepo's "Desde el 25 de setiembre" is exactly Caldas's first observatory date in 1807.**
- Path: crossed the equator on 28 Sep, then went through Mons Maenalus, the head of Serpentarius, and the back of Hercules. That is northward, matching Restrepo's "curso … al N. E.".
- Caldas, letter of 6 Nov 1807 (Caldas 1978, carta 115, p. 264): "creo no le dejaré hasta su total desaparición". This is consistent with the comet being lost in Antioquia on 12 Nov.

**Comets of 1808** (Kronk & Meyer 2023; comethunter.de list)
- C/1808 F1 (Pons) and C/1808 M1 (Pons): telescopic discoveries of spring and summer 1808. Details not fetched here, but neither falls in Sep–Nov.
- X/1808 N1: seen only on 4 and 6 July 1808.
- C/1808 R1 (Pons), CBET 5258 (2023):
  - observed only 11–18 Sep 1808
  - magnitude about 8–9, "small and faint"
  - declination +62° to +88°, near the north celestial pole
  - It would have been invisible from Antioquia (6°N), never in Libra, and not seen after 18 Sep.
- **No comet was visible to the naked eye in Libra, or anywhere, in Sep–Nov 1808.** The 1858 date "12 de noviembre de 1808" for the comet is therefore impossible, and so is the 1827 "este año" read as 1808.

## 3. Caldas and Portilla on the 1807 sky
- **Portilla, J. G. (2017).** "Caldas y el gran cometa de 1807", *Rev. Acad. Colomb. Cienc. Ex. Fis. Nat.* 41(159): 244–252, doi:10.18257/raccefyn.449.
  - Quotes Caldas's 1807 notice: "Su luz era rojiza, débil, y como dentro de nieblas", and the tail "cuya fuerza disminuía por grados insensibles hasta desaparecer".
  - Argues that Caldas underestimated the tail "por falta de contraste".
  - Speculates about "una erupción de corta intensidad acaecida unos 15 meses antes" the Dec 1808 event, but calls cirrus over the Tequendama area "la segunda, y más probable" explanation.
  - **Portilla does not mention a dim sun in Oct–Nov 1807 and does not cite Restrepo.** Restrepo's note is therefore the only explicit dim-sun statement for that autumn, and it is independent of Portilla.
- *Redactor Americano* no. 32 (19 Mar 1808) reprints Caldas's notice. Its footnote says a man in Santafé saw the comet by naked eye from 10 Sep, and another in Cartagena. Portilla reports no sun remark there.
- *Semanario* 1808 volume (JCB copy `semanariodelnuev01unse`): in-book search for "cometa" gave **no hits**. Either the "número cero" notice is not in that scan or its OCR is defective. A search for "nieblas" gave only geographical uses (pp. 30, 80, 250, 265, 266).
- *Semanario* 1809 volume (`semanariodelnuev02unse`; its OCR is known to be partial): no hits for "cometa" or "opaco". So no dim-sun remark was found in Restrepo's *Ensayo sobre la geografía … de Antioquia* (published there in 1809), but the OCR is incomplete.
- Caldas's Noticia (Semanario No. 5, 5 Feb 1809) dates the onset of the 1808 veil to **11 Dec 1808**. Caldas had his own observatory and was attentive to the sky. Had there been daily dimming in Oct–Nov 1808 in Santafé, he would be expected to report it. This is a further, indirect argument against an 1808 reading of the Oct–Nov dim sun.

## 4. Interpretation
- **Evidence for 1807 (strong):**
  - The comet details match 1807 precisely: first observatory date 25 Sep, Virgo/Libra, northward course, still followed in Nov.
  - No comet existed to match 1808.
  - Restrepo couples the sun and the comet as simultaneous ("se vió también").
  - The Oct–Nov window matches the comet's period of visibility, not Caldas's 11 Dec 1808 onset.
- **Why Restrepo wrote 1808 (plausible mechanism):**
  - In 1827 he hung the note on the founding of the *Semanario* (Jan 1808), probably because Caldas's comet notice appeared in its "número cero" of Oct 1807.
  - In 1858 he made "1808" explicit and added Caldas, "por algunos meses", and "sin explicación satisfactoria". These look like memory of Caldas's Dec 1808–Jan 1809 veil merged into the 1807 note.
- **Residual alternative:** that the dim sun was a genuine 1808 memory and Restrepo attached the 1807 comet to it wrongly. Against this:
  - the shared months
  - Caldas's silence about Oct–Nov 1808
  - the 1827 wording, which has no "por algunos meses"
- **Physical caveats:**
  - A low sun whose disc is visible to the naked eye is commonplace in haze or smoke. Oct–Nov is a rainy season in the Andes, and dry-season burning is less likely.
  - "Simultaneously in Santafé, Antioquia and Quito" is a broad claim made from memory around 1825.
  - The only verification is OCR text, not page images.
- **What it constrains:** nothing about the date of the 1808/09 eruption, beyond removing a possible pre-11-Dec-1808 onset. It is a weak hint of an aerosol or haze episode in the northern Andes in autumn 1807 (Portilla's hypothesis). Candidate sources would include regional volcanic activity in 1807; this was not investigated here.

## 5. Still to do (not reachable here)
- Read the page images of 1827 t. 2 p. 82 (scan leaf of 00rest_0 n81) to confirm the marginal "Año de 1808" and that no year follows "noviembre". IA page images were not fetchable.
- Read Caldas's 1807 "número cero" notice directly: BanRep hemeroteca digital, *Semanario* / *Redactor Americano* no. 32. Check whether it, or the *Redactor* footnote, mentions the sun.
- Kronk, *Cometography* vol. 2 (1800–1899), for C/1808 F1 and M1 details. Bode's *Jahrbuch* and the *Monatliche Correspondenz* for 1808 were not reached (rate limits).

## Search log
| # | Repository / tool | Query / target | Result |
|---|---|---|---|
| 1 | IA metadata | historiadelarevo02rest_0, historiadelarevo00rest_0, historiadelarevo01rest, historiadelarev00restgoog, semanariodelnuev01unse | servers and dirs obtained (semanario01 needed a second try: SERVER_ERROR, then OK via /server and /dir) |
| 2 | inside.php 02rest_0 | cometa; noviembre; 1808; 1807 | footnote p. 84; marginal-note boxes recovered; no year after "noviembre" |
| 3 | BookReader page OCR 02rest_0 idx 83 | footnote end | noise after "12 de noviembre" |
| 4 | BookReader page OCR 00rest_0 idx 81 (two calls) | body and footnote tokens | asterisk after "semanario de la Nueva-Granada"; marginal "Año de 1808." mid-body; footnote ends "noviembre" |
| 5 | BookReader 00rest_0 idx 82 | continuation page | HTTP 429, not read |
| 6 | inside.php 00rest_0 | 1808; 1807 | 1807 = marginal notes pp. 80, 82, 84; 1808 on p. 82 = marginal note; p. 76: "La última erupción notable del Cotopaxi fué el 2 de abril de 1808" (worth noting; see below) |
| 7 | inside.php 00rest_0 | "tres años" | HTTP 429 |
| 8 | inside.php 01rest (1858) | "noviembre de 1808" | HTTP 429 |
| 9 | inside.php 01rest | cometa; Antioquia noviembre cometa; "visible en Antióquia"; "hermoso cometa" | p. 621: "…12de noviembre de 1808" |
| 10 | BookReader 01rest idx 620, 621, 622 | 1858 note | wrong leaves (index offset); not found |
| 11 | inside.php 00restgoog (1858) | "octubre y noviembre" | p. 620 "…noviembre de 1808" |
| 12 | raccefyn (Portilla 2017), two PDFs | comet dates, haze, Restrepo | see §3 |
| 13 | WebSearch | comets 1808 Pons; "C/1808 R1"; Restrepo "sol opaco"; Portilla citation | comethunter list, CBET 5258; no web hit for Restrepo's dim-sun note |
| 14 | comethunter.de; CBET 5258; Wikipedia, Great Comet of 1807 | 1807/1808 comets | see §2 |
| 15 | IA advancedsearch | Semanario titles | HTTP 429 |
| 16 | inside.php semanario02 | cometa; opaco | 0 hits (OCR partial) |
| 17 | inside.php semanario01 | cometa; nieblas | 0 hits; 5 geographical "nieblas" hits |

**Side note on the Cotopaxi hit.** The 1827 t. 2, p. 76 OCR reads "La última erupción notable del Cotopaxi fué el 2 de abril de 1808". The GVP lists a Cotopaxi eruption in 1803 rather than 1808; I have not checked whether "1808" is an OCR misreading. Restrepo may be giving a date for a regional eruption, which deserves a check by the GVP strand. I did not read the context.

## Source register
| Source/edition | Region/lang | Type | Covers 1808–09? | Digitized (URL) | Opened from here? |
|---|---|---|---|---|---|
| Restrepo, *Historia de la revolución…* 1st ed., Paris 1827, t. 2 (copy A) | Colombia / es | history | yes (1807–08 note) | https://archive.org/details/historiadelarevo00rest_0 | yes (OCR, inside.php and page OCR; no images) |
| Same, t. 2 (copy B) | Colombia / es | history | yes | https://archive.org/details/historiadelarevo02rest_0 | yes (OCR) |
| Restrepo, *Historia…* 2nd ed., Besanzón 1858, t. 1 | Colombia / es | history | yes (p. 579 note) | https://archive.org/details/historiadelarevo01rest | yes (inside.php; page OCR indexing failed) |
| Same, 1858 (Google scan) | Colombia / es | history | yes | https://archive.org/details/historiadelarev00restgoog | yes (inside.php) |
| Portilla 2017, "Caldas y el gran cometa de 1807", RACCEFyN 41(159) | Colombia / es | modern article | 1807 | https://raccefyn.co/index.php/raccefyn/article/download/449/281/3437 ; https://doi.org/10.18257/raccefyn.449 | yes (WebFetch summary) |
| Same (alternate PDF) | Colombia / es | modern article | 1807 | https://raccefyn.co/index.php/raccefyn/article/download/449/1546/3066 | yes |
| CBET 5258 (2023), C/1808 R1 (Pons) | intl / en | comet orbit | Sep 1808 | https://tamkin3.eps.harvard.edu/iau/cbet/005200/CBET005258.txt | yes |
| comethunter.de, Pons comet list | intl / en | comet list | 1807–08 | https://comethunter.de/pons.html | yes |
| Wikipedia, Great Comet of 1807 | en | reference | 1807–08 | https://en.wikipedia.org/wiki/Great_Comet_of_1807 | yes |
| *Semanario del Nuevo Reyno de Granada* 1808 (JCB) | Bogotá / es | periodical | 1808 | https://archive.org/details/semanariodelnuev01unse | yes (inside.php; no comet hit) |
| *Semanario…* 1809 (JCB), incl. Restrepo's Antioquia *Ensayo* | Bogotá / es | periodical | 1809 | https://archive.org/details/semanariodelnuev02unse | yes (OCR partial) |
| *Redactor Americano* no. 32, 19 Mar 1808 | Bogotá / es | periodical | 1807 comet | Portilla cites a BanRepCultural hemeroteca URL (not copied); no URL found here | not tried |
| Caldas, *Cartas* (1978), carta 115 (6 Nov 1807) | Colombia / es | letters | 1807 | no URL found | no (cited via Portilla) |
| Kronk, *Cometography* vol. 2 (CUP) | intl / en | catalogue | 1808 comets | https://assets.cambridge.org/97805218/72164/frontmatter/9780521872164_frontmatter.pdf (front matter only) | not tried |
| Bode, *Astronomisches Jahrbuch* 1810/1811; *Monatliche Correspondenz* 1808–09 | DE / de | periodical | 1808 comets | no URL found (IA search rate-limited) | not tried |
| Univ. Nacional, "Caldas y la astronomía" lecture PDF | Colombia / es | lecture | 1807 comet | https://ingenieria.bogota.unal.edu.co/repositorio_documental_ajustado/PaginaFacultadIngenieria/DocumentosPresentaciones/CatedraCaldas/CaldasAstronomia.pdf | not tried |
