# Active research plan

Start: 2026-09-28 10:04:49 UTC. Deadline: **2026-09-30 10:04:49 UTC**. The full dataset is in scope. The goal is as many rigorous previously unsolved answers as possible within the allotted time; bibliographic updates and known rediscoveries are useful but are not counted as new answers.

Latest checkpoint, approximately 20:35 UTC on 29 September: ten whole-entry
candidates (F28,N5,M0,H4,F41,GA3,F38,F34,N8,N9), two partial candidates
(G9,B9), zero established novel results. All twelve await specialist review and
novelty assessment. Whole-entry coverage may combine candidate new subparts
with explicitly credited prior subparts; it is not a count of twelve new theorems.

B9 now has an infinite special B5 family, hence the exact cardinality aleph0
for every B_N with N>=5. See infinite-family-proof.md and its audit. The
u_n recurrence and shifted-tail cancellation are universal algebra, with
symbolic integral Burau separation. The finite faithful-action tests passed;
do not repeat them without a concrete concern. Investigate B3/B4 separately
if a structural exhaustion argument emerges; bounded-height counts alone
do not settle those cases. This is one new partial candidate.

N9(a) now has a full fixed-group candidate in problems/N9/proof.md. The
rank-two form encoding uses a fixed circuit and full integer kernel; the
input-dependent affine condition forces the unit chart by a square
Pfaffian and a modulus-three guard. Native GAP checks one fixed toy group;
Lean checks the universal integer normalization. The full universal group
has not been numerically expanded or formally verified. See audit.md.
Do not repeat the passed finite checks without a concrete new concern.

N8 now has a general candidate decision algorithm in every finite rank and
class. Its consolidated proof and audit are problems/N8/general-proof.md and
general-audit.md. The full arbitrary-rank algorithm is not implemented end
to end. Earlier bounded checks retain their original scope; no passed suite
needs repetition without a new concern.

A bounded direct equational-proving attempt for F20 obtained no new target:
the eight weight-seven consequences missed by rewriting remain unproved.
Its 58 input files have an independent GAP semantic audit and negative
models; E's unsuccessful attempts are retained. See F20-equational-probe.md.
Do not merely enlarge these budgets. F23's higher-rank prior construction
and S4's derived-length-three prior case do not resolve their full questions.

A second F20 encoding with independently checked commutator identities also
proved no new target. G11's cyclic-subgroup estimates leave its whole-group
coset contribution uncontrolled. Both follow-ups are saved with their limits;
neither changes the candidate count. The 19:22 internal proof readthrough
found no new gap and is not external validation.

G9 now has a complete candidate proof of effective approximation in every
finite rank and independently checked numerical rank-two bounds. The
exact constant remains unknown. Preserve the distinction between a
mathematical terminating algorithm and practical fine-precision execution.

GA3 now has a complete intended nonabelian argument. A controlled
collapse gives a real-tree action with abelian arc fixators and trivial
tripod fixators; boundary separation supplies simultaneous conjugating
maps, which extend to the whole group. Arbitrary ordered length groups
and arbitrary generation are included. Guirardel2004 and Rybak2026 are
explicitly credited. The finite free-group controls passed in Python
and GAP after one preserved GAP variable-name failure. They do not
verify the general tree argument.

F38(c) now has a full candidate: graded shortening upgrades the finite
stabilizer condition to a linear comparison. Its structural theorem
application and novelty need specialist review; finite implementations
pass independent complete-graph checks. F20's cover probe was inconclusive.
The earlier N9 encodings remain obstructed, but the new alternating-form
construction above does not use them.

N3 now has a restricted nested-cover construction for countable ascending
nilpotent exhaustions, with the countable case explicitly credited to
Romanovskii1969. The general cardinality problem remains unresolved.
No candidate count is added; see `research/notes/N3-nested-cover.md`.

M4's finite-coordinate reduction now has an explicit obstruction, and
N6's profinite-comparison source does not compute genus cardinality.
Both remain unresolved; see the two dated scope notes.

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


## Working focus after the filling checkpoint (2026-09-29T03:13:42.489680+00:00)

The finite-stabilizer/filling criterion and its decidability are explicit prior Gupta–Kapovich results; the positive pair theorem is prior Kapovich–Lustig. Implementation and independent certificate replay are complete. Do not repeat these samples or count the criterion as new. Any further F38(c) advance must address non-filling pairs with commensurable stabilizers, or give a superlinear envelope counterexample. Resume the wider unresolved portfolio as appropriate. Counts6 whole,3 partial,0 established novel; original deadline unchanged.


