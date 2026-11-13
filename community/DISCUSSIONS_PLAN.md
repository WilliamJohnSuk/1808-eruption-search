# Discussions: category plan

GitHub Discussions categories can only be created in the repository's web settings (Settings > General > Features > Discussions, then the pencil icon on the Discussions page). This file is the plan to follow, and the record of why each category exists.

Votes in every category are advice to the maintainer, not a decision about evidence (see GOVERNANCE.md).

| # | Category (exact name) | Format | Purpose | Seed threads at launch |
|---|---|---|---|---|
| 1 | Announcements | Announcement (maintainers post, everyone replies) | Releases, new findings accepted, calls for help | "Welcome: what this project is and how AI work is marked" (pin) |
| 2 | Start here | Question and answer (best answer marked; answers upvoted) | Newcomer questions, how to read a source, how to use the forms | "How do I report a source without git?" |
| 3 | Candidate volcanoes | Open-ended discussion | One thread per candidate; arguments for and against, with links to evidence | One per candidate: Dakataua, Gaua, Cabalían, Agung, Todoko-Ranu, Dukono, Teon, Nila, northern Sulawesi; plus "Ruled out and why" (Etna, Vesuvius, Hekla, Long Island) |
| 4 | Evidence review | Open-ended discussion | One thread per row of findings/findings.csv: is it real, is it weather, what would check it? | F01-F21, one thread each, starting with F01 Bogotá, F04 Edo, F06 *Townsend*, F07 EIC temperatures, F08 NEEM |
| 5 | Polls | Poll | Priorities: which source to chase next, which candidate to test first, which open task matters most | "Which hand item should be retrieved first?" (options from access/open_tasks.md section 3); "Which candidate should the next free check test?" |
| 6 | Sources and archives | Open-ended discussion | Leads too vague for an issue; archive tips; who holds what | "Ship logs from the eastern islands, Nov 1808-Mar 1809: who might have them?" |
| 7 | Method and AI | Open-ended discussion | How the AI work was done, its errors, critique of methods and of the verification levels | "Where did the AI get it wrong? (corrections welcome)" |
| 8 | Translation help | Question and answer | Requests to read a passage in Dutch, Spanish, Portuguese, classical Chinese, Japanese, Vietnamese, Malay/Jawi, Tok Pisin | none |

Category forms: `.github/DISCUSSION_TEMPLATE/candidate-volcanoes.yml` and `evidence-review.yml` apply when the categories exist with exactly those names (GitHub matches the form's file name to the category's slug).

Linking issues and discussions: when a discussion produces a concrete claim, open a "Submit a finding" issue and link it; when an issue turns into an argument, convert it to a discussion (the issue menu has "Convert to discussion").

Summaries: a maintainer (or an AI agent run by one, labelled `ai-generated`) posts a short summary at the top of long threads, saying what was agreed, what was not, and what changed in the repo.
