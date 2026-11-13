#!/usr/bin/env python3
"""Download 1808-09 newspaper scans and OCR text for the 1808/09 eruption search.

Run on your own Mac (these sites block cloud servers, not you):

    cd ~/Documents/'1808-9 Volcano Project'/scripts
    python3 fetch_newspapers.py test        # quick check of every site, ~5 min
    python3 fetch_newspapers.py all         # everything that is fully scripted
    python3 fetch_newspapers.py ia          # one source at a time (see SOURCES below)

Everything lands in <project>/newspapers/script_downloads/<source>/, with a run_log.txt
and an index.csv per source. Re-running skips files already downloaded.
Only uses Python's standard library and the system `curl`.
"""
import csv
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse as up

# downloads, cookies and run_log.txt live in <project>/newspapers/script_downloads (moved there 27 Oct 2026)
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "newspapers", "script_downloads")
START = dt.date(1808, 9, 1)
END = dt.date(1810, 6, 30)     # widened 16 Oct: Asian/Pacific news took 4-8 months to reach print
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")
DELAY = 1.5          # seconds between requests; be polite
LOG = None


# ---------------------------------------------------------------- helpers

def log(*a):
    line = " ".join(str(x) for x in a)
    print(line, flush=True)
    if LOG:
        LOG.write(line + "\n")
        LOG.flush()


def fetch(url, dest=None, headers=None, tries=3, delay=DELAY, quiet404=False, data=None):
    """GET url with curl. Returns bytes (or dest path when dest given), None on failure."""
    jar = os.path.join(ROOT, ".cookies.txt")
    cmd = ["curl", "-sS", "-L", "--compressed", "-A", UA, "-b", jar, "-c", jar,
           "--max-time", "300", "-w", "%{http_code}"]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    if data:
        cmd += ["--data", data]
    for attempt in range(1, tries + 1):
        time.sleep(delay)
        tmp = (dest + ".part") if dest else None
        out = subprocess.run(cmd + (["-o", tmp] if tmp else ["-o", "-"]) + [url],
                             capture_output=True)
        if dest:
            code = out.stdout.decode()[-3:]
            body = None
        else:
            code = out.stdout[-3:].decode(errors="replace")
            body = out.stdout[:-3]
        if out.returncode == 0 and code.startswith("2"):
            if dest:
                os.replace(tmp, dest)
                return dest
            return body
        if not (quiet404 and code == "404"):
            log(f"   ! {code or out.returncode} on {url} (try {attempt}) {out.stderr.decode()[:120]}")
        if tmp and os.path.exists(tmp):
            os.remove(tmp)
        if code in ("404", "410", "403"):
            break
        time.sleep(5 * attempt)
    return None


def fetch_json(url, headers=None):
    b = fetch(url, headers=headers)
    if b is None:
        return None
    try:
        return json.loads(b)
    except ValueError:
        log("   ! not JSON:", url, b[:200])
        return None


def outdir(name):
    d = os.path.join(ROOT, name)
    os.makedirs(d, exist_ok=True)
    return d


def safe(s, n=80):
    s = re.sub(r"[^\w\-. ]+", "_", s, flags=re.UNICODE).strip().replace(" ", "_")
    return s[:n] or "x"


def in_window(datestr):
    """True/False for a parseable date, None when the date can't be judged."""
    if not datestr:
        return None
    m = re.match(r"(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?", datestr.strip())
    if not m:
        return None
    y, mo, d = int(m.group(1)), m.group(2), m.group(3)
    if not mo:
        if START.year < y < END.year:
            return True
        return None if y in (START.year, END.year) else False
    if not d:
        first = dt.date(y, int(mo), 1)
        return START.replace(day=1) <= first <= END
    try:
        return START <= dt.date(y, int(mo), int(d)) <= END
    except ValueError:
        return None


def days():
    d = START
    while d <= END:
        yield d
        d += dt.timedelta(days=1)


class Index:
    def __init__(self, d, fields):
        self.path = os.path.join(d, "index.csv")
        self.fields = fields
        new = not os.path.exists(self.path)
        self.f = open(self.path, "a", newline="", encoding="utf-8")
        self.w = csv.DictWriter(self.f, fieldnames=fields)
        if new:
            self.w.writeheader()

    def add(self, **row):
        self.w.writerow({k: row.get(k, "") for k in self.fields})
        self.f.flush()


# ---------------------------------------------------------------- Internet Archive

