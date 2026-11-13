---
ai-generated: true
author: Claude (Anthropic AI model)
model: not recorded
directed-by: William John Suk (project lead)
verified-by: none
verification: mixed (see the label on each item)
strand: science_alternatives
date: 2026-10-28
---

# Tibet and the Himalaya, 1808-10: what written records exist, and what the plateau's natural archives say

Thread "Read the Vietnamese court chronicle 1808-10", 28 Oct 2026, answering William's question "are there pertinent records from Tibet?". Register section B67. Verification levels as marked: [text] = read from a web page or abstract through the fetcher; [data] = numbers read from a NOAA data file; [memory] = Claude's unverified recollection; [calc] = Claude's calculation; [suggestion] = Claude's proposal. No page images were read for this note.

**Short answer.** Nothing from Tibet for 1808-10 has been read by this project, and nothing Tibetan for those years is reachable from here. The pertinent Tibetan material is of three kinds: (1) written records, which for 1808-10 are confined to Tibetan biographies and Qing amban papers, neither catalogued for weather; (2) two Himalayan ice cores at 28°N whose published volcanic records show Tambora but not 1809, and whose raw sub-annual sulfur and bismuth data have never been examined for 1809 (a Mac download and the script below would do it); (3) Tibetan tree rings, which show the 1810s as the coldest decade in 300-500 years but, in the papers read, do not separate 1809 from 1815.

## 1. What the project files already held

Only one Tibetan item: Moorcroft's twilight observation of 22 Aug 1812 from western Tibet in Stothers' list (notes/papers_downloaded_2026-10-22.md), after the window. The REACHES extract (data/reaches_1808-07_1810-06_2026-10-27.tsv, B60) has no rows for Tibet, Qinghai or Xinjiang; its Sichuan rows give the nearest gazetteer evidence: winter 1809/10 heavy snow at Pixian in the Chengdu plain (30.8°N) and snow with ice at Santai (Jan 1810), crop damage at several Sichuan sites 1809-10, hail and floods in summer 1808 [data, coded categories, already noted at B60 line 75].

## 2. Written records from Tibet for 1808-10

| Source | What it is | Covers 1808-10? | Status |
|---|---|---|---|
| Kashag (Tibetan government) archives on natural disasters | Published selections: *Rang byung gnod 'tshe gangs skyon skor* (1987) and *Bod kyi rang byung gnod 'tshe'i skor gyi lo rgyus yig tshags bdams sgrig* (2017), the latter covering 1824-1956 [text, Palden Gyal 2024] | No: the compilations begin with the snow disasters of 1824-1830 | not pertinent to the window |
| Qing amban memorials and the Qing Shilu, Jiaqing 13-15 | The ambans reported hail, snow, earthquakes, epidemics and famine relief in Tibet to Beijing; Qing palace memorials (First Historical Archives, Beijing; NPM Taipei) and the 8-volume *Qing dai Xizang difang dang'an wenxian xuanbian* (2017) [text, Palden Gyal 2024 for the source types] | Possibly | not searchable from here (ctext, Academia Sinica Shilu database blocked); U69 |
| Tibetan biographies (rnam thar) | The 9th Dalai Lama Lungtok Gyatso (1805-15, enthroned 1808, died March 1815) and the regent Demo Rinpoche (d. 1811) have biographies; namthar record omens (rainbows, earthquakes, sky signs) around enthronements and deaths [memory]; scans at BDRC | Yes in principle | needs a Tibetan reader; U129 |
| European visitors | Manning in Lhasa Dec 1811-Apr 1812; Moorcroft and Hearsey in western Tibet Jul-Sep 1812 [memory] | No, both after the window; no European was in Tibet in 1808-10 | not pertinent |
| Nepal (neighbour, 27°N) | Documenta Nepalica (Heidelberg) catalogues the Regmi Research Collection with English abstracts; it holds, for example, "an order to supply foodgrains from the Tarāī to famine-affected areas in eastern hills, VS 1873" (1816, the Tambora famine) [text]; VS 1865-1867 = 1808-10 not yet searched; Regmi Research Series PDFs at Digital Himalaya | Yes | form search needs a browser; U128 |

