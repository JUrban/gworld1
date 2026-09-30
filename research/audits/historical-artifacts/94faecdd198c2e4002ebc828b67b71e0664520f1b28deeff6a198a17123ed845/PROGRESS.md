# GroupWorld progress

Active experiment: 28 September 2026 10:04:49 UTC to 30 September 2026 10:04:49 UTC.

Current counts: **2 partial candidates**, **10 whole-entry candidate solutions**, **0 established novel results**. All twelve candidates await independent review; novelty remains provisional. See [the current results and review guide](CURRENT_RESULTS.md) for controlling proofs and exact scopes. The development notes below include superseded intermediate scopes as well as current results; they preserve the research history.

- 30 September, 08:18 UTC: B9's [complete fixed-color procedure](../problems/B9/fixed-color-decision.md) decides every special partner of a supplied first braid via strand deletion and at most m-1 specialness tests. All 52 original first-color fixtures complete:40 have no partner,12 have16 total partners,all in known classes. Native GAP independently checks every decision, including failed-division and nonspecial-root controls. B4 still requires classification of unrestricted first colors; no tally change.

- 30 September, 07:55 UTC: G9's [flow shortening](../problems/G9/flow-shortening-supplement.md) raises the lower bound to **2.676871486** within the same completed atom families. Among 62,003 central words, 286 shorten by two letters; separate GAP replay verifies every replacement and the resulting rational series. Upper bound and partial-candidate count are unchanged.

- 30 September, 07:48 UTC: G9's [two-ended completion](../problems/G9/two-ended-completion-proof.md) further improves the lower bound to **2.676836909**, with the same upper bound. The original atoms supply 3,239 complete two-parameter families and one height-one family. Python and separate GAP reconstruction verify the finite description, all central representatives and the exact rational root enclosure. No larger bridge enumeration or new problem count is added.

- 30 September, 07:29 UTC: G9's [horizontal completion](../problems/G9/horizontal-completion-proof.md) improves the current lower bound to **2.668423113**, retaining upper bound **2.943737759**. The same 21,483 original atoms give 8,881 complete horizontal families and an exact rational alphabet series, independently reconstructed in GAP. The older G9 entry below describes the superseded finite-alphabet lower endpoint. No new bridge enumeration or problem count is added.

- B9: a new [infinite-family proof](../problems/B9/infinite-family-proof.md) gives countably infinitely many special braids in every B_N with N>=5. A recurrence constructs special terms whose high strands cancel; an integral Burau entry n(n-1) separates all parameters. Independent GAP verifies the symbolic entry and six faithful-action instances. The [audit](../problems/B9/infinite-family-audit.md) retains the first constant-polynomial comparison failure. The [small-strand supplement](../problems/B9/small-strand-proof.md) deduces exact counts 1, 2 and 4 in B1, B2 and B3 from Dehornoy's prior results; only the B4 exponent-two sector remains unclassified. B9 remains one partial candidate. This extends the earlier uncounted height counterexample; external review and novelty remain pending.

- N9: a new [candidate proof](../problems/N9/proof.md) answers(a) negatively in one fixed torsion-free class-two group. Its two-generator subgroups encode a fixed nonrecursive Diophantine set. A modulus-three normalization forces integral circuit values; the ambient presentation never changes. GAP independently checks the full integer kernel and seven retractions in a fixed toy group, alongside17 general-criterion examples. Lean verifies the universal integer normalization, not the full group theorem. The [audit](../problems/N9/audit.md) retains the initial Lean abort and distinguishes the prior uniform theorem and free-nilpotent part(b). This adds one whole-entry coverage candidate, with prior(b) credited; novelty and external review remain pending.

- N8: now a **whole-entry coverage candidate**, combining the general N8(b) algorithm with prior N8(a). The [consolidated proof](../problems/N8/general-proof.md) handles every finite rank and class. Its diagonal separating functional fixes each first exceptional parameter to finitely many integers, even with arbitrarily many later columns; exact universal periods finish the tail. The [audit](../problems/N8/general-audit.md) records44 independently reconstructed Lie spaces, three actual group fixtures, complete integer lattices and the limits of those checks. The full all-rank implementation, independent specialist review and novelty assessment remain outstanding. This promotes the same N8 entry and does not add another entry to the ten-candidate portfolio.

- G9: a new partial candidate supplies an effective two-sided approximation algorithm for the standard growth constant in every finite rank. A flow-recoverable unfolding proof gives an explicit error bound. Separate finite certificates give `2.658596558 <= lambda_2 <= 2.943737759`: GAP independently verifies all 21,483 bridge atoms for the lower bound, and all 648 relations, 7,872 transitions and 1,968 integer inequalities for the upper bound. The exact constant, fine-precision computation and novelty remain unresolved. See `problems/G9/flow-growth-proof.md` and its audit. The extension in `problems/G9/solvable-extension-proof.md` gives the same modulus for every free solvable rank and derived length. Independent GAP checks68 noncommutative-deck recoveries; this does not add another candidate. The website's quoted decimal is used only for comparison; its cited self-avoiding-walk paper discusses numerical estimates.