IA_ITEMS = [
    # Semanario del Nuevo Reyno de Granada (Bogota)
    "semanariodelnuev01unse", "semanariodelnuev02unse",
    # Gazeta do Rio de Janeiro 1808 issues and 1809 extracts
    "gazeta-do-rio-de-janeiro-1808", "gazeta_rj_1808_003", "gazeta_rj_1808_004",
    "gazeta_rj_1808_005", "gazeta_rj_extra_1808_002", "gazeta-rj-extra-1808-001-1",
    "gazetadelriojane00unkn", "gazetadelriojane00unkn_0", "gazetaextraordin00unkn",
    "gazetaextraordin00unkn_0", "gazetaextraordin00unkn_1", "gazetaextraordin00unkn_2",
    "extractodelagaze00unkn", "extractodelagaze00unkn_0", "extractodelagaze00unkn_1",
    "noticiasrecebida00unkn",
    # Gaceta de Caracas t. I (Oct 1808 - 1810) and t. II
    "gacetadecaracas0001vari", "gacetadecaracas0002vari",
    # Seville / Spanish gazettes 1808-09
    "gazetaministeria00unkn", "gazetaministeria00unkn_0", "gazetasextraordi00unkn",
    # O Telegrafo Portuguez (Lisbon 1808-09)
    "otelegrafoportug00unkn", "otelegrafoportug00unkn_0",
    # Correio Braziliense (London) - Google scans, years to be checked
    "correiobrazilie00unkngoog", "correiobrazilie01unkngoog", "correiobrazilie02unkngoog",
    "correiobrazilie03unkngoog", "correiobrazilie04unkngoog", "correiobrazilie05unkngoog",
    "correiobrazilie06unkngoog",
]


def ia_download(ident, d, idx, want_text=True):
    meta = fetch_json(f"https://archive.org/metadata/{ident}")
    if not meta or "files" not in meta:
        log(f"   - {ident}: no such item")
        idx.add(source="ia", id=ident, status="missing")
        return
    title = meta.get("metadata", {}).get("title", "")
    date = meta.get("metadata", {}).get("date", "")
    files = meta["files"]
    pdfs = [f["name"] for f in files if f["name"].lower().endswith(".pdf")]
    txts = [f["name"] for f in files if f["name"].endswith("_djvu.txt")]
    got = []
    for name in pdfs[:1] + (txts[:1] if want_text else []):
        dest = os.path.join(d, f"{ident}__{safe(name, 60)}")
        if os.path.exists(dest):
            got.append(os.path.basename(dest))
            continue
        url = f"https://archive.org/download/{ident}/{up.quote(name)}"
        if fetch(url, dest=dest, delay=0.5):
            got.append(os.path.basename(dest))
    log(f"   + {ident}: {title[:60]} [{date}] -> {', '.join(got) or 'nothing'}")
    idx.add(source="ia", id=ident, title=title, date=date, files=";".join(got),
            status="ok" if got else "failed")


def run_ia():
    d = outdir("internet_archive")
    idx = Index(d, ["source", "id", "title", "date", "files", "status"])
    log("== Internet Archive: fixed list of items")
    for ident in IA_ITEMS:
        ia_download(ident, d, idx)
    # Diario de Mallorca: one item per day, weather table on each
    dm = outdir("internet_archive/diario_de_mallorca")
    idx2 = Index(dm, ["source", "id", "title", "date", "files", "status"])
    log("== Internet Archive: Diario de Mallorca, one item per day")
    for day in days():
        ia_download(f"DiarioDeMallorca_{day:%Y%m%d}", dm, idx2, want_text=False)


# ---------------------------------------------------------------- direct file links

DIRECT = [
    # Correio Braziliense vol. II (Anno II, n.08-13, Jan-Jun 1809), Brasiliana USP facsimile.
    # The Internet Archive Google scans cover vols I, III, IV... but not vol. II.
    ("brasiliana_usp/Correio_Braziliense_v2_1809_Jan-Jun.pdf",
     "https://digital.bbm.usp.br/bitstream/bbm/6879/1/45000033194_Output.pdf"),   # 340 MB
]


def run_direct():
    log("== Direct downloads")
    for rel, url in DIRECT:
        dest = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.exists(dest):
            log(f"   = {rel} already here")
            continue
        ok = fetch(url, dest=dest)
        log(f"   {'+' if ok else '!'} {rel}")


# ---------------------------------------------------------------- DSpace 7 repositories

DSPACE = [
    # (folder, API base, search query)
    ("bnp_peru_minerva", "https://bibliotecadigital.bnp.gob.pe/server/api", "Minerva peruana"),
    ("uca_gazeta_guatemala", "https://repositorio.uca.edu.sv/server/api", "Gazeta de Guatemala"),
    ("udistrital_redactor", "https://repository.udistrital.edu.co/server/api", "Redactor Americano"),
]