Chinese gazetteers for the Tibetan borderlands (Sichuan, Yunnan, Gansu) are in REACHES (section 1). The only Tibetan climate-history paper found for the period, Palden Gyal, "The sociopolitical impact of a natural disaster: the snow disaster of the Earth-Rat year (1828) in northwestern Tibet", *Climates and Cultures in History* 1 (2024), does not mention 1808-10 or Tambora [text].

## 3. Natural archives on the plateau

### 3.1 Ice cores at 28°N

| Core | Published volcanic record | 1809 | Raw data |
|---|---|---|---|
| East Rongbuk col, Everest NE ridge (28.03°N, 86.96°E, 6518 m; Kaspari, Mayewski, Hou, Kang, Qin) | Xu et al. 2009, *Chinese Science Bulletin* 54:1411: bismuth enrichment factor 1800-2002, nine events above mean + 2σ; Tambora 1815 the largest; Agung 1963 and Pinatubo 1991 the others used as horizons; 1845 (Tonga 1846?), 1911, 1919, 1953, 1967 the rest; Krakatau 1883 "not clearly captured"; recording efficiency 67 % [text] | not among the nine events: no Bi peak above 2σ for 1809-10 [text] | NOAA rongbuk2009.txt: sub-annual (about 0.03-0.05 yr) S, Bi, Tl and 24 other elements 1650-2002 (Kaspari et al. 2009 *JGR* 114:D04302), youngest first; the fetcher reads only the top 42,000 characters (1980-2002), so 1800-1825 could not be read here [data]. Kaspari 2009 never discusses 1809 [text]. |
| Dasuopu, Xixabangma (28.38°N, 85.72°E, 7200 m; Thompson, Gabrielli) | Gabrielli et al. 2020 *PNAS* 117:3967: 23 trace elements 1499-1992, annual to decadal, layer-counted, 1963 bomb horizon [text]; the paper (captcha-walled here) is about pollution, not eruptions | decadal crustal-enrichment factors for Bi [data, NOAA 10-yr EFc file]: 1790s 4.5, 1800s 4.3, 1810s 3.4, 1820s 4.5, 1830s 4.6: no decadal signal for either 1809 or Tambora, so only the full-resolution file can answer | NOAA dasuopu2020elem-noaa.txt: full-resolution Bi, Tl, Cd, Sb, Pb; the fetcher reaches only 1917-1992 [data] |
| East Rongbuk 5-year chemistry (Kaspari et al. 2007 *GRL*) | Ca, Cl, δD only | 1805-09 pentad: Ca 71 µg/L (lowest of 1800-25), δD −154.4 ‰ (most depleted of 1800-25) [data]; not a volcanic proxy | read |
| Puruogangri, central plateau (33.9°N, 89.1°E, 6070 m; Thompson et al. 2006) | 5-year means of sulfate, chloride, dust, δD | sulfate 1805-09 = 1092 ppb, the highest of 1790-1829, but dust (410,000) and calcium also peak, and 1815-19 sulfate (517) is below 1800-04 (857): dust-derived sulfate, not usable for eruptions [data] | read |