- F38 is now a whole-entry candidate: the new `problems/F38/bounded-proof.md` answers part (c) in every finite rank, alongside the existing part (a) candidate and prior part (b). Bounded translation equivalence is characterized by commensurable conjugacy stabilizers. The key sufficiency argument imports Sela's graded shortening theorem, with explicit free-factor, shortness and limiting-kernel checks. Independent GAP reconstructs 12 complete Whitehead graphs and 20,948 edges, checks 15 finite orbits and six negative witnesses, and replays 2,376 factor-twist records and 234 rank-two bounds. These checks do not prove the structural theorem application. Specialist review and novelty remain pending; see `bounded-audit.md`. Earlier restricted-case and exponential-envelope notes are preserved as historical stages.
- F25: an exact12-cycle shows why Lee's degree-sorting argument cannot simply drop its distinct-frequency hypothesis. Every basepoint and generator order fails; independent GAP verifies the complete finite graph. This is a proof-strategy obstruction, not a solution or counterexample to the polynomial bound. See `research/notes/F25-equal-frequency-obstruction.md`.
- The independent repository, frozen corpus, clock, recorded computation runner and research plan are in place.
- N3 follow-up: an exact torsion-killing criterion identifies what a replacement cover construction must prove. Explicit witnesses show that enlarging every local bound by one still fails for a three-generator profile. Standalone integer arithmetic checks the full normal-subgroup certificate and corrected word; GAP independently verifies both quotient orders and free-group identities. Failed additive, large-preimage and uncorrected-prefix routes are retained. This is supplementary progress, not a solution to N3; see `research/notes/N3-profile-repair-obstruction.md`.
- A5: Jayadevan's September2026 prior affirmative result is now reproduced in Lean4.24: the author build,1624-declaration transitive axiom audit and independent exact statement checks pass. Earlier permission/restatement failures are retained. See `research/notes/A5-prior-Lean-proof-audit.md`. External prior, no new candidate.
- M3: A5 plus Bieri–Strebel gives an effective finite presentation of the maximal metabelian quotient on promised solvable inputs. Deciding whether its normally finitely generated kernel is trivial remains open here. An exact S4-to-S3 control passes GAP; `research/notes/M3-effective-metabelian-quotient.md`. No count change.
- First textual reading of all 195 entries completed, including 49 heading-star entries. Full original statements, linked background and residual scope remain part of targeted audits.
- F42: derived the exact extremal formula and a covering-graph construction, then found Koch-Hyde–Olive's September 2026 preprint already proving the same answer. Preserved as a rediscovery, excluded from new-solution count.
- F11: derived a cyclic-retract/index-three counterexample, then found the same mechanism in Snopce–Tanushevski–Zalesskii (2019). Also excluded. Original HTML screenshots for F11/F42 have now been inspected.
- Primary sources also report prior resolutions of F15, F30, F31 and F40. B11 has a 2025 primary seminar announcement; full proof not yet located. Scope checks are recorded in `research/triage.csv` and `literature/LEDGER.md`.
- N8(b): the latest partial candidate covers all targets through class 24, all targets with c-d<=13, leading degrees through ten in arbitrary class, branches with at most two remaining exceptional offsets, and the earlier separated-offset scopes. The new polynomial-tail argument retains every later coordinate, including further exceptional kernels. Independent GAP checks all eight homogeneous kernels in a three-exception range, 3,201 polynomial columns and 34 joint controls across actual weighted class-21/24 groups, two complete integer fibers and four group witnesses. A class-25 mixed-term boundary is retained. See `problems/N8/fourteen-layer-proof.md` and `fourteen-layer-audit.md`. These finite checks do not prove the structural all-rank lemmas; the uniform branch algorithm is not implemented end to end. General N8, specialist validation and novelty remain unresolved. A separate hyperelliptic route is an unverified, uncounted lead.
- H4: candidate negative answer to polynomial-time conversion into an explicit Dehn presentation. Short presentations of finite metacyclic groups have doubly exponential order; a forbidden-factor automaton bounds the order of any finite group in terms of every Dehn presentation's size. Thus every explicit output is superpolynomial, even with changed generators. Proof: `problems/H4/proof.md`. GAP verified four finite models and independently computed three presentation orders. Related finite-group lower-bound ideas from2012 are credited; novelty and specialist review remain outstanding. Compressed output is a different specification. The strengthened bound in `problems/H4/infinite-input-proof.md` also covers infinite non-elementary virtually free inputs. GAP independently checked three conjugacy-class partitions and two free-kernel presentations (ranks6 and60); this remains the same candidate.
- F28: explicit negative answer using a rational matrix conjugation on an index-two subgroup of F2. The image also has index two, and the bounded-orbit argument excludes every nontrivial invariant subgroup. Candidate proof: `problems/F28/proof.md`. Exact matrix/word checks covered 13,120 words; GAP independently checked subgroup indices/ranks and defining identities. Related arithmetic constructions in the literature establish weaker normal-subgroup statements; a matching prior full answer has not yet been found.
- F34: whole-entry coverage combines candidate (a) with known (b); this is a counting reconciliation, not an additional solved subpart. See `research/notes/F34-coverage-reconciliation.md`. Part (a): candidate uniform decision algorithm for potential positivity in every finite rank. A positive image under an injection pulls back through a spanning-tree basis; a nonzero-determinant test on the full EDT0L solution relation decides existence. GAP independently verified270 explicit positive automorphism witnesses in ranks2--4 and3 scope controls. Rank2 and part(b) are prior; potentially new scope is rank>=3. Full recompression is imported, not implemented. Proof and audit: `problems/F34/part-a-proof.md`, `part-a-audit.md`.
- F38(a): candidate all-finite-rank decision procedure for translation equivalence, using a determinant product, a full EDT0L solution relation and finite rational span closure. Rank two is prior; potential novelty is ranks at least three. The final polynomial stage passed independent GAP replay on43 controlled systems,902 basis vectors and1151 transitions, with309 independent free-word checks. Full recompression is an imported theorem, not implemented. Part (c) is now covered by the separate candidate described above. Proof and audit: `problems/F38/part-a-proof.md`, `part-a-audit.md`.
- F41: a full intended-scope candidate now gives square-root orbit growth for every nontrivial nonprimitive word in every finite rank. A signed piece-cover counting lemma combines Kharlampovich--Myasnikov's definable-set theorem with Pillay's characterization of generic elements. Proof and audit: `problems/F41/multipattern-proof.md`, `multipattern-audit.md`. Exact Python checks cover 46,536 positional schemes; GAP independently verifies 77 representative word counts. The identity exception is explicit; the stronger cyclic-orbit conjecture is not claimed. The earlier rank-two argument and prior-scope credits are retained. This promotes the same entry from partial to whole, without adding a ninth candidate. Deep imported theorems and novelty remain for independent review.
- N5: candidate uniform decision algorithm for direct decomposability of every finitely generated nilpotent group, including torsion. A finite bound on possible factors modulo the centre leads to integer central-extension lifting conditions. Full proof and audit: `problems/N5/proof.md`, `audit.md`. The centre solver passed 120 cases and 54 independent GAP projection checks; complete finite-central-quotient pipelines agreed on 82 finite groups and seven infinite examples, with all 36 constructed group decompositions verified in GAP. The general rational-decomposition stage is invoked as established machinery, not claimed as implemented here.
- M0: candidate positive answer in every finite rank: an endomorphism of a free metabelian group preserving all primitive elements is an automorphism. A singular Fox matrix over a finite field is detected by a primitive word constructed from explicit elementary free-group automorphisms. Proof and audit: `problems/M0/proof.md`, `audit.md`. Python and GAP independently checked 177 records, including genuine extension fields, basis changes, singular examples and automorphism controls. Rank at most two was already known; the potentially new range is rank at least three.
- M0 follow-up: an end-to-end constructor now selects the normalizations, character and primitive witness from input endomorphism words. GAP independently verified 29 new witnesses and 13 exact unit determinants; two bounded searches deliberately returned inconclusive. Three failed checker runs are retained. Details are in `problems/M0/constructor-audit.md`; this strengthens the existing candidate without adding another count.
- GA5(b): exact prior answer confirmed in Bartholdi–Sidki, Theorem 1.2 (preprint 2018, published 2020): the infinite-rank free abelian group has a self-similar action on the binary tree. Excluded from new-result counts; the 2023 intransitive construction is no longer used as the main scope evidence.
- OR2, OR6, OR7, OR8, OR11 and OR12: prior positive/negative answers or direct consequences of published theorems now checked against the full original page. In particular Wang–Zhang's July 2026 preprint explicitly answers all three subparts of both OR7 and OR8. OR12's finite-index transfer is written out in `research/notes/OR-prior-resolutions.md`. None increases the candidate tally.
- AUX3(b) and FP17: prior positive answers checked and excluded. AUX3(a) remains separate; FP17 is supported by the exact primary publisher abstract, with full-text access limitations documented.
- MA3, MA5 and M4: further primary scope checks recorded. The available results cover special parabolic subgroups, connected linear groups and finite-rank projective metabelian groups respectively; none settles the corresponding full entry. An FP9 universal-tree lead retains an explicit effectivity gap and is not counted.
- M4 follow-up: the full Artamonov 1978 proof is now archived and read. Its module freeness and compatible-basis steps remain finite-rank; Bass's big-projective theorem does not directly apply to the countable Laurent ring. No new candidate.
- N3 source audit: a 2003 paper states a full positive answer, but its proposed torsion-free construction fails. An allowed three-generator class-five profile has an explicit central element of order two, verified by standalone integer-series arithmetic and GAP. This is a counterexample to the paper's Proposition 3.5, **not** to N3; it adds no solution count. Proof and certificates: `research/notes/N3-published-cover-audit.md`.
- B3, B8 and B13: prior positive answers now checked against original statements. B3 is the July/September 2026 Bharathram–Birman–Brendle preprint; B8 is Fromentin (2011), with the generator-index convention converted; B13 is Bell–Schleimer (2025), for fixed strand number. All are excluded from discovery counts. Details: `research/notes/braid-prior-resolutions.md`.
- B9: a [29-letter special braid in B5](../problems/B9/height-counterexample.md) has minimum expression height six, refuting the literal bound in Dehornoy's survey, Question3.19. GAP independently checks eleven such examples and regenerates every lower-height finite matrix image. The unrestricted GroupWorld counting question remains unresolved; this related result adds no candidate count. The audit retains the initial GAP timeout and the successful revised evaluation.
- F20: bounded KBMAG probes reproduce the known rank-two weight-five case. At weight six, ten of eighteen next-layer commutators reduce to identity; larger runs hit rewriting limits, and one subsequent reduction failed. No new solution or counterexample follows. All failures are retained.
- GA2: the biautomaticity theorem located assumes finite presentability, while the question assumes only finite generation. That scope remains unresolved here.
- GA3: a whole intended-scope candidate proves that every nonabelian Lambda-free group discriminates its free square by fixing one factor and conjugating the other. The proof controls the collapse to a real tree and extends the resulting maps to arbitrarily generated groups. Guirardel's collapse theorem and the boundary separation machinery, also present in Rybak2026, are credited prior work. The literal abelian omission is separate and not counted. Proof and audit: `problems/GA3/proof.md`, `audit.md`. Python checked160 exact cone separations and46 dynamics inclusions; independent GAP checked6,400 free-group images, three bad-separator controls and49 abelian controls. Those computations do not verify the general collapse. The first GAP reserved-variable failure is retained. Specialist review and novelty remain outstanding.
- E5 and H12: prior full positive answers checked in Sela and Groves–Hull, including arbitrary factors for E5 and torsion for H12. Both are excluded from discovery counts. Chiodo’s restricted impossibility theorem for A6 does not settle arbitrary-word output; that scope gap is recorded.
- A4: the algebraic cyclicity decision follows from prior residual finiteness of knot groups and enumeration of proofs/finite quotients. Hass’s primary argument and the presentation-only adaptation are documented; this is excluded from discovery counts.
- H13, FP6 and N1: prior answers checked. Bridson supplies synchronously combable groups that are not automatic; virtual fibering gives virtually free-by-cyclic knot groups; the N1 fixed-element classification already includes higher ranks. Scope and reading limits are in `research/notes/H13-FP6-N1-prior-scope.md`.
- FP21: a rank-two reformulation, without a new solution, is in `research/notes/FP21-braid-reduction.md`. Dlugie's splitting and residual finiteness of the three-strand quotient make BP(2,m) residually finite exactly when the four-strand truncated braid group is. GAP checked the splitting's finite presentation identities in 1.83 seconds. The available triangle-free Shephard theorem does not cover the four-strand presentation; larger exponents remain unresolved here.
- F27: Barmak's tiling examples lie in the excluded commutator-subgroup case. The 2025 one-relator survey still states the actual question as open. A bounded normal-root investigation yielded only elementary constraints and a stalled stabilizer-orbit route; no new candidate. Exact scope and sources are in `research/notes/F27-normal-root-lead.md`.
- GAP 4.16.1 and relevant packages are available. Chromium rendering works using locally extracted system libraries, without root access. The first GAP check exposed an nq crash on the rank-one/class-three request; the rerun handles the infinite cyclic case directly, and the failed log is retained.

See `research/PLAN.md` for the portfolio and `research/LOG.md` for dated progress. Known results and bibliographic updates are not counted as new solutions.

Latest scope refresh: S9 is a prior full positive answer (Timoshenko2006),
already recorded in the final paragraph of the website background. For
S3, the 1998 primary paper also covers last-derived relators; the broader
module-invariant route retains a group-ring annihilator obstruction.
See `research/notes/S3-S9-scope-followup.md`. Neither adds a candidate.

M0 now also has a terminating constructor with an explicit finite-field
bound, using Kronecker substitution and deterministic factorization.
GAP verified nine new witness certificates and three unit determinants.
See `problems/M0/kronecker-construction.md`. This strengthens the same
candidate and makes no claim of practical complexity or specialist review.

Earlier N9(a) follow-up: the fixed ambient group remained an essential gap
in that attempted construction; the later candidate above uses a different encoding.
An attempted reduction by varying retracts of a fixed base fails
because retracts reflect solvability of equations. The prior uniform
construction has been written with a class-two coproduct, resolving
a cross-commutation issue in the literal central-product reading of
the accessible source text. GAP checked four exact examples. The
original article PDF was not obtained, so its terminology is qualified;
see `research/notes/N9-fixed-ambient-and-coproduct.md`. No result count
is added.