def md(obj, key):
    v = obj.get("metadata", {}).get(key)
    return v[0]["value"] if v else ""


def dspace_base(base):
    """Return a working REST API base, trying common DSpace 7 locations."""
    site = base.split("/server/api")[0]
    cands = [base, site + "/rest/api", site + "/api", site + "/dspace-rest/api",
             site + "/server/server/api"]
    home = fetch(site + "/", tries=1)
    if home:
        for m in re.finditer(rb'"nameSpace"\s*:\s*"([^"]+)"', home):
            cands.insert(0, site + m.group(1).decode() + "/api")
        for m in re.finditer(rb'(https?://[^"\s]+?/server)/?["/]', home):
            cands.insert(0, m.group(1).decode() + "/api")
    for c in dict.fromkeys(cands):
        raw = fetch(c, tries=1, quiet404=True)
        try:
            j = json.loads(raw) if raw else None
        except ValueError:
            j = None
        if j and "_links" in j:
            if c != base:
                log(f"   REST API found at {c}")
            return c
    log(f"   ! no DSpace REST API found for {site}; saving home page")
    return None


def run_dspace(only=None, max_pages=60):
    for folder, base, q in DSPACE:
        if only and only != folder:
            continue
        base = dspace_base(base)
        if not base:
            continue
        d = outdir(folder)
        idx = Index(d, ["uuid", "title", "date", "in_window", "files", "url"])
        log(f"== DSpace: {folder} ({q})")
        page, total = 0, None
        while page < max_pages:
            url = (f"{base}/discover/search/objects?query={up.quote(q)}"
                   f"&dsoType=ITEM&size=50&page={page}")
            res = fetch_json(url)
            if not res:
                log("   ! search failed; saving raw response for diagnosis")
                raw = fetch(url)
                if raw:
                    open(os.path.join(d, f"_raw_search_p{page}.txt"), "wb").write(raw)
                break
            sr = res.get("_embedded", {}).get("searchResult", {})
            objs = sr.get("_embedded", {}).get("objects", [])
            if total is None:
                total = sr.get("page", {}).get("totalElements")
                log(f"   {total} results")
            if not objs:
                break
            for o in objs:
                it = o.get("_embedded", {}).get("indexableObject", {})
                uuid, title = it.get("uuid"), it.get("name", "")
                date = md(it, "dc.date.issued") or md(it, "dc.date.created") or md(it, "dc.date")
                win = in_window(date)
                if win is None:
                    m = re.search(r"(1808|1809)", title)
                    win = None if m else False
                files = []
                if win is not False:
                    files = dspace_bitstreams(base, uuid, d, f"{date}_{safe(title, 50)}")
                idx.add(uuid=uuid, title=title, date=date, in_window=win,
                        files=";".join(files), url=f"{base.replace('/server/api', '')}/items/{uuid}")
            page += 1


def dspace_bitstreams(base, uuid, d, stem):
    got = []
    bundles = fetch_json(f"{base}/core/items/{uuid}/bundles")
    if not bundles:
        return got
    for b in bundles.get("_embedded", {}).get("bundles", []):
        if b.get("name") != "ORIGINAL":
            continue
        bs = fetch_json(b["_links"]["bitstreams"]["href"] + "?size=100")
        for s in (bs or {}).get("_embedded", {}).get("bitstreams", []):
            name = s.get("name", s["uuid"])
            dest = os.path.join(d, safe(f"{stem}__{name}", 140))
            if not os.path.exists(dest):
                fetch(f"{base}/core/bitstreams/{s['uuid']}/content", dest=dest)
            if os.path.exists(dest):
                got.append(os.path.basename(dest))
    log(f"   + {stem}: {len(got)} file(s)")
    return got


# ---------------------------------------------------------------- BOE (Gazeta de Madrid, Seville gazettes)

BOE_SERIES = [
    # prefix, title, first day, last day, known (date, number) to seed the count
    ("GMD", "Gazeta de Madrid", dt.date(1808, 9, 1), dt.date(1810, 6, 30), (dt.date(1808, 8, 12), 112)),
    ("GMS", "Gazeta Ministerial de Sevilla", dt.date(1808, 9, 1), dt.date(1809, 1, 12), (dt.date(1808, 7, 20), 15)),
    ("GGB", "Gazeta del Gobierno (Junta Central)", dt.date(1809, 1, 6), dt.date(1809, 12, 30), (dt.date(1809, 1, 5), 0)),
    # Cadiz / Isla de Leon, 13 Mar 1810 - 25 Jan 1812; GEI-1810-110 is 20 Dec 1810
    ("GEI", "Gazeta de la Regencia de Espana e Indias", dt.date(1810, 3, 13), dt.date(1810, 6, 30), (dt.date(1810, 3, 12), 0)),
]

