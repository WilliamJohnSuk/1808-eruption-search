import json, numpy as np
D='/tmp/claude-0/-home-claude/d4d9de8b-aa01-5095-a917-597aca5223d2/scratchpad/emu/volcanic-forcing-deposition/data/'
ax=json.load(open(D+'axes.json')); lat=np.array(ax['lat'],float); h=np.array(ax['h'],float); so2=np.array(ax['so2'],float)
G={s:np.array(json.load(open(D+f'greenland_{s}.json'))['mean']) for s in ['jan','jul']}
A={s:np.array(json.load(open(D+f'antarctica_{s}.json'))['mean']) for s in ['jan','jul']}
lats=sorted(set(lat.tolist()))
# Tambora-like: bracket 8S with -10.51 and -4.04, SO2 56-60 Tg, all heights
print("Emulator Tambora-like predictions (SO2 53-64 Tg), by season and latitude:")
tamb={}
for s in ['jan','jul']:
    for L in [-10.51,-4.04]:
        m=(np.abs(lat-L)<0.01)&(so2>52)&(so2<65)
        r=G[s][m]/A[s][m]
        print(f"  {s} lat {L}: n={m.sum()} G mean {G[s][m].mean():.1f} A mean {A[s][m].mean():.1f}  ratio median {np.median(r):.2f} (range {r.min():.2f}-{r.max():.2f})")
        tamb[(s,L)]=np.median(r)
# interpolate to 8S: weight 0.61 toward -10.51 ((8-4.04)/(10.51-4.04)=0.61)
rj=0.61*tamb[('jan',-10.51)]+0.39*tamb[('jan',-4.04)]
rl=0.61*tamb[('jul',-10.51)]+0.39*tamb[('jul',-4.04)]
rapr=np.exp(0.5*(np.log(rj)+np.log(rl)))
print(f"Tambora-like emulator ratio: jan {rj:.2f}, jul {rl:.2f}, geometric mean (crude April proxy) {rapr:.2f}; observed Tambora ratio 0.87 (Sigl 2015 via Marshall 2021)")
for name,rt in [('jan-case',rj),('jul-case',rl),('geo-mean',rapr)]:
    print(f"  bias factor (emulator/observed) using {name}: {rt/0.87:.2f}")
# Calibrated target: observed 1809/Tambora ratio-of-ratios = 1.19 (range 0.8-1.9 per note B55; eVolv2k composite gives 1.03/0.87=1.18)
print("\nCalibrated inversion: find latitudes where emulator ratio(lat,season)/emulator Tambora ratio(same season) is within the observed 1809/Tambora ratio-of-ratios")
for s,rt in [('jan',rj),('jul',rl)]:
    print(f"\n season {s} (emulator Tambora ratio {rt:.2f}):")
    for lo,hi,label in [(1.0,1.4,'central 1.0-1.4'),(0.8,1.9,'full range 0.8-1.9')]:
        out=[]
        for L in lats:
            m=(lat==L)&(so2>20)
            rr=(G[s][m]/np.maximum(A[s][m],1e-6))/rt
            frac=((rr>lo)&(rr<hi)).mean()
            if frac>0.05: out.append((L,round(float(frac),2)))
        print(f"   {label}: latitudes with >5% of grid points consistent:", out)
    # median ratio-of-ratios by latitude
    med=[]
    for L in lats:
        m=(lat==L)&(so2>20)
        med.append((L, round(float(np.median((G[s][m]/np.maximum(A[s][m],1e-6))/rt)),2)))
    print("   median ratio-of-ratios by latitude:", med)
