"""Driver for EVA_H (Aubry et al. 2020; Python port by B. Chakraborty, GitHub thomasaubry/EVA_H).
Runs single-eruption scenarios and returns (a) the integrated flux of sulfate from the stratosphere
to the troposphere in the SH extratropical (box 7), tropical (box 5) and NH extratropical (box 8)
boxes, used here as a hemispheric deposition proxy, and (b) monthly SAOD at 550 nm by latitude.
Claude's calculation (28 Oct 2026). Model code unchanged; only the input spreadsheet is generated.
"""
import os, sys, json, numpy as np, pandas as pd
EVAH = '/tmp/claude-0/-home-claude/9ef394ea-bd92-5242-9b96-ac810034ace0/scratchpad/evah/EVA_H/EVA_H_Python_scripts'
WORK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EVAH)
import scipy.interpolate as _si
if not hasattr(_si, 'interp2d'):
    _si.interp2d = None  # removed in SciPy 1.14; EVA_H imports but never calls it
os.chdir(EVAH)
from parameters import ModelParams
from so2injection_8boxes import so2injection_8boxes
from eightboxequations import eightboxequations
from postproc import postproc
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator

S_PER_SO2 = 0.50052  # as in so2injection_8boxes

def make_xlsx(name, year, month, day, lat, mass_tgS, h_km, tropo_km, path):
    kt_so2 = mass_tgS / S_PER_SO2 * 1000.0
    df = pd.DataFrame([[name, year, month, day, lat, 0.0, kt_so2, tropo_km, h_km]],
        columns=['Volcano name','Eruption year','Eruption month','Eruption day','Latitude (degree north)',
                 'Longitude (Degree east)','Mass of SO2 (kt of SO2)','Tropopause altitude at volcano location (km a.s.l.)',
                 'Altitude of SO2 emission (km a.s.l.)'])
    df.to_excel(path, index=False)
    return kt_so2

def run(lat, h_km, mass_tgS=19.3, year=1990, month=12, day=1, tropo_km=None, months=72,
        seasonal_mix=None, background=False, want_saod=False, tag='scn'):
    """seasonal_mix: None (default EVA_H: no seasonal cycle) or (amix, smix) arrays of length 6."""
    mp = ModelParams()
    if seasonal_mix is not None:
        mp.amix = np.array(seasonal_mix[0], float); mp.smix = np.array(seasonal_mix[1], float)
    if tropo_km is None:
        tropo_km = 16.5 if abs(lat) <= 25 else (10.0 if abs(lat) > 45 else 13.0)
    xp = os.path.join(WORK, f'inj_{tag}.xlsx')
    make_xlsx('scenario', year, month, day, lat, mass_tgS, h_km, tropo_km, xp)
    inmass, intime = so2injection_8boxes(mp.h1lim, mp.h2lim, mp.latlim, xp)
    intime = np.asarray(intime, float)
    t0 = float(intime[0])
    tspan = [t0 - 0.01, t0 + months]
    if background:
        ic = np.array([0.0126,0.0468,0.0152,0.0192,0.0359,0.0218,0.0349,0.0417]); back = mp.backinj
    else:
        ic = np.zeros(8); back = np.zeros(8)
    sol = solve_ivp(eightboxequations, tspan, ic, args=[inmass, intime, mp, back], rtol=1e-6, atol=1e-10,
                    dense_output=True, max_step=0.25)
    tref = np.arange(t0, t0 + months + 0.001, 1.0)
    y = sol.sol(tref).T  # months x 8
    # tropospheric loss fluxes (Tg S / month): box5 (tropics), box7 (SH extratropics), box8 (NH extratropics)
    tf = np.linspace(tspan[0], tspan[1], 20001); yf = sol.sol(tf).T
    dt = tf[1]-tf[0]
    dep = {'SH': float(np.trapezoid(yf[:,6]/mp.tauloss[6], dx=dt)),
           'TR': float(np.trapezoid(yf[:,4]/mp.tauloss[4], dx=dt)),
           'NH': float(np.trapezoid(yf[:,7]/mp.tauloss[7], dx=dt))}
    out = {'lat': lat, 'h_km': h_km, 'mass_tgS': mass_tgS, 'month': month, 'inj_boxes_tgS': inmass[:,0].round(4).tolist(),
           'dep_tgS': dep, 'NH_over_SH': dep['NH']/dep['SH'] if dep['SH']>0 else float('inf'),
           'NH_share_extratrop': dep['NH']/(dep['NH']+dep['SH']),
           'mass_in_stratosphere_total_tgS_monthly': y.sum(axis=1).round(4).tolist(),
           'mass_NH_extratrop_monthly': y[:,[2,5,7]].sum(axis=1).round(4).tolist(),
           'mass_SH_extratrop_monthly': y[:,[0,3,6]].sum(axis=1).round(4).tolist(),
           'mass_tropics_monthly': y[:,[1,4]].sum(axis=1).round(4).tolist()}
    if want_saod:
        gmsaod, saod, reff, ext, ssa, asy, latg, alt = postproc(y, mp, mp.mstar, mp.R_reff, np.array([0.550]))
        out['saod_lat_grid'] = latg.tolist()
        out['saod550_monthly_by_lat'] = saod[:,:,0].round(5).tolist()
        out['gm_saod550_monthly'] = gmsaod[:,0].round(5).tolist()
    return out

if __name__ == '__main__':
    r = run(-8.25, 30.0, 28.1, year=1990, month=4, day=10, tag='test')
    print(json.dumps({k:v for k,v in r.items() if 'monthly' not in k}, indent=1))
