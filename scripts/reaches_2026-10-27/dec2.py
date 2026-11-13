import csv,sys,re
S=sys.argv[1]
exec(open(S+'/dec.py').read().split('def d(c)')[0].split('S=sys.argv[1]')[1])
sub['14']['42']='Abnormal sky colour'
def d(c):
    m,s=c[:2],c[2:4]; return f"{mainn.get(m,m)}:{sub.get(m,{}).get(s,s)}({c[4:7]}/{c[7:]})"
out=open(S+'/window_1808-07_1810-06_named.tsv','w')
out.write('greg_y\tgreg_m\tgreg_d\tJQ_lunar\tprovince\tcounty\tlat\tlon\tevents\tsource\tcompendium_record\n')
for r in csv.DictReader(open(S+'/x1806.tsv'),delimiter='\t'):
    y=int(r['year_greg_st']); m=int(r['mon_greg_st'])
    if not ((y==1808 and (m>=7 or m==-9999)) or y==1809 or (y==1810 and m<=6)): continue
    codes=[c for c in str(r['event_code']).split(';') if c]
    lun=f"JQ{int(r['year_lunar_st'])-1795}/{r['mon_lunar_st']}/{r['date_lunar_st']}".replace('-9999','?')
    out.write('\t'.join([str(y),str(m).replace('-9999','?'),r['date_greg_st'].replace('-9999','?'),lun,r['place_provin'],r['place_city'],r['place_latitu'][:6],r['place_longit'][:7],'; '.join(d(c) for c in codes),r['source'],r['record_ID']+'/'+r['subrecord_ID']])+'\n')
