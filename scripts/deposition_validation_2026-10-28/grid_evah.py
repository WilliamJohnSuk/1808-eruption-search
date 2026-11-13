import json, numpy as np, itertools, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/9ef394ea-bd92-5242-9b96-ac810034ace0/scratchpad/work')
from run_evah import run
rows=[]
lats=[20,15,10,5,0,-5,-10,-15,-20,-25,-30]
heights=[18,22,26,30]
seasonal=[('default',None),('seasonal_mix_0.2',([0.2]*6,[7,1,7,1,7,1]))]
for (sname,smix) in seasonal:
    for month in [12,6,4]:
        for lat in lats:
            for h in heights:
                r=run(lat,h,19.3,year=1990,month=month,day=1,seasonal_mix=smix,tag='grid')
                rows.append(dict(variant=sname,month=month,lat=lat,h_km=h,inj_SHmid=r['inj_boxes_tgS'][0],inj_TRmid=r['inj_boxes_tgS'][1],inj_NHmid=r['inj_boxes_tgS'][2],
                   inj_SHlow=r['inj_boxes_tgS'][3],inj_TRlow=r['inj_boxes_tgS'][4],inj_NHlow=r['inj_boxes_tgS'][5],inj_SHlmost=r['inj_boxes_tgS'][6],inj_NHlmost=r['inj_boxes_tgS'][7],
                   dep_SH=round(r['dep_tgS']['SH'],3),dep_TR=round(r['dep_tgS']['TR'],3),dep_NH=round(r['dep_tgS']['NH'],3),NH_over_SH=round(r['NH_over_SH'],3),NH_share=round(r['NH_share_extratrop'],3)))
        print(sname, month, 'done', flush=True)
import pandas as pd
df=pd.DataFrame(rows); df.to_csv('evah_grid.csv',index=False)
for (sname,_) in seasonal:
    for month in [12,6,4]:
        sub=df[(df.variant==sname)&(df.month==month)]
        piv=sub.pivot(index='lat',columns='h_km',values='NH_over_SH')
        print('\n',sname,'month',month,'NH/SH extratropical deposition ratio'); print(piv.to_string())