GA1 scope correction, 2026-09-29T03:19:17.768194+00:00: retire the nonabelian free-Q-group question as a direct prior2009 consequence. Do not continue root-adjunction attempts for it. Fourth-power surjectivity contradicts the published tree-free power-equation theorem unless the group is abelian. Rank0/1 are elementary positive cases. Counts unchanged.


## Working focus after S5 prior-proof verification (2026-09-29T03:35:05.537079+00:00)

S5 is already proved in an external pre-launch Lean repository; pinned compilation, axiom audit and statement matching are complete. Do not spend the remaining experiment independently rediscovering it or count its theorem as ours. The installed pinned Lean toolchain can support later checks if a concrete proof concern warrants them. Return to unresolved mathematics and specific candidate concerns. Counts6 whole,3 partial,0 established novel; original deadline unchanged.


## Working focus after F28 Lean checkpoint (2026-09-29T04:05:15.277767+00:00)

The entire F28 matrix-orbit obstruction now has a checked Lean proof, and the informal proof uses the same energy/parity argument. Do not enlarge finite word samples or formalization scope merely for volume. The free-group bridge remains an explicit written proof. Return to a genuinely unresolved portfolio question or a specific proof concern. Counts6 whole,3 partial,0 established novel; original deadline retained.


## Working focus after C4 probe (2026-09-29T04:28:42.557535+00:00)

C4 has a checked FullHRed implementation and independent GAP replay, but no new bound. Do not enlarge random/exhaustive samples without a structural hypothesis. Width3 is prior; unrestricted mixed reversing-length control is false by2004. A useful return requires a potential specific to the handle strategy or a provable slow family. Resume unresolved portfolio work. Counts6 whole,3 partial,0 established novel; original deadline retained.


## Working focus after N8 support lemma (2026-09-29T04:39:33.784766+00:00)

The first type(1,q) correction has at most one parameter in every degree, by the tensor/Lyndon support proof in N8-general-first-kernel.md. Next prove or refute its double-primitive condition: delta V=[U,D], delta W=[U,V] should force D scalar U. It holds in complete one-chain rational calculations q<=14, independently replayed in GAP, but no all-degree proof exists here. Do not promote finite dimensions to a uniform theorem or enlarge samples without a hypothesis. Other leading types and later layers remain distinct. Counts6 whole,3 partial,0 established novel; original clock retained.


## Immediate next action after the uniform N8 obstruction (2026-09-29T04:44:08.394406+00:00)

The double-primitive question above is now proved by the cyclic-word argument in Section6 of N8-general-first-kernel.md. Do not repeat bounded dimension probes. Implement a general type(1,q) third-from-last integral branch solver using the at-most-one kernel and nonzero quadratic obstruction. Preserve all leading scales; reject other leading types as unsupported unless separately handled. Test mixed derivative-chain cases in class11/12 outside the old families, plus zero-kernel, nonprimitive, inconsistent and out-of-scope controls. Independently replay witnesses and full integral/quadratic certificates in GAP, then audit before enlarging the existing N8 partial scope. Counts6 whole,3 partial,0 established novel; original deadline unchanged.


## Working focus after general N8 type-one extension (2026-09-29T05:05:34.330407+00:00)

The general type-one third-from-last solver and independent GAP audit are complete. Do not repeat these samples. The next concrete lead uses Lazard elimination of a weight-two generator to reduce type(2,q), q>3, to the same free differential-chain support/cyclic argument; see `research/notes/N8-type2-first-kernel-lead.md`. Check the complete leading types and exceptional type(2,7) group branch, then independently replay its full integral/quadratic certificates before any scope promotion. The lead is not yet a candidate extension. Retain broader portfolio work and the original clock. Counts6 whole,3 partial,0 established novel.


## Working focus after N8 type-two checkpoint (2026-09-29T05:13:43.813896+00:00)

The combined p<=2 third-from-last scope is audited and implemented. Retain the new Remeslennikov--Stohr support credit; do not claim that lemma as novel or repeat its bounded probes. Other leading types still require control of decomposable correction directions. Return to the wider unresolved portfolio or pursue a specific proof concern. Counts6 whole,3 partial,0 established novel; original deadline unchanged.


## 05:32 source follow-up

GA5(c) existential rank2 scope is prior; do not spend discovery budget rediscovering it. G7/E6 leads did not settle their questions. A possible next F38(c) positive recognition route is a common filling subgroup, enumerated via the finite fringe of a cyclic subgroup (Takahasi). This would be a consequence of prior filling machinery, not a full decision or an automatic new count; keep Lee’s automorphism-versus-injection boundary control.


