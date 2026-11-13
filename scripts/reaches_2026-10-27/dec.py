import sys
S=sys.argv[1]
sub={'10':{'01':'Rain','11':'Snow','21':'Hail','23':'Icy rain','25':'Uncertain precip'},
'11':{'01':'Warm','02':'Prolonged sunny','12':'Icy objects','13':'Frozen ground water','14':'Frozen sea','15':'Prolonged overcast','21':'Hard rime','22':'Rime on woods','31':'Frost','32':'Black frost','51':'Dew'},
'12':{'01':'Haze','03':'Dust','13':'Red haze','14':'Yellow haze','22':'Black dust rain','23':'Red dust rain','32':'Black dust','33':'Red dust','51':'Fog','52':'Rime','62':'Black fog','63':'Red fog','64':'Yellow fog'},
'13':{'01':'Thunder','51':'Lightning','71':'Lightning-like in sky'},
'14':{'01':'Halo','02':'Colored halo','11':'Corona','21':'Rainbow','22':'Colored rainbow'},
'15':{'01':'Typhoon','11':'Tornado','12':'Waterspout','21':'Wind','32':'Black wind','33':'Red wind','34':'Yellow wind'},
'16':{'01':'Clouds','02':'Abnormal clouds','22':'Black cloud','23':'Red cloud','24':'Yellow cloud'},
'17':{'01':'Gas','02':'Strange gas','20':'Colored gas','21':'White gas','22':'Black gas','23':'Red gas','24':'Yellow gas'},
'30':{'01':'Drought','02':'Enduring sunny','11':'Dried channel','31':'Dried lake','41':'Dried well','51':'Dried river'},
'31':{'01':'Flood','21':'Tidal flood','31':'Lake flood','41':'Landslide','51':'River flood'},
'32':{'01':'Locust','02':'Insects','61':'Agro-disease'},'33':{'01':'Crops'},
'34':{'01':'Pestilence','02':'Peculiar epidemic','07':'Cholera'},'35':{'01':'Famine','02':'Cannibalism'},
'50':{'01':'Earthquake','03':'Landscape change','21':'Abnormal tide','42':'Sea colour','45':'Sea smell','62':'River colour','64':'Reverse flow'},
'53':{'01':'Black rain','03':'Red rain','05':'Yellow rain','07':'Coloured snow','08':'Red snow','10':'Grey snow'},
'56':{},'57':{},'58':{},'59':{'01':'Peculiar sounds'},
'62':{'01':'Darkish day/sun','02':'Dim sun','03':'Sun covered','04':'Overcast','05':'Red sun','06':'Sun colours','08':'Solar eclipse','11':'Sunspot','12':'Sun as disk'},
'63':{'01':'Bright as day','02':'Dim moon','05':'Red moon','06':'Moon colours','08':'Lunar eclipse'},
'64':{'01':'Astronomical'},'65':{},'68':{},'71':{'01':'Disaster mgmt','03':'Migration','05':'War','06':'Relief','09':'Impoverishment','10':'Death','11':'Price','13':'Building damage'},'95':{'01':'Dragon','20':'Unrecognized disaster','21':'Fire'}}
mainn={'10':'Precip','11':'Temp','12':'Visib','13':'Thunder','14':'Optical','15':'Wind','16':'Cloud','17':'Gas','30':'Drought','31':'Flood','32':'Pest','33':'Crops','34':'Disease','35':'Famine','50':'Geophys','53':'ColPrecip','56':'RainPlants','57':'RainAnimals','58':'RainMetal','59':'Sound','62':'Sun','63':'Moon','64':'Astro','65':'Plant omen','68':'Animal omen','71':'Socio','95':'Other'}
def d(c):
    m,s=c[:2],c[2:4]
    return f"{mainn.get(m,m)}:{sub.get(m,{}).get(s,s)}({c[4:7]}/{c[7:]})"
for l in open(f"{S}/win.tsv"):
    y,mo,da,ly,lm,ld,lat,lon,codes,rid=l.rstrip('\n').split('\t')
    print(f"{y}-{mo}-{da}\tJQ{int(ly)-1795}/{lm}/{ld}\t{float(lat):.2f},{float(lon):.2f}\t{rid}\t"+'; '.join(d(c) for c in codes.split(';')))
