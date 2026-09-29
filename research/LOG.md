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


## 2026-09-28 approximately 19:08--19:34 UTC — N8 class-nine proof and prototype

Resumed the original clock and repository after a preparation-only detour in
the preceding continuation. That detour did not advance the research goal;
its separate checkout is not used for this run and did not reset the deadline.

Developed a homogeneous delta-stable free basis of the derived free Lie
algebra, using the primary free-metabelian torsion-free module theorem and
the previously credited homogeneous Shirshov lemma. Wrote five correction
kernel proofs, an exact simultaneous-commutator-conjugation period, and a
new degree-nine quadratic obstruction. The all-rank class-nine theorem is
written as a proposed extension under audit in problems/N8/class9-proof.md.
The counted N8 scope remains classes three through eight pending completion
of the independent checks.

Exact Python checks passed for 21 rank-two and 23 rank-three kernels and two
obstructions in each rank. The rank-two solver completed 27 target records
(including repeated controls), with 21 witnesses; GAP independently replayed
68 linear decisions, 17 polynomial certificates and 85 samples. Eight
polynomial branches had no admissible parameter. A nonprimitive type(1,2)
example required first residue2 and third residue1, both modulo4.

Two rank-three kernel benchmarks timed out before a multidegree-block
projection and zero-skipping reconstruction completed the same suite in
115.16s. A long-word arithmetic comparison timed out; a shorter comparison
passed 128 coordinate/rational-line cases and eight collection cases. An
exact tail formula passed 18 comparisons with full group commutators. The
full rank-three target benchmark timed out at400s in its first joint tail;
this is not counted as a completed decision. Further high-weight decisions
and GAP verification are running. Failed scripts and logs are retained.

No new whole-entry count, established novelty, external review, subagent,
push or contact is claimed. All recorded computations use one core and8GB
per process within the shared budget.


## 2026-09-28 approximately 19:35--20:15 UTC — independent class-nine audit and arbitrary-class lead

The last continuation returned to preparation context and only rechecked a
separate preparation checkout. It made no progress on the research goal.
The original active repository and deadline were revalidated; research
resumed without restarting the clock.

Completed independent rank-three class-nine kernel checks in GAP's free
associative algebra, using exact relations and full modular ranks. Added
component Hermite arithmetic and retained the seven completed new-stratum
records from an otherwise timed-out rank-three target benchmark. The first
GAP target replay was deliberately interrupted after five witnesses and
one linear decision; subsequent exact integer-coordinate and component
versions first reproduced the full rank-two certificate suite. The larger
replays remain in progress. See problems/N8/class9-audit.md for exact
completed evidence and every unsuccessful run. Counted scope remains
unchanged until the audit is closed.

Developed a uniform special family in every class c>=6: targets in degree
c-2 with leading term ad_z^(c-4)(T), T in L2. A free differential-algebra
argument classifies the first correction by parity. For even n=c-5 the
functional T_j -> A+(-2)^j B gives a nonzero quadratic obstruction
1-4^(n/2), leaving at most two integer parameters. A block-quadratic
argument proves uniqueness of the degree-one leading direction. The
written proof and implementation now recognize rational scope before
checking integral factorization; unsupported inputs are never returned
as negative answers.

Exact jet identities passed for n=1,...,16. Group suites passed in class10
and class11, rank2, and mixed-generator class7, rank3. They include both
negative perturbations and nonprimitive leading factors. The class10
GAP replay passed; the other independent group replays are running.
Version-one sources are retained before the recognition refinement.
The special-family proof is still an uncounted extension under audit.

All computations use one core and8GB each; current concurrent reservations
are within the shared budget. No subagents, specialist review, remote
push, contact or parent-repository edit.

## 2026-09-28 approximately 20:22 UTC — uniform N8 family added to the partial scope

All three selected group suites have now been independently replayed in
GAP, including both negative cases in each suite. Two additional same-degree
outside-scope inputs are themselves commutators and correctly return
unsupported;16 signed leading scales agree with the earlier factor routine.
Closed the uniform-family audit and extended the existing N8 partial scope.
Tally remains three whole-entry and two partial candidates, zero established
novel results. The separate all-target class-nine replays remain live.

## 2026-09-28 approximately 20:23--20:34 UTC — second uniform-family lead and remaining replay

The class-nine ordinary integer-coordinate replay timed out after all five
witnesses and12 linear decisions, at its first polynomial certificate.
Two intermediate versions timed out after five witnesses and three linear
decisions. Exact commutator identities, verified Hall commutator-tree caches
and sparse zero-exponent skipping each reproduced the rank-two suite before
being used in later rank-three replays. Two such replays remain live. Their
finite prefixes are not complete validation and no class-nine scope update
has been made on their strength.

A second arbitrary-class lead uses leading type(2,2n+3) in class2n+7.
A free-alphabet derivative argument excludes degree-one factors, while a
projection onto the free Lie algebra on C in L2 and T in L3 excludes every
other leading type. The same parity and quadratic functional appear in
the remaining correction. Rank-two exact probes passed in class11 (first
rank31/32; obstruction ranks59,60) and class13 (first rank101/101), also
checking that only the two signed type(2,q) leading pairs survive. The
class13 run has a scheduled stack snapshot and normal completion. This
lead is uncounted pending implementation, independent replay and proof
audit. Current scope/counts and original deadline remain as recorded.

## 2026-09-28 20:35:40 UTC — class-nine rank-three audit completed

The final sparse GAP replay passed in126.40 seconds, with empty stderr:
five witnesses,12 linear decisions, six polynomial certificates (four
empty parameter lists),30 group samples. The final rank-two counterpart
passed the existing full suite in4.64 seconds. The previous Hall-cache
replay was deliberately interrupted after497.65 seconds, after the identical
dataset had passed; its completed prefix is retained, not called a pass.

Extended the same N8 partial candidate through all targets in class nine
and all finite ranks. Updated proof/audit, scope ledger, triage and progress.
The overall tally remains three whole-entry and two partial candidates,
zero established novel results. Neither the failed broad benchmark nor
any incomplete replay is treated as completed. The original deadline,
resource budget and outstanding specialist/novelty review are unchanged.

## 2026-09-28T21:04:36.661492+00:00 — second N8 family audited; wider portfolio resumed

Collected terminal records for all three new Python group suites and
the independent GAP replays. Class11/rank2 and class9/rank3 passed;
class13/rank2 timed out after600.02 seconds without a completed witness.
Wrote the all-rank proof and audit, explicitly retaining this limitation,
and extended the same partial N8 scope. Tally remains3 whole-entry,
2 partial,0 established novel results. Original deadline unchanged.

The preceding preparation-only detour updated only the separate
`gworld-prep` checkout. It did not reset this run or its deadline.
This goal continuation explicitly resumes the original research.