## Working focus after uniform N8 third-layer extension (2026-09-29T05:44:55.353545+00:00)

All third-from-last leading types are now implemented/audited. The graded-tail construction avoids the apparent decomposable-coefficient obstacle and subsumes the earlier p<=2 restriction. Do not repeat the completed samples. Lower leading layers need control of successive affine kernels; a plausible next structural question is whether the same construction handles offsets smaller than the first leading weight. No higher-layer conclusion follows yet. Keep broader unresolved-portfolio work active; F38 common filling subgroups would be prior positive scope only. Original deadline and counts6 whole,3 partial,0 established novel retained.


## Working focus after N8 fourth-layer checkpoint (2026-09-29T06:14:32.951506+00:00)

All fourth-from-last leading types are implemented and independently replayed.
Do not repeat their finished suites or retry the same180second rank-three cap.
The general-offset lead has a proposed complete fifth/sixth-layer scheme:
retain the offset-two line, solve offset3 jointly with its parameter, then
use the nonzero offset4 obstruction. The complete integral parameter step
must be retained. It is not implemented or counted yet. Return also to a
concrete unresolved problem in the wider portfolio; do not let incremental
N8 layers displace the original195-entry goal. Counts6 whole,3 partial,
0 established novel; original clock and review caveats retained.


## Working focus after common-filling-carrier implementation (2026-09-29T06:39:06.744044+00:00)

The finite common-filling-carrier search is implemented and audited as a
prior positive branch for F38(c). Do not repeat the completed sample suites
or count this as a new solution. The remaining non-filling, commensurable-
stabilizer cases need a linear comparison argument; Lee's rank-two pair
shows carrier existence is not necessary. Neither a same-rank primitive-
length reflection theorem for F37 nor a general automorphism/tree quantifier
replacement was obtained. Resume a concrete unresolved mathematical lead,
including the retained N8 fifth/sixth-layer scheme if useful, while preserving
the full195-entry objective and the original48hour clock.


## Working focus after fifth/sixth-layer extension (2026-09-29T07:03:56.815798+00:00)

N8 now covers gamma_(c-5), c>=9, with the exact implementation/proof/audit
complete. Do not repeat the finished bounded suites. Further layers require
a proof controlling multiple nonconsecutive exceptional kernels; successive
quadratic filtering alone is not justified. Return to another concrete open
portfolio problem rather than merely adding more N8 test sizes. O6
Linton reduction retains the primitive-extension hypothesis and supplies no
full answer. Preserve the six whole/three partial candidate counts and the
original48hour clock. No mathematical jobs remain after this checkpoint.


## Working focus after the audit/MA7 checkpoint (2026-09-29T07:32:23.155731+00:00)

The F41 parameter audit found no gap; do not repeat its finite suites.
MA7's new explicit finite noncommutative construction is complete and
independently checked, but the short website entry is already prior.
Do not count it as a new GroupWorld solution or infer a commutative-ring
answer. The renderer works with the path in docs/LOCAL_TOOLS.md; do not
repeat package downloads for already present libraries.

Return to a concrete unresolved mathematical lead in the broader frozen
portfolio. M4 still needs a compatible free basis beyond finite rank;
FP9 still lacks effective enumeration of all embeddings; F38(c) still
has stabilizer-passing cases outside its known positive branches. These
are mathematical gaps, not solved statuses. Preserve the whole195-entry
objective,6 whole/3 partial candidates,0 established novel and original
48hour clock. No mathematical jobs remain at this checkpoint.


## Working focus after A5/M3 checkpoint (2026-09-29T07:52:51.723191+00:00)

A5 now has reproduced prior formal evidence; do not rerun its successful
build/axiom audit or count it as ours. M3 has an effective ordinary
metabelian-quotient construction, but the normal kernel's triviality
remains unresolved. Finite normal generation is not a word-problem
algorithm or a general finite module presentation. The S4 control
prevents a false positive. Retain the full unresolved portfolio and
return to a concrete discovery lead; do not spend time rediscovering
the already indexed F15/F42 answers. No jobs remain. The original
deadline and6 whole/3 partial candidate counts are unchanged.


## Working focus after N3 profile-repair checkpoint (2026-09-29T08:23:41.895156+00:00)