# BOE files these two papers under day folders that do not match the issue date
# (GGB-1809-7 sits under 1809/01/07 but is the issue of 10 Feb 1809), so they are
# fetched by issue number and saved without a date; read the date off page 1.
BOE_BY_NUMBER = {"GGB", "GEI"}


def boe_by_number(d, idx, prefix, title, lo, hi):
    year = lo.year
    day, n, misses, found = lo, 1, 0, 0
    while misses < 6 and day <= dt.date(year, 12, 31):
        name = f"{prefix}-{year}-{n}.pdf"
        dest = os.path.join(d, f"nodate__{name}")
        hit = os.path.exists(dest) or any(f.endswith("__" + name) for f in os.listdir(d))
        probe = day
        while not hit and probe <= min(day + dt.timedelta(days=30), dt.date(year, 12, 31)):
            url = f"https://www.boe.es/gazeta/dias/{probe:%Y/%m/%d}/pdfs/{name}"
            if fetch(url, dest=dest, tries=1, delay=0.3, quiet404=True):
                if open(dest, "rb").read(4) == b"%PDF":
                    hit, day = True, probe
                    break
                os.remove(dest)
            probe += dt.timedelta(days=1)
        if hit:
            found += 1
            misses = 0
            idx.add(date="", series=prefix, pdf=f"{prefix}-{year}-{n}", status="ok (by number)")
            log(f"   {prefix} No. {n} (BOE folder {day})")
        else:
            misses += 1
            log(f"   {prefix} No. {n}: not found")
        n += 1
    log(f"   {title}: {found} issues found (named by number; dates must be read from the pages)")


def run_boe():
    """BOE Gazeta PDFs: boe.es/gazeta/dias/YYYY/MM/DD/pdfs/<PREFIX>-YYYY-<N>.pdf (N not zero-padded).

    Issue numbers run on from the last issue found, and restart at 1 in January.
    Known: GMD-1808-112 (12 Aug 1808), GMD-1808-156 (16 Dec 1808), GMD-1809-157 (6 Jun 1809),
    GMS-1808-15 (20 Jul 1808), GGB-1809-1 (8 Jan 1809). Not every day has an issue.
    """
    d = outdir("boe_gazetas")
    idx = Index(d, ["date", "series", "pdf", "status"])
    log("== BOE: Gazeta de Madrid, Gazeta Ministerial de Sevilla, Gazeta del Gobierno")
    for prefix, title, first, last_day, (seed_date, seed_n) in BOE_SERIES:
        log(f"-- {title} ({prefix})")
        if prefix in BOE_BY_NUMBER:
            boe_by_number(d, idx, prefix, title, max(first, START), min(last_day, END))
            continue
        lo, hi = max(first, START), min(last_day, END)
        last_n, last_hit = seed_n, seed_date
        found = 0
        day = lo
        while day <= hi:
            if day.year != last_hit.year:            # new year: numbering may restart
                cands = list(range(1, 6)) + list(range(last_n + 1, last_n + 6))
            else:
                gap = (day - last_hit).days
                width = min(4 + 2 * gap, 40)
                cands = list(range(last_n + 1, last_n + 1 + width))
            if prefix == "GMD" and day.year >= 1809:   # 1809-10 Madrid numbers track the day of year
                doy = day.timetuple().tm_yday
                cands = list(range(doy - 3, doy + 4)) + cands
            hit = None
            for n in dict.fromkeys(c for c in cands if c > 0):
                name = f"{prefix}-{day.year}-{n}.pdf"
                dest = os.path.join(d, f"{day}__{name}")
                if os.path.exists(dest):
                    hit = n
                    break
                url = f"https://www.boe.es/gazeta/dias/{day:%Y/%m/%d}/pdfs/{name}"
                if fetch(url, dest=dest, tries=1, delay=0.3, quiet404=True):
                    if open(dest, "rb").read(4) != b"%PDF":
                        os.remove(dest)
                        continue
                    hit = n
                    break
            if hit:
                last_n, last_hit = hit, day
                found += 1
                idx.add(date=day, series=prefix, pdf=f"{prefix}-{day.year}-{hit}", status="ok")
                log(f"   {day}: {prefix} No. {hit}")
            day += dt.timedelta(days=1)
        log(f"   {title}: {found} issues found")


