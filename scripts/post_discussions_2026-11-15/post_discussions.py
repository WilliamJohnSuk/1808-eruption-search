#!/usr/bin/env python3
"""Post the approved seed Discussions to WilliamJohnSuk/1808-eruption-search.

Run on the maintainer's Mac (needs the GitHub CLI `gh`, logged in as the repo owner).
  python3 post_discussions.py seed_posts_2026-11-15.json            # dry run: lists what would be posted
  python3 post_discussions.py seed_posts_2026-11-15.json --post     # posts for real

- Posts in file order, a few seconds apart.
- Skips any post whose title already exists as a Discussion, so it is safe to run again.
- Adds the labels named in the file (e.g. ai-generated); a missing label is reported, not fatal.
- Polls are not in the file: GitHub's API cannot create polls (see POLLS_PASTE.md).
- Pinning is done by hand afterwards (open the post, "Pin discussion" in the right sidebar).
"""
import json, subprocess, sys, time

OWNER, NAME = "WilliamJohnSuk", "1808-eruption-search"


def gql(query, **variables):
    payload = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(["gh", "api", "graphql", "--input", "-"], input=payload,
                       capture_output=True, text=True)
    out = json.loads(r.stdout or "{}")
    if r.returncode != 0 or out.get("errors"):
        raise RuntimeError(out.get("errors") or r.stderr)
    return out["data"]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    posts = json.load(open(sys.argv[1], encoding="utf-8"))
    really = "--post" in sys.argv

    d = gql("""query($o:String!,$n:String!){ repository(owner:$o,name:$n){ id
        discussionCategories(first:50){ nodes{ id slug name } }
        labels(first:100){ nodes{ id name } } } }""", o=OWNER, n=NAME)["repository"]
    repo_id = d["id"]
    cats = {c["slug"]: c["id"] for c in d["discussionCategories"]["nodes"]}
    labels = {l["name"]: l["id"] for l in d["labels"]["nodes"]}

    existing, cursor = set(), None
    while True:
        q = gql("""query($o:String!,$n:String!,$c:String){ repository(owner:$o,name:$n){
            discussions(first:100, after:$c){ nodes{ title } pageInfo{ hasNextPage endCursor } } } }""",
                o=OWNER, n=NAME, c=cursor)["repository"]["discussions"]
        existing |= {x["title"] for x in q["nodes"]}
        if not q["pageInfo"]["hasNextPage"]:
            break
        cursor = q["pageInfo"]["endCursor"]

    missing = sorted({p["category"] for p in posts} - set(cats))
    if missing:
        sys.exit(f"These categories do not exist (check the slugs in Settings > Discussions): {missing}\nFound: {sorted(cats)}")

    todo = [p for p in posts if p["title"] not in existing]
    print(f"{len(posts)} posts in file; {len(posts) - len(todo)} already exist; {len(todo)} to post.")
    for i, p in enumerate(todo, 1):
        print(f"[{i}/{len(todo)}] {p['category']}: {p['title']}")
        if not really:
            continue
        res = gql("""mutation($r:ID!,$c:ID!,$t:String!,$b:String!){
            createDiscussion(input:{repositoryId:$r,categoryId:$c,title:$t,body:$b}){ discussion{ id url } } }""",
                  r=repo_id, c=cats[p["category"]], t=p["title"], b=p["body"])["createDiscussion"]["discussion"]
        print("    ", res["url"])
        ids = [labels[l] for l in p.get("labels", []) if l in labels]
        for l in p.get("labels", []):
            if l not in labels:
                print(f"     (label '{l}' not found in the repo; skipped)")
        if ids:
            try:
                gql("""mutation($id:ID!,$l:[ID!]!){ addLabelsToLabelable(input:{labelableId:$id,labelIds:$l}){ clientMutationId } }""",
                    id=res["id"], l=ids)
            except RuntimeError as e:
                print("     (could not add labels:", e, ")")
        if p.get("pin"):
            print("     -> pin this one by hand: open it and click 'Pin discussion'")
        time.sleep(4)
    if not really:
        print("\nDry run only. Add --post to post them.")


if __name__ == "__main__":
    main()
