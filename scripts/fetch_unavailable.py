"""Fetch the items in unavailable_sources.md that a script can get (27 Oct 2026).

Run on William's Mac from the project's scripts/ folder (next to fetch_na_mets.py):
    cd ~/Documents/'1808-9 Volcano Project'/scripts
    caffeinate -i python3 fetch_unavailable.py all       # papers + Stroud + all NA scans + NOAA listing
    python3 fetch_unavailable.py papers                  # U16, U17, U18, U19, U20, U23 only
    caffeinate -i python3 fetch_unavailable.py na        # U9, U8 (NA scans)
    caffeinate -i python3 fetch_unavailable.py na-extra  # U10 (NA inv. 98, 91, 15; lower yield)
    python3 fetch_unavailable.py list                    # U5, U6: list NOAA ice-core files to pick from
    caffeinate -i python3 fetch_unavailable.py deshima   # U11: Deshima day registers inv. 222 and secret 257 (Nov 1808-Nov 1809); added 2 Nov 2026
    caffeinate -i python3 fetch_unavailable.py deshima-extra  # U11: inv. 221 (Nov 1807-Nov 1808) and 223 (Nov 1809-Oct 1810)
Existing files are skipped, so it can be rerun after an interruption.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)  # the project folder (scripts/ sits inside it)
UA = {"User-Agent": "Mozilla/5.0 (Macintosh) research-download/1.0"}

PAPERS = [  # (U-number, url, path under BASE)
    ("U16", "https://archive.org/download/sim_connecticut-evangelical-magazine_1810-07_3_7/sim_connecticut-evangelical-magazine_1810-07_3_7.pdf",
     "newspapers/Connecticut_Evangelical_Magazine/1810-07/ConnecticutEvangelicalMagazine_1810-07.pdf"),
    ("U17", "https://archive.org/download/dreissigjahreind00park/dreissigjahreind00park.pdf",
     "books/Parkinson_1907_Dreissig_Jahre_in_der_Suedsee/Parkinson_1907_Dreissig_Jahre_in_der_Suedsee.pdf"),
    ("U19", "https://www.openaccessrepository.it/record/121979/files/fulltext.pdf",
     "papers/Stenni_1999_AnnGlaciol_HerculesNeve_sulfate.pdf"),
    ("U20", "https://scholars.unh.edu/cgi/viewcontent.cgi?article=1522&context=earthsci_facpub",
     "papers/Yalcin_2007_JGR_StElias_volcanic_record.pdf"),
    ("U23", "https://www.tsunami.irides.tohoku.ac.jp/media/files/_u/topic/file/1ie7dmxotg.pdf",
     "papers/Tsuji_2025_TsunamiEngRep42_1808_tsunami.pdf"),
]
NA = [("U9", "2.01.27.03", "96"), ("U8", "2.01.27.05", "23")]
NA_DESHIMA = [("U11", "1.04.21", "222"), ("U11", "1.04.21", "257")]
NA_DESHIMA_EXTRA = [("U11", "1.04.21", "221"), ("U11", "1.04.21", "223")]
NA_EXTRA = [("U10", "2.01.27.03", "98"), ("U10", "2.01.27.03", "91"), ("U10", "2.01.27.05", "15")]
NOAA_DIRS = [
    "https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/",
    "https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/law/",
    "https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/wais/",
]


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
                return r.read()
        except Exception as e:
            print(f"  retry {i + 1}: {e}")
            time.sleep(2 ** (i + 1))
    print(f"  FAILED: {url}")
    return None


def save(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        print(f"have {path}")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = get(url)
    if data is None:
        return
    if path.endswith(".pdf") and not data.startswith(b"%PDF-"):
        print(f"  WARNING: not a PDF, probably a bot page; open in Safari instead: {url}")
        path += ".html"
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"saved {path} ({len(data)} bytes)")


def papers():
    for u, url, rel in PAPERS:
        print(f"[{u}]")
        save(url, os.path.join(BASE, rel))


def stroud():
    print("[U18] Hughes, Stroud register summary 1771-1813")
    ident = "met-office-archive-treasures-18th-19th-century"
    raw = get(f"https://archive.org/metadata/{ident}")
    files = json.loads(raw).get("files", []) if raw else []
    hits = [f["name"] for f in files if "S_Summary_1771_1813" in f["name"]]
    print("  matching files:", hits)
    pick = [h for h in hits if h.lower().endswith(".pdf")] or hits[:1]
    for h in pick:
        save(f"https://archive.org/download/{ident}/{urllib.parse.quote(h)}",
             os.path.join(BASE, "archives", "MetOffice_Hughes_Stroud_register_1771-1813", os.path.basename(h)))


_ead = {}


def na_uuid(toegang, invnr):
    """Find the METS UUID of one inventory number in the archive's EAD XML."""
    if toegang not in _ead:
        xml = get(f"https://www.nationaalarchief.nl/onderzoeken/archief/{toegang}/download/xml")
        _ead[toegang] = ET.fromstring(xml) if xml else None
    root = _ead[toegang]
    if root is None:
        return None
    for did in root.iter():
        if not did.tag.endswith("did"):
            continue
        ids = [e.text.strip() for e in did if e.tag.split("}")[-1] == "unitid" and e.text]
        if invnr not in ids:
            continue
        for e in did.iter():
            for v in e.attrib.values():
                m = re.search(r"mets/v1/([0-9a-f-]{36})", v)
                if m:
                    return m.group(1)
    return None


def na(items):
    for u, toegang, invnr in items:
        print(f"[{u}] NA {toegang} inv. {invnr}")
        uuid = na_uuid(toegang, invnr)
        if uuid is None:
            print("  no METS UUID found (not scanned, or EAD layout differs); skipped")
            continue
        print(f"  METS {uuid}")
        outdir = os.path.join(BASE, "archives", "Nationaal_Archief", f"{toegang}_inv{invnr}")
        subprocess.run([sys.executable, os.path.join(HERE, "fetch_na_mets.py"), uuid, outdir,
                        f"NL-HaNA_{toegang}_{invnr}"])


def noaa_list():
    print("[U5, U6] NOAA Antarctic ice-core files (paste this list back to Claude)")
    pat = re.compile(r"sulf|so4|volc|sigl|plummer|wdc|dss|law", re.I)
    for d in NOAA_DIRS:
        html = get(d, tries=2)
        if html is None:
            continue
        names = sorted(set(re.findall(r'href="([^"?/][^"]*)"', html.decode("latin-1"))))
        print(d)
        for n in names:
            if n.endswith("/") or pat.search(n):
                print("   ", n)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "papers"):
        papers()
        stroud()
    if what in ("all", "na"):
        na(NA)
    if what in ("all", "na-extra"):
        na(NA_EXTRA)
    if what == "deshima":  # not part of "all"
        na(NA_DESHIMA)
    if what == "deshima-extra":
        na(NA_DESHIMA_EXTRA)
    if what in ("all", "list"):
        noaa_list()
