import pandas as pd, numpy as np, sys, warnings; warnings.filterwarnings('ignore')
ice={'DomeC':[59.44,16.43,9.00,2.83,5.44,4.14,2.05],'SPole':[60.28,15.80,7.91,2.35,5.45,4.26,3.11],'Eclipse':[64.86,16.13,3.84,1.12,3.56,6.64,2.70],'Siple':[63.4,16.77,6.3,np.nan,1.21,5.99,4.91]}
def sc(a,b):
    r=[min(x,y)/max(x,y) for x,y in zip(a,b) if not np.isnan(x) and not np.isnan(y) and x>0 and y>0]; return sum(r)/len(r)
out=[]
for f in sys.argv[1:]:
    d=pd.read_csv(f,encoding='latin-1',low_memory=False)
    g=lambda c: pd.to_numeric(d.get(c),errors='coerce') if c in d else pd.Series(np.nan,index=d.index)
    feot=g('FEOT(WT%)'); alt=g('FEO(WT%)').fillna(0)+g('FE2O3(WT%)').fillna(0)*0.8998
    alt[(g('FEO(WT%)').isna())&(g('FE2O3(WT%)').isna())]=np.nan
    feot=feot.fillna(alt)
    ox=pd.DataFrame({'SiO2':g('SIO2(WT%)'),'TiO2':g('TIO2(WT%)'),'Al2O3':g('AL2O3(WT%)'),'FeOt':feot,'MnO':g('MNO(WT%)'),'MgO':g('MGO(WT%)'),'CaO':g('CAO(WT%)'),'Na2O':g('NA2O(WT%)'),'K2O':g('K2O(WT%)'),'P2O5':g('P2O5(WT%)')})
    ok=ox[['SiO2','Al2O3','FeOt','CaO','Na2O','K2O']].notna().all(axis=1)
    s=ox.fillna(0).sum(axis=1); n=ox.div(s,axis=0)*100
    for i in d.index[ok]:
        k=[n.at[i,c] for c in ['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O']]
        rec=dict(file=f.split('_2026-09_')[-1].replace('.csv',''),location=d.at[i,'LOCATION'],sample=d.at[i,'SAMPLE NAME'],material=d.at[i,'MATERIAL'],rock=d.at[i,'ROCK NAME'],age_min=d.at[i,'MIN. AGE (YRS.)'],age_max=d.at[i,'MAX. AGE (YRS.)'],geol_age=d.at[i,'AGE'],eruption_year=d.at[i,'ERUPTION YEAR'],citation=str(d.at[i,'CITATIONS'])[:40])
        rec.update({c:round(v,2) for c,v in zip(['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O'],k)})
        rec.update({kk:round(sc(k,vv),3) for kk,vv in ice.items()})
        out.append(rec)
o=pd.DataFrame(out); o.to_csv('georoc_scored_2026-10-26.csv',index=False); print(len(o)); print(o.groupby(['file','material']).size())
