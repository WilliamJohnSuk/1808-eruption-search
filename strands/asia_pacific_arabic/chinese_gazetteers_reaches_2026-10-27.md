---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: asia_pacific_arabic
date: 2026-10-27
---

# Chinese local gazetteers (difangzhi), Jiaqing 13-15 (Jul 1808 - Jun 1810), via REACHES

Thread "Search Chinese local gazetteers for 1808-09 omens", 27 Oct 2026. Register section B60.
Earlier China work (16 Oct): notes/asian_arabic_round4.md part I (court record, Qingshigao, 18 Taiwan gazetteers, 371 Daizhige geography files, biji). This pass covers the mainland county gazetteers that were missing then.

## Verification levels used here

- **[coded]**: a REACHES database row. REACHES (Academia Sinica / NOAA study 23410, CC0) codes every record in Zhang De'er, *Zhongguo sanqiannian qixiang jilu zongji* (vol. 3, 1st ed. 2004 for the Qing). Each row gives date (lunar and Gregorian), county, coordinates, event codes and the source gazetteer with juan. **It does not contain the quoted Chinese text.** So no quotation below is verbatim; the wording is the database's category, translated by Claude. The original sentence must be read in Zhang De'er (page = first number of the record ID, e.g. 2755-36 = p. 2755) or in the gazetteer itself.
- **[text]**: fetched as modern text; **[calc]**: Claude's counts from the database.
- No page image was seen in this pass.

## How the data were obtained

- ctext.org, its API, zh.wikisource category pages, shidianguji, baidu, dsjyj.com.cn: blocked (robots or proxy). zh.wikisource has mostly Siku-era (pre-1808) provincial gazetteers anyway.
- archive.org full-text search does index some Chinese OCR, but only 14-17 hits for 嘉慶十三年/十四年, all modern books; the one gazetteer with OCR (道光《新寧縣志》 1839, Taishan) cannot be searched inside (no hOCR) and its text URL is too long for the fetch tool. Not useful.
- NOAA blocks Claude's cloud container. William downloaded `reachesv3.1data.txt`, the three code tables and `noaa-reaches-vol234.xlsx` to `~/Downloads/1808-9 Volcano Project/data/reaches/` (27 Oct 03:28-03:32 UTC). The .txt has lost all Chinese characters ("?"); the .xlsx keeps province, county and source.
- Extraction scripts: scripts/reaches_2026-10-27/ (README there). Outputs: data/reaches_1808-07_1810-06_2026-10-27.tsv (646 rows, all provinces, decoded, with sources) and data/reaches_south_china_baseline_1780-1840_2026-10-27.tsv.
- REACHES Jiaqing 13-14 = Zhang De'er vol. 3 pp. 2748-2762 (JQ15 to p. 2768).

## 1. Core window, Nov 1808 - Mar 1809, south of 32°N (all 87 rows read)

Nothing in the gazetteers coded for this window describes a red sky, red or dim sun, haze, ash or dust fall, booms, sea surge or pumice anywhere in South China. The 9 Jan - early Feb 1809 Edo red-sky period has no Chinese counterpart in this database. **We found no report of red skies, a dim sun, ashfall or detonations in these.** The rows are mostly harvest, flood, drought, famine and price entries dated only to the year.

Dated weather items in the core window:

