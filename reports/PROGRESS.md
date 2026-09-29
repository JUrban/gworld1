# GroupWorld progress

Active experiment: 28 September 2026 10:04:49 UTC to 30 September 2026 10:04:49 UTC.

Current counts: **3 partial candidates**, **7 whole-entry candidate solutions**, **0 established novel results**. All ten candidates await independent review; novelty remains provisional.

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
- N8(b) extension: all targets with nonzero degree-three leading term are now covered in arbitrary class, along with every equal-weight branch and the stated free-generator branches. A weighted free Lie algebra and denominator-clearing powers give finitely many integral pair orbits. GAP independently verifies46 subgroup automorphisms,2412 inverse-image equalities and92 commutator witnesses, and rejects a dependent-generator control. See `problems/N8/weighted-orbit-proof.md` and its audit. The full finite-union algorithm is proved, not implemented end to end; arbitrary-class N8(b) remains partial and novelty is unverified.
- N8(b): constructive candidate algorithms in all finite ranks for every target in classes three through ten, plus every target in gamma_(c-5) for arbitrary class c>=9 and the earlier arbitrary-class families. The new fifth/sixth-layer proof retains complete coupled integral point/line solutions and all remaining tail coordinates. Independent GAP replay checks44 witnesses,424 integer decisions,227 nullities,40 Nielsen periods,25 coupled systems and27 quadratics, including three parameter lines of step6. Proof and audit: `problems/N8/fifth-sixth-layer-proof.md`, `fifth-sixth-layer-audit.md`. This remains one partial candidate; arbitrary lower layers, specialist review and novelty remain outstanding. Earlier low-class/family proofs and all failed runs are retained.
- H4: candidate negative answer to polynomial-time conversion into an explicit Dehn presentation. Short presentations of finite metacyclic groups have doubly exponential order; a forbidden-factor automaton bounds the order of any finite group in terms of every Dehn presentation's size. Thus every explicit output is superpolynomial, even with changed generators. Proof: `problems/H4/proof.md`. GAP verified four finite models and independently computed three presentation orders. Related finite-group lower-bound ideas from2012 are credited; novelty and specialist review remain outstanding. Compressed output is a different specification. The strengthened bound in `problems/H4/infinite-input-proof.md` also covers infinite non-elementary virtually free inputs. GAP independently checked three conjugacy-class partitions and two free-kernel presentations (ranks6 and60); this remains the same candidate.
- F28: explicit negative answer using a rational matrix conjugation on an index-two subgroup of F2. The image also has index two, and the bounded-orbit argument excludes every nontrivial invariant subgroup. Candidate proof: `problems/F28/proof.md`. Exact matrix/word checks covered 13,120 words; GAP independently checked subgroup indices/ranks and defining identities. Related arithmetic constructions in the literature establish weaker normal-subgroup statements; a matching prior full answer has not yet been found.
- F34(a): candidate uniform decision algorithm for potential positivity in every finite rank. A positive image under an injection pulls back through a spanning-tree basis; a nonzero-determinant test on the full EDT0L solution relation decides existence. GAP independently verified270 explicit positive automorphism witnesses in ranks2--4 and3 scope controls. Rank2 and part(b) are prior; potentially new scope is rank>=3. Full recompression is imported, not implemented. Proof and audit: `problems/F34/part-a-proof.md`, `part-a-audit.md`.
- F38(a): candidate all-finite-rank decision procedure for translation equivalence, using a determinant product, a full EDT0L solution relation and finite rational span closure. Rank two is prior; potential novelty is ranks at least three. The final polynomial stage passed independent GAP replay on43 controlled systems,902 basis vectors and1151 transitions, with309 independent free-word checks. Full recompression is an imported theorem, not implemented. F38(c) remains unresolved here. Proof and audit: `problems/F38/part-a-proof.md`, `part-a-audit.md`.
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
- B9: exact enumeration gives 52 special braids through term height four in B5; finite matrices give a certified lower bound of 1930 in B6 at height five. GAP independently checks all witnesses and distinctness. The unrestricted counting problem remains unresolved; this is exploratory evidence, not another counted partial candidate. A failed 120-second Artin calculation is retained.
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

N9(a) follow-up: the fixed ambient group remains an essential gap.
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
