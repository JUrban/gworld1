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

## 2026-09-28 approximately 13:08–13:18 UTC — one-relator prior-result audit

Archived and read Wang–Zhang's July 2026 paper: it explicitly answers OR7(a,b,c) and OR8(a,b,c) negatively using commutator-relator groups with Baumslag–Solitar retracts. These prior examples, whose authors disclose ChatGPT assistance, are excluded from the experiment's discovery count. Confirmed Minasyan–Zalesskii's exact positive OR11 theorem. OR2 follows from Dahmani–Guirardel's general hyperbolic isomorphism theorem; OR6 follows from Wise, with k=0,+/-1 and r=1 handled separately.

For OR12, read Louder–Wilton Theorems 5.1 and 6.5(i), and Logan's use of the Fischer–Karrass–Solitar ends theorem. A fully invariant finite-index subgroup supplies the elementary transfer of co-Hopficity needed to deduce the exact answer. Recorded this as a routine consequence of prior results, not a novel solution. The complete original one-relator HTML and page rendering were inspected, including all separately paragraphed OR7 subparts; metadata and live triage updated. Detailed note: research/notes/OR-prior-resolutions.md. No tally change. No mathematical computation was needed for this bibliographic audit.

## 2026-09-28 approximately 13:21–13:30 UTC — N8 penultimate-layer extension

Extended the central-target argument to all targets in gamma_(c-1), in every finite rank and class. For unequal leading weights, all integral leading pairs lie on at most two rational lines with finitely many divisor scale allocations. For equal weights, finitely many Hermite sublattices represent the pairs modulo exact commutator-preserving Nielsen moves. A single final central correction is an integer linear system; terms involving two corrections vanish. Full proof and audit added under problems/N8/.

The Python prototype passed 85 records in 58.56 seconds, through rank-two/class-nine and rank-three/class-seven. It includes 14 comparisons with the separate class-five solver, 19 negative central perturbations and five negative leading-term controls. In 27 positive cases an earlier leading branch failed, including a scale-sensitive class-six example that would be missed by retaining only primitive first factors. GAP/nq independently verified all 49 word witnesses and all 187 central subgroup-membership branches (140 negative) in 120.23 seconds. Two harmless GAP parse-time global-binding warnings are documented; both jobs completed, and all output was inspected. Each used one CPU slot and a 4 GB limit. No failed run occurred in this extension.

Added this scope to the same N8 partial candidate. The tally remains three whole-entry candidates (F28,N5,M0), one partial candidate (N8), zero established novel results. Earlier intermediate layers remain unresolved, and external review/novelty checks remain outstanding. No Kourovka mathematics or code was imported; the 48-hour deadline is unchanged.

## 2026-09-28 approximately 13:35–13:47 UTC — complete class-six N8 scope

The next correction stage led to an explicit proof that L2 tensor L3 embeds into L5 under the bracket: cyclic invariance of a kernel tensor would force full alternation, while alternation annihilates its L3 block. A separate polynomial-syzygy dimension calculation identifies the degree-four metabelian kernel. Together these prove three zero-kernel correction maps needed for leading target degrees three and four. Finite Nielsen residue normalization handles the remaining first-stage freedom. Combined with previous strata, this gives a candidate decision algorithm for every target in class six, all finite ranks.

The exact kernel suite passed 44 records in 11.61 seconds. It also retained a nonzero higher-degree kernel with a nonzero degree-seven cross term, preventing an unsupported generalization. The group prototype passed 63 records in 11.31 seconds, including 19 negative middle-layer perturbations and a positive case needing a nonzero residue modulo three. GAP independently checked all 40 positive witnesses and all 133 new lifting subgroup-membership tests, including 76 negative, in 8.85 seconds. All three runs completed with empty stderr, each using one core and a 4 GB limit. Full proof and audit are in problems/N8/class6-proof.md and class6-audit.md.

The same N8 partial candidate now covers all targets in classes3-6, plus the two previously recorded arbitrary-class strata. Other intermediate layers in classes>=7 remain unresolved. Tally unchanged: three whole-entry candidates, one partial candidate, zero established novel results. Independent review and full novelty checks remain outstanding.

