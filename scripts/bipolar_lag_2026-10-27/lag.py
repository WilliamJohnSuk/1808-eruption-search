"""Bipolar sulfate timing and hemispheric ratio for the 1809 event, Tambora 1815 and Krakatau 1883.
All inputs are published table values (see notes/bipolar_sulfate_lag_2026-10-27.md); outputs are Claude's calculation.
Usage: python3 lag.py > ../../data/bipolar_lag_1809_2026-10-27.csv (CSV) ; summary to stderr."""
import sys, itertools, statistics as st
ERUPT = {"T": 1815.27, "K": 1883.65}   # Tambora 10 Apr 1815, Krakatau 27 Aug 1883
# onset (decimal yr) per core: (hemisphere, source, {event: onset})
ONSET = {
 "WDC06A": ("SH", "Sigl 2013 T1", {"U": 1809.4, "T": 1815.4, "K": 1884.0}),
 "DSS":    ("SH", "Plummer 2012 T2", {"U": 1809.7, "T": 1815.8, "K": 1884.5}),
 "NEEM-S1":("NH", "Sigl 2013 T1", {"U": 1809.7, "T": 1815.6, "K": 1883.6}),
 "NGRIP":  ("NH", "Plummer 2012 T2", {"U": 1809.3, "T": 1816.1, "K": 1883.5}),
}
END = {"WDC06A": {"U": 1812.1, "T": 1818.4, "K": 1886.4}, "DSS": {"U": 1811.1, "T": 1819.3, "K": 1885.9},
       "NEEM-S1": {"U": 1811.2, "T": 1817.6, "K": 1886.3}, "NGRIP": {"U": 1811.8, "T": 1817.9, "K": 1886.2}}
# deposition midpoints, Cole-Dai 2009 T2 (month precision, +-4 mo)
MID = {"SP01": ("SH", {"U": 1810.42, "T": 1817.04}), "WDC": ("SH", {"U": 1810.54, "T": 1816.79}),
       "SU07": ("NH", {"U": 1810.71, "T": 1816.71})}
# fluxes kg SO4/km2: (NH, SH) per pairing
FLUX = {
 "NEEM-S1/WDC06A (Sigl 2013)": {"U": (30.6, 33.8), "T": (39.0, 88.6), "K": (18.5, 11.2)},
 "NGRIP/DSS (Plummer 2012)":   {"U": (38.6, 24.6), "T": (40.3, 57.2), "K": (15.4, 16.8)},
 "Gao 2007 hemispheric means": {"U": (28, 26), "T": (59, 51), "K": (11, 11)},
}
rows = []; log = lambda *a: print(*a, file=sys.stderr)
log("== Onset NH minus SH (yr; + = Greenland later) ==")
lags = {"U": [], "T": [], "K": []}
for nh, sh in itertools.product([k for k in ONSET if ONSET[k][0]=="NH"], [k for k in ONSET if ONSET[k][0]=="SH"]):
    d = {e: round(ONSET[nh][2][e]-ONSET[sh][2][e], 2) for e in "UTK"}
    for e in "UTK": lags[e].append(d[e])
    log(f"{nh}-{sh}: 1809 {d['U']:+.1f}  Tambora {d['T']:+.1f}  Krakatau {d['K']:+.1f}  1809 minus Tambora {d['U']-d['T']:+.1f}")
    rows.append(("onset_lag", f"{nh}-{sh}", d["U"], d["T"], d["K"], round(d["U"]-d["T"], 2)))
for e in "UTK": log(f"  mean {e}: {st.mean(lags[e]):+.2f} yr (range {min(lags[e]):+.1f} to {max(lags[e]):+.1f})")
log("== Midpoint NH minus SH (Cole-Dai 2009) ==")
for sh in ["SP01", "WDC"]:
    d = {e: round(MID["SU07"][1][e]-MID[sh][1][e], 2) for e in "UT"}
    log(f"SU07-{sh}: 1809 {d['U']*12:+.0f} mo  Tambora {d['T']*12:+.0f} mo  difference {(d['U']-d['T'])*12:+.0f} mo")
    rows.append(("midpoint_lag", f"SU07-{sh}", d["U"], d["T"], "", round(d["U"]-d["T"], 2)))
log("== Analogue eruption dates for 1809 (core delay from Tambora / Krakatau) ==")
for e in "TK":
    imp = []
    for c, (h, s, o) in ONSET.items():
        delay = o[e]-ERUPT[e]; x = o["U"]-delay; imp.append(x)
        rows.append((f"implied_date_{e}", c, round(x, 2), round(delay, 2), "", ""))
        log(f"  {e} {c}: delay {delay:+.2f} -> eruption {x:.2f}")
    log(f"  {e} mean {st.mean(imp):.2f} sd {st.stdev(imp):.2f}")
imp = [MID[c][1]["U"]-(MID[c][1]["T"]-ERUPT["T"]) for c in MID]
log("  Cole-Dai midpoints, Tambora analogue:", [round(x, 2) for x in imp], "mean", round(st.mean(imp), 2))
log("== Durations (yr) ==")
for c in END:
    d = {e: round(END[c][e]-ONSET[c][2][e], 1) for e in "UTK"}; log(f"  {c}: {d}")
    rows.append(("duration", c, d["U"], d["T"], d["K"], ""))
log("== NH/SH flux ratio R and 1809/Tambora double ratio ==")
for p, f in FLUX.items():
    R = {e: f[e][0]/f[e][1] for e in "UTK"}; a = R["U"]/(1+R["U"])
    log(f"  {p}: R1809 {R['U']:.2f} RTamb {R['T']:.2f} RKrak {R['K']:.2f}  R1809/RTamb {R['U']/R['T']:.2f}  NH fraction 1809 {a:.2f}")
    rows.append(("ratio", p, round(R["U"], 2), round(R["T"], 2), round(R["K"], 2), round(R["U"]/R["T"], 2)))
# per-core 1809/Tambora ratios in project CSV (antarctic_sulfate_map_2026-10-26): Greenland mean 0.70, Antarctic 0.475
log(f"  Multi-core 1809/Tambora: Greenland 0.70 / Antarctica 0.475 = {0.70/0.475:.2f}; Cole-Dai 2009 0.61/0.45 = {0.61/0.45:.2f}")
print("quantity,pair_or_core,v1809,vTambora,vKrakatau,v1809_minus_or_over_Tambora")
for r in rows: print(",".join(str(x) for x in r))
