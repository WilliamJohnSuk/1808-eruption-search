# Scripts for notes/creative_next_steps_2026-10-28.md (28 Oct 2026)

- `invert.py`: raw inversion of the Marshall et al. 2021 Greenland/Antarctic deposition emulator grid (GitHub cemac/volcanic-forcing-deposition, Zenodo 10.5281/zenodo.4038013; files data/axes.json, greenland_{jan,jul}.json, antarctica_{jan,jul}.json, forcing_{jan,jul}.json) against the 1809 composite deposition (Greenland 25.9, Antarctica 25.1 kg/km2, Sigl et al. 2013). Uncalibrated; see the note for why the raw answer (17-30 S) is not to be trusted.
- `calib.py`: Tambora calibration (emulator Tambora-like Greenland/Antarctic ratio versus the observed 0.87) and the ratio-of-ratios inversion.
- Output: data/deposition_emulator_ratio_by_latitude_2026-10-28.csv (median emulator Greenland/Antarctic ratio by eruption latitude for January and July eruptions, raw and normalised to the emulator's April-proxy Tambora ratio).
- Coral footprint: data/coral_footprint_1806-1816_2026-10-28.csv, computed from PAGES2k v2 corals (pages2kv2.json, GitHub mirror fzhu2e/cfr-data of the NOAA PAGES2k 2017 dataset); anomalies in standard-deviation units relative to a 1790-1830 monthly (or annual) climatology; for monthly records the yearly value is the July-June mean (year given = July year). Sign is the raw proxy sign: for d18O and Sr/Ca, positive = cooler and/or saltier.

All values are Claude's calculations (verification level: computed from downloaded published data, not checked against page images).
