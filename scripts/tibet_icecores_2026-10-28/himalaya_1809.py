"""Himalayan ice cores: test for an 1809 volcanic signal. Version 2.1 (28 Oct 2026, 04:55, -999.00 rows no longer mistaken for headers; v1 matched no Everest column
because the names carry units, and scaled z-scores on dust-spiked raw samples).

Reads NOAA template text files: lines starting with '#' are comments; one or more tab-separated data tables,
each with its own header line. Tested layouts:
  Everest East Rongbuk  rongbuk2009.txt          (Kaspari et al. 2009; sub-annual 1650-2002; S, Bi, Tl, Al, Ca, ...)
  Dasuopu               dasuopu2020elem-noaa.txt  (Gabrielli et al. 2020; sub-annual; Bi, Tl, Sb, Cd, Pb, Al, Fe, ...)
Column names may carry units, e.g. "Bi(ppt)"; they are matched on the symbol only.

For each marker the script takes the yearly MEDIAN and yearly MAXIMUM of (a) the raw concentration and
(b) the ratio to a crustal reference (Al, Fe or Ca). The ratio removes the dust that dominates these cores:
a volcanic input raises Bi, S and Tl without raising Al, a dust year raises everything.
Robust z: log10 of the yearly value against the median and MAD (x1.4826) of the same yearly statistic over the
baseline years 1700-1800 (yearly values, not samples). ** marks z >= 2.5, * marks z >= 2.0.
Prints 1800-1830 for both statistics, sample counts (a gap shows as n=0), and the ten largest years 1700-1850
of each ratio. Writes himalaya_v2_yearly.csv (every year, every series) and himalaya_v2_samples_<core>.csv
(all columns, 1790-1830) for a closer look.
Usage: python3 himalaya_1809.py rongbuk2009.txt dasuopu2020elem-noaa.txt
"""
import sys, re, math, csv
from collections import defaultdict

MISSING = {'nan', 'na', 'n/a', '-999', '-999.0', '-999.9', '-9999', ''}

def num(tok):
    try:
        v = float(tok)
    except ValueError:
        return None
    if math.isnan(v) or v <= -900:
        return None
    return v

def looks_numeric(tok):
    try:
        float(tok)
        return True
    except ValueError:
        return tok.strip().lower() in MISSING

def clean(tok):
    return re.sub(r'\(.*?\)', '', tok).replace(' ', '').strip()

def unit_of(raw):
    m = re.search(r'\((.*?)\)', raw)
    return m.group(1) if m else ''

def is_age(name):
    n = name.lower()
    return n.startswith('year') or n.startswith('age')

def parse(path):
    tables, cur = [], None
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            s = line.rstrip('\r\n')
            if s.startswith('#') or s.strip() == '':
                continue
            toks = [t.strip() for t in (s.split('\t') if '\t' in s else s.split())]
            if sum(0 if looks_numeric(t) else 1 for t in toks) > len(toks) // 2:
                cur = {'raw': toks, 'cols': [clean(t) for t in toks], 'rows': []}
                tables.append(cur)
            elif cur is not None:
                vals = [num(t) for t in toks]
                vals += [None] * (len(cur['cols']) - len(vals))
                cur['rows'].append(vals[:len(cur['cols'])])
    return [t for t in tables if len(t['rows']) > 0]

def series(tables, name):
    for t in tables:
        low = [c.lower() for c in t['cols']]
        if name.lower() in low:
            j = low.index(name.lower())
            ages = [i for i, c in enumerate(t['cols']) if is_age(c)]
            if len(ages) == 0:
                continue
            ai = ages[0]
            out = [(r[ai], r[j]) for r in t['rows'] if r[ai] is not None and r[j] is not None]
            return out, t['raw'][j]
    return None, None

def ratio(tables, name, ref):
    sa, ua = series(tables, name)
    sb, ub = series(tables, ref)
    if sa is None or sb is None:
        return None, None
    d = {}
    for age, v in sb:
        d.setdefault(round(age, 3), v)
    out = []
    for age, v in sa:
        w = d.get(round(age, 3))
        if w is not None and w > 0:
            out.append((age, v / w))
    if len(out) < 0.5 * len(sa) and len(sa) == len(sb):
        out = [(a1, v / w) for (a1, v), (a2, w) in zip(sa, sb) if w > 0]
    return out, ua.split('(')[0] + '/' + ub.split('(')[0]

