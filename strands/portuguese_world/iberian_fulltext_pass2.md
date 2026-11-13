---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: portuguese_world
date: undated
---

# Iberian full-text pass 2: Spanish and Portuguese material, Sept 1808 – 1810

Compiled 2026-10-16 by a second-pass worker.
- Status: PARTIAL. The WebFetch budget, shared across agents at 400 calls per hour, was exhausted four times. See §5 and the leads in §6.
- Scope: Spanish- and Portuguese-language periodicals and books digitized on the Internet Archive (IA). This includes books published 1809–1819 or later that reprint dated 1808–09 observations, and English/French books on Iberian America and Brazil.

## 0. Method

### Tools used
- **IA metadata** `advancedsearch.php`: works. Without URL-encoding, quoted phrases fail with "query missing".
- **IA per-item search** `https://<server>/fulltext/inside.php?item_id=X&doc=X&path=<dir>&q=term`: works. The server and dir come from `archive.org/metadata/X`.
- **IA library-wide full-text search (FTS): NEW and highly productive.**
  - `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=<q>&hits_per_page=100`
  - Restrict by year with `&filter_map={"year":{"1808":"gte","1840":"lte"}}`.
  - Restrict to one collection with `&page_type=collection_details&page_target=<collection>`.
  - Lucene `+"phrase" +term` gives document-level AND. A plain `AND` returns 0 hits. Bare terms are ORed.
  - Long URLs (above ≈ 230 characters) are refused by the proxy.
  - The WebFetch summariser truncates long hit lists to about 35–60 hits and often refuses to quote every snippet. **Long-list results are therefore incomplete.**

### Verification level
Everything below is IA OCR text passed through the WebFetch summariser. No page images were viewed.

## 1. Bottom line
1. **No dated observation of haze, dimmed or odd sun, unusual twilight, ashfall, detonations or eruption news for Sept 1808 – 1810 was found in any Spanish- or Portuguese-language item reached in this pass.** This adds substantial new negative coverage. The most important new negatives are:
   - ***Gaceta de Caracas* t. I** (1939 facsimile; IA `gacetadecaracas0001vari`; 462 images). It runs continuously from no. 1 (24 Oct 1808) to about mid-1810, including every issue for Dec 1808 – Feb 1809. Searches for temblor, terremoto, volcan, niebla, ceniza, humo, polvo, estruendo, calor, lluvias, sequia, tempestad, cometa, fenomeno and atmosfera found only figurative or military uses (§2.1). **This closes the "Gazeta de Caracas not examined" gap in spanish_north.md.**
   - ***Gazeta del Gobierno de México* t. I** (IA `gazetadelgobiern01unkn`; Oct 1809 news onward, Jan–June 1810 issues). Nothing relevant (§2.2).
   - ***Diario de Mallorca*** (Palma). IA holds a complete daily run for Nov 1808 – Mar 1809, 151 issues in the `DiarioDeMallorca` collection, sourced from BVPH. Each issue carries "Observaciones Meteorológicas de ayer": thermometer, barometer, and an "Atmósfera" column at 3 hours, plus sunrise and sunset. The OCR of the table is badly garbled, and in the sampled 1808–09 issues the "Atmósfera" column seems to hold only wind directions. Collection-wide FTS for niebla, neblina, vapores, nublado, sereno, nubes, cubierto and calima gave no sky-state hit for 1808–09 (§2.3). **Palma is a lead that needs page images. It is not a negative.**
2. **Lead — a daily Barcelona diary:** Raimundo Ferrer, *Barcelona cautiva* (Barcelona: Brusi, 1815, 8+ vols). This is a day-by-day diary of occupied Barcelona from Feb 1808. Vol. 3 (about Jan–Dec 1809) was searched for niebla, sol and cielo: only military, figurative or ordinary weather references.
   - Vol. 3, p. 174: "el cielo ha enervado con la lluvia las operaciones terrestres y con el viento las marítimas". Ordinary weather; the date is not established.
   - Vols. 2 and 4 were not searched (budget).
3. **False positives eliminated:**
   - Humboldt, *Ensayo político sobre la Nueva España*, Spanish edition of 1827 (IA `cihm_18394`), reads "[paso de] mercurio sobre el sol, el dia 9 de noviembre de 1809". This is a misprint or translation error for Humboldt's transit of Mercury at Callao on 9 Nov 1802. It is irrelevant.
   - The *Diario de Mallorca* "Sol: Pálido el tirano" (26 Oct 1808) is a patriotic poem by Arriaza, reprinted in *Poesías patrióticas* (1810) and elsewhere.
   - "Manifiesto de las operaciones del Exército del Centro desde 3 dic. 1808 hasta 17 feb. 1809" (IA `bub_gb_Pfh5Z4qHOpMC`): "La densa y fuerte niebla que habia, fue seguramente la causa de que los…". This is ordinary winter fog during operations in La Mancha. Toreno's history has the same fog ("sobreviniendo tras de nieve y ventiscas espesa niebla"). Neither is evidence of a dry fog.
   - The Guatemalan festival relation *Guatemala por Fernando Séptimo el día 12 de diciembre de 1808* (1809; JCB; IA `guatemalaporfern00unkn`):
     - p. 64: "tostados con el rigor del Sol" (dry-season heat).
     - p. 27: "la atmosfera iluminada con cohetes" (fireworks).
     - p. 32: "ni los signos del Cielo, ni las señales de la tierra pudieron hacerla preveer". This refers to an earlier agricultural calamity, not a sky anomaly.

     No haze or odd-sun remark appears for 12–14 Dec 1808 in Guatemala City. This is a useful negative, being one day after Caldas's first sighting, though festival relations seldom note weather.

