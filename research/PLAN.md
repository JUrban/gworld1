# Active research plan

Start: 2026-09-28 10:04:49 UTC. Deadline: **2026-09-30 10:04:49 UTC**. The full dataset is in scope. The goal is as many rigorous previously unsolved answers as possible within the allotted time; bibliographic updates and known rediscoveries are useful but are not counted as new answers.

Latest checkpoint, approximately 02:52 UTC on 29 September: six whole-entry
candidates (F28,N5,M0,H4,F41,GA3), three partial candidates
(N8,F38(a),F34(a)), zero established novel results. All nine await
specialist review and novelty assessment.

GA3 now has a complete intended nonabelian argument. A controlled
collapse gives a real-tree action with abelian arc fixators and trivial
tripod fixators; boundary separation supplies simultaneous conjugating
maps, which extend to the whole group. Arbitrary ordered length groups
and arbitrary generation are included. Guirardel2004 and Rybak2026 are
explicitly credited. The finite free-group controls passed in Python
and GAP after one preserved GAP variable-name failure. They do not
verify the general tree argument.

The preceding F38(c) work gives a decidable necessary stabilizer
condition and an effective exponential comparison after it passes;
the linear bound remains unresolved. F20's cover probe was inconclusive,
and N9's fixed-ambient encoding remains obstructed.

Next: return to an unresolved mathematical lead in the wider portfolio,
while retaining GA3's bibliographic and specialist-review caveats. Do
not expand the free-group controls merely to increase their volume.
The original deadline and resource budget remain unchanged.

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

## Working focus after the all-rank class-seven checkpoint

The exceptional N8 kernel now has an all-rank proof, and the extended
prototype has independent GAP certificates. Keep this as the same
partial candidate; do not infer class-eight completeness. Larger
integer systems and repeated Magnus multiplication caused two saved
timeouts before arithmetic improvements. Further computational scaling
should follow a new mathematical question, not just larger examples.

E5,H12 and A4 are prior positive answers/consequences and leave the
discovery queue. A6's unrestricted-word scope remains separate from
Chiodo's bounded-length theorem. Return to the broader unresolved
portfolio and adversarial review of F28,N5,M0 before another N8
extension. The proofs and bibliographic status still need external
specialist review; computation is supporting evidence only.

## Working focus after the 15:45 UTC scope checkpoint

H13 and FP6 leave the discovery queue as prior answers; N1's existing
full-classification update is corroborated. FP21 now has a precise
rank-two equivalence with residual finiteness of Br_4(m), but neither
an infinite linear image nor the triangle-free Shephard theorem
resolves that case. Do not count this reformulation as another partial
solution. H4's promise/preprocessing distinction also remains open here.

Next, give a concrete unresolved mathematical lead a bounded attempt,
then return to adversarial review of the four candidates. Avoid merely
repeating the broad searches or increasing the size of earlier finite
enumerations. For FP21, any further representation argument must prove
faithfulness or separate every nontrivial element, not just produce
an infinite residually finite quotient.

## Working focus after the 16:06 UTC verification checkpoint

F27's tiling lead does not apply outside the commutator subgroup. The
normal-root stabilizer route remains missing an actual infinite orbit;
the elementary abelianization and free-factor reductions are recorded
without a new-result claim. N9(a)'s fixed-ambient quantifier remains an
obstruction to the familiar varying central-product construction.

The F28, N5 and M0 proofs have been reread without a new gap found in
this pass. M0 now has an end-to-end witness constructor with independent
GAP certificates, including symbolic checks of its positive cases.
Do not spend further time enlarging that sample without a new concern.
Return to a concrete unresolved mathematical route in the wider
portfolio, alternating discovery with the outstanding novelty and
specialist-review needs of the four candidates. The clock and tally
remain unchanged.

## Working focus after the class-eight verification checkpoint

N8's candidate now covers all targets in classes three through eight
in every finite rank, as well as the previously stated arbitrary-class
strata. The six new kernel lemmas and the quadratic cokernel argument
are written out. Independent GAP checks cover the final bounded
datasets; every timed-out benchmark and the corrected fixture alias
remain documented. A difficult nonprimitive rank-three benchmark was
not completed and must not be described as passed.

