import csv, math, statistics as st
MEL=(-74.35,164.70); PLE=(-72.67,165.50)
def dist(a,b):
    la1,lo1,la2,lo2=map(math.radians,(a[0],a[1],b[0],b[1]))
    return 6371*math.acos(min(1,math.sin(la1)*math.sin(la2)+math.cos(la1)*math.cos(la2)*math.cos(lo1-lo2)))
T="text of the published table read through a web-fetch text extraction (not checked against the page image)"
P="PDF text layer of the published table (pdftotext; William's copy), not checked against the page image"
rows=[
# region, site, core, lat, lon, f1809, f1815, source, verification, note
("Antarctica","WAIS Divide","WDC06A",-79.47,-112.09,33.8,88.6,"Sigl et al. 2013 JGR 118, Table 1-2",T,""),
("Antarctica","WAIS Divide","WDC05Q",-79.47,-112.08,48.4,92.1,"Sigl et al. 2013 JGR 118, Table 2",T,""),
("Antarctica","WAIS Divide","WDC (Cole-Dai)",-79.47,-112.09,41,81,"Cole-Dai et al. 2009 GRL 36 L22703, Table 2",P,"probably the WDC05 shallow core; not independent of WDC05Q"),
("Antarctica","South Pole","SP01",-89.95,17.67,29,66,"Budner & Cole-Dai 2003 via Cole-Dai et al. 2009 Table 2",P,"Nardin 2020 Table 4 gives 28.04 / 64.01"),
("Antarctica","South Pole","SP04",-89.95,17.67,23.1,26.3,"Ferris et al. 2011 via Sigl et al. 2013 Table 2 and Nardin et al. 2020 Table 4",T,"Tambora unusually low for South Pole; ratio unreliable"),
("Antarctica","South Pole","PS1",-90.0,0.0,32,67.6,"Delmas et al. 1992 via Nardin et al. 2020 Table 4",T,""),
("Antarctica","South Pole","PS14",-90.0,0.0,29.8,72.3,"Delmas et al. 1992 via Nardin et al. 2020 Table 4",T,""),
("Antarctica","Siple Station","SI85",-75.92,-84.25,53,129,"Dai et al. 1991 JGR 96, Table 1",T,"Cole-Dai 2009 repeats 53/129; Nardin gives 54/133"),
("Antarctica","Dyer Plateau","DY89",-70.67,-64.87,54,90,"Cole-Dai et al. 1997 via Cole-Dai et al. 2009 Table 2",P,""),
("Antarctica","Byrd Station","Byrd",-80.02,-119.52,11,24,"Langway et al. 1994 via Nardin et al. 2020 Table 4",T,""),
("Antarctica","Law Dome","DSS (Plummer)",-66.77,112.80,24.6,57.2,"Plummer et al. 2012 Clim. Past 8, Table 2",T,"Sigl 2013 cites 25.2/58.4"),
("Antarctica","Law Dome","Law Dome (Palmer)",-66.77,112.80,45,80,"Palmer et al. 2001 via Cole-Dai et al. 2009 Table 2",P,"older Law Dome cores; same site as DSS"),
("Antarctica","Plateau Remote","PR",-84.0,43.0,8.3,22,"Cole-Dai et al. 2000 via Cole-Dai et al. 2009 Table 2",P,""),
("Antarctica","Dome C","EDC96",-75.10,123.35,10.2,39.3,"Castellano et al. 2005 JGR 110, Table 1",T,"Cole-Dai 2009 repeats 10.2/39"),
("Antarctica","Dronning Maud Land","DML05 (B32)",-75.00,0.01,15.4,32.5,"Traufetter et al. 2004 via Sigl 2013 and Nardin 2020 Table 4",T,""),
("Antarctica","Dronning Maud Land","DML07",-75.58,3.43,27.5,54.6,"Traufetter et al. 2004 via Nardin et al. 2020 Table 4",T,""),
("Antarctica","Dronning Maud Land","DML17",-75.17,7.0,24.6,49.8,"Traufetter et al. 2004 via Nardin et al. 2020 Table 4",T,"coordinates approximate"),
("Antarctica","Dronning Maud Land","DML03",-74.5,3.0,35.8,47.3,"Traufetter et al. 2004 via Nardin et al. 2020 Table 4",T,"coordinates approximate"),
("Antarctica","Dome A","DA2005 (Jiang)",-80.37,77.37,12.04,17.84,"Jiang et al. 2012 via Nardin et al. 2020 Table 4",T,"very low accumulation"),
("Antarctica","Dome A","DA2009",-80.42,77.12,26.71,11.89,"An et al. 2026 EGUsphere preprint egusphere-2026-769, Table 1",T,"preprint; a referee doubts the Tambora identification at this core; excluded from summary statistics"),
("Antarctica","Northern Victoria Land","GV7",-70.68,158.87,23.32,41.12,"Nardin et al. 2020 Geosciences 10:38, Tables 2 and 4",T,"coastal, about 470 km from Mt Melbourne"),
("Antarctica","Northern Victoria Land (Talos Dome)","TD96",-72.80,159.10,44.46,42.31,"Nardin et al. 2020 Geosciences 10:38, Table 2",T+"; core assignment inferred by Claude: the GV7-ITASE core (55 m, c. 150 yr) cannot reach 1809, so the two values are TD96 and TALDICE, in table column order","CHECK AGAINST PAGE IMAGE"),
("Antarctica","Northern Victoria Land (Talos Dome)","TALDICE",-72.82,159.18,38.32,34.44,"Nardin et al. 2020 Geosciences 10:38, Table 2",T+"; core assignment inferred by Claude (see TD96)","CHECK AGAINST PAGE IMAGE"),
("Antarctica","Siple Dome","SDMA",-81.65,-148.81,None,None,"Kurbatov et al. 2006 JGR 111 D12307",P,"Tambora missed (fractured ice); 1809 sulfate present with trachytic tephra matched to the Pleiades or Mt Melbourne; no flux ratio possible"),
("Greenland","Summit","SU07",72.6,-38.5,36,59,"Cole-Dai et al. 2009 Table 2",P,""),
("Greenland","Site T","ST89",72.58,-38.45,28,47,"Dai et al. 1991 Table 1",T,""),
("Greenland","GITS","GITS",77.14,-61.04,33,48,"via Cole-Dai et al. 2009 Table 2",P,""),
("Greenland","D3","D3",65.18,-43.83,47,85,"via Cole-Dai et al. 2009 Table 2",P,"coordinates assume Dye 3; check"),
("Greenland","NEEM","NEEM-2011-S1",77.45,-51.06,30.6,39.0,"Sigl et al. 2013 Table 1",T,""),
("Greenland","NorthGRIP","NGRIP",75.10,-42.32,38.6,40.3,"Plummer et al. 2012 Table 2",T,""),
]
out=[]
for r in rows:
    reg,site,core,lat,lon,a,b,src,ver,note=r
    ratio=round(a/b,2) if a and b else ""
    dm=round(dist((lat,lon),MEL)) if reg=="Antarctica" else ""
    dp=round(dist((lat,lon),PLE)) if reg=="Antarctica" else ""
    out.append(dict(region=reg,site=site,core=core,lat=lat,lon=lon,flux_1809_kg_km2=a if a else "",flux_tambora_kg_km2=b if b else "",
        ratio_1809_to_tambora_claude_calc=ratio,dist_mt_melbourne_km_claude_calc=dm,dist_pleiades_km_claude_calc=dp,source=src,verification=ver,note=note))
