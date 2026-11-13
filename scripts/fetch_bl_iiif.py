#!/usr/bin/env python3
"""Download every page image of a British Library manuscript from its IIIF manifest.

Written 4 Nov 2026 for BL Add MS 12350 (Bugis diary of Bone, 1808 to 9 July 1809,
and Jul-Aug 1812), which the BL marks Public Domain. See unavailable_sources.md U34
and notes/wide_source_search_2026-11-04.md section 9.8.

Usage (run from the project's scripts/ folder; Python 3 standard library only):

    python3 fetch_bl_iiif.py
    python3 fetch_bl_iiif.py MANIFEST_URL OUT_DIR [WIDTH [FIRST LAST]]

FIRST and LAST (optional) are canvas numbers, counted from 1, to fetch only part
of a long volume. For Add MS 12357 (Bone diary 1795-1812, 413 folios; image count unconfirmed) run
the script once with WIDTH 400 to get small previews of every page, find the
1808-1809 pages (Omar 2003 says the Christian dates are on the left-hand pages, with month
names usually in Portuguese; not yet checked for this volume), then fetch that range
again at 2000 into a second folder.

    python3 fetch_bl_iiif.py https://bl.digirati.io/iiif/ark:/81055/vdc_100126474616.0x000001 ../archives/BL_Add_MS_12357_preview 400

The defaults fetch Add MS 12350 into ../archives/BL_Add_MS_12350/ at 2000 px wide,
the largest size the server allows. Files are named NNN_<canvas label>.jpg, and the
script skips files that already exist, so it can be re-run after an interruption.
It waits 1 s between images to be polite to the server.
"""
import json
import os
import re
import sys
import time
import urllib.request

DEFAULT_MANIFEST = "https://bl.digirati.io/iiif/ark:/81055/vdc_100101830026.0x000001"
DEFAULT_OUT = os.path.join("..", "archives", "BL_Add_MS_12350")
UA = {"User-Agent": "1808-eruption-research/1.0 (IIIF page download)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def label_text(label):
    # IIIF v2 labels are strings; v3 labels are {"en": ["..."]} or similar.
    if isinstance(label, str):
        return label
    if isinstance(label, dict):
        for v in label.values():
            if v:
                return v[0]
    if isinstance(label, list) and label:
        return label_text(label[0])
    return "page"


def image_services(manifest):
    """Yield (label, service_base) for each canvas, IIIF v2 or v3."""
    if "sequences" in manifest:  # v2
        for canvas in manifest["sequences"][0]["canvases"]:
            img = canvas["images"][0]["resource"]
            svc = img.get("service", {})
            if isinstance(svc, list):
                svc = svc[0]
            base = svc.get("@id") or svc.get("id")
            yield label_text(canvas.get("label")), base
    else:  # v3
        for canvas in manifest.get("items", []):
            anno = canvas["items"][0]["items"][0]
            body = anno["body"]
            svc = body.get("service", [{}])
            if isinstance(svc, list):
                svc = svc[0]
            base = svc.get("@id") or svc.get("id")
            yield label_text(canvas.get("label")), base


def main():
    manifest_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MANIFEST
    out = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT
    width = sys.argv[3] if len(sys.argv) > 3 else "2000"
    first = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    last = int(sys.argv[5]) if len(sys.argv) > 5 else 10**6
    os.makedirs(out, exist_ok=True)
    manifest = json.loads(get(manifest_url))
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    pages = list(image_services(manifest))
    print(f"{len(pages)} canvases in manifest")
    for n, (label, base) in enumerate(pages, 1):
        if n < first or n > last:
            continue
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", label).strip("_")[:40]
        path = os.path.join(out, f"{n:03d}_{safe}.jpg")
        if os.path.exists(path) and os.path.getsize(path) > 10000:
            continue
        url = f"{base}/full/{width},/0/default.jpg"
        try:
            data = get(url)
        except Exception as e:  # keep going; re-run picks up gaps
            print(f"FAILED {n} {label}: {e}")
            continue
        with open(path, "wb") as f:
            f.write(data)
        print(f"{n:03d} {label} {len(data)//1024} KB")
        time.sleep(1)
    print("done:", out)


if __name__ == "__main__":
    main()