N8(b) uniform-family extension: in every class c>=6 and finite rank, the
candidate algorithm now covers targets with leading term ad_z^(c-4)(T)
in degree c-2, for nonzero rational z in L1 and T in L2, with arbitrary
later layers. A parity argument and nonzero quadratic obstruction give
a finite lifting algorithm. Independent GAP replay checked nine witnesses,
28 linear decisions and14 polynomial certificates over15 supported targets
in classes7,10,11; scope controls distinguish unsupported commutators from
negative decisions. See problems/N8/iterated-adjoint-proof.md and its audit.
This extends the same partial candidate. The all-target class-nine extension has also completed its bounded
computational audit. Novelty and independent specialist review remain
outstanding for both extensions.

N8(b) second uniform family: for every odd c=2n+7>=9, the candidate
now also recognizes and decides targets with nonzero degree-(c-2) term
ad_C^(n+1)(T), C in L2 and T in L3. The proof excludes every other
leading type, then uses a parity kernel and quadratic obstruction.
Independent GAP checks cover ten supported targets in class9/rank3
and class11/rank2: six witnesses,21 linear decisions, seven polynomial
certificates and35 samples. A class13 replay timed out before any witness
and is retained as incomplete. See `problems/N8/degree2-iterated-proof.md`
and its audit. This extends the same partial candidate and changes no tally.

N4/MA6 scope refresh: prior automorphism-tower theorems cover free
nilpotent groups, not the full N4 scope. July2026 primary work still
states rational parabolic non-freeness as a conjecture and disproves
the converse of the orbit test. Neither check produces a new result.
See `research/notes/N4-MA6-current-scope.md`.


## 2026-09-28T21:27:09.307132+00:00 — wider scope audit

F24(b) is excluded as a prior full positive answer: Diao-Feighn 2005 explicitly identifies it as a consequence of its Grushko algorithm. H5 recognition methods still supply no negative decision here. The H4 candidate is compatible with polynomial hyperbolicity certifiers that permit failure; see research/notes/F24-automatic-scope-refresh.md.


## 2026-09-28T21:41:56.112567+00:00 — nonlinear class-ten extension

N8(b) now also covers the nonlinear class-ten family rho*[z,2[T,ad_z^3 T]+3[ad_z T,ad_z^2 T]], with leading degree eight and arbitrary later layers. The written argument is all-rank; independent GAP evidence covers five rank-two targets. Four rank-three checks concern only family recognition. Original lead, corrected test failure and exact sources are retained. No full class-ten or new-entry result is claimed.


## 2026-09-28T22:08:34.500889+00:00 — F38(a) candidate

F38(a): candidate all-finite-rank decision procedure for translation equivalence, using a determinant product, a full EDT0L solution relation and finite rational span closure. Rank two is prior; potential novelty is ranks at least three. The final polynomial stage passed independent GAP replay on43 controlled systems,902 basis vectors and1151 transitions, with309 independent free-word checks. Full recompression is an imported theorem, not implemented. F38(c) remains unresolved here. Proof and audit: `problems/F38/part-a-proof.md`, `part-a-audit.md`.


## 2026-09-28T22:21:55.381017+00:00 — F34(a) candidate

F34(a): candidate uniform decision algorithm for potential positivity in every finite rank. A positive image under an injection pulls back through a spanning-tree basis; a nonzero-determinant test on the full EDT0L solution relation decides existence. GAP independently verified270 explicit positive automorphism witnesses in ranks2--4 and3 scope controls. Rank2 and part(b) are prior; potentially new scope is rank>=3. Full recompression is imported, not implemented. Proof and audit: `problems/F34/part-a-proof.md`, `part-a-audit.md`.


## 2026-09-28T22:34:32.776894+00:00 — audit checkpoint

The shared F34(a)/F38(a) polynomial method now has a separate internal audit and a finite accepted-path bound after a grammar is supplied. This adds no candidate or implementation claim; general recompression remains imported. A concrete subgroup example blocks the same determinant substitution for F39(a). See `research/notes/F34-F38-shared-foundation-audit.md`.

GA1's proposed nonorientable-surface obstruction is ruled out by prior Z^2-free actions. General root adjunction still falls outside the combination theorem checked here; see `research/notes/GA1-root-adjunction-boundary.md`. No result count changes.


## 2026-09-28T22:55:03.075849+00:00 — complete gamma_8 stratum in class ten

Extended the same N8(b) partial candidate to every gamma_8 target in class ten, in all finite ranks. The new proof excludes all first-kernel exceptions except the previously handled nonlinear family. GAP independently verified24 structural cases and the complete rank-two target certificates:9 witnesses,44 linear decisions,1 polynomial certificate,5 samples. A rank-three structural run timed out after9 completed records; two initial GAP fixture-loading failures are retained. No full class-ten theorem or new problem count is claimed. See `problems/N8/class10-third-proof.md` and `class10-third-audit.md`.


## 2026-09-28T23:14:32.455430+00:00 — boundedness and fixed-subgroup scope

F38(c)'s automorphism quantifier cannot be replaced by all injective endomorphisms. A prior rank-two pair and 108 Python/GAP word checks document the obstruction and failure under free-factor inclusion; F38(a) is unaffected. See research/notes/F38-bounded-scope-boundary.md. F1(b)'s rank-three case and F26's rank-three/UPG cases are prior and excluded; see research/notes/F1-F26-prior-rank-three.md. New class-ten N8 ideas remain uncounted. Tally:4 whole,4 partial,0 established novel.


## 2026-09-28T23:36:21.500599+00:00 — all-target class-ten extension

N8(b) now has a candidate decision procedure for all targets in class ten, in all finite ranks; see problems/N8/class10-proof.md and class10-audit.md. Independent GAP replay verified16 witnesses,111 linear decisions (32 negative),13 coupled systems (6 inconsistent),9 polynomial certificates (4 empty),45 samples, and14 rank-two structural records. The rank-three Python structural suite passed17 cases; two GAP replays timed out and are explicitly incomplete. A saved first-run failure exposed a final-layer conjugation term and was corrected. Tally unchanged at4 whole,4 partial,0 established novel.


N5 integrality follow-up: ten targeted splitting controls and eight central relator systems passed. Independent GAP replay verifies four positive projections and all eight direct lift decisions, including four negative systems. The audit rejects arbitrary modular idempotents with incompatible local ranks; no correction was needed. See `problems/N5/integrality-audit.md`. F6 remains distinct from the prior Out(F3) theorem; the exact Aut/Out scope is recorded in `research/notes/F6-outer-versus-automorphism-scope.md`. Counts are unchanged.


Uncounted N8 lead: an odd-adjoint construction proposes another family
in classes11,15,19,... . Formal identities and the rank-two class11
kernel/obstruction passed structural checks, including a GAP replay.
The first GAP attempt timed out and remains recorded. Group-level
construction and a separate proof audit are outstanding; the current
candidate scope and counts have not been enlarged. See
`research/notes/N8-odd-adjoint-family-lead.md`.


The previously uncounted odd-adjoint lead has now been promoted to an
extension of the same N8 partial candidate after the integral group
implementation, GAP replay and separate internal recognition/proof audit.
The historical lead is preserved unchanged. Its earlier expanded-word
GAP timeout remains a failed structural run; the successful recursive
replay and the new group replay are separate evidence. No candidate
count increase or established novelty is claimed.


## 2026-09-29T00:36:11.621403+00:00 — H4 infinite-input extension

The torsion-conjugacy bound gives m log_2(2m)>2^n-n-1 for every explicit Dehn output of the short metacyclic family and its free product with Z. This extends H4 to infinite non-elementary virtually free inputs and strengthens the output bound. Eight exact formula checks, four explicit orbit partitions, three independent GAP class partitions and two GAP free-kernel presentations passed. The short torsion representative lemma is prior Batty/Papasoglu material, explicitly credited. No torsion-free or compressed-output result is claimed.

F37’s proposed determinant shortcut remains unproved for products of primitives; the precise reflection and encoding gaps are saved in research/notes/F37-embedding-reflection-gap.md. Counts remain4 whole,4 partial,0 established novel.


Wider portfolio checkpoint,29September: the locally free construction route for MA4 is ruled out by a finite-normal-generation obstruction, with a perfect locally free linear control preserving the distinction. Recent compressed-primitivity and four-strand hyperbolic-quotient theorems do not settle C2 or B12. Proof/scope notes and source audits are saved; no candidate count changes.


N8 central-factor audit,29September: an alternative finite-projective-fibre proof and Groebner/multiplication-matrix implementation supplies the same all-class central-target decision result without the Klyachko rotation lemma. Thirteen Lie cases and two affine controls passed; independent GAP checked16 positive group witnesses. The first conversion failure is retained. See `problems/N8/projective-factor-audit.md`. This strengthens verification of the existing partial candidate; counts remain5 whole,3 partial,0 established novel.


F20 follow-up:143 selected weight-six finite covers show no surviving weight-seven commutator in integral first homology. GAP and Python/FLINT agree on these and75 known weight-five controls. The bounded result is inconclusive; failed runs are retained. See `research/notes/F20-finite-cover-homology.md`. A broader fixed-coproduct retraction obstruction is added to the N9 note, without answering its fixed-ambient problem. Counts remain5 whole,3 partial,0 established novel.


F38(c) follow-up: an implemented necessary condition decides whether the two conjugacy stabilizers are commensurable. If they are not, it returns an exact automorphism proving unboundedness. Python controls and two independent GAP certificate replays passed; one earlier GAP failure is preserved. Sufficiency is unproved, so this is a research tool, not a full decision procedure. See `research/notes/F38-stabilizer-obstruction.md`. Counts remain5 whole,3 partial,0 established novel.


