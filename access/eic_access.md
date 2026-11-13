# East India Company records: what Claude can reach (16 Oct 2026)

| Resource | Reachable from here? | What was done | Result |
|---|---|---|---|
| BL catalogue searcharchives.bl.uk (IOR/L/MAR/B ship journals) | Yes (catalogue text) | Read records for Wexford 173C, Preston 307E etc. | Preston: no digitised content; BL says MSS must be consulted in London (reader pass; can pre-order online). |
| Qatar Digital Library, Wexford journal IOR/L/MAR/B/173C (304 images, PDF 589 MB) | Record page yes; page images NO (image server errors via WebFetch; viewers robots-blocked) | Confirmed item, image URL pattern `https://iiif.qdl.qa/iiif/images/81055/vdc_100000001441.0x000131/IOR_L_MAR_B_173C_NNNN.jp2/full/full/0/default.jpg` | Free to view in a browser; William can open Universal Viewer https://www.qdl.qa/en/universal-viewer/81055/vdc_100000001441.0x000131 and look at the Cape arrival (9 Dec 1808) pages, or download them and upload. |
| oldweather/EEIC GitHub (CDMP keyed EIC logbooks, 893 logs) | Yes (git clone) | Extracted every record 15 Oct 1808 – 31 Mar 1809: 29 ships, 1,978 daily records -> data/eic_keyed_weather_1808-10_1809-03.csv | Keyed weather words only (FAIR, HAZY, FOGGY, DARK...), not free remarks. No smoky/ash/dust/red-sun/dry-fog wording; haze/fog entries are ordinary (Southern Ocean fog, monsoon haze). Wexford is keyed: 25 Nov–9 Dec 1808 SE Africa to Cape, nothing unusual. |
| NOAA NCEI C00785 (keyed data) / C01017 (1,235 log images) | Metadata yes; images behind NERMS login | — | Images need an NCEI account or order. |
| Asiatic Annual Register vols 10–12 (archive.org Google scans) | Yes (OCR) | Keyword search + ~45 pages read; see asiatic_annual_register_scan.md | Nothing for Dec 1808–mid 1809. Padang earthquake Nov/3 Dec 1807 (vol 10 p.198) is a year early. |

## Wexford page images checked (William's downloads)
- QDL image 0209 = Fri 18 & Sat 19 Nov 1808, lat obs 24°16'S / 24°38'S, lon ~55°E (SE of Madagascar). Remarks: light airs, variable, fair, some light showers; cable and sail work; "In company as before"; sick list 1. Nothing on sky, sun or haze. QDL image numbers run ~10 ahead of the CDMP page numbers, so 8–9 Dec 1808 (Cape arrival) should be QDL ~219.
- Images 0209–0220 (18 Nov–17 Dec 1808) transcribed: notes/wexford_journal_nov-dec1808.md (negative).

## Haze frequency test, EIC keyed logs (16 Oct 2026)
All CDMP-keyed EIC observations at lat ≤30° (N or S), lon 40–135°E; share of daily records whose weather words include HAZY/HAZE/THICK/SMOKY. Baseline = same calendar month in all other years 1789–1834.

| Month | Baseline obs / % hazy | 1808–09 obs / % hazy |
|---|---|---|
| Aug | 3161 / 15.6 | 256 / 18.4 |
| Sep | 2957 / 15.2 | 207 / 10.1 |
| Oct | 3521 / 9.7 | 165 / 1.8 |
| Nov | 3525 / 8.8 | 119 / 2.5 |
| Dec | 2916 / 13.6 | 49 / 4.1 |
| Jan 1809 | 3724 / 13.1 | 191 / 7.9 |
| Feb 1809 | 3570 / 10.9 | 147 / 13.6 |

No excess haze in the tropical Indian Ocean / South China Sea Sept–Dec 1808; if anything below normal. Caveats: small 1808 samples, keying captures only standard weather words, ship/keyer mix varies. 27 individual hazy entries Sept–10 Dec 1808 all read as ordinary monsoon weather (rain, squalls, lightning).
- Full journal run 2 Aug 1808 – 25 Mar 1809 (QDL images 0175–0246) now transcribed: notes/wexford_journal_aug1808-mar1809.md. Negative throughout. Partial QDL PDF (Safari, 96%) is enough: images are ASCII85-wrapped JPEGs, PDF image index = QDL image number + 1.

## Extension back to March 1808 (16 Oct 2026, after the window question)
Same test, calendar-year 1808 (a slightly different line parser from the table above, so Oct–Dec numbers differ a little; both agree). Words HAZ/THICK/SMOK.

| Month 1808 | Baseline obs / % | 1808 obs / % |
|---|---|---|
| Mar | 5222 / 12.9 | 76 / 14.5 |
| Apr | 5085 / 7.4 | 108 / 7.4 |
| May | 4116 / 12.2 | 145 / 11.0 |
| Jun | 2788 / 15.5 | 37 / 13.5 |
| Jul | 3245 / 16.0 | 111 / 9.0 |
| Aug | 4335 / 15.8 | 126 / 19.0 |
| Sep | 3727 / 15.6 | 100 / 17.0 |
| Oct | 3425 / 10.6 | 84 / 3.6 |
| Nov | 2861 / 10.6 | 79 / 2.5 |
| Dec | 3606 / 14.5 | 28 / 0.0 |

No haze excess Mar–Sept 1808 either. August's small excess is Wexford in the Gulf (seasonal shamal haze). All 703 keyed records Mar–Sept 1808 (24 ships): data/eic_keyed_weather_1808-03_1808-09.csv. Only odd entry: Harriet 18 Sept 1808, 7.2N 74.3E, "WATER SMOOTH, DISCOLORED" (near the Malabar/Ceylon coast; coastal or river water likely; weak, unverified).

### Unkeyed port stays = unread daily logs in the key window
CDMP keyed sea days only, so long harbour stays are blank in the data but present in the manuscripts. List: data/eic_unkeyed_port_stays_1808.txt. The 1808–09 China fleet lay at Whampoa/Canton from late Sept 1808 to early Mar 1809: Royal George (L/MAR/B/17L, there from 5 July 1808), Alnwick Castle (189D), Elphinstone (201C), Essex (229T), Canton (288H), Warley (182H). In Bengal (Hooghly) through Oct 1808–early 1809: Streatham (185B), Earl Spencer (227F), Sir William Bensley (247D), Harriet (275K). Bombay: Earl St Vincent (209F), Alexander (174F), Lord Eldon (143D). Madras: Phoenix (175I, Aug–Oct 1808). Of these only Royal George is on QDL (record vdc_100000001320.0x000340, 13 Apr 1807–28 Jun 1809, 272 images, PDF 410 MB, browser download requested from William 16 Oct). The rest are BL reading-room only.
