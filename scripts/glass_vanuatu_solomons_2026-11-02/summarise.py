"""T10 (2 Nov 2026): per-volcano summary of the 26 Oct GEOROC similarity scores for Vanuatu and the Solomons.
Reads data/georoc_scored_2026-10-26.csv (7-oxide Borchardt similarity vs 1809 ice glass), writes
data/glass_vanuatu_solomons_by_volcano_2026-11-02.csv. Run from the 1808-eruption folder."""
import pandas as pd
d = pd.read_csv('data/georoc_scored_2026-10-26.csv', low_memory=False)
G = {  # GEOROC location tail -> volcano (subaerial or named centres only; dredges, ODP sites, basins left as 'marine/other')
 'AMBRYM':'Ambrym','AD 1913 FORMATION':'Ambrym','AOBA (=AMBAE)':'Ambae (Aoba)','YASUR(=YASOWA)':'Yasur (Tanna)','TANNA (=TANUA)':'Yasur (Tanna)','SIWI FORMATION':'Yasur (Tanna)','GREEN HILL':'Yasur (Tanna)',
 'GAUA (SANTA MARIA)':'Gaua','SANTA MARIA PYROCLASTIC SERIES':'Gaua','EAST EPI':'Epi / Kuwae','WEST EPII':'Epi / Kuwae','TONGOA':'Epi / Kuwae','MERELAVA':'Mere Lava','LOPEVI':'Lopevi',
 'VANUA LAVA':'Vanua Lava','MOTO LAVA':'Mota Lava','UREPARAPARA':'Ureparapara','FUTUNA':'Futuna','EFATE':'Efate','ERROMANGO (=EROMANGA)':'Erromango','TUKOSMERU':'Tukosmeru (Aneityum)',
 'HUNTER':'Hunter','EAST MATTHEW':'Matthew','WEST MATTHEW':'Matthew','VANIKORO':'Vanikoro','SANTA CRUZ ARCHIPELAGO - VANIKORO':'Vanikoro','ESPIRITU SANTO':'Espiritu Santo (old)',
 'SAVO':'Savo','NEW GEORGIA ISLANDS - KOLOMBANGARA':'Kolombangara','NEW GEORGIA ISLANDS - SIMBO':'Simbo','BAGANA':'Bagana','SANTA CRUZ ARCHIPELAGO - TINAKULA':'Tinakula',
 'NEW GEORGIA ISLANDS - KOLO CALDERA':'Kolo caldera','SANTA CRUZ ARCHIPELAGO - UTUPUA':'Utupua','NEW GEORGIA ISLANDS - RENDOVA':'Rendova','NEW GEORGIA ISLANDS - VELLA LAVELLA':'Vella Lavella',
 'NEW GEORGIA ISLANDS - GHIZO':'Ghizo','NEW GEORGIA ISLANDS - VANGUNU':'Vangunu','NEW GEORGIA ISLANDS - NEW GEORGIA':'New Georgia','NEW GEORGIA ISLANDS - NGGATOKAE':'Nggatokae'}
rows = []
for f, arc in [('NEW_HEBRIDES_ARC_VANUATU_ARCHIPELAGO','Vanuatu'), ('SOLOMON_ISLAND_ARC','Solomons')]:
    x = d[d.file == f].copy()
    x['tail'] = x.location.astype(str).str.split('/').str[-1].str.strip()
    x['volcano'] = x['tail'].map(G).fillna('marine/other')
    x['gl'] = x.material.astype(str).str.startswith('GL')
    x['best'] = x[['DomeC','SPole']].max(axis=1)
    for v, y in x.groupby('volcano'):
        for kind, z in [('glass', y[y.gl]), ('whole rock', y[~y.gl])]:
            if len(z) == 0: continue
            b = z.loc[z.best.idxmax()]
            rows.append(dict(arc=arc, volcano=v, material=kind, n=len(z), n_ge_092=int((z.best >= 0.92).sum()),
                best_DomeC=z.DomeC.max(), best_SPole=z.SPole.max(), K2O_median=round(z.K2O.median(), 2),
                SiO2_median=round(z.SiO2.median(), 1), best_sample=b['sample'], best_SiO2=b.SiO2, best_K2O=b.K2O,
                best_age=str(b.eruption_year) if str(b.eruption_year) != 'nan' else str(b.geol_age), best_citation=b.citation))
o = pd.DataFrame(rows).sort_values(['arc','best_DomeC'], ascending=[True, False])
o.to_csv('data/glass_vanuatu_solomons_by_volcano_2026-11-02.csv', index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_colwidth', 28)
print(o.drop(columns=['best_citation']).to_string(index=False))