Completed two bibliographic exclusions: Myropolska's Theorem1.3 and Grigorchuk corollary answer AUX3(b) positively; (a) remains separate. Ould Houcine's 2007 primary publisher abstract explicitly gives the positive FP17 answer. The full FP17 proof was not retrieved (old author URL404, direct publisher403), and that evidence limitation is recorded. Both original full HTML pages and the relevant rendered statements were inspected. No new count or imported Kourovka argument results from these prior findings.

## 2026-09-28 approximately 13:47–14:01 UTC — wider matrix/metabelian pass

Archived and read the exact primary scope of Krasilnikov's finite-basis theorem (nilpotent derived subgroup; connected linear groups), Chorna–Geller–Shpilrain's special parabolic subgroup algorithms, and Artamonov's finite-rank projective metabelian theorem. Original MA3, MA5 and M4 statements and renderings were inspected; the two short theorem pages were also viewed. None resolves the corresponding full GroupWorld entry. A stale MathNet URL failed; the subsequent language-option mismatch was identified, and the Russian and English PDFs are separately retained with correct metadata.

Recorded why several tempting reductions are incomplete: a kernel's ordinary infinite generation does not show failure of finite normal generation; solvable word-problem undecidability is not itself metabelianity-recognition undecidability; the bounded-degree linear embedding theorem does not cover arbitrary locally linear groups. An abstract countable universal tree of groups for FP9 was written out, with its missing effective diagram and recursive-presentation step explicit. It is not a counted partial answer.

Updated live triage, the literature ledger and the next portfolio focus. No mathematical computation or subagent was launched during this pass, and no Kourovka-run mathematics or code was imported. Tally unchanged: three whole-entry candidates, one partial candidate, zero established novel results. Deadline unchanged.

## 2026-09-28 approximately 14:02–14:17 UTC — braid prior answers and bounded B9 evidence

Confirmed three prior positive answers: Fromentin for B8, Bell–Schleimer for B13, and the July 2026 Bharathram–Birman–Brendle preprint (September v2) for B3. Archived the primary texts, inspected the original complete braid page and each exact rendered paragraph, and documented proof-audit limitations. All three are excluded from discovery counts.

For B9, exact Artin-action enumeration through term height four produced 52 special braids in B5. GAP independently checked every recursive witness, equality classes and finite-height closure, and separated all52 by finite Burau matrices. A height-five Artin run timed out at120seconds and is preserved. A different finite-matrix calculation then certified1930 distinct special braids in B6 at height at most five; GAP independently checked the free-word parent identities and all matrix images. Successful runs used one core and4GB, with empty stderr. The numerical bound2^n printed in Dehornoy p.13 cannot hold, but no fixed-strand exhaustion theorem or disproof of the height-converse question follows. This evidence is not an additional counted partial candidate.

Tally unchanged: three whole-entry candidates, one partial candidate, zero established novel results. No Kourovka mathematics/code imported; no subagents or external contacts; deadline unchanged.

## 2026-09-28 approximately 14:20–14:47 UTC — F20/GA scope and rank-two class-seven N8

Archived and read Moravec–Morse's computational F20 paper and the relevant
parts of Kharlampovich–Vdovina's Lambda-tree survey. The original F20,
GA2 and GA3 full pages and rendered paragraphs were checked. GA2's
finitely generated quantifier is not covered by the finitely presented
biautomaticity theorem. GA3's literal missing nonabelian hypothesis is
recorded without claiming an intended-problem discovery.

Five one-core/4GB KBMAG probes reproduce the known rank-two weight-five
case but do not settle weight six. Ten of eighteen next-layer targets
reduce to identity; the others are undecided. Enlarged limits hit the
equation or state bounds. One reduction then raises a GAP method error;
its zero exit status did not fool the recorded runner, which rejected
the absent completion marker. All logs and the earlier script are saved.

For N8, a rank-two correction kernel has dimension at most one, allowing
the remaining class-seven obstruction to be decided by an integer-valued
univariate quadratic modulo a fixed lattice. A displayed determinant-minus-one
minor handles the other new correction kernel. Higher linear layers
are solved jointly. The initial exploratory shorthand x->xy was corrected
to the exact commutator-preserving x->yx; the final proof and algorithm
use the latter.

