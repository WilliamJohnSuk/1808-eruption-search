import pandas as pd, warnings, re; warnings.filterwarnings('ignore')
ice={'DomeC':[59.44,16.43,9.00,2.83,5.44,4.14,2.05],'SPole':[60.28,15.80,7.91,2.35,5.45,4.26,3.11],'Eclipse':[64.86,16.13,3.84,1.12,3.56,6.64,2.70],'Siple':[63.4,16.77,6.3,None,1.21,5.99,4.91]}
def sc(a,b):
    r=[min(x,y)/max(x,y) for x,y in zip(a,b) if x is not None and y is not None and x>0 and y>0]; return sum(r)/len(r)
rows=[]
def add(src,isl,volc,samp,age,name,si,ti,al,feot,mn,mg,ca,na,k,p):
    v=[si,ti,al,feot,mn,mg,ca,na,k,p]; v=[0 if pd.isna(x) else float(x) for x in v]
    if v[0]==0: return
    s=sum(v); n=[x*100/s for x in v]; key=[n[0],n[2],n[3],n[5],n[6],n[7],n[8]]
    rows.append(dict(src=src,island=isl,volcano=volc,sample=samp,age=age,name=name,**{o:round(x,2) for o,x in zip(['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O'],key)},**{k_:round(sc(key,v_),2) for k_,v_ in ice.items()}))
b=pd.read_excel('Gill_ECL1499_Banda_wholerock.xlsx',header=0).iloc[1:]
for _,r in b.iterrows(): add('ECL1499',r['Island'],r['Island'],r['Sample'],r['Age'],r['Name'],r['SiO2'],r['TiO2'],r['Al2O3'],r['FeOT'],0,r['MgO'],r['CaO'],r['Na2O'],r['K2O'],r['P2O5'])
h=pd.read_excel('Gill_ECL1502_Halmahera_wholerock.xls',header=0)
for _,r in h.iterrows(): add('ECL1502',r['Island'],r['Volcano'],r['Sample'],str(r['Jezek field notes'])[:60],r['Name'],r['SiO2'],r['TiO2'],r['Al2O3'],r['FeO*'],r['MnO'],r['MgO'],r['CaO'],r['Na2O'],r['K2O'],r['P2O5'])
s=pd.read_excel('Gill_ECL1503_Sangihe_wholerock.xlsx',sheet_name='Geochemistry',header=0)
for _,r in s.iterrows(): add('ECL1503',r['Island'],r['Volcano'],f"{r['Collection']}{r['Number']}",str(r['Field notes'])[:60],r['Name'],r['SiO2'],r['TiO2'],r['Al2O3'],r['Fe2O3']*0.8998 if not pd.isna(r['Fe2O3']) else None,r['MnO'],r['MgO'],r['CaO'],r['Na2O'],r['K2O'],r['P2O5'])
d=pd.DataFrame(rows); d.to_csv('/tmp/gill_scored.csv',index=False)
print(len(d)); print(d.groupby(['src']).size())
pd.set_option('display.width',250)
print(d.sort_values('DomeC',ascending=False).head(25)[['src','island','volcano','sample','age','SiO2','FeOt','K2O','DomeC','SPole','Eclipse']].to_string())
print(d.sort_values('SPole',ascending=False).head(10)[['src','volcano','sample','age','SiO2','K2O','DomeC','SPole']].to_string())
g=d.groupby(['src','volcano']).agg(n=('DomeC','size'),SiO2min=('SiO2','min'),SiO2max=('SiO2','max'),K2Omax=('K2O','max'),DomeC=('DomeC','max'),SPole=('SPole','max'),Eclipse=('Eclipse','max'))
print(g.to_string())
