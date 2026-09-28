# Research log

Preparation, 28 September 2026: sources downloaded and indexed; site status markers and Hall of Fame cross-referenced; one external bibliographic status correction recorded; shared GAP installation and infrastructure checked. No targets selected, no mathematical searches or proof attempts performed. The 48-hour clock remains unstarted.

After explicit launch, append UTC time, problem/subpart, action, evidence, result, and next step. Record failed approaches and uncertainty as well as successful ones.

## 2026-09-28 10:04–10:10 UTC — launch and initial portfolio

User explicitly launched the 48-hour experiment. Deadline 2026-09-30 10:04:49 UTC, 20 CPU cores / 100 GB RAM. Preparation revision e1dc7b2; initialized clock committed as 90a2de7. A literal apostrophe-escape typo in the recorded launch quotation was corrected without altering either timestamp.

Read the full extracted text of the 146 entries without heading stars; identified convention traps (e.g. trivial solutions to the literal E4 wording) to avoid counting as intended new answers. Began primary-literature checks for free-group and self-similarity questions. A September 2026 preprint explicitly claims F15; F30 has a recent positive result. These are not our solutions. An early self-similarity preprint and later publication appear to differ, so version-sensitive checks are needed.

Developed a tentative exact answer to F42 using the rank of a folded core graph and finite coverings with all fundamental loops of length n. Saved the first argument before proceeding to verification and novelty research. No claims counted.

## 2026-09-28 10:22 UTC — first status checkpoint

Inspected original HTML renderings for F11 and F42. Both early arguments match already published/preprinted results and are excluded from novelty counts. Updated working triage (frozen source catalogue untouched). Located prior work on F15, F30, F31, F40 and a B11 announcement. Installed isolated Python/browser dependencies and locally extracted eight Ubuntu browser libraries; no root access used. Corrected a literal escape in the launch text only, without changing start/deadline.

## 2026-09-28 10:35 UTC — N8(b) class-three candidate

Derived a finite decision procedure in all finite ranks. For nonzero degree-two image, enumerate finite-index lattices in the support plane and solve integer central correction systems; commutator-preserving Nielsen moves prove completeness. For zero degree-two image, normalize one factor into gamma_2 and reconstruct the unique possible rank-one tensor using exact rational formulas. Wrote a self-contained candidate proof and prototype.

The Python recorded run passed 173 checks (fixed seed 9282608). The initial GAP run returned shell status zero but no marker: nq had aborted on rank one. This is retained as a failed run. Handling rank one directly as the infinite cyclic group and using --quitonbreak gave a successful rerun with 165 independently evaluated witnesses. Both successful runs used one CPU slot and 4 GB address-space limits.

Targeted literature searches found the known class-two theorem (Roman’kov 2016), the distinct general-equation undecidability results, and useful 1998 negative examples, but no class-three single-commutator decision result yet. Candidate novelty remains provisional.

Download caveats: the GA5 thesis returned HTTP 503; no PDF archived. A Roman’kov publisher request returned HTTP 202 with zero bytes, now explicitly marked unusable in its metadata. The downloader was tightened to require nonempty HTTP 200 responses. The 2021 Roman’kov survey and 1998 Akhavan-Malayeri–Rhemtulla PDF were archived successfully.

## 2026-09-28 10:49 UTC — class-four extension checked

Extended the N8(b) procedure to class four by splitting according to the first nonzero Lie layer. Nonzero degree two has unique degree-two factor corrections, followed by linear degree-four corrections. Nonzero degree three has only finitely many scaling choices. Pure degree four reduces to either an exterior decomposition in L2 or at most two rational linear factors of a quadratic, followed by integer linear algebra. The key natural map on L4 has a six-by-six multilinear minor with determinant -54; polarization extends injectivity to every rank. Full candidate proof written.

The class-four prototype passed 108 checks, fixed seed 9282604 (178.67 s on one CPU slot, 4 GB limit); GAP independently evaluated all 100 positive witnesses in 2.48 s. No test failure occurred. Classes three and four are one partial candidate, with bibliographic novelty still provisional. Targeted class-four literature searches did not locate a matching decision theorem.

A separate bounded probe found outer-slot injectivity in rank two for degrees three through seven; this is only a finite calculation and establishes no general higher-degree theorem. The degree-two map is zero, as expected.