Read primary introductions for N4 and MA6, including the July2026
Jang–Yi revision. A new H4 output-size argument was worked out around
20:59–21:01 UTC and preserved as an uncounted lead pending full audit.

## 2026-09-28T21:14:46.624527+00:00 — H4 candidate completed at the local audit level

Wrote a negative uniform complexity argument: every Dehn presentation of
a finite group has an acyclic forbidden-factor automaton, bounding group
order by (2m)^((m+1)^2). Explicit presentations of size4n+8 define
C_(2^(2^n)-1) semidirect C_(2^n); every Dehn output is exponentially large
in n up to polynomial factors. Source and rendering audit completed,
including the absence of a finite-group exclusion. Changed output
generators are allowed; compressed output is expressly distinguished.

Python passed43 cases and10759 direct substring comparisons. GAP
verified4 finite models and3 independent presentation orders. First
GAP run passed with global-variable warnings; preserved its exact
source, then declared local variables and reran successfully with
empty stderr. The prior2012 finite-group suggestion is credited.
No established novelty is claimed. Added H4 as the fourth whole-entry
candidate; two partial candidates remain, zero established novel results.

N4 and MA6 primary-source checks produced scope qualifications only;
recorded them without adding candidates. No agents, contacts or push.
Original clock and all frozen source inputs unchanged.


## 2026-09-28T21:27:09.306817+00:00 — wider scope audit

Broader portfolio pass retired F24(b) using Diao-Feighn 2005, whose introduction explicitly names the problem. Read its input and algorithm statements. Audited H5 recognition versus decision and compared the H4 size obstruction with polynomial hyperbolicity certification methods; no conflict found in their stated scopes. Saved exact primary sources and F24/H5 rendered audits. No new count. The prior preparation-only response made no progress on mathematical discovery; this continuation resumes the same original run and deadline.


## 2026-09-28T21:41:56.112567+00:00 — nonlinear class-ten extension

Completed the nonlinear class-ten family argument: forced leading type and direction, injective polarization recognition, all-rank one-dimensional first kernel, and a nonzero final quadratic obstruction. The exact formal probe passed after a saved test-helper precondition failure. Five supported rank-two targets and three scope controls passed in Python; GAP independently verified three witnesses, seven linear checks, seven polynomial certificates (four empty) and35 samples. Two rank-three positive recognition cases and two scope controls passed. Added the family to the same N8 partial scope; tally unchanged at4 whole,2 partial,0 established novel. No live jobs remain from these suites, no push/contact/agents, original clock unchanged.


## 2026-09-28T22:08:34.500889+00:00 — F38(a) all-rank candidate

The preceding preparation-only turn was no mathematical progress on this active goal; revalidated the original clock and resumed the existing F38 lead without restarting it. Verified exact full tuple representations in Diekert-Elder, wrote a determinant-gated reduction and finite polynomial-span decision proof, inspected the source statement and primary theorem pages, and checked explicit cancellation/rational constraints. Independent GAP replay verifies43 controlled systems (902 actual-path basis vectors,1151 transitions) and309 free-word records. A first GAP syntax failure and its zero exit code are preserved as failed; final stderr is empty. Rank-two Lee/OConnor work and the June2026 Shpilrain survey are credited. Recorded one partial candidate, bringing the tally to4 whole,3 partial,0 established novel. No full recompression implementation or F38(c) answer claimed. No agents, contacts or push; all jobs terminal.


## 2026-09-28T22:21:55.381017+00:00 — F34(a) positivity application

Developed a second application of the finite polynomial method: injective images reflect potential positivity by collapsing a spanning tree in the image subgroup graph. This yields a full decision argument for F34(a) using nonzero determinant, without claiming part(b) anew. Read original source/render/background and current primary higher-rank scope statements. Constructed270 explicit positive automorphism witnesses and3 scope controls; independent GAP checks all subgroup bases, automorphism surjectivity and positive paths. Both jobs passed with empty stderr. Recorded one further partial candidate:4 whole,4 partial,0 established novel. No new Kourovka import, agents, contacts or push. Original deadline unchanged.


## 2026-09-28T22:34:32.776894+00:00 — shared decision audit and GA1 boundary

The preceding preparation-only response made no progress on this active research goal. Revalidated the original launch/deadline and resumed gworld1 with no live recorded jobs. Wrote a shared F34/F38 audit with an explicit finite control-path bound for the polynomial stage and a counterexample to transferring the determinant reduction to F39(a). No gap found in this bounded internal reread; no outside review or new candidate count.

A GA1 surface-obstruction lead fails by Martino–ORourke's prior Z^2 actions, including the genus-three nonorientable surface. Read the relevant primary proofs and archived both author-hosted papers. General root adjunction does not satisfy the cited maximal-abelian amalgamation hypotheses. Recorded the exact remaining gap. Tally remains4 whole,4 partial,0 established novel. No agents, push or contacts; original clock unchanged.


## 2026-09-28T22:55:03.075849+00:00 — class-ten third-layer extension

Completed the class-ten gamma_8 extension: a fresh-letter quotient lemma, complete type(1,7) classification and three injectivity arguments give finite integral lifting for all leading degree-eight targets. Rank-two Python/GAP structural and group suites passed. Nine rank-three structural cases completed before a180-second timeout; the full suite is incomplete. Both initial GAP attempts lacked required exported fixtures and failed despite exit0; corrected exports preceded the successful v2 replays. Exact sources, failures and docstring-only changes are retained. Extended the same N8 partial scope; tally stays4 whole,4 partial,0 established novel. Original clock unchanged, all jobs terminal, no push/contact/agents.


## 2026-09-28T23:14:32.455430+00:00 — boundedness and fixed-subgroup scope

The preceding preparation-only response made no mathematical progress on this active goal; revalidated the original clock and resumed gworld1. The saved F38 boundedness jobs are terminal and passed with empty stderr. Archived and read the primary Lee--Ventura example, recorded the automorphism/injection/real-tree distinction, and credited prior rank-three F1(b)/F26 scope from Martino and Ventura. No candidate count changes. A concrete full-class-ten N8 lead is saved separately as unproved, with missing kernels and an exceptional obstruction to investigate. No agents, contacts or push; original deadline unchanged.


## 2026-09-28T23:36:21.500599+00:00 — all-target class-ten extension

Completed an all-target class-ten N8 candidate using six kernel arguments and an injective coupled stage followed by a quadratic obstruction. Both Python structural suites passed; rank-two GAP passed, two rank-three GAP attempts timed out without per-case confirmation. The first group run failed on a discarded class-ten conjugation term; a new tail routine retained it. Main and supplemental Python/GAP suites then passed, covering all coupled outcomes and the older degree-seven exception. Exact failed/successful sources and checks retained. Extended the same N8 partial scope, with no tally increase. All jobs terminal, original frozen inputs and clock unchanged, no agents/push/contacts.


## 2026-09-28T23:52:51.187084+00:00 — N5 integral lifting and F6 scope audit