## 2. Detail by source

### 2.1 *Gaceta de Caracas*, t. I (1808–1810)
- **Item:** IA `gacetadecaracas0001vari`, https://archive.org/details/gacetadecaracas0001vari. Metadata: date 1810, volume 1, 462 images.
  - The page headers give "1808 ~1810". This is evidently the Academia Nacional de la Historia facsimile (Paris, 1939), t. I.
  - p. 11: "salió a luz el 24 de octubre de 1808".
- **Issue sequence confirmed by the hits:**
  - 1808: Viernes 28 Oct (p. 21), 31 Oct (p. 25), 4 Nov (p. 27), 11 Nov (p. 31), 22 Nov (p. 45), 25 Nov (p. 49), 29 Nov (p. 53), 9 Dic (p. 61), 20 Dic (p. 69), 30 Dic (p. 73).
  - 1809: 3 Ene (p. 77, no. 18), 6 Ene (p. 81), 13 Ene (p. 89), 3 Feb (p. 101), 10 Feb (p. 105), 17 Feb (p. 109), 24 Feb (p. 113), up to 22 Dic 1809 (p. 257).
  - 1810 issues follow, to p. ~460.
- **Searches and results:**
  - temblor 0; terremoto 0.
  - volcan 2: p. 178, the personal name "Da. Petronila Volcan"; p. 370, figurative ("el volcan del comun deseo").
  - niebla 3, all figurative: p. 305; p. 339; p. 406 "la niebla pestilente de la Laguna", which is figurative or political.
  - ceniza 1: p. 137, "reducir á ceniza una ciudad abierta", military.
  - humo 3: p. 42 holocausts; p. 149 battle; p. 238 burned houses.
  - estruendo 5: artillery or figurative.
  - polvo 4: figurative.
  - calor 5: figurative.
  - tempestad 8: political.
  - atmosfera 1: p. 110, a whirlwind metaphor in a political essay of Feb 1809.
  - lluvias 0; sequia 0; cometa 0; fenomeno 0.
- **Result:** NEGATIVE. The paper prints no local weather, sky or seismic news for Caracas in Oct 1808 – 1810, as far as OCR reveals.
- **Dated news content relevant to other strands:** p. 18 "Santa Fé, 7 de Setiembre de 1808"; p. 103 a letter from Lima dated 8 Oct 1808; p. 105 Guatemala, 14–15 Aug 1808; pp. 273–275 Santa Fé, 8 Dec 1809. None of these mentions natural phenomena in OCR.

### 2.2 *Gazeta del Gobierno de México*, t. I (1810)
- **Item:** IA `gazetadelgobiern01unkn`, John Carter Brown Library (JCB) copy, 366 images. Other volumes on IA: 4 pt. 1–2, 5 pt. 1–2, 6, 6 pt. 1, 7, 9 pt. 5, 11, `00unkn_5`, all dated 1810 in metadata.
- **Searches and results:**
  - temblor 0; ceniza 0.
  - volcan 1: p. 40, figurative.
  - heladas 1: p. 80, "aquellas heladas regiones", a European war report.
  - escasez 6: war or politics. p. 103 "enmedio de la escasez que se padece" has unclear context.
  - "1809": 12 hits, all Peninsular war datelines from Oct–Nov 1809.
- **Result:** NEGATIVE for this volume.
- **Not on IA:** the *Gazeta de México* proper for 1808–09 (t. XV–XVI), and the *Diario de México* for 1808–10. IA has only the 1806 *Diario* (`diariodemxico02bustgoog`, with 0 hits for "1809") and a 1808 single-sheet letter (`seoreditordeldia00nava`).

### 2.3 *Diario de Mallorca* (Palma), daily, Nov 1808 – Mar 1809 complete on IA
- **Items:** IA collection `DiarioDeMallorca` (2,037 items, 1808–1814; uploaded from BVPH). Identifiers have the form `DiarioDeMallorca_YYYYMMDD`. All 151 issues for 1 Nov 1808 – 31 Mar 1809 are present.
- **Daily table:** "Observaciones Meteorológicas de ayer". Rows at 7 a.m., noon and evening. Columns: Termómetro, Barómetro, Atmósfera, plus "Afec. Ast. de hoy", i.e. sunrise and sunset.
- **Example, 5 Jan 1809 issue (OCR):** "Observaciones Meteorológicas de ayer. Afec. Ast. de hoy / … Wermómer.] Barómet. Armósfera.| Sale eTsola las 7 / … |27 px tale ENE. |y 20m. 42.5. … OSO. … se pone las 4". The "Atmósfera" column apparently holds wind direction (ENE, OSO, NNO …), sometimes with a weather word.
  - A 1811 example hit: "ONO-sereno" (1 Oct 1811).
  - A 1813 example hit: "Nubes y aguas".
