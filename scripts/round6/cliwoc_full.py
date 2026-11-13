import pandas as pd, sys
f=sys.argv[1]
d=pd.read_csv(f,sep='\t',dtype=str,encoding='latin-1',on_bad_lines='skip',low_memory=False)
print(d.shape)
d['Y']=pd.to_numeric(d.YR,errors='coerce'); d['M']=pd.to_numeric(d.MO,errors='coerce'); d['Dd']=pd.to_numeric(d.DY,errors='coerce')
d['date']=pd.to_datetime(dict(year=d.Y,month=d.M,day=d.Dd),errors='coerce')
w=d[(d.date>='1808-09-01')&(d.date<='1810-06-30')].copy()
print('records',len(w))
txt=['Weather','Clearness','ShapeClouds','DirClouds','PrecipitationDescriptor','StateSea','OtherRem','LifeOnBoard','ShipAndRigMemo','BiologyMemo','WarsAndFightsMemo','EncRem','CargoMemo']
txt=[c for c in txt if c in w.columns]
for c in txt: print(c, w[c].notna().sum())
w=w.sort_values(['ShipName','date'])
w[['date','ShipName','Nationality','LogbookLanguage','latitude','longitude']+txt].to_csv('/tmp/claude-0/work/cliwoc_full_1808-09_1810-06.csv',index=False)