Completed the textual pass through all 49 heading-star entries as well. Neither a star nor its absence substitutes for an exact subpart/background audit.

## 2026-09-28 10:54 UTC — broader follow-up portfolio

Archived and checked primary statements for prior resolutions of A3 and A5 (the latter a September 2026 preprint claim). Marked both outside the new-result count. Recorded unproved routes/gaps for N5, N9(a), B9, F28 and higher-class N8 in research/notes/portfolio-followups.md. No additional candidate claimed. The generated problem READMEs retain the preparation snapshot; the main README now explicitly points to the live triage and dated claims.

## 2026-09-28 11:08 UTC — F28 full candidate

Derived an explicit injective map on the Schreier basis of an index-two subgroup of F2. In its faithful PSL(2,Z) representation the map is conjugation by Q=[[0,-1],[2,1]]. The positive definite identity Q^t P Q=2P bounds every forward conjugation orbit over R. An orbit staying integral is finite, so its matrix commutes with some positive power of Q. No such power is scalar, and the determinant-one integral centralizer consists only of +/-I. This excludes every nontrivial forward-invariant subgroup, with no normality or finite-generation assumption.

Inspected the original HTML and screenshot. The first renderer refused to isolate this BR-led entry; added an explicit option capturing its complete containing paragraph, preserving the original bytes and including adjacent entries. Wrote `problems/F28/proof.md`. Exact Python checks passed for 13,120 reduced words of length at most eight; maximum observed domain survival was 14 steps. GAP independently confirmed domain/image index two and rank three, plus the matrix identities. Controls show that diagonal conjugation and finite-order elliptic conjugation do retain nontrivial invariant subgroups.

Initial targeted literature searches found closely related work by Nekrashevych–Sidki, Berlatto–Sidki and Kapovich, archived with metadata. Their inspected statements do not supply this stronger rank-two/index-two result. Novelty remains provisional. The run now has one whole-entry candidate (F28) and one partial candidate (N8(b), classes three and four), not established new theorems.

Also identified the explicit prior positive answer to F8 (Antolín–Jaikin-Zapirain 2022, Corollary 1.5). MA1 has a preprint-version trap: an elementary-generation assertion in Knudson v1 is absent from the v2 abstract, so no status resolution is inferred.

## 2026-09-28 approximately 11:18 UTC — higher-class N8 lead

A multilinear modular calculation found outer-map ranks 2/2, 6/6, 20/24, 115/120 and 700/720 in degrees three through seven. An exact rational calculation confirmed the degree-five kernel dimension four and produced an explicit nonzero witness. Thus the earlier rank-two observations do not generalize to full outer-slot injectivity. The completed class-four certificate remains valid.

Derived a weaker universal lemma: a nonzero bracket [z,Y] with z of degree one always has a nonzero outer quadratic, because otherwise Y is cyclically invariant, contradicting zero cyclic symmetrization of Lie brackets. Added this simpler argument to the class-four proof without changing the already checked implementation.

Two kernel calculations via the free metabelian Lie representation now suggest a full class-five extension. Their free parameters can be reduced to finitely many integral residues by exact commutator-preserving moves. Pure degree five also reduces to degree-one factors or a degree-(2,3) block-quadratic test. Saved the complete proposed case analysis and outstanding checks in `research/notes/N8-class5-lead.md`. **Class five is not yet counted.** No change to the candidate tally.

## 2026-09-28 11:36 UTC — N8(b) class-five extension checked

Completed a candidate proof in all finite ranks. A metabelian Lie representation identifies the two one-dimensional correction kernels; exact conjugation by the target and exact Nielsen moves reduce their integer parameters to finite residue sets. Pure degree five splits into bracket types (1,4) and (2,3), both decidable using finitely many rational linear factors of block quadratics and integer linear systems. The complete argument is in `problems/N8/class5-proof.md`.

The first prototype run reached case 62 and timed out at 300 seconds. A 110-second profile reproduced the expensive Smith decomposition on a tall redundant tensor system. Preserved both failed logs and the old implementation at `09a9c3a`. Selecting independent rows of the augmented equations preserves the complete integer solution set and reduced the unchanged 70-case suite to 10.25 seconds. GAP independently evaluated all 61 positive witnesses in 2.33 seconds. Separate tests checked 27 instances of the kernel lemmas in ranks two through four and four controls for equation compression, including rational-but-nonintegral and inconsistent systems. No mathematical test failure occurred.

