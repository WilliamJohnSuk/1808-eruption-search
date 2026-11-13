import pandas as pd, numpy as np, sys
f=sys.argv[1]
use=['YR','MO','DY','latitude','longitude','ShipName','LogbookLanguage','Clearness','VoyageFrom','VoyageIni']
d=pd.read_csv(f,sep='\t',dtype=str,encoding='latin-1',on_bad_lines='skip',usecols=use)
for c in ['YR','MO','DY','latitude','longitude']: d[c]=pd.to_numeric(d[c],errors='coerce')
e=d[(d.LogbookLanguage=='ENGLISH')&d.Clearness.notna()].copy(); e['hz']=e.Clearness.str.upper().str.contains('HAZ')
inwin=(e.YR*12+e.MO>=1808*12+9)&(e.YR*12+e.MO<=1810*12+6)
def box(name,la0,la1,lo0,lo1,mos,win):
    m=e.latitude.between(la0,la1)&e.longitude.between(lo0,lo1)&e.MO.isin(mos)
    o=e[m&~inwin]; w=e[m&win]
    p=o.hz.mean(); n=len(w); k=int(w.hz.sum())
    from math import comb
    pv=sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1)) if n else float('nan')
    print(f'{name}: other years n={len(o)} ({o.YR.nunique()} yrs, {o.ShipName.nunique()} ships) hazy={100*p:.1f}% | window n={n} hazy={k} ({100*k/max(n,1):.0f}%) binomial P(>=k)={pv:.3g}')
W=lambda y0,m0,d0,y1,m1,d1: (e.YR*10000+e.MO*100+e.DY).between(y0*10000+m0*100+d0,y1*10000+m1*100+d1)
box('Townsend: equatorial-N Atlantic 0-30N 40-20W, Dec',0,30,-40,-20,[12],W(1808,12,1,1808,12,31))
box('Townsend: same box Dec-Jan',0,30,-40,-20,[12,1],W(1808,12,1,1809,1,31))
box('Tigris: SW Indian Ocean 35-20S 35-55E, Dec',-35,-20,35,55,[12],W(1808,12,1,1808,12,31))
box('Penelope: NW Atlantic 35-45N 75-60W, Nov',35,45,-75,-60,[11],W(1808,11,1,1808,11,30))
box('Penelope: NW Atlantic 35-45N 75-60W, Oct-Dec',35,45,-75,-60,[10,11,12],W(1808,10,1,1808,12,31))
box('All tropics 30S-30N, Dec 1808-Feb 1809',-30,30,-180,180,[12,1,2],W(1808,12,1,1809,2,28))
box('All tropics 30S-30N, Sep-Nov 1808',-30,30,-180,180,[9,10,11],W(1808,9,1,1808,11,30))
box('All tropics 30S-30N, Mar-Jun 1809',-30,30,-180,180,[3,4,5,6],W(1809,3,1,1809,6,30))
box('All lat, Dec 1808-Jun 1809',-90,90,-180,180,list(range(1,13)),W(1808,12,1,1809,6,30))
for s in ['PENELOPE','TOWNSEND','TIGRIS']:
    x=e[e.ShipName==s]; print(s, x.groupby(x.YR).hz.agg(['size','mean']).round(2).to_dict('index'))
print(e[e.ShipName=='PENELOPE'].groupby(['YR','MO']).hz.agg(['size','sum']).to_string())
print('--- excluding TOWNSEND')
e=e[e.ShipName!='TOWNSEND']; inwin=(e.YR*12+e.MO>=1808*12+9)&(e.YR*12+e.MO<=1810*12+6)
box('All tropics 30S-30N, Dec 1808-Feb 1809, no Townsend',-30,30,-180,180,[12,1,2],W(1808,12,1,1809,2,28))
box('All tropics, 1-31 Dec 1808, no Townsend',-30,30,-180,180,[12],W(1808,12,1,1808,12,31))
box('All lat, Dec 1808-Jun 1809, no Townsend',-90,90,-180,180,list(range(1,13)),W(1808,12,1,1809,6,30))