def median(v):
    s = sorted(v)
    n = len(s)
    if n == 0:
        return None
    return s[n // 2] if n % 2 == 1 else 0.5 * (s[n // 2 - 1] + s[n // 2])

def yearly(pairs):
    by = defaultdict(list)
    for age, v in pairs:
        by[int(math.floor(age))].append(v)
    return {y: (len(v), median(v), max(v)) for y, v in sorted(by.items())}

def robust(vals):
    logs = [math.log10(v) for v in vals if v is not None and v > 0]
    if len(logs) < 10:
        return None, None
    m = median(logs)
    mad = max(median([abs(x - m) for x in logs]) * 1.4826, 0.05)   # floor 0.05 dex so a flat baseline cannot inflate z
    return m, mad

def zscore(v, m, mad):
    if v is None or v <= 0 or m is None or mad is None or mad == 0:
        return None
    return (math.log10(v) - m) / mad

def fmt(zv):
    if zv is None:
        return '   .  '
    flag = '**' if zv >= 2.5 else ('* ' if zv >= 2.0 else '  ')
    return f'{zv:+5.1f}{flag}'

def report(core, path, tables, raw_names, ratio_pairs, out_rows, y0=1800, y1=1830):
    allages = [r[i] for t in tables for i, c in enumerate(t['cols']) if is_age(c) for r in t['rows'] if r[i] is not None]
    print(f'\n== {core} ({path}): {len(tables)} table(s), ages {min(allages):.1f}-{max(allages):.1f}')
    for t in tables:
        print('   columns:', ' '.join(t['raw']), f'[{len(t["rows"])} rows]')
    ser = []
    for n in raw_names:
        s, u = series(tables, n)
        if s is None:
            print(f'   no column {n}')
        else:
            ser.append((n, u, s))
    for a, b in ratio_pairs:
        s, u = ratio(tables, a, b)
        if s is not None:
            ser.append((a + '/' + b, u, s))
    stats = []
    for name, unit, s in ser:
        yr = yearly(s)
        base_years = [y for y in yr if 1700 <= y <= 1800]
        if len(base_years) < 30:
            base_years = [y for y in yr if y <= 1800]
        if len(base_years) == 0:
            print(f'   {name}: no baseline years, skipped')
            continue
        mm, madm = robust([yr[y][1] for y in base_years])
        mx, madx = robust([yr[y][2] for y in base_years])
        stats.append((name, unit, yr, (mm, madm), (mx, madx), base_years))
        for y, (n, med, mxv) in yr.items():
            out_rows.append([core, name, unit, y, n, med, mxv, zscore(med, mm, madm), zscore(mxv, mx, madx)])
    if len(stats) == 0:
        return
    names = [s[0] for s in stats]
    print('   baseline medians (of yearly medians) and spread (MAD, log10 units): ' + '; '.join(
        f'{st[0]} {10 ** st[3][0]:.3g} {unit_of(st[1])} +-{st[3][1]:.2f}dex' for st in stats if st[3][0] is not None))
    print(f'   baseline years: {min(stats[0][5])}-{max(stats[0][5])} ({len(stats[0][5])} yrs). z = robust z of log10 yearly value; ** z>=2.5, * z>=2.0')
    for which, idx, label in ((3, 1, 'yearly MEDIAN'), (4, 2, 'yearly MAXIMUM')):
        print(f'   --- z of {label} ---')
        print('   year   n | ' + ' '.join(f'{n:>7}' for n in names))
        for y in range(y0, y1 + 1):
            n = stats[0][2].get(y, (0, None, None))[0]
            cells = []
            for st in stats:
                yv = st[2].get(y)
                m, mad = st[which]
                cells.append(fmt(zscore(yv[idx], m, mad)) if yv else '   .   ')
            mark = ' <- 1809' if y == 1809 else (' <- Tambora' if y == 1816 else '')
            print(f'   {y}  {n:2d} | ' + ' '.join(f'{c:>7}' for c in cells) + mark)
    print('   --- ten largest years 1700-1850 by yearly MAXIMUM (z) ---')
    for st in stats:
        if '/' not in st[0]:
            continue
        m, mad = st[4]
        top = sorted(((zscore(v[2], m, mad) or -99, y) for y, v in st[2].items() if 1700 <= y <= 1850), reverse=True)[:10]
        print(f'   {st[0]:>6}: ' + '  '.join(f'{y}({zv:+.1f})' for zv, y in top))

def dump_samples(core, tables, y0=1790, y1=1831):
    merged, order = {}, []
    for t in tables:
        ages = [i for i, c in enumerate(t['cols']) if is_age(c)]
        if len(ages) == 0:
            continue
        ai = ages[0]
        for c in t['raw']:
            if c not in order:
                order.append(c)
        for r in t['rows']:
            if r[ai] is None or r[ai] < y0 or r[ai] >= y1:
                continue
            d = merged.setdefault(round(r[ai], 4), {})
            for c, v in zip(t['raw'], r):
                d[c] = v
    fn = f'himalaya_v2_samples_{core.split()[0].lower()}.csv'
    with open(fn, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['age_key'] + order)
        for k in sorted(merged):
            w.writerow([k] + [merged[k].get(c, '') for c in order])
    print(f'   wrote {fn} ({len(merged)} samples {y0}-{y1 - 1})')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    out_rows = []
    for path in sys.argv[1:]:
        tables = parse(path)
        if 'rongbuk' in path.lower() or 'everest' in path.lower():
            core = 'Everest East Rongbuk 28.0N 6518 m'
            raw = ['S', 'Bi', 'Tl', 'Al', 'Ca', 'Fe']
            pairs = [('S', 'Ca'), ('S', 'Al'), ('Bi', 'Al'), ('Tl', 'Al'), ('Bi', 'Fe')]
        else:
            core = 'Dasuopu 28.4N 7200 m'
            raw = ['S', 'Bi', 'Tl', 'Sb', 'Cd', 'Pb', 'As', 'Al', 'Fe']
            pairs = [('S', 'Al'), ('Bi', 'Al'), ('Bi', 'Fe'), ('Tl', 'Al'), ('Sb', 'Al'), ('Cd', 'Al'), ('As', 'Al')]
        report(core, path, tables, raw, pairs, out_rows)
        dump_samples(core, tables)
    with open('himalaya_v2_yearly.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['core', 'series', 'unit', 'year', 'n', 'median', 'max', 'z_median', 'z_max'])
        for r in out_rows:
            w.writerow(['' if v is None else v for v in r])
    print('\nwrote himalaya_v2_yearly.csv')
