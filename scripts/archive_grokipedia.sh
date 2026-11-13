#!/bin/zsh
# archive_grokipedia.sh - time-stamped archive of the Grokipedia "1808 mystery eruption" page,
# related Grokipedia pages, and every page it cites as evidence. Written by Claude for William John Suk, 12 Nov 2026.
# Run on William's Mac from the project's scripts/ folder:  zsh archive_grokipedia.sh        (add --no-wayback to skip Wayback saves)
# Output: ../archives/grokipedia/<UTC timestamp>/ with raw HTML, response headers, SHA-256 hashes and manifest.csv.
# Each run makes a new folder, so runs can be diffed later (diff -r, or ask Claude).
set -u
setopt no_glob   # URLs contain ? and = (zsh would treat them as wildcards)
WAYBACK=1; [[ "${1:-}" == "--no-wayback" ]] && WAYBACK=0
TS=$(date -u +%Y-%m-%dT%H%M%SZ)
OUT="../archives/grokipedia/$TS"; mkdir -p "$OUT/grokipedia" "$OUT/evidence"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
echo "kind,url,file,http_code,bytes,sha256,fetched_utc" > "$OUT/manifest.csv"

GROK=(
 https://grokipedia.com/page/1808_mystery_eruption
 https://grokipedia.com/page/Agrihan
 https://grokipedia.com/page/Agrigan
 https://grokipedia.com/page/Tambo_Quemado
 https://grokipedia.com/page/Unexplained_volcanic_eruption
 https://grokipedia.com/page/Zavaritski_Caldera
 https://grokipedia.com/page/Year_Without_a_Summer
 https://grokipedia.com/robots.txt
 https://grokipedia.com/sitemap.xml
)
# The 38 references listed on the 1808 page (read 12 Nov 2026), plus pages we used to check its claims
EVID=(
 https://cp.copernicus.org/articles/10/1707/2014/cp-10-1707-2014.pdf
 https://www.sciencedaily.com/releases/2014/09/140918111220.htm
 https://climate.envsci.rutgers.edu/pdf/StateOfThePlanet5.pdf
 https://online.ucpress.edu/elementa/article/10/1/00047/195026/Stratospheric-aerosol-injection-may-impact-global
 https://publikationen.bibliothek.kit.edu/1000062918/4387356
 https://www.science.smith.edu/climatelit/the-effects-of-the-little-ice-age/
 https://climate.envsci.rutgers.edu/pdf/Schmidt2012JD018414.pdf
 https://pmc.ncbi.nlm.nih.gov/articles/PMC9985606/
 https://opensky.ucar.edu/system/files/2024-08/articles_18555.pdf
 https://adsabs.harvard.edu/full/1986AREPS..14..267D
 https://adsabs.harvard.edu/full/1988AREPS..16...73R
 http://www.geo.utexas.edu/courses/387H/Lectures/AR4WG1_Print_Ch06.pdf
 https://pmc.ncbi.nlm.nih.gov/articles/PMC2527990/
 https://www.climate.gov/news-features/blogs/beyond-data/how-tree-rings-tell-time-and-climate-history
 https://doi.org/10.1029/91JD01634
 https://doi.org/10.1029/2006GL026013
 https://doi.org/10.5194/cp-17-1455-2021
 https://doi.org/10.1038/nature14565
 https://doi.org/10.1029/2006GL028033
 https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022PA004581
 https://cp.copernicus.org/articles/17/1455/2021/
 https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014PA002717
 https://doi.org/10.5194/cp-10-1707-2014
 https://doi.org/10.5194/cp-10-359-2014
 https://doi.org/10.1029/2008JD010185
 https://volcano.si.edu/volcano.cfm?vn=382030
 https://volcano.si.edu/volcano.cfm?vn=273070
 https://volcano.si.edu/volcano.cfm?vn=264020
 https://volcano.si.edu/volcano.cfm?vn=233010
 https://www.volcanocafe.org/tambo-quemado-the-eruption-of-1808/
 https://volcano.si.edu/volcano.cfm?vn=355021
 https://www.nature.com/articles/s41561-019-0402-y
 https://cp.copernicus.org/articles/21/1521/2025/
 https://www.sciencedirect.com/science/article/pii/S0277379122005674
 https://www.oeschger.unibe.ch/e54522/e54528/e118437/e185340/e1385294/e1385295/e1385298/VICS_Workshop_Programme_AbstractBook_080523_eng.pdf
 https://e5k.github.io/IAVCEI-SA2025/abstracts/6-1-11/
 https://ceoas.oregonstate.edu/reu-2023-projects
 https://www.pnas.org/doi/10.1073/pnas.2416699122
 https://volcano.si.edu/volcano.cfm?vn=284160
 https://www.usgs.gov/volcanoes/agrigan
 https://www.lawfaremedia.org/article/grokipedia-stopped-reviewing-edits-in-april.-it-didn-t-tell-anyone
)

grab () { # kind url
  local kind=$1 url=$2 name file code
  name=$(print -r -- "$url" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]+#_#g' | cut -c1-150)
  file="$OUT/$kind/$name"
  code=$(curl -sS -L -m 90 -A "$UA" -D "$file.headers.txt" -o "$file" -w '%{http_code}' "$url" 2>>"$OUT/errors.txt")
  local bytes=$(stat -f%z "$file" 2>/dev/null || echo 0)
  local sha=$(shasum -a 256 "$file" 2>/dev/null | cut -d' ' -f1)
  echo "$kind,\"$url\",$kind/$name,$code,$bytes,$sha,$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$OUT/manifest.csv"
  echo "$code  $bytes  $url"
}
for u in $GROK; do grab grokipedia "$u"; sleep 2; done
for u in $EVID; do grab evidence "$u"; sleep 1; done

# Independent public timestamps: ask the Internet Archive to capture each Grokipedia page (slow; about 10 s each)
if (( WAYBACK )); then
  echo "url,wayback_status,capture_location" > "$OUT/wayback.csv"
  for u in $GROK; do
    loc=$(curl -sS -m 120 -A "$UA" -o /dev/null -D - "https://web.archive.org/save/$u" 2>>"$OUT/errors.txt" | awk 'tolower($1)=="location:"||tolower($1)=="content-location:"{print $2}' | tr -d '\r' | head -1)
    echo "\"$u\",done,\"$loc\"" >> "$OUT/wayback.csv"; echo "wayback: $u $loc"; sleep 10
  done
fi
echo "\nSaved to $OUT  (manifest.csv lists every file with its SHA-256)."
