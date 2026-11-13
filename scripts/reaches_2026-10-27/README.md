REACHES (Wang et al. 2018/2023; NOAA study 23410, CC0) extraction, 27 Oct 2026.
Inputs (downloaded by William to ~/Downloads/1808-9 volcano research/data/reaches/): reachesv3.1data.txt (Chinese text lost as "?"), reachesv3.1codes-*.txt, noaa-reaches-vol234.xlsx (has province, county, source).
x2.py: xlsx Data sheet -> rows 1806-1811 (x1806.tsv). dec.py holds the hand-built code dictionary (main + subcategory). dec2.py: window Jul 1808-Jun 1810 with names and sources. base.py: per-year counts 1780-1840 (late-spring cold south of 32N; winter cold south of 25.5N by season start year; sky-colour codes without wind/dust; GD/GX drought+famine sites).
Run: python3 -I x2.py <xlsx> <S>/x1806.tsv ; python3 -I dec2.py <S> ; python3 -I base.py <dir with reachesv3.1data.txt>