N3 now has an exact torsion-killing profile criterion and two independently
certified obstructions, including the uniform rule d(U)=c(U)+1. Do not
repeat the finished class6/7 checks or treat these as counterexamples to
N3: the finite target has a free nilpotent cover. The larger class8 sweep
timed out, and pair-bound4 cases were not reached. The huge-preimage
shortening and uncorrected-prefix routes failed; the integral central
correction completed the needed proof.

Any further N3 repair must construct a single compatible profile over
arbitrary generator sets and preserve the target under torsion removal.
Larger changes of profile remain possible; none is established here.
Return also to concrete unresolved leads across the frozen195-entry
portfolio, rather than growing this auxiliary example indefinitely.
Preserve6 whole/3 partial candidates,0 established novel and the original
48hour clock. No jobs remain after this checkpoint.


## Working focus after F25 checkpoint (2026-09-29T08:45:47.947218+00:00)

The direct extension of Lee degree sorting to equal frequencies is false,
even after changing minimum representative or ordering the generators.
The12-cycle obstruction and all powers are certified; do not repeat these
finished finite checks or infer a negative answer to F25. A possible block
approach would require a new bound on entire equal-frequency move blocks;
no such bound is proved. F41 fixed-word constants do not supply it.

Return to a concrete unresolved portfolio lead under the original deadline.
All jobs have ended;6 whole/3 partial candidates,0 established novel.


## Working focus after F38 envelopes/primitive powers (2026-09-29T09:14:49.432439+00:00)

The exact finite-envelope and primitive-power calculations have completed;
do not rerun their successful suites. Arbitrary finite bounds and the
explicit exponential estimate do not decide linear comparison. The
rank>=3 primitive-power classification has an elementary proof and exact
growth witnesses, but novelty is unverified and prior general tools
already decide the family. Rank2 is excluded by Lee's example.

A possible next mathematical lead is free-factor support: pointwise
stabilizers of a proper free factor may force every finite-orbit conjugacy
class into it. The Nielsen graph method suggests this, but no general
support theorem or implementation has been claimed here. Broader F38(c)
stabilizer-passing cases still need a route to linear bounds. Return to
other unresolved portfolio leads as appropriate; preserve the original
48hour clock and6 whole/3 partial/0 established-novel counts. No jobs remain.


## Working focus after G9 (2026-09-29T09:50:38.335166+00:00)

The all-rank effective approximation argument and both numerical finite
certificates are now complete as a partial candidate. Do not rerun passed
checks. The numerical interval is coarse; no fine-precision execution or
best-known claim has been made. Possible later numerical improvement would
need new atom alphabets/forbidden words, but avoid spending the remaining
run only on incremental digits. Return to another unresolved portfolio
entry with a concrete proof route, and retain time for auditing the ten
current candidates. All jobs are terminal; original deadline unchanged.


## After the G9 noncommutative extension (2026-09-29T10:02:45.925478+00:00)

The flow-recovery theorem now covers all free-solvable derived lengths
with the same explicit approximation modulus. Independent noncommutative
controls pass; wrong-order controls expose the distinction from lattice
arithmetic. No further G9 suite needs repeating. The exact constants,
fine-precision execution and external novelty/proof assessment remain
open, and the tally stays6 whole/4 partial/0 established novel.

Resume the broader unresolved portfolio. Avoid spending remaining time
solely on sharpening the already certified numerical interval. All jobs
are terminal and the original30September10:04:49UTC deadline is unchanged.


## Working focus after the weighted-orbit extension (2026-09-29T10:29:07.089788+00:00)

N8 now additionally covers all degree-three targets and the equal-weight
and free-generator branches in arbitrary class. The denominator-clearing
construction passes independent subgroup-automorphism checks; retain the
explicit limit that the full finite-union algorithm is not implemented.
The remaining unequal branches have decomposable heavier leading terms.
Next examine whether the F38(c) necessary stabilizer condition can be
strengthened to a linear length bound via relative splittings or tree
actions; it is currently only an exponential envelope. Keep novelty and
proof-dependency audits of the whole-entry candidates in the schedule.


## Working focus after the full F38(c) candidate (2026-09-29T11:00:34.010172+00:00)

The candidate proof and finite decision implementation are complete for
F38(c); independent complete Whitehead-graph checks pass. Preserve its
explicit dependency on graded shortening and the separate specialist and
novelty caveats. Do not repeat finite controls merely to increase volume.
Return to the wider unresolved portfolio or a specific mathematical
proof concern. N8's remaining unequal weighted branches, the F20/F25
obstructions, and fixed-ambient questions remain unresolved. Maintain
all 195-entry scope and original deadline; 7 whole / 3 partial / 0 established novel.


