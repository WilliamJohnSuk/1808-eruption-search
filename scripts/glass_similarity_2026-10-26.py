ox=['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O']
ice={'DomeC_1809':[59.44,16.43,9.00,2.83,5.44,4.14,2.05],
'SouthPole_1809':[60.28,15.80,7.91,2.35,5.45,4.26,3.11],
'Eclipse_1809':[64.86,16.13,3.84,1.12,3.56,6.64,2.70],
'SipleDome_1810':[63.4,16.77,6.3,None,1.21,5.99,4.91]}
# candidates: name, type, full oxide dict (SiO2,TiO2,Al2O3,FeOt or Fe2O3T,MnO,MgO,CaO,Na2O,K2O,P2O5)
F=0.8998
def wr(si,ti,al,fe2o3,mn,mg,ca,na,k,p): # Fe2O3T -> FeOt, anhydrous normalise
    fe=fe2o3*F; v=[si,ti,al,fe,mn or 0,mg,ca,na,k,p]; s=sum(v); return [x*100/s for x in [si,al,fe,mg,ca,na,k]]
def gl(si,al,fe,mg,ca,na,k): return [si,al,fe,mg,ca,na,k]
def mean(rows): return [sum(c)/len(c) for c in zip(*rows)]
C={}
C['Dukono DK1 (wr, Bani 2021)']=wr(58.0,0.8,13.9,10.5,0,2.0,7.3,3.1,3.7,0.4)
C['Dukono DK2 (wr)']=wr(59.5,0.8,15.3,8.4,0,2.7,5.8,3.4,2.5,0.3)
C['Dukono DK3 (wr)']=wr(59.3,0.7,15.8,8.6,0,2.3,6.0,3.5,2.5,0.3)
C['Ibu mean IB1-3 (wr)']=mean([wr(67.1,.69,15.1,5.0,0,.84,3.00,4.42,3.22,.186),wr(67.1,.70,14.9,5.0,0,.85,2.97,4.38,3.20,.185),wr(66.6,.69,14.9,5.0,0,.85,3.00,4.35,3.19,.188)])
C['Gamkonora mean GK1-2 (wr)']=mean([wr(57.0,.84,17.4,9.0,0,3.08,6.84,3.78,1.64,.304),wr(57.7,.78,17.7,8.8,0,3.20,6.95,3.74,1.50,.255)])
C['Gamalama GL (wr)']=wr(56.6,.84,17.3,9.5,0,3.49,7.26,3.45,1.56,.192)
C['Makian MK3 most evolved (wr)']=wr(55.8,.69,19.0,7.7,0,3.35,7.54,3.92,1.21,.159)
C['Hunga 2022 light pumice (bulk)']=gl(57.5,15.0,13.5,3.7,8.9,2.0,0.6)
C['NIB marine glass grp C 1.475m (Horz)']=gl(60.66,15.12,10.08,2.49,7.29,2.51,0.81)
C['NIB marine glass grp C 1.166m (Horz)']=gl(72.35,13.92,3.58,0.72,3.19,4.34,1.13)
C['NIB marine glass grp B 0.068m (Horz)']=gl(69.86,14.92,4.08,0.93,2.71,3.20,3.13)
C['Witori W-H6 Tili (glass)']=gl(71.97,13.64,3.80,0.90,3.57,4.19,1.22)
C['Dakataua Dk Buludava (glass)']=gl(66.53,14.66,5.03,1.39,4.02,4.58,2.15)
C['Long Is. Tibito Ambra A1 (glass)']=gl(56.70,15.18,10.90,3.10,7.08,3.39,2.11)
def sc(a,b):
    r=[min(x,y)/max(x,y) for x,y in zip(a,b) if x is not None and y is not None]
    return sum(r)/len(r)

# Borchardt similarity coefficient on SiO2, Al2O3, FeOt, MgO, CaO, Na2O, K2O (mean of min/max ratios),
# same method as notes/glass_comparison_2026-10-22.md. Whole-rock rows: Fe2O3T converted to FeOt (x0.8998)
# and normalised anhydrous; they are NOT glass and are scored only to place each volcano in a magma family.
import csv, sys
out = sys.argv[1] if len(sys.argv) > 1 else 'glass_similarity_2026-10-26.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['candidate', 'material'] + ['SC_' + k for k in ice] + ['SiO2', 'Al2O3', 'FeOt', 'MgO', 'CaO', 'Na2O', 'K2O', 'note'])
    for n, v in C.items():
        mat = 'whole-rock' if '(wr' in n else ('bulk' if 'bulk' in n else 'glass')
        w.writerow([n, mat] + [f'{sc(v, i):.2f}' for i in ice.values()] + [f'{x:.2f}' for x in v] +
                   ["Claude's calculation; whole-rock scores are indicative only" if mat != 'glass' else "Claude's calculation"])