Return to the wider unresolved portfolio and adversarial review of
F28, N5 and M0 before extending the N8 computation again. M4's
countable-rank question remains distinct from Artamonov's finite-rank
theorem; a local-freeness argument alone does not prove it. For GA1,
an archimedean small-root argument does not handle arbitrary ordered
abelian length groups. No new candidate follows from the latest
bounded reading pass over these questions.

The elementary higher-kernel family recorded in the class-eight lead
already prevents a naive uniqueness extrapolation to type (1,6).
It is not a class-nine decision procedure. Avoid spending the run
merely enlarging existing validation suites: further computations
should answer a new mathematical question or a specific audit concern.
The tally remains three whole-entry candidates, one partial candidate,
and zero established novel results. No external review has occurred.

## Working focus after the 17:45 UTC source-audit checkpoint

M4's full finite-rank proof has been obtained; the countable module and
augmentation-basis gaps remain. N3 cannot be retired on the strength of
GSW 2003 alone: its Proposition 3.5 has an explicit class-five torsion
counterexample, independently checked. This is a supplementary audit,
not a negative answer to N3 or another counted partial result. The
finite example already has a torsion-free nilpotent cover.

The new audit has a compact proof and two independent arithmetic
verifiers. Do not enlarge the torsion search merely to obtain bigger
examples. Return to the wider unresolved portfolio and candidate proof
audits; any attempt to repair the N3 construction must impose and prove
new sufficient hypotheses on the profile while preserving arbitrary
cardinality. No external specialist review or novelty certification has
occurred. The original clock and three-whole/one-partial tally remain.

## Working focus after the 18:08 UTC checkpoint

S9 is retired as a prior full positive answer. S3's last-derived-relator
cases are also prior; its broader Fox-module route still needs control
of annihilators when torsion survives in the lower quotient. The exact
obstruction is recorded, without a new claim.

M0 now has a terminating constructive implementation with a proved
finite-field bound; the earlier bounded implementation is retained.
Do not enlarge its sample merely for volume. Return to a concrete
unresolved mathematical lead, alternating with adversarial review.
The count remains three whole-entry candidates and one partial, with
zero established novel results. The original deadline remains fixed.

## Working focus after the N9 construction audit

The attempted fixed-ambient N9(a) reduction is blocked by equation
reflection for retracts. A precise coproduct construction supports the
prior uniform undecidability reduction, but its ambient group depends
on the input. Do not count the repair or mistake an undecidable
endomorphism orbit for undecidable retract recognition.

The original 2016 article PDF remains unavailable; the literal product
interpretation is qualified accordingly. Four GAP examples support
the algebraic distinction, and the first run's global-scope warnings are
preserved. Further similar examples would not answer the fixed-group
question. Resume the unresolved portfolio or a specific adversarial
proof concern in the existing candidates; retain the original deadline
and three-whole/one-partial tally.

## Working focus after the uniform-family checkpoint

The class-nine rank-three replay is now complete; its successful sparse
variant and every failed/interrupted comparison are retained. No broad
benchmark that timed out is described as completed. The uniform-family
extension has its own completed bounded independent audit.

A second, uncounted family with degree-two leading factors is written in
research/notes/N8-degree-two-iterated-adjoint-lead.md. Rank-two structural
probes passed in classes11 and13, but no full group procedure or independent
replay has been implemented for that lead. Give its next decisive check a
bounded attempt, then return to the wider unresolved portfolio and specific
adversarial concerns in F28,N5,M0,F41. Do not turn verification performance
tuning or enlargement of finite samples into the research objective.


## Working focus after the N5 integrality audit

N5 passes the targeted composite-congruence and relator-defect audit without correction. Its general rational decomposition remains imported machinery, not an end-to-end implementation. F6 has a full prior Out(F3) theorem, but its Aut(F_n) scope is not retired. Do not repeat these small audits for volume. Resume a concrete unresolved mathematical lead, maintaining statement and novelty checks and the original deadline. Current tally:4 whole-entry candidates,4 partial candidates,0 established novel results.


