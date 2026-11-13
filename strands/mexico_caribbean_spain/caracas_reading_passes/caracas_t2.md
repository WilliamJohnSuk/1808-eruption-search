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

# Gaceta de Caracas, tomo II (facsimile 1939): search for 1808-09 eruption clues

Source: `/mnt/user-data/uploads/Downloads/1808-newspapers/internet_archive/gacetadecaracas0002vari__gacetadecaracas0002vari_djvu.txt` (34,737 lines). "L" numbers below are line numbers in that file. **All quotations are uncorrected Internet Archive OCR only** (labelled [OCR]); I have not checked them against page images.
Method: hyphenated line breaks joined; case-insensitive regex sweep using the Spanish list in `eruption_clue_search_terms.md` (classes 0-9) plus OCR variants and wider weather and sky words (sol, luna, cielo, nubes, calor, frio, lluvia, cosecha, clima, viento, etc.); every hit (~250 contexts) read by eye. Part B: ~600 place-name matches indexed, and every datelined distant item read. Scripts: `scratchpad/scripts/sweep.py`, `scratchpad/scripts/places.py`. Raw hits: `scratchpad/raw_hits_t2.txt`, `raw_extra_t2.txt`, `raw_places_t2.txt`.

## Coverage

The volume is **not a continuous run**. The facsimile seems to bind about 32 issues with large gaps; the OCR shows no other material in between (each issue is about 1,000 lines, and the issues are separated by the "Imprenta de Gallagher y Lamb" colophons). Two numbering series are interleaved. Friday issues carry high numbers: No. 136 (4 Jan 1811), No. 149 (5 Apr), No. 362 (26 Jul), No. 365 (16 Aug). Tuesday issues are marked "Tom. I": No. 14 (8 Jan), No. 41 (16 Jul), No. 45 (13 Aug).

- **First issue:** an issue with no masthead at L~100-1249, probably Tue 1 Jan 1811. It contains the Burke "Derechos de la America del Sur", Quito 1810 events, and Buenos Aires news to Oct 1810, and ends with "Guayra 31 de Diciembre". The first dated masthead is "DEL VIERNES 4 DE ENERO DE 1811" at L1329.
- **Last issue:** "Del VIERNES [OCR 92] de Febrero de [1812]" at L33630, i.e. Fri 21 Feb 1812. The text ends at L34737 with notices dated 23-25 Feb 1812.
- **Issue start lines and dates.** Several OCR mastheads are corrupt; I corrected them using the weekday.
  - **1811:** L1254 Fri 4 Jan; L2310 Tue 8 Jan; L3678 Fri 11 or 18 Jan (OCR "13"); L4627 No. 139, date illegible (Jan-Mar); L5779 Fri 5 Apr; L6770 Tue 4 Jun; L7927 Fri 7 Jun; L9141 Tue 11 Jun; L10045 Fri 21 Jun; L11158 Tue 25 Jun; L12309 Fri 28 Jun (OCR "9g"); L13380 Tue 9 Jul; L14574 Fri 12 Jul; L15538 Tue 16 Jul; L16693 Tue 23 Jul; L17835 Fri 26 Jul (OCR "36"); L18888 Tue 30 Jul; L19971 Tue 13 Aug (OCR "18"); L21102 Fri 16 Aug; L22184 an issue with no masthead (after 16 Aug, contents about Jul-Aug 1811); L23471 Tue 24 Dec; L24312 Fri 27 Dec (OCR "97"); L25363 Tue 31 Dec.
  - **1812:** L26425 Fri 3 Jan; L27414 Tue 7 Jan; L28526 Fri 10 Jan; L29374 Tue 14 Jan; L30456 Fri 17 Jan; L31506 Tue 21 Jan (OCR "2"); L32743 Tue 18 Feb (OCR "19"); L33630 Fri 21 Feb.
- **Issues per month:**

| Month | Issues |
|---|---|
| Jan 1811 | 4, plus No. 139 (Jan-Mar) |
| Feb-Mar 1811 | 0 legible |
| Apr 1811 | 1 |
| May 1811 | 0 |
| Jun 1811 | 6 |
| Jul 1811 | 6 |
| Aug 1811 | 2, plus 1 undated |
| Sep-Nov 1811 | 0 |
| Dec 1811 | 3 |
| Jan 1812 | 6 |
| Feb 1812 | 2 |

  About 32 issues in all. Big gaps: Feb-May 1811, and Sep-Nov 1811 (except the undated issue).