The bounded kernel probe passed 51 records in 2.08 seconds. A first group
test failed after 6.49 seconds because Smith coefficients overflowed Python
word-list expansion; its scripts and partial outputs are preserved.
Exact kernel-lattice reduction shortened witnesses. The rerun passed 67
targets in 94.23 seconds, with 39 positives and 28 negatives. GAP independently
verified all 39 witnesses, 196 linear decisions (89 negative), 40 arithmetic
certificates (22 negative), 192 parameter samples, and the degree-six
rank-four injection in 6.48 seconds. The samples support the polynomial
degree proof rather than replacing it. The GAP global-variable warning
is documented; all raw output was inspected and preserved.

The same N8 partial candidate now includes all rank-two/class-seven
targets. Its larger-rank/class-seven and higher-class intermediate
layers remain unresolved. Tally unchanged: three whole-entry candidates,
one partial candidate, zero established novel results. No Kourovka
mathematics or code was imported; no subagents, pushes or external
contacts occurred. The original 48-hour deadline remains unchanged.

## 2026-09-28 approximately 14:48–15:22 UTC — all-rank class-seven N8 and equation scope

Proved a complete classification of the exceptional (1,4) correction
kernel in arbitrary finite rank, using the homogeneous free generators
of the derived Lie algebra. The kernel is zero except when D=(ad_z)^2 T,
when it is precisely the line generated by (T,-[T,[z,T]]). The same
structural decomposition gives the all-rank (2,3) Nielsen kernel.
The new (2,2) leading type has a unique first correction and a joint
linear tail. The resulting group algorithm covers all class-seven
targets in every finite rank. The primary homogeneous Shirshov lemma
was checked in Bryant–Kovacs–Stohr (2005); no restricted-Lie assertion
is silently used.

The bounded kernel suite passed32 records. Two rank-three group runs
reached300-second limits: the first had no completed target; the second
completed nine positive targets. Their exact scripts, partial outputs
and raw logs are retained. Installed python-flint0.9.0 for larger exact
integer systems; verified unimodular Hermite/LLL transformations and
compared80 integer systems with the earlier Smith implementation.
A degree-grouped Magnus multiplication agreed with the original in42
checks. The resulting full group suite passed26 targets in275.03seconds,
with13 positive witnesses and13 negative decisions. Its four scheduled
faulthandler stack dumps are diagnostic reports, not failed checks.

GAP/nq independently verified all13 witnesses,81 linear decisions
(39negative),8 quadratic certificates (6negative),48 parameter samples,
and degree-six direct-sum ranks28+53=81, in217.69seconds with empty
stderr. The all-rank proof does not rely on inferring a universal kernel
bound from these finite examples. Each job used one CPU slot and at
most8GB; raw logs were inspected and retained. The largest new
certificate blob is approximately32.7MB, below the90MB repository limit.

The same N8 partial candidate now covers all targets in classes3-7,
all finite ranks, plus the earlier arbitrary-class degree-two and
penultimate/central strata. Other intermediate layers in classes>=8
remain unresolved. Tally unchanged: three whole-entry candidates
(F28,N5,M0), one partial candidate (N8), zero established novel results.
Independent specialist review and fuller novelty checks remain due.

Separately, checked Sela's full E5 theorem including coefficients and
arbitrary factors, and Groves–Hull's H12 theorem including torsion.
Both are prior positive answers. Chiodo's A6 theorem excludes fixed
bounded output length only; the unrestricted question is not resolved
by that theorem. A4 has a prior positive consequence from residual
finiteness and a routine proof-enumeration adaptation of Hass's finite
quotient argument. All four original full pages/paragraphs and rendered
statements were inspected. F28,N5,M0 were re-read internally without
finding a gap; this is not independent validation or a new experiment.

No Kourovka mathematics or code was imported. No subagents, pushes or
external contacts occurred. The original 48-hour deadline is unchanged.

## 2026-09-28 approximately 15:23–15:47 UTC — wider scope and FP21 reformulation

Confirmed prior answers for H13 and FP6 from primary texts: Bridson's
synchronous combable examples have cubic Dehn function and are not
automatic; virtual fibering covers all knot-exterior cases and gives
a finite-index free-by-cyclic subgroup. Read the original complete
pages, exact fragments and rendered paragraphs. Also checked N1's
existing full-classification update against Papistas's primary abstract;
it is not limited to rank two. Full Papistas/Formanek proofs were not
obtained. A direct publisher download returned 403; the web abstract
was available. A misspelled monograph URL returned 404 before correction.