Targeted literature checks again found class-two decision results, general-equation results and width computations, but no matching class-five algorithm. A Poroshenko algorithm found in the search concerns free metabelian Lie algebras over algebraically closed fields, so it is not the present integral group problem. Novelty remains provisional. The count is still one N8 partial candidate and one F28 whole-entry candidate, with no established novel results.

## 2026-09-28 approximately 11:49 UTC — new arbitrary-class N8 route and portfolio refresh

Drafted `problems/N8/independent-abelianization-proof.md`: fixed independent abelianization vectors give finitely many IA orbits of factor pairs, since each homogeneous correction map has finite integral cokernel. A constructive central-layer orbit algorithm uses integer images and explicit finite generating sets for kernels in the nilpotent IA group. Together with finite Hermite leading-pair enumeration, this proposes a decision procedure for targets outside gamma_3 in every nilpotency class. It remains a draft outside the claim ledger pending a separate proof audit and implementation checks. No new candidate is counted.

Archived Coulon–Fournier-Facio's accepted September 2026 version and verified Theorem 1.1, which already answers F35 in every rank >=2. Archived Lee's paper explicitly answering F1(b), F34(a), F38(c) in rank two, and Shpilrain's current automorphic-orbit survey. Updated live triage. The rank-two F37 reduction to equations was also derived but excluded as a routine consequence of classical Nielsen/Makanin results; a primary ICM source explicitly records the needed primitive-element definability. The higher-rank questions remain separate.

## 2026-09-28 approximately 12:15 UTC — two arbitrary-class N8 target strata

Completed and internally audited the IA argument drafted at 11:49 UTC. Fixed independent abelianizations give a finite list of factor-pair representatives; explicit central-layer IA orbit lifting decides membership. The implementation passed 32 direct records through rank-two/class-six and rank-three/class-four, including nonprimitive integer orbits and full leading-pair enumeration in smaller classes. GAP independently evaluated all 16 positive witnesses. A separate 12-case comparison with the previous class-five algorithm, including negative cases, passed.

The initial comparison timed out after 300 seconds without reporting a disagreement. Baseline code and failure are preserved at `31a1112` and `results/n8-ia-cross-v1`. Filtration-aware substitution and cached completed commutator pairs reduced the same comparison to 226.11 seconds. The unchanged direct suite passed again in 14.97 seconds; its witness fixtures were byte-for-byte identical to the independently checked originals. These are implementation checks, not a replacement for the termination and completeness proof.

A second route handles central targets in every class. Blessenohl–Laue's primary text supplies Klyachko's Lie idempotent and its product factorization. Inspected printed p.5 visually and retained the image in `literature/figures/N8-Laue-page5.png`. The product implies that no nonzero degree-n Lie tensor is invariant under a proper cyclic rotation. This proves nonvanishing of a block quadratic for every unequal-weight homogeneous bracket. Its rational linear factors give finitely many candidate first-factor lines, with integer linear systems deciding the second factor. Equal weights reduce to the injective exterior-square map. Exact Nielsen normalization reduces any nontrivial central group target to these homogeneous cases. The proof credits the imported classical theorem explicitly.

The central implementation passed 54 records in 4.08 seconds. They cover every weight type through rank-two/class-eight and rank-three/class-six, nonprimitive factors, identity boundaries, five negative examples justified independently by an Eisenstein obstruction in a metabelian representation, an exterior-rank negative control, and eight comparisons with the separate class-five solver. GAP evaluated all 35 positive witnesses (33 nonidentity, two identity) in 2.18 seconds.

Added both target strata to the same N8 partial candidate. The tally is unchanged: one whole-entry candidate (F28), one partial candidate (N8), zero established novel results. Intermediate target layers in classes >=6 remain unresolved. Targeted bibliography checks did not find a matching theorem, but the prior IA-orbit and Klyachko results are credited and novelty remains provisional. No Kourovka mathematics or code was imported.

## 2026-09-28 approximately 12:41 UTC — N5 whole-entry candidate