The F38 stabilizer condition now has an exact weaker interpretation: it decides whether each length can be bounded by some function of the other, and supplies effective exponential bounds. Linear comparison remains unresolved. Proof: `research/notes/F38-stabilizer-length-envelope.md`; counts unchanged.


## 2026-09-29T03:13:42.489680+00:00 — prior filling case for F38(c)

F38(c): implemented the prior filling positive case. Gupta–Kapovich Propositions4.16–4.17 already characterize filling by finite conjugacy stabilizer and decide it; Kapovich–Lustig Proposition13.8 already gives boundedness for filling pairs. The existing mod-three orbit routine now detects finite outer groups via basis classes and pair products. Six group, six word and four pair controls passed. Independent GAP replay verified7 negative witnesses,52 finite orbits,287 inverse pairs and293 transitions. Both runs have empty stderr; no mathematical failures. Non-filling pairs passing the necessary condition remain unresolved. See `research/notes/F38-filling-recognition.md`. No count increase:6 whole,3 partial,0 established novel.


## 2026-09-29T03:19:17.768194+00:00 — GA1 prior negative answer

GA1 is negative in the substantive nonabelian scope by an immediate consequence of Brady–Ciobanu–Martino–O Rourke2009: x^4 y^4=z^4 in a tree-free group forces commutativity. Taking fourth roots of arbitrary a,b,ab shows every divisible tree-free group is abelian. The free Q-groups of ranks zero and one retain elementary positive actions. The original unstarred entry is retired as prior; no new candidate. See `research/notes/GA1-prior-fourth-power-obstruction.md`.


## 2026-09-29T03:35:05.537079+00:00 — S5 prior proof verified

S5 is retired as a prior affirmative result by Achyuth Jayadevan. The public Lean development was pinned and built here; all298 project-declaration axiom checks and an independent exact-statement check passed. Full source and compact logs are archived; large toolchains and caches remain ignored. Details and trust limits: `research/notes/S5-prior-Lean-proof-audit.md`. This is external prior work, not another candidate or specialist review. Counts remain6 whole,3 partial,0 established novel.


## 2026-09-29T04:05:15.277767+00:00 — F28 formal matrix verification

F28 now has a simpler integral proof and a Lean verification of the entire matrix-orbit obstruction: every infinite integral sequence X_(n+1)Q=QX_n with det X_0=1 starts at ±I. An invariant positive energy and odd recurrence replace the real norm and algebraic-integer arguments. The free-group/ping-pong bridge remains written mathematics. Successful final compilation and transitive axiom audit passed in8.848s; three failed versions and one warning-bearing intermediate success are preserved. See `problems/F28/matrix-lean-audit.md`. Counts remain6 whole,3 partial,0 established novel, with independent review outstanding.


F37/N3 route checks: the inspected commutator-length embeddings do not meet the determinant condition needed by the F37 lead. N3’s existing torsion example already defeats strict-monotone and disjoint-superadditive profile repairs; a nested finite-subset construction cannot cover arbitrary cardinalities. Details are appended to the existing notes. Neither problem has gained a solution here.


C4 computational checkpoint:45832 bounded FullHRed evaluations completed; independent GAP replay checked22501 selected steps and67 faithful Artin input/output pairs. No asymptotic bound obtained. The width3 theorem is prior, and a broader proposed length-bound route was disproved by Dehornoy–Wiest2004. Details: `research/notes/C4-handle-reduction-probe.md`. No candidate-count change.


N8 structural advance: a new coefficient/Lyndon argument proves that every first correction of leading type(1,q) has at most one parameter, in every degree. An exceptional leading factor is supported on the derivative chain of that direction. Independent Python/GAP agree on22 related finite systems. The needed uniform next obstruction remains unproved; group-decision scope and counts are unchanged. See `research/notes/N8-general-first-kernel.md`.


N8 follow-up in the same work period: the uniform next obstruction is now proved using cyclic rotation of associative words and the fact that non-linear Lie polynomials have zero cyclic coefficient sums. The proposed integral branch algorithm is written, but group implementation and scope checks are pending; no candidate scope/count has yet been enlarged. Section6 of the same note supersedes its earlier open-obstacle discussion.


N8 general type-one extension: the candidate now decides every third-from-last target whose complete integral leading-pair list has only type(1,c-3), in every finite rank and class c>=6. Nonzero metabelian image of its leading term is sufficient. A coefficient/support lemma bounds the first kernel by one; a cyclic-word argument forces a nonzero final quadratic obstruction. Seven independent GAP witnesses,27 linear decisions and5 quadratic certificates passed, with negative and unsupported controls. The initial class12 timeout is preserved. See `problems/N8/type1-third-proof.md` and `type1-third-audit.md`. This broadens the same partial candidate; counts remain6 whole,3 partial,0 established novel.


N8 combined type-one/two extension: the third-from-last algorithm now admits every target whose complete integral leading list has first weight at most2, in every finite rank and class c>=8. GAP independently passed10 witnesses,40 linear decisions and8 quadratic certificates, including the exceptional type(2,7) class11 branch. See `problems/N8/type12-third-proof.md` and its audit. The support lemma is now explicitly credited as a consequence of Remeslennikov--Stohr2007 via Lazard elimination; the elementary alternative proof is retained. This remains one partial N8 candidate; counts6 whole,3 partial,0 established novel.


GA5(c) now has a checked prior existential positive answer in rank two from
Nekrashevych Section1.10.4; the classification in (a) stays separate. The
G7 metric-profile citation does not supply an accepted convergence proof:
its numerical implication fails for a monotone submultiplicative sequence,
which is not a group counterexample. The E6 strong-conciseness theorem
also has different scope. See the three dated research notes; no counts change.


N8 uniform third-layer extension: every normalized leading type is now
covered in arbitrary class c>=6 and finite rank. A graded-tail free Lie
subalgebra permits the prior inner-solution theorem; the remaining branches
have either a nonzero quadratic obstruction, an injective first correction,
or finitely many exact Nielsen residues. GAP checked19 group witnesses,
101 integer decisions and11 Nielsen periods; separate weighted Lie checks
include decomposable coefficients. Two wrong negative fixture expectations
were preserved and corrected by explicit verified witnesses. See
`problems/N8/third-layer-proof.md` and `third-layer-audit.md`. This extends
the same partial candidate;6 whole,3 partial,0 established novel.


N8(b) fourth-from-last extension, 29 September06:13UTC: the uniform proof
now retains all final correction coordinates in one integral system.
An explicit class-eleven control shows that retaining a single quotient
witness would miss a solution. The final three suites cover41 targets;
GAP independently checks18 witnesses,148 integer decisions(72 negative),
18 polynomials(6 empty),90 samples,56 nullities and20 Nielsen periods.
Three rank-three180second timeouts are retained; the same suite completed
in200.331seconds with a longer allowance and passed GAP in42.813seconds.
See `problems/N8/fourth-layer-proof.md` and `fourth-layer-audit.md`.
This promotes gamma_(c-3), c>=7, within the same partial candidate.
Further general-offset lemmas have bounded independent checks but no
fifth/sixth-layer group solver is claimed. Counts remain6 whole,3 partial,
0 established novel; specialist review and the original deadline remain.


F38(c) research-tool update: a complete finite search for a common subgroup
in which both conjugacy classes are filling now supplies another prior
positive branch. It recognizes proper-free-factor and non-free-factor
cyclic-HNN vertex examples. GAP checks29 quotient graphs,7 positive carrier
identities and the supporting orbit certificates. The integrated classifier
retains negative witnesses and an explicit unresolved outcome; Lee's known
rank-two positive pair correctly survives as unresolved by this sufficient
test. See `research/notes/F38-common-filling-carrier.md`. This is prior
mathematical scope made effective, with no candidate or novelty count added.


N8 fifth/sixth-layer checkpoint, 2026-09-29T07:03:56.815798+00:00: the proposed complete coupled
lifting scheme is now implemented and independently replayed.82 final records
include44 positive,32 negative and6 unsupported controls. All ten final
mathematical jobs pass; the class-twelve GAP replay took380.732seconds.
One rank-three fixture-coverage assertion failure is retained with all inputs;
a new metabelian-image negative control completes that suite. The scope is
gamma_(c-5), c>=9, within the same partial candidate. Counts remain6 whole,
3 partial,0 established novel. O6 literature check confirms a prior reduction
to primitive extension groups, with the remaining hypothesis unresolved.


F41 follow-up: the parameter-free genericity step and dependence of
constants on the fixed word were re-audited without finding a gap. The
imported theorems still require specialist review; see
`problems/F41/followup-audit.md`.

MA7: the short website question has a prior affirmative existence answer. An additional
explicit finite noncommutative-ring construction is now written and
independently checked:343 elementary factors, a rank38 obstruction and a
unit off-diagonal entry. It satisfies the stronger nonscalar condition
for fixed n=3, but supplies no commutative-ring result or established
novelty. See `problems/MA7/exterior-ring-proof.md` and its audit. No entry
is added to the candidate tally. O6's pending visual statement check is
also complete after restoring the existing browser-library path.


## 2026-09-29T11:00:34.010172+00:00 — F38 whole-entry candidate

The new full part (c) proof upgrades F38 from partial to whole-entry
candidate. One-sided linear comparison is equivalent to a finite
conjugacy-stabilizer orbit; two-sided comparison is equivalent to
commensurable stabilizers. The proof imports Sela's graded shortening,
while the terminating decision uses the existing Whitehead/mod-three
procedure. Independent GAP reconstructs all 12 tested minimum graphs
and 20948 edges. See `problems/F38/bounded-proof.md` and `bounded-audit.md`.
Earlier unresolved F38(c) entries above are historical. Counts now
7 whole, 3 partial, 0 established novel; specialist and novelty review pending.