The previous preparation-only response made no mathematical progress on the active goal. Revalidated the original gworld1 clock and empty job list. A targeted N5 audit rejects modular idempotents whose local ranks cannot lift to an integral splitting; ten composite/exact/mixed-centre controls pass. Eight relator systems agree with direct lift enumeration in Python and GAP, including four negative decisions. GAP also verifies four positive projections. Both recorded jobs passed with empty stderr; no candidate correction was required.

Archived and checked the primary Out(F3) conjugacy theorem and its prior Aut(F2) scope. The original F6 asks about Aut, so the rank-three outer theorem does not retire it. Original statement and primary theorem pages viewed. Tally remains4 whole,4 partial,0 established novel. No new Kourovka import, agents, contacts or push; all jobs terminal and original deadline retained.


## 2026-09-29T00:08:06.727074+00:00 — odd-adjoint nonlinear N8 lead

Derived a proposed all-finite-rank family in classes11,15,19,... using an odd-adjoint identity, a unique linear leading direction, symmetric-tensor recognition, a one-dimensional first kernel and a nonzero quadratic obstruction. Saved the full lead without changing candidate scope. Formal checks passed at four odd indices; a rank-two class11 Hall calculation confirms leading possibilities, kernel and obstruction. The first expanded-word GAP replay timed out without per-check confirmation; the word-verified recursive Hall replay passed with empty stderr in4.835s. A group decision implementation and separate proof/scope audit remain. Original clock and frozen corpus unchanged; no live jobs, agents, contacts or push.


## 2026-09-29T00:18:10.005364+00:00 — odd-adjoint nonlinear candidate extension

Previous turn was progress (committed N5 audit and a new mathematical lead). Revalidated the original clock and empty job ledger. Implemented rational scope recognition via exact polarization and complete integral lifting for the odd-adjoint family. Rank2/class11 suite passed4 positive,3 negative,3 unsupported controls. GAP verified4 witnesses,10 linear decisions,8 complete primitive first affine lines,8 polynomial certificates (4 empty),40 samples. Rank3 recognition passed2 positive and2 unsupported controls. All three new jobs passed with empty stderr; no new failed runs. The prior structural timeout remains recorded. Re-read/viewed original N8, audited the all-rank direction and tensor arguments, and extended the same partial candidate to classes11,15,19,... family only. Counts unchanged. Original corpus/clock unchanged, no agents/push/contacts.


## 2026-09-29T00:36:11.621403+00:00 — H4 strengthened obstruction

The preceding preparation-only turn made no mathematical progress on the active goal. Revalidated the existing gworld1 launch/deadline and terminal job state. A broader portfolio pass did not produce another candidate; recorded the F37 embedding-reflection gap without assuming it true. Developed H4 via the classical torsion-conjugacy lemma: the short finite family has enough distinct classes to force m log_2(2m)>2^n-n-1; a free product with Z gives infinite non-elementary virtually free inputs. Read the original full H4 page, viewed its statement, archived Batty/Papasoglu and read/viewed Theorem3.27. Both new recorded jobs passed with empty stderr; GAP verified class partitions and free kernels of ranks6,60. Extended the same candidate, not the count. No Kourovka import, agents, contacts or push; original clock/frozen input hashes unchanged.


## 2026-09-29T00:58:28.060374+00:00 — full intended-scope F41 candidate

The preceding preparation-only turn made no mathematical progress on the active research goal. Revalidated the existing gworld1 launch/deadline and empty jobs ledger. Resumed the saved F41 source lead and proved a polynomial-times-square-root bound for one-variable sub-multipatterns using a signed equality graph and a spanning tree. Combined KM Theorem13 with Pillay's generic-type characterization to cover every nontrivial nonprimitive orbit. Read and viewed the exact primary definitions/theorems and original F41 statement; the deeper source proofs remain imported dependencies.

Python passed46,536 positional schemes and an uncovered negative control. GAP independently passed77 exact counts. Its first run had a global-scope warning; preserved that source/log and replaced the closure with an explicit loop. The second run passed with empty stderr. Promoted the same F41 partial entry to a whole intended-scope candidate:5 whole,3 partial,0 established novel. The identity exception, spherical-limsup convention and stronger cyclic-rate nonclaim remain explicit. No new Kourovka import, agents, contacts or push; original clock and frozen corpus unchanged.


## 2026-09-29T01:27:14.020908+00:00 — wider portfolio obstruction and scope checks

The preceding preparation-only response made no mathematical progress on this active goal. Revalidated the original gworld1 clock and empty jobs ledger. Proved that locally residually solvable groups have no nontrivial perfect finitely normally generated normal subgroup, ruling out a locally free MA4 construction. Included a perfect locally free linear direct-limit control, so the proof cannot be overextended to perfectness alone. No general MA4 answer or new count.

Archived and checked Kapovich2026 compressed primitivity (C2) and Mangioni--Sisto2026 selected B4 quotients (B12). Neither theorem matches the full original question. Original statements and precise primary theorem pages were viewed. Updated their working triage rows, retaining unresolved scope. No mathematical job was run, no agents/contact/push, no new Kourovka transfer, original deadline and frozen inputs unchanged.


## 2026-09-29T01:35:30.157324+00:00 — alternate N8 central-factor proof

Developed a finite-projective-fibre argument from Shirshov-Witt and a terminating rational-point enumeration via quotient-algebra multiplication matrices. It gives another central-target decision proof, without the original Klyachko rotation lemma or its two-direction bound. The new exact solver passed13 Lie cases and2 affine controls; independent GAP/nq verified16 positive group lifts. A first rational-type conversion failure was preserved before the explicit conversion fix. Final Python and GAP runs passed with empty stderr in2.026s and2.126s.

Re-read/viewed original N8 and the exact primary Shirshov-Witt statement. The finite scheme proof and integral scaling argument were internally rechecked; no outside review or new novelty/scope claim. All jobs terminal; original clock and inputs unchanged. No agents/contact/push or new Kourovka transfer.


## 2026-09-29T02:00:26.125130+00:00 — F20 integral cover probe and N9 obstruction

Resumed the original active run with its unchanged clock and empty job ledger. Tested143 selected weight-six covers and75 known weight-five controls using integral lifted-relator lattices; no weight-seven target survives. Independent Python/FLINT replay agrees on all218 covers, with three exact boundary/torsion controls. The first GAP run failed on an immutable generating tuple; its source and partial JSON are retained. The initial SymPy replay timed out after152 completed records; its source and prefix remain explicitly incomplete. Corrected GAP runs and the final38.048-second Python replay have empty stderr.

Proved that any retract of the class-two coproduct containing the entire base and the new commutator equals the whole coproduct. This blocks a broader attempted N9 fixed-ambient encoding; it does not settle N9(a). Re-read original F20/N9 statements and viewed both actual renderings. Updated working notes, ledger and triage. Counts remain5 whole,3 partial,0 established novel. Original inputs verified unchanged; no agents, contacts, push or new Kourovka transfer.


