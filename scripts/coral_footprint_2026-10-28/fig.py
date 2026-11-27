import json, csv, math, statistics as st, sys
from collections import defaultdict
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
SURF='#fcfcfb'; INK='#0b0b0b'; INK2='#52514e'; MUTED='#898781'; GRID='#e1e0d9'; BASE='#c3c2b7'
S1,S2,S3='#2a78d6','#eb6834','#1baf7a'
jsonp, extp, out = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(jsonp)); cols = list(d.keys()); idx = list(d[cols[0]].keys())
recs = {}
for i in idx:
    r={c: d[c][i] for c in cols}; recs[r['dataSetName']+'|'+r['paleoData_variableName']]=r
def fl(x):
    try: return float(x)
    except: return float('nan')
def pts(r):
    return sorted([(a,b) for a,b in zip(map(fl,r['year']),map(fl,r['paleoData_values'])) if not (math.isnan(a) or math.isnan(b))])
def make_month(times):
    # Corrected 27 Nov 2026 (from the ChatGPT handoff): nearest-month binning for records on a
    # start-of-month grid with two-decimal dates; floor rule kept for mid-month or irregular grids.
    fr=[(a*12)%1 for a in times]
    if fr and all(min(f,1-f)<0.1 for f in fr): return lambda a: int(round(a*12))%12
    return lambda a: min(11, int(math.floor((a - math.floor(a))*12 + 1e-9)))
month=None
def monthly_z(r, lo=1790, hi=1831):
    global month
    p=pts(r); by=defaultdict(list); month=make_month([a for a,b in p])
    for a,b in p:
        if lo<=a<hi: by[month(a)].append(b)
    clim={m:st.mean(x) for m,x in by.items()}
    sd=st.pstdev([b-clim[month(a)] for a,b in p if lo<=a<hi])
    return [(a,(b-clim[month(a)])/sd) for a,b in p]
def jj_year(z):
    jj=defaultdict(list)
    for a,v in z:
        m=month(a); y=math.floor(a); jj[y if m>=6 else y-1].append(v)
    return {y:st.mean(x) for y,x in jj.items() if len(x)>=6}
def annual_z(r, lo=1790, hi=1831):
    p=pts(r); base=[b for a,b in p if lo<=a<hi]; mu,sd=st.mean(base),st.pstdev(base)
    return {int(math.floor(a+1e-6)):(b-mu)/sd for a,b in p}
ext=defaultdict(dict)
for row in csv.DictReader(open(extp)):
    ext[row['series']][float(row['year'])]=float(row['value'])
X0,X1=1804.5,1818.5
fig,axs=plt.subplots(3,2,figsize=(14,10.5),facecolor=SURF); axs=axs.ravel()
def style(ax,title,ylabel,base=0):
    ax.set_facecolor(SURF); ax.set_xlim(X0,X1)
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(BASE)
    ax.grid(True,axis='y',color=GRID,linewidth=0.6); ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED,length=0,labelsize=8.5)
    ax.set_xticks(range(1805,1819,2)); ax.set_xticklabels([str(y) for y in range(1805,1819,2)])
    ax.axhline(base,color=BASE,linewidth=0.8)
    ax.set_title(title,loc='left',fontsize=10.5,color=INK,weight='bold',pad=10)
    ax.set_ylabel(ylabel,color=INK2,fontsize=8.5)
    for x,lab in [(1808.92,'inferred eruption\nNov-Dec 1808'),(1815.3,'Tambora\nApr 1815')]:
        ax.axvline(x,color=MUTED,linewidth=0.8)
        ax.text(x+0.1,ax.get_ylim()[1] if False else 0,'',fontsize=7)
def vlabels(ax):
    y1=ax.get_ylim()[1]
    ax.text(1808.92+0.12,y1,'inferred eruption\nNov-Dec 1808',fontsize=7.5,color=INK2,va='top')
    ax.text(1815.3+0.12,y1,'Tambora\nApr 1815',fontsize=7.5,color=INK2,va='top')
def endlabel(ax,xs,ys,text,color,dy=0):
    ax.text(xs[-1]+0.15,ys[-1]+dy,text,fontsize=8.5,color=INK2,va='center')
# (a) Lombok monthly
ax=axs[0]; z=monthly_z(recs['Ocn-Lombok.Charles.2003|d18O']); xs=[a for a,v in z if X0<=a<=X1]; ys=[v for a,v in z if X0<=a<=X1]
ax.plot(xs,ys,color=S1,linewidth=1.8); style(ax,'a. Lombok Strait, 13 km from Agung: monthly δ18O anomaly','sd (positive = cooler / drier)'); ax.set_ylim(-3,4.5); vlabels(ax)
ax.annotate('Dec 1808 +2.1',xy=(1808.92,2.12),xytext=(1806.2,3.6),fontsize=8,color=INK2,arrowprops=dict(arrowstyle='-',color=MUTED,lw=0.8))
ax.annotate('Mar 1811 +4.1',xy=(1811.17,4.08),xytext=(1811.6,4.1),fontsize=8,color=INK2)
# (b) Palau and Guam monthly
ax=axs[1]
for key,col,name,dy in [('Ocn-PalauUlongChannel.Osborne.2014|d18O',S1,'Palau 7°N',0.3),('Ocn-DoubleReef.Asami.2005|d18O',S2,'Guam 14°N',-0.3)]:
    z=monthly_z(recs[key]); xs=[a for a,v in z if X0<=a<=X1]; ys=[v for a,v in z if X0<=a<=X1]
    ax.plot(xs,ys,color=col,linewidth=1.6,label=name)