## Immediate lead after the 00:07 UTC checkpoint

`research/notes/N8-odd-adjoint-family-lead.md` contains a new uncounted
family for classes11,15,19,... . Structural identities and the first
rank-two class11 kernel/obstruction passed Python and GAP. The complete
proof argument is saved, but the integral group decision constructor
and separate recognition audit remain. Next implement the h=3 case,
using complete integral solution lattices and independent replay of
linear/polynomial certificates. The first GAP timeout is preserved;
recursive Hall evaluation fixes its representation cost. Do not rerun
the expanded-word method or increase formal samples merely for volume.
Tally remains4 whole,4 partial,0 established novel, original deadline.


## Working focus after the odd-adjoint candidate checkpoint

The h=3 group implementation and certificate replay are complete. The
unbounded family proof and tensor-recognition audit are now recorded in
problems/N8/odd-adjoint-proof.md and odd-adjoint-audit.md. Higher classes
have formal identity checks, not group benchmarks; rank3 has scope
recognition, not group decisions. Do not enlarge those suites merely
for volume. Return to unresolved problems and specific candidate proof
concerns; a full-class11 result would require several additional kernel
classifications beyond this family. Counts4 whole,4 partial,0 established
novel; original deadline retained.


## Working focus after the H4 infinite-input checkpoint

H4 now has a stronger torsion-class counting proof, valid even for infinite non-elementary virtually free inputs. Its bounded GAP checks are complete; do not enlarge finite samples without a new concern. F37’s determinant route lacks both reflection for products under full-rank self-embeddings and an effective encoding of primitive-factor constraints; rank-changing embeddings show the unrestricted reflection statement false. The obstacle is recorded, not a solution. Return to unresolved mathematical leads or a specific candidate proof concern. Counts4 whole,4 partial,0 established novel; original deadline retained.


## Working focus after the full F41 candidate checkpoint

F41 has a complete intended-scope candidate, with imported definability and generic-type theorems and a new quantitative piece-cover argument. Its counting checks are complete. Do not spend further cycles increasing those samples; a useful audit must target the exact source theorem, parameter-free separation or a counterexample to the general counting lemma. Resume the wider unresolved portfolio alongside such audits. Original deadline retained;5 whole,3 partial,0 established novel.


## Working focus after the F20/N9 checkpoint (2026-09-29T02:00:26.125130+00:00)

F20 finite-cover homology is inconclusive after218 exactly replayed covers; neither larger rewriting budgets nor a blind enlargement of finite covers is a priority. A useful next step needs a structural kernel argument or a different quotient. N9 cannot be encoded by enlarging a proper subgroup containing the fixed base and the new commutator in a class-two coproduct; that obstruction is now proved. Return to a new unresolved lead or a specific candidate proof concern. Do not infer N9 undecidability from the varying-ambient theorem. Counts5 whole,3 partial,0 established novel; original clock retained.


## Working focus after the F38 stabilizer checkpoint (2026-09-29T02:26:28.296428+00:00)

F38(c) now has a terminating necessary-condition test, with exact negative witnesses and finite-orbit certificates. Its bounded implementation controls are complete; do not enlarge them merely for volume. The next substantive question is whether commensurable conjugacy stabilizers imply bounded translation equivalence, or whether there is a counterexample. Finite orbit arguments alone do not prove a uniform linear bound; compactness can lose relative vanishing rates. The quantifier remains automorphisms, not embeddings or all tree actions. Preserve the wider unresolved portfolio rather than assuming this converse. Counts5 whole,3 partial,0 established novel; original deadline unchanged.


F38 quantitative refinement: `research/notes/F38-stabilizer-length-envelope.md` proves that the test exactly decides mutual functional bounds and yields exponential bounds by Whitehead shortening. Any further advance must control the envelope linearly or exhibit a superlinear pair passing the test. Do not confuse a computable finite envelope with the required linear bound. The exact-envelope procedure is described, not implemented.