## Working focus after N8 universal substitutions (2026-09-29T12:13:43.448957+00:00)

The universal construction and decomposable-pair controls are complete.
Do not repeat the passed finite suites. Preserve the distinction between
the candidate branch proof and its not-yet-complete end-to-end implementation.
The remaining mathematical obstacle is overlapping pre-Nielsen exceptional
offsets; it is not settled by one quadratic per parameter. Further scope
needs a specific argument controlling their interaction. Return also to
concrete unresolved portfolio problems and proof dependencies of existing
whole-entry candidates. All jobs terminal;8 whole/2 partial/0 established
novel, original deadline unchanged.


## Next concrete step after the exceptional boundary (2026-09-29T12:29:35.464647+00:00)

N8's counted partial scope is now leading degrees<=8 in arbitrary class
and all targets in classes<=14. Do not repeat the completed19-kernel suite.
The new `research/notes/N8-parametric-tail-lead.md` proposes a complete
univariate polynomial-matrix lattice decision, followed by a joint tail
algorithm through n<=2t+3. Its prospective ten-final-layer/class18 scope
is explicitly unverified and not counted. Next audit and implement that
integer decision lemma with full Smith transformations, rank-drop values,
finite bounds and periodic residues; independently replay complete positive
and negative certificates. Then test actual group correction branches with
the overlapping offsets3,5 before any further scope promotion. Preserve
the full portfolio and the original deadline; all current jobs terminal.


## Next step after the overlapping-tail audit (2026-09-29T13:53:00.374793+00:00)

The ten-final-layer/class18 candidate has completed independent finite
replay; do not repeat these passed suites without a new mathematical issue.
The proposed parameter-transmission route in
`research/notes/N8-parameter-transmission-lead.md` is the next concrete
bounded lead: write the complete integral two-parameter block argument,
including rank-zero/one cases and the later universal residue procedure.
Its proposed nonzero-coefficient fixture fails an earlier compatibility
condition; do not present it as a surviving two-parameter branch. Find a
valid test or prove why that case cannot occur. No class19/20 or
leading-degree9/10 extension is counted from this lead. Alternate with
specific unresolved portfolio questions and candidate dependency audits.
All jobs terminal;8 whole/2 partial/0 established novel; original clock.


## Next step after two-exception blocks (2026-09-29T14:22:20.018109+00:00)

The candidate scope is leading degrees <=10 in arbitrary class and all
targets through class20. The passed polynomial-family and two-block
suites should not be repeated without a new concern. The next concrete
N8 lead combines parameter elimination with a joint linear tail through
n<=13; see `research/notes/N8-fourteen-layer-lead.md`. It is unverified and
uncounted. A three-exception (3,5,7) group fixture and the full tail, not
just a late Lie relation, are necessary next checks. Alternate with a
specific broader-portfolio route or adversarial review of a whole-entry
candidate; avoid repeating status-only searches. All jobs terminal.
Original deadline and 8 whole/2 partial/0 established novel unchanged.


## Next checks after the three-exception checkpoint (2026-09-29T15:04:04.817848+00:00)

Finish the existing class24 constructor `n8-polynomial-group-tail-c24-v3`
and quotient preflight; revalidate their own recorded processes before any
restart. Then run the independent polynomial-group GAP verifier on the
completed class24 fixture and finish its manifest/audit. Only then decide
whether the proposed fourteen-layer/class24 scope has adequate support.
Class21 independent group replay and the strict class25 boundary already
pass and should not be repeated without a new concern. Current candidate
scope/counts remain unchanged. The compatible-deformation probe is a
failed unbounded branch, not a positive example; its general obstruction
question is only a lead. Original deadline unchanged.


## Next step after fourteen final layers (2026-09-29T15:24:41.390301+00:00)

The class24 constructor, quotient preflight and full independent GAP
replay have passed; do not repeat completed suites without a new issue.
Candidate N8 scope is c-d<=13/all classes<=24, with the previous
leading-degree<=10 theorem retained. General N8 remains unresolved.
The next bounded lead is research/notes/N8-hyperelliptic-lead.md: write
the complete constant-leading-quadratic integer-curve decision lemma,
then audit whether the group reduction really introduces only fixed
congruences and the claimed number of parameters. No class25/26 or
three-exception arbitrary-class extension is adopted. Alternate with
a concrete portfolio route or a candidate dependency review. All jobs
terminal;8 whole/2 partial/0 established novel; original deadline.


## Next step after the curve-arithmetic audit (2026-09-29T15:41:40.504278+00:00)