## 2026-09-29T02:26:28.296428+00:00 — F38(c) decidable stabilizer obstruction

The preceding F20/N9 turn made concrete progress. Revalidated the original gworld1 clock and empty job ledger. Proved the necessary commensurability condition and combined classical Whitehead stabilizer generation with Handel–Mosher level-three aperiodicity to decide it. Failure produces an explicit automorphism fixing one conjugacy class and moving the other through pairwise distinct classes. A passed condition is not an answer to F38(c); its converse remains unproved.

Implemented the algorithm. Ten pair controls and four subgroup-orbit controls passed in Python. The two successful GAP replays checked seven infinite-orbit witnesses, twelve finite invariant orbits, 321 two-sided inverse pairs and 343 transitions. These are nineteen certificate fixtures, not nineteen solved problems. The first GAP run failed on an unavailable identifier despite exit zero; its exact source and output are retained. GAP does not reconstruct the complete Whitehead graphs, and the deep aperiodicity theorem remains imported.

Read the original full F38 statement/background and viewed its rendering. Archived five primary sources; precise reading limits and two actual source-page inspections are recorded in the note. No novelty asserted for this combination. Counts remain five whole-entry and three partial candidates, zero established novel results; existing F38(a) scope unchanged. No new Kourovka import, agents, contacts or push; all jobs terminal and original clock retained.


## 2026-09-29T02:30:50.784647+00:00 — precise weaker F38 comparison

The converse investigation yields an elementary quantitative clarification: finite stabilizer orbit is equivalent to comparison by an arbitrary function, and Whitehead shortening upgrades it to an effective exponential bound. Wrote the exact bound and a finite algorithm for the optimal length envelope after a passed test. The missing linear bound remains explicit; no F38(c) solution or new count. This is proof work, with no new mathematical job or agent. Only indexed excerpts/abstracts of adjacent algebraic-closure and quadratic-equation papers were consulted; they are not dependencies. Original clock and frozen inputs unchanged.


## 2026-09-29T02:52:23.718212+00:00 — full intended-scope GA3 candidate

The preceding F38 turn made progress. Revalidated the original active clock and empty jobs ledger. Completed the GA3 geometric lead: a finite-generator translation scale ensures a nontrivial real-tree collapse; abelian arc and trivial tripod fixators give boundary separation. Identity/conjugation maps extend from the finite coefficient subgroup to all G. The missing literal nonabelian hypothesis remains explicit and is not counted separately.

Read and viewed the original statement, Guirardel's general-Lambda collapse fact and CSA lemma, and the exact Rybak boundary statements/separation proof. Rybak2026 credits the boundary mechanism; no matching full Lambda-free application was located. Wrote proof and audit with precise reading limits.

Python verified160 boundary-cone separations,46 north-south cone inclusions and6400 positive images in the free-group control. Independent GAP verified6400 images,3 bad separators and49 abelian controls. The first GAP attempt failed on a reserved variable despite exit zero; exact source/log retained. Final Python and GAP jobs have empty stderr. The computations do not verify the general tree collapse. Promoted GA3 to a whole intended-entry candidate:6 whole,3 partial,0 established novel, all9 awaiting independent review. No agents, contacts, push or Kourovka import; original clock and frozen corpus unchanged.


## 2026-09-29T03:13:42.489680+00:00 — prior filling case for F38(c)

F38(c): implemented the prior filling positive case. Gupta–Kapovich Propositions4.16–4.17 already characterize filling by finite conjugacy stabilizer and decide it; Kapovich–Lustig Proposition13.8 already gives boundedness for filling pairs. The existing mod-three orbit routine now detects finite outer groups via basis classes and pair products. Six group, six word and four pair controls passed. Independent GAP replay verified7 negative witnesses,52 finite orbits,287 inverse pairs and293 transitions. Both runs have empty stderr; no mathematical failures. Non-filling pairs passing the necessary condition remain unresolved. See `research/notes/F38-filling-recognition.md`. No count increase:6 whole,3 partial,0 established novel.

Revalidated the original active clock and empty job ledger. Read original HTML/background and viewed the frozen F38 rendering; read/viewed the exact Gupta–Kapovich p20 and Kapovich–Lustig p38 statements. The proposed filling criterion was found to be prior and is explicitly excluded from new results. An NSF PDF request timed out; arXiv v4 was archived successfully. No agents, contacts, push or new Kourovka transfer. Original frozen inputs unchanged.


## 2026-09-29T03:19:17.768194+00:00 — GA1 prior negative answer

GA1 is negative in the substantive nonabelian scope by an immediate consequence of Brady–Ciobanu–Martino–O Rourke2009: x^4 y^4=z^4 in a tree-free group forces commutativity. Taking fourth roots of arbitrary a,b,ab shows every divisible tree-free group is abelian. The free Q-groups of ranks zero and one retain elementary positive actions. The original unstarred entry is retired as prior; no new candidate. See `research/notes/GA1-prior-fourth-power-obstruction.md`.

Read full original group-actions page and viewed GA1. Archived the exact primary theorem, read its introduction and main proof as text, and viewed pages1,11,13. The first browser launch lacked the documented local library path; corrected rendering succeeded. No mathematical job, agents, contact, push or Kourovka transfer. Counts6 whole,3 partial,0 established novel; original clock retained.


## 2026-09-29T03:35:05.537079+00:00 — S5 prior formal proof reproduced

The preceding preparation-only response made no mathematical progress on the active goal. Revalidated the original gworld1 clock and empty job ledger; resumed the saved external S5 source lead. Archived Jayadevan's exact public revision and verified GitHub's pre-launch push date. Full original HTML read and actual S5 rendering viewed. Official Lean4.24 release digest and all9 dependency revisions checked. Pinned project build, all298 declaration axiom audits, author completion and an independent exact S5 restatement passed in92.635s with empty stderr. Setup completed in107.098s. No failed proof job. The compiler trust flag was not treated as a full cached-Mathlib rebuild; an overstrong runner comment was corrected and its executed version retained. S5 retired as external prior work, no count added. Counts6 whole,3 partial,0 established novel; no agents/contact/push/parent transfer and original deadline retained.


## 2026-09-29T04:05:15.277767+00:00 — F28 proof simplification and full matrix lemma

The preceding preparation-only turn made no mathematical progress on the active goal. Resumed the original gworld1 clock; its saved first Lean job was terminal, failed on an import path, and was not restarted blindly. F28 now has a simpler integral proof and a Lean verification of the entire matrix-orbit obstruction: every infinite integral sequence X_(n+1)Q=QX_n with det X_0=1 starts at ±I. An invariant positive energy and odd recurrence replace the real norm and algebraic-integer arguments. The free-group/ping-pong bridge remains written mathematics. Successful final compilation and transitive axiom audit passed in8.848s; three failed versions and one warning-bearing intermediate success are preserved. See `problems/F28/matrix-lean-audit.md`. Counts remain6 whole,3 partial,0 established novel, with independent review outstanding.

