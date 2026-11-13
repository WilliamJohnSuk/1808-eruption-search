import csv,sys,collections
D=sys.argv[1]
f=open(D+'/reachesv3.1data.txt',encoding='utf-8',newline='')
lines=(l for l in f if not l.startswith('#'))
rd=csv.DictReader(lines,delimiter='\t')
A=collections.defaultdict(set);B=collections.defaultdict(set);C=collections.defaultdict(set);Dg=collections.defaultdict(set);T=collections.Counter()
for r in rd:
    try:
        y=int(r['year_greg_st']); m=int(r['mon_greg_st']); lat=float(r['place_latitu']); lon=float(r['place_longit'])
    except: continue
    if y<1750 or y>1860: continue
    codes=[c for c in r['event_code'].strip().split(';') if c]
    T[y]+=1
    key=(lat,lon)
    subs={c[:4] for c in codes}
    cold = subs & {'1011','1131','1132','1023','1112','1113','1121','1122'}
    if cold and lat<32 and m in (4,5,6): A[y].add(key)
    if cold and lat<25.5 : B[(y if m>=7 else y-1)].add(key)   # winter season labelled by its starting year
    if subs & {'1442','6205','6202','6201','1623','1723','1213','6206','1222','1223','5301'} and not subs & {'1521','1532','1533','1534','1203','1214'}: C[y].add(key)
    if subs & {'3001','3501'} and 20<=lat<=25.6 and 106<=lon<=117.5: Dg[y].add(key)
print('year total lateSpringColdSouth winterColdLat<25.5(season start) skyColourNoWind GD/GX drought+famine sites')
for y in range(1780,1841):
    print(y,T[y],len(A[y]),len(B[y]),len(C[y]),len(Dg[y]),sep='\t')
