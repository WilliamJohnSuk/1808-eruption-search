# Discussions: paste-ready seed posts (T32)

Drafted 4 Nov 2026 by Claude (AI) for William John Suk, to paste into GitHub Discussions after the eight categories in `DISCUSSIONS_PLAN.md` exist. Each post is marked `ai-generated`; William posts them from his account, so he should read each one first. Titles are in **bold**; the body follows. Category names match the plan exactly.

Paths such as `findings/findings.csv` are relative to the repository. Discussions do not turn them into links, so before posting either leave them as plain paths or prefix them with `https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/`.

---

## 1. Announcements

**Welcome: what this project is and how AI work is marked** (pin)

Late in 1808 (the ice-core literature calls it "the 1809 eruption") a large tropical volcano erupted somewhere on Earth. Its sulfate fell on Greenland and Antarctica at the same time, and its haze dimmed the sun over Bogotá from 11 December 1808. Nobody knows which volcano it was.

This repository is an open search of the historical record for it: newspapers, ships' logs, parish books, court chronicles, missionary letters, ice cores and corals. It holds a source register, notes for each line of research, a findings table where every row carries a verification level, and the data and scripts behind every calculation.

Most of the text so far was written by an AI model (Claude) working under [William John Suk](https://williamsuk.ai)'s direction. Every AI-written note says so in its front matter, and nothing it wrote counts as checked until a person has read the source. Your checks are what turn a lead into evidence; see [findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md). Before launch, William read the page images behind three headline findings (F01, F09, F15). One of those checks caught an AI error, described in Method and AI.

How to help: report a source, re-check a finding, propose a candidate, or take a free task from [access/open_tasks.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/access/open_tasks.md). Votes here guide priorities; they never decide what is true ([GOVERNANCE.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/GOVERNANCE.md)). Negative results are welcome, phrased as "I found no report of ... in these sources".

For conduct reports, or anything that should not be public, email 1808@williamsuk.ai.

William John Suk, maintainer (https://williamsuk.ai)

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 2. Start here

**How do I report a source without git?**

Open an issue with the form ["Report a source"](https://github.com/WilliamJohnSuk/1808-eruption-search/issues/new?template=report-a-source.yml) (Issues > New issue). A link and one sentence is enough to start. Say how you read it (a page image, OCR text, or someone's summary) and whether an AI tool helped. Before you start, search [sources/register.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/sources/register.md) and [access/unavailable_sources.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/access/unavailable_sources.md): if the source is already listed, say what you can add. If the source is in a language you don't read, ask in Translation help.

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 3. Candidate volcanoes

Template for each candidate post: what favours it, what argues against it, what test would settle it. Facts below come from `strands/candidates/` and `findings/findings.csv`; they are the project's current reading, not settled.


**Dakataua / Makalia (New Britain, Papua New Guinea)**

For: Top of the priority list Claude drew up on 26 Oct. Its Makalia glass scores 0.92 against the 1809 ice glass (F20; Claude's calculation, not checked by a person). We know of no surviving written record for the region in 1808 (local history there was kept orally, and the oral traditions searched so far say nothing of c. 1808). The nearest cores, 230 km away, are undated, and no core from Lake Dakataua exists (F35).

Against or unknown: The glass match is shared by many arcs. Zr/Nb of about 66 (Claude's calculation from GEOROC) would separate it from Gaua and Leyte if the ice shards are ever analysed.

What would settle it: A dated c. 1808 tephra at Dakataua, or trace elements on the ice shards.

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Gaua (Vanuatu)**

For: Top of the priority list Claude drew up on 26 Oct. Whole-rock and glass chemistry match (F20; Claude's calculation, not checked by a person).

Against or unknown: Tanna, Ambrym and Kuwae match as well (F34; Claude's calculation). The Espiritu Santo coral 97 km away and a stalagmite 150 km away show no 1809-11 cooling (F35).

What would settle it: A core from Lake Letas; trace elements (Zr/Nb about 43, Claude's calculation from GEOROC).

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Cabalían (southern Leyte, Philippines)**

For: Top of the priority list Claude drew up on 26 Oct. Parish registers were being kept in the region in 1808, so a written trace could survive.

Against or unknown: Three Bohol parishes 150-180 km away show no excess burials after Nov 1808 (Claude's count, one pass) (F27). The *Ramoncita* passed 15-20 km off in Jan-Feb 1809 and her charts note nothing (F32). Leyte's own registers before 1861 are lost.

What would settle it: The *Ramoncita* diary (U151); HMS *Psyche*'s log at Surigao, 1809 (T17).

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Agung (Bali)**

For: Raffles (1815) heard that Bali residents remembered an Agung eruption about seven years before (F13). The Lombok Strait coral 13 km away turns cool/dry from December 1808 (F22; Claude's calculation).

Against or unknown: Scale unknown; the memory is second-hand and OCR only. Agung is not yet in the trace-element lookup (U154).

What would settle it: Lake cores of eastern Java; Agung trace elements.

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Todoko-Ranu (Halmahera)**

For: Possible. Kau Bay holds the only existing cores in the candidate zone that could resolve 1809 (F35).

Against or unknown: We found no report of an eruption; the Dutch Ternate records for 1808-09 are in Jakarta and still unread (T20).

What would settle it: Resampling the Kau Bay cores; the Ternate day register (ANRI, T20).

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Dukono (Halmahera)**

For: Possible on Claude's glass comparison (F20; not checked by a person).

Against or unknown: As for Todoko-Ranu.

What would settle it: As above.

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Teon (southern Banda arc)**

For: Possible on Claude's glass comparison (F20; not checked by a person).

Against or unknown: No sediment or coral record within 200 km (F35); we found few written records for these islands in 1808.

What would settle it: The Banda day register Aug 1808-Jul 1809 (ANRI).

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Nila (southern Banda arc)**

For: Possible on Claude's glass comparison (F20; not checked by a person).

Against or unknown: As for Teon.

What would settle it: As above.

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Northern Sulawesi (Lokon, Mahawu and neighbours)**

For: Possible on Claude's glass comparison (F20; not checked by a person).

Against or unknown: Dutch Manado records for 1808-10 not found online.

What would settle it: Manado letters in the ANRI Ternate series.

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Karthala (Grande Comore, Comoros): a new GVP listing for 1808**

For: The current Global Volcanism Program page lists a confirmed 1808 Karthala eruption (no VEI given). It was not in the 2018 GVP snapshot the project first screened (F39).

Against or unknown: Karthala is a basaltic shield, so a poor fit for the andesitic 1809 ice glass (Claude's inference). We do not yet know what source GVP used for the 1808 date.

What would settle it: The reference behind the GVP entry; any written record from the Comoros, Zanzibar or passing ships in 1808-09 (GVP re-screen, T59).

What do you know about this volcano's history around 1800? Sources please.

_Drafted by Claude (AI); read and posted by William John Suk._


**Claims seen online (checked 12 Nov 2026)**

Agrigan (Mariana Islands) and Tambo Quemado (Bolivia) are named as "proposed sources" on Grokipedia, an AI-written encyclopedia. We found no publication behind the Agrigan claim: its footnote does not mention Agrigan, GVP and USGS list 1917 as its only historical eruption, and the 4 Dec 1808 Japanese tsunami it cites was a local event. The Tambo Quemado "zircon dating" footnote points to a student project on a differently named volcano that never mentions 1808, and Tambo Quemado is rhyolite while the 1809 ice glass is andesite (F38). If you know of a real paper behind either claim, please post it here.

_Drafted by Claude (AI); read and posted by William John Suk._


**Ruled out, and why** (Etna, Vesuvius, Hekla, Long Island, non-volcanic causes)

Etna (March 1809) and Vesuvius erupted in the window but were small and northern; our onset-lag test points to a tropical source (F29, Claude's calculation), though Meuer et al. 2024 argued for a northern extratropical one (F37). Hekla had no eruption then. Long Island (Papua New Guinea) had its great eruption in the 1660s and no record of activity 1700-1827. Non-volcanic explanations of the ice signal fail on sulfur mass, timing and isotopes ([strands/science_alternatives/nonvolcanic_alternatives.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/nonvolcanic_alternatives.md)). If you think one of these was dismissed too quickly, say why here.

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 4. Evidence review

One thread per row of [findings/findings.csv](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/findings.csv). Regenerated from the table and findings/checks.csv on 15 Nov 2026 (F01-F39). "Verification" is the level Claude reached; a person's check is named separately.


**F01: Bogotá, New Granada, from 11 Dec 1808 to late Jan/early Feb 1809**

Whitish sky, silvery sun mistaken for the moon, dimmed stars (Caldas, Semanario No. 5, 5 Feb 1809)

Source: Semanario del Nuevo Reyno de Granada año 2 no. 5 (5 Feb 1809) printed pp. 37-40; Banrep p17054coll26 id 1606. Verification (Claude's reading or calculation): page image checked. Status: core witness. Notes: [strands/colombia_caldas/caldas.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/colombia_caldas/caldas.md) ; [strands/method/downloads_2026-10-16_findings.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/downloads_2026-10-16_findings.md). Checked by a person: William John Suk read the page image himself (check C001, 2026-11-14): confirms.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F02: Lima, Peru, mid-Dec 1808 to mid-Feb 1809**

Evening glow cone towards Chorrillos every night to about 20:00 (Unanue, Clima de Lima 2nd ed. 1815, Secc. I pp. 13-14 n. 3)

Source: Wellcome Collection b21945469. Verification (Claude's reading or calculation): OCR only. Status: core witness; zodiacal light possible. Notes: [strands/peru_south/unanue_south.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/peru_south/unanue_south.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F03: Popayán, New Granada, Dec 1808 - Jan 1809 (recalled 1815)**

Pérez Valencia compares dim sun of 24 Apr 1815 with Dec 1808 and Jan 1809

Source: Acosta (ed.) 1849 Viajes científicos p. 79. Verification (Claude's reading or calculation): OCR only. Status: lead. Notes: [strands/colombia_caldas/caldas_letters_round2.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/colombia_caldas/caldas_letters_round2.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F04: Edo, Japan, 9 Jan to c. 16-25 Jan 1809**

Very red sky at sunrise (east) and sunset (southwest) every day

Source: Katayama Enzen chronicle; Kagoshima Univ. Tamazato Bunko TZ0441 vol. 1 image 30. Verification (Claude's reading or calculation): page image checked. Status: lead; weak baseline. Notes: [strands/asia_pacific_arabic/asian_arabic_round4.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/asian_arabic_round4.md). Checked by a person: none yet (a reader of Japanese has been asked to check it).

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F05: Tottori, Japan, 5 Feb 1809**

Sun's disc red as vermilion morning and evening

Source: Inpu nenpyō. Verification (Claude's reading or calculation): OCR only. Status: lead; single day. Notes: [strands/asia_pacific_arabic/asian_arabic_round4.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/asian_arabic_round4.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F06: Atlantic, 16°S-28°N along c. 30°W, 10 Dec 1808 - 9 Jan 1809**

Packet Townsend logs hazy almost daily vs c. 10% baseline

Source: CLIWOC 2.1 (NMM NAI/3/17). Verification (Claude's reading or calculation): computed. Status: weak; one observer who wrote hazy on 58% of days. Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F07: Tropical Indian Ocean, first Bay of Bengal, Dec 1808 - Jan 1809 onward**

EIC noon air temperature drops 0.65 °C within voyages (17 voyages), beyond all 39 null years

Source: oldweather/EEIC keyed logs. Verification (Claude's reading or calculation): computed. Status: weak to moderate; 8 ships in Jan 1809. Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F08: NEEM, Greenland, late 1809 arrival**

Winter 1808/09 clean; 1809 sulfate crosses background c. Oct 1809, implying eruption c. Dec 1808 - Mar 1809

Source: NEEM-2011-S1 2 cm (PANGAEA 940553). Verification (Claude's reading or calculation): computed. Status: moderate; one core. Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F09: York Factory, Hudson Bay, 4 Nov 1808**

The darkest day I have seen in Hudsons Bay

Source: HBCA B.239/a/119. Verification (Claude's reading or calculation): page image checked. Status: probably weather; a month before Bogotá. Notes: [strands/north_america/hbc_york_factory_journals.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/north_america/hbc_york_factory_journals.md). Checked by a person: William John Suk read the page image himself (check C003, 2026-11-15): confirms.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F10: Salem, Massachusetts, 8-12 Nov 1808**

Sun very red, dark days (Bentley diary)

Source: Bentley diary. Verification (Claude's reading or calculation): OCR only. Status: probably smoke; too early. Notes: [strands/europe_press/free_sources_round5.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/europe_press/free_sources_round5.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F11: NW Atlantic off New England, 3-9 Nov 1808**

HMS Penelope logs hazy 4 of 8 days

Source: CLIWOC 2.1 (NMM SPN/9). Verification (Claude's reading or calculation): computed. Status: weak. Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F12: SE of Madagascar, 16-20 Dec 1808**

Tigris logs hazy/thick hazy 3 of 6 days

Source: CLIWOC 2.1 (BL IOR/L/MAR/B/219D). Verification (Claude's reading or calculation): computed. Status: weak. Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F13: Bali, c. 1808 ±1 yr**

Raffles 1815: residents recall lesser effects from Agung eruption about seven years before

Source: Lady Raffles Memoir 1830 p. 244; earlier printing: Raffles, History of Java vol. 1 (1817), Wellcome copy IA b22012382_0001 leaf 85 ("Karang Asam"). Verification (Claude's reading or calculation): OCR only. Status: uncertain. Notes: [strands/asia_pacific_arabic/indonesia_pass2.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/indonesia_pass2.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F14: San Fernando, Cádiz, Jan-Mar 1809**

Calimoso (hazy) days, 10 in winter 1809, all with ESE/SE wind

Source: SF1799-1813 (Zenodo 7104289). Verification (Claude's reading or calculation): computed. Status: probably Saharan dust (negative). Notes: [strands/science_alternatives/scientific_data_round6.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/scientific_data_round6.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F15: Bogotá, New Granada, Jan-Jul 1808 baseline**

Caldas defines his 'velo' (Semanario núm. 7, 14 Feb 1808, printed p. 56 footnote 3) and logs it as an ordinary but infrequent sky state: 've.' on about 10 of 212 days in his Jan-Jul 1808 tables (4 Mar, 12 Mar, 20 Mar, 23 Mar, 9/15/29 Feb, 4 Apr, 6 May, 28 Jun; none in Jan or Jul), twice with a corona (Sun 15 Feb, Feb table in núm. 10, printed p. 83; Moon 12 Mar) [corrected 15 Nov 2026 after a human check: the corona had been dated 14 Feb because the sky column is printed half a row high, and veils had been described as 'a handful a month']; all seven tables human-checked by William John Suk 15 Nov 2026; the Dec 1808 veil, constant for weeks and coronaless, was unlike anything in his 1808 record [Claude's inference]

Source: Semanario del Nuevo Reyno de Granada 1808 núm. 7 (printed p. 56, PDF p. 78) and the Jan-Jul 1808 tables (PDF pp. 71, 105, 131, 165, 199, 245, 281; Feb = núm. 10, printed p. 83); JCB copy archive.org semanariodelnuev01unse. Verification (Claude's reading or calculation): page image checked. Status: supports F01. Notes: [strands/colombia_caldas/caldas.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/colombia_caldas/caldas.md). Checked by a person: William John Suk read the page image himself (check C002, 2026-11-15): confirms.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F16: London, late Mar-Apr 1809**

Luke Howard: rose-coloured haze over an opaque twilight

Source: Howard. Verification (Claude's reading or calculation): OCR only; day dates garbled. Status: weak; post-frontal; Etna erupted 27 Mar 1809. Notes: [strands/europe_press/nonIberian_fulltext_pass2.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/europe_press/nonIberian_fulltext_pass2.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F17: Batavia environs, Java, 5 Oct 1809 (drought of the 1809 season; onset not stated)**

Order on rice shortage: 'the unusual drought of the season' caused a complete rice failure in most districts, substitute root crops failed, some districts without food; 12 koyang of rice issued weekly (Plakaatboek vol. 15 printed p. 912)

Source: Van der Chijs (ed.) Nederlandsch-Indisch Plakaatboek vol. 15 (archive.org nederlandschind01unkngoog). Verification (Claude's reading or calculation): page image checked; related Mar-Aug 1809 and 1810 rice orders OCR only. Status: lead; not diagnostic (El Niño, or forced labour on Daendels's Great Post Road that took farmers from their rice fields, could also explain it; context in notes §1a); El Niño check done 27 Oct (F23): El Niño unlikely (inference); see also F24. Notes: [strands/asia_pacific_arabic/newbritain_banda_halmahera_records_2026-10-26.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/newbritain_banda_halmahera_records_2026-10-26.md). Checked by a person: none yet (a reader of Dutch has been asked to check it).

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F18: H15 core, Mizuho Plateau, East Antarctica, 1809 layer (ECM age 1810)**

1809/Tambora H2SO4 deposition 44/68 kg/km2 (0.65); unanalysed 'fine ash-like materials (~10 um)' in the 1809 layer (Kohno et al. 1996 pp. 49, 51)

Source: Kohno et al. 1996 Proc. NIPR Symp. Polar Meteorol. Glaciol. 10:36-54; Kawano et al. 1999 Seppyo 61:13-24. Verification (Claude's reading or calculation): page image checked. Status: lead; possible tephra sample held by NIPR; 1809/1815 assignment by peak pair. Notes: [strands/asia_pacific_arabic/japanese_red_skies_literature_2026-10-26.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/japanese_red_skies_literature_2026-10-26.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F19: Talos Dome, Victoria Land, Antarctica, 1809-10 (ice layers)**

1809/Tambora sulfate ratio 1.05 (TD96) and 1.11 (TALDICE) vs 0.48 mean of 15 other Antarctic cores, c. 5 sd high; GV7 at 450 km normal (0.57)

Source: Nardin et al. 2020 Geosciences 10:38 Table 2 and 17 other core papers. Verification (Claude's reading or calculation): computed; Talos input values page image checked. Status: points to a small local Victoria Land eruption (Mt Melbourne or Pleiades); not the main source; Hercules Névé next test. Notes: [strands/science_alternatives/antarctic_sulfate_map_2026-10-26.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/antarctic_sulfate_map_2026-10-26.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F20: Candidate arcs: Halmahera, Sulawesi, Banda, Luzon, New Britain, Solomons, Vanuatu, Tonga, 1809 ice glass (Dome C and South Pole)**

Major-element match of the 1809 glass against 8,740 GEOROC and 248 Gill analyses: many unrelated medium-K arc andesites score 0.90-0.95 (Dakataua Makalia glass 0.92, SW Luzon and Vanuatu marine glasses 0.92-0.95); low-K Tonga, New Britain arc front, Witori and N Banda score <=0.83

Source: GEOROC 2026-09 convergent-margin files; Gill EarthChem Library 1499/1502/1503; ice glass from Plunkett et al. 2023 and others. Verification (Claude's reading or calculation): computed. Status: desk comparison at its limit; rules out low-K arcs only; needs trace elements or a dated c. 1808 proximal tephra. Notes: [strands/candidates/glass_candidates_compilation_2026-10-26.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/candidates/glass_candidates_compilation_2026-10-26.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F21: Hiroshima, Japan, Jul-Aug 1809**

Summer mean maximum temperature c. 31 C (Jul) and 33.1 C (Aug), at or above normal: no 1809 summer cooling; Jul-Aug 1808 missing

Source: Hirano et al. 2018 Geogr. Rev. Japan A 91:311 Fig. 9. Verification (Claude's reading or calculation): inferred (values digitised by Claude from the figure). Status: negative; rainy-day proxy; one site. Notes: [strands/asia_pacific_arabic/japanese_red_skies_literature_2026-10-26.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/japanese_red_skies_literature_2026-10-26.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F22: Lombok Strait (13 km from Agung) and Palau, Dec 1808 onset; Jul 1809-Jun 1813 peak**

Coral cool/dry excursion starts Dec 1808 (Lombok +2.1 sd, Palau +2.2 sd); Lombok normal in the 1809 dry season, then its most extreme four-year window of 1782-1990 (Jul 1809-Jun 1813, +1.33 sd); Fiji, GBR, Malindi, Galápagos cool/dry 1809-12; Vanuatu not

Source: PAGES2k v2 coral compilation (34 records; Charles et al. 2003 Lombok; NOAA files). Verification (Claude's reading or calculation): computed. Status: aftermath, not location; supports a late-1808 eruption (inference). Notes: [strands/science_alternatives/coral_footprint_1809-12_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/coral_footprint_1809-12_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F23: Tropical Pacific (ENSO), Dec 1808 - May 1809 (corals); 1808-1810 (tree rings)**

ENSO state: tree-ring and multiproxy lists La Niña 1808-10; corals El Niño-like Dec 1808-May 1809 then neutral; Lombok coral normal Jul-Nov 1809, so El Niño unlikely to explain the 1809 Batavia drought (inference)

Source: Gergis & Fowler 2009; Li et al. 2013; McGregor et al. 2010; Freund et al. 2019; PAGES2k v2 corals. Verification (Claude's reading or calculation): computed; literature read as fetched text. Status: context for F17 and F24. Notes: [strands/science_alternatives/coral_treering_enso_1809_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/coral_treering_enso_1809_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F24: Batavia, Java, decree 14 Jul 1809 (printed 14 Aug 1809); letter 23 Aug 1809**

Governor-General's decree orders root crops planted 'om by eene eventueele Schaarschheid van Ryst'; Daendels: rice 'in sommige districten van Java minder gunstig geslaagd', no cause; no eruption, earthquake, ash or sky report in NA 2.01.27.05 inv. 19, 20, 22 for 1808-11

Source: Bataviaasch Vendu-Nieuws 14 Aug 1809 No. 33 (NA 2.01.27.05 inv. 20); Daendels missive 23 Aug 1809 fol. 100v-103 (inv. 19). Verification (Claude's reading or calculation): page image checked. Status: lead; supports F17; not diagnostic. Notes: [strands/asia_pacific_arabic/dutch_colonial_archives_1808-10_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/dutch_colonial_archives_1808-10_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F25: Guangdong and Guangxi, South China, JQ13 10th month (Nov-Dec 1808); 1809**

Frost coded at Lingshan and Hepu (Guangxi coast) Nov-Dec 1808; drought-famine 1809 at 26 sites, highest count of 1796-1819; we found no red sky, dim sun, haze, ash or sea surge coded for Nov 1808-Mar 1809 (weak negative: Tambora's optics not coded either)

Source: REACHES v3.1 coding of Zhang De'er 2004 (NOAA study 23410). Verification (Claude's reading or calculation): coded database rows (no quoted text); counts computed. Status: lead; not diagnostic (pirate blockade alternative); Gregorian months are the database's conversion. Notes: [strands/asia_pacific_arabic/chinese_gazetteers_reaches_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/chinese_gazetteers_reaches_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F26: Red River delta (Bắc Thành), Vietnam, 1809 autumn crop; famine Oct-Nov 1809 to Jul 1810 (Gregorian dates Claude's conversion)**

1809 autumn crop lost to 'nắng hạn lâu ngày' (long drought) in some places and typhoon and salt water in others; famine 'liền năm đói kém' in Bắc Thành to Jul 1810; we found no sky, ash, darkness, boom or earthquake entry Jan 1808-Feb 1811

Source: Đại Nam thực lục, Chính biên Đệ nhất kỷ q. XXXIV-XLII, 2002 Viện Sử học translation, tập 1 pp. 716-807 (esp. pp. 766, 771, 772, 783-789). Verification (Claude's reading or calculation): page image checked (of the modern translation; Hán original not seen). Status: lead; part of the 1809 drought belt with F17, F24, F25; not diagnostic. Notes: [strands/asia_pacific_arabic/dai_nam_thuc_luc_1808-10_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/dai_nam_thuc_luc_1808-10_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F27: Bohol (Baclayon, Tagbilaran, Loon), 150-180 km from Cabalían, Nov 1808 - Apr 1809 (test window); crisis 1810-11**

We found no excess of burials after Nov 1808 and no note of sky, ash, noise, earthquake, hunger or sickness in three parish burial books 1806-1811; all three show a mortality crisis 1810-11 with a children's wave Jan-Apr 1811

Source: FamilySearch DGS 7768815 (Baclayon), 7769534 (Tagbilaran), 5382642 (Loon), images as in the note. Verification (Claude's reading or calculation): page image checked (counts Claude's, one pass). Status: negative (weak) for a very large eruption near Bohol; silent on distant candidates. Notes: [strands/candidates/cabalian_parish_records_familysearch_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/candidates/cabalian_parish_records_familysearch_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F28: East Rongbuk, Everest (28°N), 1808.2-1811.4 (samples); Tambora 1815.71**

Sixteen samples 1808-1811 show no bismuth enrichment (EFc 1.7-27 vs threshold 371); Tambora recorded as one sample with Bi EFc 3,882; Dasuopu silent 1809-11 but unvalidated

Source: NOAA rongbuk2009.txt (Kaspari et al. 2009); dasuopu2020elem-noaa.txt (Gabrielli et al. 2020); Xu et al. 2009 method. Verification (Claude's reading or calculation): computed. Status: negative (weak); does not locate the source. Notes: [strands/science_alternatives/tibet_himalaya_records_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/tibet_himalaya_records_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F29: Greenland and Antarctica (WDC06A, DSS, NEEM-S1, NGRIP), 1809 deposition (ice layers)**

Greenland minus Antarctic onset lag −0.05 yr (range −0.4 to +0.3): synchronous, so tropical; about 55% of deposited sulfate in the north (NH/SH vs Tambora 1.4, 0.9-2.2); Tambora-analogue eruption date 1809.07 ± 0.41 (Claude's calculation)

Source: Sigl et al. 2013; Plummer et al. 2012; Gao et al. 2007 (tables read as fetched text). Verification (Claude's reading or calculation): computed. Status: method result; tropical only (Claude's inference; Meuer et al. 2024 argue for a northern extratropical source, see F37). Notes: [strands/science_alternatives/bipolar_sulfate_lag_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/bipolar_sulfate_lag_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F30: Global (method), 1809 (ice layers)**

Latitude band from the hemispheric sulfate ratio withdrawn: the Marshall et al. 2021 emulator predicts the Greenland/Antarctic ratio of eleven known tropical eruptions with rms error ×3.0 and no correlation; observed ratios vary with season (Oct-Feb about ×2 Greenland-heavy), not latitude, inside ±17°

Source: eVolv2k v2.1 (hemi variable); Crowley & Unterman 2013; Marshall et al. 2021 emulator; EVA_H. Verification (Claude's reading or calculation): computed. Status: withdrawn result (the 28 Oct band 12°S-3°N is no longer used); Cabalían not excluded by latitude. Notes: [strands/science_alternatives/deposition_ratio_validation_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/science_alternatives/deposition_ratio_validation_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F31: S Atlantic, SE Pacific, SE Africa, W Sumatra (1810), Sep 1808 - Jul 1810**

We found no ash, pumice, detonations, darkness, dimmed or red sun, odd twilight or sea wave in four logs read in full (Cyrus, Hero, Sukey, Fame); none was in the Indonesian-Melanesian zone in the window

Source: NHA MS220 Logs 46, 257, 230; PEM Log 90 (archive.org); AOWV voyage database. Verification (Claude's reading or calculation): page image checked. Status: negative; out of the candidate zone. Notes: [strands/ship_logs/american_logbooks_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/ship_logs/american_logbooks_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F32: Surigao Strait past Panaon, c. 15-20 km from Cabalían (Claude's distance), 21 Jan - 11 Feb 1809**

Ramoncita (Lima-Manila) track charts: navigational notes only; we found no ash, pumice or haze noted

Source: Museo Naval via Biblioteca Virtual de Defensa, mnm_0079_0004-0006 (path=75468). Verification (Claude's reading or calculation): page image checked. Status: negative (very weak: charts, not the diary); diary unread (T26, U151). Notes: [strands/portuguese_world/ramoncita_bvd_2026-11-02.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/portuguese_world/ramoncita_bvd_2026-11-02.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F33: Deshima, Nagasaki, Japan, 9 Nov 1808 - Apr 1809**

Dutch factory day register: storms 15-17 Dec 1808 and 22-24 Mar 1809, junk wrecks; we found no sky, haze, ash or earthquake entry, nor in the register's index for the year; secret register political

Source: Nationaal Archief 1.04.21 inv. 222 and 257 (Doeff). Verification (Claude's reading or calculation): page image checked. Status: negative (weak: selective register); Apr-Nov 1809 unread (T25). Notes: [strands/method/free_checks_T5-T10_2026-11-02.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/free_checks_T5-T10_2026-11-02.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F34: Vanuatu and Solomon arcs, Quaternary rocks (comparison with 1809 ice glass)**

Glass filter extended: Tanna 0.93/0.97, Ambrym 0.92/0.95, Gaua 0.91/0.94, Kuwae 0.92/0.91, Ambae 0.91; Solomons with young activity 0.88 or less; Bougainville untested

Source: GEOROC 2026-09 Vanuatu and Solomon arc files; ice glass as F20. Verification (Claude's reading or calculation): computed. Status: extends F20: a Gaua match is not specific to Gaua. Notes: [strands/method/free_checks_T5-T10_2026-11-02.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/free_checks_T5-T10_2026-11-02.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F35: Within 300 km of the candidates, 1806-1822 (Santo coral, Taurius Cave); late Holocene (cores)**

We found no tephra dated to c. 1809 in 58 catalogued archives near the candidates; Espiritu Santo coral (97 km from Gaua) and Taurius Cave stalagmite (150 km) show no 1809-11 cooling (stalagmite wet 1809-10); Kau Bay the only basin with cores that could resolve 1809

Source: PANGAEA via DataONE, DataCite, NOAA paleo; Quinn et al. 1996 data; Taurius Cave NOAA study 14988. Verification (Claude's reading or calculation): computed; catalogue read as fetched text. Status: negative (catalogue level) for Gaua's surroundings; coverage gaps (IMLGS not queried, U132). Notes: [strands/candidates/existing_cores_near_candidates_2026-10-28.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/candidates/existing_cores_near_candidates_2026-10-28.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F36: Tonga, Tahiti/Huahine, Hawaiʻi, Nov 1808 - Nov 1810**

We found no eruption, darkness, ash or sky report in Mariner vol. 2, the LMS reports of 1810-11 and the Connecticut Evangelical Magazine letters, or Campbell's Hawaiʻi chapters; 'weather remarkably fine' at Vava'u Nov 1810

Source: Mariner/Martin 1817 vols 1-2; LMS reports repr. 1811; Campbell 1816 (Gutenberg 46468); Connecticut Evangelical Magazine Jul 1810 pp. 278-279. Verification (Claude's reading or calculation): OCR only (Connecticut Evangelical Magazine page image checked). Status: negative; Davies's Tahiti journal 1808-10 at SOAS unread. Notes: [strands/asia_pacific_arabic/tonga_tahiti_hawaii_1808-10_2026-10-27.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/asia_pacific_arabic/tonga_tahiti_hawaii_1808-10_2026-10-27.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F37: worldwide (literature), 2024 - 12 Nov 2026**

We found no paper, preprint, thesis, abstract or news story that names a source volcano for 1808/09 or moves its date; all call it unidentified. Newest item Zanchettin et al. 2026 (Rendiconti Lincei 37:679-704) restates Meuer 2024 (northern extratropical) and notes UKESM1 uses an October date

Source: Zanchettin et al. 2026; Ro et al. 2026 egusphere-2026-6056; Innes et al. 2026 QSR; EGU26-18473, -19866; register B75-B78. Verification (Claude's reading or calculation): publisher and abstract text read. Status: negative; repeat about Feb 2027 (T58). Notes: [strands/method/new_scholarship_check_2026-11-12.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/new_scholarship_check_2026-11-12.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F38: Agrigan (Mariana Is.); Tambo Quemado (Bolivia), 1808-09 (claims read 12 Nov 2026)**

Grokipedia (AI-written) says Agrigan was "proposed in October 2025" with a 4 Dec 1808 Japanese tsunami; its footnote (Brönnimann 2019) does not mention Agrigan, we found no publication, GVP and USGS list 1917 as the only historical eruption, and the tsunami was a local Nankai event. Its "2023 Oregon State zircon" Tambo Quemado claim points to a project on Cerro Volcán Quemado that never mentions 1808. Of 26 checked claims, 14 are misattributed or wrong

Source: grokipedia.com/page/1808_mystery_eruption; Brönnimann et al. 2019 Nat. Geosci.; GVP 284160; OSU CEOAS REU 2023; Tsuji 2025. Verification (Claude's reading or calculation): page text read; claims untraced. Status: claims untraced; probably confabulated (inference); register B79. Notes: [strands/method/grokipedia_audit_2026-11-12.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/grokipedia_audit_2026-11-12.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._


**F39: Karthala, Grande Comore (11.75 S), 1808**

The current GVP page lists a confirmed 1808 Karthala eruption (no VEI), plus 1814 and 1821; none is in the GVP 4.6.7 snapshot of 8 May 2018 the project used; basaltic shield, so a poor fit for the andesitic ice glass (inference)

Source: GVP volcano 233010 (read 12 Nov 2026); VOTW467_8May18 eruption data (pyvolcans 1.3.3). Verification (Claude's reading or calculation): database text read; snapshot compared. Status: lead, low; GVP re-screen T59. Notes: [strands/method/grokipedia_audit_2026-11-12.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/grokipedia_audit_2026-11-12.md). Checked by a person: none yet.

Is it real, is it weather, and what would check it? If you can read the source, please record a check ([findings/CHECKS_README.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/findings/CHECKS_README.md)).

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 5. Polls

**Which hand item should be retrieved first?**

Votes set priorities; they don't settle evidence.

Options (from [access/open_tasks.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/access/open_tasks.md) section 3):
1. The *Ramoncita*'s diary, Lima to Manila 1809, passing Cabalían (U151)
2. HMS *Psyche*'s master's log at Surigao, Apr-Oct 1809 (T17)
3. The Banda and Ternate day registers, 1808-10, in Jakarta (T20)
4. The Bugis court diary of Bone, 1808-09, British Library (U34)
5. Unpublished 1809 ice-glass analyses held by researchers (U90-U92)

_Drafted by Claude (AI); read and posted by William John Suk._

**Which candidate should the next free check test?**

Votes set priorities; they don't settle evidence.

Options: Dakataua, Gaua, Cabalían, Agung, a Halmahera volcano (Todoko-Ranu or Dukono), a southern Banda volcano (Teon or Nila).

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 6. Sources and archives

**Ship logs from the eastern islands, Nov 1808-Mar 1809: who might have them?**

On the free evidence, Claude placed no Royal Navy ship east of the Straits of Malacca and south of the China coast in those months (Claude's judgement; a few were in the South China Sea). The Nationaal Archief catalogue lists no Dutch navy journal after June 1808, and CLIWOC has no entries there ([strands/ship_logs/fleet_log_inventory_2026-11-02.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/ship_logs/fleet_log_inventory_2026-11-02.md)). Who else was at sea: country traders from Bengal, American traders to Canton, Spanish galleons, Bugis and Chinese junks? If you know of a surviving log, journal or letter book for a ship in the Moluccas, Banda, New Guinea or the Philippines in these months, please post it.

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 7. Method and AI

**Where did the AI get it wrong? (corrections welcome)**

Most of this repository was drafted by Claude. Some of its errors it caught itself, and others only a person caught. William's page-image check of F15 found a corona dated one day early, because a table column was printed half a row out (see the post "A human check caught an AI error"). Claude was also asked not to take colonial categories for granted. It should not call people "natives", and it should not describe places without Europeans as "empty", "unpopulated" or as having "no observers", when people lived there and kept their histories mostly in oral form. The corrections, and the pattern behind them, are logged in [strands/method/language_corrections_log.md](https://github.com/WilliamJohnSuk/1808-eruption-search/blob/main/strands/method/language_corrections_log.md).

It has also corrected itself several times: a latitude band was withdrawn after validation (F30), a ship's itinerary was a year out (HMS *Cornwallis*), and a "January 1811" burial count was read from too few entries. There will be more errors. If you find a misread source, a wrong date conversion, an overconfident inference or a negative stated too strongly, post it here or open a "Re-check" issue. A correction that holds up is worth more than a new lead.

_Drafted by Claude (AI); read and posted by William John Suk._

---

## 8. Translation help

**Can you read one of these? Passages waiting for a reader**

Several findings rest on Claude's reading of a language, and no person has checked that reading yet. If you read one of these, please reply here or open a ["Re-check a source or finding"](https://github.com/WilliamJohnSuk/1808-eruption-search/issues/new?template=recheck-a-source-or-finding.yml) issue:

- Japanese: the Edo chronicle behind F04 (one reader is already checking it; a second check is welcome) and the Tottori entry behind F05.
- Dutch: the Batavia rice orders behind F17 and F24, and the Deshima day register behind F33.
- Vietnamese and literary Chinese: the Đại Nam thực lục passages behind F26 (we read only the modern translation; the Hán original is unseen) and the South China gazetteer entries coded in F25.
- Bugis script: the Bone court diary, 1808-09 (U34).

Say which page you read, and whether an AI tool helped.

_Drafted by Claude (AI); read and posted by William John Suk._
