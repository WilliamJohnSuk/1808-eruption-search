"""T12 (2 Nov 2026): pre-registered trace-element ratio lookup for the 1809 candidates.
Reads the GEOROC precompiled arc files (Sept 2026 download, on the Mac in data/georoc/),
selects each candidate's samples, keeps intermediate compositions (SiO2 55-68 wt%, as the
1809 ice glass is c. 59-65 wt%), and reports median and 25-75 % range of incompatible-element
ratios. Writes trace_ratio_lookup_2026-11-02.csv and trace_ratio_separation_2026-11-02.csv.
Run from data/georoc/:  python3 trace_ratios.py"""
import pandas as pd, numpy as np, glob, itertools
G = {  # candidate group: (file key, LOCATION regex)
 'Dakataua/Makalia (Willaumez, New Britain)': ('BISMARCK', r'DAKATAUA|MAKALIA|TALASEA'),
 'Witori/Pago (New Britain)': ('BISMARCK', r'WITORI|PAGO'),
 'Ulawun/Lolobau (New Britain)': ('BISMARCK', r'ULAWUN|LOLOBAU'),
 'Garove (Witu)': ('BISMARCK', r'GAROVE'),
 'Gaua (Vanuatu)': ('NEW_HEBRIDES', r'GAUA|SANTA MARIA'),
 'Ambrym (Vanuatu)': ('NEW_HEBRIDES', r'AMBRYM'),
 'Ambae/Aoba (Vanuatu)': ('NEW_HEBRIDES', r'AOBA|AMBAE'),
 'Kuwae/Tongoa/Epi (Vanuatu)': ('NEW_HEBRIDES', r'TONGOA|EPI|KUWAE'),
 'Tanna/Yasur (Vanuatu)': ('NEW_HEBRIDES', r'TANNA|YASUR'),
 'Leyte (Cabalian area)': ('LUZON', r'LEYTE'),
 'Camiguin/Hibok-Hibok (N Mindanao)': ('LUZON', r'CAMIGUIN|HIBOK|BUTAY|MAMBAJAO|GINSILIBAN|VULCAN'),
 'Dukono/Todoko (Halmahera)': ('HALMAHERA', r'DUKONO|TODOK'),
 'Ibu/Gamkonora (Halmahera)': ('HALMAHERA', r'IBU|GAMKONORA'),
 'Nila/Teon/Serua (Banda)': ('BANDA', r'NILA|TEUN|TEON|SERUA|SERAWERNA'),
 'N Sulawesi (Lokon, Soputan, Mahawu, Klabat, Tongkoko)': ('SULAWESI', r'LOKON|SOPUTAN|MAHAWU|KLABAT|TONGKOKO|MANADO'),
 'Savo (Solomons)': ('SOLOMON', r'SAVO'),
 'Bagana (Bougainville)': ('SOLOMON', r'BAGANA'),
}
E = ['RB','SR','Y','ZR','NB','CS','BA','LA','CE','ND','SM','YB','HF','TA','PB','TH','U']
R = {'Zr/Nb':('ZR','NB'),'La/Nb':('LA','NB'),'Th/Nb':('TH','NB'),'Ba/La':('BA','LA'),'Th/La':('TH','LA'),
     'La/Yb':('LA','YB'),'Ba/Th':('BA','TH'),'Zr/Hf':('ZR','HF'),'Nb/Ta':('NB','TA'),'Rb/Cs':('RB','CS'),
     'Ce/Pb':('CE','PB'),'U/Th':('U','TH'),'Sr/Y':('SR','Y'),'Zr/Y':('ZR','Y')}
files = {k: f for f in glob.glob('GEOROC_2026-09_*.csv') for k in ['BISMARCK','NEW_HEBRIDES','LUZON','HALMAHERA','BANDA','SULAWESI','SOLOMON'] if k in f}
cache = {}
rows, samp = [], {}
for g, (fk, rx) in G.items():
    if fk not in cache: cache[fk] = pd.read_csv(files[fk], encoding='latin-1', low_memory=False)
    d = cache[fk]; m = d['LOCATION'].astype(str).str.upper().str.contains(rx)
    s = d[m].copy(); si = pd.to_numeric(s['SIO2(WT%)'], errors='coerce')
    num = {e: pd.to_numeric(s.get(e+'(PPM)'), errors='coerce') for e in E}
    inter = (si >= 55) & (si <= 68); used = 'SiO2 55-68'
    if inter.sum() < 3: inter = si.notna() | si.isna(); used = 'all SiO2 (fewer than 3 intermediate samples)'
    rec = {'group': g, 'n_samples': int(m.sum()), 'selection': used, 'n_selected': int(inter.sum()),
           'SiO2_median': round(si[inter].median(), 1) if si[inter].notna().any() else np.nan}
    samp[g] = {}
    for rn, (a, b) in R.items():
        v = (num[a] / num[b])[inter].replace([np.inf, -np.inf], np.nan).dropna(); v = v[v > 0]
        samp[g][rn] = v
        rec[rn+'_n'] = len(v)
        rec[rn+'_med'] = round(v.median(), 2) if len(v) else np.nan
        rec[rn+'_p25'] = round(v.quantile(.25), 2) if len(v) >= 3 else np.nan
        rec[rn+'_p75'] = round(v.quantile(.75), 2) if len(v) >= 3 else np.nan
    rows.append(rec)
L = pd.DataFrame(rows); L.to_csv('trace_ratio_lookup_2026-11-02.csv', index=False)
# pairwise separation among the priority candidates: ratios whose 25-75 % ranges do not overlap (n>=3 each)
P = ['Dakataua/Makalia (Willaumez, New Britain)', 'Gaua (Vanuatu)', 'Leyte (Cabalian area)', 'Dukono/Todoko (Halmahera)',
     'Nila/Teon/Serua (Banda)', 'N Sulawesi (Lokon, Soputan, Mahawu, Klabat, Tongkoko)', 'Ambrym (Vanuatu)', 'Kuwae/Tongoa/Epi (Vanuatu)', 'Tanna/Yasur (Vanuatu)']
out = []
for a, b in itertools.combinations(P, 2):
    sep = []
    for rn in R:
        x, y = samp[a][rn], samp[b][rn]
        if len(x) >= 3 and len(y) >= 3:
            xa, xb, ya, yb = x.quantile(.25), x.quantile(.75), y.quantile(.25), y.quantile(.75)
            if xb < ya or yb < xa:
                sep.append('%s (%.1f vs %.1f)' % (rn, x.median(), y.median()))
    out.append({'a': a, 'b': b, 'separating_ratios_IQR_no_overlap': '; '.join(sep) if sep else 'none (or too few data)'})
pd.DataFrame(out).to_csv('trace_ratio_separation_2026-11-02.csv', index=False)
pd.set_option('display.width', 250)
print(L[['group','n_samples','n_selected','SiO2_median'] + [r+'_med' for r in ['Zr/Nb','La/Nb','Th/Nb','Ba/La','Th/La','La/Yb','Sr/Y','Nb/Ta']]].to_string())
print(pd.DataFrame(out).to_string())
