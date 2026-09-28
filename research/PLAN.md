# Active research plan

Start: 2026-09-28 10:04:49 UTC. Deadline: **2026-09-30 10:04:49 UTC**. The full dataset is in scope. The goal is as many rigorous previously unsolved answers as possible within the allotted time; bibliographic updates and known rediscoveries are useful but are not counted as new answers.

## First pass: source and literature triage

Survey all 195 entries and their named subparts, including heading-star entries with possible residual questions. Record evidence and exact scope in `research/triage.csv` and a dated literature ledger. Prioritize current primary sources over old surveys and search snippets. Distinguish a new preprint's claim from an established result. Do not treat a website's unstarred status as current openness.

Early lines of investigation, subject to checking and revision:

1. F42: extremal free independent sets in balls and spheres. Develop a folded-graph upper bound and explicit covering-graph constructions, then audit literature and verify small cases independently.
2. Free-group subgroup/automorphism questions: F8, F11, F15, F20, F26–F31, F34, F38–F41. Several have recent literature; remove already answered scopes and retain genuinely unresolved, tractable parts. Use graph algorithms and exact word calculations where helpful.
3. Matrix and solvable/nilpotent questions: MA1/MA3/MA5/MA6/MA7, N4–N9, M0–M5, S1–S8. Identify convention issues before selecting concrete constructions or algorithmic reductions. Do not count trivial readings that miss the intended question.
4. Group actions: GA1–GA5 and F28. Check current self-similar-group literature carefully: preliminary searches already expose changes between preprint and published assertions.
5. One-relator, algorithmic and growth questions: review recent surveys for known progress and computationally testable special cases. Maintain a few higher-risk structural leads without letting one consume the portfolio.

## Iteration policy

For each lead, write the exact problem and a proposed route; identify the first decisive test. Alternate proof and exact computation. Give a stalled lead a bounded effort, record what failed, and move to another. Keep alternative leads ready. A promising complete argument triggers an immediate statement/literature/correctness audit and a compact artifact, not an immediate novelty claim.

## Computation and evidence

Use the recorded runner for research computations. Allocate at most 20 CPU slots and 100 GB requested memory in total; monitor actual usage and account for jobs outside the wrapper. Record deterministic seeds, exact bounds, versions and actual return codes. Prefer small verifiers, independent representations and negative controls. Do not commit large raw searches.

## Reports and checkpoints

Update `research/LOG.md`, `research/triage.csv`, and `research/claims.jsonl` as evidence changes. Record any reused Kourovka mathematics/code in the transfer ledger. Keep a rolling `reports/PROGRESS.md`, commit substantial progress frequently, and do not push. Freeze the deadline ledger and write `reports/FINAL_REPORT.md`; do not label interim checkpoints as completion of the experiment.

Reserve the last eight hours for overlapping discovery and verification, with the final hours focused on statement fidelity, complete arguments, reproducibility, novelty qualifications and counting. No subagents are authorized; parallelism is computational only.