Read the primitive Burnside results of Bou-Rabee–Hooper and Dlugie.
Wrote out the consequence that BP(2,m) is residually finite if and only
if the four-strand truncated braid group Br_4(m) is residually finite.
The argument proves the needed three-strand residual finiteness via
cyclic central extensions of triangle groups and finite Heisenberg
quotients, and gives the finitely-generated split-extension lemma.
Goldman's dihedral theorem corroborates the three-strand case; her
triangle-free theorem does not apply to the four-strand presentation.
The commuting label-2 edge must be included in its presentation graph.
This is an uncounted reformulation, with no novelty claim and no
large-exponent answer. An infinite linear quotient is insufficient.

A deterministic GAP check verified Dlugie's explicit splitting maps
using the faithful Artin action and a separate semidirect-product
calculation, including an incorrect-sign control. It passed in 1.83
seconds on one core with a 2GB limit and empty stderr. Raw stdout,
including its leading carriage return, is preserved. This finite
identity check does not itself establish residual finiteness.

H4's preprocessing literature was read without confusing a recognition
procedure with an arbitrary promise algorithm. Other broad searches
and tentative routes in nilpotent, solvable and tree-action questions
produced no completed new argument. The records identify these gaps.

Tally unchanged: three whole-entry candidates (F28,N5,M0), one partial
candidate (N8), zero established novel results. No Kourovka mathematics
or code imported; no subagents, pushes or external contacts. Original
deadline unchanged.

## 28 September 2026, approximately 15:48–16:08 UTC — F27 lead and M0 constructor

Read the F28, N5 and M0 candidate proofs again; this internal pass found
no new gap. This is not external validation. Investigated a possible
F27 construction using an automorphism stabilizer and normal roots.
Abelianization leaves finitely many possible root vectors, while the
Freiheitssatz reduces roots of a word in a free factor to that factor.
Neither observation gives finiteness of conjugacy classes. No root
with the required infinite stabilizer orbit was found. Barmak's tiling
examples lie in the commutator subgroup and do not meet F27's hypothesis;
the 2025 one-relator survey still lists the actual question as open.
Archived and read the relevant primary passages, the original full
page/background and the F27 screenshot. No new candidate.

Revisited N9(a)'s fixed-group obstacle without resolving it. The known
varying central-product construction and the earlier failed central
tilt remain insufficient. A proposed N3 route using nested nilpotent
covers also lacks a torsion-freeness proof and an arbitrary-cardinality
construction. A Notebook search lead credits a countable-case result
to Romanovskii (1969), but that original preprint was not located or
audited here; no new status or solution claim is based on it. Broader
searches of one-relator solvable centers yielded no completed S3 result.

Implemented an end-to-end M0 witness constructor. It takes arbitrary
generator-image words, handles nonunimodular abelianization, constructs
IA and character normalizations by explicit Nielsen moves, finds a
singular finite-field Fox matrix, and returns an actual primitive free
basis with zero image column. Unit determinants are decided exactly;
bounded search exhaustion is explicitly inconclusive. The final
certificate refers to the original input map, including non-IA maps.

The seeded Python run produced 29 witnesses and 13 exact unit
determinants among 44 inputs, with two intentional bound controls,
in 0.72 seconds on one core/4GB. GAP independently verified the 29
free-basis/image certificates and all 13 symbolic unit determinants in
1.87 seconds, one core/4GB, with empty stderr. An F4 character was
selected by the search rather than supplied. The longest witness-basis
word had length 76.

Preserved three failed GAP checks with exact checker snapshots. The
first two exposed equality between integer and polynomial constants;
the diagnostic showed actual=1 and expected=1. After subtracting and
testing zero, the third reached an unavailable generic symbolic-matrix
inverse. Explicit affine inverses fixed that implementation issue.
The candidate proof and Python certificates were unchanged. The runner
rejected all three despite zero GAP exit codes, because the marker was
missing. Raw output hashes, including carriage returns, are preserved.

Tally remains three whole-entry candidates (F28,N5,M0), one partial
candidate (N8), and zero established novel results. No imported
Kourovka mathematics/code, subagents, push or external contact. The
48-hour deadline remains 30 September 2026 at 10:04:49 UTC.

## 28 September 2026, 16:09–17:02 UTC — class-eight proof and implementation audit

