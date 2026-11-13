import json, csv, statistics as st, math
rows = list(csv.DictReader(open('work/coral_footprint_1800-1820.csv')))
def region(lat, lon):
    if 30 <= lon <= 60 and lat < 20: return 'W Indian Ocean'
    if 30 <= lon <= 40 and lat >= 20: return 'Red Sea'
    if 100 <= lon <= 150 and lat > -15: return 'Maritime Continent / W Pacific'
    if (lon > 140 or lon < -150) and lat <= -14: return 'SW Pacific / Coral Sea'
    if -100 <= lon <= -75 and lat < 15: return 'E Pacific'
    if lon >= 100 and lat <= -25: return 'W Australia'
    return 'Caribbean / W Atlantic'
by = {}
for r in rows:
    if r['cool_dry_sign'] == '' : continue
    s = int(r['cool_dry_sign']); reg = region(float(r['lat']), float(r['lon']))
    for y in range(1800,1821):
        v = r.get(f'anom_{y}')
        if v not in ('', None):
            by.setdefault(reg,{}).setdefault(y,[]).append(float(v)*s)
    r['region']=reg
for reg in sorted(by):
    print(f"\n{reg}: records = {sorted(set(r['record'].split('.')[0].replace('Ocn-','')+':'+r['variable'] for r in rows if r.get('region')==reg and r['cool_dry_sign']!=''))}")
    print('  year: mean cool/dry index (n)')
    print('  ' + '  '.join(f"{y}:{st.mean(by[reg][y]):+.2f}({len(by[reg][y])})" for y in range(1804,1820) if y in by[reg]))
