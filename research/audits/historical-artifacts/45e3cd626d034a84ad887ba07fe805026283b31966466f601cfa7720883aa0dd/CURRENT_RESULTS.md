# Current candidate results and review guide

Snapshot: **30 September 2026, 05:57 UTC**. The experiment is still active;
its deadline is **30 September 2026, 10:04:49 UTC**. This is an interim
index, not the final report.

There are **ten whole-entry coverage candidates, two partial-entry
candidates, and zero established novel results**. “Whole-entry” means
that the proposed arguments, together with explicitly credited prior
answers, cover the entry's intended scope. It does not mean ten entirely
new theorems. Correctness and novelty require independent specialist
review. All proof audits below were conducted by the same research agent;
an independent GAP reconstruction is a separate computational check,
not an independent mathematical referee.

## Ten whole-entry coverage candidates

| Entry | Current proposed result | Controlling argument and audit | Prior scope and principal limits |
| --- | --- | --- | --- |
| F28 | An isomorphism between index-two subgroups of a rank-two free group has no nontrivial subgroup H with f(H) contained in H. No finite-generation or normality assumption on H is needed. | [Proof](../problems/F28/proof.md), [audit](../problems/F28/audit.md), [matrix formalization](../problems/F28/matrix-lean-audit.md). | The Lean result verifies the matrix argument, not the complete free-group theorem. Novelty unverified. |
| N5 | A uniform algorithm decides nontrivial direct decomposability of a finitely presented group promised to be finitely generated nilpotent, including torsion, and constructs factors. | [Proof](../problems/N5/proof.md), [audit](../problems/N5/audit.md), [integrality audit](../problems/N5/integrality-audit.md), [rational Lie implementation](../problems/N5/rational-lie-audit.md), [class-two pipeline](../problems/N5/class2-pipeline-audit.md), [mixed class-two pipeline](../problems/N5/class2-mixed-audit.md), [finite-presentation interface](../problems/N5/class2-input-audit.md), [higher-class input](../problems/N5/general-malcev-input-audit.md), [rational support kernels](../problems/N5/general-support-audit.md), [general native pipeline](../problems/N5/general-pipeline-audit.md), [general presentation command](../problems/N5/general-fp-audit.md). | The torsion-free decision is prior work. Rational decomposition is credited prior machinery; its Lie-algebra stage is now implemented and separately checked. The complete pipeline now accepts finite presentations under the nilpotency promise with no supplied class bound, includes torsion, and returns factor words in the original generators. Twelve native controls, fifteen presentation conversions and five standalone commands pass, including negative integral gluing and class-four cases. The promise, written completeness arguments and trusted algebraic dependencies remain essential; no practicality claim is made. |
| M0 | In every finite rank, an endomorphism of a free metabelian group that preserves primitive elements is an automorphism. | [Proof](../problems/M0/proof.md), [audit](../problems/M0/audit.md), [terminating witness constructor](../problems/M0/kronecker-construction.md), [constructive Jacobian audit](../problems/M0/flow-inverse-audit.md). | Ranks at most two are prior. Bachmuth's inverse-function theorem is credited and now also derived constructively by integral flows in the supplement. Its finite-field witness bounds are effective, without a practical complexity claim. |
| H4 | There is no uniform polynomial-time conversion of arbitrary finite presentations of hyperbolic groups into explicit finite Dehn presentations, even allowing a change of generators. | [Proof](../problems/H4/proof.md), [audit](../problems/H4/audit.md), [infinite-input extension](../problems/H4/infinite-input-proof.md) and [audit](../problems/H4/infinite-input-audit.md). | The lower bound also has infinite, non-elementary virtually free inputs. It concerns ordinary explicit output words; compressed output and a torsion-free input restriction are not covered. Classical bounds and related earlier work are credited. |
| F41 | For a nontrivial nonprimitive word in rank r at least two, its automorphic orbit has ball growth at most a polynomial times (2r−1)^(n/2). | [Multipattern proof](../problems/F41/multipattern-proof.md), [audit](../problems/F41/multipattern-audit.md), [follow-up](../problems/F41/followup-audit.md), [dependency boundary](../problems/F41/dependency-boundary-audit.md). | This gives the requested exponential gap, not the stronger conjectured word-dependent growth rate. Identity and rank-one cases are treated separately. The proof depends on the arbitrary-definable-set multipattern theorem of Kharlampovich–Myasnikov and Pillay's genericity theorem. |
| GA3 | Every nonabelian group acting freely without inversions on a Λ-tree has the stated discrimination of its free square by conjugating one factor; arbitrary generation and arbitrary ordered abelian Λ are allowed. | [Proof](../problems/GA3/proof.md), [audit](../problems/GA3/audit.md), [elementary separator](../problems/GA3/elementary-separator-supplement.md). | The nonabelian restriction is necessary: the literal statement is false for nontrivial abelian groups. The general collapse imports substantial tree-action results. The supplement derives the separator directly from axis translations and finite endpoint avoidance; free-group fixtures do not verify the general collapse. |
| F38 | Uniform decisions for translation equivalence (a) and bounded translation equivalence (c), in every finite rank. For (c), the proposed criterion is commensurability of the oriented conjugacy stabilizers in Out(F_r). | [(a) proof](../problems/F38/part-a-proof.md) and [audit](../problems/F38/part-a-audit.md); [(c) proof](../problems/F38/bounded-proof.md), [audit](../problems/F38/bounded-audit.md), and [canonical normalization](../problems/F38/normalization-supplement.md). | Part (b) and rank-two decisions are prior. Part (a) imports a full EDT0L solution-relation construction, not implemented here. Part (c)'s essential sufficiency step imports Sela's graded shortening theorem; finite tests do not establish that application. The ambient-automorphism quantifier is retained. |
| F34 | A uniform algorithm decides whether a word can be made positive by an automorphism, in every finite rank. | [(a) proof](../problems/F34/part-a-proof.md), [audit](../problems/F34/part-a-audit.md). | Rank two and the stability statement in (b) are prior. The same unimplemented full EDT0L construction as F38(a) is imported. The identity convention is stated explicitly. |
| N8 | An algorithm decides a single commutator equation [x,y]=g in every finite-rank free nilpotent group, in every finite class, and constructs solutions. | [General proof](../problems/N8/general-proof.md), [general audit](../problems/N8/general-audit.md), [limited analytic formalization](../problems/N8/averaging-lean-audit.md), [division-free positional bridge](../problems/N8/polynomial-bridge-lean-audit.md), [full-block implication](../problems/N8/block-separation-lean-audit.md), [concrete convergent transfers](../problems/N8/sweep-convergence-lean-audit.md). | This is the current candidate for (b); the negative answer to (a) for general nilpotent groups is prior. Earlier class-bounded notes are intermediate stages. The full arbitrary-rank algorithm is not implemented; all-rank structural lemmas remain a central review requirement. |
| N9 | The retract problem is undecidable in one fixed finitely generated torsion-free class-two group, already on two-generator isolated Heisenberg subgroups with primitive images in both graded layers. | [Proof](../problems/N9/proof.md), [audit](../problems/N9/audit.md), [isolated-input supplement and source audit](../problems/N9/isolated-inputs-and-prior-scope.md). | The class-wide undecidability theorem and the positive free-nilpotent case (b) are prior. Potential new scope is one fixed ambient group. The construction imports DPRM; the universal presentation is not numerically expanded. Lean verifies an integer normalization lemma, not the full reduction. |