## 2026-09-29T11:26:00.871224+00:00 — N3 restricted repair, no new count

The nested cover construction now has a complete written restricted
argument and independent finite checks. It covers countable ascending
unions of nilpotent subgroups, including the already known countable
case (Romanovskii1969). Arbitrary locally nilpotent groups remain
unresolved here. GAP checks13 stages and an order-four negative control.
See `research/notes/N3-nested-cover.md`; counts remain7 whole,3 partial,
0 established novel. The original deadline remains unchanged.


## M4 and N6 scope controls (2026-09-29T11:39:51.555754+00:00)

M4 now has an explicit retraction with diagonal abelianization for which
closing any nontrivial image under coordinate supports forces an infinite
chain. Its image is free metabelian, so this obstructs a proposed reduction
and does not answer M4. One GAP job passed in1.925seconds at1core/4GB,
with empty stderr; its finite boundary and symbolic infinite proof are
clearly separated in `research/notes/M4-support-chain.md`.

N6: Segal's May2026 primary preprint decides profinite comparison but
explicitly does not supply genus cardinality computation. Introduction
and beginning of Section2 read; actual PDF p2 and frozen N6 rendering
viewed. `research/notes/N6-profinite-comparison-scope.md` records the
remaining classification gap and the website's unstated comparison class.

Neither adds a candidate:7 whole,3 partial,0 established novel. No active
jobs, subagents, pushes, contacts or imported Kourovka mathematics.
The parent/preparation repositories and original deadline are unchanged.


## F34 coverage reconciliation (2026-09-29T11:42:39.555127+00:00)

F34 is reclassified as whole-entry candidate coverage: candidate(a) plus
prior(b), using the same convention as F38. This is a bookkeeping
correction and adds no mathematical result or solved subpart. Current
tally8 whole/2 partial/0 established novel still concerns the same ten
entries. The known stability implication is explicitly recovered from
the existing graph lemma; the 2025 primary paper's precise use of it
was read and actual PDFp20 viewed. The original2005 paper remains
unavailable. See `research/notes/F34-coverage-reconciliation.md`. No
mathematical reruns; old proof/audit/manifests retained.


## Portfolio and F38 source recheck (2026-09-29T11:47:55.442832+00:00)

The wider scan produced no further candidate: B11 still has a prior
Shoemaker announcement without a full proof located; B8/B13 are already
prior; B9 still needs fixed-strand exhaustion; H15/AUX4/F39 retain their
recorded gaps. A targeted reread of the F38 graded-shortening definitions
and local lemma found no new gap in the selected shortness/free-factor/
limit-kernel checks, with specialist review still required. No tests were
rerun. See `research/notes/portfolio-29sep-late-morning.md`.

Counts remain8 whole-entry coverage candidates,2 partial entries,0
established novel. The F34 change was accounting only. All jobs terminal;
no subagents, pushes or contacts. Original deadline unchanged.


## N8 universal exact substitutions (2026-09-29T12:13:43.448957+00:00)

The candidate now covers all leading degrees <=7 in arbitrary class and,
with the existing deepest-six-layer theorem, all targets in classes <=13.
The key new step integrates later correction kernels as universal group
word substitutions preserving the commutator exactly, so no ambient free-
generator hypothesis is needed. A complete finite fiber quotient handles
separated exceptional offsets, including the boundary t'=2t.

Independent GAP replay passes22 universal maps,88 inverse equalities and
6 wrong-Nielsen controls in six weighted groups. Another32 substitutions
on8 pairs with decomposable heavier leading coefficients pass128 inverse
equalities. The first GAP generator-list error and all41 rejected fractional
powers are retained. The full new branch algorithm is a candidate proof,
not an end-to-end implementation; overlapping exceptional offsets remain
unresolved. See `problems/N8/universal-gauge-proof.md` and its audit.

Kuno's primary symplectic-expansion source and its Massuyeau credit are
recorded; this classical ingredient is not claimed as new. All jobs are
terminal, all evidence is local, and no subagents/pushes/contacts occurred.
Counts remain8 whole-entry coverage candidates,2 partial,0 established novel.
The original deadline remains30September10:04:49UTC.


## N8 exceptional weight boundary (2026-09-29T12:29:35.464647+00:00)

A nonzero pre-Nielsen kernel now has the proved bound t<=q-3p. The
separation criterion therefore covers every leading gap<=6, giving all
leading degrees<=8 in arbitrary class and all targets in classes<=14.
All later exceptional directions lie in the first direction's two-generator
Lie algebra, but explicit offsets3,5 show that overlap is real. Python/FLINT
and independent GAP verify19 complete kernel dimensions and5 identities
in0.120 and1.975seconds, respectively, with empty stderr. No failed run.

Proof/audit: `problems/N8/exceptional-boundary-proof.md`. This is a scope
refinement of the existing partial candidate; full end-to-end group branch
implementation, specialist review and novelty remain outstanding. A new
univariate parametric lattice route is saved in
`research/notes/N8-parametric-tail-lead.md`; it is not yet implemented,
audited or counted. Broader portfolio searches are recorded separately
in `research/notes/portfolio-29sep-noon.md` and added no candidate.

All jobs terminal;8 whole/2 partial/0 established novel; no subagents,
pushes, contacts or imported Kourovka arguments. Original clock unchanged.


## N8 one-parameter arithmetic component (2026-09-29T12:46:29.054516+00:00)

A complete integer-parameter linear solver now has a written elementary
proof and independent GAP replay. This is prior arithmetic, explicitly
credited to Schuster2007 and Bozga–Iosif–Lakhnech2009. The successful
suites cover24 complete systems,268 finite decisions,352 residue decisions,
2040 fixed specializations and19 final witnesses. Three implementation/
representation failures and their sources/logs are retained; both successful
runs have empty stderr. All jobs and handles are terminal.

See `problems/N8/parametric-integer-proof.md` and its audit. The proposed
reduction of actual group corrections to this arithmetic remains unverified,
so N8 scope and counts stay unchanged:8 whole/2 partial/0 established novel.
The preceding preparation-only check advanced no solving; the recorded run
has now resumed under its original30September10:04:49UTC deadline. No
subagents, pushes, contacts, or changes to parent/preparation repositories.


## N8 parametric tail construction (2026-09-29T13:19:35.161426+00:00)

The proposed overlapping-kernel extension now has a detailed group-coordinate
proof. Class15 independent GAP replay verifies52 polynomial columns,8 joint
controls,3 full kernels, the complete integral successor line and both group
witnesses; a separate verifier checks positive and negative parameter sets.
Class18 construction and complete arithmetic replay pass, with50 tail
coordinates and63 polynomial equations. Its full GAP group replay remains
live (`n8-parametric-tail-gap-c18-v1`), so uniform scope is not promoted yet.

A real class19 mixed term is nonzero, with54 coefficients independently
checked in GAP: the raw linear-tail argument stops strictly at c-d<=9.
The integer solver now uses exact component Hermite reduction after a larger
Smith calculation stalled; all24 arithmetic systems and independent replay
pass again. One timeout and two intentional diagnostic/fixture-selection
interruptions are retained, with saved polynomial input reused explicitly.
See `problems/N8/parametric-tail-audit.md` for boundaries and executed versions.

Counts8 whole/2 partial/0 established novel and original deadline unchanged.
At most2 cores/16GB reserved; no subagents, pushes, contacts, or parent/prep
changes. The only remaining live job is the named class18 group replay.


## N8 overlapping-tail audit completed (2026-09-29T13:53:00.374793+00:00)

Independent class 18 GAP group replay passes in 427.270968 seconds: 250
polynomial columns, 10 joint controls, 2 direct identity controls, 3 complete
kernels,1 full integral successor line and 2 group witnesses. Class15
passes the same final checker in 3.827367 seconds, with 52 columns, 8 joint
controls, 4 negative-target comparisons and 10 direct identity controls.
Complete arithmetic replays and the strict class 19 mixed-term control were
already successful. The candidate scope is now all ten final layers and
all targets through class 18, using the previous leading-degree<=8 theorem.

Compact NQ input and exact group commutator identities remove expensive
expanded-word conversion and repeated full corrections. Five unsuccessful
class 18 group runs and their executed sources remain recorded. All current
runs have terminated; successful final stderr files are empty. The general
ambient branch algorithm is not implemented end to end and still needs
specialist review. No claim of established novelty.

A separate two-parameter transmission lead remains uncounted. Independent
Lie checks confirm its proposed proportional obstructions, but also show
that the suggested perturbation fixes the first parameter too early. That
failed example is preserved. A bounded wider portfolio pass added no
candidate; see `research/notes/portfolio-29sep-early-afternoon.md`.

Counts remain 8 whole-entry coverage candidates, 2 partial, 0 established
novel. At most 3 cores / 24 GB reserved during this follow-up; no subagents,
pushes, contacts, or parent/preparation-repository changes. Original
30 September 10:04:49 UTC deadline unchanged.


## N8 two-exception branch extension (2026-09-29T14:22:20.018109+00:00)

A complete candidate argument now handles at most two remaining exceptional
offsets. It retains the full integer block quotient, reduces the first
quadratic to finitely many parameters or one polynomial family, then uses
every residue of later exact substitutions. This covers leading gaps <=8,
leading degrees <=10 in arbitrary class, and all targets through class 20
with the preceding ten-final-layer result. General N8 remains unresolved.

Independent GAP checks 11 complete polynomial systems, 67 complete fiber
sections, 413 residue decisions and 671 specializations. Two actual weighted
group fixtures check 33 block columns, 30 terminal columns, 12 quadratic
samples, 7 block kernels, both complete integer lattices and 4 witnesses.
The (4,6) fixture also verifies the Nielsen period and all three residues.
Three representation failures are retained. Full ambient branch enumeration
is not implemented; the general proof and novelty still need specialist
review. See `problems/N8/two-exception-proof.md` and its audit.

