import glob, os, numpy as np, pandas as pd
rows=[]
for f in glob.glob('/tmp/claude-0/dl/EEIC/imma/*/*.imma'):
    ship=os.path.basename(f).split('.')[0]
    for l in open(f,encoding='latin-1'):
        try:
            yr=int(l[0:4]); mo=int(l[4:6]); dy=int(l[6:8])
            lat=l[12:17].strip(); lon=l[17:23].strip(); at=l[69:73].strip()
            if not(lat and lon and at): continue
            lat=int(lat)/100; lon=int(lon)/100; at=int(at)/10
        except ValueError: continue
        rows.append((ship,f,yr,mo,dy,lat,lon,at))
d=pd.DataFrame(rows,columns=['ship','file','yr','mo','dy','lat','lon','AT'])
d=d[(d.AT>-5)&(d.AT<40)]
d['bx']=(d.lat//10).astype(int).astype(str)+'_'+(d.lon//10).astype(int).astype(str)
excl=d.yr.isin([1809,1810,1811,1812,1815,1816,1817,1818])
clim=d[~excl].groupby(['bx','mo']).AT.agg(['mean','count']).reset_index()
d=d.merge(clim,on=['bx','mo'],how='left'); d=d[d['count']>=30]
d['anom']=d.AT-d['mean']
d.to_csv('/tmp/claude-0/work/eeic_at_anoms.csv.gz',index=False)
tr=d[d.lat.abs()<=30]
print('total obs',len(d),'tropical',len(tr))
g=tr.groupby(['yr','mo']).agg(n=('anom','size'),ships=('file','nunique'),anom=('anom','mean'),sd=('anom','std')).reset_index()
g['se']=g.sd/np.sqrt(g.ships)  # conservative: effective n ~ ships
g.to_csv('/tmp/claude-0/work/eeic_tropical_monthly.csv',index=False)
pd.set_option('display.width',200)
print(g[(g.yr>=1806)&(g.yr<=1812)].round(2).to_string())
print(g[(g.yr>=1814)&(g.yr<=1817)].round(2).to_string())
a=tr.groupby('yr').agg(n=('anom','size'),ships=('file','nunique'),anom=('anom','mean'))
print(a.loc[1800:1820].round(2).to_string())