Developed six all-rank correction-kernel lemmas for N8(b), then a
stronger quadratic cokernel obstruction in the exceptional (1,4)
branch. The latter leaves at most two integer parameters, avoiding
the initially proposed cubic/progression route. The complete candidate
argument is in `problems/N8/class8-proof.md`; scope promotion awaits
the remaining independent group checks. Tally remains unchanged.

Exact bounded checks passed 39 kernels and eight quadratic obstructions
in ranks two and three, and GAP independently confirmed all their
ranks. The final rank-two suite passed 22 targets; GAP checked 15
witnesses, 75 linear decisions, ten polynomial decisions and 50 samples.
Preserved all syntax failures, diagnostic runs, incomplete suites,
raw logs and relevant source snapshots. The audit details them.

The rank-three investigation exposed a mutable test-fixture alias:
appending to a borrowed Hall word changed the stored word but not its
algebraic value. An exact reproducer archives the discrepancy; copying
the word fixes the fixture. No proof or group-arithmetic correction
was needed for that failure. A separate certificate change retains
the original target word, avoiding a redundant large expansion.

To make the larger checks practical, projected joint-tail systems to
injective Hall pivot rows, preserving their entire integral solution
sets. Added balanced cached word expansion, checked against the prior
sequential arithmetic and every Hall word through degree eight in
ranks two and three. Integer-kernel shortening was also verified; its
measured improvement was small and is not credited with the major
speed gain. All checks use exact arithmetic; no numeric approximation
decides membership.

The combined rank-three run has passed its eight primitive leading-type
examples and both mixed-generator exceptional examples. Its random
nonprimitive (1,3) example is expensive; a separate bounded suite is
checking degree-seven and degree-eight negative controls. The previous
rank-two nonprimitive example already exercised period three, residue
one. Do not describe a partial run as a completed suite.

A wider reading pass over the unresolved matrix, free-group, solvable
and tree-action questions yielded no further candidate. In particular,
an archimedean small-root argument does not apply to arbitrary ordered
abelian length groups in GA1. No new scope claim follows. A telescoping
derivation identity supplies higher (1,2m+2) kernel examples for future
N8 investigation, but no class-nine algorithm is inferred.

## 28 September 2026, 17:03–17:23 UTC — class-eight candidate scope recorded

The rank-three broad Python benchmark reached its 400-second cap after
completing ten positive targets, on its random nonprimitive (1,3) case.
Kept the complete prefix and the timeout; the unfinished case is not
reported as passed. A separate deterministic control run completed five
negative targets before its 240-second cap. Running only its remaining
case and the two boundaries completed the eight-control dataset.
The data-only merger checks disjoint targets and common Hall words and
records source-file hashes. No completed target needed to be rerun for
that merge.

The first GAP positive and control runs each reached 600 seconds without
a completion marker. A cached word evaluator passed the full rank-two
comparison and then checked all ten rank-three witnesses, but larger
subgroup membership tests remained slow. That intermediate checker was
interrupted after 335 seconds and is preserved with its progress output.

The final GAP verifier uses its own integral polycyclic coordinates in
an abelian lower-central tail. It checks the defining-pcp and
lower-central-suffix conditions, infinite relative orders and coordinate
support, solves the resulting integer system with GAP's SolutionIntMat,
and multiplies every positive coefficient solution in the actual group.
The relevant primary nq source and Polycyclic/GAP API documentation were
read locally. This avoids repeated general subgroup construction and
retains independent integer and group arithmetic. The full rank-two
comparison passed before using the revised verifier on rank three.

Both final rank-three GAP checks completed with empty stderr: the ten
positive records in 119.68 seconds, and the eight controls in 85.56
seconds. They verify eleven witnesses, 42 linear decisions (seven
negative), fourteen polynomial decisions (six empty parameter sets)
and seventy parameter samples. Together with the final rank-two data,
there are forty completed target records, 26 witnesses, 117 linear
checks, 24 polynomial certificates and 120 samples. These counts refer
to the final datasets, not the overlapping preliminary suites. The
39 kernel and eight quadratic-obstruction ranks were also checked in
GAP separately.

Promoted the written class-eight extension to the same partial N8(b)
candidate in the append-only claim ledger, current triage and progress
report. Scope is now all targets in classes three through eight, in
every finite rank, plus the earlier arbitrary-class strata. Classes
nine and higher retain uncovered intermediate layers. No external
specialist review or exhaustive novelty certification has occurred.
The tally remains three whole-entry candidates, one partial candidate,
and zero established novel results. All work is local; no push,
external contact, subagent or Kourovka mathematical/code transfer.
The original deadline remains 30 September 2026 at 10:04:49 UTC.

