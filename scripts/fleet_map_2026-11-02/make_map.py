"""Draft fleet map (T3 v1), 2 Nov 2026. Draws an SVG world map (equirectangular,
lon -110..190, lat -45..65) of Royal Navy distant stations on 1 Jan 1809 (Steel),
ships per station, ADM 51 log coverage of the core window, packet routes,
candidate volcanoes and dated veil/twilight observations.
Usage: python3 make_map.py land.geojson out.svg  (land = Natural Earth 110m land)"""
import json, sys, csv, os
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__)); data = os.path.join(here, '..', '..', 'data')
L0, L1, B0, B1, K = -110, 190, -45, 65, 5.0
W, H = (L1-L0)*K, (B1-B0)*K
def xy(lon, lat):
    if lon < L0: lon += 360
    return (lon-L0)*K, (B1-lat)*K
def ring(coords, shift):
    return 'M' + 'L'.join('%.1f,%.1f' % ((c[0]+shift-L0)*K, (B1-c[1])*K) for c in coords) + 'Z'
land = json.load(open(sys.argv[1])); paths = []
for f in land['features']:
    g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    for p in polys:
        for shift in (0, 360):
            paths.append(ring(p[0], shift))
# station counts (Steel 1 Jan 1809) and Atlantic log coverage (T1 csv)
st = Counter(r['region'] for r in csv.DictReader(open(os.path.join(data, 'rn_stations_steel_1809-01-01.csv'))))
cov = Counter(); 
for r in csv.DictReader(open(os.path.join(data, 'rn_logs_atlantic_stations_2026-11-02.csv'))):
    if r['core_cover'] == 'full': cov[r['station']] += 1
S = [  # label, lon, lat, ships, logs covering whole core window, label dx, dy
 ('Leeward Is.', -61.5, 13.5, st['Leeward Islands / West Indies'], cov['Leeward'], 14, 16),
 ('Jamaica', -77, 18, st['Jamaica'], cov['Jamaica'], -95, 4),
 ('N. America / Newfoundland', -63.6, 44.6, st['North America / Newfoundland'], None, 14, -8),
 ('Brazil (Rio)', -43.2, -22.9, st['Brazil / South America'], cov['Brazil'], 12, 4),
 ('Cape', 18.4, -33.9, st['Cape of Good Hope'], cov['Cape'], 12, 14),
 ('W. Africa / Atlantic is.', -13.2, 8.5, st['Africa / Atlantic islands'], None, -150, 22),
 ('East Indies', 80.3, 13.1, st['East Indies'], 25, -150, 40),
 ('New South Wales', 151.2, -33.9, st['New South Wales'], None, 10, 14),
]
o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" font-family="Helvetica,Arial,sans-serif" font-size="11">' % (W, H+120),
     '<rect width="100%%" height="100%%" fill="#eef3f7"/><clipPath id="c"><rect width="%d" height="%d"/></clipPath>' % (W, H),
     '<g clip-path="url(#c)"><path d="%s" fill="#d9d4c7" stroke="#a8a192" stroke-width="0.5"/>' % ' '.join(paths)]
for lat in range(-40, 61, 20): o.append('<line x1="0" x2="%d" y1="%.1f" y2="%.1f" stroke="#c9d5df" stroke-width="0.5"/>' % (W, (B1-lat)*K, (B1-lat)*K))
# packet routes from Falmouth
fal = xy(-5.07, 50.15)
for lon, lat, n in [(-61.5, 13.5, 'Leeward'), (-77, 18, 'Jamaica'), (-43.2, -22.9, 'Brazil'), (-63.6, 44.6, 'Halifax'), (-9.1, 38.7, 'Lisbon')]:
    x, y = xy(lon, lat); o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#7b6fa8" stroke-width="1" stroke-dasharray="4 3"/>' % (fal + (x, y)))
