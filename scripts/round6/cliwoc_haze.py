import pandas as pd, numpy as np, re, sys
f=sys.argv[1]
use=['YR','MO','DY','latitude','longitude','ShipName','Nationality','LogbookLanguage','Weather','Clearness','ShapeClouds','OtherRem','EncRem','PrecipitationDescriptor','StateSea','VoyageFrom','VoyageTo']
d=pd.read_csv(f,sep='\t',dtype=str,encoding='latin-1',on_bad_lines='skip',usecols=use)
for c in ['YR','MO','DY','latitude','longitude']: d[c]=pd.to_numeric(d[c],errors='coerce')
d['txt']=(d.Weather.fillna('')+' | '+d.Clearness.fillna('')+' | '+d.ShapeClouds.fillna('')+' | '+d.OtherRem.fillna('')).str.upper()
veil=re.compile(r'HAZ|SMOK|DARK|GLOOM|DUSK|RED SKY|RED SUN|DIM|ASH|DUST|SULPH|PUMIC|OBSCUR|NEVEL|DAMP|DIS|CALIM|BRUMA|NIEBLA|CERRAZ|FIERY|LURID|COPPER|BLOOD')
en=d[(d.LogbookLanguage=='ENGLISH')&d.Clearness.notna()].copy()
en['haze']=en.Clearness.str.upper().str.contains('HAZ')
en['period']=np.where((en.YR*12+en.MO>=1808*12+9)&(en.YR*12+en.MO<=1810*12+6),'1808-09..1810-06','other')
print('English logs with Clearness field, by year (n, %hazy):')
y=en.groupby('YR').agg(n=('haze','size'),hz=('haze','mean')); print(y.loc[1795:1825].assign(hz=lambda x:(100*x.hz).round(1)).to_string())
# monthly baseline: same calendar month, same 10-deg lat band
en['band']=(en.latitude//15)*15
base=en[en.period=='other'].groupby(['MO','band']).haze.mean()
w=en[en.period!='other'].copy()
w['exp']=[base.get((m,b),np.nan) for m,b in zip(w.MO,w.band)]
print('\n1808-09..1810-06 English Clearness obs:',len(w),'hazy obs',int(w.haze.sum()),'expected',round(w.exp.sum(),1))
print(w.groupby(['YR','MO']).agg(n=('haze','size'),hazy=('haze','sum'),exp=('exp','sum')).round(1).to_string())
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120)
x=w[w.haze&(w.YR*12+w.MO<=1809*12+6)]
print(x[['YR','MO','DY','ShipName','latitude','longitude','Clearness']].to_string())
# all-language veil-word grep in window
v=d[(d.YR*12+d.MO>=1808*12+9)&(d.YR*12+d.MO<=1810*12+6)]
v=v[v.txt.str.contains(veil)&~v.Clearness.fillna('').str.upper().str.contains('HAZ')]
print('\nOther veil-word hits:'); print(v[['YR','MO','DY','ShipName','latitude','longitude','txt']].to_string())
e=d[(d.YR*12+d.MO>=1808*12+9)&(d.YR*12+d.MO<=1810*12+6)&d.EncRem.notna()]
print('\nEncRem sample:'); print(e.EncRem.str.upper().value_counts().head(15).to_string())
print(e[e.EncRem.str.upper().str.contains('VOLCAN|ERUPT|EARTHQ|ASH|PUMIC|NEWS|TERREMOTO|VOLCÁN',regex=True)][['YR','MO','DY','ShipName','EncRem']].to_string())
