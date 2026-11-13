import pandas as pd, numpy as np, sys
out=[]
for sid,name in [('ITE00100554','Milan'),('EZE00100082','Prague')]:
    d=pd.read_csv(f'/tmp/claude-0/dl/ghcn/{sid}.csv',dtype=str)
    d=d[d.ELEMENT.isin(['TMAX','TMIN'])&d.Q_FLAG.isna()]
    d['v']=d.DATA_VALUE.astype(float)/10; d['date']=pd.to_datetime(d.DATE)
    p=d.pivot_table(index='date',columns='ELEMENT',values='v')
    p['DTR']=p.TMAX-p.TMIN; p['TM']=(p.TMAX+p.TMIN)/2
    p=p['1785':'1830']
    m=p.resample('MS').mean(); m['n']=p.DTR.resample('MS').count()
    base=m['1790':'1807']
    clim=base.groupby(base.index.month)[['DTR','TM']].mean(); sd=base.groupby(base.index.month)[['DTR','TM']].std()
    m['DTRa']=m.DTR-clim.DTR.reindex(m.index.month).values
    m['DTRz']=m.DTRa/sd.DTR.reindex(m.index.month).values
    m['TMa']=m.TM-clim.TM.reindex(m.index.month).values
    m['st']=name
    out.append(m)
    print(name, 'source flags', d.S_FLAG.unique(), 'clim DTR by month', clim.DTR.round(1).tolist())
    sel=m['1808-06':'1810-06'][['n','DTR','DTRa','DTRz','TMa']].round(2)
    print(sel.to_string())
    for lab,a,b in [('1801-07',1801,1807),('1809',1809,1809),('1810',1810,1810),('1811-14',1811,1814),('1816',1816,1816),('1817-20',1817,1820)]:
        s=m[str(a):str(b)]; print(lab,'mean DTRa',round(s.DTRa.mean(),2),'TMa',round(s.TMa.mean(),2))
pd.concat(out).to_csv('/tmp/claude-0/work/dtr_monthly.csv')
