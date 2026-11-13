import pandas as pd, numpy as np, re, sys, unicodedata
d=pd.read_csv(sys.argv[1],sep='\t',skiprows=18,dtype=str,encoding='latin-1')
d.columns=[c.strip() for c in d.columns]
for c in ['Year','Month','Day']: d[c]=pd.to_numeric(d[c],errors='coerce')
norm=lambda s: unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().lower()
d['ss']=d.SS.map(norm)
terms={'calim':r'calim','bruma':r'brum','niebla':r'nebl|niebl','cerraz':r'cerraz','vapor':r'vapor|vahos|celaj','sol':r'sol |sol$|rojo|encarnad|plateado|palido|empanad'}
for k,v in terms.items(): d[k]=d.ss.str.contains(v)
day=d.groupby(['Year','Month','Day'])[list(terms)].any().reset_index()
print('years/months with data:'); print(day.groupby('Year').size().to_string())
m=day.groupby(['Year','Month'])[list(terms)].mean().reset_index(); m['ndays']=day.groupby(['Year','Month']).size().values
base=m[~m.Year.isin([1809])]
clim=base.groupby('Month')['calim'].agg(['mean','std','count'])
mm=m.merge(clim,on='Month'); mm['z']=(mm.calim-mm['mean'])/mm['std']
pd.set_option('display.width',200)
print(mm[(mm.Year>=1808)&(mm.Year<=1810)][['Year','Month','ndays','calim','mean','std','z','bruma','niebla','vapor','sol']].round(2).to_string())
print('\nRank of each month 1808-09 among same calendar month, all years:')
for (y,mo) in [(1808,9),(1808,10),(1808,11),(1808,12),(1809,1),(1809,2),(1809,3),(1809,4)]:
    s=m[m.Month==mo].sort_values('calim',ascending=False).reset_index(drop=True)
    r=s.index[s.Year==y]
    print(y,mo,'calim frac',round(float(s.calim[s.Year==y].iloc[0]),2) if len(r) else None,'rank',(int(r[0])+1 if len(r) else None),'of',len(s))
x=d[(d.Year*100+d.Month).between(180810,180904)&d.ss.str.contains('sol |rojo|encarnad|plateado|palido|calim|brum')]
print(x[['Year','Month','Day','Hour','SS']].to_string())
print('\nWinter (Nov-Mar) calim days by winter, and obs hours used:')
d['wy']=np.where(d.Month>=11,d.Year+1,d.Year)
w=day.copy(); w['wy']=np.where(w.Month>=11,w.Year+1,w.Year); w=w[w.Month.isin([11,12,1,2,3])]
print(w.groupby('wy').agg(days=('calim','size'),calim=('calim','sum')).to_string())
print(d.groupby('Year').Hour.unique().to_string())
print('\nAll calim days by year/month count:'); print(day[day.calim].groupby(['Year','Month']).size().unstack(fill_value=0).to_string())
x=d[(d.Year*100+d.Month).between(180901,180903)]
print(x[x.ss.str.contains('calim')][['Year','Month','Day','Hour','W_D','W_F','T_A2','H','SS']].to_string())
print('\nwinds Jan-Feb 1809 all obs:'); print(x.W_D.value_counts().head(10).to_string())