Re-read full original HTML and linked F28/GA5 background, and viewed the original F28 rendering. Preserved the exact SymPy energy probe. This is internal formal verification in the pinned trusted environment, not specialist review or a cached-Mathlib rebuild. No agents, contacts, push, or new Kourovka transfer; original frozen inputs and deadline unchanged.


## 2026-09-29T04:12:26.368159+00:00 — unresolved-route scope follow-up

Archived the saved Calegari–Walker primary PDF, inspected the relevant commutator-length examples and separated their zero-determinant factorizations from the still-missing F37 primitive-length reflection theorem. An initial F37 image lookup found no file; a new original-page rendering then completed and was actually viewed. Re-viewed N3 and checked that its existing torsion example already satisfies strict monotonicity, c(U)>=|U| and superadditivity on disjoint sets. The proposed nested finite-set construction cannot cover uncountably many generators. These are route limits, not solutions or novelty claims. Broader solvable-group source queries supplied no new full answer. Counts6 whole,3 partial,0 established novel unchanged; no new mathematical job, agents, contacts, push or Kourovka transfer. Original deadline retained.


## 2026-09-29T04:28:42.557535+00:00 — C4 algorithm and bounded probe

The preceding preparation-only turn made no research progress; revalidated the original active gworld1 clock and empty jobs ledger. Completed the saved C4 implementation, reproduced the exact published nine-step trace, and evaluated45832 bounded inputs without hitting a cap. Independent GAP replay checked235 records/22501 steps and67 faithful Artin pairs; all four recorded jobs passed with empty stderr. Archived Dehornoy1997, the convergence note, and Dehornoy–Wiest2004; the latter disproves a tempting broader length conjecture but not C4. Source-reading and actual image-view limits are documented. No asymptotic theorem or new candidate; counts6 whole,3 partial,0 established novel. No agents/contact/push/Kourovka transfer; original clock and frozen inputs retained.


## 2026-09-29T04:39:33.784766+00:00 — general N8 first-correction lemma

Derived a degree-uniform support lemma in free differential Lie algebras: [T,D]=delta V forces D,V into the T-chain. Polynomial divisibility by the sum of position variables excludes outside endpoint seeds; Lyndon triangularity eliminates all outside letters. Hence every fixed nonzero type(1,q) first-correction kernel has dimension at most one. Independent Python/GAP checks cover9 common-direction systems and13 double-primitive systems, all passing with empty stderr. The latter suggest, but do not prove, a uniform quadratic obstruction. Full original N8 HTML reread/rendering viewed; exact prior Lyndon source page1822 read/viewed. No group-scope or count extension, no failed jobs, agents/contact/push or Kourovka transfer; original deadline retained.


## 2026-09-29T04:44:08.394406+00:00 — N8 uniform quadratic obstruction lead

The double-primitive gap in the preceding note is now resolved algebraically: compare first-letter components in [z,V]=[t,D], [z,W]=[t,V]. All three polynomials become cyclically invariant, which forces their Lie components of length>=2 to vanish. The explicit differential-chain embedding and highest-bracket-length projection give a nonzero final quadratic obstruction for every first exceptional type(1,q), q>2. Wrote the proposed finite integral branch algorithm. Group implementation/scope audit remain outstanding, so no candidate scope is promoted. The initial support-only note is retained as a version. Original deadline/inputs unchanged; no new process, agents, contacts or push.


## 2026-09-29T05:05:34.330407+00:00 — general N8 type-one third-layer extension

The preceding uniform-obstruction turn made mathematical progress. Revalidated the original clock, frozen inputs and job ledger. Implemented the complete type(1,c-3) third-from-last branch algorithm, with every signed leading scale and explicit unsupported other types. Internal support/cyclic/weight audit completed. Python checked21 target records; independent GAP checked7 witnesses,27 linear decisions(10 negative),5 quadratic certificates(2 empty),25 samples,13 first nullities and15 metabelian scope tests. All final jobs passed with empty stderr. The first class12 Python attempt timed out and is retained; equivalent Hall coordinates fixed the bottleneck, with24 full old/new pair-list comparisons.

Reread the full original N8 page/background and viewed the actual statement. Promoted only this recognizable arbitrary-class stratum within the existing partial N8 candidate. Counts6 whole,3 partial,0 established novel; outside specialist review and novelty remain outstanding. Saved a separate unpromoted type(2,q) structural lead. No agents/contact/push/Kourovka transfer; original deadline unchanged.


## 2026-09-29T05:13:43.813896+00:00 — N8 type-two extension and prior support credit

The type(2,q) free-chain reduction and quadratic obstruction are now written and internally audited. Six recorded Python/GAP jobs passed with empty stderr:25 target records;10 GAP witnesses,40 linear decisions(16 negative),8 quadratic certificates(4 empty),40 parameter samples,18 first nullities and19 scope controls. The class11 exceptional line, signed nonprimitive scales, both-type dispatch and higher-type exclusions are covered. Promoted only the combined p<=2 third-from-last stratum, in every finite rank and class c>=8, within the same partial N8 candidate.

Archived Altassan2013 and viewed precise pages19/24. Its prior inner-solution theorem, credited to Remeslennikov--Stohr2007, already implies the support lemma via Lazard embedding; recorded the reduction and updated earlier type1 credit. Journal full PDFs were inaccessible and not described as read. No novelty asserted for the support lemma or certified for the group-stratum theorem. Counts6 whole,3 partial,0 established novel. No failed type12 jobs, agents/contact/push/Kourovka transfer; original clock retained.


## 2026-09-29T05:30:25.564544+00:00 — wider portfolio source audit

The preceding N8 turn made progress. Revalidated the original active clock and empty jobs ledger. Read/viewed the exact GA5/E6/G7 statements and relevant primary pages. Retired GA5(c) existential scope as prior rank2 binary action, retaining its normal-subgroup distinction from F28. Wrote a numerical control and elementary Folner-ball repair for the G7 source inference; neither solves G7. E6 strong conciseness does not imply completion EN. The first multi-ID render invocation failed because the script takes one ID; both single-ID reruns succeeded and were viewed. No mathematical jobs, agents, contact, push or Kourovka transfer. Counts6 whole,3 partial,0 established novel.


## 2026-09-29T05:44:55.353545+00:00 — uniform N8 third-from-last layer

A graded-tail subalgebra makes C and each first correction U free generators, allowing the prior inner-solution theorem for arbitrary leading weights. This yields the uniform kernel bound and quadratic obstruction; equal weights are injective and adjacent weights have exact finite Nielsen residues. Full original N8 HTML/background reread and actual statement viewed; exact Shirshov/inner-solution pages viewed again.