The complete constrained-curve lemma and finite Pell/resultant controls
are recorded; do not repeat their passed suites without a new issue.
Next audit research/notes/N8-three-exception-curve-reduction.md, especially
the full integer rank-one block quotient, its constant leading second
parameter, the affine initial constraints in early truncation, and every
universal residue after the delayed quadratic. Construct an actual group
family reaching that quadratic (the old class24 tests stop before it),
including nonprimitive scales and later residue conditions. Do not present
the older failed Lie perturbations as surviving absorbed branches.
The proposed at-most-three-exception/class26 scope remains unadopted.
Alternate with broader-portfolio work or a whole-entry dependency audit.
All jobs terminal; current counts8 whole/2 partial/0 established novel;
original deadline30 September10:04:49UTC.


## Next checks after three-exception evidence (2026-09-29T16:17:00.171390+00:00)

Revalidate and finish existing n8-delayed-quadratic-c26-v1 and
n8-delayed-quotient-c26-v1. Constructor diagnostics now show generic Smith
arithmetic as a bottleneck; preserve any timeout and exact source before
optimizing. Once a complete certificate exists, independently replay actual
group equations, full integer fibers and arithmetic. Formal substitutions
still need an ambient period-lattice specialization. Do not promote scope
from the small blocks alone; they have finite parameter fibers. Candidate
scope/counts and immutable deadline unchanged.


## Class26 continuation (2026-09-29T16:29:27.154798+00:00)

Revalidate the live n8-delayed-quadratic-c26-v2 and
n8-delayed-quotient-c26-v2 processes; previous v1 runs are terminal timeouts.
The constant-matrix arithmetic regression suites pass and need no repetition
without a new concern. Once the class26 certificate exists, replay its group,
families and arithmetic independently. Build and independently check the
ambient universal period quotient; all finite cosets must remain represented.
Prepared sources alone do not count as checks. Cache GAP workspaces only in
ignored large-artifacts with final hashes/regeneration notes. No scope promotion
yet;8 whole/2 partial/0 established novel; original deadline unchanged.


## Next native replay checks (2026-09-29T16:47:10.412636+00:00)

Constructor n8-delayed-quadratic-c26-v2 and its complete-family/arithmetic
replays pass. Both Python period versions pass; v2 includes terminal period.
Revalidate and finish existing n8-delayed-quotient-c26-v2,
n8-delayed-quadratic-group-gap-v1 and n8-delayed-periods-gap-v2. The first
native period run is a terminal timeout, not live. Preserve any further
failures and their exact sources before optimizing. Native independent
passes remain necessary before the proposed scope promotion. The restricted
Lie separating-functional lemma is a separate lead and does not settle
the general absorption question. Keep all quotient residues and the
immutable deadline; do not repeat passed arithmetic suites without cause.


## Next step after three remaining exceptions (2026-09-29T17:06:25.081284+00:00)

The three-exception/class26 extension has completed its finite audit. Do not
restart the timed-out generic Smith or full Hall-polynomial jobs; the exact
constant-matrix solver and native small-exponent group-coefficient method pass.
The compact substitution periods and full native residue replay pass as well.
All jobs are terminal. Return to a concrete unresolved portfolio question or
an adversarial candidate audit before expanding N8 further. A separate N8 lead
is the separating functional in research/notes/N8-compatible-deformation-functional.md:
it proves non-absorption only in its restricted Lie model. Extending it to
arbitrary fixed components and later exceptions would require a new proof;
finite rank agreement alone is insufficient. Keep broader discovery active,
then reserve the final eight hours for overlapping discovery and verification.
Counts8 whole/2 partial/0 established novel; original deadline unchanged.


## Working focus after the 2026-09-29T17:27:31.759755+00:00 portfolio checkpoint

The new N3 negative probes and N9 orbit obstruction do not close their
remaining gaps. Do not infer finite Aut(G)-orbit enumeration for general
retracts, nor a valid profile enlargement from empty final-layer torsion.
All jobs are terminal. Next pursue a specific structural route or a new
candidate concern, without repeating passed finite suites. The last-eight-
hours verification reserve and original deadline remain unchanged.


## Next checks after diagonal separation (2026-09-29T18:16:54.901693+00:00)

General N8 now has a specific unadopted route; read
research/notes/N8-diagonal-separation-lead.md Sections7--8. The first-exception
block can retain its full integer lattice: separation would make the first
parameter finite without any block quotient or curve arithmetic. All new
finite checks pass and are terminal. Do not repeat them without a concern.
Next test leading D with multiple E letters and a nonzero fixed lower X
prefix, then adversarially audit the whole leading-pair/exception/universal-
tail assembly. Only then decide whether to promote the same N8 candidate.
Keep wider discovery active and the last-eight-hours verification reserve;
original deadline30 September10:04:49UTC, counts8 whole/2 partial/0 novel.


