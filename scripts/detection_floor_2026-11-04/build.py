"""Detection-floor distance table (T11, first half), 4 Nov 2026.
Great-circle distance from each candidate volcano to each observer whose 1808-10
record the project has read (or, flagged 'unread', has located). Coordinates are
approximate (GVP summit positions rounded; observer town or ship position).
Writes data/detection_floor_distances_2026-11-04.csv and prints the nearest-read table."""
import csv, math, os
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','..','data','detection_floor_distances_2026-11-04.csv')
cands=[('Dakataua (Makalia)',-5.06,150.11),('Gaua',-14.27,167.50),('Cabalian',10.29,125.22),
('Agung',-8.34,115.51),('Todoko-Ranu (Halmahera)',1.25,127.47),('Dukono',1.69,127.89),
('Teon',-6.92,129.13),('Nila',-6.73,129.50),('Mahawu / Lokon-Empung',1.36,124.82),
('Tavui (Rabaul)',-4.12,152.20),('Kanlaon (Negros)',10.41,123.13),('Balbi (Bougainville)',-5.92,154.98),
('Lamington',-8.95,148.15),('Victory',-9.20,149.07)]
# name, lat, lon, record kind, read status, project reference
obs=[
('Bima court record (Sumbawa)',-8.46,118.72,'court record, dated entries','summary and word list read','wide_source_search 9.1'),
('Bone court diary (SW Sulawesi)',-4.54,120.33,'court day-book','UNREAD (digitised, U34)','wide_source_search 9.8'),
('Ship Castlereagh, Flores Sea, Dec 1808',-8.5,121.7,'ship remark (Horsburgh)','read (OCR)','moluccas_newbritain_records 1'),
('Ambon (Ludeking earthquake list; Van der Crab)',-3.70,128.18,'retrospective list','read (OCR)','moluccas_newbritain_records 2'),
('Ternate (De Clercq Korte Kroniek)',0.79,127.38,'retrospective chronicle','read (OCR)','moluccas_newbritain_records 2'),
('Bohol parish burials (Baclayon)',9.62,123.91,'monthly burial counts (indirect)','read (page images)','B70-B71'),
('Ship Ramoncita off Panaon, 21 Jan-11 Feb 1809',10.0,125.1,'track charts, no diary','charts read; diary unread (U151)','ramoncita_bvd_2026-11-02'),
('Manila (letters in Gazeta de Mexico; Comyn)',14.60,120.98,'letters; treatise','read','B35; eyewitness_books_pass2 C1'),
('Lockerby, Fiji (Bua)',-16.8,178.6,'narrative from notes','read (OCR)','wide_source_search 9.11'),
('Tonga (Mariner)',-21.13,-175.2,'narrative','read','B59'),
('Sydney (HRNSW letters)',-33.87,151.2,'letters','read (OCR); Sydney Gazette unread','B74 T7'),
('Batavia (Bataviasche Koloniale Courant, Jan-Jun 1810 only)',-6.13,106.83,'gazette','read (OCR)','moluccas_newbritain_records 3'),
('Deshima (Nagasaki) day register',32.74,129.87,'daily register','read Nov 1808-Apr 1809','B57 T6'),
('Hawaii (Campbell)',21.3,-157.86,'memoir','read','B59'),
('Guam (Freycinet, retrospective)',13.47,144.75,'retrospective','read (OCR)','wide_source_search 2026-11-04 (B75)'),
# added 4 Nov 2026, third pass (wide_source_search section 12)
('Yogyakarta/Surakarta court and Residency record (Carey 2007)',-7.80,110.37,'court texts, Residency letters (via monograph)','searched (full text of monograph)','wide_source_search 12.7'),
('Tanna, Diana stay late Jul 1809 (Golovnin, retold)',-19.53,169.27,'voyage narrative (secondary retelling)','read (secondary)','wide_source_search 12.2'),
('Bone court diary BL Add MS 12357 (SW Sulawesi)',-4.54,120.33,'court day-book','UNREAD (digitised, U219)','wide_source_search 12.5'),
('Ternate day-register copy Jun 1808-Feb 1809 (ANRI)',0.79,127.38,'day register','UNREAD (archive, U221)','wide_source_search 12.8'),
('Reports on Bali to Daendels 1808-09 (ANRI Bali-Lombok no. 64)',-8.45,115.61,'official reports','UNREAD (archive, U222)','wide_source_search 12.9'),
]
def gc(a,b,c,d):
    a,b,c,d=map(math.radians,(a,b,c,d))
    h=math.sin((c-a)/2)**2+math.cos(a)*math.cos(c)*math.sin((d-b)/2)**2
    return 6371*2*math.asin(math.sqrt(h))
rows=[]
for cn,cla,clo in cands:
    for on,ola,olo,kind,status,ref in obs:
        rows.append([cn,on,round(gc(cla,clo,ola,olo)),kind,status,ref])
with open(OUT,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['candidate','observer_record','distance_km_claude_calc','record_kind','read_status','project_ref']); w.writerows(rows)
for cn,_,_ in cands:
    r=[x for x in rows if x[0]==cn]
    rd=sorted([x for x in r if not x[4].startswith('UNREAD')],key=lambda x:x[2])
    ur=sorted([x for x in r if x[4].startswith('UNREAD')],key=lambda x:x[2])
    print(f"{cn} | {rd[0][1]} {rd[0][2]} km | 2nd {rd[1][1]} {rd[1][2]} km | nearest unread {ur[0][1]} {ur[0][2]} km")
