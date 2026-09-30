# GroupWorld: a 48-hour experiment

**Active run: 28 September 2026, 10:04:49 UTC → 30 September 2026, 10:04:49 UTC.**

[Current results and review guide](reports/CURRENT_RESULTS.md) · [Progress history](reports/PROGRESS.md) · [Research plan](research/PLAN.md) · [Research log](research/LOG.md). The initial preparation snapshot is preserved in Git. The generated catalogue and problem READMEs retain their preparation status; current assessments are in [the working triage](research/triage.csv) and [dated claim ledger](research/claims.jsonl).

[Entry/subpart scope ledger](reports/RESULT_SCOPE.md) ·
[Interim final-report draft](reports/FINAL_REPORT_DRAFT.md) ·
[Closing audit plan](reports/CLOSING_AUDIT_PLAN.md).
These are preparation for the original deadline, not a completed run.

Current working tally: **ten whole-entry candidates and two partial
candidates**, all awaiting independent review and novelty assessment.
The latest candidate is [N9](problems/N9/proof.md): undecidability of the
retract problem in one fixed torsion-free class-two group, already for
two-generator subgroups. Its [audit](problems/N9/audit.md) includes actual
GAP retractions and a Lean check of the integer normalization lemma;
the full theorem is not formally verified. Part(b) is credited prior work.
An [additional audit](problems/N9/isolated-inputs-and-prior-scope.md)
shows that every input subgroup is isolated and checks the precise
boundary of the published free-nilpotent algorithm.
[N8](problems/N8/README.md) also has a candidate
algorithm for single commutator equations in every finite-rank free
nilpotent group. See its [general proof](problems/N8/general-proof.md)
and [audit](problems/N8/general-audit.md). A [limited Lean check](problems/N8/averaging-lean-audit.md) verifies the stochastic contraction and maximum principle used in its separation argument. The full all-rank implementation
is not complete; the theorem argument and novelty require specialist review.
The new [B9 partial candidate](problems/B9/infinite-family-proof.md) constructs
infinitely many special braids on five strands, giving countably infinitely
many in every B_N with N>=5. The [small-strand supplement](problems/B9/small-strand-proof.md)
deduces the counts 1, 2 and 4 for B1, B2 and B3 from prior structural
results; only the exponent-two sector in B4 remains unclassified.
[G9](problems/G9/flow-growth-proof.md) provides
effective approximation of free-metabelian growth in every finite rank,
and certified rank-two bounds `2.658596558 <= lambda_2 <= 2.943737759`.
The exact constant remains undetermined; see the [audit](problems/G9/flow-growth-audit.md).

This is a fresh repository for the collection of [open problems in combinatorial group theory](https://shpilrain.ccny.cuny.edu/gworld/problems/oproblems.html) selected by G. Baumslag, A. G. Myasnikov and V. Shpilrain, together with its [Hall of Fame](https://shpilrain.ccny.cuny.edu/gworld/problems/Halloffame.html). The snapshot was downloaded on 28 September 2026.

[Start here](START_HERE.md) · [Problem catalogue](data/CATALOG.md) · [Status notes](docs/STATUS_NOTES.md) · [Experiment protocol](docs/PROTOCOL.md) · [Lessons from Kourovka](docs/KOUROVKA_LESSONS.md)

The archive contains **195 numbered entries in 16 categories**, both background pages, the Hall of Fame and the locally linked PDF. Each entry has an offline HTML excerpt and an exact source fragment under `problems/ID/`. The numbered-entry count is not a count of currently open problems: entries have multiple parts, overlap, and include known results.

The catalogue preserves 49 heading stars, 11 entries with subpart stars, and 69 Hall of Fame links referring to 58 distinct entries. Sixty entries have at least one of these site indications. One additional bibliographic update records Gardam's 2021 answer to O12(b), which is unmarked on the site. All scope and openness assessments still require review before research; no exhaustive current literature survey has been done.

## Relationship to Kourovka

This repository has its own Git history, corpus, clock and result ledgers. The existing Kourovka repository is a read-only reference for methods, code, arguments and corrections. It is **not** a clean-room experiment: any later use of a Kourovka result must be recorded in [the transfer ledger](research/transfers.jsonl). The preparation source revision and file hashes are in [provenance/kourovka.json](provenance/kourovka.json).

Locally this checkout is `/project/gworld1`, excluded from the enclosing Kourovka checkout using that checkout's `.git/info/exclude`. It can be moved or published as a separate repository. No remote is configured. The GAP installation is shared through a local configuration file; its binaries and large datasets are not copied.

## Tools and state

Python 3 and Git suffice for the preparation utilities. Set up `config/local-tools.json` from [the example](config/local-tools.example.json), or set `GWORLD_GAP_ROOT`, to use `bin/gap`. The local GAP 4.16.1 installation and `smallgrp`, `fga`, `kbmag`, `nq`, `polycyclic`, and `ace` packages passed a load check. [Environment record](provenance/environment.json).

```sh
python3 scripts/session.py status
python3 -m unittest discover -s tests -v
```

The authorized run budget is 48 hours, 20 CPU cores and 100 GB RAM. `scripts/run_recorded.py` records bounded research commands and refuses jobs after the deadline. `state/session.json` is the authoritative clock.

Source bytes, retrieval metadata, links and SHA-256 hashes are retained in [sources/manifest.json](sources/manifest.json). One malformed publisher link, `Back.htm`, returns 404; its adjacent correct `Back.html` link is downloaded. [Source scope and limitations](sources/README.md).

The local pre-commit hook rejects staged blobs of 90,000,000 bytes or more. After cloning elsewhere, enable it with `git config core.hooksPath .githooks`.