A fresh F5 primary-source check separates Humphries's rank-three result
from an isolated general-n introductory sentence; property (T) blocks the
same induced-character route in rank four, without proving full rigidity.
Other bounded portfolio queries produced no new candidate. A possible N8
fourteen-final-layer/class24 route is saved separately, explicitly unverified
and uncounted; it needs an actual three-exception group audit.

Counts remain 8 whole-entry coverage candidates, 2 partial, 0 established
novel results. All jobs terminal; at most 4 cores / 32 GB reserved. No
subagents, pushes, contacts or parent/preparation changes. Original deadline
30 September 10:04:49 UTC unchanged.


## N8 three-exception and nonlinear-tail checkpoint (2026-09-29T15:04:04.817848+00:00)

The new fourteen-final-layer/class24 proof is written but remains uncounted
pending its upper-bound group audit. The candidate scope stays class20
and leading degree10 in arbitrary class. All eight Lie kernels through
the first three exceptions are independently checked, including an extra
ambient generator. The class21 polynomial group family passes independent
GAP replay:744 columns,16 joint controls,3 complete kernels,1 complete
integer fiber and2 group witnesses. Class25 has a genuine mixed boundary
term; its115 leading coefficients are independently checked.

Five unsuccessful/incomplete runs and their executed sources are retained.
They include two constructor timeouts, one intentional collection-bottleneck
interruption, an NQ integer limit, and a verifier's group-word nesting error.
The class24 constructor v3 is running with a1200-second cap; it uses cached
linear collection and FLINT rank and saves the polynomial system before
arithmetic. A native class24 quotient preflight is also pending. See
`problems/N8/fourteen-layer-audit.md` for completed evidence and limits.

A new compatible-deformation Lie probe clears the earlier successor
obstruction, but its quadratic and later linear obstructions are independent.
It therefore still fails as an unbounded absorbed-parameter branch; see
`research/notes/N8-compatible-deformation-probe.md`. An M0 internal recheck
makes the right/left Fox-Jacobian conversion explicit without finding a
new gap or changing scope; `research/notes/M0-29sep-convention-recheck.md`.

Counts8 whole/2 partial/0 established novel; at most2 cores/16GB reserved.
No subagents, pushes, contacts, parent or preparation-repository changes.
The original30 September10:04:49UTC deadline is unchanged.


## N8 fourteen-final-layer audit completed (2026-09-29T15:24:41.390301+00:00)

The candidate partial scope now covers c-d<=13 and, with the previous
leading-degree-ten theorem, all targets through class24. General N8 is
unresolved. The class24 constructor passes in534.781437 seconds; its
independent native GAP replay passes in169.786400 seconds, checking2457
polynomial columns,18 joint controls,3 complete homogeneous kernels,
one complete integer fiber of dimension3 and2 actual group witnesses.
The separate quotient preflight confirms Hirsch length389 and no torsion.
Together with class21 and the strict class25 boundary, the audit retains
16 terminal runs:10 successful and6 failed or intentionally interrupted.
The largest new certificate is40,136,372 bytes, below the90,000,000 limit.
See problems/N8/fourteen-layer-audit.md for exact evidence and limits.

The actual polynomial examples are not surviving unbounded absorbed
branches. The general proof keeps those branches, all integer residues
and all later kernels; its structural dependencies need specialist review.
The all-rank branch algorithm is not implemented end to end. Counts remain
8 whole-entry candidates,2 partial candidates,0 established novel results.

A separate hyperelliptic arithmetic route is saved as an unverified,
uncounted lead. Berczes--Evertse--Gyory2013 Theorem2.2 provides a prior
effective bound; only the introduction/notation/statements through page4
were read, and actual page4 viewed, not the full proof. The group-family
reduction and low-degree arithmetic cases still need a full argument.
All jobs terminal; at most2 cores/16GB reserved in this work period. No
pushes, contacts, subagents or parent/preparation changes. Original
30 September10:04:49UTC deadline unchanged.


## N8 constrained-curve arithmetic checkpoint (2026-09-29T15:41:40.504278+00:00)

A complete arithmetic lemma now reduces a quadratic with fixed nonzero
leading coefficient to a square-root curve, retaining all extra polynomial
conditions and fixed-modulus congruences. The degree>=3 stopping bound
is imported from Berczes--Evertse--Gyory2013; its enormous enumeration
is not implemented. Low-degree cases have explicit finite/periodic
arguments. See research/notes/N8-constrained-curve-lemma.md and its audit.

The finite audit independently agrees on244 complete Pell decisions
(49 positive,195 negative),706 complete seeds,463 residue states,
11 polynomial records,1137 congruence controls and7 conic-intersection
cases with10 points. A real curve point rejects the tempting incorrect
congruence modulus. A GAP polynomial-matrix determinant representation
failure and its exact source are retained; the final exact Sylvester
replay passes. All5 runs are terminal,4 successful and1 failed.

The group reduction in research/notes/N8-three-exception-curve-reduction.md
is an unadopted draft. Its early-truncation argument explicitly requires
affine dependence of the initial constraints on the second parameter.
No arbitrary-class three-exception, leading-degree12 or class26 extension
is counted. Current N8 scope remains c-d<=13/all targets through class24,
with the previous arbitrary-class families. Counts8 whole/2 partial/
0 established novel unchanged. One core/4GB reserved for this arithmetic
work; no push/contact/subagent/parent changes. Original deadline unchanged.


## Three-exception group evidence, still unadopted (2026-09-29T16:17:00.171390+00:00)

Two weighted actual-group blocks and four exact formal universal substitutions
pass independent native GAP replay. Complete integer fibers and arithmetic
replays pass as well. The25 retained runs comprise10 successful and15 failed,
interrupted or configuration-rejected runs; details and limitations are in
research/notes/N8-three-exception-audit-interim.md. Native Hall multiplication
polynomials resolved large-exponent collection costs without changing equations.

The class26 delayed-quadratic constructor and native quotient preflight remain
live; the constructor has reached a330x273 block with integer kernel rank4.
No class26 or general three-exception extension adopted. Current counts remain
8 whole-entry candidates,2 partial candidates,0 established novel results.
A focused F38 shortening-source recheck found no new gap; structural dependencies
and novelty still need specialist review. Original deadline unchanged.


## Class26 arithmetic optimization and source review (2026-09-29T16:29:27.154798+00:00)

The constant-matrix optimization passes all5 regression runs, including
independent GAP replay of24 integer systems and11 complete polynomial-family
systems. Two earlier class26 jobs timed out, one in generic Smith arithmetic
and one after constructing the quotient while building multiplication
polynomials. Both failures and exact sources are retained. Two revised jobs
are live; scope is unchanged. See research/notes/N8-constant-diagonal-audit.md.

The three-exception draft now makes the full integer quotient and rank-one
Bezout reduction explicit. GA3's general-Lambda collapse and boundary-source
application were reread; no new gap found in that focused check. Details in
research/notes/GA3-29sep-collapse-recheck.md. Neither review is specialist
validation. Counts8 whole/2 partial/0 established novel and deadline unchanged.


## Delayed quadratic and restricted separation lemma (2026-09-29T16:47:10.412636+00:00)

The class26 constructor passes with the full four-parameter integer block,
first quadratic and following universal layer. Independent complete-family
and arithmetic GAP replays pass. Python specializes the full universal period
lattice and retains all finite residues symbolically, including terminal
period479001600. Native group/period replays and multiplication-polynomial
construction remain live. One native period timeout is retained. Details:
research/notes/N8-delayed-quadratic-audit-interim.md. The class26/three-exception
scope remains unadopted; no count change.

A separate complete7-case Lie-space probe passes in GAP and independent
E-index tensors. Evaluation at(1,-2,1) gives a uniform proof of non-absorption
in that restricted compatible-deformation model. It is a supporting lead,
not a general group result: research/notes/N8-compatible-deformation-functional.md.
The original clock and8 whole/2 partial/0 established novel counts remain.


## N8 three-exception extension completed (2026-09-29T17:06:25.081284+00:00)

The candidate partial scope now includes branches with at most three remaining
exceptional offsets, leading gaps<=10 and leading degrees<=12 in arbitrary
class, and all targets through class26 when combined with c-d<=13. General
N8 remains unresolved. See problems/N8/three-exception-proof.md and its audit.
The proof retains all integer torsion cosets and fixed congruences, including
the rank-one delayed quadratic. Its effective curve bound is prior arithmetic.

The class26 native group replay passes in105.778seconds, reconstructing all60
possible quadratic coefficients,273 block columns,237 terminal columns, the
complete rank4 integer block lattice and2 group witnesses. Independent complete
integer-family and arithmetic replays pass. The final native period replay
passes in65.990seconds on16 exact specialized map cases, checking inverse
compositions, commutators and the complete integer period quotient. Elementary
maps reduce the block quotient order to16345929600; the terminal period is
479001600. Every residue is described; those huge sets were not enumerated.

The full audit retains50 terminal runs:27 successful,23 unsuccessful. Failures
and superseded sources remain available; none is silently recast as a pass.
The largest certificate is75046692bytes. A91776352-byte native GAP workspace
is an ignored local performance cache with documented hash/regeneration;
the constructor and native uncached group-verification path are included.
Recorded overlap peaked at7cores/48GB reserved memory. All jobs are terminal.

The group examples have finite first-parameter fibers; none is a surviving
unbounded absorbed-quadratic branch. The separate restricted Lie functional
lemma is a supporting lead, not a general non-absorption theorem. The all-rank
branch algorithm is not implemented end to end, and inherited structural
arguments and novelty still need specialist review. Counts remain8 whole-entry
candidates,2 partial candidates,0 established novel results. No push, contacts,
subagents or parent/preparation changes. Original deadline unchanged.