- The volume ends on 21 Feb 1812, so the **26 Mar 1812 Caracas earthquake is not covered**. There is no "terremoto" or "temblor" in the natural sense anywhere in the text.

## Hits

**No genuine hit for clue types 1-9 or for 1808-1810 sky phenomena.** The only natural-phenomenon report in the whole volume is the known Azores item:

1. **Sabrina island, Azores (known; not the target).** L24852-24860, Fri 27 Dec 1811 (masthead L24312), in a European news column after a report from "...Sound" dated 7 Sept. [OCR] "El 4 de Julid el capitan de la corvéta de guerra Sabina tomo posesion en nombre de § M. dela Isla ultimamente arrojada por un volcan cerca de San Miguel en las Azores. Se puso por nombre Sabinu. Esta Isla-ha ido gradualmente aumentandose por la ejeccién de la materias volcanicas hasta haber adquirido dos 0 tres millas de circunferencia." Judgment: the 1811 Sabrina eruption, printed about 5.5 months late. It is useful only as evidence of how slowly distant natural news reached Caracas. Not the 1808-09 event.

Minor items, all from 1811 and none weather-anomaly evidence:
- **Abundant tobacco harvest, Venezuela.** L7170, Tue 4 Jun 1811. [OCR] "los cosecheros, que teinendo extre manos una abundante cosecha de excelente tabace, carecen de venta y despacho..." Judgment: a good 1810-11 crop. The trouble is markets, not weather. Weak negative evidence against crop failure in Venezuela.
- **Scarcity in Lisbon (war, not weather).** L7835, Tue 4 Jun 1811, from the Gazeta de Martinica of 21 May. [OCR] "Lisboa Marzo 1.—Cada dia son mas escasas las provisivnes en esta ciudad, aunque los Americanos traben una gran porcion de harina..." Judgment: caused by the siege and Masséna's army. Reject as climate.
- **Yellow fever at Cartagena, Spain, late 1811.** L28145, Tue 7 Jan 1812, from the Ambigu. [OCR] "La fiebre amarilla he vuelto 4 manifestarse en Cartagena, llevandose i 30 personas por dia. Se han tamado en Gibraltar y a lo largo de la costa [as precauciones..." Judgment: the 1810-11 Mediterranean yellow-fever epidemics. Not weather-attributed in the text; irrelevant to the target.
- **Sowing instructions, Mérida/Barinas region.** L19869, Tue 30 Jul 1811. [OCR] "...para mudar las sementeras y para cultivar maiz, legumbres y otros frutos de mantenimiento..." Judgment: wartime food provisioning. No weather content.
- **Heat-resistance experiments by a Spaniard (Paris/London).** L24523-24613, Fri 27 Dec 1811. Experiments with hot oil and an oven heated to 260 °F, with temperatures given in Reaumur and Fahrenheit. Judgment: a scientific curiosity, not meteorological.

## Distant-news log (Part B)