| Gregorian | Lunar | Place (modern) | Coded event | Source (per REACHES) | Rec. | Note |
|---|---|---|---|---|---|---|
| 18 Nov - 16 Dec 1808 | JQ13/10 | Lingshan, Guangxi (22.3°N) | frost; water froze | 民國《靈山縣志》地志 | 2756-16 | [coded] |
| 18 Nov - 16 Dec 1808 | JQ13/10 | Hepu (Lianzhou), Guangxi coast (21.7°N) | icy rain, frost | 道光《廉州府志》卷二十一事紀 | 2756-17 | [coded]; same cold surge as Lingshan |
| 23 Nov 1808 | JQ13/10/6 | Mouding (Dingyuan), Yunnan | iridescent / coloured clouds (慶雲-type, vocab 彩雲) | 道光《定遠縣志》卷六祥異 | 2757-07 | [coded]; usually an auspicious stock omen; weak lead only |
| 4 Nov 1808 | JQ13/9/16 | Wenchang, Hainan | typhoon with tidal flood, deaths | 咸豐《文昌縣志》卷十六災祥 | 2756-06 | [coded]; typhoon surge, not a tsunami |
| 16 Jan - 13 Feb 1809 | JQ13/12 | Yangshan, N Guangdong | heavy snow | 道光《陽山縣志》卷十三事紀 | 2755-36 | [coded]; = F5 of 16 Oct (now traced to its gazetteer) |
| 16 Jan - 13 Feb 1809 | JQ13/12 | Eryuan, Yunnan | heavy snow | 民國《新纂雲南通志》卷十八氣象 | 2757-09 | [coded] |
| 14 Feb 1809 | JQ14/1/1 | Tianjin and Dongguang (N China) | black vapour (黑氣) | 同治《續天津縣志》卷一祥異; Qingshigao | 2757-10, 2757-25 | [coded]; Dongguang = F1 of 16 Oct; Tianjin is a second site the same New Year's Day |
| 19 Feb 1809 | JQ14/1/6 | Yizhang, S Hunan | "yellow rain" | 嘉慶《宜章縣志》卷二十三事紀 | 2761-07 | [coded]; pollen or dust are the usual causes |
| Feb - Mar 1809 | JQ14/1-2 | Shandong, Henan (several) | gale with darkened day | various | 2758-07/10, 2760-20/21 | [coded]; spring dust storms, ordinary |

## 2. Spring 1809: late snows across SE China (new)

| Gregorian | Lunar | Place | Coded event | Source | Rec. |
|---|---|---|---|---|---|
| 18 Apr 1809 | JQ14/3/4 | Yingshang, Anhui | heavy frost | 道光《潁上縣志》卷十三祥異 | 2759-17 |
| 28 Apr 1809 | JQ14/3/14 | Wanzai, Jiangxi (28.2°N) | heavy snow | 道光《萬載縣志》卷二十五祥異 | 2759-34 |
| 6 May 1809 | JQ14/3/22 | Qimen, Anhui (29.9°N) | cold, rain and snow | 道光《祁門縣志》卷三十六祥異 | 2759-24 |
| 14 May 1809 | JQ14/4/1 | Chengbu, SW Hunan (26.4°N) | rain and snow | 同治《城步縣志》卷十祥異 | 2761-12 |
| 14 Jun 1809 (as coded) | JQ14/5/2 | Kaihua and Jiangshan, W Zhejiang | rain and snow | 光緒《開化縣志》卷十四祥異; 同治《江山縣志》卷十二祥異 | 2759-07/08 |

- Qingshigao (F2 of 16 Oct) gives Jiangshan's snow as 立夏前三日 = about 3 May 1809. REACHES codes it 5th month 2nd day (14 Jun). One of the two is a date error (perhaps 四月 vs 五月, or a 1st-edition coding slip). The two neighbouring counties agree with each other, so the Zhang De'er page (2759) is needed to settle it.
- The 1808 harvest-year counts below show that late-spring snows in the south are rare in REACHES, so this cluster is worth noting. It fits cooling after an eruption in late 1808, but a single cold spring has other causes.

## 3. Spring 1808: a larger late-snow cluster BEFORE the putative eruption (new)

In the 4th lunar month of JQ13 (26 Apr - 24 May 1808), REACHES codes snow or heavy snow at ten sites in Hunan (Daozhou, Baoqing), S Hunan/Guangdong border (Yizhang), Guizhou (Weining, Changshun), Chongqing (Qijiang) and Yunnan (Songming, Luoping, Luliang), plus frost at Yueqing, Zhejiang (JQ13/4/4 = 29 Apr 1808) and frost at Jingyuan, Gansu. Sources: 嘉慶《宜章縣志》卷二十三, 光緒《道州志》卷十二, 道光《寶慶府志》卷九十九, 道光《大定府志》卷四十五, 道光《廣順州志》卷十二, 道光《綦江縣志》卷十, 光緒《續修嵩明州志》卷二, 民國《羅平縣志》卷一, 道光《陸涼州志》卷八, 光緒《樂清縣志》卷十三 (records 2752-02 to 2757-06). [coded]