Implemented every leading type and promoted this layer within the same partial candidate after audit. Final Python group suites cover34 targets; GAP independently verifies19 witnesses,101 linear decisions(45 negative),2 polynomials,10 samples,39 nullities,11 Nielsen periods. Separate native Python/GAP weighted-Lie checks verify7 kernels and4 composite-coefficient obstructions. All8 final jobs pass with empty stderr. Two initial fixture expectations were wrong: equal-weight perturbations had solutions. Preserved the failures and verified the corrected positive witnesses in GAP; solver unchanged. Counts6 whole,3 partial,0 established novel; no agents/contact/push/Kourovka transfer and original clock retained.


## 2026-09-29T06:14:32.951506+00:00 — uniform N8 fourth-from-last layer

The preceding third-layer turn made progress. Revalidated the original active
clock and exact state. A finite first-parameter reduction followed by a
joint integral tail gives every fourth-from-last leading type. The explicit
class-eleven control demonstrates failure of the arbitrary-particular
quotient-lift rule. Final Python suites cover41 targets; GAP independently
checks18 witnesses,148 integer decisions(72 negative),18 polynomials(6 empty),
90 samples,56 nullities and20 Nielsen periods. All six final jobs pass with
empty stderr. Preserved two earlier successful rank-two runs and three
rank-three180second timeouts; unchanged v4 completes under900second allowance.
A diagnostic profile identifies Hermite reduction, correcting the tentative
nearest-plane attribution; the exact shortening routine passes42 comparisons.

General pre-Nielsen offset and consecutive-kernel lemmas are written, with
six independent weighted-Lie kernel/successor checks and five quadratic
obstructions. A post-Nielsen kernel-dimension-three control preserves the
scope boundary. These suggest further layers but no further group scope
is promoted. Full original N8 statement/background and rendering were
checked during the derivation. Counts6 whole,3 partial,0 established novel;
no agents/contact/push/Kourovka transfer; original deadline retained.


## 2026-09-29T06:39:06.744044+00:00 — F38(c) finite common-filling-carrier implementation

The preceding N8 turn made progress; revalidated its committed state and
original active clock. Wider portfolio searches left the stated scope gaps
open. Implemented a complete finite principal-fringe search for a common
filling carrier, including independently conjugated input classes. Integrated
it as a positive prior-theorem branch after the negative stabilizer and
ambient-filling tests. Failure of this sufficient test remains unresolved.

Four mathematical jobs passed with empty stderr. Python checks29 quotient
graphs against all partitions of five small cycles,9 carrier pairs and5
integrated cases. GAP independently checks graph ranks/edge-loop subgroups,
7 positive carrier identities,48 finite invariant orbits,7 infinite-orbit
witnesses,462 inverse pairs and464 transitions across the two replays.
The cyclic-HNN vertex examples are ambient non-filling, and Lee's rank-two
positive example correctly remains unresolved by this test. Archived/read/
viewed the exact prior fringe theorem. No new candidate, specialist review,
agents/contact/push or Kourovka transfer;6 whole,3 partial,0 established
novel and the original deadline retained.


## 2026-09-29T07:03:56.815798+00:00 — fifth/sixth-layer N8 lifting completed

Implemented the retained general-offset scheme with complete integral affine
lines, isolated coupled points and joint final tails. Wrote the uniform proof
and audited the d>=4 boundary. Five final suites/ten mathematical jobs pass,
including independent GAP replay of44 witnesses,424 integer decisions,227
nullities,40 Nielsen periods,25 coupled systems and27 quadratic certificates.
The targeted derivative correction gives three independently verified step6
lines, with two empty quadratics and one positive branch. Rank-three first
suite failed only its negative-fixture coverage assertion; retained its full
sources/results and added a metabelian-image negative control. No guessed
negative was forced and no valid positive was discarded. Actual exit codes,
empty successful stderr and raw output hashes checked.

Also read the original O6 HTML/background and Linton publisher Theorem5.6,
its proof and Corollary5.7: a reduction, not a full solution. Fresh Chromium
capture failed from missing libatk; an attempt to download the dependencies
also failed because the local apt package lists are absent. O6 visual audit
is explicitly pending; no solution/scope count follows from that check.
The whole195-entry objective, original clock and local-only commit policy
remain active. Counts6 whole,3 partial,0 established novel.


## 2026-09-29T07:32:23.155731+00:00 — F41 audit, wider scan and MA7 finite-ring construction

Reread the exact F41 model-theoretic dependencies and viewed their four
retained pages. The parameter-free formula is essential for both orbit
invariance and finite-translate genericity; no gap found in this pass.
Singleton and finite-index-union controls explain two possible misuses.
Deep imported results and novelty still await outside review.

Broader revisits of M4, FP9, GA4, S4/S7, F25/F39 and the growth/automatic
portfolio did not yield a new full solution. No scope was promoted from
these searches. MA7 yielded an explicit finite noncommutative-ring
construction satisfying even n>=3 and nonscalarity modulo every proper
ideal. A degree-one quotient and bivector-rank bound exclude all proposed
commutator factors; a343-transvection certificate is independently checked
in native GAP algebra arithmetic. Python0.320s/GAP2.327s, exit0, empty
stderr. The short website question is already prior by Dennis--Vaserstein
1988, so no new GroupWorld candidate is counted. Ring commutativity and
stable-size variants remain separate; related construction novelty unknown.

The O6 rendering failure was an omitted local library path: dependencies
were already present. Restored invocation, captured/viewed O6 and MA7,
and documented the command. Publisher/RG403 and expired-certificate source
downloads are recorded without claiming access. No failed mathematical
run, agents, contact, push or old-research transfer. Original clock and
counts6 whole,3 partial,0 established novel retained.


## 2026-09-29T07:52:51.723191+00:00 — A5 verified as prior; effective M3 reduction

The preceding preparation-only turn rechecked corpus readiness but made no
progress toward the active solving goal. Revalidated the original active
clock and clean research checkout; resumed here without resetting time.

Read Jayadevan's A5 preprint and selected formal modules, archived its
version-pinned arXiv source, and viewed the original A5 statement plus
PDF pages1/5. The unchanged author build and1624-declaration axiom audit
pass. Our independent expanded enumeration/certificate statements also
pass. Two failed wrapper runs are preserved: missing archive executable
permission, then a dependent-type rewriting error in our restatement
after the author's checks had passed. Corrected statement verified in
8.749s; author sources unchanged. No complete cache/kernel rebuild claim.

A5 is now retired as external prior. For M3, combining A5 with the precise
Bieri-Strebel covering theorem supplies an effective ordinary presentation
of G/G'' on solvable inputs, plus normal generators of G''. Wrote the
termination/soundness proof and the remaining kernel-triviality gap.
GAP verifies an S4-to-S3 control in1.825s. Original M3 rendering viewed.
Neither this reduction nor a word-problem-oracle corollary solves M3.