Returned to the wider portfolio and derived a candidate positive algorithm for direct decomposability of every finitely generated nilpotent group, including torsion. The finite torsion kernel of G/Z(G) -> R/Z(R), where R is the rational completion of G/T(G), gives an explicit bound on the indices of possible quotient factors in finitely many rational preimages. This reduces the quotient stage to a finite enumeration. Central lifting is then expressed using all relator defects, integer Smith decomposition, finite torsion shears, and a finite congruence image of an explicit integral matrix group. Complete proof and audit are in `problems/N5/proof.md` and `audit.md`.

The original full HTML, fragment and rendered statement were inspected. Prior rational decomposition results are credited to Baumslag–Miller–Ostheimer and, directly, Fisher–Gray–Hydon. The latter primary proof was separately read to verify the rational partition property. A concrete arbitrary-lift obstruction was found while auditing BMO Lemma 24 and verified in GAP; the new proof avoids that shortcut. This is not a claim that the published main theorem cannot be repaired.

The central subroutine passed 120 cases, with 60 independent finite subgroup-set comparisons and 45 independent modular comparisons; GAP independently checked all 54 positive central projections. The full quotient-branch/lifting pipeline agreed with GAP's separate decomposition routine on all 82 nilpotent groups of orders 4,6,8,9,12,16,27,32. GAP independently checked its 32 factor pairs. Seven infinite virtually abelian examples also passed, including three independently proved indecomposable groups with torsion; all four constructed decompositions were checked in GAP. Every recorded run passed. All jobs used one CPU slot and a 4 GB limit. The general rational-decomposition and bounded-index stages are established algorithms invoked by the proof, not an end-to-end software implementation claimed here.

Recorded N5 as a whole-entry candidate, with novelty provisional and external review outstanding. The tally is now two whole-entry candidates (F28,N5), one partial candidate (N8), and zero established novel results. No Kourovka mathematics or code was imported. The 48-hour clock is unchanged.

At 12:43 UTC, an additional GAP check independently computed six rational support preimages in three infinite products with nonabelian rational factors and noncentral finite torsion. The formula K_i=Y_i T(K) and its finite index bound held in all six cases. This addresses the bounded-index reduction separately from the finite-central-quotient lifting examples.

## 2026-09-28 approximately 13:05 UTC — M0 whole-entry candidate; GA5(b) prior answer

The solvable-group scan retained its scope boundaries: finite or derived-length-three commutator-width results do not settle S4 in all lengths; a recent co-Hopfian/injective direct-product paper does not answer the Hopfian/surjective question S5. No new result was inferred for S4–S8. Further F28 novelty searches found related work but no matching full answer.

Following the group-actions reference trail located Bartholdi–Sidki’s exact binary-tree theorem for an infinite-rank free abelian group, Theorem 1.2 of arXiv:1805.04732 (published 2020). Archived and read its proof, checked the original GA5 HTML and rendered statement, and corrected the live triage and literature ledger. GA5(b) is a prior positive answer and is excluded from discovery counts.

A finite-field route for M0 was derived at approximately 12:52 UTC. After reducing a primitive-preserving endomorphism to IA, a nonunit Fox determinant has a zero over a finite field. A Nielsen basis change makes all but one character value equal to one. Explicit free-group elementary automorphisms then realize SL on the kernel hyperplane, so a primitive word detects any singularity. The chain rule contradicts preservation of primitivity. Full candidate proof and internal audit are in problems/M0/. The classical square-Jacobian criterion is credited to Bachmuth; no assumption of tame automorphisms in rank three is made.

The exact Python checker passed 177 records in 0.32 seconds: 103 primitive-column orbits, 20 singular examples including basis changes, and 54 positive automorphism controls. GAP independently checked all 177 records in 1.93 seconds using affine-matrix word evaluation and explicit two-sided inverse free bases. Fields of orders 3,4,5,8,9,16 and ranks two through four are covered. An initial GAP run failed on an unavailable KroneckerDelta function; its failed logs remain, and the sole correction was an explicit index comparison. The successful rerun has empty stderr. All jobs used one core and 4 GB.

Archived and read primary 1992, 2015 and 2020 sources. The 2020 paper explicitly leaves higher ranks open, while the 2015 theorem requires preservation of primitive systems of length r-1. The candidate is for individual elements in all finite ranks; only rank >=3 is potentially new. The tally is now three whole-entry candidates (F28,N5,M0), one partial candidate (N8), zero established novel results. Independent specialist review and fuller novelty checks remain due. No Kourovka arguments or code were imported, and the 48-hour clock is unchanged.
