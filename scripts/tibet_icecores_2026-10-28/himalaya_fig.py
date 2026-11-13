import sys, csv, math, os
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = sys.argv[1]; OUT = sys.argv[2]
ev = list(csv.DictReader(open(os.path.join(D, 'everest_samples_1795-1830_efc.csv'))))
def f(x):
    try: return float(x)
    except: return None
ea = [f(r['age']) for r in ev]; ebi = [f(r['Bi_ppt']) for r in ev]; eef = [f(r['EFc_Bi_Xu']) for r in ev]
# Dasuopu EFc per sample from raw file
dl = [l for l in open(os.path.join(D, 'dasuopu2020elem-noaa.txt'), encoding='utf-8', errors='replace').read().split('\n') if l and not l.startswith('#')]
h = dl[0].split('\t'); di = {c: i for i, c in enumerate(h)}
da, def_ = [], []
for l in dl[1:]:
    t = l.split('\t')
    if len(t) != len(h): continue
    age = f(t[di['age_CE']]); bi = f(t[di['Bi']]); al = f(t[di['Al']]); fe = f(t[di['Fe']])
    if age is None or bi is None or not (1795 <= age < 1831): continue
    e = []
    if al: e.append((bi / al) / (0.16 / 81500))
    if fe: e.append((bi / fe) / (0.16 / 39200))
    if e: da.append(age); def_.append(sum(e) / len(e))
fig, axs = plt.subplots(3, 1, figsize=(9, 8.5), sharex=True)
for ax in axs:
    ax.axvspan(1808.9, 1810.9, color='#f4c7c3', alpha=0.6, lw=0)
    ax.axvline(1815.27, color='#7a1f1f', ls='--', lw=1)
    ax.set_xlim(1795, 1831); ax.grid(True, which='major', color='#dddddd', lw=0.6)
ax = axs[0]
x = [a for a, b in zip(ea, ebi) if b]; y = [b for b in ebi if b]
ax.semilogy(x, y, '.-', color='#1f3b73', ms=4, lw=0.8)
ax.set_ylabel('Everest Bi (ppt)'); ax.set_title('Everest East Rongbuk (28.0°N, 6518 m) and Dasuopu (28.4°N, 7200 m): bismuth, 1795-1830', fontsize=10)
ax.annotate('Tambora: 197 ppt at 1815.71', xy=(1815.71, 196.7), xytext=(1818.5, 120), fontsize=8, arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(1809.9, 0.03, '1809-10\nwindow', ha='center', fontsize=8, color='#7a1f1f')
ax = axs[1]
x = [a for a, b in zip(ea, eef) if b]; y = [b for b in eef if b]
ax.semilogy(x, y, '.-', color='#1f3b73', ms=4, lw=0.8)
ax.axhline(20.1, color='grey', lw=0.8, ls=':'); ax.axhline(370.8, color='#b00', lw=0.8, ls=':')
ax.text(1795.3, 23, 'median EFc 20', fontsize=7, color='grey'); ax.text(1795.3, 420, 'Xu 2009 rule: mean + 2 sd = 371', fontsize=7, color='#b00')
ax.set_ylabel('Everest EFc(Bi), Xu style')
ax = axs[2]
ax.semilogy(da, def_, '.-', color='#2d6a4f', ms=4, lw=0.8)
ax.axvspan(1815.80, 1817.01, color='#cccccc', alpha=0.7, lw=0); ax.text(1816.4, 400, 'no\nsamples', ha='center', fontsize=7)
ax.axhline(18.6, color='grey', lw=0.8, ls=':'); ax.text(1795.3, 21, 'median EFc 19', fontsize=7, color='grey')
ax.set_ylabel('Dasuopu EFc(Bi), Al and Fe'); ax.set_xlabel('year (layer-counted age; Tambora erupted 10 Apr 1815, dashed)')
ax.annotate('1823.62: Bi 48 pg/g, EFc 1383\n(Galunggung Oct 1822? suggestion)', xy=(1823.62, 1383), xytext=(1818.3, 2000), fontsize=7, arrowprops=dict(arrowstyle='->', lw=0.8))
fig.text(0.01, 0.005, 'Data: NOAA rongbuk2009.txt (Kaspari et al. 2009) and dasuopu2020elem-noaa.txt (Gabrielli et al. 2020); below-detection replacement values removed; EFc = (Bi/x)ice / (Bi/x)UCC, Rudnick & Gao 2003; Claude\'s calculation 28 Oct 2026 (B68).', fontsize=6.5)
fig.tight_layout(rect=(0, 0.02, 1, 1)); fig.savefig(OUT, dpi=140); print('wrote', OUT)