- All fall in one lunar month, so this is probably one strong cold surge, and the Yunnan-Guizhou sites are high (1,500-2,200 m), where April snow is less unusual.
- Even so, 10 sites is the joint highest late-spring count 1780-1840 (with 1786). It sits in the Mar-Jun 1808 window that Chenoweth (2001) and Timmreck (2021) mention as a possible earlier date. **Suggestion, not a finding:** worth a look by whoever tests the "two eruptions / early 1808" idea; it is not evidence of an eruption by itself.

## 4. 1809 drought and famine in Guangdong and Guangxi

In JQ14 (1809) 26 county sites in Guangdong and Guangxi (box 20-25.6°N, 106-117.5°E) record drought or famine: the Pearl River delta (Guangzhou fu, Nanhai, Foshan, Shunde, Sanshui, Xiangshan, Xinhui, Zengcheng, Longmen), the West River (Gaoyao, Sihui, Guangning, Deqing, Xining, Kaijian, Huaiji, Cangwu), Kaiping, Enping, central Guangxi (Wuming, Shanglin, Binzhou) and Lingshan/Qinzhou. Dated ones are spring 1809 (JQ14/1-4); Xinhui already reports famine and high prices in JQ13/12 (Jan-Feb 1809). [coded]

- Baseline [calc]: 1808 = 10 sites, 1810 = 9, 1786 = 51, 1787 = 41, 1795 = 29, 1820 = 22. So 1809 is the largest southern drought-famine year between 1796 and 1819.
- It coincides with the Batavia rice failure "unusual drought of the season" (Plakaatboek order 5 Oct 1809, register B51).
- **Alternative cause:** 1809 was the peak of the Red Flag pirate war; Zheng Yi Sao's fleets blockaded the Pearl River delta and burned delta villages in 1809, which cut rice imports. Delta famine and high prices are therefore not purely climatic. The West River and Guangxi droughts are less affected by that.
- Nationwide drought counts (REACHES drought series, Lin et al. 2020) are low in 1808 (29) and 1809 (27) compared with 1807 (104) and 1811 (122) [text], so the drought was regional.

## 5. Sea, earth and sound

- No abnormal tide, sea-colour change or sea surge coded anywhere on the China coast Jul 1808 - Jun 1810. Nothing matches the 4 Dec 1808 Kii tsunami or the 18 Aug 1808 Naha oscillations. [coded]
- Earthquake: only Henan 1809. [coded]
- Pengze, Jiangxi, JQ14/7 (Aug 1809): "abnormal sky colour" with "peculiar sounds", in a drought summer (嘉慶《彭澤縣志》卷十五祥異, 2759-28). Too late for the eruption itself; could be thunder-less lightning or a meteor. [coded]

## 6. Later items (context)

- Winter 1809/10: Shanghai, Songjiang, Jinshan, Qingpu, Tianchang, Xiao: severe cold, waters frozen (Nov 1809 - Jan 1810); Taizhou haze; Sichuan heavy snow. Confirms F4 of 16 Oct (frozen Huang and Huai).
- 4-20 Feb 1810 (JQ15/1): widespread dust storm with darkened sun over Shandong, Henan, Anhui, N Jiangsu (two waves, about 4 Feb and 19-20 Feb). Red wind, red fog, red sun at some sites. Classic spring dust, matches Qingshigao 風霾晝晦 of 20 Feb 1810.
- 5 Feb 1810: "red snow" at Yongtai, Fujian (民國《永泰縣志》卷二大事, 2766-25). Odd; red snow usually means dust in snow, and it falls during the same dust-storm month.

## 7. Sensitivity check against Tambora [calc]

