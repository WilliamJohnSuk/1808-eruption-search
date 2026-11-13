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

# Round 2: text of Caldas's letters, Dec 1808 – Jul 1809 (strand "caldas_letters_text")

Worker notes, 16 Oct 2026. Builds on `caldas_correspondents_pass3.md`.

**Tools.** WebFetch and WebSearch only. The work relied on archive.org full-text search (FTS) and in-book search (`inside.php`).

**Interruptions.**
- The shared WebFetch budget (400 per hour) ran out once at the start.
- archive.org FTS returned HTTP 429 twice (about 60 s each). Those two queries ("Mi querido Arroyo" and "Semanario Arroyo suscriptores") were not read on the first try; the first was repeated successfully later.

**Verification.** No page image was read. All quotations are OCR text returned by inside.php or FTS, reassembled from short verbatim fragments.

---

## 0. Bottom line

1. **The text of Caldas's letters to Arroyo of 21 Jan, 6 Feb and 6 Mar 1809 was NOT reached.**
   - Posada's *Cartas de Caldas* (1917, Biblioteca de Historia Nacional vol. 15) exists only at Banrep. That host is robots-blocked from here, including the CONTENTdm API download.
   - The book is not mirrored on archive.org. archive.org has only BHN volumes of 1902–1906.
   - *Repertorio Colombiano* is not on archive.org. HathiTrust is robots-blocked.
   - FTS for the exact dates ("febrero 6 de 1809", "marzo 6 de 1809", "21 de enero de 1809" + Santafé) and for "Mi querido Arroyo" found no Caldas text.
   - **These letters remain the top human-retrieval target** (see §4).
2. **NEW, INDEPENDENT POPAYÁN EVIDENCE (strongest result).** Santiago Pérez Valencia's Popayán earthquake register, printed by Joaquín Acosta in 1849, contains an interpolated remark in Pérez Valencia's own hand. It compares a sunset dimming of 24 April 1815 "and following days" with the same appearance **"en diciembre de 1808 y enero de 1809"**.
   - This gives the Dec 1808 – Jan 1809 phenomenon at a **second site, Popayán**, about 300 km SSW of Bogotá.
   - The witness is one of Caldas's own Popayán observers, but the text is not derived from Caldas's printed Noticia.
   - It also implicitly links the 1808–09 appearance to the post-Tambora sky of April 1815.
