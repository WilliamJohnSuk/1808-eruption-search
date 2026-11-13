import json, csv, math, statistics as st, sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly, Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.lines import Line2D
SURF='#fcfcfb'; INK='#0b0b0b'; INK2='#52514e'; MUTED='#898781'; GRID='#e1e0d9'; BASE='#c3c2b7'
BLUE=['#86b6ef','#3987e5','#184f95']; RED=['#ea9a93','#d75853','#892b2a']; NEUT='#c3c2b7'
csvp, geop, out = sys.argv[1], sys.argv[2], sys.argv[3]
CUT=25
def shift(lon): return lon if lon>=CUT else lon+360
gj=json.load(open(geop)); patches=[]
for f in gj['features']:
    g=f['geometry']
    rings = [g['coordinates'][0]] if g['type']=='Polygon' else [p[0] for p in g['coordinates']]
    for ring in rings:
        xs=[shift(x) for x,y in ring]; ys=[y for x,y in ring]
        if max(xs)-min(xs)>180: xs=[x-360 if x>CUT+180 else x for x in xs]
        patches.append(MPoly(list(zip(xs,ys)), closed=True))
rows=list(csv.DictReader(open(csvp)))
# aggregate by site (sub-annual and annual records only; sign-bearing)
sites={}
for r in rows:
    if r['cool_dry_sign']=='' or r['mean_1809_12'] in ('', 'nan') or '-yr' in r['resolution']: continue
    key=(round(float(r['lat']),1), round(float(r['lon']),1))
    sites.setdefault(key, []).append(float(r['mean_1809_12'])*int(r['cool_dry_sign']))
def cls(v):
    if v>=1: return BLUE[2]
    if v>=0.5: return BLUE[1]
    if v>=0.25: return BLUE[0]
    if v>-0.25: return NEUT
    if v>-0.5: return RED[0]
    if v>-1: return RED[1]
    return RED[2]
NAMES={(-8.2,115.6):'Lombok Strait',(7.3,134.3):'Palau',(13.6,144.8):'Guam',(-15.0,167.0):'Espiritu Santo, Vanuatu',(-16.8,179.2):'Fiji (4 records)',(-22.5,166.5):'New Caledonia',(-22.1,153.0):'Abraham Reef',(-21.2,-159.8):'Rarotonga',(-19.9,-174.7):'Tonga',(-0.4,-91.2):'Galápagos',(8.0,-82.0):'Panama',(-3.2,40.1):'Malindi',(-23.2,43.6):'Ifaty, Madagascar',(-28.5,113.8):'Houtman Abrolhos',(27.8,34.3):'Red Sea',(29.4,35.0):'Aqaba',(17.9,-67.0):'Puerto Rico',(30.6,-65.0):'Bermuda',(25.4,-80.2):'Biscayne Bay',(24.6,-82.3):'Dry Tortugas'}
fig=plt.figure(figsize=(15,7.2), facecolor=SURF); ax=fig.add_axes([0.03,0.26,0.94,0.62])
ax.set_facecolor(SURF)
ax.add_collection(PatchCollection(patches, facecolor=GRID, edgecolor=BASE, linewidth=0.4))
ax.set_xlim(CUT, CUT+280); ax.set_ylim(-45,45); ax.set_aspect('equal')
for s in ax.spines.values(): s.set_visible(False)
ax.set_xticks(range(30,306,30)); ax.set_xticklabels([f"{x}°E" if x<=180 else f"{360-x}°W" for x in range(30,306,30)], color=MUTED, fontsize=8)
ax.set_yticks(range(-40,41,20)); ax.set_yticklabels([f"{abs(y)}°{'S' if y<0 else 'N' if y>0 else ''}" for y in range(-40,41,20)], color=MUTED, fontsize=8)
ax.tick_params(length=0); ax.grid(True, color=GRID, linewidth=0.6)
ax.axhline(0, color=BASE, linewidth=0.6)
# D'Arrigo warm pool box
ax.add_patch(Rectangle((110,-15),50,20, fill=False, edgecolor=MUTED, linewidth=0.8))
ax.text(111.5,3.2,"warm-pool box of D'Arrigo et al. 2006", fontsize=7.5, color=MUTED, va='center')
# volcanoes
volc={'Dakataua':(-5.06,150.11),'Gaua':(-14.27,167.50),'Cabalían':(10.29,125.22),'Agung':(-8.34,115.51),'Tambora (1815)':(-8.25,118.0)}
for n,(la,lo) in volc.items():
    ax.scatter([shift(lo)],[la], marker='^', s=70, facecolor=INK, edgecolor=SURF, linewidth=1.2, zorder=5)
