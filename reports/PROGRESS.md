# GroupWorld progress

Active experiment: 28 September 2026 10:04:49 UTC to 30 September 2026 10:04:49 UTC.

Current counts: **1 partial candidate**, **0 whole-entry candidate solutions**, **0 established novel results**. Novelty of the partial candidate remains provisional.

- The independent repository, frozen corpus, clock, recorded computation runner and research plan are in place.
- First reading of all 146 entries without heading stars completed at extracted-text level. Heading-star residual scope and full original statements remain part of triage.
- F42: derived the exact extremal formula and a covering-graph construction, then found Koch-Hyde–Olive's September 2026 preprint already proving the same answer. Preserved as a rediscovery, excluded from new-solution count.
- F11: derived a cyclic-retract/index-three counterexample, then found the same mechanism in Snopce–Tanushevski–Zalesskii (2019). Also excluded. Original HTML screenshots for F11/F42 have now been inspected.
- Primary sources also report prior resolutions of F15, F30, F31 and F40. B11 has a 2025 primary seminar announcement; full proof not yet located. Scope checks are recorded in `research/triage.csv` and `literature/LEDGER.md`.
- N8(b): a constructive algorithm for the single-commutator problem in every finite-rank free nilpotent group of class three. The written candidate proof is `problems/N8/class3-proof.md`. The exact prototype passed 173 checks; GAP independently verified 165 positive witnesses. Higher classes remain open in this investigation.
- GAP 4.16.1 and relevant packages are available. Chromium rendering works using locally extracted system libraries, without root access. The first GAP check exposed an nq crash on the rank-one/class-three request; the rerun handles the infinite cyclic case directly, and the failed log is retained.

See `research/PLAN.md` for the portfolio and `research/LOG.md` for dated progress. Known results and bibliographic updates are not counted as new solutions.