## Two partial-entry candidates

| Entry | Current proposed result | Controlling argument and audit | What remains |
| --- | --- | --- | --- |
| G9 | The standard growth constant of a free metabelian group is computable, with an explicit approximation modulus in every finite rank. Certified rank-two bounds are 2.658596558 ≤ λ₂ ≤ 2.943737759. The method extends to free solvable groups. | [Flow proof](../problems/G9/flow-growth-proof.md) and [audit](../problems/G9/flow-growth-audit.md); [solvable extension](../problems/G9/solvable-extension-proof.md) and [audit](../problems/G9/solvable-extension-audit.md). | The exact growth constant requested by the entry remains undetermined. Fine-precision computation is not demonstrated. The extension is not a second problem count. |
| B9 | There are countably infinitely many special braids in every B_N with N at least five. Deductions from Dehornoy's prior structure give exact counts 1, 2 and 4 in B₁, B₂ and B₃. | [Infinite-family proof](../problems/B9/infinite-family-proof.md) and [audit](../problems/B9/infinite-family-audit.md); [small-strand proof](../problems/B9/small-strand-proof.md) and [audit](../problems/B9/small-strand-audit.md). | In B₄, only the exponent-two sector remains unclassified; at least ten special braids are known in total. The [positive-parameter reduction](../problems/B9/positive-parameter-reduction.md), [strand restriction](../problems/B9/exponent-two-parameter-reduction.md) and [excluded families](../research/notes/B9-family-return-obstruction.md) do not exhaust that sector. |

