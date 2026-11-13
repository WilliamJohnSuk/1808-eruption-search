import pandas as pd, numpy as np
d=pd.read_csv('/tmp/claude-0/work/eeic_at_anoms.csv.gz')
d['t']=d.yr+(d.mo-1)/12+(d.dy-1)/365
tr=d[d.lat.abs()<=30].copy()
w=tr[(tr.t>=1808.5)&(tr.t<1809.5)]
print('Ships Dec 1808-Feb 1809 (tropical obs):')
x=w[(w.t>=1808+11/12)&(w.t<1809+2/12)]
print(x.groupby('ship').agg(n=('anom','size'),lat=('lat','mean'),lon=('lon','mean'),anom=('anom','mean'),first=('t','min'),last=('t','max')).round(2).to_string())
# within-voyage comparison: voyages with tropical obs both in Aug-Nov 1808 and Jan-Apr 1809
pre=tr[(tr.t>=1808+7/12)&(tr.t<1808+11/12)]; post=tr[(tr.t>=1809)&(tr.t<1809+4/12)]
a=pre.groupby('file').anom.agg(['mean','size']); b=post.groupby('file').anom.agg(['mean','size'])
j=a.join(b,lsuffix='_pre',rsuffix='_post',how='inner'); j=j[(j.size_pre>=10)&(j.size_post>=10)]
j['diff']=j.mean_post-j.mean_pre
print('\nWithin-voyage: Aug-Nov 1808 vs Jan-Apr 1809'); print(j.round(2).to_string()); print('mean diff',round(j['diff'].mean(),2),'n voyages',len(j))
# null: same within-voyage diff for same calendar windows in other years (not 1809,1810,1816,1817)
res=[]
for y in range(1789,1834):
    if y+1 in (1809,1810,1811,1816,1817): continue
    pre=tr[(tr.t>=y+7/12)&(tr.t<y+11/12)]; post=tr[(tr.t>=y+1)&(tr.t<y+1+4/12)]
    a=pre.groupby('file').anom.agg(['mean','size']); b=post.groupby('file').anom.agg(['mean','size'])
    jj=a.join(b,lsuffix='_pre',rsuffix='_post',how='inner'); jj=jj[(jj.size_pre>=10)&(jj.size_post>=10)]
    if len(jj): res.append((y,len(jj),(jj.mean_post-jj.mean_pre).mean()))
r=pd.DataFrame(res,columns=['yr','nvoy','meandiff']); print('\nOther years:'); print(r.round(2).to_string())
print('null mean',round(r.meandiff.mean(),2),'sd',round(r.meandiff.std(),2))
