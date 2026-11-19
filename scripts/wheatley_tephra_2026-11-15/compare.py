"""Extract and compare the Kurbatov 2017 / Wheatley tephra shards (USAP-DC 601038).

Usage: python3 compare.py SDWheatley_tephra-data.xlsx out.csv [data/glass_candidates.csv]
Writes every shard row to out.csv, prints group means, and prints Borchardt similarity
coefficients (Claude's calculation, not checked by a person) against the 1809 ice glass,
Tambora 1815 and candidate glasses. The xlsx is not in the repo: get it from doi:10.15784/601038.
"""
import openpyxl,csv,statistics as st,sys
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
rows=[]
for s in ['1991 C.E. Tephra','1963 C.E. Tephra','1815 C.E. Tephra','1809 C.E. Tephra','1257 C.E. Tephra']:
  for r in wb[s].iter_rows(min_row=2,values_only=True):
    if r[0] and str(r[0]).startswith('IESDW'):
      rows.append([s.split()[0]]+list(r[:14]))
with open(sys.argv[2],'w',newline='') as f:
  w=csv.writer(f); w.writerow(['interval_CE','IGSN','core','AntT_ID','particle_size_um','n_points','SiO2','TiO2','Al2O3','FeO','MgO','CaO','Na2O','K2O','total'])
  for r in rows: w.writerow([r[0]]+[round(x,2) if isinstance(x,float) else x for x in r[1:]])
ox=['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O']
idx=[6,8,9,10,11,12,13]  # in rows (offset 1)
def m(sel): return [st.mean(r[i] for r in sel) for i in idx]
def sd(sel): return [st.pstdev(r[i] for r in sel) for i in idx]
g={}
g['W1809_all']=[r for r in rows if r[0]=='1809']
g['W1809_WDC']=[r for r in g['W1809_all'] if r[2]=='WDC-06A']
g['W1809_SPRESSO']=[r for r in g['W1809_all'] if r[2]=='SPRESSO']
g['W1815_all']=[r for r in rows if r[0]=='1815']
for k,v in g.items(): print(k,len(v),[f'{a:.2f}±{b:.2f}' for a,b in zip(m(v),sd(v))])
ice={'DomeC_1809':[59.44,16.43,9.00,2.83,5.44,4.14,2.05],'SouthPole_1809':[60.28,15.80,7.91,2.35,5.45,4.26,3.11],'Eclipse_1809':[64.86,16.13,3.84,1.12,3.56,6.64,2.70],'SipleDome_1810':[63.4,16.77,6.3,None,1.21,5.99,4.91],
'Tambora_ref':[57.63,19.62,4.47,1.29,3.12,6.49,6.36],
'Dakataua_Buludava_gl':[66.53,14.66,5.03,1.39,4.02,4.58,2.15],'Witori_WH6_gl':[71.97,13.64,3.80,0.90,3.57,4.19,1.22],'NIB_C_1.166m_gl':[72.35,13.92,3.58,0.72,3.19,4.34,1.13],'NIB_B_0.068m_gl':[69.86,14.92,4.08,0.93,2.71,3.20,3.13],'LongIs_Tibito_gl':[56.70,15.18,10.90,3.10,7.08,3.39,2.11]}
def sc(a,b):
  r=[min(x,y)/max(x,y) for x,y in zip(a,b) if x is not None and y is not None]; return sum(r)/len(r)
for k in ['W1809_all','W1809_WDC','W1809_SPRESSO','W1815_all']:
  v=m(g[k]); print(k,{n:round(sc(v,c),2) for n,c in ice.items()})
# per shard vs andesite
for r in g['W1809_all']: print(r[3],r[2],round(sc([r[i] for i in idx],ice['DomeC_1809']),2),round(sc([r[i] for i in idx],ice['Dakataua_Buludava_gl']),2))
# 1815: per shard SiO2 range, and how many shards near Tambora
for r in g['W1815_all']: print('1815',r[2],r[3],[round(r[i],1) for i in idx], round(sc([r[i] for i in idx],ice['Tambora_ref']),2))

# Score the 1809 rhyolite mean against every candidate row in data/glass_candidates.csv
# that has all seven oxides as single numbers (Claude's calculation).
if len(sys.argv) > 3:
    w1809 = m(g['W1809_all'])
    out = []
    for r in csv.DictReader(open(sys.argv[3], encoding='utf8')):
        try: v = [float(r[k]) for k in ox]
        except (ValueError, KeyError): continue
        out.append((round(sc(w1809, v), 2), r['volcano'], r['deposit'][:60], r['sample_type'][:30], v[0]))
    for o in sorted(out, reverse=True): print(o)
