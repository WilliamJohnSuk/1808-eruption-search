import openpyxl,sys,csv
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
ws=wb['Data']
w=csv.writer(open(sys.argv[2],'w'),delimiter='\t')
hdr=None
for row in ws.iter_rows(values_only=True):
    if hdr is None:
        if row[0]=='new_ID' and row[1]=='record_ID' and row[2] and 'subrecord' in str(row[2]) and not str(row[3] or '').startswith('A ') and row[3] is not None and len(str(row[3]))<30: hdr=row; w.writerow(hdr)
        continue
    try: y=int(row[hdr.index('year_greg_st')])
    except: continue
    if 1806<=y<=1811: w.writerow(row)
print(hdr)