# ---------------------------------------------------------------- Gallica (French papers): OCR text per issue

GALLICA_TITLES = ["Gazette de France", "Journal de l'Empire",
                  "Gazette nationale ou le Moniteur universel", "Journal de Paris"]


def run_gallica(pdf=False):
    d = outdir("gallica")
    idx = Index(d, ["title", "date", "ark", "files"])
    log("== Gallica: issue OCR text" + (" + PDF" if pdf else ""))
    for t in GALLICA_TITLES:
        q = (f'dc.title all "{t}" and dc.type all "fascicule" and '
             f'gallicapublication_date>="{START:%Y/%m/%d}" and '
             f'gallicapublication_date<="{END:%Y/%m/%d}"')
        startrec = 1
        while True:
            url = ("https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2"
                   f"&maximumRecords=50&startRecord={startrec}&query={up.quote(q)}")
            x = fetch(url, delay=4)
            if x is None:
                break
            x = x.decode("utf-8", "replace")
            if startrec == 1:
                n = re.search(r"<srw:numberOfRecords>(\d+)", x)
                log(f"   {t}: {n.group(1) if n else '?'} issues in window")
                if not n or n.group(1) == "0":
                    open(os.path.join(d, f"_raw_{safe(t)}.xml"), "w").write(x)
            recs = re.findall(r"<srw:record>(.*?)</srw:record>", x, re.S)
            if not recs:
                break
            for r in recs:
                ark = re.search(r"ark:/12148/(bpt6k\w+)", r)
                date = re.search(r"<dc:date>([^<]+)</dc:date>", r)
                if not ark:
                    continue
                ark, date = ark.group(1), (date.group(1) if date else "")
                stem = os.path.join(d, f"{safe(t, 30)}_{date}_{ark}")
                files = []
                if not os.path.exists(stem + ".txt"):
                    fetch(f"https://gallica.bnf.fr/ark:/12148/{ark}.texteBrut",
                          dest=stem + ".txt", delay=4)
                if os.path.exists(stem + ".txt"):
                    files.append(stem + ".txt")
                if pdf and not os.path.exists(stem + ".pdf"):
                    fetch(f"https://gallica.bnf.fr/ark:/12148/{ark}.pdf", dest=stem + ".pdf", delay=4)
                idx.add(title=t, date=date, ark=ark, files=";".join(os.path.basename(f) for f in files))
            startrec += 50


# ---------------------------------------------------------------- Delpher (Dutch papers): keyword hits

DELPHER_TERMS = ["vulkaan", "volkaan", "vulcaan", "volcaan", "brandende berg", "vuurspuwende",
                 "vuurbraakende", "aardbeving", "aardbeeving", "aschregen", "asregen",
                 "uitbarsting", "uitbersting", "Java", "Bali", "Banda", "Ternate"]
DELPHER_DATE = None   # chosen by calibration: a query form that returns 1808-09 records


def delpher_query(term):
    return DELPHER_DATE.format(term=term)


def delpher_calibrate():
    """Find which date syntax the KB SRU accepts, using a word common in 1808 papers."""
    global DELPHER_DATE
    forms = ['"{term}" and date within "%s %s"' % (START.strftime("%d-%m-%Y"), END.strftime("%d-%m-%Y")),
             '"{term}" and date >= "%s" and date <= "%s"' % (START.strftime("%d-%m-%Y"), END.strftime("%d-%m-%Y")),
             '"{term}" and date within "%s %s"' % (START.strftime("%Y-%m-%d"), END.strftime("%Y-%m-%d")),
             '"{term}" and date = "1808" or "{term}" and date = "1809"']
    for f in forms:
        q = f.format(term="Batavia")
        x = fetch("https://jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve"
                  f"&x-collection=DDD_artikel&maximumRecords=3&query={up.quote(q)}")
        n = re.search(rb"<srw:numberOfRecords>(\d+)", x or b"")
        dates = re.findall(rb"<dc:date>([^<]+)", x or b"")
        log(f"   calibrate [{f}]: {n.group(1).decode() if n else '?'} records, sample dates {dates[:3]}")
        if n and int(n.group(1)) > 0 and dates and all(d[:4] in (b"1808", b"1809") for d in dates):
            DELPHER_DATE = f
            return True
    DELPHER_DATE = '"{term}"'
    log("   ! no date syntax worked; searching without a date limit and filtering locally")
    return False