- **Samples read in full:** 10 Dec 1808 (no table that day), 12 Dec 1808, 17 Dec 1808, 25 Dec 1808, 5 Jan 1809, 19 Jan 1809, 12 Feb 1809. Wind only was legible. No sky-state words were legible for Dec 1808 – Feb 1809.
- **Collection-wide FTS:**
  - niebla 25 hits. 1809 hits are military fogs: 7 Feb 1809, "densisima niebla" covering escaping emigrants at sea; 28 Feb 1809, "densa niebla" stopping operations; 20 May 1809. Also a 25 Jan 1814 description of "niebla, ó nube de color de aurora". That is outside the window, but would be worth reading if 1814 matters.
  - neblina 0; calima 0; vapores 2 (figurative); nublado 2 (figurative); sereno 17 (1 Apr 1810 "un cielo el mas hermoso, despejado y sereno"; no 1808–09 table hits); nubes 10 (none in 1809); cubierto (no sky uses).
- **Assessment:** this is a potentially valuable daily Mediterranean series. The OCR does not permit reading the sky column. **Lead:** view page images via BVPH or IA for Dec 1808 – Mar 1809 and compare with Cádiz "calimoso" days (29 Jan – 2 Feb, 7–8 Feb, 27–28 Feb 1809).

### 2.4 Raimundo Ferrer, *Barcelona cautiva* (Barcelona: A. Brusi, 1815–), diary 1808–1814
- **Items:** IA `barcelonacautiva01ferr` … `05ferr` (5 vols on IA).
- **Vol. 3** (`barcelonacautiva03ferr`, about Jan–Dec 1809):
  - niebla 1: p. 120, the castle of Mongat firing on English frigates (fog in a military context).
  - sol 14: p. 452 "dos horas de sol"; p. 565 "ardor del sol" (meat spoiling, summer); the rest are "soldado".
  - cielo 30: only p. 174 is literal weather ("el cielo ha enervado con la lluvia las operaciones terrestres y con el viento las marítimas").
- **Vol. 2** (Sept–Dec 1808) and **vol. 4:** not searched; the budget ran out. The vol. 2 server is ia800400 /31/items/barcelonacautiva02ferr.

### 2.5 Other Spanish items
- **Juarros, *Compendio de la historia de la ciudad de Guatemala*:**
  - t. I (1808; IA `compendiodelahis11juar`, `compdelahis01juarguat`; 1809 issue `compendiodelahis00juar`).
  - t. II (1818; `compendiodelahis21juar`) is **not indexed for full text** ("not yet indexed").
  - 1857 edition: `compendiodelah102domiguat`, `compendiodelahi00juargoog`.
  - FTS for +"de 1808" +juarros returned these items, but no snippet showed natural phenomena. Not resolved.
