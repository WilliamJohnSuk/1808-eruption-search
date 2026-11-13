# Newspaper download scripts (1808/09 eruption search)

These run on your Mac, because the archive sites block cloud servers but not your own connection. The scripts live in `scripts/` of the project folder (`~/Documents/1808-9 Volcano Project/`, moved out of Downloads on 27 Oct 2026). Everything `fetch_newspapers.py` downloads goes into `newspapers/script_downloads/`, along with its `run_log.txt`; `fetch_unavailable.py` files its downloads into papers/, books/, newspapers/ and archives/.

## Step 1: test (about 5 minutes)
Open Terminal and paste:

    cd ~/Documents/'1808-9 Volcano Project'/scripts && python3 fetch_newspapers.py test

Then tell Claude in the thread that the test is done. Claude reads `run_log.txt`, `_test/` and `_probe/` to see which sites answered and how the sites without an API lay out their pages, and then writes the remaining downloaders.

If macOS asks to install "command line developer tools", click Install. That is what provides `python3`.

## Step 2: download
    python3 fetch_newspapers.py all

You can stop it with Ctrl-C at any time, and re-running it skips files that were already downloaded. Expect it to take an hour or more. The Diario de Mallorca alone is about 330 daily PDFs.

To run a single source, replace `all` with its name:

| command | what it gets | status |
|---|---|---|
| `ia` | Internet Archive: Semanario 1808–09; Gazeta do Rio 1808 and 1809 extracts; Gaceta de Caracas t. I; Seville gazettes; Telegrafo Portuguez; Correio Braziliense; Diario de Mallorca daily Sept 1808–Jun 1810 | API is well documented |
| `dspace` | Minerva Peruana (BNP Perú), Gazeta de Guatemala (UCA), Redactor Americano (U. Distrital): issue PDFs plus `index.csv` | standard DSpace 7 API, untested on these sites |
| `boe` | Gazeta de Madrid, Gazeta Ministerial de Sevilla, Gazeta del Gobierno and (from 13 Mar 1810) Gazeta de la Regencia, day by day | depends on BOE day pages, untested |
| `gallica` | Gazette de France, Journal de l'Empire, Moniteur, Journal de Paris: OCR text for each issue (use `gallica-pdf` to get the scans too) | Gallica SRU, untested |
| `delpher` | Dutch newspapers: OCR of articles matching vulkaan, aardbeving, asch and similar terms | Delpher SRU, untested |
| `trove` | Sydney Gazette articles 1808–09. Needs a free Trove API key: `TROVE_KEY=yourkey python3 fetch_newspapers.py trove` | optional |
| `probe` | saves pages from BNE (El Aviso), the Hemeroteca Brasileira (Gazeta do Rio 1809), HNDM (Mexico) and Prensa Histórica | so their downloaders can be written next |

The date window is set at the top of the script (`START`, `END`). Since 16 Oct it runs 1 Sept 1808 to 30 June 1810, because news from Asia and the Pacific took 4–8 months to reach print in Europe and the Americas.

## Results of the first test (16 Oct)
- **Work from William's Mac:** Internet Archive, U. Distrital, Delpher and HNDM.
- **Fixed, awaiting `test2`:** BOE (wrong day-page address; now uses the direct PDF pattern), UCA (API at a different path; now auto-detected) and HNDM search pages.
- **Block scripts outright (403):** BNE Hemeroteca, Hemeroteca Brasileira and Gallica. These will not be scripted around. Download their issues in Safari, save them into the matching newspapers/ subfolder, and Claude reads them.
- **Rate-limited (429):** Prensa Histórica. Only a few issues are needed from it, so download them by hand.
- **Unreachable (connection timeout):** BNP Perú. Check whether it opens in Safari.

## Note on Gazeta del Gobierno and Gazeta de la Regencia file names (16 Oct)
The BOE stores these two papers under day folders that are not the issue date. For example, `1809-01-07__GGB-1809-7.pdf` is No. 7 of 10 Feb 1809. Files downloaded before 17:05 UTC on 16 Oct carry that misleading date. From the next run on, the script fetches these two papers by issue number and names new files `nodate__GGB-1809-<n>.pdf`. In either case, read the date from page 1. The Gazeta de Madrid and Seville file dates are unaffected.

## Added 4 Nov 2026 (wide source search)
- `fetch_bl_iiif.py`: downloads every page image of a British Library manuscript from its IIIF manifest. It uses the Python 3 standard library only, can be re-run, and waits 1 s between images. The default target is BL Add MS 12350, the Bugis diary of Bone 1808-1809, which the BL marks Public Domain, saved into `../archives/BL_Add_MS_12350/`. Usage: `python3 fetch_bl_iiif.py [MANIFEST_URL OUT_DIR WIDTH]`. (U34, T50)
- `detection_floor_2026-11-04/build.py`: great-circle distances from 14 candidate volcanoes to the 1808-10 observer records read so far. It writes `data/detection_floor_distances_2026-11-04.csv`. (T11, first half)