x, y = xy(-35, 30); o.append('<text x="%.1f" y="%.1f" fill="#5b4f8a" font-size="10">Post Office packets (Falmouth)</text>' % (x, y))
x, y = xy(-30, 20); o.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="#5b4f8a"/><text x="%.1f" y="%.1f" fill="#5b4f8a" font-size="10">packet Townshend: hazy 10 Dec 1808-9 Jan 1809</text>' % (x, y, x+6, y+12))
# Europe placeholder
x, y = xy(-12, 58); o.append('<text x="%.1f" y="%.1f" fill="#444" font-style="italic">Home waters, Baltic, Mediterranean: several hundred ships, not yet mapped (T2)</text>' % (x, y))
for name, lon, lat, n, c, dx, dy in S:
    x, y = xy(lon, lat); r = 4 + (n ** 0.5) * 2.2
    o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#2f6690" fill-opacity="0.35" stroke="#2f6690"/>' % (x, y, r))
    lab = '%s: %d ships' % (name, n) + ('' if c is None else ', %d logs cover Nov-Mar' % c)
    o.append('<text x="%.1f" y="%.1f" fill="#16324f" font-weight="bold">%s</text>' % (x+dx, y+dy, lab))
# East Indies placements (fleet notes 8)
for lab, lon, lat in [('Bombay / Gulf', 72.8, 19), ('Madras / Bay of Bengal', 85, 15), ('Penang', 100.3, 5.4), ('Russel, Dover, Phaeton: S. China Sea Nov-Dec 1808', 113.5, 22.2)]:
    x, y = xy(lon, lat); o.append('<circle cx="%.1f" cy="%.1f" r="2.5" fill="#16324f"/><text x="%.1f" y="%.1f" font-size="9" fill="#16324f">%s</text>' % (x, y, x+4, y-3, lab))
x, y = xy(120.9, 14.6); o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#16324f">Psyche, Doris: Manila Apr-Oct 1809</text>' % (x+4, y-4))
# candidates
for lab, lon, lat, top in [('Dakataua', 150.1, -5.06, 1), ('Gaua', 167.5, -14.27, 1), ('Cabalian', 125.22, 10.29, 1), ('Agung', 115.5, -8.34, 0), ('Dukono', 127.9, 1.7, 0), ('Teon/Nila', 129.1, -6.8, 0)]:
    x, y = xy(lon, lat); s = 6 if top else 4
    o.append('<path d="M%.1f,%.1f l%d,%d h-%d z" fill="#c0392b"/>' % (x, y-s, s, 2*s, 2*s))
    o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#8e2a1f"%s>%s</text>' % (x+7, y+4, ' font-weight="bold"' if top else '', lab))
# observations
for lab, lon, lat in [('Bogota veil 11 Dec 1808', -74.1, 4.6), ('Edo red skies from 9 Jan 1809', 139.7, 35.7), ('Ramoncita, Surigao Strait 21 Jan-Feb 1809', 125.5, 9.8)]:
    x, y = xy(lon, lat); o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#e1a100" stroke="#7a5a00"/><text x="%.1f" y="%.1f" font-size="9" fill="#7a5a00">%s</text>' % (x, y, x+6, y+12, lab))
x, y = xy(-150+360, -20) if False else xy(170, 20)
o.append('<text x="%.1f" y="%.1f" font-size="11" fill="#444" font-style="italic" text-anchor="end">No Royal Navy ship in the Pacific</text>' % xy(185, 30))
o.append('</g>')
y0 = H + 20
leg = ['DRAFT v1 (2 Nov 2026). Royal Navy distant stations on 1 Jan 1809 (Steel\'s Navy List [page image]); circle area = ships on station.',
       '"Logs cover Nov-Mar" = ADM 51 captain\'s log at Kew covering all of 1 Nov 1808-31 Mar 1809 [catalogue text]; East Indies figure from fleet notes section 6; N. America not yet checked.',
       'Red triangles = candidate volcanoes (bold = top three, B53). Gold dots = dated observations of the veil or red skies. Station positions are station centres, not ship positions [inference].',
       'Sources: data/rn_stations_steel_1809-01-01.csv, data/rn_logs_atlantic_stations_2026-11-02.csv, data/packets_steel_1809-01-01.csv; land: Natural Earth 110 m (public domain).']
for i, t in enumerate(leg): o.append('<text x="10" y="%d" font-size="11" fill="#333">%s</text>' % (y0 + 20*i, t.replace('&', '&amp;')))
o.append('</svg>'); open(sys.argv[2], 'w').write('\n'.join(o))
print('ok', dict(st), dict(cov))
