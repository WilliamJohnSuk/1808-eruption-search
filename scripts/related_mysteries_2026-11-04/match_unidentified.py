#!/usr/bin/env python3
"""Match unidentified eVolv2k v2.1 events 1750-1850 against GVP VOTW 4.6.7 eruptions.

Inputs: data/evolv2k_v2.1_events_2026-10-28.csv (project) and the VOTW 4.6.7
(8 May 2018) eruption + names files bundled in the pyvolcans 1.3.3 wheel (PyPI).
Usage: python3 match_unidentified.py ERUPTIONS_CSV NAMES_CSV EVOLV_CSV OUT_CSV
Window: start year within -2..+1 of the ice-core year; VEI >= 3 (or VEI unknown);
latitude band by the eVolv2k default latitude: 45 -> 30..75N, -45 -> 30..75S, 0 -> 25S..25N.
"""
import csv, sys
er, nm, ev, out = sys.argv[1:5]
names = {}
for row in csv.reader(open(nm, encoding='latin-1')):
    names[row[2]] = (row[0], row[1])
cands = []
for x in csv.DictReader(open(er)):
    try:
        y = int(float(x['Start Year'])); lat = float(x['Latitude'])
    except ValueError:
        continue
    vei = x['VEI'].strip()
    cands.append((y, lat, float(x['Longitude']), vei, x['Eruption Category'], x['Volcano Number'], x['Start Month']))
UNID = {1762: 'tropical', 1770: 'N', 1786: 'N', 1796: 'N', 1797: 'N', 1809: 'tropical', 1821: 'S', 1846: 'N'}
band = {'N': (30, 75), 'S': (-75, -30), 'tropical': (-25, 25)}
rows = []
for yr, b in UNID.items():
    lo, hi = band[b]
    for (y, lat, lon, vei, cat, vn, mo) in cands:
        if yr - 2 <= y <= yr + 1 and lo <= lat <= hi and (vei == '' or int(vei) >= 3):
            n, c = names.get(vn, ('?', '?'))
            rows.append([yr, b, n, c, y, mo, vei or 'unknown', 'confirmed' if cat == '1' else 'uncertain', round(lat, 2), round(lon, 2)])
rows.sort(key=lambda r: (r[0], -(int(r[6]) if r[6] != 'unknown' else 0)))
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ice_year', 'band', 'volcano', 'country', 'gvp_start_year', 'start_month', 'vei', 'gvp_category', 'lat', 'lon'])
    w.writerows(rows)
for r in rows:
    print(*r, sep=' | ')
