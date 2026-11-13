# Launch checklist (move to `community/archive/` once the repository is public)

What must happen before the first push and before the repository goes public. Written 4 Nov 2026, updated the same day with William's decisions. Keep `access/open_tasks.md` (T-numbers) in step. 13 Nov 2026: William created the empty private repository `WilliamJohnSuk/1808-eruption-search`; initial commit 3a81f27 pushed to `main` the same day (353 files). William renamed his GitHub account to `WilliamJohnSuk` the same day; the repository is now `WilliamJohnSuk/1808-eruption-search` and old links redirect.

## 1. Evidence: bring the trail up to date (thread "Close the pre-launch gaps in the synthesis")

- [x] (done 4 Nov) **Fold B54-B74 into the synthesis and findings** (T19). Results since 26 Oct are in the register and notes but not yet in `findings/findings.csv` or `findings/why_unidentified.md`. New rows need the three provenance columns (`ai_generated`, `verified_by`, `independent_checks`). Re-read the README's "What is known so far" afterwards.
- [x] (done 4 Nov) **Release gap 1, strand summaries** (T29): a one-page `README.md` in each `strands/<region>/` folder.
- [ ] **Release gap 2, the source register**: `sources/register.md` (374 KB) is ordered by research round with duplicates. Either a one-row-per-source table, or ship it with a note saying so (part of T23).
- [x] (done 4 Nov, T42: `strands/method/findings_table_check_2026-11-04.md`; consistency check only, not a human check) **Release gap 3, check the findings table** against its notes files; OCR-only quotations stay clearly labelled. These checks can be the first rows of `findings/checks.csv`.
- [x] (superseded 10 Nov by William's T43 decision: personal and access details stay explicit) **Release gap 4, personal and access details** (T30): 28 files mention Mac paths, library names or what the container could not reach. No keys or session cookies were found (checked 4 Nov).
- [x] (done 4 Nov for `data/README.md` and `CITATION.cff`; the blog link is Stage B step 12) **Release gap 5, packaging** (T31): blog post final and linked; one provenance and licence line per data file in `data/README.md` (T38's remainder; the audit CSV feeds it). `CITATION.cff` done.
- [x] (done 4 Nov: nothing over about 40 words found) T35: cut long verbatim passages from modern copyrighted works to short quotations.

## 2. Licences and hosting

- [x] **Share-alike data**: the Gill-derived table is in `data/cc-by-sa/` with its own CC BY-SA 4.0 `LICENSE.md`; the exception is stated in `LICENSE.md` and the README. GEOROC-derived tables stay in `data/` (CC BY 4.0).
- [x] **Strip list** from the audit (`strands/method/hosting_licence_audit_2026-11-04.md` section 6): FamilySearch scripts removed from the repo copy and from `sync_repo_copy.sh`; the repo copy holds no paywalled papers, Blong screenshots or FamilySearch images.
- [x] **Takedown note** (contact widzodev@icloud.com) in README, LICENSE.md and `sources/scans/README.md`.
- [ ] **Hosted scans**: `sources/scans/` is ready (README, `index.csv`). HBCA pages are HOST at William's decision (T41 copies the cited pages from the Mac). Other cited public-domain pages: T40 sets each HOST-AFTER-CHECK row of the audit CSV to HOST or LINK-ONLY. LINK-ONLY rows and the audit's "never" list stay out.
- [ ] T36 and T39: item-level licence checks (T39 needs Safari); GEOROC and GVP terms U192, U193.

## 3. Decisions (T33, answered 4 Nov 2026)

- [x] (a) Conduct and takedown contact: widzodev@icloud.com.
- [x] (b) Title: "Human/AI collab to identify the missing 1808/9 volcano." Proposed slug: keep **`1808-eruption-search`** (planned since October and already in the forms, CITATION.cff and the blog placeholder). A shorter alternative is `missing-1808-volcano`; if you choose it, replace the slug in `.github/ISSUE_TEMPLATE/config.yml`, `CITATION.cff` and step 4.4 below.
- [x] (c) AI marking stays in the research files (front matter, findings columns, labels); no banner on the front page.
- [x] (d) `findings.csv` has `ai_generated`, `verified_by` and `independent_checks`; `findings/checks.csv` records any number of independent human, AI or mixed checks (rules in `findings/CHECKS_README.md`, form "Re-check a source or finding").
- [x] (e) CITATION.cff author: William John Suk (website https://williamsuk.ai).
- [x] (f) GitHub becomes the master copy at launch; launch private first.

## 4. Going live (T34): private first, then public

**Stage A: private test launch**
1. Create an empty repository at <https://github.com/new>: name `1808-eruption-search`, **Private**, no README, licence or .gitignore. Tell a thread when it exists.
2. A thread runs the sync one last time and pushes the repo copy (threads cannot create repositories, but can push to one that exists).
3. Settings > General > Features: tick **Issues** and **Discussions**. Both work in a private repository, including the issue forms and the Discussions category forms. On the Discussions tab, create the eight categories in `community/DISCUSSIONS_PLAN.md` with the exact names and formats.
4. Labels: in Terminal on the Mac, with the GitHub CLI logged in, from the repo folder:
   ```zsh
   gh auth status && bash scripts/create_labels.sh WilliamJohnSuk/1808-eruption-search
   ```
   (Or ask a thread to run it.)
5. Test: open one issue with each of the five forms, start a Discussion in two categories, answer a poll, and open a small pull request to see the template. To test as an outsider, invite a friend as a collaborator (Settings > Collaborators). Close or delete the test items afterwards.
6. From this point **GitHub is the master copy**. Threads clone the repository and work through branches and pull requests; `scripts/sync_repo_copy.sh` is retired, because it would overwrite contributors' edits. The library folder stays Claude's working space, and its changes reach GitHub only by pull request.

Two things will not work yet while the repository is private, if you are on GitHub Free: **Pages** (the website) and **branch protection with required code-owner review**. Both need a public repository on the Free plan. Outsiders also cannot see, discuss or vote until it is public, so votes in Stage A are only you and anyone you invite.

**Stage B: public launch**
7. Read the repository through once more as a visitor (sections 1 and 2 above done).
8. Settings > General > Danger Zone > Change visibility > **Public**.
9. Settings > Branches: add a rule for `main` with "Require a pull request before merging" and "Require review from Code Owners". Allow yourself to bypass it, because GitHub does not let an owner approve their own pull request.
10. Settings > Pages: deploy from branch `main`, folder `/ (root)`, and check that the README renders as the home page.
11. Seed the Discussions (T32 drafts the text) and pin the welcome post.
12. Put the link in the blog post (its closing paragraph has a placeholder) and publish it.

## 5. Already done (4 Nov 2026)

- Public README (old one in `community/archive/`), CONTRIBUTING, CODE_OF_CONDUCT (Contributor Covenant 2.1), GOVERNANCE (including the independent-checks schema), CONTRIBUTORS, CITATION.cff.
- Five issue forms (report a source, submit a finding, re-check a source or finding, propose a candidate volcano, request or offer a retrieval), pull-request template, CODEOWNERS, two Discussions category forms.
- 47 labels in `community/labels.json` (table in `community/LABELS.md`) and `scripts/create_labels.sh`.
- `scripts/add_frontmatter.py`: AI-provenance front matter on all notes under `strands/` and `findings/` (`verified-by: none` on all); the sync re-runs it until it is retired at launch.
- `findings/findings.csv` provenance columns; `findings/checks.csv`; `data/cc-by-sa/`; `sources/scans/`.