def run_delpher():
    d = outdir("delpher")
    idx = Index(d, ["term", "date", "paper", "title", "url"])
    log("== Delpher: keyword search in newspapers")
    delpher_calibrate()
    for term in DELPHER_TERMS:
        q = delpher_query(term)
        url = ("https://jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve"
               "&x-collection=DDD_artikel&recordSchema=ddd&maximumRecords=1000"
               f"&query={up.quote(q)}")
        x = fetch(url)
        if x is None:
            continue
        x = x.decode("utf-8", "replace")
        open(os.path.join(d, f"_raw_{safe(term)}.xml"), "w").write(x)
        recs = re.findall(r"<srw:recordData>(.*?)</srw:recordData>", x, re.S)
        log(f"   {term}: {len(recs)} hit(s)")
        for r in recs:
            g = lambda tag: (re.search(rf"<{tag}[^>]*>([^<]*)</{tag}>", r) or [None, ""])[1]
            ident = g("dc:identifier")
            if in_window(g("dc:date").replace("/", "-")[:10]) is False:
                continue
            idx.add(term=term, date=g("dc:date"), paper=g("ddd:papertitle"),
                    title=g("dc:title"), url=ident)
            if ident:
                urn = re.search(r"urn=([^&]+)", ident)
                if urn:
                    dest = os.path.join(d, safe(f"{g('dc:date')}_{urn.group(1)}", 120) + ".xml")
                    if not os.path.exists(dest):
                        fetch(f"https://resolver.kb.nl/resolve?urn={urn.group(1)}:ocr", dest=dest)


# ---------------------------------------------------------------- Trove (Sydney Gazette)

TROVE_TERMS = ["volcano", "earthquake", "eruption", "fog", "haze", "sun", "ashes", "comet",
               "pumice", "darkness", "atmosphere", "phenomenon", "smoke", "sealing", "Macquarie", "Campbell",
               "eclipse", "moon"]


def run_trove():
    key = os.environ.get("TROVE_KEY")
    d = outdir("trove_sydney_gazette")
    if not key:
        log("== Trove skipped: set TROVE_KEY (free key from trove.nla.gov.au, 'API' page) to run it")
        return
    idx = Index(d, ["term", "date", "heading", "id", "url"])
    log("== Trove: Sydney Gazette (title 3) article text")
    for term in TROVE_TERMS:
        url = ("https://api.trove.nla.gov.au/v3/result?category=newspaper&encoding=json"
               f"&q={up.quote(term)}&l-title=3&l-decade=180&n=100&include=articletext"
               f"&l-year=1808&l-year=1809")
        res = fetch_json(url, headers={"X-API-KEY": key})
        if not res:
            continue
        arts = []
        for c in res.get("category", []):
            arts += c.get("records", {}).get("article", [])
        log(f"   {term}: {len(arts)} article(s)")
        for a in arts:
            if in_window(a.get("date", "")) is False:
                continue
            dest = os.path.join(d, f"{a.get('date')}_{a.get('id')}.txt")
            with open(dest, "w") as f:
                f.write(a.get("heading", "") + "\n\n" + re.sub("<[^>]+>", "\n", a.get("articleText", "")))
            idx.add(term=term, date=a.get("date"), heading=a.get("heading"), id=a.get("id"),
                    url=a.get("troveUrl"))


# ---------------------------------------------------------------- HNDM Mexico (pages for building the downloader)

def run_hndm():
    d = outdir("_probe/hndm")
    base = "https://hndm.iib.unam.mx/consulta/"
    log("== HNDM: saving search pages for 1808-09 and titles G/D")
    pages = {
        "anio1808": (base + "busqueda/buscarPorRangoDeFecha", "anio=1808"),
        "anio1809": (base + "busqueda/buscarPorRangoDeFecha", "anio=1809"),
        "letraG": (base + "busqueda/buscarPorLetra?letra=G", None),
        "letraD": (base + "busqueda/buscarPorLetra?letra=D", None),
        "palabra_volcan": (base + "busqueda/buscarPalabras", "palabras=volcan"),
    }
    for name, (url, data) in pages.items():
        b = fetch(url, data=data)
        if not b:
            continue
        open(os.path.join(d, name + ".html"), "wb").write(b)
        n = 0
        for l in dict.fromkeys(re.findall(rb'href="([^"]+)"', b)):
            s = html.unescape(l.decode("utf-8", "replace"))
            if re.search(r"(publicacion|ejemplar|visor|pdf|Gazeta|Diario|1808|1809)", s, re.I) and n < 25:
                full = up.urljoin(url, s)
                bb = fetch(full, tries=1)
                if bb:
                    open(os.path.join(d, f"{name}_link{n}.html"), "wb").write(bb[:3_000_000])
                    open(os.path.join(d, f"{name}_link{n}.url"), "w").write(full)
                    n += 1
        log(f"   {name}: {len(b)} bytes, followed {n} links")


