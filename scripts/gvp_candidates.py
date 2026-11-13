import pandas as pd, sys, numpy as np
D=sys.argv[1]; OUT=sys.argv[2]
v=pd.read_excel(D+'/VOTW467_8May18_Holocene_list_textdata_portable.xls',header=0)
e=pd.read_excel(D+'/VOTW467_8May18_Eruption_list_textdata_portable.xls',header=1)
e=e[pd.to_numeric(e['Volcano Number'],errors='coerce').notna()].copy()
e['Volcano Number']=e['Volcano Number'].astype(int)
for c in ['Start Year','Start Year Uncertainty','VEI','End Year']: e[c]=pd.to_numeric(e[c],errors='coerce')
hist=e['Evidence Method (dating)'].eq('Historical Observations')
e['unc']=e['Start Year Uncertainty'].where(e['Start Year Uncertainty'].notna(), np.where(e['Evidence Method (dating)'].notna() & ~hist,50,0))
blank={'Halmahera','Sulawesi','Sangihe Islands','Banda Sea','Mindanao','Central Philippines',"New Guinea and D'Entrecasteaux Islands",'Northeast of New Guinea','New Britain','New Ireland','Admiralty Islands','Bougainville and Solomon Islands','Santa Cruz Islands','Vanuatu','Fiji Islands','Tonga Islands','Samoan and Wallis Islands','Pacific Ocean (central)','Pacific Ocean (southwestern)','Galapagos Islands','Pacific Ocean (eastern)'}
partly={'Lesser Sunda Islands','Northern Chile, Bolivia and Argentina','Peru','Africa (eastern)','Africa (northeastern) and Red Sea','Indian Ocean (western)','Izu, Volcano, and Mariana Islands','Andaman Islands','Hawaiian Islands','Southeast Asia','Middle East (southern)','Africa (central)','Africa (western)','Africa (northern)','Cape Verde Islands','Atlantic Ocean (central)'}
t=v[v.Latitude.abs()<=25].copy()
rows=[]
for _,r in t.iterrows():
    ee=e[e['Volcano Number']==r['Volcano Number']]
    cov=ee[(ee['Start Year']-ee.unc<=1811)&(ee['Start Year']+ee.unc>=1806)]
    cov_nh=cov[~hist.loc[cov.index]] if len(cov) else cov
    cov_h=cov[hist.loc[cov.index]] if len(cov) else cov
    h1700=ee[hist.loc[ee.index]&(ee['Start Year']>=1700)&(ee['Start Year']<=1900)]
    first_hist=ee[hist.loc[ee.index]]['Start Year'].min()
    zone='blank' if r.Subregion in blank else ('partly watched' if r.Subregion in partly else 'watched (records read, negative)')
    rock=str(r['Dominant Rock Type'])
    evolved=any(k in rock for k in ['Andesite','Dacite','Rhyolite','Trachyte','Trachyandesite'])
    nh=';'.join(f"{int(a)}±{int(b)} {m} VEI{'' if np.isnan(c) else int(c)}" for a,b,m,c in zip(cov_nh['Start Year'],cov_nh.unc,cov_nh['Evidence Method (dating)'],cov_nh.VEI))
    hh=';'.join(f"{int(a)} VEI{'' if np.isnan(c) else int(c)} {s}" for a,c,s in zip(cov_h['Start Year'],cov_h.VEI,cov_h['Eruption Category']))
    lk=str(r['Last Known Eruption']); lky=int(lk.split()[0]) if lk.endswith('CE') and lk.split()[0].isdigit() else None
    if not nh and not hh and lky and 1790<=lky<=1830: nh=f'last known eruption {lk} (no eruption row in this GVP snapshot)'
    tier='A' if nh else ('B' if (zone=='blank' and evolved and len(h1700)==0) else ('C' if zone=='blank' else ''))
    if hh and not nh: tier=tier or 'H'
    if pd.notna(r['Elevation (m)']) and r['Elevation (m)']< -200: tier='X'
    rows.append(dict(tier=tier,volcano=r['Volcano Name'],gvp_number=r['Volcano Number'],country=r.Country,subregion=r.Subregion,zone=zone,lat=r.Latitude,lon=r.Longitude,elev_m=r['Elevation (m)'],type=r['Primary Volcano Type'],dominant_rock=rock,evolved_rock=evolved,last_known_eruption=r['Last Known Eruption'],first_eruption_dated_by_historical_observation=('' if np.isnan(first_hist) else int(first_hist)),historical_eruptions_1700_1900=len(h1700),undated_or_proxy_dated_eruption_covering_1806_1811=nh,historical_eruption_covering_1806_1811=hh))
df=pd.DataFrame(rows)
order={'A':0,'B':1,'H':2,'C':3,'':4,'X':5}
df['o']=df.tier.map(order); df=df.sort_values(['o','zone','subregion','volcano']).drop(columns='o')
df.to_csv(OUT,index=False)
print(df.tier.value_counts().to_string())
pd.set_option('display.width',250)
print(df[df.tier=='A'][['volcano','country','zone','dominant_rock','undated_or_proxy_dated_eruption_covering_1806_1811']].to_string())
print(df[df.tier=='H'][['volcano','country','zone','historical_eruption_covering_1806_1811']].to_string())
print(df[df.tier=='B'][['volcano','subregion','dominant_rock','last_known_eruption','first_eruption_dated_by_historical_observation']].to_string())