## 2026-09-28 17:29–17:45 UTC — M4 proof scope and N3 construction audit

Obtained Artamonov's full 1978 English paper from MathNet im1711, read
the whole extracted text and viewed printed pages 221–222. The theorem
is finite-rank. Its module freeness and augmentation-compatible basis
steps do not supply an infinite-rank argument. Read Bass's original
big-projective theorem after locating its hypotheses in Lam's survey;
the countable Laurent ring has zero Jacobson radical and is not
Noetherian, so the direct invocation fails. Recorded the precise gap
and committed this source audit as af1bc2d. No M4 candidate.

A follow-up on locally nilpotent covers located GSW 2003, whose
Corollary 3.7 states a full positive answer to N3. Read all of section 3,
the full original GroupWorld nilpotent page and N3 fragment, and viewed
the original statement plus printed pages 232–233. The construction
lemma's degree-layer argument drops needed normal conjugates. A small
UT4(Z) witness and independent GAP class-three calculation confirm
that its proposed spanning subgroup is too small (ranks two versus
three in the relevant intersection).

A bounded nq probe of three-generator profiles with every coordinate
pair class two found actual torsion at full class five. At class four
there is a finite relative order but no group torsion; this distinction
is retained. The first exact Magnus search looked only at individual
Hall words and failed to find a witness; preserved its assertion log
and source. The next search found a product of two weight-five Hall
words with order two, a five-term square identity, and a mod-two
separator supported on three tensor monomials.

Wrote the proof that 78 relator/conjugation-difference vectors span the
exact normal subgroup in gamma3 of the free class-five group. Since
this layer is abelian and three conjugation differences vanish, its
integer lattice is closed under both positive and negative generator
conjugation. A dependency-free Python verifier reconstructs the words
and checks the positive identity and every separator value. Independent
GAP/nq checks the same positive identity in the free class-five group
and verifies a nontrivial central order-two image in the quotient.
The preliminary GAP check passed with a forward-global syntax warning;
its source/log were retained and the final check has empty stderr.

The final standalone and GAP checks take about 0.22 and 1.97 seconds.
Peak requested simultaneous resources in this pass were two CPU cores
and 12 GB memory. All failed/diagnostic runs and raw log hashes remain.
Detailed audit and certificates: research/notes/N3-published-cover-audit.md.

This disproves GSW Proposition 3.5, not N3 or the possibility of another
cover. The finite example is itself covered by the free class-five
group. Record N3 under published-claim/proof review, not as a verified
prior resolution and not as a new negative answer. The tally remains
three whole-entry candidates, one partial candidate, zero established
novel results. No subagents, external review/contact, push, parent-repo
modification or imported Kourovka mathematics/code. Original deadline
remains 30 September 2026 at 10:04:49 UTC.

## 2026-09-28 approximately 17:49–18:03 UTC — wider scope and S3 module lead

Returned to algorithmic, growth, automatic and solvable-group entries.
The full original S9 background ends with Timoshenko's 2006 answer in
all derived lengths; an initial reading of its preceding paragraph
would incorrectly retain d>=4. Archived the primary paper and abstract,
read the theorem/corollary, viewed p.456, and retired S9 from discovery.

For S3, obtained Timoshenko1998. Its English endpoint was not a PDF;
the Russian original downloaded successfully but has garbled extracted
text. Viewed the statement and exact source pages925,926,930,931.
Last-derived relators, including proper powers, are already covered.
The broader theorem requires a centreless lower quotient and a group
ring without zero divisors. Wrote out the cover-chain-complex reduction
of the remaining centre problem to invariant elements in a quotient
Fox module. Proper powers surviving in the lower quotient produce an
explicit annihilator, preventing the naive cancellation step. No new
candidate or solvable-quotient computational search follows.

H16's automatic/biautomatic distinction and S4–S8's existing scope gaps
remain. No imported Kourovka mathematics, author contact or push.

## 2026-09-28 approximately 17:59–18:08 UTC — terminating M0 construction