HNDM_PUBS = {
    "gazeta_de_mexico": "558075be7d1e63c9fea1a2b0",   # 1784-01-14 .. 1809-12-02
    "diario_de_mexico": "558075be7d1e63c9fea1a213",   # 1805-10-01 ..
    "gazeta_del_gobierno_de_mexico": "558075be7d1e63c9fea1a2a1",   # 1810-01-02 .. 1821-09-29 (successor of the Gazeta)
}


def run_hndm_download(only=None, first_item_only=False):
    base = "https://hndm.iib.unam.mx"
    for name, pub in HNDM_PUBS.items():
        if only and only != name:
            continue
        d = outdir(f"hndm/{name}")
        idx = Index(d, ["date", "item", "pages", "files"])
        log(f"== HNDM: {name}")
        b = fetch(f"{base}/consulta/publicacion/listItems/{pub}?offset=0&max=5000")
        if not b:
            continue
        s = b.decode("utf-8", "replace")
        items = re.findall(r"Fecha del fasc[^<]*</dt>\s*<dd>([\d-]+)</dd>.*?item/visualizar/([0-9a-f]{24})", s, re.S)
        items = [(dte, it) for dte, it in items if in_window(dte)]
        log(f"   {len(items)} issues in window")
        for dte, it in items[:1] if first_item_only else items:
            # the publication viewer is a plain GET form: anio, mes, dia, pagina
            y, m, dd = dte.split("-")
            got, npages, n = [], 1, 1
            while n <= npages:
                url = (f"{base}/consulta/publicacion/visualizar/{pub}?coleccion=&anio={y}"
                       f"&mes={m}&dia={dd}&pagina={n}")
                page = fetch(url)
                if not page:
                    break
                p = page.decode("utf-8", "replace")
                if n == 1:
                    mm = re.search(r"esNumeroPos\(this,(\d+),", p)
                    npages = int(mm.group(1)) if mm else 1
                    if first_item_only:
                        open(os.path.join(d, f"_viewer_{dte}.html"), "w").write(p)
                pid = re.search(r"/consulta/publicacion/pdf/([0-9a-f]{24})\.pdf", p)
                if pid:
                    dest = os.path.join(d, f"{dte}_p{n:02d}.pdf")
                    if os.path.exists(dest) or fetch(f"{base}/consulta/publicacion/pdf/{pid.group(1)}.pdf", dest=dest):
                        got.append(os.path.basename(dest))
                n += 1
            log(f"   {dte}: {len(got)} of {npages} page PDF(s)")
            idx.add(date=dte, item=it, pages=npages, files=";".join(got))


# ---------------------------------------------------------------- probe: sites with no public API

PROBES = {
    "bne_el_aviso": ["https://hemerotecadigital.bne.es/hd/es/issn/2219-7982"],
    "hemeroteca_brasileira": [
        "https://memoria.bn.gov.br/DocReader/DocReader.aspx?bib=749664",
        "https://memoria.bn.gov.br/DocReader/DocReader.aspx?bib=749664&pasta=ano%20180&pesq=",
    ],
    "hndm_mexico": ["https://hndm.iib.unam.mx/consulta/busqueda",
                    "https://hndm.iib.unam.mx/consulta/accesoDirecto/lineaDelTiempo"],
    "prensa_historica": [
        "https://prensahistorica.mcu.es/latinoamerica/en/publicaciones/listar_numeros.do"],
    "bnp_peru_html": ["https://bibliotecadigital.bnp.gob.pe/items/077be426-4904-4812-9771-fac566560f5e"],
}


def run_probe():
    """Save the raw pages of sites without an API so the downloaders can be written."""
    d = outdir("_probe")
    log("== Probe: saving raw pages for sites that need custom downloaders")
    for name, urls in PROBES.items():
        for i, url in enumerate(urls):
            b = fetch(url)
            dest = os.path.join(d, f"{name}_{i}.html")
            if b:
                open(dest, "wb").write(b)
                links = set(re.findall(rb'(?:href|src)="([^"]+)"', b))
                log(f"   {name}_{i}: {len(b)} bytes, {len(links)} links")
                # follow one level of links that look like issue lists, calendars or PDFs
                n = 0
                for l in sorted(links):
                    s = html.unescape(l.decode("utf-8", "replace"))
                    if re.search(r"(1808|1809|calend|ejemplar|pdf|pasta|issue|numero)", s, re.I) and n < 15:
                        full = up.urljoin(url, s)
                        bb = fetch(full)
                        if bb:
                            open(os.path.join(d, f"{name}_{i}_link{n}.html"), "wb").write(bb[:3_000_000])
                            open(os.path.join(d, f"{name}_{i}_link{n}.url"), "w").write(full)
                            n += 1
            else:
                log(f"   {name}_{i}: FAILED")