3. One fragment of a **1809 Caldas letter to Arroyo** was found, quoted in a modern anthology (*Soy Caldas*, Libros al Viento). It concerns his job and salary security after Mutis's death, not the sky (§2).
4. Camilo Torres (Caldas's circle) wrote to Popayán in 1809:
   - to his brother Jerónimo, 5 Feb 1809;
   - to Santiago Pérez Valencia, 5 Jun 1809;
   - other letters of 6, 20 and 21 Jun 1809 printed in *Boletín de Historia y Antigüedades* vol. 5.

   All the snippets seen are political (Junta Central elections). **No sky content was seen.** Torres's letters to Arroyo were printed in *Repertorio Colombiano* vol. XVIII ("Cartas de Camilo Torres"), which was not reached.

---

## 1. Pérez Valencia's Popayán register (Acosta 1849)

### Source
J. Acosta (ed.), *Viajes científicos a los Andes ecuatoriales ó colección de memorias sobre física, química e historia natural de la Nueva Granada, Ecuador y Venezuela* (París: Lasserre, 1849). The material is in Acosta's note on the New Granada earthquake of 16 Nov 1827 ("París, abril 10 de 1828"). Page 79 has the heading **"Temblores en Popayan desde fines del siglo pasado."**

Two independent scans:
- `viajescietifico00bous`: https://archive.org/details/viajescietifico00bous, printed p. 79. Viewer: https://archive.org/details/viajescietifico00bous/page/79
- `viajescientfico00acosgoog` (Google scan): https://archive.org/details/viajescientfico00acosgoog, viewer p. 85.

### Provenance
p. 79, OCR, reassembled from consecutive verbatim fragments:
> "Posteriormente el virtuoso ó ilustrado patriota don Santiago Perez Valencia me confió el registro original que por muchos años ha llevado en Popayan, y que publico aquí sin privarlo dé la indicación de algunos sucesos coetáneos que están también intercalados de su propia mano en él, y que, aunque ajenos de este lugar, le dan mayor carácter de actualidad."

"Later the virtuous and enlightened patriot don Santiago Pérez Valencia entrusted me with the original register that he has kept for many years in Popayán. I publish it here without removing the notes of some contemporary events, also inserted in his own hand, which, though foreign to this place, give it greater immediacy."

### The row
p. 79. Columns: date | hour | remarks.
> "1815. — 13 de junio. | A las 12 del dia. | Oscuridad del sol al ponerse e[l] 24 de abril del mismo año y signier.tes [siguientes] como en diciembre de 1808 y enero de 1809."

"1815, 13 June, at noon [tremor]. Darkness of the sun at setting on 24 April of the same year and following [days], as in December 1808 and January 1809."

The next remark: "El 30 de abril de 1816, meteoro luminoso á las ocho de la noche que estalló con explosión ruidosa. (Erupciones cutáneas malignas.)"

### Checks
- **Row attribution:**
  - In the OCR boxes of `viajescietifico00bous` p. 79, "1815. — 13 de junio." sits at top 2808 / left 569 and "Oscuridad…" at top 2810 / left 1257. They are on the same line, with the remark in the right-hand column.
  - The Google scan, p. 85, reads continuously "1815. — 13 de junio. A las 12 del día. Oscuridad del sol al ponerse e…".
- **Other rows nearby:** 1805 (16 Jun, 3 a.m., "Bastante notable"), 1812 (28 May, 11½ p.m., "Bastante fuerte"), 1816 (28–29 Nov).
- **No 1808 or 1809 tremor rows:** in this book "1808" occurs only in this remark, in an Aragua coffee statistic, in an altitude of "1808 metros" and in Caldas's 1808 meteorology. "1809" occurs only in this remark.
- **Extent of the register:** Hassaurek, *Four years among Spanish-Americans* (1867/68), p. 91 (archive.org `cu31924021200658`), says Pérez Valencia "for forty years kept a register". "According to this register, Popayan experienced one hundred and two earthquakes between the years 1805 and 1841."

### Assessment (per common rules)
| Field | Value |
|---|---|
| Observer | Santiago Pérez Valencia (Popayán lawyer and patriot). The 1809 Semanario names him, with Antonio Arboleda, as Caldas's Popayán rain observer. |
| Place | Popayán, 2.44°N 76.6°W, about 1,760 m |
| Event date | Dec 1808 and Jan 1809 (month resolution; no days). Comparison event: 24 Apr 1815 "y siguientes". |
| Writing date | The remark was written after 24 Apr 1815, so the 1808–09 reference is a recollection about 6 years later (or a cross-reference to an earlier entry in his register). The register was handed to Acosta after 1828 and printed in 1849. |
| Excerpt | above (OCR) |
| Repository of original | unknown (the Pérez Valencia register; possibly Acosta papers, or Archivo Central del Cauca) |
| Verification | OCR via archive.org inside.php, two scans; no page image |
| Independence | Independent of Caldas's Bogotá Noticia (different site and writer). Same scientific circle, so he may have known of Caldas's account. |
| What it shows | The optical phenomenon (dimmed or reddened sun at setting) was seen in Popayán in **both December 1808 and January 1809**. It fits Caldas (Bogotá, veil from 11 Dec 1808 and still current ~early Feb 1809). |
| Alternatives | Dry-season biomass-burning smoke (Dec–Feb is the drier season in the Cauca valley). Local volcanic degassing (Puracé, Sotará); no catalogued 1808–09 eruption (pass 3). |
| Extra | The observer equates 1808–09 with April 1815. 24 Apr 1815 is 14–19 days after Tambora's climax (5–11 Apr 1815). That timing is fast but compatible with equatorial stratospheric transport (Krakatau 1883 circled the globe in about 13 days). This supports reading 1808–09 as a stratospheric aerosol veil of the same type. Treat the 1815 link as suggestive only, and flag it for the Tambora literature. |

**Follow-ups:**
- Read the page image of p. 79 to confirm the OCR, especially "signier.tes" and the column alignment.
- Find the manuscript register.
- Check whether Acosta's 1828 note was also printed in French (1828–30) with the table. One FTS attempt in French found nothing.

---

## 2. Caldas's letters, Dec 1808 – Jul 1809: what was found

| Item | Result |
|---|---|
| Caldas → Arroyo, 21 Jan / 6 Feb / 6 Mar / 6 Jun 1809 | **Text not reached.** The only modern quotation found is in *Soy Caldas* (Libros al Viento/Idartes, PDF, no page numbers): "De este modo – le comentaba a su amigo Arroyo en 1809– he asegurado el plan a los treinta y nueve años de trabajos. Con qué lentitud y con qué miseria se pagan los conocimientos." This is about his post and salary after Mutis's death (Sept 1808). The month is not given. No sky content. |
| Pacheco, *La Ilustración en el Nuevo Reino* (1975) | Cites a Caldas → Arroyo letter of "Santafé, 6 febrero 1808" (Cartas de Caldas p. 259). Snippet only. Note: **1808, not 1809**. It may be the same as the "6 Feb 1809" of the 1978 census (a date slip in one source?). **Unresolved: check in Posada 1917 p. 259.** |
| EAFIT *Catalejo*, Puerta Olaya, "Ciencia criolla: El Semanario de Caldas" | Cites Caldas → Arroyo letters of 20 Mar 1801, 5 Apr 1801, 6 Nov 1807 and 5 Aug 1811 (Semanario's end). Nothing for Dec 1808 – Jul 1809. Note "6 Nov 1807": the pass-3 census row "6 Nov 1808, Quito" may be this letter, misdated. |
| Gómez Hoyos, *La Revolución Granadina de 1810* (1962; Tomo II 1982) | FTS snippet "6 de febrero de 1809 tom[ó] posesión de un empleo concedido tan precariamente". The subject could not be confirmed (inside.php URL too long, or a lending copy). It may refer to Caldas's appointment; unverified. |
| Appel (1994), *Francisco José de Caldas: a scientist at work* (TAPS 84) | archive.org lending copy `franciscojosedec0000appe`. inside.php is refused for lending items, so it could not be searched. |
| *Boletín de Historia y Antigüedades* vols 1–14 (archive.org `boletndehistor01…14colouoft`) | vol. 8: no Caldas–Arroyo letter of 1809 (one 1902-era reference to a Caldas letter "publicada en…"). vol. 5: Camilo Torres letters of 6, 20 and 21 Jun 1809 and Popayán 5 Jun 1809, all on the election of the deputy to the Junta Central. vol. 10: Tanco–Caldas and Torres 21 Oct 1809 items. No sky content in any snippet. |
| Ibáñez, *Crónicas de Bogotá* vol. 2 (`raha_103298`) | p. 251 quotes "Cartas de Camilo Torres" to Arroyo from *Repertorio Colombiano* xviii, about **1804** (death of Archbishop Portillo). This confirms that RC vol. XVIII holds Torres → Arroyo letters. |
| Acosta 1849, other "1809" hits | none besides §1 |

---

## 3. Redactor Americano (Bogotá), Dec 1808 – Mar 1809

- **Universidad Distrital repository.** It holds single-article clippings (TIFF) catalogued by subject, e.g. Redactor No. 33 (4 Mar 1808) and a Redactor item of 19 Apr 1807 on drought rogativas (handle 11349/94783). The DSpace REST and OAI endpoints and the handle resolver all failed from here (client error). WebSearch surfaced no item dated Dec 1808 – Mar 1809. **Not reached.** A human should search the repository UI for "Redactor Americano" and filter dc.date.created to 1808-12 … 1809-03.
- **Castro Henao (2012), *Lingüística y Literatura* 61** cites Redactor and Alternativo issues only up to ERA No. 47 (4 Nov 1808). It has no Dec 1808 – Mar 1809 content.
- **Posada, *Bibliografía bogotana*** (1917–25) is digitized at the Wellcome Collection (https://wellcomecollection.org/works/yp5q8at3). It is useful for listing the surviving Redactor issues; it was not searched.

---

## 4. Open leads for a human (with download points)

1. **Posada (ed.), *Cartas de Caldas*, Bogotá 1917 (BHN vol. 15), public-domain PDF at Banrep:** http://babel.banrepcultural.org/cdm/ref/collection/p17054coll10/id/4076. Read the Arroyo letters of 21 Jan, 6 Feb and 6 Mar 1809, and check p. 259 (6 Feb 1808 or 1809?). Look for: "sol", "nube", "velo", "fenómeno", "Popayán", "Pasto", "Neiva", "Tunja", "Santa Marta", and whether Caldas asks Arroyo, Arboleda or Pérez Valencia for their observations.
2. ***Repertorio Colombiano*, vol. XVIII (and 1897–98 volumes)**, which holds the "Cartas de Camilo Torres" and the Caldas–Arroyo letters. HathiTrust full view likely: https://catalog.hathitrust.org/ (search "Repertorio colombiano"; blocked from here).
3. **Page image of Acosta 1849, p. 79** (archive.org, above). The manuscript Pérez Valencia register is not located; suggested places are Archivo Central del Cauca (Popayán) and the Acosta papers.
4. **UD repository, Redactor Americano clippings Dec 1808 – Mar 1809:** https://repository.udistrital.edu.co/ (search "Redactor Americano").
5. **Appel 1994 (archive.org lending copy):** https://archive.org/details/franciscojosedec0000appe. Borrow it and check its chapter on 1808–09 and the letters to Arroyo.
6. **Camilo Torres, letters to Jerónimo Torres (5 Feb 1809) and to S. Pérez Valencia (5 Jun 1809).** They are cited in Altez (ed.) 2012, archive.org `altez-r.-ed.-las-independencias-hispanoamericanas-un-debate-para-siempre-2012`. Check them for any remark on the sky.

---

## 5. Search log

| Repository / tool | Query | Result |
|---|---|---|
| archive.org advancedsearch | title:(repertorio colombiano); repertorio AND colombiano | 1 and 14 unrelated hits; RC not on archive.org |
| archive.org advancedsearch / metadata | (caldas AND cartas) OR title:(biblioteca de historia nacional) | BHN vols 1902–1906 only (bibliotecadehis00/01/02/03histgoog); vol. 15 absent |
| archive.org metadata | p17054coll10_4076 | empty (Banrep item not mirrored) |
| archive.org advancedsearch | identifier:p17054coll10_* AND (caldas OR cartas) | 0 |
| Banrep CONTENTdm API | /digital/api/collection/p17054coll10/id/4076/download | robots-disallowed |
| archive.org FTS | "Arroyo" "Caldas" 1809 | secondary works only |
| archive.org FTS | "Caldas" "Arroyo" "nube" | Acosta 1849 (Cotopaxi cloud), noise |
| archive.org FTS | "febrero 6 de 1809" | 8 hits, Río de la Plata/Charcas, none Caldas |
| archive.org FTS | "marzo 6 de 1809" | 15 hits, none Caldas |
| archive.org FTS | "21 de enero de 1809" Santafé | 8 hits, none Caldas |
| archive.org FTS | "Mi querido Arroyo" | 429 once, then 6 hits, none Caldas |
| archive.org FTS | "empleo concedido tan precariamente" | Gómez Hoyos 1962/1982 (subject unconfirmed) |
| archive.org FTS | "ha dos meses observamos" | 0 (Semanario not in FTS index) |
| archive.org FTS | "diciembre de 1808 y enero de 1809" | **Acosta 1849 ×2 (Pérez Valencia remark)**; others irrelevant |
| archive.org FTS | "Perez Valencia" Popayan temblores | Acosta 1849; Hassaurek 1867/68; Groot; BHA |
| archive.org FTS | "Perez Valencia" Popayan tremblements; Popayan soleil 1808 1809 tremblement | no French reprint found |
| archive.org FTS | Caldas AND identifier:boletndehistor* | filter unsupported (0) |
| archive.org FTS | "Santiago Arroyo" Caldas carta 1809; "Camilo Torres" Arroyo 1809 | Torres letters 1809 (BHA 5, 10; Altez 2012); Ibáñez vol. 2 |
| archive.org FTS | "Jerónimo" "5 de febrero de 1809" | Altez 2012 only |
| archive.org FTS | "Semanario" "Arroyo" "suscriptores" Caldas | 429, not read |
| inside.php | viajescietifico00bous: 1809, sol, abril, meteoro, 1812, 1815, 1816, junio, temblores, Popayan, Valencia, "Perez Valencia", "registro original", Oscuridad, 1808 | §1 |
| inside.php | viajescientfico00acosgoog: Oscuridad | p. 85 confirms |
| inside.php | larevoluciongran0000rafa; franciscojosedec0000appe | error (lending items) |
| inside.php | Gómez Hoyos Tomo II; Altez 2012 | URL too long for proxy |
| inside.php | popayanenlacolon00olan: 1808 | political only |
| inside.php | cu31924021200658 (Hassaurek): Valencia, register | p. 91 |
| inside.php | raha_103298 (Ibáñez): Arroyo, Popayán, Torres | p. 251, Torres → Arroyo 1804, from RC xviii |
| inside.php | boletndehistor08colouoft: Arroyo | nothing relevant |
| inside.php | boletndehistor05colouoft: 1809 | Jun 1809 election letters |
| archive.org djvu.txt | viajescietifico00bous full text | WebFetch only exposes the first 78 k characters; p. 79 not reachable that way |
| archive.org page image | /download/…/page/79.jpg | client error |
| WebSearch | Cartas de Caldas 1917 BHN XV pdf | Wellcome Bibliografía bogotana; no Cartas |
| WebSearch | Caldas Arroyo 1809 Semanario febrero; … sol nube humo | nothing new |
| WebSearch | Cartas de Caldas 1978 pdf; Cartas de Caldas ilustradas pdf | Museo Nacional catalogue; Soy Caldas PDF |
| WebSearch | Repertorio colombiano 1897/98 Caldas Arroyo; tomo XVIII Camilo Torres | nothing digitized found |
| WebSearch | Pérez Valencia Popayán temblores Acosta 1815; Acosta 1828 tremblement | nothing |
| WebSearch | Redactor Americano 1809 udistrital | items of 1807–08 only |
| UD repository | REST discover; OAI; handle 11349/34194 | client errors |
| redcol.minciencias | VuFind search | server error |
| googleapis books | volumes search | client error |
| HathiTrust catalog | repertorio colombiano | robots-disallowed |
| U. Rosario bitstream cea7e375… | – | 1924 Revista del Rosario, irrelevant |
| EAFIT Catalejo PDF | Caldas letters cited | §2 |
| Museo Nacional CALDAS.WEB.pdf | 1809 letters | none |
| Idartes *Soy Caldas* PDF | 1809 letters | §2 quote |
| bffrepositorio UNAL bitstream 004b9cb0… | Noticias meteorológicas | known Noticia text (pp. 355–356) |

---

## Source register

| Source / edition | Region / lang | Type | Covers 1808–09? | URL | Opened from here? |
|---|---|---|---|---|---|
| Acosta (ed.), *Viajes científicos a los Andes ecuatoriales* (1849), p. 79, Pérez Valencia register | Popayán / es | printed register | **yes (Dec 1808, Jan 1809)** | https://archive.org/details/viajescietifico00bous | yes (OCR via inside.php) |
| Same, Google scan | es | printed | yes | https://archive.org/details/viajescientfico00acosgoog | yes (OCR) |
| Hassaurek, *Four years among Spanish-Americans* (1867/68), p. 91 | en | travel book | describes register 1805–1841 | https://archive.org/details/cu31924021200658 | yes (OCR) |
| Posada (ed.), *Cartas de Caldas* (1917, BHN 15) | es | letters | yes | http://babel.banrepcultural.org/cdm/ref/collection/p17054coll10/id/4076 | blocked (robots, incl. API) |
| Cervantes Virtual record of the above | es | catalogue | – | https://cervantesvirtual.com/portales/escuela/obra/cartas-de-caldas-1168856/ | yes |
| *Biblioteca de historia nacional* vols (1902–06) | es | series | no (early vols) | https://archive.org/details/bibliotecadehis00histgoog | metadata yes |
| *Repertorio Colombiano* vol. XVIII and 1897–98 | es | periodical | likely (Caldas and Torres letters) | no URL found (HathiTrust catalog https://catalog.hathitrust.org/ blocked) | blocked |
| *Boletín de Historia y Antigüedades* vols 1–14 | es | periodical | 1809 political letters | https://archive.org/details/boletndehistor05colouoft (vols 01–14 same pattern) | yes (inside.php) |
| Ibáñez, *Crónicas de Bogotá* vol. 2 | es | history | cites RC xviii | https://archive.org/details/raha_103298 | yes |
| Pacheco, *La Ilustración en el Nuevo Reino* (1975) | es | history | cites letters | https://archive.org/details/pacheco-ilustracion-1975 | FTS snippets |
| Gómez Hoyos, *La Revolución Granadina de 1810* (1962; Tomo II 1982) | es | history | 1809 | https://archive.org/details/larevoluciongran0000rafa | FTS snippets; inside blocked |
| Appel 1994, *Francisco José de Caldas* (TAPS 84) | en | monograph | likely | https://archive.org/details/franciscojosedec0000appe | lending; not searchable |
| Altez (ed.) 2012, *Las Independencias Hispanoamericanas* | es | essays | Torres letters 1809 | https://archive.org/details/altez-r.-ed.-las-independencias-hispanoamericanas-un-debate-para-siempre-2012 | FTS snippets |
| *Soy Caldas* (Libros al Viento, Idartes) | es | anthology | 1809 letter fragment | https://idartesencasa.gov.co/sites/default/files/libros_pdf/65.%20Soy%20Caldas.pdf | yes |
| Amaya & Suárez 2018, *Ojos en el cielo* (Museo Nacional) | es | catalogue | no | https://www.museonacional.gov.co/Publicaciones/Expo_en_casa/Documents/CALDAS.WEB.pdf | yes |
| Puerta Olaya, "Ciencia criolla: El Semanario de Caldas", *Catalejo* (EAFIT) | es | article | no | https://publicaciones.eafit.edu.co/index.php/revista-catalejo/article/download/6617/5340/24100 | yes |
| Castro Henao 2012, *Lingüística y Literatura* 61 | es | article | Redactor to Nov 1808 | https://www.redalyc.org/pdf/4765/476549333010.pdf | yes |
| *Popayán en la colonia* (Olano 1910) | es | history | political | https://archive.org/details/popayanenlacolon00olan | yes |
| Redactor Americano clippings (UD repository) | Bogotá / es | newspaper clippings | yes (if catalogued) | https://repository.udistrital.edu.co/items/2db75d4f-691f-49f6-85be-d4296c8e907b/full (No. 33, 1808) | item pages yes; search no |
| UD repository, Redactor 19 Apr 1807 rogativas item | es | clipping | no (1807) | https://repository.udistrital.edu.co/signposting/describedby/d7ab5ee2-5e15-48f6-a50b-568dc421d531 | yes |
| UD repository, Semanario 1808 collection | es | periodical | to Nov 1808 | https://repository.udistrital.edu.co/collections/fe3091fd-26ab-49c6-9f76-fce483275a89 | yes |
| Posada, *Bibliografía bogotana* (1917–25), Wellcome | es | bibliography | lists imprints | https://wellcomecollection.org/works/yp5q8at3 | record yes; not searched |
| UNAL *Obras completas* "Noticias meteorológicas" | es | reprint | yes (Noticia) | https://bffrepositorio.unal.edu.co/server/api/core/bitstreams/004b9cb0-49b7-4d43-851a-83f56340e3ff/content | yes |
| Revista del Rosario 1924 (U. Rosario repository) | es | periodical | no | https://repository.urosario.edu.co/bitstreams/cea7e375-92f4-4e17-9b52-13c880dc087d/download | yes |
| ACCEFYN *Cartas de Caldas* (1978); *Cartas … ilustradas* (2016) | es | letters | yes | https://repositorio.accefyn.org.co/jspui/handle/001/1296 | blocked (bot wall, pass 3) |
| redcol.minciencias (Colombian aggregator) | es | catalogue | indexes UD items | https://redcol.minciencias.gov.co/Record/UDISTRITA2_7a1388f42fcdc60b7feb6eb9bcf7035c/Cite | record yes; search server error |