## Diagonal-separation group tests complete (2026-09-29T18:25:39.745813+00:00)

Both additional actual group checks pass, including the nonzero fixed lower
first-factor prefix and the constant two-Y BCH term. All jobs are terminal.
Do not repeat or enlarge passed fixtures. Next freshly audit the entire
proposed general algorithm: finite leading pairs, polynomial averaging lemma,
normalization and full-block convolution, finite first-parameter recursion,
and universal tail. Recheck credited theorem hypotheses and original N8
statement/novelty independently of finite tests. The simpler recursion keeps
the entire integer block and needs no curve arithmetic or universal quotient
inside the first-exception block. Scope/counts remain unchanged for now.
Original deadline and last-eight-hours verification reserve still apply.


## After general N8 candidate (2026-09-29T18:40:27.581634+00:00)

General N8(b) is now an internally audited whole-entry coverage candidate;
novelty and specialist review remain pending. All jobs are terminal. Do not
expand or repeat passed N8 fixtures without a new mathematical concern.
Return to the wider unresolved portfolio or strengthen a different candidate
with a concrete dependency concern. Keep proof/statement/novelty statuses
separate, and reserve the final eight hours for overlapping verification and
final reporting. Current counts9 whole/1 partial(G9)/0 established novel;
original deadline30 September10:04:49UTC.


29 September19:42UTC: B9 yielded a genuine counterexample to the survey
height bound, independently checked in GAP. Preserve this related result
without counting the full entry. A useful next structural test is whether
right-shelf iterations can stay in one fixed Bn indefinitely: acyclicity
would then give infinitely many distinct special braids. A bounded list
alone cannot establish that.

B9 fixed-right-argument test completed: all3969 trajectories leave B5
within five steps. Park this bounded route; do not merely enlarge its
seed set. The certified height6/B5 result is preserved at6bb0c76.
Return to a distinct unresolved scope or a concrete candidate dependency
concern, retaining final-eight-hours audit/reporting reserve.


## B9 remaining sector after small-strand deduction (2026-09-29T20:54:32.070772+00:00)

B9 now has exact counts for every N except4, subject to candidate review
for the N>=5 infinite family. In B4 only exponent sum2 remains: count
right cosets A B2 in B3 admitting A=a S(c) with a,c special. Four prior
examples give the known total lower bound10. No exhaustion yet; a
bounded-height search or the square-root equation alone cannot prove it.
Do not repeat passed right-power tests. The one-parameter B3 matrix
root family includes nonspecial sigma2, so that route is not a criterion.
Consider this structural coset problem or return to wider discovery,
keeping the last-eight-hours audit/report reserve and original deadline.


## After coloring probe and lattice scope check (2026-09-29T21:09:47.972454+00:00)

Do not enlarge the completed depth12 B9 coloring search without a new
structural hypothesis. Its two-cone shortcut has an exact counterexample;
the B4 exponent-two coset problem remains. B12 has prior affirmative
coverage for5<=n<=12 via full braid-group lattice images and peripheral
fillings, so restrict any new B12 work to n>=13. Do not infer this covers
that remaining range or that B_n is fully residually hyperbolic.
Return to a genuinely different unresolved scope or a concrete candidate
proof concern. Original deadline and final-eight-hours audit reserve hold.


## Working checkpoint,29 September approximately22:15UTC

N9 now has an isolated-input strengthening and a full2017 free-case
source audit in isolated-inputs-and-prior-scope.md. This supplements the
existing fixed-group candidate without changing the count.

B9 now excludes the entire known infinite B5 family as a source of
exponent-two B3 parameters through the ten known B4 inputs. Its other
proposed recurrence-tail cancellation is exactly a known parameter ray.
Do not enlarge finite searches along either route; the new universal
obstructions are in research/notes/B9-family-return-obstruction.md.
Other underlying families and the full B4 exhaustion remain unproved.
Tally remains10whole/2partial/0established-novel. Original deadline unchanged.


## After interim review index (2026-09-29T22:28:26.470635+00:00)

