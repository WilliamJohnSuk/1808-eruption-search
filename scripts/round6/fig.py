import pandas as pd, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
g=pd.read_csv('/tmp/claude-0/work/eeic_tropical_monthly.csv')
g['t']=g.yr+(g.mo-0.5)/12
s=g[(g.yr>=1805)&(g.yr<=1819)]
fig,ax=plt.subplots(figsize=(10,4.2))
ax.axhline(0,color='#888',lw=0.8)
ok=s.ships>=5
ax.errorbar(s.t[ok],s.anom[ok],yerr=s.se[ok],fmt='o-',ms=3,lw=1,color='#2a5d9f',ecolor='#9bb7dd',label='EIC ships, 30°S–30°N, monthly mean (≥5 ships)')
ax.plot(s.t[~ok],s.anom[~ok],'x',color='#999',label='<5 ships')
for x,l in [(1808+11.35/12,'Bogotá veil\n11 Dec 1808'),(1815+3.3/12,'Tambora\n10 Apr 1815')]:
    ax.axvline(x,color='#c0392b',ls='--',lw=1); ax.text(x+0.05,1.0,l,fontsize=8,color='#c0392b',va='top')
ax.set_ylim(-2,1.2); ax.set_xlim(1805,1819.5)
ax.set_ylabel('Marine air temperature anomaly (°C)'); ax.set_title('East India Company logbooks: tropical marine air temperature, monthly (oldweather/EEIC)')
ax.legend(fontsize=8,loc='lower left'); fig.tight_layout()
fig.savefig('/mnt/project-files/1808-eruption/data/eic_tropical_air_temp_monthly_1805-1819.png',dpi=130)