Broader source revisits found no further full resolution; already recorded
F15/F42 results remain prior. Frozen input hashes and actual log hashes
verified. All jobs ended. Counts6 whole,3 partial,0 established novel;
original48hour clock and195-entry objective retained; no agents or push.


## 2026-09-29T08:23:41.895156+00:00 — N3 profile-repair obstructions certified

The immediately preceding preparation-only turn made no progress toward
the active solving goal. Revalidated the original active clock and clean
research worktree and resumed here. Preparation export and parent Kourovka
checkout were not modified.

Derived an exact equivalent criterion for a torsion-free cover: a coherent
enlarged pseudo-free profile must kill all its torsion in the canonical
map to the target. Rechecked the original full HTML and actual rendering.
The arbitrary-cardinality requirement remains explicit.

A class-six profile probe found surviving torsion when pair bounds rise
from2 to3. Extracted a538-letter/11-factor central order-two witness and
a three-factor square identity. A mod-two additive envelope failed; an
exact multiplicative echelon certificate instead proves nonmembership,
checking180 rows,15 central commutators,1080 signed conjugates and240
relator differences. Standard Python and independent GAP both pass.

The separate uniform increment, including full bound6 to7, also fails.
A GAP preimage had277662 letters; attempted shortening hit its preset
memory limit (actual exit0, missing success marker, correctly failed).
The old compact prefix alone has infinite order there. Constructed an
independent central correction via the full480-generator integer normal
lattice: cube the prefix and append56 central Hall factors. The resulting
word has an explicit24-factor square identity and a nontrivial target
image. Final standalone5.989s/GAP13.413s, both exit0 and empty stderr.

The first broader probe timed out after180s at class8; no class8 result
or pair-bound4 result is inferred. Earlier syntax-warning versions and
failed constructor sources are retained. All jobs have terminated.
Maximum two cores/18GB combined reservations; no agents, contact or push.
Counts remain6 whole/3 partial candidates,0 established novel. Neither
profile example is a counterexample to N3, whose finite target has an
obvious free nilpotent cover. Original48hour deadline unchanged.


## 2026-09-29T08:45:47.947218+00:00 — F25 equal-frequency degree-sorting obstruction

The preceding preparation-only turn did not advance the active solving
goal. Revalidated the existing run, original deadline and current worktree;
continued in gworld1 without changing the preparation export or parent.
The previously downloaded Lee0311410v3 source was retained and inspected.

Read the original F25 statement/background and actual screenshot; archived
Lee0401269v3, separated cyclic/ordinary counting and checked the frequency
hypotheses. A bounded exact probe completed35 records:26 complete plateaux,
9 nonminimal words with shortening moves, no truncation. Distinct-frequency
control has112 vertices reached by degree-sorted chains.

Extracted a12-letter balanced-frequency word whose type-II plateau is a
12-cycle with alternating degrees2,3. No basepoint or generator order
permits sorted chains to reach more than4 vertices. A two-move3,2 path
supplies an explicit failure of the proposed extension of Lee Lemma3.1.
The full signed-permutation closure has144 cyclic words. A power argument
gives arbitrarily long examples, still with constant cyclic orbit size.

Independent GAP checked all96 moves at12 vertices,1152 exact substitutions,
48 nonloop directed move representatives,72 start/order reachability sets,
the cycle and signed-permutation closure. Final run1.974s, empty stderr,
exit0, marker present. Earlier passing versions and sources retained; v2
adds structural checks. All five jobs terminal,1 core/4GB each.

Wrote the exact proof and limitations; this neither solves F25 nor refutes
Lee under its actual hypotheses. No new candidate or novelty count. The
original6 whole/3 partial/0 established-novel tally and48hour clock remain.
No subagents, author contact or push.


## 2026-09-29T09:14:49.432439+00:00 — F38 finite envelopes and primitive-power classification

Returned to the unresolved portfolio. M4 countable-rank and S4 higher
solvable-class leads still have gaps; no new claim was made for them.
Read the original F38 statement/background and viewed its actual rendering.
No frozen input or experiment clock changed.

The finite stabilizer-orbit test now has an exact interpretation: it
decides existence of any finite-valued one-way length envelope. A finite
Whitehead pair graph computes prefixes and gives an explicit exponential
bound. GAP reconstructs five graphs and checks9226 directed edges,
23188 exact substitutions and two negative witnesses. No linear-bound
conclusion is inferred from the exponential estimate or finite prefixes.

Derived an elementary classification for primitive powers in rank>=3.
An exact Nielsen-iteration formula and a product of three two-vertex
graphs show that a fixed family of r twists detects every non-power.
The transported negative witness fixes one input and gives linear
unbounded growth of the other. Independent GAP checks7274 formulas,
58192 substitutions,18 normalizations and the graph intersection.
Rank2 is excluded by Lee's prior positive example. General part(c)
remains unresolved. Existing broader tools already decide this family;
the new result is its explicit elementary classification.

All four jobs passed, actual exit0, empty stderr, marker present; each
reserved one core/6GB and all finished in under3seconds. No jobs remain.
Source snapshots and manifests accompany both new proof packages.
Targeted primitive/power literature searches found no explicit match;
novelty remains unverified. Counts stay6 whole/3 partial/0 established
novel. No subagents, external contact, push, or imported Kourovka argument.


## G9 effective approximation and finite growth bounds (2026-09-29T09:50:38.335166+00:00)

After a broader unsolved-portfolio scan, developed a bridge unfolding
argument that is injective at the level of metabelian flows once its
strictly decreasing span list is retained. This yields an explicit
all-rank effective modulus for approximating the standard growth constant.
The proof does not claim efficiency or an exact closed value. Ordinary
ball counts were independently reproduced in GAP through the first genuine
metabelian collisions. Python checked17121 unfolding recoveries; GAP
checked243 samples/controls and native Laurent representations.

Fixed-height codes through18 letters give only2.622033. A new atom alphabet
with arbitrary heights yields2.658596558: C++ and Python counts agree,
and GAP independently verifies every one of21483 words and its distinct
native Magnus representation. A separate648-relation avoidance automaton
with1968 states supplies upper2.943737759. GAP reconstructs all7872
transitions and verifies1968 exact comparison inequalities.

The full statement and background were read, actual original paragraph
viewed, and prior flow/unfolding sources credited. The site's quoted
2.63815853034 is only a comparison: the cited Guttmann--Conway preprint
Section5.3 discusses estimates, not a rigorously enclosed decimal.
Loh and Bodart--Osin general upper semicomputability does not alone give
our two-sided approximation. Novelty remains unverified.

Two early GAP language errors are preserved with their exact source
versions; the runner correctly rejected both despite zero exit status.
All successful checks have empty stderr and required markers (compilation
jobs use actual exit status). Jobs were sequential, one core each,
maximum16GB reservation and70.855seconds runtime. No jobs remain.

