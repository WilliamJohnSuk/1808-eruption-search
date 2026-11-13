---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: method
date: undated
---

# Novelty check, round 3 (16 Oct 2026)

Items:
- (A) The interpolated remark in Santiago Pérez Valencia's Popayán register (Acosta 1849, p. 79) comparing the sun of 24 Apr 1815 with that of "diciembre de 1808 y enero de 1809".
- (B) "Velo" as a routine cloud category in Caldas's 1808 Semanario registers (definition after Lamarck in No. 7, 14 Feb 1808), contrasted with the Dec 1808 veil.

Method: WebSearch plus WebFetch. WebFetch output is a small-model summary of OCR or HTML text, not verified against page images. Bash has no internet access.

## Verdicts (provisional, updated below)

(see final section)

## Search log

| # | Tool / target | Query or URL | Result |
|---|---|---|---|
| 1 | WebSearch | "Pérez Valencia" Popayán temblores registro Acosta | only news pages; no hits |
| 2 | WebSearch | Caldas "velo" Lamarck Semanario 1808 nubes meteorología | Pabón-Caicedo PDF; UNAL bffrepositorio PDF; Discover magazine; UDistrital Semanario scans |
| 3 | OpenAlex API | works/doi:10.5194/cp-10-1707-2014 | W2103776013, cited_by_count 45 |
| 4 | OpenAlex API | works?filter=cites:W2103776013 | **BLOCKED: proxy HTTP 429 (rate limited); told not to retry** |
| 5 | Semantic Scholar API | paper/DOI:.../citations | fetch error, not reachable |
| 6 | WebFetch | Pabón-Caicedo, "Caldas y la meteorología" (UNAL Ingeniería, Cátedra Caldas PDF) | cites Guevara-Murua 2014; reproduces the 1807 table and the Feb 1809 note; no "velo" definition, no Lamarck, no Pérez Valencia, no analysis of 1808 registers |
| 7 | WebFetch | UNAL bffrepositorio bitstream (reprint of "Noticias meteorológicas", pp. 355-359) | primary text (Caldas Feb 1809); names Pérez Valencia as a Popayán rain observer, Aug-Dec 1808; not secondary analysis |
| 8 | WebFetch | PANGAEA 10.1594/PANGAEA.872046 | Caldas's Bogotá daily T/P/precip, Jan-Jun 1808, digitized (Domínguez-Castro et al. 2017 supplement); no sky/cloud field listed |
| 9 | WebFetch | Domínguez-Castro et al. 2017, Sci. Data 4:170169 (docta.ucm.es PDF) | lists the COLBOG2 1808 series; cites Guevara-Murua; no "velo" or cloud classification discussed |
| 10 | WebSearch | Popayán terremotos historia sísmica "Perez Valencia" 1827 1834 registro | Espinosa 1999 Geoscopia; SGC Boletín; UNAL Cuadernos de Geografía |
| 11 | WebFetch | Espinosa Baquero 1999, "Sismos y ciudades en Colombia" (sogeocol PDF) | no Pérez Valencia, Acosta or 1815 |
| 12 | WebFetch | revistas.sgc.gov.co Boletín Geológico 716/677 | binary, unreadable |
| 13 | WebFetch | Sarabia et al. 2010, Cuad. Geogr. 19 (1785 and 1917 quakes) | no |
| 14 | WebFetch | SGC "Sismicidad histórica de Colombia" PDF | cites Ramírez 1975 and Espinosa *Historia sísmica 1550-1830*; no Pérez Valencia; no Popayán events 1800-1830 |
| 15 | WebFetch | Espinosa B. 1994, "Un naturalista desconocido, el General Joaquín Acosta", Rev. Acad. Colomb. Cienc. 19(73):287-291 (raccefyn 3884) | **cites the register**: p. 291 "un catálogo de sismicidad llevado por el payanés Santiago Pérez Valencia entre 1785 y 1841"; no sun remark, no 1808/09 |
| 16 | WebFetch | Marín et al. 2006, Bol. Geol. UIS 28(1) | no |
| 17 | WebFetch | Guevara-Murua et al. 2014, Clim. Past PDF | Popayán only via Caldas's place list; no Pérez Valencia or Acosta; quotes "clouds that meteorologists know by the name of veil" (p. 1710) but does not discuss the No. 7 definition, Lamarck or the daily registers; says the post-July 1808 records are lost |
| 18 | WebSearch | Tambora 1815 Colombia Popayán sol rojo abril 1815 | news and general pages only |
| 19 | WebSearch | "Perez Valencia" Popayan earthquake register 1808 1809 sun | PANGAEA/b2find: Popayán precipitation Aug-Dec 1808 (Arboleda & Pérez Valencia), digitized by Domínguez-Castro et al. (from Caldas's Feb 1809 rain table, not the quake register) |
| 20 | WebFetch | Avilán-Caldas 2025, Historia y Sociedad 49 (Restrepo 1806 notebook) | Lamarck only as botanical source; no velo |
| 21 | WebFetch | Wikipedia "1808 mystery eruption" | no Popayán, Pérez Valencia, Acosta or velo |
| 22 | WebFetch | Guevara-Murua et al. author comment, cpd-10-C927-2014 | Popayán only via New Monthly Magazine quote; nothing else |
| 23 | WebFetch | Gómez-Capera et al. 2014 RACCEFyN 38(147) (1785 quake) | no |
| 24 | WebFetch | Castaño, Nieto & Ojeda 2005, Nómadas 22 (Semanario) | no meteorology, no velo |
| 25 | WebFetch | Salcedo & Castaño 2011, Bol. Geol. 33(2) (1785) | no; cites Espinosa 2003 CD-ROM |
| 26 | WebSearch | "Historia sísmica de Colombia 1550-1830" Popayán 1815 | no online text of the Espinosa CD-ROM |
| 27 | WebFetch | Caballero Acosta 2014 (Medellín 1730) | no |
| 28 | WebFetch | **Salcedo Hurtado, Gómez Capera & Espinosa Baquero 2004, "State-of-the-art of the historical seismology in Colombia", Annals of Geophysics 47(2/3), doi:10.4401/ag-3311** | **cites the register** (p. 438): "who made a compilation of earthquakes felt in Popayan City from 1785 to 1841"; "The catalogue by Santiago Pérez was published by Joaquín Acosta in Paris in 1849". No 1815, no "sun" |
| 29 | WebSearch | "Sismicidad histórica y reciente del área de Popayán" (Espinosa 1992) | full text not online; only cited |
| 30 | WebFetch | Sarabia & Cifuentes 2009, INGEOMINAS (Popayán 1736) | no Pérez Valencia or 1815 (mentions 1817, 1827) |
| 31 | WebFetch | Marín Arias et al. 2006, Bol. Geol. 28(2) (Popayán 1983) | no |
| 32 | WebSearch | Mora Pacheco clima Bogotá colonial Caldas | SOLCHA 2020 paper by Mora Pacheco, "Más allá de Caldas...": no 1808 registers, no velo |
| 33 | WebFetch | Gómez-Gutiérrez 2024, RACCEFyN 48(186):178-194 ("Prehistoria del OAN... registros meteorológicos... 1772-1802") | ends in 1802/1805; only notes that Caldas printed Jan 1808 obs. in Feb 1808 (p. 180); no velo, no Lamarck |
| 34 | WebFetch | Gómez-Gutiérrez 2016, RACCEFyN 40(156) cover note | no |
| 35 | WebFetch | Portilla 2025, RACCEFyN 49(192) (1804 astronomical obs.) | no |
| 36 | OpenCitations API | citations of 10.5194/cp-10-1707-2014 | 49 citing DOIs obtained (list kept below) |
| 37 | Crossref API | titles of citers | 2 resolved (France 2019 Human Ecology, sea serpents; Silva 2020 Historia Agraria, Portugal); **geoj.12191 and joc.5955 blocked, HTTP 429** |

Citing DOIs not screened (no access or no time): sciadv.adr5065; geoj.12191; jcli-d-14-00673.1; 2018gl081018; joc.5955; cp-17-1455-2021; cp-13-1451-2017; cp-12-1361-2016; 2015gl066154; s00484-018-1528-0; s41561-019-0402-y; epsl.2023.118458; s10584-017-1910-7; 978-3-319-19042-6_1/_4; wcc.407; tc-18-363-2024; abc120; ab4557; cp-19-959-2023; 2016jd024751; igeof.00167169p.2018.57.1.1823; b978-0-08-100405-0.16001-x; geografie2017122020147; 2017pa003203; dunod.bardi.2021; 2022pa004581; s41586-023-05751-z; rdc.2022.83; and the CP discussion papers. Most are ice-core or volcanic-forcing papers and unlikely to cite Popayán.

## Verdicts

**(A) The Pérez Valencia sun remark (Acosta 1849 p. 79, 24 Apr 1815 compared with Dec 1808 / Jan 1809).**
The register itself is known and cited: Espinosa B. 1994, Rev. Acad. Colomb. Cienc. 19(73):291 (https://raccefyn.co/index.php/raccefyn/article/download/3884/5126/36552), and Salcedo Hurtado et al. 2004, Ann. Geophys. 47:438 (https://www.annalsofgeophysics.eu/index.php/annals/article/download/3311/3357/3417). Hassaurek (1867) also describes it.
**The sun remark itself was not found in:** these two works, Guevara-Murua 2014 and its author comment, Wikipedia, the SGC historical-seismicity PDF, eight Colombian macroseismic papers (listed above), Pabón-Caicedo, or the web searches. Nothing links it to the 1808/09 veil or to Tambora.
Could not reach: Espinosa 2003 CD-ROM *Historia sísmica de Colombia 1550-1830* (the most likely place it would be quoted, entry for 1815); Espinosa 1992 *Sismicidad histórica... Popayán*; Ramírez 1975; the unscreened citers above.
Note: the main Tambora eruption was on 10-11 Apr 1815, so 24 Apr 1815 is very early for a stratospheric effect in the Andes. Local causes (Puracé, smoke, haze) are alternatives.

**(B) "Velo" as a routine category in Caldas's 1808 registers (definition after Lamarck, No. 7).**
Not found in: Guevara-Murua 2014 (quotes the Feb 1809 sentence about "clouds that meteorologists know by the name of veil", p. 1710, but not the No. 7 definition, Lamarck or the daily sky codes; it uses only monthly data), Domínguez-Castro et al. 2017 and PANGAEA 872046 (digitized Jan-Jun 1808 T, P and precipitation, with no sky-state field shown), Pabón-Caicedo, Gómez-Gutiérrez 2024, Portilla 2025, Castaño/Nieto/Ojeda 2005, Mora Pacheco (SOLCHA 2020), Avilán-Caldas 2025, or web searches.
Partial precedent: Domínguez-Castro et al. 2017 already digitized Caldas's 1808 daily instrumental registers (but not the cloud codes).
Could not reach: Nieto Olarte's and Appel's books, Arias de Greiff, Díaz Piedrahita, Bateman (no online full text found), theses, Boletín de Historia y Antigüedades, *Meteorología Colombiana*.

## Source register

| Source | Region/lang | Type | Covers 1808-09? | URL | Opened from here? |
|---|---|---|---|---|---|
| Espinosa B. 1994, RACCEFyN 19(73) | CO/es | article | register 1785-1841 | https://raccefyn.co/index.php/raccefyn/article/download/3884/5126/36552 | yes (OCR text) |
| Salcedo et al. 2004, Ann. Geophys. 47 | CO/en | article | register cited | https://www.annalsofgeophysics.eu/index.php/annals/article/download/3311/3357/3417 | yes (OCR text) |
| Guevara-Murua et al. 2014 | en | article | yes | https://cp.copernicus.org/articles/10/1707/2014/cp-10-1707-2014.pdf | yes |
| Guevara-Murua author comment 2014 | en | discussion | yes | https://cp.copernicus.org/preprints/10/C927/2014/cpd-10-C927-2014.pdf | yes |
| Domínguez-Castro et al. 2017 Sci Data | en | article | yes (COLBOG2 1808) | https://docta.ucm.es/bitstreams/40dc2f30-d8e3-4877-8127-be63e71b1905/download | yes |
| PANGAEA 872046 Bogotá 1808 | data | dataset | Jan-Jun 1808 | https://doi.pangaea.de/10.1594/PANGAEA.872046 | yes |
| PANGAEA Popayán precip 1808 | data | dataset | Aug-Dec 1808 | https://b2find.eudat.eu/dataset/9a697e64-3779-5cb5-b93f-315868f531a1 | yes |
| Pabón-Caicedo, Caldas y la meteorología | CO/es | teaching text | yes | https://www.ingenieria.bogota.unal.edu.co/repositorio_documental_ajustado/PaginaFacultadIngenieria/DocumentosPresentaciones/CatedraCaldas/CaldasMeteorologiq.pdf | yes |
| Noticias meteorológicas reprint (UNAL) | CO/es | primary reprint | yes | https://bffrepositorio.unal.edu.co/server/api/core/bitstreams/004b9cb0-49b7-4d43-851a-83f56340e3ff/content | yes |
| Gómez-Gutiérrez 2024 RACCEFyN 48 | CO/es | article | no (to 1805) | https://raccefyn.co/index.php/raccefyn/article/download/prehistoria_del_observatorio_astronomico_nacional_registros_mete/3978 | yes |
| Portilla 2025 RACCEFyN 49 | CO/es | article | no | https://raccefyn.co/index.php/raccefyn/article/download/3195/4572/34299 | yes |
| Castaño, Nieto, Ojeda 2005 Nómadas | CO/es | article | Semanario | https://www.redalyc.org/pdf/1051/105116726010.pdf | yes |
| Mora Pacheco SOLCHA 2020 | CO/es | paper | no | https://www.flacso.edu.ec/flax15/_upload/solcha2020/url_documentacion/PONENCIAMESACOLOMBIAMsalld8213759.pdf | yes |
| Avilán-Caldas 2025 Hist. y Soc. | CO/es | article | no | https://revistas.unal.edu.co/index.php/hisysoc/article/view/120975 | yes |
| SGC Sismicidad histórica PDF | CO/es | web text | no | https://www2.sgc.gov.co/sgc/mapas/Documents/PDF DESCRIPCION/SismicidadHistoricadeColombia.pdf | yes |
| Espinosa 1999 Sismos y ciudades | CO/es | article | no | https://sogeocol.edu.co/documentos/sism_ciu_col.pdf | yes |
| Sarabia & Cifuentes 2009 (1736) | CO/es | report | no | https://recordcenter.sgc.gov.co/B6/21001000024413/documento/pdf/2105244131105000.pdf | yes |
| Marín Arias et al. 2006 | CO/es | article | no | https://revistas.uis.edu.co/index.php/revistaboletindegeologia/article/download/1579/1973/3983 | yes |
| Marín et al. 2006 (Caldas dept.) | CO/es | article | no | https://revistas.uis.edu.co/index.php/revistaboletindegeologia/article/download/3320/3506/11468 | yes |
| Salcedo & Castaño 2011 | CO/es | article | no | https://revistas.uis.edu.co/index.php/revistaboletindegeologia/article/download/2542/2870/7709 | yes |
| Gómez-Capera et al. 2014 | CO/es | article | no | https://raccefyn.co/index.php/raccefyn/article/download/63/46/303 | yes |
| Sarabia et al. 2010 Cuad. Geogr. | CO/es | article | no | https://revistas.unal.edu.co/index.php/rcg/article/view/16863 | yes |
| Caballero Acosta 2014 | CO/es | article | no | https://dialnet.unirioja.es/descarga/articulo/5386888.pdf | yes |
| SGC Boletín Geológico 716 | CO/es | article | ? | https://revistas.sgc.gov.co/index.php/boletingeo/article/view/716/677 | blocked (binary) |
| Espinosa 2003 Historia sísmica 1550-1830 (CD-ROM) | CO/es | catalogue | likely | no URL found | not tried |
| Espinosa 1992 Sismicidad... Popayán | CO/es | report | likely | no URL found | not tried |
| Ramírez 1975 Historia de los terremotos | CO/es | book | likely | no URL found | not tried |
| OpenAlex cites:W2103776013 | API | citations | - | https://api.openalex.org/works?filter=cites:W2103776013 | blocked (429) |
| Semantic Scholar citations | API | citations | - | https://api.semanticscholar.org/graph/v1/paper/DOI:10.5194/cp-10-1707-2014/citations | blocked (fetch error) |
| OpenCitations | API | citations | - | https://api.opencitations.net/index/v1/citations/10.5194/cp-10-1707-2014 | yes |