Datelined or sourced items read in full. Natural content is noted where there is any; otherwise "none".
- **Buenos Aires / Río de la Plata / Paraguay / Peru / Chile** (to early Oct 1810), L960-1030, first issue (prob. 1 Jan 1811): Liniers executed 26 Aug 1810, Córdoba, Montevideo blockade, ships *Misletoe* and *Fourdroyant*. Natural content: none.
- **"Guayra 31 de Diciembre"** (1810), L1069: frigate *Cherub* arrives from Barbados. None.
- **Cartagena (New Granada), 25 Oct 1810**, L2331-2420: Junta letter. None.
- **Mexico and Jamaica** (Dec 1810), L4572: Hidalgo revolt, Venegas. None.
- **Santa Fe de Bogotá, Junta bando of 28 Jan 1811**, L5786-5900: political. Nothing on the Dec 1808 sky veil or other natural matters.
- **Cartagena; Peru, 26 Mar 1811; Martinique, 11 and 21 May 1811; Lisbon, 1 Mar**, L7269-7840: Lima troops defeated near Cuzco. Lisbon scarcity (war; see Hits). Nothing natural otherwise.
- **Cumaná news**, L10057: military. None.
- **Mexico, 9 and 22 Jan 1811** (Gazetas de Mexico and private letters), L11344-11460: insurgency, Acapulco coast (General Paris's camp surprised at Tres Palos). None.
- **Santa Fe, 18, 20 and 22 Apr / Mar 1811**, L11246, L11336, L12146-12289: Lozano, Miranda. None.
- **Cartagena, 28 Mar 1811; Jamaica; Trinidad de Cuba; Havana; Mexico**, L12588-12960: political and naval (Spanish ships "desarbolados, podridos" for lack of money, not storms). None.
- **Mexico** (letter: viceroy reported dead), L18660. None.
- **Santa Fe, 20 Jul 1811 anniversary**, L22569 (undated issue). None.
- **Lima / Upper Peru** (Goyeneche's armistice with Castelli, Huaqui, June 1811), L23931. None.
- **North Sea / Pomerania, 7 Sep 1811, then Azores (Sabrina)**, L24830-24860: see Hits.
- **Cartagena de Indias independence act, 11 Nov 1811**, L27414-27860. None.
- **Ambigu, 20 Nov 1811**, L28028-28150: includes the yellow fever at Cartagena (Spain). See Hits.
- **Cundinamarca Gazeta Extraordinaria, 9 Nov 1811; Buenos Aires and Montevideo to mid-Sept 1811** (letter from Martinique to Cumaná), L29222-29240. None.
- **Puerto Rico, 15 Jul 1811** (via Gazeta de la Regencia, Cádiz, 21 Sep), L29828. None.
- **Quito, Nov 1811**, L30946; **Guayaquil documents**, L30824. Political. None.
- **"Colombia" column** (Cartagena / Santa Fe), L31509-31590. None.
- **Havana** (letter from North America, 20 Dec 1811; Puerto Rico, 16 Dec 1811: "revolution y mucha miseria" in Havana), L32277-32320. Political. None.
- **Canaries**: mentioned only as the origin of Canarian residents of Venezuela (L16541, L18305, L19901, L23092). None.
- **Asia** (Manila, China, India, Batavia): no news items at all. "India(s)" occurs only as "España e Indias" and "Cartagena de Indias"; "Canton" occurs only as a military district in Venezuela (L20841). The Pacific is mentioned only in Burke's canal essay (L~120-140). **Cape Verde, Central America (other than one passport to Panama, L22698) and at-sea reports**: none with natural content. The ship notices (e.g. a Puerto Rico privateer, L9732; piracy at night, L14985) mention no weather.
- **1812 Caracas earthquake**: not present; the volume ends 21-25 Feb 1812.

## Borderline and rejected

Every other keyword hit was figurative, about warfare, or an OCR false match. Rejected examples:
- **Gunfire words.** "estruendo de las armas" (L572, L598) is a figure of speech. "cañonazos" at L9734 and L14999 is real gunfire from privateers and a fort.
- **Darkness and ash words.** "tinieblas" and "obscuridad" (of ignorance or tyranny, or nighttime raids) at L7395, L12690, L14678, L14985, L14999, L15101, L15481, L22626. "reducidas a cenizas" (destruction or burning) at L9096, L21620, L34284. "cenizas" (the dead) at L18032.
- **Light and sky words.** "velo" ("rasgar el velo") at L8811 and L10683. "eclipsado el brillo de la verdad" at L8225. "rayos / estrellas de primera magnitud" (praise of teachers) at L3232. "la gran luminaria del cielo por medio de las obscuras nubes de la impostura" at L19025. "negras nubes" over "la aurora de la libertad" at L30405. "cometas para anunciar el fallecimiento de los Monarcas" at L29525 is a general remark on superstition, not an observed comet.
- **Fire and volcano words.** "incendio / incendiados" (fire in war or in the law code) at L17350 and L20879. "llamas" (burning papers; the Inquisition) at L34291 and L34568. "lava" matches are OCR fragments ("playa", "esclava", "revelava").
- **Other false matches.** "Escorial" (L15921). "acrehedor" (L3220 etc., caught by "hedor"). "tierra tembl..." matches mean "temblaron" (they trembled) at L5173 and L12245. "temporal" means worldly (L22752). "tempestad(es)" is figurative (L25594, L30855). "truenos y lluvias" is a biblical quotation (1 Samuel 12), L29691. "Catarroja" is a place near Valencia (L33479). "la Cometa" is the name of a Spanish schooner (L1694). "Meteor" is the name of an American schooner (L16660). "sierras nevadas" (Mérida) is geography (L18177). "hambre / peste" at L3492, L14129, L25026 and L28244 refer to war and siege.

**Conclusion:** this volume has no late or retrospective report of the 1808-09 eruption signals: no Bogotá veil, no Lima twilights, no booms, ash or cold. Coverage is sparse (about 32 issues; Feb-May and Sep-Nov 1811 are missing) and the content is overwhelmingly political. The only volcanic item is the known Sabrina island (Azores, 1811).