For B9, the [three-strand underlying exclusion](../problems/B9/three-strand-underlying-exclusion.md)
now treats every special pair in its stated sector, including the unknown
exponent-two first braid. An additional terminal parameter of total exponent
two would require underlying strand numbers at least five and four. The
[positive underlying exclusion](../problems/B9/positive-underlying-exclusion.md)
also rules out every positive special second underlying braid beyond B2,
without a strand bound. Any remaining input in this sector has a nonpositive
second underlying braid. The [four-strand reduction](../problems/B9/four-strand-underlying-reduction.md)
leaves one necessary permutation case there, requiring a second input
outside the ten known B4 examples. It excludes all known inputs for
arbitrary special first underlying braid. The B4 sector is still not exhausted.
The [higher-strand permutation check](../research/notes/B9-general-permutation-obstruction.md)
records why that permutation pattern cannot simply be extended: explicit
special lifts pass the three-position permutation test while their
parameters need seven strands. They give no new B4 braid.

## How to review the evidence

Start with the controlling proof and its audit, then follow its certificate
and source links. They distinguish a universal argument from finite
examples, record conventions and hypotheses, and retain failed runs.
Certificate manifests under [research/certificates](../research/certificates/)
bind particular artifact versions; an older manifest is not a blanket
certification of later supplements. Some candidates have several manifests
or directly cited check records rather than one overall manifest.

There are no complete formal verifications of these twelve candidate
theorems. The Lean work for F28, F34/F38, N8 and N9 checks explicitly delimited parts.
The [shared F34/F38 span audit](../problems/F38/shared-span-lean-audit.md)
verifies universal reachability and termination implications, while leaving
the concrete polynomial lift and equation-solution construction outside Lean.
Separate reproduced Lean proofs for the prior A5 and S5 results are not
new solutions from this experiment. In particular, GAP tests of selected
nilpotent groups, finite word graphs or polynomial examples cannot establish
all-rank structural claims or the hypotheses of an imported theorem.

The [F31 prior-result audit](../research/notes/F31-prior-construction-audit.md)
checks Lei--Zhang's counterexample construction and its graph-embedding
rank argument. It is credited prior work, with no candidate-count increase.

