# Scripts for notes/coral_footprint_1809-12_2026-10-28.md (28 Oct 2026)

Input: `pages2kv2.json` from github.com/fzhu2e/cfr-data (mirror of the NOAA PAGES2k v2 2017 dataset, Emile-Geay et al. 2017); world coastlines `countries.geo.json` from github.com/johan/world.geo.json (Natural Earth). Python 3 with matplotlib; run each script with `python3 -I`.

- `footprint.py pages2kv2.json out.csv`: every coral record with data in 1806-1816; monthly climatology 1790-1830 (or first 50 years) and July-June yearly anomalies in sd units for sub-annual records, annual anomalies for annual records; writes the CSV (`data/coral_footprint_1800-1820_2026-10-28.csv`), a yearly JSON and a monthly JSON (`data/coral_footprint_monthly_z_1800-1820_2026-10-28.json`); prints the Lombok monthly detail.
- `composite.py`: regional composites by year from the CSV (expects it at `work/coral_footprint_1800-1820.csv`; edit the path).
- `map.py csv geojson out.png`: the footprint map (`data/coral_footprint_map_1809-12_2026-10-28.png`).
- `fig.py pages2kv2.json external_series.csv out.png`: the six-panel figure (`data/coral_footprint_series_1805-1818_2026-10-28.png`); the external series file is `data/coral_footprint_external_series_2026-10-28.csv` (Tierney 2015 regional SST, Lough 2007 and 2015, Wei 2009, Quinn 1996 raw values, D'Arrigo 2006 printed values, Lombok NOAA anomalies, each with its source URL).

All values are Claude's calculations from downloaded published data (verification level: computed, not checked against page images). Colours follow the project data-visualisation palette; the red diverging steps were derived from the blue steps by matching OKLCH lightness.
