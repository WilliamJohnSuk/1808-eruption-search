#!/usr/bin/env python3
"""Build community/seed_posts_2026-11-15.json from the approved seed-post files.

Reads community/discussion_seed_posts_2026-11-04.md (sections 1-8) and
community/seed_post_method_ai_human_check_F15_2026-11-15.md. Polls are left
out: GitHub's API cannot create polls (see POLLS_PASTE.md).
Run from the repository root: python3 scripts/post_discussions_2026-11-15/build_posts.py
"""
import json, re

SLUGS = {"Announcements": "announcements", "Start here": "start-here",
         "Candidate volcanoes": "candidate-volcanoes", "Evidence review": "evidence-review",
         "Polls": "polls", "Sources and archives": "sources-and-archives",
         "Method and AI": "method-and-ai", "Translation help": "translation-help"}
CAND = {"Dakataua": "candidate:dakataua", "Gaua": "candidate:gaua", "Cabalían": "candidate:cabalian",
        "Agung": "candidate:agung", "Todoko-Ranu": "candidate:todoko-ranu", "Dukono": "candidate:dukono",
        "Teon": "candidate:teon", "Nila": "candidate:nila", "Northern Sulawesi": "candidate:north-sulawesi",
        "Karthala": "candidate:other"}

text = open("community/discussion_seed_posts_2026-11-04.md", encoding="utf-8").read()
posts = []
for sec in re.split(r"\n## \d\. ", text)[1:]:
    name, body = sec.split("\n", 1)
    slug = SLUGS[name.strip()]
    if slug == "polls":
        continue
    body = body.strip().rstrip("-").strip()
    chunks = re.split(r"\n(?=\*\*[^*\n]+\*\*[^\n]*\n\n)", "\n" + body)
    for ch in chunks:
        ch = ch.strip()
        m = re.match(r"\*\*([^*\n]+)\*\*([^\n]*)\n\n(.*)", ch, re.S)
        if not m:
            continue  # section intro text, not a post
        title = (m.group(1) + m.group(2)).replace("(pin)", "").strip()
        b = m.group(3).strip().rstrip("-").strip()
        labels = ["ai-generated"]
        for k, v in CAND.items():
            if slug == "candidate-volcanoes" and title.startswith(k):
                labels.append(v)
        if slug == "evidence-review":
            labels.append("finding")
        posts.append({"category": slug, "title": title, "body": b, "labels": labels,
                      "pin": slug == "announcements"})

f15 = open("community/seed_post_method_ai_human_check_F15_2026-11-15.md", encoding="utf-8").read()
f15 = f15.split("---", 2)[2].strip()
t = re.match(r"\*\*Title:\*\* (.+)\n", f15)
f15_post = {"category": "method-and-ai", "title": t.group(1).strip(), "body": f15[t.end():].strip(),
            "labels": ["ai-generated", "correction"], "pin": False}
i = next(n for n, p in enumerate(posts) if p["category"] == "method-and-ai")
posts.insert(i, f15_post)  # post the F15 story first; the next post refers to it

json.dump(posts, open("community/seed_posts_2026-11-15.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(posts), "posts:", dict(Counter(p["category"] for p in posts)))
