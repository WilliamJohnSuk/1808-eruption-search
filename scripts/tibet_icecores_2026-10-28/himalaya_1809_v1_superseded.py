# SUPERSEDED 28 Oct 2026 04:50: this first version matched no Everest column (names carry units, e.g. "Bi(ppt)") and scaled z on dust-spiked raw samples. Kept for the record of the first run; use himalaya_1809.py (v2).
"""Extract 1795-1830 from the two NOAA Himalayan ice-core trace-element files and look for the 1809 and 1815 signals.
Usage: python3 himalaya_1809.py rongbuk2009.txt dasuopu2020elem-noaa.txt
Files: https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/everest/rongbuk2009.txt (Kaspari et al. 2009 JGR, sub-annual S, Bi, Tl ... 1650-2002)
       https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/dasuopu/dasuopu2020elem-noaa.txt (Gabrielli et al. 2020 PNAS, 23 elements 1499-1992)
Written 28 Oct 2026 without access to the files (NOAA is blocked in the container): the parser is generic for the NOAA
text template (comment lines start with #; a header line of column names; tab- or space-separated numbers; -999 = missing).
Output: per-year medians 1795-1830 for S, Bi, Tl (and Cd, Sb for Dasuopu) with z-scores against a 1750-1800 baseline, as CSV and PNG.
"""
import sys, re, statistics as st
def parse(path):
    tables=[]; hdr=None; rows=[]
    for line in open(path, encoding='utf-8', errors='replace'):
        line=line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        toks=re.split(r'\t|\s{2,}|\s', line.strip())
        toks=[t for t in toks if len(t)>0]
        if any(re.search('[A-Za-z]', t) for t in toks):          # header line
            if hdr and rows: tables.append((hdr, rows))
            hdr=toks; rows=[]
        else:
            try: rows.append([float(t) for t in toks])
            except ValueError: pass
    if hdr and rows: tables.append((hdr, rows))
    return tables
def agecol(h):
    for i,c in enumerate(h):
        if re.match(r'(age|year|yr)', c, re.I): return i
    return None
def series(tables, name):
    """all (age, value) pairs for a column whose header equals name (case-sensitive) across tables"""
    out=[]
    for h,rows in tables:
        a=agecol(h)
        if a is None or name not in h: continue
        j=h.index(name)
        for r in rows:
            if len(r)>max(a,j) and r[j]>-900: out.append((r[a], r[j]))
    return out
def yearly(pairs, y0, y1):
    d={}
    for a,v in pairs:
        y=int(a)
        if y0<=y<=y1: d.setdefault(y,[]).append(v)
    return {y:st.median(v) for y,v in sorted(d.items())}
def report(label, tables, cols):
    print('\n==', label)
    for h,rows in tables: print('   table columns:', h[:12], '... rows:', len(rows))
    out={}
    for c in cols:
        p=series(tables,c)
        if not p: print('   no column', c); continue
        base=[v for a,v in p if 1750<=a<1800]
        if len(base)<5: base=[v for a,v in p if 1700<=a<1800]
        mu=st.median(base); sd=st.pstdev(base) if len(base)>1 else float('nan')
        yr=yearly(p,1795,1830)
        out[c]=(yr,mu,sd)
        print(f'   {c}: baseline 1750-1800 median {mu:.3g}, sd {sd:.3g}, samples/yr about {len([1 for a,v in p if 1795<=a<=1830])/36:.1f}')
        for y,v in yr.items():
            z=(v-mu)/sd if sd==sd and sd>0 else float("nan")
            flag=' <-- ' + '*'*min(5,int(abs(z))) if z==z and z>=2 else ''
            print(f'      {y}: {v:.4g}  z={z:+.1f}{flag}')
    return out
if __name__=='__main__':
    res={}
    for path in sys.argv[1:]:
        t=parse(path)
        if 'rongbuk' in path.lower(): res['Everest (East Rongbuk, 28.0N, 6518 m)']=report('Everest East Rongbuk '+path, t, ['S','Bi','Tl'])
        else: res['Dasuopu (28.4N, 7200 m)']=report('Dasuopu '+path, t, ['Bi','Tl','Cd','Sb','Pb'])
    with open('himalaya_1809_yearly.csv','w') as f:
        f.write('core,element,year,median,z_vs_1750-1800\n')
        for core,d in res.items():
            for el,(yr,mu,sd) in d.items():
                for y,v in yr.items():
                    z=(v-mu)/sd if sd==sd and sd>0 else ''
                    f.write(f'{core},{el},{y},{v},{z}\n')
    print('\nwrote himalaya_1809_yearly.csv')
    try:
        import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
        n=sum(len(d) for d in res.values()); fig,axs=plt.subplots(n,1,figsize=(7,2.2*n),sharex=True); axs=[axs] if n==1 else list(axs); k=0
        for core,d in res.items():
            for el,(yr,mu,sd) in d.items():
                ax=axs[k]; k+=1; ax.plot(list(yr), [ (v-mu)/sd if sd else v for v in yr.values()], 'k.-'); ax.axvline(1809,color='r',ls='--'); ax.axvline(1815,color='b',ls='--'); ax.set_ylabel(f'{el} z'); ax.set_title(core+' '+el, fontsize=8)
        axs[-1].set_xlabel('year'); fig.tight_layout(); fig.savefig('himalaya_1809.png',dpi=130); print('wrote himalaya_1809.png')
    except Exception as e: print('no plot:', e)
