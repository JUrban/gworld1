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

## Working focus after the 12:15 UTC checkpoint

N8 now has candidate algorithms for the two extreme target strata in arbitrary class, in addition to all targets in classes three through five. The remaining challenge is intermediate target layers. A possible next route uses weighted free presentations of lower-central subgroups, but finite integral orbit representatives for arbitrary higher-weight factors have not been proved; do not infer them from the degree-one IA argument. Alternate this bounded investigation with the unresolved portfolio in `research/notes/portfolio-followups.md`, and continue the novelty audit of F28.

## Working focus after the 12:43 UTC checkpoint

N5 has a whole-entry candidate including torsion, with an explicit finite reduction and tested central lifting. Keep its remaining specialist/novelty audit separate from the implemented examples. Next, revisit the other unresolved algorithmic and solvable-group questions and deepen F28's novelty check; do not let the N8 and N5 developments narrow the original 195-entry portfolio.

## Working focus after the 13:05 UTC checkpoint

M0 now has an all-finite-rank candidate from finite-field Fox matrices and
explicit primitive-word orbits. Rank <=2 is prior; rank >=3 needs independent
specialist and novelty review. GA5(b) has been removed from the discovery
queue using the exact binary-tree theorem of Bartholdi–Sidki (2018/2020).
Continue alternating the wider portfolio with review of the four current
candidates. The solvable-group search did not settle S4–S8; in particular,
co-Hopfian direct-product results do not answer the Hopfian question S5.

## Working focus after the 13:30 UTC checkpoint

OR2/6/7/8/11/12 have prior resolutions or direct prior consequences; all
are excluded from new-result counts. Exact scope and transfer arguments
are recorded in `research/notes/OR-prior-resolutions.md`.

The N8 candidate now also covers the penultimate lower-central term in
every class. For a bounded next investigation, examine whether the first
correction kernel for higher-weight factors can be controlled by exact
commutator-preserving operations; do not assume that a second lifting
stage remains linear. Alternate with N3/N4/N9, unresolved metabelian and
matrix questions, and the wider portfolio. Bibliographic leads for AUX3(b)
and FP17 await primary full-scope checks. Maintain separate audits of
M0, N5 and F28 rather than treating their candidate status as validation.

## Working focus after the 13:45 UTC checkpoint

Three degree-five correction injections extend N8 to all targets in
class six. A higher-degree nonzero kernel is explicitly recorded, so
the same uniqueness argument cannot simply be repeated for class seven.
Return to the wider unresolved portfolio before extending this calculation
further. AUX3(b) and FP17 have now been excluded using exact prior scope
evidence; FP17's full proof remains unavailable in the archive, which is
documented rather than presented as a completed full-text audit.

## Working focus after the 14:01 UTC checkpoint

The wider matrix/metabelian pass produced scope clarifications and no
new candidate. MA5's connected case, MA3's special parabolic subgroups
and M4's finite-rank theorem are now documented from primary sources.
FP9's abstract universal-tree construction still lacks an effective
diagram; do not treat countability as recursive presentability.

Give the remaining free-group, braid and group-action questions another
bounded pass, using the precise B9 terminology warning in
`research/notes/portfolio-followups.md`. Continue auditing the existing
four candidates and return to the unresolved N8 kernels only after
this wider pass. Preserve the distinction between exploratory reductions
and complete candidates.

## Working focus after the 14:17 UTC checkpoint

B3, B8 and B13 are prior results. B9 has reproducible finite lower bounds but no fixed-strand stopping argument; avoid spending the run merely enlarging these lists. Continue the remaining group-action and free-group scopes, with exact quantifiers, before returning to N8 higher correction kernels. Existing candidates still need adversarial proof and novelty review.

## Working focus after the rank-two class-seven checkpoint

The wider pass left F20's weight-six rewriting inconclusive and exposed
the finite-generation/presentation gap in GA2. Neither adds a candidate.
N8's rank-two class-seven case is now a candidate extension with a
written quadratic-lattice proof and independent GAP certificates.
Do not infer the same kernel bound in arbitrary rank from the bounded
probe. Keep the exact Nielsen move x->yx in future arguments.

Return to adversarial checks and wider unresolved entries before further
large computations. Useful mathematical questions include whether the
(1,4) correction kernel admits a proved all-rank bound, and whether any
other target can be handled by a finite number of one-variable polynomial
conditions. Such leads are not part of the counted scope until complete.
