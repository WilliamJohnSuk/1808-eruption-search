"""Coral footprint of 1809-1812: anomalies for every PAGES2k v2 coral record covering 1809-1812.
Input: pages2kv2.json (fzhu2e/cfr-data mirror of the NOAA PAGES2k 2017 dataset).
Output: CSV with yearly anomalies 1800-1820 (sd units), 1809-12 and 1815-18 means, percentile of the 1809-12 window.
"""
import json, sys, math, csv, statistics as st
from collections import defaultdict
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src)); cols = list(d.keys()); idx = list(d[cols[0]].keys())
recs = [{c: d[c][i] for c in cols} for i in idx]
def fl(x):
    try: return float(x)
    except: return float('nan')
SIGN = {'d18O': 1, 'Sr_Ca': 1, 'temperature': -1, 'calcification': None}
def make_month(times):
    """Month index 0-11 for a record's time stamps (corrected 27 Nov 2026, from the ChatGPT handoff).
    Records stored on a start-of-month grid with two-decimal dates (e.g. 1808.83 = November) are
    binned to the nearest month; floor() put 1808.83 in October and 1809.08 in January. Records on
    mid-month or irregular grids keep the original floor rule."""
    fr = [(a*12) % 1 for a in times]
    if fr and all(min(f, 1-f) < 0.1 for f in fr):
        return lambda a: int(round(a*12)) % 12
    return lambda a: min(11, int(math.floor((a - math.floor(a))*12 + 1e-9)))
rows = []; yearly_out = {}; monthly_keep = {}
for r in recs:
    if 'coral' not in str(r.get('archiveType','')).lower(): continue
    t = [fl(x) for x in r['year']]; v = [fl(x) for x in r['paleoData_values']]
    pts = [(a,b) for a,b in zip(t,v) if not (math.isnan(a) or math.isnan(b))]
    if not pts: continue
    pts.sort(); ts=[p[0] for p in pts]
    if min(ts) > 1812 or max(ts) < 1809: continue
    # any data in 1806-1816?
    if not any(1806 <= a < 1817 for a,b in pts): continue
    name = r['dataSetName']; var = r['paleoData_variableName']
    early=[x for x in ts if x < 1900] or ts
    gaps = [early[i+1]-early[i] for i in range(len(early)-1)]
    med = st.median(gaps)   # spacing before 1900, so a record that is 5-yr early and annual late counts as 5-yr
    sub = med < 0.9
    # yearly series of anomalies in sd units
    if sub:
        # monthly climatology 1790-1830 by calendar month
        by_m = defaultdict(list)
        month = make_month(ts)
        for a,b in pts:
            if 1790 <= a < 1831: by_m[month(a)].append(b)
        base_lo, base_hi = 1790, 1831
        if sum(len(x) for x in by_m.values()) < 25*6:
            # fall back: first 50 years of the record
            base_lo = math.floor(min(ts)); base_hi = base_lo + 50; by_m = defaultdict(list)
            for a,b in pts:
                if base_lo <= a < base_hi: by_m[month(a)].append(b)
        clim = {m: st.mean(x) for m,x in by_m.items() if len(x) >= 5}
        anoms_base = [b - clim[month(a)] for a,b in pts if base_lo <= a < base_hi and month(a) in clim]
        sd = st.pstdev(anoms_base)
        z = {a: (b - clim[month(a)])/sd for a,b in pts if month(a) in clim}
        # July-June years
        jj = defaultdict(list)
        for a,zz in z.items():
            m = month(a); y = math.floor(a)
            yy = y if m >= 6 else y-1   # months Jul(6)-Dec -> year y; Jan-Jun -> y-1
            jj[yy].append(zz)
        yearly = {y: st.mean(x) for y,x in jj.items() if len(x) >= 6}
        res = 'monthly; Jul-Jun means'
        monthly_keep[name+'|'+var] = (z, month)
    else:
        base = [b for a,b in pts if 1790 <= a < 1831]
        base_lo, base_hi = 1790, 1831
        if len(base) < 25:
            base_lo = math.floor(min(ts)); base_hi = base_lo + 50
            base = [b for a,b in pts if base_lo <= a < base_hi]
        mu, sd = st.mean(base), st.pstdev(base)
        yearly = {}
        for a,b in pts:
            yearly[int(math.floor(a+1e-6))] = (b-mu)/sd
        res = 'annual' if med < 1.5 else f'{med:.0f}-yr' + (' blocks before 1940, annual after' if 'Wei' in name else '')
    sign = SIGN.get(var)
    def win(y0,y1):
        xs=[yearly[y] for y in range(y0,y1+1) if y in yearly]
        return st.mean(xs) if xs else float('nan')
    m0912, m1518, m0608 = win(1809,1812), win(1815,1818), win(1806,1808)
    # percentile of 1809-12 window among all 4-yr windows (cool/dry positive)
    ys = sorted(yearly); allw=[]
    for y in ys:
        xs=[yearly[k] for k in range(y,y+4) if k in yearly]
        if len(xs)==4: allw.append(st.mean(xs))
    pct = float('nan')
    if sign is not None and not math.isnan(m0912) and allw:
        val = m0912*sign
        pct = 100.0*sum(1 for w in allw if w*sign >= val)/len(allw)   # % of windows at least this cool/dry
    rows.append(dict(record=name, pages2k_id=r['paleoData_pages2kID'], lat=r['geo_meanLat'], lon=r['geo_meanLon'], variable=var, units=r.get('paleoData_units'), resolution=res,
        record_span=f"{min(ts):.0f}-{max(ts):.0f}", baseline=f"{base_lo}-{base_hi-1}", cool_dry_sign=sign if sign is not None else '',
        mean_1806_08=round(m0608,2), mean_1809_12=round(m0912,2), mean_1815_18=round(m1518,2),
        pct_windows_as_cool_dry=round(pct,1) if not math.isnan(pct) else '',
        **{f'anom_{y}': (round(yearly[y],2) if y in yearly else '') for y in range(1800,1821)}))
    yearly_out[name+'|'+var] = yearly
