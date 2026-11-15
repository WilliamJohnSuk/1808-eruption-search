# Posting the seed Discussions (15 Nov 2026)

The seed posts were reviewed and approved by William John Suk in chat on 15 Nov 2026, batch by batch.

- `build_posts.py` turns `community/discussion_seed_posts_2026-11-04.md` and `community/seed_post_method_ai_human_check_F15_2026-11-15.md` into `community/seed_posts_2026-11-15.json` (57 posts; polls left out). Re-run it from the repository root after any edit to those files.
- `post_discussions.py` posts the JSON with `gh api graphql` (createDiscussion, then addLabelsToLabelable). It is a dry run unless given `--post`, and it skips titles that already exist, so it is safe to re-run.
- `POLLS_PASTE.md`: the two polls, to paste by hand.
- The Evidence review posts were generated from `findings/findings.csv` and `findings/checks.csv` on 15 Nov 2026. "Verification" in each is the level Claude reached; a person's check is named separately.
