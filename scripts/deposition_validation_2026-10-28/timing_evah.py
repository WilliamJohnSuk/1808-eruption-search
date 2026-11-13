import json, numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/9ef394ea-bd92-5242-9b96-ac810034ace0/scratchpad/work')
from run_evah import run
import pandas as pd
sites={'Bogota 4.6N':2.5,'Lima 12S':-12.5,'Edo 35.7N':37.5,'Tottori 35.5N':37.5,'Europe 50N':52.5,'Sydney 34S':-32.5,'Canton 23N':22.5,'Batavia 6S':-7.5}
out=[]
scen=[('Dec1808_5S_26km',-5,26,19.3,12,1),('Dec1808_10N_26km',10,26,19.3,12,1),('Dec1808_10S_26km',-10,26,19.3,12,1),('Dec1808_5S_20km',-5,20,19.3,12,1),('Dec1808_5S_32km',-5,32,19.3,12,1),('Tambora_Apr1815_8S_30km',-8.25,30,28.1,4,10),('Krakatau_Aug1883_6S_26km',-6.1,26,9.5,8,27)]
res={}
for name,lat,h,m,mo,d in scen:
    r=run(lat,h,m,year=1990,month=mo,day=d,want_saod=True,background=False,tag='tim')
    res[name]=r
    latg=np.array(r['saod_lat_grid']); S=np.array(r['saod550_monthly_by_lat']); gm=np.array(r['gm_saod550_monthly'])
    row={'scenario':name,'peak_gm_saod550':round(float(gm.max()),3),'month_of_gm_peak':int(gm.argmax())}
    for sname,sl in sites.items():
        j=int(np.argmin(np.abs(latg-sl))); s=S[:,j]; pk=s.max(); ip=int(s.argmax())
        m10=int(np.argmax(s>=0.1*pk)); m50=int(np.argmax(s>=0.5*pk))
        # month after eruption when SAOD first exceeds 0.02 (roughly the threshold for visible twilight effects; Claude's rough threshold)
        m02=int(np.argmax(s>=0.02)) if (s>=0.02).any() else -1
        row[sname]=f"peak {pk:.3f} @m{ip}; 10% m{m10}; 50% m{m50}; >0.02 m{m02}"
    out.append(row)
    # hemispheric mean SAOD (area weighted) NH extratropics (>25N), tropics, SH extratropics
    w=np.cos(np.deg2rad(latg))
    def band(mask): return (S[:,mask]*w[mask]).sum(axis=1)/w[mask].sum()
    nh=band(latg>25); tr=band(np.abs(latg)<=25); sh=band(latg<-25)
    row['peak_band_saod_NHx_TR_SHx']=f"{nh.max():.3f} {tr.max():.3f} {sh.max():.3f} (NHx/SHx {nh.max()/sh.max():.2f})"
    row['first12mo_mean_band_saod_NHx_TR_SHx']=f"{nh[:12].mean():.3f} {tr[:12].mean():.3f} {sh[:12].mean():.3f}"
    print(name, flush=True)
df=pd.DataFrame(out)
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',60)
for c in df.columns: print(c); print(df[['scenario',c]].to_string(index=False)) if c!='scenario' else None
json.dump({k:{kk:vv for kk,vv in v.items()} for k,v in res.items()}, open('evah_timing_full.json','w'))
df.to_csv('evah_timing_summary.csv',index=False)