f="/mnt/project-files/1808-eruption/data/antarctic_sulfate_1809_vs_tambora.csv"
with open(f,"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for o in out: print(o["core"],o["ratio_1809_to_tambora_claude_calc"],o["dist_mt_melbourne_km_claude_calc"])
# stats
indep=["WDC06A","SP01","PS1","PS14","SI85","DY89","Byrd","DSS (Plummer)","PR","EDC96","DML05 (B32)","DML07","DML17","DML03","DA2005 (Jiang)"]
r=[o["ratio_1809_to_tambora_claude_calc"] for o in out if o["core"] in indep]
print("Antarctic non-VL n",len(r),"mean",round(st.mean(r),3),"median",st.median(r),"sd",round(st.stdev(r),3),"min",min(r),"max",max(r))
g=[o["ratio_1809_to_tambora_claude_calc"] for o in out if o["region"]=="Greenland"]
print("Greenland n",len(g),"mean",round(st.mean(g),3),"sd",round(st.stdev(g),3))
m=st.mean(r);s=st.stdev(r)
for c in ["GV7","TD96","TALDICE"]:
    v=[o for o in out if o["core"]==c][0]; x=v["ratio_1809_to_tambora_claude_calc"]
    print(c,x,"z",round((x-m)/s,2),"excess flux if expected ratio=mean:",round(v["flux_1809_kg_km2"]-m*v["flux_tambora_kg_km2"],1))