# ---------------------------------------------------------------- main

SOURCES = {
    "ia": run_ia,
    "direct": run_direct,
    "dspace": run_dspace,
    "boe": run_boe,
    "gallica": run_gallica,
    "delpher": run_delpher,
    "trove": run_trove,
    "probe": run_probe,
    "hndm": run_hndm,
    "mexico": run_hndm_download,
}


def run_test():
    """One small request per site, so we learn what works from your connection."""
    global END
    log("== TEST: one small request per site")
    checks = [
        ("Internet Archive", "https://archive.org/metadata/semanariodelnuev02unse"),
        ("BNP Peru (DSpace API)", DSPACE[0][1] + "/discover/search/objects?query=Minerva%20peruana&size=1"),
        ("UCA El Salvador (DSpace API)", DSPACE[1][1] + "/discover/search/objects?query=Gazeta%20de%20Guatemala&size=1"),
        ("U. Distrital (DSpace API)", DSPACE[2][1] + "/discover/search/objects?query=Redactor&size=1"),
        ("BOE day page", "https://www.boe.es/gazeta/dias/1809/01/10/"),
        ("Gallica SRU", "https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=1&query=dc.title%20all%20%22Gazette%20de%20France%22"),
        ("Delpher SRU", "https://jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve&x-collection=DDD_artikel&maximumRecords=1&query=vulkaan"),
        ("BNE Hemeroteca", "https://hemerotecadigital.bne.es/hd/es/issn/2219-7982"),
        ("Hemeroteca Brasileira", "https://memoria.bn.gov.br/DocReader/DocReader.aspx?bib=749664"),
        ("HNDM Mexico", "https://hndm.iib.unam.mx/consulta/busqueda"),
        ("Prensa Historica", "https://prensahistorica.mcu.es/latinoamerica/en/publicaciones/listar_numeros.do"),
    ]
    d = outdir("_test")
    for name, url in checks:
        b = fetch(url, tries=1)
        status = f"OK {len(b)} bytes" if b else "FAILED"
        log(f"   {name:32s} {status}")
        if b:
            open(os.path.join(d, safe(name) + ".txt"), "wb").write(b[:500_000])
    run_probe()
    log("== TEST done. Tell Claude in the thread; it will read run_log.txt and _test/, _probe/.")


def run_test2():
    """Second check after the first test: the fixed BOE, UCA and Delpher parts plus HNDM pages."""
    global START, END
    log("== TEST 2")
    saved = START, END
    START, END = dt.date(1809, 6, 5), dt.date(1809, 6, 7)   # 6 Jun 1809 is Gazeta No. 157
    run_boe()
    log("   UCA API:", dspace_base(DSPACE[1][1]))
    START, END = saved
    DELPHER_TERMS[:] = ["aardbeving"]
    run_delpher()
    run_hndm()
    log("== TEST 2 done. Tell Claude in the thread.")


def run_test3():
    """Third check: Delpher date syntax and one Mexico issue."""
    log("== TEST 3")
    delpher_calibrate()
    run_hndm_download(first_item_only=True)
    log("== TEST 3 done. Tell Claude in the thread.")


def main():
    global LOG
    arg = sys.argv[1] if len(sys.argv) > 1 else "test"
    LOG = open(os.path.join(ROOT, "run_log.txt"), "a", encoding="utf-8")
    log(f"\n#### {dt.datetime.now():%Y-%m-%d %H:%M} run: {' '.join(sys.argv[1:]) or 'test'}"
        f"  window {START}..{END}")
    if arg == "test":
        run_test()
    elif arg == "test2":
        run_test2()
    elif arg == "test3":
        run_test3()
    elif arg == "all":
        for k in ("ia", "direct", "dspace", "boe", "delpher", "mexico", "trove"):
            try:
                SOURCES[k]()
            except Exception as e:   # keep going with the next source
                log(f"!! {k} crashed: {e!r}")
    elif arg == "gallica-pdf":
        run_gallica(pdf=True)
    elif arg in SOURCES:
        SOURCES[arg]()
    else:
        print(__doc__)
        print("sources:", ", ".join(SOURCES), "| test | all | gallica-pdf")


if __name__ == "__main__":
    main()
