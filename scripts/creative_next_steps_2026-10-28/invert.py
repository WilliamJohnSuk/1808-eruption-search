import json, numpy as np
from collections import Counter
D='/tmp/claude-0/-home-claude/d4d9de8b-aa01-5095-a917-597aca5223d2/scratchpad/emu/volcanic-forcing-deposition/data/'
ax=json.load(open(D+'axes.json')); lat=np.array(ax['lat'],float); h=np.array(ax['h'],float); so2=np.array(ax['so2'],float)
G={s:json.load(open(D+f'greenland_{s}.json')) for s in ['jan','jul']}
A={s:json.load(open(D+f'antarctica_{s}.json')) for s in ['jan','jul']}
F={s:json.load(open(D+f'forcing_{s}.json')) for s in ['jan','jul']}
print('grid',len(lat),'lats',sorted(set(lat.tolist())))
print('h',sorted(set(h.tolist())))
print('so2',sorted(set(so2.tolist()))[:5],'...',sorted(set(so2.tolist()))[-3:])
# sanity: units check, print deposition for Tambora-like (8S, 60 Tg SO2, h ~ 25.5) jan vs jul
for s in ['jan','jul']:
    gm=np.array(G[s]['mean']); am=np.array(A[s]['mean'])
    m=(np.abs(lat+8)<0.1)&(np.abs(so2-60)<2)
    print(s,'Tambora-like 8S 60Tg: h,G,A:',[(float(h[i]),round(float(gm[i]),1),round(float(am[i]),1)) for i in np.where(m)[0]])
# Observed 1809 composite deposition (Sigl 2013 table; kg/km2). Use given uncertainties.
obs=dict(G=25.9,sG=15.2,A=25.1,sA=13.3)
def consistent(s,k=1.0,obs=obs):
    gm=np.array(G[s]['mean']); gs=np.array(G[s]['sd']); am=np.array(A[s]['mean']); asd=np.array(A[s]['sd'])
    return (np.abs(gm-obs['G']) < k*np.sqrt(gs**2+obs['sG']**2)) & (np.abs(am-obs['A']) < k*np.sqrt(asd**2+obs['sA']**2))
lats=sorted(set(lat.tolist()))
for k in [0.5,1.0]:
    for s in ['jan','jul']:
        c=consistent(s,k)
        print(f'\n{s} k={k}: {c.sum()} consistent grid points')
        rows=[]
        for L in lats:
            m=c&(lat==L)
            if m.sum()==0: continue
            rows.append((L,int(m.sum()),float(so2[m].min()),float(so2[m].max())))
        for r in rows: print(f'  lat {r[0]:6.1f}: n={r[1]:3d} SO2 {r[2]:.0f}-{r[3]:.0f} Tg')
# Ratio-only test: Greenland/Antarctic ratio ~1.03 with generous error; which latitudes give ratio in [0.7,1.5]
print('\nRatio-only filter (G/A in 0.7-1.5), by latitude, fraction of grid points at that latitude:')
for s in ['jan','jul']:
    gm=np.array(G[s]['mean']); am=np.array(A[s]['mean'])
    r=gm/np.maximum(am,1e-6)
    ok=(r>0.7)&(r<1.5)
    out=[]
    for L in lats:
        m=(lat==L)
        out.append((L, round(float(ok[m].mean()),2), round(float(np.median(r[m])),2)))
    print(s, [(o[0],o[1]) for o in out])
    print(s,'median ratio by lat', [(o[0],o[2]) for o in out])
# also forcing for consistent points
for s in ['jan','jul']:
    c=consistent(s,1.0)
    fm=np.array(F[s]['mean'])
    print(s,'forcing of consistent points: median',round(float(np.median(fm[c])),2),'range',round(float(fm[c].min()),2),round(float(fm[c].max()),2),'SO2 median',float(np.median(so2[c])))
