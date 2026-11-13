"""Final validation pass (Claude's calculation, 28 Oct 2026). Emulator = Marshall et al. 2021 (cemac/volcanic-forcing-deposition).
Predicted Greenland/Antarctic ratio evaluated (a) at a FIXED SO2 window 35-60 Tg (the 1809 and Tambora range; the emulator's
ratio depends on mass and its Greenland values go negative below ~20 Tg, so small eruptions cannot be evaluated at their own mass),
(b) at the event's own mass where >= 20 Tg SO2. Month weighting: log-linear between the January and July emulators with
w = (1+cos(2pi(month-1)/12))/2. Observed R bases as in validate_emulator.py plus Sigl 2013 pairs for Makian, Agung, Pinatubo+Hudson."""
import json, numpy as np, pandas as pd, math
from scipy import stats
D='/tmp/claude-0/-home-claude/9ef394ea-bd92-5242-9b96-ac810034ace0/scratchpad/emu/volcanic-forcing-deposition/data/'
ax=json.load(open(D+'axes.json')); lat=np.array(ax['lat'],float); h=np.array(ax['h'],float); so2=np.array(ax['so2'],float)
G={s:np.array(json.load(open(D+f'greenland_{s}.json'))['mean']) for s in ['jan','jul']}
A={s:np.array(json.load(open(D+f'antarctica_{s}.json'))['mean']) for s in ['jan','jul']}
lats=np.array(sorted(set(lat.tolist())))
def logratio_at(season,Lg,lo,hi):
    m=(np.abs(lat-Lg)<0.01)&(so2>=lo)&(so2<=hi)
    g=G[season][m]; a=A[season][m]; ok=(g>0)&(a>0)
    r=g[ok]/a[ok]
    return math.log(np.median(r)), math.log(np.percentile(r,10)), math.log(np.percentile(r,90))
def emu_ratio(season,L,lo,hi):
    i=np.clip(np.searchsorted(lats,L),1,len(lats)-1); L0,L1=lats[i-1],lats[i]; w=(L-L0)/(L1-L0)
    a=logratio_at(season,L0,lo,hi); b=logratio_at(season,L1,lo,hi)
    return [(1-w)*a[k]+w*b[k] for k in range(3)]
def wjan(month,day=1): return 0.5*(1+math.cos(2*math.pi*(month+(day-1)/30.0-1)/12.0))
def pred(L,month,day,lo=35,hi=60):
    rj=emu_ratio('jan',L,lo,hi); rl=emu_ratio('jul',L,lo,hi); w=wjan(month,day)
    return [math.exp(w*rj[k]+(1-w)*rl[k]) for k in range(3)]+[math.exp(rj[0]),math.exp(rl[0]),w]