Developed an explicit finite-field selection for the existing M0 proof.
A base-B Kronecker substitution separates the Laurent determinant's
monomials. After shifting to a polynomial of degree D, choose a prime
not dividing either endpoint coefficient, then an irreducible factor.
Its residue root is nonzero and different from one. This gives a proved
field-order bound and a direct Nielsen basis for the character, avoiding
discrete logarithms. Polynomial-basis digits give the transvection
coefficients without enumerating all field elements.

Implemented the separate scripts/m0_kronecker_witness.py. Twelve inputs
in ranks1–4 produced nine witnesses and three unit determinants; fields
of orders2,4,5,8,11 occur, longest basis word28. Four extra polynomial
cases exercise substitution arithmetic. Python passed in0.42 seconds;
independent GAP arithmetic verified all12 decisions in1.88 seconds.
The first Python run used the default factorizer with no random seed;
retained its exact source/output, switched explicitly to deterministic
Berlekamp factorization, and reran. Final certificate JSON and GAP input
are byte-identical, so the independent GAP check applies unchanged.

All three runs used one core/8GB, passed with empty stderr, and their
raw log hashes were checked. Wrote the complete finite-bound proof,
limits, regeneration instructions and an artifact manifest. The old
bounded constructor remains unchanged. This adds no result count;
M0's specialist review and novelty audit are still outstanding. No
external contact, push, subagents or parent-repo modification.

## 2026-09-28 approximately 18:09–18:21 UTC — N9 fixed-group reduction audit

Read the original N9 statement, full page, background and actual
rendering. The background and Roman'kov2016 introduction both distinguish
uniform retract undecidability from the fixed-group question. Obtained
the author's paper text through web extraction but not its PDF:
publisher HTTP202/empty, author-page HTTP403. Archived and visually
checked Myasnikov2016 slide35, physical page65.

The literal central-product construction forces both new generator
images to be central in the base, so its retraction exists only for a
trivial target. Wrote an explicit class-two coproduct repair for targets
in G', proving that the base embeds and that a retraction exists exactly
when the target is a commutator. This preserves the uniform theorem;
its ambient group still varies. Source terminology is qualified until
the original article PDF is checked.

The attempted automorphism/shear encoding in a fixed base also fails:
retracts reflect equations with coefficients in them, so a fixed common
target has constant commutator status across such a family. Preserved
this obstruction and the older failed extra-central-generator route.

GAP/nq verified the corrected inclusions/retractions for four integer
parameters and rejected the invalid central-product assignments, with
an explicit zero-target control. First run passed with parser warnings;
its exact source/logs remain. The locally scoped rerun passed in1.93s
with empty stderr, one core/8GB. No new whole or partial candidate,
external review, imported Kourovka argument, contact or push.

## 2026-09-28 approximately 18:22--18:45 UTC — F41 rank-two transfer candidate

Read the full original free-group page and background, rendered F41,
and viewed its screenshot. The identity exception and distinction
between spherical limits, limsups and balls are explicit. No literal
loophole is counted.

Developed a core-graph estimate for injective images of a filling
nonprimitive word. The abstract loop is counted in a single intrinsic
automorphic orbit; every edge is traversed twice, so extra label length
costs at least twice as much ambient word length. After summing over
the finitely many graph types and restoring conjugators, polynomial
intrinsic cyclic-orbit growth implies the ambient square-root bound.

Located Puder's exact prior twice-traversal lemma and threshold theorem,
and credited them. Replaced an uncertain all-length interpretation of
the Khan citation by Erlandsson--Souto's precise punctured-torus curve
counting theorem. This gives F41 for pi(w)<=2. Ambient rank two and
pi=2 in ranks>=5 are already prior; only ranks three and four remain
potentially new in this partial candidate. No matching result was
found in bounded searches, but novelty and specialist review remain
outstanding.

The deterministic Python graph audit checked11,048 closed paths of
length<=8, including9,912 filling nonprimitive paths, with unused-edge
and primitive single-traversal controls. It also generated18 marked
immersed labelled examples in ambient ranks3,4. GAP/fga independently
verified their Nielsen markings, injective rank-two subgroup images,
word identities, immersion and lengths. Runs passed in0.42s and1.87s,
one core/8GB each, empty stderr. Three noninjective controls demonstrate
why the theorem must not be extended to arbitrary homomorphic images.

Proof and audit are in problems/F41/. Tally becomes three whole-entry
candidates and two partial candidates, with zero established novel
results. No external contact, push, subagents or parent-repo changes.