N8's [assembled analytic theorem](../problems/N8/analytic-assembly-audit.md)
now proves constancy directly from the positional delta/diagonal functional
identities and continuity. It includes cyclic relocation and the concrete
energy argument, with no convergence assumption. The subsequent
[polynomial interface](../problems/N8/positional-polynomial-audit.md)
checks explicit diagonal substitution and rational coefficient constancy
from polynomial identities. The [ordered-word dictionary](../problems/N8/word-dictionary-audit.md)
now connects this to the actual free associative algebra, its global
derivation and the two restriction identities. The [Lie exception](../problems/N8/lie-exception-audit.md)
now proves scalar-power exclusion and separation inside the generated Lie
subalgebra. Its identification with an abstract free Lie algebra, the
homogeneous projections, group application and complete algorithm remain
outside Lean. The [weighted word block](../problems/N8/weighted-block-audit.md)
now checks the weight-based exception, separation from the full actual-word
correction span, and the two-value consequence from concrete block equations.
The [group-block supplement](../problems/N8/group-block-supplement.md)
now spells out their production from Hall/BCH coordinates, including the
sign, weight and full-column identities. That bridge remains a written
proof obligation outside Lean.

The [projective leading-pair implementation](../problems/N8/projective-leading-pairs-audit.md)
now retains every signed integral scale. A class-five group example shows
why that matters: both primitive branches fail while four nonprimitive
branches succeed. GAP separately confirms all eight lift decisions.
This implements the general proof's first stage, not its full recursion.

The largest shared dependency is the full solution-language construction
used by F34(a) and F38(a). Other priority review points are F38(c)'s graded
shortening application, N8's uniform leading-pair and exceptional-parameter
arguments, F41's arbitrary-set multipattern input, GA3's general Λ-tree
collapse, and N9's passage from a fixed Diophantine circuit to one fixed
ambient group. These are review priorities, not assertions of detected
errors. Their current internal audits are linked above.

Known answers, rediscoveries, failed strategies and unresolved leads remain
in the [triage](../research/triage.csv), [claim ledger](../research/claims.jsonl),
[literature ledger](../literature/LEDGER.md) and [progress history](PROGRESS.md).
F11 and F42 are explicit examples of rediscoveries excluded from the tally.
The source catalogue has 195 entries, not 195 currently open problems; its
stars and Hall of Fame links do not settle every subpart's present status.

Historical statements such as “N8 is partial” or earlier candidate counts
remain in dated notes and immutable audit artifacts. This index identifies
the current scopes without rewriting that history. Later corrections must
be recorded explicitly in the claim ledger and reflected here. No external
publication, contact with authors, or Git push has been performed.

The closing audit has begun. Its current same-agent proof rereads cover
[N5](../research/audits/N5-closing-proof-reread.md),
[F34/F38](../research/audits/F34-F38-closing-proof-reread.md), and
[F41](../research/audits/F41-closing-proof-reread.md), together with
[N8](../research/audits/N8-closing-proof-reread.md),
[GA3](../research/audits/GA3-closing-proof-reread.md), and
[N9](../research/audits/N9-closing-proof-reread.md), followed by
[F28](../research/audits/F28-closing-proof-reread.md),
[M0](../research/audits/M0-closing-proof-reread.md), and
[H4](../research/audits/H4-closing-proof-reread.md).
The partial boundaries are also checked for
[G9](../research/audits/G9-closing-proof-reread.md) and
[B9](../research/audits/B9-closing-proof-reread.md).
No new gap was identified in those passes; their imported-theorem and
implementation limits remain explicit. Artifact reconciliation is recorded
in [the checkpoint](artifact-checkpoint-2026-09-30.md), and remaining work
in [the closing plan](CLOSING_AUDIT_PLAN.md). These are interim checks,
not a completed experiment or outside mathematical validation.

The [current scope ledger](RESULT_SCOPE.md) separates entry coverage from
named-part answers and credited prior parts. Its JSON companion retains
all 195 catalogue IDs, including uncounted and status-unverified entries.

The [interim resource/process checkpoint](resource-process-checkpoint-2026-09-30.md)
records the requested-limit peaks and actual process observation. It is
not the final deadline closeout or a measurement of peak memory use.

The [expanded artifact checkpoint](artifact-checkpoint-expanded-2026-09-30.md)
includes the closing manifests and historical scope versions: all 6,731
examined bindings have exact available content. Final deadline reconciliation
remains outstanding.
