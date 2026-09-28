# GroupWorld progress

Active experiment: 28 September 2026 10:04:49 UTC to 30 September 2026 10:04:49 UTC.

Current counts: **1 partial candidate**, **1 whole-entry candidate solution**, **0 established novel results**. Both candidates await independent review; novelty remains provisional.

- The independent repository, frozen corpus, clock, recorded computation runner and research plan are in place.
- First textual reading of all 195 entries completed, including 49 heading-star entries. Full original statements, linked background and residual scope remain part of targeted audits.
- F42: derived the exact extremal formula and a covering-graph construction, then found Koch-Hyde–Olive's September 2026 preprint already proving the same answer. Preserved as a rediscovery, excluded from new-solution count.
- F11: derived a cyclic-retract/index-three counterexample, then found the same mechanism in Snopce–Tanushevski–Zalesskii (2019). Also excluded. Original HTML screenshots for F11/F42 have now been inspected.
- Primary sources also report prior resolutions of F15, F30, F31 and F40. B11 has a 2025 primary seminar announcement; full proof not yet located. Scope checks are recorded in `research/triage.csv` and `literature/LEDGER.md`.
- N8(b): constructive algorithms for the single-commutator problem in every finite-rank free nilpotent group of classes three, four or five. Candidate proofs: `problems/N8/class3-proof.md`, `class4-proof.md` and `class5-proof.md`. Class three passed 173 exact checks and 165 GAP witness checks; class four passed 108 exact checks and 100 GAP witness checks; class five passed 70 exact checks and 61 GAP witness checks, plus 27 sampled kernel checks. This remains one partial candidate; classes six and above remain unanswered here.
- F28: explicit negative answer using a rational matrix conjugation on an index-two subgroup of F2. The image also has index two, and the bounded-orbit argument excludes every nontrivial invariant subgroup. Candidate proof: `problems/F28/proof.md`. Exact matrix/word checks covered 13,120 words; GAP independently checked subgroup indices/ranks and defining identities. Related arithmetic constructions in the literature establish weaker normal-subgroup statements; a matching prior full answer has not yet been found.
- GAP 4.16.1 and relevant packages are available. Chromium rendering works using locally extracted system libraries, without root access. The first GAP check exposed an nq crash on the rank-one/class-three request; the rerun handles the infinite cyclic case directly, and the failed log is retained.

See `research/PLAN.md` for the portfolio and `research/LOG.md` for dated progress. Known results and bibliographic updates are not counted as new solutions.
