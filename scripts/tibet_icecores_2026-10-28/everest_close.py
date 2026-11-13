"""Close reading of rongbuk2009.txt (Kaspari 2009) and dasuopu2020elem-noaa.txt (Gabrielli 2020). Reads from argv[1] dir."""
import sys, re, math, csv, os
from collections import defaultdict, Counter
D = sys.argv[1]
def num(t):
    try:
        v = float(t)
    except ValueError:
        return None
    return None if (math.isnan(v) or v <= -900) else v
# ---------- Everest: two space-delimited tables
lines = open(os.path.join(D, 'rongbuk2009.txt'), encoding='utf-8', errors='replace').read().split('\n')
tabs = []; cur = None
for l in lines:
    t = l.split()
    if not t: continue
    if t[0].startswith('Year'):
        cur = {'cols': [re.sub(r'\(.*?\)', '', c) for c in t], 'raw': t, 'rows': []}; tabs.append(cur); continue
    if cur is None: continue
    vals = [num(x) for x in t]
    if any(v is None for v in vals[:2]) or vals[0] is None: continue
    if len(vals) == len(cur['cols']): cur['rows'].append(vals)
print('Everest tables:', [(len(t['rows']), t['cols']) for t in tabs])
T1, T2 = tabs[0], tabs[1]
assert len(T1['rows']) == len(T2['rows'])
# join by row (check ages equal)
mism = sum(1 for a, b in zip(T1['rows'], T2['rows']) if abs(a[0] - b[0]) > 1e-6)
print('age mismatches between tables:', mism)
cols = T1['cols'] + T2['cols'][2:]
rows = [a + b[2:] for a, b in zip(T1['rows'], T2['rows'])]
ci = {c: i for i, c in enumerate(cols)}
# replacement floors: value equal to the column minimum that occurs >= 20 times
floors = {}
for c in cols[2:]:
    vals = [r[ci[c]] for r in rows if r[ci[c]] is not None]
    cnt = Counter(vals); mn = min(vals)
    if cnt[mn] >= 20: floors[c] = (mn, cnt[mn])
print('replacement floors (value, count):', floors)
def val(r, c):
    v = r[ci[c]]
    if v is None: return None
    if c in floors and v <= floors[c][0]: return None
    return v