Reading [suggestion]: the Everest Bi record is the only published Himalayan test, and it is negative for 1809 at the 2σ level while positive for Tambora; since Krakatau 1883, of similar sulfur yield to 1809, is also absent, the absence does not discriminate. The sub-annual Everest sulfur series has never been examined for 1809. If the 1809 aerosol reached 28°N it should show as an excess-sulfate pulse in 1809-10 ice at Everest (Tambora's arrival there would calibrate the lag); a null at Everest with a clear Tambora would be a mild argument for a source whose plume stayed south, which is what the bipolar deposition split (B55) and the latitude band (B62) also suggest. This is a desk test: two NOAA files, the script below, an evening.

### 3.2 Tree rings

| Study | Region, proxy | 1809-10 | 1815-16 and the 1810s |
|---|---|---|---|
| Gao, Camarero, Babst & Liang 2023, *Nature Communications* 14:6616 | 3,304 ring-width chronologies worldwide, incl. the Institute of Tibetan Plateau Research collection | on the Tibetan Plateau the probability of evergreen-conifer growth below −2σ rose 804 % in 1809-24 relative to 1759-1808; resilience "decreased following the 1809 eruption and lasted until several years after the 1815 eruption"; Tibetan and Mongolian plateaus had the longest influence times, beyond 1824; year-by-year regional results only in figures [text] | combined with 1809 |
| Wang, Shao, Zhang & Li 2021, *Climate of the Past* 17:241 | Qilian juniper, Henan County, Qinghai (34.6°N, 3806 m), annual minimum temperature 1380-2014 | 1809 named only as "another stratospheric eruption"; 1781-1813 listed as warm [text] | −0.5 °C in 1816 [text] |
| Li, Huang, Yin & Shao, EGU 2017 | NW Yunnan spruce ring width + MXD, Jul-Oct Tmax, 304 years | not isolated | cold 1801-1833; 1810s one of the two coldest decades [text] |
| Huang, Bräuning, Grießinger et al. 2025, *Quaternary Science Reviews* 355:109266 | SE Tibetan Plateau MXD, Aug-Sep Tmin since 1246 | not isolated; cold 1806-1830 | eruption-year −0.33 °C, next year −0.37 °C (all tropical eruptions composited) [text] |

Reading [suggestion]: the plateau's trees record the 1810s cold decade clearly, but no paper read isolates the 1809-11 response from Tambora's. A superposed-epoch analysis keyed to 1809 alone on the ITRDB Tibetan chronologies would be a small job and is the kind of thing Timmreck 2021 (B58) used for the Northern Hemisphere as a whole.

## 4. Sources added to unavailable_sources.md this turn

- U127 (A): the two NOAA files (Everest rongbuk2009.txt, Dasuopu dasuopu2020elem-noaa.txt), needs Mac download; script ready (section 5).
- U128 (A): Documenta Nepalica catalogue search for VS 1865-1867 (famine, drought, hail, snow, "sun"), needs Safari (form search).
- U129 (A): the 9th Dalai Lama's and the regent's biographies at BDRC, needs Safari and a Tibetan reader (whom to ask is William's decision).
- U69 (B): Qing Shilu Jiaqing 13-15 and the *Qing dai Xizang difang dang'an wenxian xuanbian* (2017) for Tibetan disaster reports 1808-10, library.

## 5. For William: one paste-able block (zsh-safe) that writes the test script and runs it on the two downloaded files

Version 2 (28 Oct 2026, 04:50). Version 1 (04:25) is kept as scripts/tibet_icecores_2026-10-28/himalaya_1809_v1_superseded.py; it matched no Everest column because the names carry units ("Bi(ppt)", "S(ppb)") and it scaled z-scores on raw samples whose spread is dominated by dust spikes. Version 2 matches on the element symbol, forms ratios to crustal references (Al, Fe, Ca) to take the dust out, and uses robust log10 statistics on yearly values. Tested on mock files shaped like the real headers (two Everest tables, a NaN row, a Dasuopu year gap), not yet on the real files. The two NOAA files are already on William's Mac (data/icecore/himalaya, downloaded 28 Oct 00:41 Mac time), so this block does not download again.

```
cd ~/Documents/'1808-9 Volcano Project' 2>/dev/null || cd ~/Downloads/1808-9 Volcano Project/; mkdir -p scripts/tibet_icecores_2026-10-28 && cat > scripts/tibet_icecores_2026-10-28/himalaya_1809.py <<'PYEOF'
"""Himalayan ice cores: test for an 1809 volcanic signal. Version 2 (28 Oct 2026; v1 matched no Everest column
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
    return num(tok) is not None or tok.strip().lower() in MISSING

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
PYEOF
cd data/icecore/himalaya && python3 ../../../scripts/tibet_icecores_2026-10-28/himalaya_1809.py rongbuk2009.txt dasuopu2020elem-noaa.txt
```

What to send back: the whole printed output (about 160 lines). If a closer look is wanted, drag in himalaya_v2_samples_everest.csv (all Everest columns, 1790-1830, about 30 KB).

How to read it: the ratio columns (S/Ca, S/Al, Bi/Al, Tl/Al) in the "yearly MAXIMUM" table are the volcanic test. A year with ** in Bi/Al or S/Ca and no ** in Al is an aerosol arrival; a year with ** in everything is a dust year. 1816-17 must show the Tambora pulse for the test to mean anything; then 1809-10 is read the same way. Expected deposition lag after a late-1808 tropical eruption: a few months to a year, so the window is mid-1809 to 1810.

## 6. Files

- This note; scripts/tibet_icecores_2026-10-28/himalaya_1809.py (same script as in section 5).
- Pages read [text]: Xu et al. 2009 (core.ac.uk 217137378), Kaspari et al. 2009 JGR (core.ac.uk 217137304) and J. Climate (217137501), NOAA/data.gov dataset pages for East Rongbuk (study 11822) and Dasuopu (study 28510), NOAA Dasuopu 10-yr EFc file, NOAA Puruogangri file, NOAA East Rongbuk 5-yr file (paleo.ltrr mirror), Gao et al. 2023, Wang et al. 2021, Li et al. EGU2017-13583, Huang et al. 2025 (FAU record), Palden Gyal 2024, Gamble, Powers & Hackett 2022 (BSOAS 85:215, medieval famines, for the source types), Documenta Nepalica item RRC_0036_0282 and its search page, vietsu.org and archive.org for nothing Tibetan.

## 7. First run on William's Mac (28 Oct 2026, 00:41 Mac time; output pasted into the thread 04:41 UTC)

[text, from William's pasted terminal output]
- Both files downloaded by curl without trouble: rongbuk2009.txt 776,293 bytes; dasuopu2020elem-noaa.txt 315,067 bytes. U127 status changed to downloaded, not read.
- Everest file layout: at least two data tables of 2,280 rows each. Table 1 columns begin Year(AD), Depth(m), Sr(ppt), Cs(ppt), Ba(ppt), La(ppt), Ce(ppt), Pr(ppt), Nd(ppt), Sm(ppq), Eu(ppq), Gd(ppq) ...; table 2 begins YearAD, Depth(m), Tm(ppq), Yb(ppq), Lu(ppq), Bi(ppt), U(ppq), Tl(ppt), Al(ppb), S(ppb), Ca(ppb), Ti(ppt) ... So Bi, Tl, Al, S and Ca sit in the same table and the ratios can be formed sample by sample. 2,280 samples over 1650-2002 is about 6.5 per year.
- Dasuopu file layout: one table, 2,564 rows, columns depth_m, age_CE, Al, As, Ba, Bi, Cd, Co, Cr, Cs, Fe, Ga ... (the remaining elements were cut from the printout). About 7.4 samples per year in 1750-1800.
- Version 1 found no S, Bi or Tl column in the Everest file (unit suffixes) and printed nothing useful for it.
- Version 1 Dasuopu yearly medians (raw concentrations, usable as numbers although the z-scores are not): 1808 is the highest or second-highest year of 1801-1815 in all five elements printed (Bi 1.26, Tl 0.89, Cd 0.65, Sb 1.88, Pb 44.1), which is the signature of a dusty year, not of a volcanic input; 1809, 1810 and 1811 are among the lowest (Bi 0.09, 0.12, 0.08). 1829-30 Sb (35, 19 against a baseline of 0.7) and Cd stand out and are unexplained here. No sample carries a year of 1816: the printed years run 1815, 1817. Whether the age model skips 1816 or the year has no samples has to be checked in the file (the v2 script prints n per year).
- No matplotlib on the Mac; v2 writes CSV only.

## 8. Result of version 2.1 on the real files (28 Oct 2026, 04:57 UTC; William's pasted terminal output; register B68)

[text: William's pasted output of himalaya_1809.py v2.1; the readings below are Claude's]

Data as parsed: rongbuk2009.txt, two tables of 2,280 rows (ages 1650.0-2002.2); table 2 holds Bi, U, Tl, Al, S, Ca, Ti, Cr, Mn, Fe, Co; 2-9 samples per year in 1800-1830. dasuopu2020elem-noaa.txt, one table of 2,564 rows (1499.3-1992.3), 23 elements (Al As Ba Bi Cd Co Cr Cs Fe Ga Mg Mn Mo Nb Ni Pb Rb Sb Ti Tl U V Zn), no S; 2-16 samples per year; no sample dated 1816 at all. Baselines (yearly medians 1700-1800): Everest S 8.8 ppb, Bi 2.1 ppt, Tl 1.1 ppt, Al 36 ppb, Ca 80 ppb, Fe 54 ppb; Dasuopu (pg/g) Bi 0.41, Tl 0.25, Sb 0.70, Cd 0.36, Pb 12.9, As 10.2, Al 10,100, Fe 11,300.

Everest, key years (z of the yearly maximum unless stated; ** z >= 2.5):

| year | n | Bi raw | Bi/Al | Bi/Fe | S raw | S/Ca (median) | Al raw | reading |
|---|---|---|---|---|---|---|---|---|
| 1808 | 4 | +0.1 | -0.2 | -0.6 | +1.0 | +0.2 | +1.1 | nothing |
| 1809 | 5 | -1.0 | -0.8 | -1.2 | -0.3 | +1.5 | -0.6 | nothing; low-dust year |
| 1810 | 7 | -0.2 | +0.6 | +0.7 | +0.4 | +1.3 | -1.1 | nothing |
| 1811 | 6 | -0.3 | +0.3 | +0.4 | +0.1 | +0.4 | +0.2 | nothing |
| 1815 | 6 | +4.4** | +8.2** | +8.2** | +1.5 | +0.3 | +0.6 | Tambora: a Bi spike without dust; S silent |
| 1816 | 6 | -1.3 | +4.5** | +6.5** | -1.7 | -4.3 | -3.6 | cleanest year of the window (all medians far below baseline); ratio maxima come from one low-Al sample |
| 1817 | 3 | -0.2 | +0.2 | +0.3 | -0.3 | +0.8 | -1.0 | nothing |

Raw Bi maxima 1800-1830: only 1815 exceeds z +2 (+4.4); next 1819 +1.9, 1826 +1.9, 1822 +1.8. Ten largest years 1700-1850 by yearly maximum: Bi/Fe 1815 (+8.2), 1747, 1816 (+6.5), 1765, 1752, 1845, 1754, 1818, 1785, 1776; Bi/Al 1818, 1776, 1785, 1815, 1783, 1777, 1765, 1805, 1796, 1747. Neither 1809 nor 1810 appears in any list.

Artefact in the ratio maxima: identical values recur across years (Tl/Al +18.7 in 1782, 1783, 1805, 1816, 1818, 1825, 1829; Bi/Al +4.5 in 1816, 1825, 1829), which can only happen if the same replacement values (below detection) for Al, Bi and Tl sit in one sample of each of those years. Such samples inflate ratio maxima and leave raw maxima alone, so the raw Bi maximum is the primary test and the ratios the confirmation. 1815 passes both (raw +4.4, Bi/Al +8.2, Bi/Fe +8.2); 1805 and 1818 (Bi/Al +6.8, +9.5; raw Bi -0.6, -0.5) fail the raw test and are artefacts. [to verify in himalaya_v2_samples_everest.csv]

Dust years (every raw maximum up): Everest 1821 and 1826; Dasuopu 1804 and 1814. Everest S medians low in 1812 (-2.5), 1814 (-1.7), 1816 (-5.1), 1818 (-3.8), 1824 (-3.8), 1827 (-5.1).

Dasuopu, key years: 1815 max Bi +1.6, Bi/Al +1.9, Bi/Fe +4.1**, As/Al +2.6**; 1816 no samples; 1817 nothing. 1809 medians Bi -1.8, Al -1.6, Fe -1.9, Bi/Al +0.6, Bi/Fe +2.6**, Sb/Al +2.5**, Cd/Al +2.5**; 1809 maxima Bi -2.0 (lowest of the decade), Bi/Al +0.6, Bi/Fe +1.9, Tl/Al +2.0*; 1810 max Bi/Fe +3.1**; 1811 max Bi/Fe +3.0**, As/Al +6.2**. Reading: the flagged medians are ratios in years of very low dust (Al and Fe medians -1.1 to -2.5); the same pattern recurs in 1802-03 (Tl/Al, Sb/Al), 1806 (Sb/Al +2.9), 1818 (Sb/Al +3.1) and 1820-26 (Bi/Fe +2.2 to +3.9), so these metals have a background that is not tied to dust and every ratio rises whenever dust falls. Ten largest Bi/Al years 1700-1850: 1823, 1849, 1820, 1838, 1752, 1828, 1836, 1791, 1788, 1837: no 1809-11 and no 1815. Dasuopu is not a validated detector in this window (no 1816, no 1815 Bi spike), which agrees with the flat decadal Bi EFc of Gabrielli 2020. Script detail: the n column of the Dasuopu tables counts the Bi series only; 1830 shows n=0 because Bi is missing there while other elements have samples.

Reading (inference): Everest records Tambora as the one bismuth event of 1800-1830 and records nothing in 1809-10. With an 1809 stratospheric sulfur load of roughly two-thirds of Tambora's (eVolv2k) and a 55 % northern deposition share (B55), an aerosol of the Tambora kind with a similar Bi yield should have left a Bi spike of order +3 in 1809 or 1810. Its absence is a weak negative that does not locate the source. The B62 latitude band (12°S-3°N) was withdrawn at B66 (28 Oct): the hemispheric sulfate ratio says only "tropical", and B66 found that Oct-Feb tropical eruptions deposit about twice as Greenland-heavily as Mar-Jun ones, so the aerosol of a Nov-Dec 1808 eruption should if anything have reached 28°N well. The Everest null therefore more likely reflects the bismuth yield of the magma, the monsoon-season sampling of East Rongbuk, or the detector's miss rate (the same core missed Krakatau 1883; capture about two-thirds, Xu 2009) than the latitude of the source. [reworded 05:05 after the coordinator pointed to B66; the first wording leaned on the withdrawn band] The sulfur channel is blind at Everest (Tambora S max +1.5), so the mildly high S/Ca medians of 1809-10 (+1.5, +1.3) are inside the noise.

Open: (a) the identical-value artefact and the season of the 1815 spike, from himalaya_v2_samples_everest.csv (asked 28 Oct 05:10); (c) the 1816 gap at Dasuopu.

(b) resolved 05:15 [text, Xu et al. 2009 CSB 54:1411 read as fetched text from the UMaine open-access copy, core.ac.uk/download/217137378.pdf]: the East Rongbuk timescale was made by annual-layer counting of δD and soluble ions, "checked against large volcanic horizons", with Tambora, Agung and Pinatubo called "faithful horizons"; stated error ±0 yr at 1963 and ±5 yr at 1534 (98 m). So the 1815 Bi peak is partly built into the dating, and the Tambora "detection" is not an independent test of the detector. The other side of that coin helps the 1809 test: with the timescale pinned at the 1815 horizon, the 1809-10 layers lie only five or six counted layers away, so their dating error is at most a year, and since no other year of 1800-1830 has a raw Bi maximum above z +2, no misdated 1809 spike is hiding in a neighbouring year. Xu 2009 also states the detection rule (Bi enrichment factor above mean + 2σ), nine events since 1800, Krakatau 1883 "not captured" and blamed on circulation and accumulation, and a 67 % recording efficiency reckoned on the seasons likely to be recorded (eruptions in December-April and late May-September are expected to be recorded, so a Nov-Dec 1808 eruption falls in the recordable class). Xu's nine Bi events since 1800 are 1815 Tambora, 1845 (assigned to the June 1846 Tonga eruption, 18°S), 1911 (Novarupta 1912), 1919 (Kelut), 1921 (unassigned), 1953 (Kelut 1951), 1963 Agung, 1967 (unassigned; Taal or Awu), 1991 Pinatubo: no 1809 or 1810 peak in the published list, and the 1845 peak also appears in this run (Bi/Fe maximum +5.1, sixth of 1700-1850), which cross-checks the scoring. The 1846 Tonga assignment, if right, shows the core can record a southern-tropics eruption. EFc definition in Xu 2009: median of Bi/x in ice over Bi/x in upper crust for x = Sr, Ca, La, Fe, Al; this run used Al and Fe singly.

## 9. Close reading of the raw files (28 Oct 2026, 05:14-05:25 UTC; William uploaded rongbuk2009.txt and dasuopu2020elem-noaa.txt to the thread; scripts/tibet_icecores_2026-10-28/everest_close.py and himalaya_fig.py; data/everest_samples_1795-1830_efc_2026-10-28.csv; figure data/himalaya_bismuth_1795-1830_2026-10-28.png)

[data: both NOAA files read in full in Claude's cloud container; every number below is Claude's calculation]

File facts. The Everest file is space-delimited, two tables of 2,280 samples with identical ages (joined row by row): Sr Cs Ba La Ce Pr Nd Sm Eu Gd Tb Dy Ho Er, then Tm Yb Lu Bi U Tl Al S Ca Ti Cr Mn Fe Co; missing rows are -999. Below-detection replacement values show as repeated column minima: Bi 0.02 ppt (41 samples), Tl 0.02 ppt (95), Al 0.02 ppb (80), S 0.15 ppb (172), U 3.0 ppq (69), Ca 0.06 ppb (21), Co 0.21 (40), Lu 2.5, Tm 1.0, Eu 1.5, Gd 1.5, Ba 0.17, Cr 0.07. These were set to missing before any ratio was formed; the identical ratio maxima of section 8 (Tl/Al +18.7 and so on) are exactly these samples and are discarded. The Dasuopu file is in pg/g with "thermal year" ages, dated by layer counting of δ18O, dust and nitrate confirmed by the 1963 beta horizon at 42.2 m (file header, text).

Enrichment factor, Xu style: EFc(Bi) = median over x in {Sr, Ca, La, Fe, Al} of (Bi/x)ice / (Bi/x)UCC, upper-crust values of Rudnick & Gao 2003 (Bi 0.16, Sr 320, La 31 ppm; Ca 2.57, Fe 3.92, Al 8.15 %). Median EFc of all 2,280 samples 20.1; Xu's rule (mean + 2 sd) gives a threshold of 371 on this series, a robust rule (median + 3 MAD in log10) 203.

| year | n | max Bi (ppt) | max EFc | max excess S (ppb) |
|---|---|---|---|---|
| 1808 | 4 | 4.5 | 18.9 | 25.6 |
| 1809 | 5 | 1.9 | 9.5 | 7.4 |
| 1810 | 7 | 3.5 | 27.1 | 16.0 |
| 1811 | 6 | 3.3 | 37.8 | 7.8 |
| 1815 | 6 | 196.7 | 3,882 | 28.7 |
| 1816 | 6 | 1.3 | 36.5 | -1.8 |
| 1817 | 3 | 3.6 | 28.3 | 6.9 |
| 1819 | 6 | 21.4 | 50.0 | 0.7 |
| 1821 | 9 | 23.1 | 57.5 | 44.1 |
| 1822 | 7 | 20.8 | 56.6 | 3.0 |
| 1826 | 5 | 22.1 | 28.2 | 18.4 |

Tambora. One sample at 1815.71 (65.09 m): Bi 196.69 ppt with Tl 0.79, Al 25.8, Fe 38.2, Ca 16.5 and S below detection; EFc 3,882, seven times the next-largest enrichment of 1700-1850 (1747, 551) and 190 times the median. It sits 71 % through the 1815 layer, about five months after the 10 April eruption if the layer begins near 1 January, the same lag as the Greenland arrival. The adjacent samples (1815.55 Bi 2.77, 1815.86 Bi 0.78) are at baseline, so the fallout was one event of under two months. Raw Bi yearly maxima 1700-1850 in order: 1776 (739 ppt), 1754 (273), 1815 (197), 1777 (184), 1752 (106), 1747 (81), 1845 (35), 1850 (30), 1778 (29), 1753 (26), 1821 (23), 1826 (22), 1819 (21), 1719 (21), 1822 (21). The 1747-1777 giants (EFc 270-550) are outside Xu 2009's post-1800 scope and unexplained here [side mystery, not pursued].

1809-10. Twelve samples from 1809.09 to 1810.91 (sixteen from 1808.20 to 1811.40, which covers any dating slack): Bi 0.13-4.52 ppt, EFc 1.7-27 (the 1809 maximum, 9.5, is below the series median), excess S from -5.6 to +25.6 ppb (1808.65, a dusty sample) against top-ten years of 28-44. The sample at 1809.48, where a Nov-Dec 1808 aerosol would land on the Tambora lag, has Bi 0.17 ppt and EFc 1.7. Nothing.

Reproduction of Xu 2009. The mean + 2 sd rule on this series flags 1747, 1765, 1776, 1815, 1911, 1943, 1945, 1949, 1953, 1963, 1967, 1974, 1990, 1991, 2001; the robust rule adds 1728, 1752, 1754, 1777, 1845, 1919, 1947, 1956, 2002. Eight of Xu's nine post-1800 events come out (1815, 1845, 1911, 1919, 1953, 1963, 1967, 1991; 1921 does not), so the published detector is reproduced from the file, and 1809-10 are a factor of ten or more below either threshold.

Expected 1809 signal [calc]. Scaling the Tambora sample by the Greenland 1809/1815 sulfate ratio (about 0.6-0.7, Sigl 2015 / eVolv2k) gives about 130 ppt; a tenth of that (20 ppt) would still rank among the seven largest yearly maxima of 1700-1850. Neither is there.

Excess S (S minus 0.100 × Ca, the median sample S/Ca of 1700-1800). The Tambora Bi sample has no measurable S at all; the 1815 excess-S maximum (28.7 at 1815.39) is a dusty sample (Ca 289 ppb) ranking eighth of 1700-1850 behind 1821 (44), 1751, 1777, 1706, 1710, 1828 and 1834. Sulfur at Everest is blind to Tambora: confirmed.

Dasuopu. Sampling is continuous from 1795.91 to 1815.80 (7-11 samples a year, no gap over half a year), then a gap from 1815.80 (114.25 m) to 1817.01 (113.94 m): 0.31 m and 1.21 years with no samples, which removes the Tambora arrival year. Other gaps: 1772.30-1773.40, 1780.33-1781.58, 1794.86-1795.91, 1822.16-1823.56 (1.40 yr), 1843.43-1845.55 (2.12 yr). EFc(Bi) (mean of Al- and Fe-referenced) has a 1700-1850 median of 18.6; the 1809-11 samples run 8-66 (the 66 at 1810.99 is a low-dust sample with Al 1,136 pg/g), so nothing. The largest Dasuopu enrichment of 1700-1850 is at 1823.62: Bi 48.4 pg/g with ordinary dust (Al 12,445), EFc 1,383, ten months after Galunggung (8-12 Oct 1822, 7°S, VEI 5) [suggestion, not checked against eVolv2k or Gabrielli 2020; Everest 1822-23 shows only Bi 20.8 ppt, EFc 57]. If that attribution holds, Dasuopu can record a Java eruption and its 1809-11 silence is a second null at 28°N; without 1816 samples it stays unvalidated for Tambora.

Reading: as in section 8 after the rewording. The Everest null is now as firm as this core can make it (no spike in any sample 1808.2-1811.4, continuous sampling, dating pinned within a year by the 1815 horizon, the published detector reproduced), it does not locate the source, and it weighs against an aerosol that delivered Tambora-like bismuth to 28°N in 1809-10. Open from these files: the Galunggung attribution at Dasuopu and the 1747-1777 Everest giants, neither needed for the 1808/09 question.