Use reports/CURRENT_RESULTS.md for controlling candidate scopes; do not
confuse historical checkpoints with the current ten/two tally. A targeted
F38 rigid/solid check found no new issue and needs no repeated finite suite.
Continue wider discovery or a concrete new dependency concern. A useful
remaining verification priority is the general N8 diagonal polynomial
separation lemma: its universal argument, not more fixed small Lie spaces.
All jobs are terminal. Keep the original deadline and final-eight-hours
verification/reporting reserve; do not create FINAL_REPORT.md prematurely.


## After N8 analytic formal check (2026-09-29T22:35:08.048427+00:00)

The contraction estimate and abstract maximum principle now pass Lean;
see averaging-lean-audit.md for exact hypotheses and the unformalized
application boundary. Do not repeat this check or enlarge finite Lie fixtures
without a new concern. The positional-polynomial identities and full-block
normalization remain useful substantive review targets; alternatively pursue
a different unresolved scope. Preserve all original deadline/counting rules.


## After the F39 unimodular obstruction (2026-09-29T22:48:31.363014+00:00)

Do not try to repair the injection relaxation for F39 using determinant±1
or surjectivity on all nilpotent quotients: the new explicit image defeats
these requirements in every rank. The bounded-orbit extension is a deduction
from prior F40, not a new problem resolution. F37's primitive-length
reflection remains a different unanswered question. All GAP jobs terminal.
Return to a distinct unresolved structural route or a concrete candidate
concern; preserve final-eight-hours audit reserve and original deadline.


## After N8 division-free bridge (2026-09-29T23:03:54.295384+00:00)

The positional evaluation-to-averaging step and concrete origin-transfer
sum/l1 properties now pass Lean; see polynomial-bridge-lean-audit.md.
Do not repeat passed checks without a new concern. The formal files remain
separate ingredients: coefficient encoding, cyclic relocation and the
contracting-word/max-principle assembly are still written arguments.
The larger review priorities are the full-block Lie projection and
convolution, and the remaining other candidates' deep imported inputs.
Wider discovery remains authorized within the original deadline, with
the final-eight-hours verification/reporting reserve unchanged.
All jobs terminal; ten whole/two partial/zero established novel.


2026-09-29T23:09:41.981280+00:00: The subsequent B9/MA5 scope scan supplied no new structural route.
Do not repeat those searches or increase existing finite braid bounds
without a new hypothesis. The N8 full-block convolution and rational
prefix normalization, or a different candidate's precise imported theorem
hypothesis, remain concrete audit targets. Twenty positional/transfer
Lean declarations are accepted at48721c0; they do not formalize the
full N8 group algorithm. Keep broader discovery and the original
final-eight-hours reporting reserve; no FINAL_REPORT yet.


## After full-block implication check (2026-09-29T23:18:16.096994+00:00)

The universal triangular/column-span implication and at-most-two root
values now pass Lean in six declarations. The formal model allows
polynomial multipliers through linear endomorphisms. Rechecked the
normalization, weight bounds and residual-coordinate passage; no new
gap found, but those remain written proof obligations. Do not repeat
these passed checks or relabel them full N8 formalization.
Return to broader discovery or a concrete concern in another candidate;
keep the final-eight-hours audit/reporting reserve and original deadline.
Ten whole/two partial/zero established novel; all jobs terminal.


## F20 finite-image checkpoint (2026-09-29T23:31:56.543036+00:00)

The seven-group F20 finite-image search is finished and inconclusive. Do not repeat or enlarge without a new structural reason. Continue a distinct unresolved scope or a concrete candidate dependency audit, retaining the original final-eight-hours audit/reporting reserve. All jobs terminal; deadline unchanged.


## N8 concrete transfer sequence (2026-09-29T23:43:16.841041+00:00)

N8 now has a concrete convergent sequence of permitted half-transfer words verified in Lean, not merely an abstract contraction inequality. See sweep-convergence-lean-audit.md. Do not repeat these passed checks or label the separate formal ingredients a fully formal algorithm. Return to a distinct unresolved route or a concrete imported dependency concern; preserve final-eight-hours verification/reporting reserve. All jobs terminal; original deadline unchanged.


## After concrete N8 sweep check (2026-09-29T23:46:08.633786+00:00)

N8 progress committed at8dce224; nineteen universal transfer declarations
accepted, with full application boundary in its audit. A targeted S1/S2
source check found no new solution. Archived Linton2407.09272v2 and kept
rational/ordinary and infinite-intersection/finite-term distinctions;
see S1-S2-late-scope-check.md. No further mathematical job, no push, no
count or deadline change. All jobs terminal. Continue a distinct lead
or substantive dependency audit; keep the original final-eight-hours
verification/reporting reserve.