E=[ # name, year, month, day, lat, VSSI TgS (eVolv2k), observed R by basis, flags
 dict(name='Huaynaputina',year=1600,month=2,day=17,lat=-16.6,vssi=18.95,evolv2k=2.0,crowley=35/10.7,sigl13=30.4/24.0,gao07=None,flag=''),
 dict(name='Ruiz',year=1595,month=3,day=1,lat=4.9,vssi=8.87,evolv2k=0.8,crowley=None,sigl13=None,gao07=None,flag='small'),
 dict(name='Parker',year=1640,month=12,day=26,lat=6.1,vssi=18.68,evolv2k=2.8,crowley=None,sigl13=46.8/12.4,gao07=None,flag='Crowley SH composite has no 1641 signal'),
 dict(name='Gamkonora',year=1673,month=5,day=20,lat=1.4,vssi=4.67,evolv2k=0.7,crowley=13.3/6.8,sigl13=6.4/11.5,gao07=None,flag='small'),
 dict(name='Tambora',year=1815,month=4,day=10,lat=-8.25,vssi=28.08,evolv2k=0.8,crowley=32.4/52.4,sigl13=39.0/88.6,gao07=59/51,flag=''),
 dict(name='Cosiguina',year=1835,month=1,day=20,lat=13.0,vssi=9.48,evolv2k=2.0,crowley=14.3/8.4,sigl13=13.1/15.1,gao07=None,flag='small'),
 dict(name='Makian',year=1861,month=12,day=28,lat=0.3,vssi=4.53,evolv2k=2.4,crowley=4.2/4.8,sigl13=19.3/7.1,gao07=None,flag='small; Crowley match uncertain'),
 dict(name='Krakatau',year=1883,month=8,day=27,lat=-6.1,vssi=9.34,evolv2k=1.7,crowley=13.6/9.2,sigl13=18.5/11.2,gao07=11/11,flag='small'),
 dict(name='Samalas',year=1257,month=7,day=1,lat=-8.4,vssi=59.42,evolv2k=1.4,crowley=113.6/83.3,sigl13=82.1/79.7,gao07=146/112,flag='month uncertain (May-Oct 1257)'),
 dict(name='Agung',year=1963,month=3,day=17,lat=-8.3,vssi=None,evolv2k=None,crowley=None,sigl13=7.2/16.5,gao07=None,flag='NEEM value 7.2+-7.6 (noise level; Surtsey overlap)'),
 dict(name='Pinatubo+Hudson',year=1991,month=6,day=15,lat=15.1,vssi=None,evolv2k=None,crowley=None,sigl13=37.2/25.4,gao07=None,flag='Antarctic value includes Cerro Hudson Aug 1991 (46S)'),
 dict(name='Colima_1585',year=1585,month=1,day=10,lat=19.5,vssi=8.51,evolv2k=10.6,crowley=None,sigl13=None,gao07=None,flag='small; outside +-17'),
]
bases=['evolv2k','crowley','sigl13','gao07']
rows=[]
for e in E:
    p=pred(e['lat'],e['month'],e['day'])
    own=pred(e['lat'],e['month'],e['day'],lo=2*e['vssi']*0.75,hi=2*e['vssi']*1.25) if (e['vssi'] and 2*e['vssi']>=20) else [float('nan')]*6
    r=dict(event=e['name'],year=e['year'],month=e['month'],day=e['day'],lat=e['lat'],so2_Tg=None if e['vssi'] is None else round(2*e['vssi'],1),jan_weight=round(p[5],2),
           emu_R_jan_35to60=round(p[3],2),emu_R_jul_35to60=round(p[4],2),emu_R_month_35to60=round(p[0],2),emu_R_p10=round(p[1],2),emu_R_p90=round(p[2],2),
           emu_R_month_ownmass=None if math.isnan(own[0]) else round(own[0],2))
    obs=[e[b] for b in bases if e[b] is not None]
    r['obs_R_geomean']=round(math.exp(np.mean(np.log(obs))),2); r['obs_R_min']=round(min(obs),2); r['obs_R_max']=round(max(obs),2); r['n_bases']=len(obs)
    for b in bases: r['obs_R_'+b]=None if e[b] is None else round(e[b],2)
    r['log10_pred_over_obs_geomean']=round(math.log10(p[0]/r['obs_R_geomean']),2)
    r['flag']=e['flag']
    rows.append(r)
df=pd.DataFrame(rows)
pd.set_option('display.width',300); pd.set_option('display.max_columns',40); pd.set_option('display.max_colwidth',50)
print(df.drop(columns=['flag']).to_string(index=False))
print('\nflags:'); print(df[['event','flag']].to_string(index=False))
core=df[df.lat.abs()<=17]
err=core['log10_pred_over_obs_geomean'].astype(float)
print(f"\nRaw emulator (fixed 35-60 Tg) vs geometric-mean observed R, |lat|<=17, n={len(err)}: mean log10 {err.mean():+.2f} (x{10**err.mean():.2f}), rms {np.sqrt((err**2).mean()):.2f} (x{10**np.sqrt((err**2).mean()):.2f}); within 1.5x {(err.abs()<=math.log10(1.5)).sum()}, 2x {(err.abs()<=math.log10(2)).sum()}, 3x {(err.abs()<=math.log10(3)).sum()}")
# bias-corrected residuals
bias=err.mean(); res=err-bias
print(f"After removing the mean bias (x{10**bias:.2f}): rms {np.sqrt((res**2).mean()):.2f} (x{10**np.sqrt((res**2).mean()):.2f}); within 1.5x {(res.abs()<=math.log10(1.5)).sum()}, 2x {(res.abs()<=math.log10(2)).sum()}")
# Correlation between predicted and observed (log), |lat|<=17: does the emulator rank the eruptions correctly?
x=np.log10(core.emu_R_month_35to60.astype(float)); y=np.log10(core.obs_R_geomean.astype(float))
rp=stats.pearsonr(x,y); rs=stats.spearmanr(x,y)
print(f"Correlation log(pred) vs log(obs), n={len(x)}: Pearson r={rp[0]:.2f} (p={rp[1]:.2f}), Spearman rho={rs[0]:.2f} (p={rs[1]:.2f})")
# Observed R vs latitude (season-adjusted and not), |lat|<=17, geometric mean basis
L=core.lat.astype(float).values; ph=np.array([2*math.pi*(m+(d-1)/30-1)/12 for m,d in zip(core.month,core.day)])
for lab,X in [('lat only',np.column_stack([np.ones(len(L)),L])),('lat+season',np.column_stack([np.ones(len(L)),L,np.cos(ph),np.sin(ph)]))]:
    beta,_,_,_=np.linalg.lstsq(X,y*math.log(10),rcond=None); yhat=X@beta; n,p=X.shape; s2=((y*math.log(10)-yhat)**2).sum()/(n-p); se=np.sqrt(np.diag(s2*np.linalg.inv(X.T@X)))
    t=beta/se; pv=2*(1-stats.t.cdf(abs(t),n-p))
    print(f"Observed lnR ~ {lab}: slope {beta[1]:+.4f}/deg (se {se[1]:.4f}, p={pv[1]:.2f}; x{math.exp(10*beta[1]):.2f} per 10 deg N); "+(f"season amplitude {math.hypot(beta[2],beta[3]):.2f} (peak month {((math.degrees(math.atan2(beta[3],beta[2]))%360)/30+1):.1f}, cos {beta[2]:+.2f} sin {beta[3]:+.2f}), p_cos={pv[2]:.2f} p_sin={pv[3]:.2f}; " if p==4 else '')+f"resid sd ln {math.sqrt(s2):.2f} (x{math.exp(math.sqrt(s2)):.2f}), n={n}")
