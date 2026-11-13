"""Indo-Pacific coral anomalies 1804-1814 from PAGES2k v2 (cfr-data copy), 27 Oct 2026.

Usage: python3 -I coral_enso.py pages2kv2.json BC09_NINO34.csv out.csv
Inputs: github.com/fzhu2e/cfr-data (pages2kv2.json, BC09_NINO34.csv).
For each record: season series (Nov-Apr labelled by the Jan year for sub-annual
records; calendar/coral year for annual ones), sign of El Nino response from the
correlation with Bunge & Clarke 2009 NDJ Nino3.4 over 1873-1995 (lag 0 or +1),
z = anomaly from a linear fit over 1780-1840, hp = deviation from a 7-yr centred
mean, sign-adjusted so + means El Nino-like. Jul-Nov z added for monthly records.
"""
import json, sys, math, csv, statistics as st

d = json.load(open(sys.argv[1]))
nino = {}
for r in csv.DictReader(open(sys.argv[2])):
    t = float(r['time']); y = int(t); m = int(round((t - y) * 12)) + 1
    nino[(y, m)] = float(r['NINO3.4'])

def ndj(y):
    v = [nino.get((y - 1, 11)), nino.get((y - 1, 12)), nino.get((y, 1))]
    return st.mean(v) if None not in v else None

def jn(y):
    v = [nino.get((y, m)) for m in range(7, 12)]
    return st.mean(v) if None not in v else None

def corr(a, b):
    ma, mb = st.mean(a), st.mean(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(
        sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))

WANT = ['Urvina', 'Savusavu', 'Hafera', 'Rarotonga', 'Vanuatu', 'Amedee', 'Palau',
        'DoubleReef', 'Lombok', 'Abraham', 'Malindi', 'Ifaty', 'HoutmanAbrolhos', 'Palmyra']
out = csv.writer(open(sys.argv[3], 'w', newline=''))
out.writerow(['record', 'lat', 'lon', 'variable', 'window', 'lag', 'r_vs_nino34', 'n_overlap',
              'year', 'z', 'hp_elnino_sign', 'z_julnov'])
ids = d['paleoData_pages2kID']
for i in ids:
    name = d['dataSetName'][i]
    if not d['archiveType'][i].lower().startswith('coral') or not any(w in name for w in WANT):
        continue
    pts = [(float(a), float(b)) for a, b in zip(d['year'][i], d['paleoData_values'][i])
           if a is not None and b is not None]
    pts = [(a, b) for a, b in pts if not math.isnan(a) and not math.isnan(b)]
    if not pts:
        continue
    res = len(pts) / (max(a for a, _ in pts) - min(a for a, _ in pts) + 1)
    ser, jnser = {}, {}
    for a, b in pts:
        y = int(math.floor(a)); f = a - y; m = int(f * 12) + 1
        if res >= 3:
            if f >= 10 / 12: ser.setdefault(y + 1, []).append(b)
            elif f < 4 / 12: ser.setdefault(y, []).append(b)
            if 7 <= m <= 11: jnser.setdefault(y, []).append(b)
        else:
            ser.setdefault(y, []).append(b)
    ser = {k: st.mean(v) for k, v in ser.items()}
    jnser = {k: st.mean(v) for k, v in jnser.items()}
    ks = [k for k in range(1780, 1841) if k in ser]
    if len(ks) < 15:
        print(name, 'no 1780-1840 coverage (gap)'); continue
    best = None
    for lag in (0, 1):
        kk = [k for k in ser if 1873 <= k <= 1995 and ndj(k + lag) is not None]
        if len(kk) < 20: continue
        r = corr([ser[k] for k in kk], [ndj(k + lag) for k in kk])
        if best is None or abs(r) > abs(best[1]): best = (lag, r, len(kk))
    sg = 1 if best[1] > 0 else -1
    mk = st.mean(ks); mv = st.mean(ser[k] for k in ks)
    sl = sum((k - mk) * (ser[k] - mv) for k in ks) / sum((k - mk) ** 2 for k in ks)
    sd = st.pstdev([ser[k] - (mv + sl * (k - mk)) for k in ks])
    if jnser:
        jb = [jnser[k] for k in range(1780, 1841) if k in jnser]
        jm, js = st.mean(jb), st.pstdev(jb)
    for k in range(1804, 1815):
        if k not in ser: continue
        z = (ser[k] - (mv + sl * (k - mk))) / sd
        w = [ser[j] for j in range(k - 3, k + 4) if j in ser]
        hp = (ser[k] - st.mean(w)) / sd * sg if len(w) >= 5 else ''
        zj = (jnser[k] - jm) / js if jnser and k in jnser else ''
        out.writerow([name, d['geo_meanLat'][i], d['geo_meanLon'][i], d['paleoData_variableName'][i],
                      'Nov-Apr' if res >= 3 else 'annual', best[0], round(best[1], 2), best[2], k,
                      round(z, 2), round(hp, 2) if hp != '' else '', round(zj, 2) if zj != '' else ''])
