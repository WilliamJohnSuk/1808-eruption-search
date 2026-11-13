import csv, math, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
rows=[r for r in csv.DictReader(open("/mnt/project-files/1808-eruption/data/antarctic_sulfate_1809_vs_tambora.csv")) if r["region"]=="Antarctica" and r["ratio_1809_to_tambora_claude_calc"]]
fig=plt.figure(figsize=(8,8)); ax=fig.add_subplot(111,projection="polar")
ax.set_theta_zero_location("S"); ax.set_theta_direction(1)  # lon 0 at bottom, east counter-clockwise
ax.set_rlim(0,26); ax.set_yticks([5,10,15,20,25]); ax.set_yticklabels(["85°S","80°S","75°S","70°S","65°S"],fontsize=8)
ax.set_xticks([math.radians(a) for a in range(0,360,30)]); ax.set_xticklabels([f"{a}°E" if a<=180 else f"{360-a}°W" for a in range(0,360,30)],fontsize=8)
seen={}
for r in rows:
    lat,lon,ratio=float(r["lat"]),float(r["lon"]),float(r["ratio_1809_to_tambora_claude_calc"])
    th=math.radians(lon%360); rr=90+lat
    site=r["site"].replace("Northern Victoria Land (Talos Dome)","Talos Dome").replace("Northern Victoria Land","GV7")
    seen.setdefault(site,[]).append((th,rr,ratio))
    flag="DA2009" in r["core"] or "SP04" in r["core"]
    sc=ax.scatter(th,rr,c=[min(ratio,1.2)],cmap="RdYlBu_r",vmin=0.2,vmax=1.2,s=110,edgecolors="k" if not flag else "grey",linewidths=0.8,marker="o" if not flag else "s",zorder=3)
offs={"Talos Dome":(10,-14),"GV7":(10,4),"South Pole":(8,8),"Dome A":(10,-4),"Law Dome":(-150,-16)}
for site,v in seen.items():
    th,rr,_=v[0]; rs=sorted(x[2] for x in v)
    lab=f"{site} {rs[0]:.2f}" if len(rs)==1 else f"{site} ({len(rs)} cores) "+", ".join(f"{x:.2f}" for x in rs)
    ax.annotate(lab,(th,rr),xytext=offs.get(site,(8,-12)),textcoords="offset points",fontsize=7.5)
for name,(lat,lon) in {"Mt Melbourne":(-74.35,164.70),"Pleiades":(-72.67,165.5)}.items():
    ax.scatter(math.radians(lon),90+lat,marker="^",c="k",s=60,zorder=4); ax.annotate(name,(math.radians(lon),90+lat),xytext=(6,4),textcoords="offset points",fontsize=7,fontweight="bold")
cb=fig.colorbar(sc,ax=ax,shrink=0.6,pad=0.08); cb.set_label("1809 flux / Tambora flux (same core)")
ax.set_title("1809 sulfate relative to Tambora, per Antarctic core\n(Claude's compilation and calculation from published fluxes; squares = doubtful values)",fontsize=10)
plt.savefig("/mnt/project-files/1808-eruption/data/antarctic_sulfate_1809_vs_tambora_map.png",dpi=130,bbox_inches="tight")