style(ax,'b. Palau and Guam: monthly δ18O anomaly','sd (positive = cooler / drier)'); ax.set_ylim(-3,4.5); vlabels(ax); ax.legend(frameon=False,fontsize=8.5,loc='upper left',bbox_to_anchor=(0,-0.13),ncol=3,labelcolor=INK2,handlelength=2.2,columnspacing=1.6)
# (c) SW Pacific annual: Vanuatu (baseline 1807-1899), Fiji mean of 4, New Caledonia Sr/Ca Jul-Jun
ax=axs[2]
van=annual_z(recs['Ocn-Vanuatu.Quinn.1996|d18O'],1807,1900)
fiji_keys=['Ocn-SavusavuBayAB.Linsley.2006|d18O','Ocn-SavusavuBay1F.Linsley.2006|d18O','Ocn-SavusavuBay1F.Linsley.2006|Sr_Ca','Ocn-SavusavuBayFiji.Bagnato.2005|d18O']
fz=[annual_z(recs[k]) for k in fiji_keys]
fiji={y:st.mean([f[y] for f in fz if y in f]) for y in range(1800,1825)}
nc=jj_year(monthly_z(recs['Ocn-AmedeeIsland.DeLong.2012|Sr_Ca']))
for ser,col,name in [(van,S1,'Espiritu Santo, Vanuatu (98 km from Gaua)'),(fiji,S2,'Fiji, mean of 4 records'),(nc,S3,'New Caledonia Sr/Ca')]:
    ys_=sorted(y for y in ser if 1805<=y<=1818); ax.plot(ys_,[ser[y] for y in ys_],color=col,linewidth=1.8,marker='o',markersize=4.5,markeredgecolor=SURF,markeredgewidth=1,label=name)
style(ax,'c. South-west Pacific, annual (New Caledonia: July-June years)','sd (positive = cooler / drier)'); ax.set_ylim(-3,3); vlabels(ax); ax.legend(frameon=False,fontsize=8.5,loc='upper left',bbox_to_anchor=(0,-0.13),ncol=3,labelcolor=INK2,handlelength=2.2,columnspacing=1.6)
# (d) Abraham Reef, Malindi, Galapagos
ax=axs[3]
for key,col,name in [('Ocn-AbrahamReef.Druffel.1999|d18O',S1,'Abraham Reef, Coral Sea 22°S'),('Ocn-Malindi.Cole.2000|d18O',S2,'Malindi, Kenya 3°S'),('Ocn-UrvinaBay.Dunbar.1994|d18O',S3,'Galápagos')]:
    ser=annual_z(recs[key]); ys_=sorted(y for y in ser if 1805<=y<=1818)
    ax.plot(ys_,[ser[y] for y in ys_],color=col,linewidth=1.8,marker='o',markersize=4.5,markeredgecolor=SURF,markeredgewidth=1,label=name)
style(ax,'d. Coral Sea, western Indian Ocean, eastern Pacific, annual','sd (positive = cooler / drier)'); ax.set_ylim(-3,3); vlabels(ax); ax.legend(frameon=False,fontsize=8.5,loc='upper left',bbox_to_anchor=(0,-0.13),ncol=3,labelcolor=INK2,handlelength=2.2,columnspacing=1.6)
# (e) Tierney regional SST
ax=axs[4]
for ser,col,name in [('Tierney2015_WPacific_SST',S1,'Western Pacific'),('Tierney2015_Indian_SST',S2,'Indian Ocean'),('Tierney2015_EPacific_SST',S3,'Eastern Pacific')]:
    s=ext[ser]; ys_=sorted(y for y in s if 1805<=y<=1818); ax.plot(ys_,[s[y] for y in ys_],color=col,linewidth=1.8,marker='o',markersize=4.5,markeredgecolor=SURF,markeredgewidth=1,label=name)
style(ax,'e. Ocean2k coral SST reconstructions (Tierney et al. 2015), April-March years','°C vs 1961-1990'); ax.set_ylim(-1.5,0.6); vlabels(ax); ax.legend(frameon=False,fontsize=8.5,loc='upper left',bbox_to_anchor=(0,-0.13),ncol=3,labelcolor=INK2,handlelength=2.2,columnspacing=1.6)
# (f) Lough Queensland rainfall
ax=axs[5]; s=ext['Lough2007_Queensland_rainfall']; ys_=sorted(y for y in s if 1805<=y<=1818)
ax.plot(ys_,[s[y] for y in ys_],color=S1,linewidth=1.8,marker='o',markersize=4.5,markeredgecolor=SURF,markeredgewidth=1)
style(ax,'f. Queensland rainfall from GBR coral luminescence (Lough 2007), Oct-Sep years','% of mean',base=100); ax.set_ylim(70,135); vlabels(ax)
fig.text(0.02,0.975,'The 1809-1812 excursion in Indo-Pacific corals, 1805-1818',fontsize=14,color=INK,weight='bold')
fig.text(0.02,0.955,"Panels a-d: anomalies in standard deviations from the 1790-1830 climatology (Vanuatu: 1807-1899), raw proxy sign, so higher δ18O or Sr/Ca = cooler and/or saltier (drier). Panel e: Ocean2k regional SST in °C. Panel f: rainfall as % of mean.",fontsize=8.5,color=INK2)
fig.text(0.02,0.937,"Monthly series use decimal years; annual values are plotted at the calendar year. Claude's calculation from PAGES2k v2 (mirror fzhu2e/cfr-data) and NOAA/NCEI data files, 28 Oct 2026 (Lombok and Palau month binning corrected 27 Nov 2026, found by ChatGPT); tables in data/, note coral_footprint_1809-12_2026-10-28.md.",fontsize=8.5,color=INK2)
fig.subplots_adjust(left=0.05,right=0.985,top=0.89,bottom=0.06,hspace=0.62,wspace=0.15)
fig.savefig(out,dpi=150,facecolor=SURF); print('saved',out)