# Xu-style EFc(Bi): median over x in Sr, Ca, La, Fe, Al of (Bi/x)_ice / (Bi/x)_UCC ; UCC Rudnick & Gao 2003 (ppm): Bi 0.16, Sr 320, Ca 25700, La 31, Fe 39200, Al 81500
UCC = {'Bi': 0.16, 'Sr': 320, 'Ca': 25700, 'La': 31, 'Fe': 39200, 'Al': 81500}
unit = {'Sr': 1e-3, 'La': 1e-3, 'Bi': 1e-3, 'Ca': 1, 'Fe': 1, 'Al': 1}   # to ppb
def efc(r):
    bi = val(r, 'Bi')
    if bi is None: return None
    out = []
    for x in ['Sr', 'Ca', 'La', 'Fe', 'Al']:
        v = val(r, x)
        if v is None or v <= 0: continue
        out.append((bi * unit['Bi'] / (v * unit[x])) / (UCC['Bi'] / UCC[x]))
    if len(out) < 3: return None
    out.sort(); n = len(out)
    return out[n // 2] if n % 2 else 0.5 * (out[n // 2 - 1] + out[n // 2])
samples = []
for r in rows:
    samples.append({'age': r[0], 'depth': r[1], 'Bi': val(r, 'Bi'), 'Tl': val(r, 'Tl'), 'Al': val(r, 'Al'), 'S': val(r, 'S'), 'Ca': val(r, 'Ca'), 'Fe': val(r, 'Fe'), 'Sr': val(r, 'Sr'), 'La': val(r, 'La'), 'EFc': efc(r)})
samples.sort(key=lambda s: s['age'])
# excess S: S - k*Ca with k = median S/Ca over 1700-1800 samples
k = sorted(s['S'] / s['Ca'] for s in samples if 1700 <= s['age'] < 1801 and s['S'] and s['Ca'])
k = k[len(k) // 2]; print(f'baseline S/Ca median (samples 1700-1800) = {k:.3f}')
for s in samples:
    s['xS'] = (s['S'] - k * s['Ca']) if (s['S'] is not None and s['Ca'] is not None) else None
# yearly maxima of Bi, EFc, xS
ymax = defaultdict(lambda: {'Bi': (None, None), 'EFc': (None, None), 'xS': (None, None), 'n': 0})
for s in samples:
    y = int(math.floor(s['age'])); ymax[y]['n'] += 1
    for k2 in ['Bi', 'EFc', 'xS']:
        v = s[k2]
        if v is not None and (ymax[y][k2][0] is None or v > ymax[y][k2][0]): ymax[y][k2] = (v, s['age'])
print('\n--- Everest: 15 largest yearly maxima of raw Bi (ppt), 1700-1850 ---')
for y, d in sorted(((y, d) for y, d in ymax.items() if 1700 <= y <= 1850 and d['Bi'][0]), key=lambda t: -t[1]['Bi'][0])[:15]:
    print(f'  {y}: Bi {d["Bi"][0]:7.2f} ppt at {d["Bi"][1]:.2f}   EFc max {d["EFc"][0]:8.1f} at {d["EFc"][1]:.2f}')
print('\n--- Everest: 15 largest yearly maxima of EFc(Bi), 1700-1850 ---')
for y, d in sorted(((y, d) for y, d in ymax.items() if 1700 <= y <= 1850 and d['EFc'][0]), key=lambda t: -t[1]['EFc'][0])[:15]:
    print(f'  {y}: EFc {d["EFc"][0]:8.1f} at {d["EFc"][1]:.2f}   Bi {d["Bi"][0]:7.2f} ppt')
# Xu rule on full series: EFc > mean + 2 sd (per sample), list years 1650-2002
ef = [s['EFc'] for s in samples if s['EFc'] is not None]
mu = sum(ef) / len(ef); sd = (sum((e - mu) ** 2 for e in ef) / (len(ef) - 1)) ** 0.5
thr = mu + 2 * sd
flag = sorted(set(int(math.floor(s['age'])) for s in samples if s['EFc'] is not None and s['EFc'] > thr))
print(f'\nXu rule: EFc mean {mu:.1f}, sd {sd:.1f}, threshold {thr:.1f}; years with a sample above it: {flag}')
# log-based rule (more robust): log10 EFc > median + 3 MAD
lg = sorted(math.log10(e) for e in ef if e > 0); med = lg[len(lg) // 2]; mad = sorted(abs(x - med) for x in lg)[len(lg) // 2] * 1.4826
thr2 = 10 ** (med + 3 * mad)
flag2 = sorted(set(int(math.floor(s['age'])) for s in samples if s['EFc'] is not None and s['EFc'] > thr2))
print(f'robust rule: median EFc {10**med:.1f}, MAD {mad:.2f} dex, threshold {thr2:.1f}; years: {flag2}')
print('\n--- Everest samples 1808.0-1811.5 and 1814.5-1817.5 ---')
print('  age     depth   Bi(ppt)  Tl    Al(ppb)  S(ppb)  Ca(ppb)  Fe   EFc    xS')
for s in samples:
    if 1808 <= s['age'] < 1811.5 or 1814.5 <= s['age'] < 1817.5:
        f = lambda v, w=7, p=2: ('.'.rjust(w) if v is None else f'{v:{w}.{p}f}')
        print(f'  {s["age"]:.2f}  {s["depth"]:6.2f} {f(s["Bi"])} {f(s["Tl"],5)} {f(s["Al"],8,1)} {f(s["S"],7,1)} {f(s["Ca"],8,1)} {f(s["Fe"],6,1)} {f(s["EFc"],7,1)} {f(s["xS"],7,1)}')
print('\n--- Everest yearly: n, max Bi, max EFc, max excess S, 1800-1830 ---')
for y in range(1800, 1831):
    d = ymax[y]; f = lambda v: '   .  ' if v is None else f'{v:6.1f}'
    print(f'  {y} n={d["n"]:2d}  Bi {f(d["Bi"][0])}  EFc {f(d["EFc"][0])}  xS {f(d["xS"][0])}')
# excess S top years
print('\n--- Everest: 10 largest yearly maxima of excess S (ppb) 1700-1850 ---')
for y, d in sorted(((y, d) for y, d in ymax.items() if 1700 <= y <= 1850 and d['xS'][0] is not None), key=lambda t: -t[1]['xS'][0])[:10]:
    print(f'  {y}: xS {d["xS"][0]:6.1f} at {d["xS"][1]:.2f}')
# write derived CSV 1795-1830
with open(os.path.join(D, 'everest_samples_1795-1830_efc.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['age', 'depth_m', 'Bi_ppt', 'Tl_ppt', 'Al_ppb', 'S_ppb', 'Ca_ppb', 'Fe_ppb', 'Sr_ppt', 'La_ppt', 'EFc_Bi_Xu', 'excess_S_ppb'])
    for s in samples:
        if 1795 <= s['age'] < 1831:
            w.writerow([s['age'], s['depth'], s['Bi'], s['Tl'], s['Al'], s['S'], s['Ca'], s['Fe'], s['Sr'], s['La'], None if s['EFc'] is None else round(s['EFc'], 2), None if s['xS'] is None else round(s['xS'], 2)])
# ---------- Dasuopu
dl = [l for l in open(os.path.join(D, 'dasuopu2020elem-noaa.txt'), encoding='utf-8', errors='replace').read().split('\n') if l and not l.startswith('#')]
hdr = dl[0].split('\t'); di = {c: i for i, c in enumerate(hdr)}
drows = [[num(x) for x in l.split('\t')] for l in dl[1:]]
drows = [r for r in drows if len(r) == len(hdr) and r[di['age_CE']] is not None]
drows.sort(key=lambda r: r[di['age_CE']])
print('\n--- Dasuopu: sampling gaps > 0.5 yr, 1700-1850 ---')
for a, b in zip(drows, drows[1:]):
    ga = b[di['age_CE']] - a[di['age_CE']]
    if ga > 0.5 and 1700 <= a[di['age_CE']] <= 1850:
        print(f'  {a[di["age_CE"]]:.2f} ({a[di["depth_m"]]:.2f} m) -> {b[di["age_CE"]]:.2f} ({b[di["depth_m"]]:.2f} m): {ga:.2f} yr, {a[di["depth_m"]] - b[di["depth_m"]]:.2f} m')
UCCd = {'Bi': 0.16, 'Al': 81500, 'Fe': 39200}
print('\n--- Dasuopu: 12 largest samples by EFc(Bi) (median of Al- and Fe-referenced), 1700-1850 ---')
ds = []
for r in drows:
    age = r[di['age_CE']]; bi = r[di['Bi']]; al = r[di['Al']]; fe = r[di['Fe']]
    if bi is None or not (1700 <= age <= 1850): continue
    e = []
    if al: e.append((bi / al) / (UCCd['Bi'] / UCCd['Al']))
    if fe: e.append((bi / fe) / (UCCd['Bi'] / UCCd['Fe']))
    if e: ds.append((sum(e) / len(e), age, bi, al, fe))
for e, age, bi, al, fe in sorted(ds, reverse=True)[:12]:
    print(f'  {age:.2f}: EFc {e:6.1f}  Bi {bi:6.2f} pg/g  Al {al:8.0f}  Fe {fe:8.0f}')
lg = sorted(math.log10(e) for e, *_ in ds); med = lg[len(lg) // 2]
print(f'  Dasuopu EFc median 1700-1850: {10**med:.1f}')
print('\n--- Dasuopu samples 1808.5-1811.5 with EFc ---')
for e, age, bi, al, fe in ds:
    if 1808.5 <= age < 1811.5: print(f'  {age:.2f}: EFc {e:6.1f}  Bi {bi:6.2f}  Al {al:8.0f}  Fe {fe:8.0f}')