Count now6 whole candidates,4 partial candidates,0 established novel.
The separate preparation checkout and parent Kourovka repository remain
untouched. Original48hour clock retained, no subagents, push or contact.


## G9 extension to all free solvable derived lengths (2026-09-29T10:02:45.925478+00:00)

The reflection/unfolding proof extends to flows on nonabelian quotient
Cayley graphs, provided R lies in the first-generator height kernel and
is invariant under its inversion. Explicitly retaining left translations
and ordered relative endpoints gives the same modulus for F/R-prime.
For R=F^(d-1), recursive flow equality supplies a uniform word-problem
algorithm; the growth constant is therefore computable uniformly in rank
and derived length. This is a candidate supplementary theorem, with no
new entry count or established novelty.

Python checks1998 recoveries in ranks2/3 and derived lengths2--4,
including controls of lengths4,20,84 distinguishing successive quotients.
Independent GAP uses native Laurent Magnus rows for the noncommutative
deck group and verifies68 outer flow recoveries plus3 derived controls.
One unsupported symbolic-ordering failure is retained; equality-based
comparison passes. Deliberately reversed translation/reflection orders
produce wrong recovered flows on31/12 fixtures, respectively. Four jobs
terminal, one core/8GB each, all under5seconds. Prior source theorem and
reading limits are in the proof/audit; old G9 manifests remain unchanged.
Counts6 whole/4 partial/0 established novel; original deadline unchanged.


## N8 weighted-orbit extension (2026-09-29T10:29:07.089788+00:00)

Returned from the broader portfolio scan to an earlier weighted-free
subgroup lead. Equal leading factors, and unequal factors whose heavier
term survives the graded-tail abelianization, can be included in a
homogeneous free Lie basis. Rational unipotent substitutions acquire
integral powers on the full subgroup lattice. This supplies finite
integral pair-orbit representatives and an arbitrary-class branch
decision argument. In particular, every degree-three target is covered.
General arbitrary-class targets remain unresolved.

Exact rational exponential-series tests construct46 automorphisms; GAP
independently checks the actual subgroup homomorphisms,2412 inverse-image
equalities and92 commutator witnesses. A dependent-generator substitution
is rejected independently. Initial nonprimitive case reached the8! bound
and returned inconclusive; source and partial evidence retained,12! bound
succeeds with maximal selected power9!. Full finite-union algorithm is
proved but not implemented. Homogeneous Shirshov source and original N8
rendering were re-viewed. Novelty and specialist review remain pending.

All9 jobs terminal, maximum simultaneous5cores/40GB, longest44.065seconds.
The main GAP run has five retained parser warnings and no runtime error.
No imported Kourovka material, subagents, pushes or contacts. Original
48hour clock unchanged; counts6 whole/4 partial/0 established novel.


## F38(c) full candidate from graded shortening (2026-09-29T11:00:34.010172+00:00)

The earlier finite-stabilizer necessary condition is now sufficient by a
quantitative relative-shortening argument. For a word in no proper free
factor, adjoin z and grade by <u,z>. Minimizing under the pointwise
parameter fixer and assuming superlinear size would yield a flexible
graded sequence. Its explicit tripod and injectivity make its limiting
quotient faithful, contradicting Sela Lemma 10.4. Proper free factors and
the exceptional rank-two primitive case are handled separately.

The exact primary definitions, local lemma proof and printed pages 89--90
were read/viewed; the inequality uses 2^m. The bounded-parameter relative
shortening result was not substituted for the graded theorem. Novelty
and independent specialist correctness review remain pending.

Python checks ten two-sided and five directed cases, including rank and
quantifier controls. Independent GAP now reconstructs 12 complete minimum
Whitehead graphs, 148 vertices, 20948 edges and 1058 loop maps; it checks 15 finite
orbits, 1150 loop/orbit transitions and 6 negative level-three witnesses.
Both languages also check 2376 factor-twist records and 234 rank-two bounds.
The two jobs pass with empty stderr in 1.223s and 8.447s, sequentially at
one core / 8 GB. Finite checks do not verify the deep shortening theorem.

Proof, audit, implementation and immutable certificate are under F38.
F38 moves from partial to whole-entry candidate: 7 whole / 3 partial / 0
established novel. Part (b) and rank-two decisions retain their prior
credits. No subagents, imported Kourovka mathematics, pushes or contacts;
parent/preparation repositories untouched and original clock retained.


## N3 restricted nested-cover construction (2026-09-29T11:26:00.871224+00:00)

A nested construction avoids the earlier overlapping-profile torsion
obstruction for groups with a countable ascending nilpotent exhaustion.
The proof retains free abelian lower central factors using integral
augmentation quotients, PBW and an explicit free Lie coproduct argument.
The countable case is prior Romanovskii1969, confirmed in the editors'
archived eighteenth-edition Notebook. The unrestricted N3 remains open
here; this is supplementary audit work, not an added candidate.

Exact Hilbert-series predictions and independent GAP ordinary-relator
computations agree on13 stages in5 chains, including rank4/class5.
Retractions, all lower central factors and torsion are checked. The
negative control has a torsion-free factor but a mixed commutator of
order4, so mere factor torsion-freeness is insufficient. Both recorded
jobs pass; GAP took74.015seconds at1core/8GB, with two harmless parser
warnings and an imprecise print label subsequently cleaned up. Executed
source retained; no mathematical rerun needed for reporting edits.

Sources, reading limits and proof are in N3-nested-cover.md, with a
hash manifest. Failed alglog TLS retrievals are noted; the editor's
Manchester PDF was obtained instead. No imported Kourovka mathematics,
subagents, pushes or contacts; original deadline unchanged. Counts
remain7 whole/3 partial/0 established novel.


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


## Diagonal separation lead (2026-09-29T18:16:54.901693+00:00)

An elementary polynomial averaging argument now proposes a separating
functional for the first exceptional quadratic in arbitrary N8 blocks.
The written coordinate audit covers fixed-prefix normalization, affine
Malcev coordinates, the full correction image and all later columns.
General N8 scope is still unadopted; adopted counts stay8 whole/2 partial/0
established novel. See N8-diagonal-separation-lead.md and its finite audit.

Independent Python and GAP reconstruct44 complete Lie spaces with identical
ranks. A new actual class17 group fixture has59 Hall coordinates, a full
24-by-22 integer block, first parameter step2, and obstruction ranks11,12,13.
Thus its later column is nonzero but does not absorb the first quadratic.
Native GAP verifies all group columns, the entire lattice, all quadratic
coefficients (seven samples of rank-six interpolation), and two witnesses.
Separate arithmetic and family replays pass. Nine runs are terminal: seven
pass, two fail before mathematics; the missing-source and obsolete-option
failures are retained. Peak reservation2cores/8GB. No push or contacts.