## Wider nilpotent portfolio checkpoint (2026-09-29T17:27:31.759755+00:00)

N9 has an elementary obstruction to a finite-automorphism-orbit shortcut:
one fixed product of two integral Heisenberg groups has infinitely many
automorphism orbits of cyclic retracts. Four actual retractions and three
nonlifting abelianization shears pass GAP. This is not a fixed-ambient
decision result; see research/notes/N9-cyclic-retract-orbits.md.

N3's new pair-bound-four probe finds torsion-free final layers of ranks177
and423 in classes7 and8. It does not test all source torsion or prove a
profile enlargement. The first collector-flag failure and both direct/fast
class8 records are retained. See N3-pair-four-central-probe.md. All jobs
are terminal; maximum reservation was one core/12GB.

Reread the current F28,N5,M0,F38(c),F41 candidate proofs; no new gap was
identified in this pass, which is internal review only. Targeted searches
on several wider entries returned previously distinguished partial scopes;
no additional full solution was inferred. Counts remain8 whole-entry
candidates,2 partial candidates,0 established novel results. No pushes,
contacts, subagents or parent/preparation changes. Original deadline unchanged.


F20 follow-up,29 September approximately19:00 UTC: direct equational proof
search also remains inconclusive. GAP independently verifies58 inputs and
two negative models, but all eight previously unresolved weight-seven
targets still lack proofs. The three successful E proofs give no new scope.
All failed searches are retained; see research/notes/F20-equational-probe.md.
F23's higher-rank chain and S4's derived-length-three prior result were
rechecked without closing their full questions. Counts remain9 whole-entry
candidates/1 partial/0 established novel; specialist review outstanding.


### 29 September, approximately 19:22 UTC: explicit-commutator search

The changed F20 encoding was semantically checked in GAP but proved no
additional target. Twelve jobs are terminal; the failed known control is
retained alongside the nine other E attempts. G11's horocyclic/coset scope
check likewise yields no new answer. The evening internal proof readthrough
found no new gap, with all imported-theorem and implementation limits retained.
Current tally remains nine whole-entry candidates, one partial candidate and
zero established novel results. No external review or publication occurred.


29 September evening source correction: AUX2 is prior positive by Hanna
Neumann. Wilton's TheoremD gives OR15 for infinite nonfree groups, with
the website's omitted free/finite conventions kept explicit. Recent small
undecidable presentations do not settle FP1 or A1. See
`research/notes/AUX2-OR15-FP1-scope.md`; no candidate-count change.


Checkpoint 2026-09-29T21:09:47.972454+00:00: B9's direct coloring-coset probe finds no new
coset in1891 states through depth12; independent GAP disproves a proposed
two-cone simplification. This is a failed strategy, not another result.
B12 now has credited prior coverage for5<=n<=12 from McMullen's lattice
representations plus Osin's filling theorem; n>=13 remains unresolved
here. See research/notes/B9-coloring-cosets.md and
research/notes/B12-lattice-quotients-prior-scope.md. Counts unchanged.


Checkpoint 2026-09-29T21:20:32.805009+00:00: F41 source-dependency audit added.
Perin--Pillay--Sklinos--Tent independently proves the subgroup theorem,
not the multipattern theorem needed here. Its orbit-nondefinability
result rules out a shortcut that our proof does not take. Primary text
and actual page7 checked; see problems/F41/dependency-boundary-audit.md.
No finite suite rerun, no imported deep proof independently established,
and no new candidate or novelty claim. Counts remain10 whole-entry
candidates/2 partial/0 established novel. All jobs terminal; no push.


Checkpoint 2026-09-29T21:31:55.952240+00:00: B9 positive parameters are now classified
completely, and each represented B3/B2 coset has a unique terminal special
pair under inverse sigma1 coloring. Any further four-strand example
needs a new terminal pair with both colors nontrivial and no positive
parameter representative. This does not bound all negative parameters.
See problems/B9/positive-parameter-reduction.md. A ten-state finite
automaton check and independent GAP reconstruction of all46 old endpoints
passed; no search bound increased. Counts unchanged:10 whole candidates,
2 partial,0 established novel. All jobs terminal; no push.


Checkpoint 2026-09-29T21:48:55.467438+00:00: B9 least remaining parameter exponent narrowed
by adjacent-strand and lower-parabolic restrictions. Underlying v in B2
yields only known parameters; higher-strand cancellation remains. The
268-case fixed-height probe finds no new coset; GAP independently checks
all filter and direct-support branches. A compact pair of distinct
special five-strand braids with a four-strand quotient disproves a
proposed rigidity extension. See problems/B9/exponent-two-parameter-reduction.md.
The first90-second timeout and GAP keyword failure are retained. All
jobs terminal; counts10 whole/2 partial/0 established novel unchanged.


Checkpoint 2026-09-29T22:03:20.231614+00:00: N9 candidate strengthened to isolated input
subgroups with primitive images in both lower-central layers. The full
integer-kernel saturation and fixed witnesses at0 and1 give the universal
proof; GAP checks its polynomial identity and seven actual toy inputs.
The first scalar/polynomial comparison failure is preserved; corrected
run passed with empty stderr. Full2017 free-case theorem/proof checked,
including introductory attribution against the prior uniform result.
See problems/N9/isolated-inputs-and-prior-scope.md. Tally unchanged:
10 whole-entry candidates,2 partial,0 established novel. All jobs terminal;
no push, external contact, subagent or parent/preparation change.


Checkpoint 2026-09-29T22:16:48.422383+00:00: B9 has an all-parameter obstruction to one
proposed way of using the infinite B5 family to obtain another B4 braid.
It excludes all n>=3 through the ten known smaller inputs; a separate
recurrence-tail attempt gives only an existing braid. Python and GAP
symbolic checks pass, with the failed first bound and unavailable inverse
method retained. See research/notes/B9-family-return-obstruction.md.
This prunes two routes but does not exhaust B4. Tally10whole/2partial/
0established-novel unchanged; all jobs terminal, no push.


## Current review guide (2026-09-29T22:28:26.470635+00:00)

[CURRENT_RESULTS.md](CURRENT_RESULTS.md) now identifies the controlling
proofs, prior coverage and verification limits for all12 candidates. Older
class-specific N8 scopes and intermediate counts are historical. A further
[F38 source check](../research/notes/F38-rigid-solid-source-check.md) found
no new gap in the canonical quotient/maximality step; specialist review of
the imported shortening argument remains outstanding. Counts10whole/
2partial/0established-novel are unchanged.


## Limited N8 formalization (2026-09-29T22:35:08.048427+00:00)