- Sky-colour codes (red sun, dim sun, red cloud, red haze, abnormal sky colour, black/red dust rain), excluding wind/dust storm rows: 1808 = 0, 1809 = 2 (the New Year black vapour), **1815 = 0, 1816 = 0**. The gazetteers as coded in REACHES did not record Tambora's optical effects either, so their silence about red skies in 1808/09 is **weak evidence of absence**.
- Winter cold south of 25.5°N (frost, snow, ice, by winter starting year): 1807/08 = 7 sites, 1808/09 = 3, 1809/10 = 1, 1814/15 = 7, **1815/16 = 8** (e.g. Chengmai, Hainan, heavy snow JQ20/11), 1831/32-1835/36 up to 22. 1808/09 is not an unusually cold southern winter.

## 8. What this pass adds, and what it does not

- Adds: the first systematic check of mainland South China gazetteers for 1808-1810, with gazetteer and juan for every row; no red-sky or ash record in South China in the Edo window; two late-spring snow clusters (1808, 1809); a regional Guangdong-Guangxi drought-famine in 1809 parallel to Batavia's.
- Does not: give any verbatim Chinese text. REACHES is only as complete as Zhang De'er, who selected weather records and may have left out omen-only entries (e.g. a plain 天赤 or 日赤 might be coded or might be omitted).

## 9. Needs William's hands (library)

1. **Zhang De'er 2004, vol. 3, pp. 2748-2768** (JQ13-15), photographs or scans, to read the original sentences for the rows above (especially 2755-10/22/23, 2756-16/17, 2757-07, 2759-07/08/24/34, 2761-12, the Guangdong famine pages 2761-2762). Interlibrary loan; the 2013 2nd edition renumbers pages, so ask for the 2004 edition or note the edition.
2. 中國方志庫 (Airusheng) or 中國地方志數據庫 / CADAL, if Syracuse University subscribes: full-text search of 嘉慶十三年 / 十四年 with 天赤, 日赤, 日無光, 紅光, 雨灰, 海溢, 霜 in Fujian, Guangdong, Guangxi, Hainan, Zhejiang gazetteers. This is the only way to catch omen entries Zhang De'er left out.
3. Optional: 澳門編年史 (Wu Zhiliang ed., 2009), vol. 2, 1808-09 entries (Macau weather and events during the British occupation of Sept-Dec 1808).
4. Already in the register (B17): W. Kerr, Meteorological Journal, Canton and Macao 1809, BL Add MS 8964 (AM Digital "Exploration", subscription). It would cover the Edo red-sky weeks from Canton.

## Search log

| # | Query / action | Result |
|---|---|---|
| 1 | curl NOAA, ctext, zh.wikisource, archive.org, REACHES site, Kanripo from container | all 403 at proxy except GitHub |
| 2 | device_bash curl (VM) | no network |
| 3 | WebFetch NOAA REACHES directory | file list; data file truncated at 47 k chars |
| 4 | WebFetch reaches.rcec.sinica.edu.tw | download buttons only, no URLs |
| 5 | archive.org fts "嘉慶十三年", "嘉慶十四年" | 14 / 17 hits, modern books only; 新寧縣志 1839 found |
| 6 | archive.org advancedsearch title 縣志/府志/州志 | 1,530 items, mostly image-only .cn scans |
| 7 | inside.php 新寧縣志 1839 | "No hOCR or Abbyy file present" |
| 8 | WebSearch (zh, several) for 嘉慶十三/十四年 with 大雪, 霜, 日赤, 旱, 饑 | only secondary snow lists; cnstock Hainan list (JQ20/11 Chengmai snow = 1815/16); no 1808-09 hits |
| 9 | WebFetch HKO, Peter Huston (新安縣志 1819), Marks ch. "It never used to snow", Hsieh 1984 Guangdong climate | nothing for 1808-09 (Xin'an list on Ng 1983 pp. 102-106 not online) |
| 10 | ctext API, zh.wikisource categories, zh.wikipedia snow list | blocked / no 1800-1815 entries |
| 11 | REACHES drought series (Lin 2020) via WebFetch | 1808 = 29, 1809 = 27 nationwide |
| 12 | REACHES full data + xlsx (William's download) | sections 1-7 |
