"""Lunar (Chinese Shixian) to Gregorian for 1808-1811, via sxtwl; prints the month table.
Usage: python3 luncal.py            -> month table
       python3 luncal.py Y M D [leap] -> one date
"""
import sys, sxtwl
TG=["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
DZ=["tý","sửu","dần","mão","thìn","tỵ","ngọ","mùi","thân","dậu","tuất","hợi"]
def gz(d):
    g=d.getDayGZ(); return TG[g.tg]+' '+DZ[g.dz]
def conv(y,m,day,leap=False):
    d=sxtwl.fromLunar(y,m,day,leap)
    return f'{d.getSolarYear()}-{d.getSolarMonth():02d}-{d.getSolarDay():02d}', gz(d)
if len(sys.argv)>=4:
    y,m,day=map(int,sys.argv[1:4]); leap=len(sys.argv)>4
    print(conv(y,m,day,leap))
else:
    for y in (1808,1809,1810,1811):
        for m in range(1,13):
            for leap in (False,True):
                try: d=sxtwl.fromLunar(y,m,1,leap)
                except Exception: continue
                if leap!=d.isLunarLeap(): continue
                # month length
                n=29
                try:
                    d30=sxtwl.fromLunar(y,m,30,leap)
                    if d30.getLunarDay()==30 and d30.isLunarLeap()==leap: n=30
                except Exception: pass
                print(f'GL{y-1801} {y} {"leap " if leap else ""}month {m:2d}: day 1 = {d.getSolarYear()}-{d.getSolarMonth():02d}-{d.getSolarDay():02d} ({gz(d)}), {n} days')