# Emulator slope for comparison (December, 35-60 Tg): predicted R at -15,-10,-5,0,5,10,15
print('\nEmulator December (w=0.93) R by latitude, 35-60 Tg:', [(Lq, round(pred(Lq,12,1)[0],2)) for Lq in [-20,-15,-10,-5,0,5,10,15,20]])
print('Emulator seasonal factor Jan/Jul at 8S, 35-60 Tg:', round(pred(-8,1,1)[3]/pred(-8,1,1)[4],2))
# 1809 inversion with the bias-corrected emulator and the validation scatter
print('\n1809 inversion (December eruption, 35-60 Tg): observed R 1.3 (eVolv2k), 0.91 (Sigl13 pair), 1.21 (Crowley), 1.08 (Gao); use R=1.1 (x/1.3) and R=1.3')
Lgrid=np.arange(-30,30.1,0.5)
for Robs,Rsd in [(1.1,math.log(1.3)),(1.3,math.log(1.3))]:
    for corr_lab,b_,s_ in [('raw emulator, error = validation rms',0.0,np.sqrt((err**2).mean())*math.log(10)),('bias-corrected emulator, error = residual rms',bias*math.log(10),np.sqrt((res**2).mean())*math.log(10))]:
        mu=np.array([math.log(pred(Lq,12,1)[0]) for Lq in Lgrid])-b_
        sd=math.sqrt(s_**2+Rsd**2)
        like=stats.norm.pdf((math.log(Robs)-mu)/sd); post=like/like.sum(); cdf=np.cumsum(post)
        q=lambda a: Lgrid[min(np.searchsorted(cdf,a),len(Lgrid)-1)]
        print(f"  R={Robs}: {corr_lab}: mode {Lgrid[post.argmax()]:+.1f}, 68% {q(0.16):+.0f}..{q(0.84):+.0f}, 95% {q(0.025):+.0f}..{q(0.975):+.0f}, P(lat>+8)={post[Lgrid>8].sum():.2f}, P(lat<-12)={post[Lgrid<-12].sum():.2f}")
df.to_csv('deposition_ratio_validation_2026-10-28.csv',index=False)
# Tambora-calibrated ratio-of-ratios at the fixed window (the B62 method), geometric-mean observed basis
pt=pred(-8.25,4,10)[0]; tobs=df.loc[df.event=='Tambora','obs_R_geomean'].iloc[0]
rr=[]
for _,r in df.iterrows():
    if r.event=='Tambora': continue
    pr=r.emu_R_month_35to60/pt; ob=r.obs_R_geomean/tobs
    rr.append(dict(event=r.event,lat=r.lat,month=r.month,pred_RR_vs_Tambora=round(pr,2),obs_RR_vs_Tambora_geomean=round(ob,2),factor=round(max(pr/ob,ob/pr),2)))
rr=pd.DataFrame(rr); print('\nTambora-calibrated ratio-of-ratios (fixed 35-60 Tg; observed = geometric mean of bases):'); print(rr.to_string(index=False))
rr.to_csv('deposition_ratio_of_ratios_vs_tambora_2026-10-28.csv',index=False)