- ***Guatemala por Fernando Séptimo el día 12 de diciembre de 1808*** (Guatemala, 1809; JCB; IA `guatemalaporfern00unkn`): see §1, item 3.
- **Humboldt, *Ensayo político sobre la Nueva España*,** Spanish editions on IA: `cihm_18394`, `18395`, `18398` (1827), `cihm_45742` (1822). The "9 de noviembre de 1809" hit is an erratum for the 1802 transit of Mercury.
- **Restrepo, *Historia de la revolución de la República de Colombia*** (1827), vol. 2 (`historiadelarevo02rest_0`): "el volcan arrojó cantidades inmensas de polvo, ceniza". The volcano and year were not checked because of the budget; the narrative starts in 1810. **Open item.**
- **Manifiesto de las operaciones del Exército del Centro** (3 Dec 1808 – 17 Feb 1809; IA `bub_gb_Pfh5Z4qHOpMC`): fog during operations; see §1.
- **Miñano, *Diccionario geográfico universal*** (1828; `b28745954_0002`): mentions the 1811 submarine eruption (Sabrina, Azores). Background only.
- **IA availability of the periodicals named in the brief:**
  - *El Espectador sevillano* 1809 and 1810: `A632861861809`, `A632861861810` (Lista's essay paper; not searched).
  - *Gazeta de Sevilla* 1810 and 1811: `A0632861561571810`, `…1811`.
  - *Gazeta ministerial de Sevilla* 1808: `A0632681544155`. Several 1808–09 single *Gazeta extraordinaria* sheets are also on IA.
  - *Semanario patriótico*: only the Americano of 1812 is on IA.
  - *Memorial literario*: only 1784–87 on IA.
  - Not found on IA: *Correo mercantil de España y sus Indias*, *Diario de Barcelona*, *Diario mercantil de Cádiz* for 1808–10, *Gazeta de la Regencia*, *Telégrafo americano*, *Minerva peruana* 1808–09.
  - One isolated *Diario de Valencia* issue (6 Jun 1808): `diariodevalencia00unkn`.
  - IA `bub_gb_AE58OwK6AecC`: *Gaceta de Madrid* 1808, months not determined. The 1808–09 run is better reached via BOE PDFs.

### 2.6 Portuguese items
- **FTS +"dezembro de 1808" +nevoeiro** (1808–1900; 48 hits): every visible hit is figurative, military, or ordinary morning fog. Examples:
  - *O Telegrafo Portuguez* 1809: "aproveitando-se do nevoeiro, 2 mil e tantos Francezes" (military).
  - Acúrsio das Neves, *Memória sobre os meios de melhorar a indústria portuguesa* (1820): "levantaram um nevoeiro tão espesso sobre todo o horizonte de Portugal" (figurative).
  - *Memórias … Luiz da Motta Feo e Torres* (1825): "um denso nevoeiro, que cerrava o dia" (naval; undated).
- **FTS +"de 1809" +"tremor de terra"** (1809–1840; 28 hits): no tremor dated 1808–1810.
  - Pizarro, *Memorias historicas do Rio de Janeiro* vol. 8 (1820): two tremors, dated 1729 and 1 Aug 1769.
  - *Jornal encyclopedico de Lisboa* (1820): "Dezembro de 1811. Tremor de terra em Caracas" (1811 is outside the window, and the date may be garbled; the great Caracas earthquake was 26 Mar 1812).
- **Pizarro e Araujo, *Memorias historicas do Rio de Janeiro*** (1820–22): all 9 vols on IA, `memoriashistoric01–09piza/ara`. FTS +pizarro +"de 1809" +nevoeiro gives only the 1710/11 French entry into Rio. NEGATIVE.
- **FTS "chuva de cinza"** (1808–1850): 0 hits.
- **On IA but not searched here:**
  - *O Investigador Portuguez em Inglaterra* 1811– (`oinvestigadorpor04unkn`, `21unkn`, `04unkngoog`).
  - *Jornal de Coimbra* vol. 11 (1817).
  - *Gazeta de Lisboa* 1811 (`naofficinadeantoniocorrealemos_gazetadelisboa_1811no154-310`), 1823 and 1824.
  - *Memorias da Academia Real das Sciencias de Lisboa* (1821).
  - *O Telegrafo Portuguez* (1808–09).
  - Isolated 1809 *Gazeta do Rio* extracts: `gazetadelriojane00unkn` (12 Aug 1809), `_0` (9 Aug 1809), `gazetaextraordin00unkn_1` (28 Aug 1809), `extractodelagaze00unkn_1` (3 Jun 1809).

### 2.7 English and French books on Iberian America
- **Dauxion Lavaysse, *A statistical, commercial, and political description of Venezuela, Trinidad…*** (London 1820; IA `statisticalcomme00daux`). Searched "1809": 3 hits (population and sugar statistics only). "haze": 0. The French original of 1813 (`voyageauxilesdet01daux`, `02daux`) and the German edition of 1816 were not searched.
- **Edwards, *History … of the West Indies*** vol. 5 (1819): has "impenetrable haze" near a 31 Dec 1808 date (FTS hit). Context not checked; probably the Saint-Domingue narrative. **Open item.**

### 2.8 Central American catalogue: Montessus de Ballore 1888 (NEW ACCESS)
- **Source:** F. de Montessus de Ballore, *Tremblements de terre et éruptions volcaniques au Centre-Amérique depuis la conquête espagnole jusqu'à nos jours* (Dijon / Société des sciences naturelles de Saône-et-Loire, 1888). IA `tremblementsdet00surgoog`, https://archive.org/details/tremblementsdet00surgoog.
- spanish_north.md listed this catalogue as "not reached". **It is on IA with full text.**
- **"1809" search:** 3 hits, all on p. 143, which are numbered entries:
  - "138. — 1809."
  - "139. — 1809, 20 juillet."
  - "140. — 1809. 20 octobre."

### Entry 138 (1809): Coseguina
OCR as returned (p. 143):
> "[138. — 1809.] Eruption du Coseguina. (Archibald Geykie, Kluge, Fuchs, Caldcleugh.) — [?]oulin [OCR 'A/^ Boulin'] donne cette éruption, d'après la tradition locale, comme ayant eu lieu vingt-six ans avant la grande explosion de 1835. (Comptes rendus de l'Académie des sciences, t. V, p. 75.) D'Archiac donne 1808, se trompant ainsi d'une année, comme pour l'éruption de 1835 qu'il place en 1834."

Translation:
> "Eruption of Coseguina (Geikie, Kluge, Fuchs, Caldcleugh). [?]oulin gives this eruption, according to local tradition, as having taken place twenty-six years before the great explosion of 1835 (Comptes rendus, t. V, p. 75). D'Archiac gives 1808, thus erring by one year, as with the 1835 eruption, which he places in 1834."

**Significance:**
- The **only basis for a "1809" Coseguina eruption is local tradition**: "26 years before 1835". It reached Europe through the Comptes rendus t. V (1837) and through Caldcleugh (1836), who says "twenty-six years of repose".
- No day or month is given. The GVP "28 March 1809" is **not** supported by this catalogue; its source remains untraced.
- D'Archiac's "1808" is an error according to Montessus. It also explains why some lists show "Coseguina 1808".
- Verification level: OCR text via the IA API. The name before "donne" is garbled.

### Entries 139–140 (1809): Honduras earthquakes
- **139:** "1809, 20 juillet." The text of this entry was not retrieved.
- **140:** "1809. 20 octobre. Tremblement de terre général au Honduras, d'après Bockstroh. — La rareté des séismes dans cette République porterait à confondre ce fait avec le pré[cédent], mais sans permettre de choisir entre les deux dates, et à les rattacher peut-être à l'éruption du Coseguina la même année."
  - Translation: "General earthquake in Honduras, after Bockstroh. The rarity of earthquakes in this Republic would lead one to confuse this event with the preceding one, but without allowing a choice between the two dates, and perhaps to connect them with the eruption of Coseguina the same year."
  - The source is Bockstroh, a late, secondary source.
- **Neither entry falls in Dec 1808 – Mar 1809.**
- The following entries on p. 144 belong to later years: "18[1]9, 18 juillet"; "18[?]. 19 octobre", an earthquake at Omoa and San Pedro from Perrey, *Annales de Chimie* t. XV, p. 424, and the *Moniteur* of 23 Nov.

### Entries before 138 (1808 or earlier)
Not retrieved, because the budget ran out. The "1808" search returned only the D'Archiac sentence, so **no Central American event is dated 1808 in this catalogue's OCR**.

### 2.9 W. B. Stevenson, *A historical and descriptive narrative of twenty years' residence in South America* (London 1825)
- **Item searched:** vol. 2, IA `b29350347_0002` (Wellcome copy).
- **Copies on IA:** `historicaldescri01stev`, `ahistoricalandd01–07stevgoog`, `b29350347_0001`, `gri_000133125008562908`, and Gutenberg texts `historicalanddes55775gut` and `55777gut`.
- **Why it matters:** Stevenson was secretary to Ruiz de Castilla, President of Quito.
  - p. 215: "in June, 1808, we embarked at Callao for Guayaquil".
  - p. 367: "I was ordered by the President, in December, 1808, to visit the river Napo". So he was travelling in the Quito and Napo country exactly in Dec 1808.
- **Searches in vol. 2:**
  - "1808": 3 hits (pp. 215, 357, 367).
  - "1809": 6 hits (pp. 20, 344, 375, 414, 426, 443), all incidental "at that time (1809)" remarks.
  - "haze": 0.
  - "eruption": 9 hits, all historical (Cotopaxi 1698, 1738–43, 1768/1774). None is dated 1808–10 or witnessed by the author.
- **Not run:** "fog", "smoke", "sun", "ashes" (budget). The chapter on the Napo journey of Dec 1808 – early 1809 (around pp. 367 ff.) should be read in full. **Lead.**

### 2.10 Other checks
- **Restrepo / Blanco & Azpurúa:** "el volcan arrojó cantidades inmensas de polvo, ceniza y piedras" refers to an eruption of **October 1566**. Irrelevant.
- **FTS +"de 1809" +crepusculos** (1809–1830): 8 hits. All are figurative, except *Jornal de Coimbra* 1819, which is a generic astronomical remark. NEGATIVE.
- **FTS "niebla seca"** (1808–1840): 3 hits. Two are Humboldt's *Viage* (1826), about the Llanos in 1800; one is the *Revista bimestre cubana* of 1831, which is generic.
- **FTS "nieblina"** (1808–1830): 2 hits, both Milton's *Paraíso perdido* in translation.
- **FTS "lluvia de ceniza"** (1808–1840): 3 hits, all literary or historical: Solís on the conquest of Mexico, and a German devotional work.
- **FTS "sol pálido"** (1808–1830): 17 hits, all poetry (Arriaza, Calderón) or fiction (*Eusebio*).
- **FTS "chuva de cinza"** (1808–1850): 0.
- **FTS +1809 +Coseguina** (1810–1900): Caldcleugh 1836, Darwin 1838 and Seebach 1892 all give "1709 and 1809". This is the same tradition as in §2.8, with no independent primary source.

## 3. Dated observations found
**None.** No dated observation of haze, odd sun, twilight, ashfall, detonations, quakes or eruption news for Sept 1808 – 1810 qualifies. The closest datable items are:

| Event date | Place | Source | What it says | Verification | Relevance |
|---|---|---|---|---|---|
| "1809", no day; "26 years before 1835" by local tradition | Coseguina, Nicaragua | Montessus de Ballore 1888, p. 143, entry 138 (citing Comptes rendus t. V p. 75; Caldcleugh) | eruption by tradition only; D'Archiac's "1808" is called an error | OCR via IA API | Undermines the GVP "28 Mar 1809" date. Too late and too small to be the source. |
| 20 Jul 1809 and/or 20 Oct 1809 | Honduras | Montessus 1888, p. 143, entries 139–140 (after Bockstroh) | "Tremblement de terre général au Honduras"; the two dates may be one event; perhaps linked to Coseguina | OCR via IA API | Outside the Dec 1808 window. Background only. |
| 7 Feb 1809 and 28 Feb 1809 (reports) | at sea and Spanish theatre (places not established) | *Diario de Mallorca* issues of those dates | "densisima niebla" covering escaping emigrants; "densa niebla" halting operations | OCR snippets via FTS | Ordinary winter fogs in military news. Not anomalous. |
| Dec 1808 – Feb 1809 | La Mancha (Exército del Centro) | *Manifiesto de las operaciones del Exército del Centro* (1809) | "La densa y fuerte niebla que habia…" | OCR snippet via FTS | Ordinary winter fog. |

## 4. Source register

| Source / edition | Region / language | Type | Covers 1808–09? | Digitized (URL) | Access from here |
|---|---|---|---|---|---|
| *Gaceta de Caracas* t. I (facsimile, 1939) | Venezuela / es | periodical | yes, 24 Oct 1808 – 1810 | https://archive.org/details/gacetadecaracas0001vari | OCR full text searched (negative) |
| *Gaceta de Caracas* t. II (1811) | Venezuela / es | periodical | no | https://archive.org/details/gacetadecaracas0002vari | not searched |
| *Gazeta del Gobierno de México* t. I (1810) and other vols | Mexico / es | periodical | 1810; with Oct–Nov 1809 news | https://archive.org/details/gazetadelgobiern01unkn | OCR searched (negative) |
| *Gazeta de México* t. XV–XVI (1808–09) | Mexico / es | periodical | yes | not on IA (HathiTrust/HNDM) | not reached |
| *Diario de México* 1808–10 | Mexico / es | daily | yes | not on IA (only 1806: diariodemxico02bustgoog) | not reached |
| *Gazeta de Guatemala* 1808–09 | C. America / es | periodical | yes | not on IA (IA has 1797, 1804 t. VII, 1812 *Gazeta del Gobierno*) | not reached |
| *Guatemala por Fernando Séptimo el día 12 de diciembre de 1808* (1809) | Guatemala / es | festival relation | yes, 12–14 Dec 1808 | https://archive.org/details/guatemalaporfern00unkn | OCR searched (negative) |
| Juarros, *Compendio de la historia de la ciudad de Guatemala* t. I (1808/09), t. II (1818), ed. 1857 | Guatemala / es | chronicle | t. II may cover | compendiodelahis11juar, compendiodelahis21juar (not FTS-indexed), compendiodelah102domiguat | t. II not indexed; not searched |
| Montessus de Ballore, *Tremblements de terre et éruptions volcaniques au Centre-Amérique* (1888) | C. America / fr | catalogue | yes | https://archive.org/details/tremblementsdet00surgoog | OCR searched (1808, 1809 entries) |
| Caldcleugh 1836; Darwin 1838; Seebach 1892 (Coseguina) | C. America / en, de | secondary | mentions 1809 | jstor-108021; darwin-online_1838_volcanic_F1649; uebervulkane00seebguat | FTS snippets |
| *Diario de Mallorca* (Palma), daily | Spain / es | daily with weather table | yes, complete Nov 1808 – Mar 1809 and beyond | https://archive.org/details/DiarioDeMallorca (e.g. DiarioDeMallorca_18081217) | OCR (weather table garbled); page images not viewed |
| Ferrer, *Barcelona cautiva* (1815–), vols. 1–5 on IA | Spain / es | daily diary | yes | barcelonacautiva01ferr … 05ferr | vol. 3 searched; vols. 2 and 4 not |
| *Manifiesto de las operaciones del Exército del Centro* (1809) | Spain / es | military report | Dec 1808 – Feb 1809 | https://archive.org/details/bub_gb_Pfh5Z4qHOpMC | FTS snippet only |
| Toreno, *Historia del levantamiento…* (1835–) | Spain / es | history | yes | historiadellevan02toreuoft etc. | FTS snippets |
| *El Espectador sevillano* 1809, 1810 | Spain / es | periodical (essays) | yes | A632861861809, A632861861810 | not searched |
| *Gazeta de Sevilla* 1810, 1811; *Gazeta ministerial de Sevilla* 1808; *Gazetas extraordinarias* 1808–09 | Spain / es | periodicals | partly | A0632861561571810; A0632681544155; gazetaextraordin00unkn_0, _2 | not searched |
| *Gaceta de Madrid* 1808 (Google scan) | Spain / es | periodical | yes | bub_gb_AE58OwK6AecC | not searched (BOE PDFs preferable) |
| *Diario de Valencia*, 6 Jun 1808 (single issue) | Spain / es | daily | no (pre-window) | diariodevalencia00unkn | not searched |
| *Semanario patriótico* (Madrid/Seville 1808–09) | Spain / es | periodical | yes | not on IA (only *Semanario Patriótico Americano* 1812) | not reached |
| *Correo mercantil de España y sus Indias*; *Diario de Barcelona*; *Diario mercantil de Cádiz*; *Memorial literario* 1808 | Spain / es | periodicals | yes | not on IA for 1808–10 (*Memorial* only 1784–87) | not reached |
| *Minerva Peruana* 1808–09; *Telégrafo americano* | Peru, RdlP / es | periodicals | yes | not on IA | not reached |
| Humboldt, *Ensayo político sobre la Nueva España* (1822, 1827 Spanish eds.) | Mexico / es | treatise | no (1803–04) | cihm_18394, 18395, 18398, cihm_45742 | FTS (false positive eliminated) |
| Humboldt, *Viage á las regiones equinocciales* (1826) | Venezuela / es | travel | no (1799–1804) | viagealasregio01–05humb | FTS snippets |
| Restrepo, *Historia de la revolución de Colombia* (1827/1858) | Colombia / es | history | from 1810 | historiadelarevo00rest_0, 02rest_0, 01rest | FTS (1566 eruption) |
| Miñano, *Diccionario geográfico universal* (1828) | general / es | gazetteer | – | b28745954_0002 | FTS snippet (1811 Sabrina) |
| Dauxion Lavaysse, *Statistical … description of Venezuela, Trinidad…* (1820); French original *Voyage aux îles de Trinidad…* (1813); German ed. (1816) | Venezuela / en, fr, de | travelogue | yes (in Venezuela about 1807–10) | statisticalcomme00daux; voyageauxilesdet01daux, 02daux; reisenachdenins00lavgoog | English searched for 1809 and haze (negative); French and German not searched |
| Stevenson, *Twenty years' residence in South America* (1825), 3 vols | Peru, Quito / en | memoir | yes (in Quito 1808–10; Napo trip Dec 1808) | b29350347_0001, _0002; ahistoricalandd01–07stevgoog; Gutenberg 55775, 55777 | vol. 2 partly searched (negative so far) |
| Semple, *Sketch of the present state of Caracas* (1812) | Venezuela / en | travelogue | 1810–11 | not checked | not searched (budget) |
| Walton, *Present state of the Spanish colonies* (1810) | Hispaniola etc. / en | survey | yes | not checked | not searched (budget) |
| Depons, *Voyage à la partie orientale de la Terre-Ferme* (1806) | Venezuela / fr | travelogue | no (pre-window) | – | not searched |
| Mollien (Colombia 1823); Robinson (Orinoco 1819) | Colombia, Venezuela / fr, en | travelogues | no (later) | – | not searched |
| Orozco y Berra (Mexican seismic chronology); Vicuña Mackenna (Chile) | Mexico, Chile / es | compilations | yes | not checked here (Vicuña *Ensayo* done in pass 1) | not searched (budget) |
| Pizarro e Araujo, *Memorias historicas do Rio de Janeiro* (1820–22), 9 vols | Brazil / pt | chronicle | yes | memoriashistoric01–09piza / ara; memriashistrica04aragoog | FTS plus vol. 8 "tremor" (1729, 1769). Negative for 1808–10 |
| Ayres de Casal, *Corografia brazilica* (1817) | Brazil / pt | geography | partly | not checked | not searched (budget) |
| Spix & Martius; Saint-Hilaire; Eschwege | Brazil / de, fr | travelogues | no (arrived 1810 or later) | – | not searched |
| *Gazeta do Rio de Janeiro* 1809 single issues and extracts | Brazil / pt, es | periodical | yes (Jun, Aug 1809) | gazetadelriojane00unkn (12 Aug 1809), gazetadelriojane00unkn_0 (9 Aug 1809), gazetaextraordin00unkn_1 (28 Aug 1809), extractodelagaze00unkn_1 (3 Jun 1809), noticiasrecebida00unkn | found; not searched (budget). The 1808 issues gazeta_rj_1808_003–005 were done in pass 1 |
| *O Telegrafo Portuguez* (Lisbon 1808–09) | Portugal / pt | periodical | yes | otelegrafoportug00unkn, _0 | FTS snippet only (military fog) |
| *Gazeta de Lisboa* 1811, 1823, 1824 | Portugal / pt | periodical | no (1808–09 not on IA) | naofficinadeantoniocorrealemos_gazetadelisboa_1811no154-310 | not searched |
| *O Investigador Portuguez* (1811–); *Jornal de Coimbra* (1812–); *Jornal encyclopedico de Lisboa* (1820) | Portugal / pt | periodicals | retrospective only | oinvestigadorpor04unkn, jornal-de-coimbra-vol-11-1817, jornalencycloped01mace | FTS snippets only |
| *Memorias da Academia Real das Sciencias de Lisboa* (1821) | Portugal / pt | proceedings | possibly | memoriasdaacadem07lisb | FTS snippet only (Limoges tremor) |
| Acúrsio das Neves, *Memória sobre … indústria portuguesa* (1820) | Portugal / pt | treatise | – | memoria-sobre-os-meios-de-melhorar-a-industria-portuguesa-… | FTS (figurative fog) |
| Edwards, *History … of the West Indies* vol. 5 (1819) | Caribbean / en | history | yes | b33287417_0005, in.ernet.dli.2015.92683 | FTS snippet "impenetrable haze" near "31st December, 1808"; context not checked |

## 5. Search log

| # | Tool / repository | Query (variants) | Coverage | Result |
|---|---|---|---|---|
| 1 | IA advancedsearch | title:(gazeta OR gaceta), date 1808–1810 / 1808–1812, NOT language:pol | – | 28 items 1808–09, 389 items 1808–12. Key: gacetadecaracas0001vari; Sevilla, Rio and Madrid sheets |
| 2 | IA advancedsearch | title:mexico + gazeta/gaceta/diario; title:guatemala + gazeta; "diario de mexico" | – | Gazeta del Gobierno de México 1810 vols; no 1808–09 Gazeta de México / Guatemala |
| 3 | IA advancedsearch | semanario patriotico, correo mercantil, memorial literario, espectador sevillano | – | Espectador sevillano 1809–10 only |
| 4 | IA advancedsearch | title:diario, date 1808–1810 | – | Diario de Mallorca daily run (719 hits); Diario de Valencia 6 Jun 1808 |
| 5 | IA advancedsearch | collection:alanjas-newspaper-collections, date Nov 1808 – Mar 1809 | – | 151 Diario de Mallorca issues only |
| 6 | IA inside.php, Gaceta de Caracas t. I | 1808, 1809, temblor, terremoto, volcan, niebla, ceniza, humo, estruendo, polvo, calor, lluvias, sequia, tempestad, cometa, fenomeno, atmosfera, actividad | 1808–10 | negative |
| 7 | IA inside.php, Gazeta del Gobierno de México t. I | temblor, volcan, 1809, heladas, ceniza, escasez | 1810 | negative |
| 8 | IA inside.php, Diario de México (1806) | 1809 | – | 0 |
| 9 | WebFetch djvu.txt, Diario de Mallorca | 10, 12, 17, 25 Dec 1808; 5, 19 Jan 1809; 12 Feb 1809 | – | weather table garbled; wind only |
| 10 | IA FTS within DiarioDeMallorca | calima, Somosierra (control), niebla, neblina, sereno, vapores, nublado, nubes, cubierto | 1808–14 | no 1808–09 sky-state hits |
| 11 | IA FTS global | "diciembre de 1808" niebla (OR); +"diciembre de 1808" +niebla | 1808–1900 | military fogs only |
| 12 | IA FTS global | "niebla seca" | all; 1808–40 | 3 hits in 1808–40, irrelevant |
| 13 | IA FTS | nieblina; "lluvia de ceniza"; "sol palido"; "color de sangre" sol | 1808–1840 | irrelevant |
| 14 | IA FTS | +"diciembre de 1808" +temblor; +"enero de 1809" +temblor | 1808–1930 | 276 and 363 hits; summariser truncated; visible hits are political or unrelated |
| 15 | IA inside.php, Barcelona cautiva vol. 3 | niebla, sol, cielo, Diciembre | 1809 | negative |
| 16 | IA FTS | +"1809" +erupcion +volcan | 1809–1830 | no 1808–10 eruption; Humboldt 1809 typo |
| 17 | IA FTS | +"noviembre de 1809" +volcan | 1822–1830 | false positive (transit of Mercury 1802) |
| 18 | IA FTS / inside | +"de 1808" +juarros; Juarros t. II "1809" | – | t. II not indexed |
| 19 | IA inside.php, Guatemala por Fernando VII | sol, cielo | Dec 1808 | negative |
| 20 | IA FTS | "chuva de cinza" | 1808–1850 | 0 |
| 21 | IA FTS | +"dezembro de 1808" +nevoeiro | 1808–1900 | 48 hits; figurative or military |
| 22 | IA FTS | +"nevoeiro tão espesso" +horizonte | 1810–1830 | figurative (1820) |
| 23 | IA FTS / inside | +pizarro +"de 1809" +nevoeiro; Pizarro vol. 8 "tremor" | – | 1710 fog; tremors 1729, 1769 |
| 24 | IA FTS | +"de 1809" +"tremor de terra" | 1809–1840 | 28 hits; none dated 1808–10 |
| 25 | IA FTS | +"december 1808" +haze | 1809–1830 | 170 hits; nothing Iberian-American |
| 26 | IA inside.php, Dauxion Lavaysse (Eng. 1820) | 1809, haze | – | negative |
| 27 | IA FTS | +"de 1809" +crepusculos | 1809–1830 | figurative |
| 28 | IA FTS | +"de 1809" +(bolcan OR reventazon); +1809 +(Coseguina OR …) | – | 0 (parenthesised OR seems unsupported) |
| 29 | IA FTS | +1809 +Coseguina | 1810–1900 | Caldcleugh, Darwin, Seebach, Montessus |
| 30 | IA inside.php, Montessus 1888 | 1809, 1808, Archiac, Coseguina, octobre, dates, Tremblement, Honduras, juillet | – | entries 138–140 (§2.8) |
| 31 | IA FTS | "cantidades inmensas de polvo" | – | 1566 eruption |
| 32 | IA FTS / inside.php, Stevenson vol. 2 | 1808, 1809, haze, eruption | – | Napo trip Dec 1808; no phenomena in the hits |
| – | WebFetch budget | – | – | **exhausted 4 times** (shared 400 calls per hour). Several planned searches were dropped (§6) |

## 6. Leads and unfinished work, in priority order
1. ***Diario de Mallorca*, Dec 1808 – Mar 1809:** read the daily "Observaciones Meteorológicas" from page images (IA jp2 or BVPH) for sky-state words. This is a daily series directly comparable with the San Fernando "calimoso" days.
2. **Stevenson vol. 2, pp. ~367–380 (Napo journey from Dec 1808):** read in full (Gutenberg 55777 text) for sky, haze, smoke or ash remarks. Search "smoke", "fog", "sun", "ashes", "Tunguragua", "Sangay".
3. ***Barcelona cautiva* vol. 2 (Sept–Dec 1808) and vol. 4:** search niebla, sol, cielo, temblor.
4. **Juarros t. II (1818):** not full-text indexed. Read the earthquake and volcano chapters for 1808–09.
5. ***Gazeta del Rio de Janeiro* 1809 single issues on IA** (gazetadelriojane00unkn, _0; gazetaextraordin00unkn_1; extractodelagaze00unkn_1): small and quick to read.
6. **Montessus 1888:** retrieve entries 130–137 (1800–1808) and the full text of entry 139. Identify "Bockstroh" and the source of the Comptes rendus t. V p. 75 tradition.
7. **Not yet searched:** Dauxion Lavaysse, French 1813; Semple 1812; Walton 1810; Ayres de Casal 1817; *El Espectador sevillano* 1809; *O Telegrafo Portuguez*; *Gaceta de Madrid* 1808 (Google); Edwards 1819 "impenetrable haze" context; Orozco y Berra's seismic chronology.

## 7. Process note
The coordinator's rules forbid hearthbot tools. While waiting for the fetch budget, this worker mistakenly called `mcp__hearthbot__no_reply_needed` once. It posted nothing; the tool only acknowledged.