rows.sort(key=lambda x: (x['lon'], x['lat']))
with open(out,'w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), 'records written')
for x in rows: print(f"{x['record'][:40]:40s} {x['variable']:13s} {x['lat']:7.2f} {x['lon']:8.2f} {x['resolution'][:7]:7s} base {x['baseline']} 06-08 {x['mean_1806_08']:5} 09-12 {x['mean_1809_12']:5} 15-18 {x['mean_1815_18']:5} pct {x['pct_windows_as_cool_dry']}")
json.dump({k:{str(y):v for y,v in yy.items()} for k,yy in yearly_out.items()}, open(out.replace('.csv','_yearly.json'),'w'))
# Lombok monthly detail
for key,(z,month) in monthly_keep.items():
    if 'Lombok' in key:
        print('\nLombok monthly z, 1807.5-1813.5:')
        for a in sorted(z):
            if 1807.5 <= a < 1813.6: print(f"  {a:.3f} m{month(a)+1:02d} {z[a]:+.2f}")
        top = sorted(z.items(), key=lambda kv: -kv[1])[:15]
        print(' top 15 months:', [(round(a,2), round(zz,2)) for a,zz in top])
        n_in = sum(1 for a,zz in top[:12] if 1810 <= a < 1813); print(' of top 12, in 1810-12:', n_in)
        print(' Dec 1808 rank among 1790-1830 months:', 1+sum(1 for a,zz in z.items() if 1790<=a<1831 and zz > z[[a for a in z if abs(a-1808.917)<0.05][0]]))
json.dump({k:{f"{a:.4f}":round(v,3) for a,v in z.items() if 1800<=a<1821} for k,(z,m) in monthly_keep.items()}, open(out.replace('.csv','_monthly_1800-1820.json'),'w'))