off={'Dakataua':(4,3),'Gaua':(4,3.5),'Cabalían':(4,2),'Agung':(-4,4.5),'Tambora (1815)':(5,-5.5)}
for n,(la,lo) in volc.items():
    dx,dy=off[n]; ax.text(shift(lo)+dx, la+dy, n, fontsize=8, color=INK, ha='left' if dx>0 else 'right', va='center', zorder=6)
# coral sites
for (la,lo),vals in sites.items():
    v=st.mean(vals)
    ax.scatter([shift(lo)],[la], s=150, facecolor=cls(v), edgecolor=SURF, linewidth=1.6, zorder=4)
lab_off={(-8.2,115.6):(-3,-6,'right'),(7.3,134.3):(4,3,'left'),(13.6,144.8):(4,3,'left'),(-15.0,167.0):(-4,-5.5,'right'),(-16.8,179.2):(5,4,'left'),(-22.5,166.5):(3,-6,'left'),(-22.1,153.0):(-4,-6,'right'),(-21.2,-159.8):(4,-5,'left'),(-19.9,-174.7):(4,-4.5,'left'),(-0.4,-91.2):(4,-4,'left'),(8.0,-82.0):(4,3,'left'),(-3.2,40.1):(4,3,'left'),(-23.2,43.6):(4,-5,'left'),(-28.5,113.8):(4,-5,'left'),(27.8,34.3):(4,-5,'left'),(29.4,35.0):(4,3.5,'left'),(17.9,-67.0):(-4,-5,'right'),(30.6,-65.0):(4,3,'left'),(25.4,-80.2):(4,3,'left'),(24.6,-82.3):(-4,-5,'right')}
VAL={(-8.2,115.6),(-15.0,167.0),(-16.8,179.2),(-22.1,153.0),(-3.2,40.1),(-0.4,-91.2),(17.9,-67.0)}
for key,vals in sites.items():
    la,lo=key; v=st.mean(vals); dx,dy,ha=next((v for k,v in lab_off.items() if abs(k[0]-la)<0.3 and abs(k[1]-lo)<0.3),(4,3,'left'))
    txt=next((n for k,n in NAMES.items() if abs(k[0]-la)<0.3 and abs(k[1]-lo)<0.3),'')
    if key in VAL: txt+=f"  {v:+.1f} sd"
    ax.text(shift(lo)+dx, la+dy, txt, fontsize=8, color=INK2, ha=ha, va='center', zorder=6)
fig.text(0.03,0.95,"Coral records of 1809-1812: cool and dry across the Indo-Pacific, strongest at Lombok", fontsize=14, color=INK, weight='bold')
fig.text(0.03,0.905,"Mean anomaly for July 1809 to June 1813 (monthly records) or 1809-1812 (annual records), in standard deviations from the 1790-1830 climatology. δ18O and Sr/Ca; positive = cooler and/or saltier (drier). "
         "20 sites, 27 records, PAGES2k v2 corals.", fontsize=9, color=INK2)
# legend row
labels=[('≤ −1','warmer / wetter',RED[2]),('−1 to −0.5','',RED[1]),('−0.5 to −0.25','',RED[0]),('within ±0.25','',NEUT),('+0.25 to +0.5','',BLUE[0]),('+0.5 to +1','',BLUE[1]),('≥ +1 sd','cooler / drier',BLUE[2])]
x0=0.05
for i,(l,sub,c) in enumerate(labels):
    x=x0+i*0.105
    fig.patches.append(plt.Circle((x,0.165),0.0075,transform=fig.transFigure,facecolor=c,edgecolor=SURF,linewidth=1.6))
    fig.text(x+0.012,0.165,l,fontsize=8.5,color=INK2,va='center')
    if sub: fig.text(x+0.012,0.14,sub,fontsize=8,color=MUTED,va='center')
fig.text(x0+7*0.105+0.005,0.165,"▲  candidate volcano (B53) and Tambora",fontsize=8.5,color=INK2,va='center')
fig.text(0.03,0.10,"Omitted: five-year records (Arlington Reef and Flinders Reef, GBR; Hendy 2002) and two calcification records; Palmyra, Mafia and Bunaken have no data for 1809-12. Vanuatu record begins 1807, baseline 1807-1856.", fontsize=8, color=MUTED)
fig.text(0.03,0.075,"Coral chronologies carry an error of several months in any year (Charles et al. 2003) that can reach a year; values at a single site are a hint, the pattern across sites is the finding.", fontsize=8, color=MUTED)
fig.text(0.03,0.045,"Claude's calculation from PAGES2k v2 (Emile-Geay et al. 2017; mirror github.com/fzhu2e/cfr-data), 28 Oct 2026. Table: data/coral_footprint_1800-1820_2026-10-28.csv. Coastlines: Natural Earth via johan/world.geo.json.", fontsize=8, color=MUTED)
fig.savefig(out, dpi=170, facecolor=SURF)
print('saved', out, len(sites), 'sites')
