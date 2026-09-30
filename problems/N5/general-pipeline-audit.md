# Complete native-pcp pipeline for N5

30 September 2026. The general decision stages of the existing N5 candidate
are now connected for **native nilpotent pcp input, in arbitrary finite class**.
The [Malcev input](general-malcev-input-audit.md) and
[support kernels](general-support-audit.md) feed a complete finite quotient
branch search and the existing exact central-lifting solver. This is an
implementation of the written candidate, not an additional theorem or a
novelty certification. An arbitrary-finite-presentation command is not part
of this stage.

## Completeness of the implemented search

Put K=G/Z(G) and S=T(K). For each partition of the rational indecomposable
factors, calculate complementary support subgroups K_1,K_2. If they do not
generate K, no direct factors with those supports can generate K. Otherwise
enumerate subgroups of each K_i of index at most |S|, retaining only Y_i
normal in K with Y_i S=K_i. The controlling proof shows that every actual
direct decomposition induces such a pair.

GAP's `LowIndexSubgroupsFpGroupIterator` returns **conjugacy-class
representatives**, not every subgroup. This does not omit the required
normal subgroups: a normal subgroup of K is normal in K_i and its conjugacy
class in K_i consists of itself. The implementation explicitly filters
normality in K. This is a justified restriction to normal subgroups, not an
assumption that the iterator enumerates all conjugates. The routine exhausts
the prescribed index bound; an interrupted run supplies no negative answer.
For |S|=1 the sole candidate is K_i itself.

Retain pairs with trivial intersection, commuting generators and join K.
Check that their full preimages X_i in G commute. For each retained pair,
obtain finite presentations of Y_i, lift generators, and evaluate every
relator in the full center of G. Export its exponent-sum row and its exact
central defect, in a Smith basis with free coordinates first. The earlier
`n5_central_constraints.py` reduces these data to finite exact splitting
constraints and constructs lifting corrections. A side with trivial Y_i
must receive a nontrivial central factor; otherwise the returned product
would have a trivial factor.

Thus the native pipeline contains all stages of the general written
algorithm. This completeness depends on the written rational-decomposition
uniqueness and support-index argument, and on the exact algebraic routines
already credited in that proof. Finite tests do not replace those arguments.

## Results and controls

All twelve groups in the support audit were processed. The search retains
34 central-lifting branches. Five inputs are decomposable: Z^3, the mixed
class-three/Heisenberg/Z product, the class-three/D8 product, the
class-three/Heisenberg/D8 product, and the product of two class-three groups.
The other seven inputs return indecomposable. The negative controls include
the trivial group, D8, free nilpotent groups of classes two through four,
the alternate torsion-free Heisenberg presentation, and the index-two gluing.

The gluing's proper rational partitions already fail the integral generation
test. Its remaining empty/full partitions cannot split a central abelian
factor: the full center lies in the rational derived ideal. As the group is
torsion-free, there is no finite factor either. This explains its negative
answer without relying solely on the program's output. The analogous
rational-derived-center obstruction explains the negative free nilpotent
and Heisenberg controls; D8's indecomposability is elementary.

Fifteen branches across the five positive inputs admit central splittings.
GAP reconstructs **every one** as native subgroups and checks nontriviality,
trivial intersection, commutation and generation of G. It also checks every
corrected relator in its selected central factor and equality of each factor's
intersection with Z(G) to that selected factor. For the largest finite-torsion
control, 4,732 subgroup pairs are considered before retaining eight central
branches. The complete exported branch lists and all central decisions are
retained, including negative branches.

Three sequential one-CPU/eight-decimal-GB runs pass with empty stderr:

| Run | Seconds | Scope |
| --- | ---: | --- |
| `n5-general-pipeline-export-v1` | 20.637 | complete quotient branch lists |
| `n5-general-pipeline-central-v1` | 0.972 | all 34 central decisions |
| `n5-general-pipeline-factors-gap-v1` | 2.076 | all fifteen positive products |

The manifest binds code, branch data, outputs, receipts and observed process
closure. This is same-agent development with separate GAP/Python checks,
not external mathematical review. There is no efficiency claim for the
general algorithm: the bounded-index enumeration and finite central searches
can be very large. Counts, novelty status and the original deadline remain
unchanged.