[N8's new audit](../problems/N8/averaging-lean-audit.md) records successful
Lean verification of two universal analytic ingredients: stochastic contraction
and the compact harmonic maximum principle. The transfer construction and
polynomial/Lie bridge remain written proofs, as does the full general algorithm.
One initial proof-script failure is retained. Tally unchanged at10whole/
2partial/0established-novel; no additional novelty claim.


## F39 injection shortcut ruled out more strongly (2026-09-29T22:48:31.363014+00:00)

An [explicit all-rank construction](../research/notes/F39-unimodular-obstruction.md)
shows that neither determinant one nor automorphisms on every free nilpotent
quotient can replace an ambient automorphism in the proposed F39 reduction.
Its image avoids primitive elements, and a variant avoids all short automorphic
orbits using the prior F40 theorem. Exact GAP word/nilpotent controls and a
finite A5 separator pass; one initial script failure is preserved. This is an
uncounted obstruction, not a new F39 algorithm. Tally10whole/2partial/0novel.


### N8 positional bridge, 2026-09-29T23:03:54.295384+00:00

A [new limited formalization](../problems/N8/polynomial-bridge-lean-audit.md)
proves the positional averaging derivation without division or a separate
zero-sum extension argument. It also checks cyclic invariance and the
concrete half-transfer sum/l1 properties in all finite dimensions. Twenty
Lean declarations pass; two failed intermediate sources remain alongside
two successful runs. This strengthens the same general N8 candidate;
the full Lie/group algorithm and the formal assembly of the analytic
steps remain outside the check. Counts and review status are unchanged.


### N8 full-block implication, 2026-09-29T23:18:16.096994+00:00

A [new audit](../problems/N8/block-separation-lean-audit.md) records six
universal Lean lemmas for triangular compatibility, annihilation of all
later columns, exclusion of the first quadratic from their full span,
and at most two liftable first-parameter values. Linear-operator
coefficients retain the polynomial multipliers required in the proof.
The group/Lie realization and complete algorithm are still written
arguments. One failed and one successful run are retained; no tally
or deadline change and no independent specialist review is implied.


## F20 finite-image checkpoint (2026-09-29T23:31:56.543036+00:00)

[F20 finite-image probe](../research/notes/F20-finite-images.md): complete pair tests in S6,S7 and five PSL2 groups find no counterexample. Python and GAP agree. This remains inconclusive for F20; ten whole/two partial/zero established novel unchanged.


## N8 concrete transfer sequence (2026-09-29T23:43:16.841041+00:00)

[N8 concrete transfer convergence](../problems/N8/sweep-convergence-lean-audit.md) now has an explicit simpler proof and nineteen accepted universal Lean declarations. It supplies the actual finite reachable sequence needed by the averaging argument, including norm/sum preservation. Full N8 formalization and specialist review remain outstanding. Ten whole/two partial/zero established novel unchanged.


## M0 constructive dependency check (2026-09-29T23:56:51.515894+00:00)

[M0 constructive Jacobian audit](../problems/M0/flow-inverse-audit.md) now supplies the exact source-convention conversion and an explicit integral-flow construction of inverse words. Independent GAP replay checks the finite certificates and a free/metabelian boundary example. The criterion remains credited prior work; no new result count. Tally10whole/2partial/0established-novel unchanged.


## F37 finite-quotient obstruction (2026-09-30T00:10:45.994599+00:00)

[F37 approach obstruction](../research/notes/F37-finite-quotient-obstruction.md): Nikolov--Segal's prescribed-generator commutator theorem implies a uniform bound on primitive-image length in every marked finite quotient. The prior unbounded-width theorem supplies words outside any fixed primitive-length ball. Thus sufficiently large balls are proper and profinitely dense; quotient exclusion cannot decide all negative instances. This does not answer F37 or change the10whole/2partial/0established-novel tally.


## Shared F34/F38 span formalization (2026-09-30T00:18:59.128695+00:00)

[Shared span audit](../problems/F38/shared-span-lean-audit.md): fifteen universal Lean declarations verify the linear reachability/span step used by F34(a) and F38(a), including finite-dimensional termination and genuine path witnesses. Concrete polynomial lifting and the imported equation-to-EDT0L theorem remain outside the formal check. One failed source retained, final run passes in7.79s. No tally change.


## N8 energy simplification (2026-09-30T00:29:20.373867+00:00)

[N8 energy proof](../problems/N8/energy-maximum-audit.md) replaces the analytic convergence construction with a shorter maximum-set/minimum-squared-norm argument. Ten Lean declarations verify the concrete half-transfer theorem in every finite dimension, with no convergence hypothesis. Connection to the positional bridge remains written; the full N8 algorithm is not formalized. Count10whole/2partial/0established-novel unchanged.


## N8 positional constancy assembled (2026-09-30T00:41:25.505810+00:00)

[N8 analytic assembly](../problems/N8/analytic-assembly-audit.md) now formally derives constancy from the original delta/diagonal functional identities and continuity. The cyclic-coordinate and energy connections are included, with no convergence assumption. Fifteen new Lean declarations plus30 unchanged prerequisites pass. Free-associative/Lie identification and the full decision algorithm remain outside. Tally10whole/2partial/0established-novel unchanged.


## GA3 separator simplification (2026-09-30T00:53:15.520379+00:00)

[Elementary separator](../problems/GA3/elementary-separator-supplement.md): a finite choice among2|C|+1 endpoints and two conjugations now gives the required simultaneous separator directly. Axis translations prove its uniform boundary dynamics. This removes the imported endpoint-density theorem from that step, while preserving the general collapse dependency and all review qualifications. No new computation or tally change: ten whole/two partial/zero established novel.


## N5 rational Lie implementation (2026-09-30T01:08:28.110142+00:00)

[New audit](../problems/N5/rational-lie-audit.md): the established rational Lie decomposition stage now has a general exact implementation, with a finite centroid-character separation bound and rational CRT projections. Python and native GAP check19 fixtures/34 factors, including quadratic fields, repeated factors, dual numbers and rational basis changes. Three retained GAP factor-normalization comparison failures preceded the final pass. The whole arbitrary-input group pipeline remains incomplete. Tally10whole/2partial/0established-novel unchanged.


## N5 rational-to-integral pipeline (2026-09-30T01:19:40.454298+00:00)

[Connected class-two implementation](../problems/N5/class2-pipeline-audit.md) now decides/constructs decompositions from exact torsion-free full-center commutator data. Fifteen fixtures include separate quotient-lattice and central-lattice gluing obstructions despite rational decomposability. Native GAP checks all33 recorded branches and6 positive decompositions. General torsion/presentation conversion remains unimplemented; this is prior torsion-free scope and adds no candidate. Counts10whole/2partial/0established-novel unchanged.


## N5 class-two torsion pipeline (2026-09-30T01:34:11.633346+00:00)

[Mixed class-two implementation](../problems/N5/class2-mixed-audit.md) joins rational support with all finite quotient splittings, central power defects and the existing mixed-center solver. Twenty fixtures pass; native GAP checks480 arithmetic equalities,102 defects,96 cross obstructions and9 actual decompositions, with separate finite-group decisions and negative quotient-coverage checks. The general mixed-center negative solver is not independently rerun in GAP; infinite negative examples retain written proofs. No new count or novelty claim.


## N5 finite-presentation interface (2026-09-30T01:51:53.957366+00:00)

[Finite-presentation interface](../problems/N5/class2-input-audit.md): class-two input conversion, exact coordinate maps and recovery of original factor words now connect to the mixed solver. Twenty-seven presentations pass810 arithmetic identities/251 relators, with12 native direct decompositions. Three standalone commands pass. Higher-class input remains unimplemented, and the fp class-two promise is not recognized. Counts unchanged.


## Closing audit checkpoint (2026-09-30T01:58:43.186500+00:00)

Closing audit started with5708 historical hash bindings:5676 current matches and32 bindings to25 old versions, all recovered exactly from Git. No missing files after correcting the scanner's project-relative/ignored-binary resolution. Four launch-input hashes match; all historical process receipts and log hashes reconcile, with the audit's own terminal record checked afterward. See artifact-checkpoint-2026-09-30.md and CLOSING_AUDIT_PLAN.md. Full principal N5 proof and integrality audit reread; no new gap identified, imported machinery and higher-class implementation limits retained.


## Closing F34/F38/F41 audit (2026-09-30T02:11:44.213008+00:00)

[Shared decisions and shortening](../research/audits/F34-F38-closing-proof-reread.md) and [F41 piece-cover growth](../research/audits/F41-closing-proof-reread.md): exact imported theorem interfaces, quantifiers and proof boundaries reread. No new gap identified; equation-language implementation, deep shortening/model theory and outside specialist review remain outstanding. Counts remain ten whole-entry coverage candidates, two partial entries, zero established novel results.


## N8 closing audit and rational polynomial interface (2026-09-30T02:22:43.998491+00:00)

[Closing reread](../research/audits/N8-closing-proof-reread.md) checks leading-factor completeness, actual free-basis hypotheses, reversible integral periods and the full later-column obstruction. [New Lean interface](../problems/N8/positional-polynomial-audit.md) gives rational coefficient constancy from polynomial identities and explicit diagonal substitution, for every finite dimension. Thirteen new declarations plus45 unchanged prerequisites pass; two failed inputs and all logs retained. Free-associative/Lie/group connections and the full algorithm remain outside. Counts10whole/2partial/0established-novel unchanged.


## Closing GA3/N9 proof audit (2026-09-30T02:36:41.567988+00:00)

General-Lambda collapse/separator and fixed-group DPRM/retraction/isolation implications reread with exact original statements and retained renderings. Guirardel general-Lambda remark and local proof checked in text and actual page images; DPRM parameter theorem checked in text. No new gap or novelty conclusion. Source-reading limits explicit,19 file bindings retained, no new mathematical job. Counts10whole/2partial/0established-novel unchanged. See research/audits/GA3-closing-proof-reread.md and N9-closing-proof-reread.md.


## Interim scope reconciliation (2026-09-30T02:38:16.544125+00:00)

All195 catalogue IDs retained in reports/result-scope-ledger.json with exact source references/current triage. Ten whole-entry candidates comprise6 unpartitioned proposed answers plus5 proposed named parts, with4 prior named parts. Two other partial entries remain. Eleven proposed components are bookkeeping, not11established new theorems.183 other entries are not asserted open. Both1CPU/2GB administrative runs pass; v1 exact generator/output retained before replacing static count prose, v2 final dynamic version passes.65 input/artifact bindings verified, bothPIDs terminated, registry empty. New research/result-scopes.json controls reports/RESULT_SCOPE.md generation; no original catalogue or mathematical proof changed. No tally/deadline change or push.


## Closing F28/M0/H4 audit (2026-09-30T02:41:54.082614+00:00)

Reread full controlling proofs and relevant supplements: F28 arbitrary-subgroup/PSL-to-integral-sequence bridge, M0 true primitive-word finite-field detection and constructive classical Jacobian criterion, H4 all-output size bound with infinite-input torsion-class extension. Original pages/references/background and four statement images checked; GGR Lemma1 page517 and Batty/Papasoglu Theorem3.27 page29 actually viewed. No new gap identified.28 hash bindings retained; no new mathematical job or bibliography conclusion. All ten whole-entry candidates now have closing reread notes; partial boundaries and final closeout remain. No count/deadline change or push.


## Closing G9/B9 partial boundaries (2026-09-30T02:45:48.945338+00:00)

Full flow-growth/solvable-extension and infinite-braid-family/small-strand/parameter-reduction arguments reread. Original source pages and actual statement renderings checked; Guba Lemma3 page5 and Dehornoy page26 viewed, specified local proofs read. No new gap identified. Exact G9 constant and B4 exponent-two exhaustion remain unresolved.20bindings retained, no new mathematical computation. A read-only wrong-case path probbr.html was absent; actual probBr.html then read in full. All twelve counted entries now have closing notes. No scope/count/deadline change, outside reviewer or push.


## Interim final-report draft (2026-09-30T02:49:42.021129+00:00)

reports/FINAL_REPORT_DRAFT.md now gives a self-contained current outcome, entry/subpart accounting, exact clock and provenance, verification boundaries, selected prior/uncounted work, retained failures and reproduction/resource limitations. Explicitly interim: no deadline snapshot, final process closure or goal completion claimed. All 22 local Markdown targets checked; original deadline remains10:04:49.670358UTC. Root/report/research-plan entry points link the closing work. No new mathematical job, count or novelty conclusion.

- 2026-09-30T08:29:05.423290+00:00: B9 family I1(beta_n) has no returning braid partner for any n>=3; fifth Burau first-column coordinate n(n-1) is invariant under every shifted partner. Separate GAP polynomial replay passes; interpreter and polynomial-zero control failures preserved. Counts unchanged.
