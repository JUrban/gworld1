# N5: rational-to-integral decisions for class-two torsion-free groups

30 September 2026. This joins two previously separate implemented stages
of [the N5 candidate](proof.md), for a precisely specified input class.
It is implementation and verification of credited prior torsion-free
scope, not another solution or a novelty claim. The general torsion-case
algorithm and conversion from arbitrary presentations remain outside this
implementation.

## Input and complete implemented scope

`scripts/n5_class2_torsionfree.py` takes nonnegative ranks r,s and an
integral alternating array beta describing

    G = <x_1,...,x_r,z_1,...,z_s |
         z_k central, [x_i,x_j]=product_k z_k^beta[i][j][k]>.

All coordinates have infinite relative order. The supplied central
subgroup must be the full center. This condition is checked by testing
that the rational radical of beta on Q^r is zero. A nonzero rational
radical vector would have a nonzero integral multiple, giving an
additional central element. The converse follows from the commutator
formula. In particular an abelian input has r=0; redundant noncentral
generators are rejected, rather than silently treated as a full-center
description.

These presentations define torsion-free groups of class at most two.
A direct model is Z^r times Z^s, with multiplication

    (u,z)(v,w) = (u+v, z+w+sum_(i>j) u_i v_j beta[i][j]).

The bilinear correction is a cocycle; its alternating part is beta.
The displayed generators have unique ordered normal forms and satisfy
exactly the presentation. Torsion-freeness follows by projecting a
finite-order element first to Z^r and then to Z^s.

Every finitely generated torsion-free class-two group admits this form:
its center is free abelian, and its quotient by the center is free
abelian, since a central power in a torsion-free nilpotent group implies
the element is central. Choose bases and lifts. Computing this description
from an arbitrary input presentation is a separate standard group step
which this interface does not implement.

The function returns either a negative decision, with every distinct
rational-support branch recorded, or positive integer coordinate vectors
generating two nontrivial direct factors. There is no class, rank, integer
coefficient or search-depth cutoff in the algorithm itself; external
resource limits still apply to executions.

## The actual connection between the two stages

1. Form the rational Lie algebra with basis X_1,...,X_r,Z_1,...,Z_s
   and the same bracket constants beta. The class-two BCH identification
   gives the rational completion of the presented group. Apply the
   [implemented rational decomposition](rational-lie-audit.md).
2. Enumerate partitions of its rational indecomposable factors. Each
   partition gives a rational projection q on G/Z(G) tensor Q. Duplicate
   q are discarded; partitions differing only by central rational
   factors do not give different quotient support data.
3. Compute the saturated integer lattices A=im(q) intersect Z^r and
   B=ker(q) intersect Z^r. Their concatenated bases have full rational
   rank. If their determinant has absolute value other than one,
   they do not give a direct decomposition of the integer quotient,
   and the branch is rejected.
4. Otherwise the two quotient subgroups commute with one another after
   lifting, because they come from commuting rational Lie ideals.
   Form their actual integral internal commutators beta(a_i,a_j) and
   beta(b_i,b_j). Apply the earlier center-splitting routine to require
   the first list in Z_1 and the second list in Z_2, with
   Z^s=Z_1 direct-sum Z_2. These are exact containments, with modulus zero.
   If a quotient factor is zero, require its central factor to be nonzero.
5. A successful splitting gives the factors directly: use the ordered
   x-words from A or B and the integral bases of Z_1 or Z_2. No further
   quotient relator defects occur because A,B are free abelian and their
   defining relations are precisely their generator commutators.

Completeness is the corresponding specialization of Sections 2--4 of
the candidate proof. Here G/Z(G) is torsion-free, so the support index
bound there is one: no omitted finite-index subgroup search is needed.
The credited rational decomposition uniqueness theorem ensures that
every group splitting has one of the enumerated rational supports.
The central solver retains all possible ranks and exact primitive
lattice constraints. Thus failure of every branch is a negative answer
for this input class, not merely failure to split a selected rational
decomposition.

## Two distinct integral obstructions

All omitted commutators in these examples are trivial, and z_1,z_2
are the full central basis. Both rational Lie algebras are H_3 plus H_3.

**Quotient obstruction.** Take four noncentral generators and

    [x1,x2]=z1,       [x1,x4]=z2,       [x3,x4]=z2^2.

The two rational noncentral supports have saturated integral bases

    A = <2e1-e3,e2>,       B = <e3,e4>.

They commute across the two sides, but A+B has index two in Z^4.
They cannot be quotient images of direct factors of G. Neither a
different lift nor a central correction changes that index.

**Central obstruction.** Instead take

    [x1,x2]=z1^2 z2,       [x3,x4]=z2.

The quotient supports do split Z^4. But the required central summands
would contain the saturated lines <(2,1)> and <(0,1)>, respectively.
Their sum has index two in Z^2, so they cannot be complementary direct
summands. Thus passing only the rational and quotient stages would
give a false positive here.

In either example the rational center is contained in the derived
algebra, excluding a nontrivial purely central rational direct factor.
The two nonabelian rational factors exhaust the other partitions by
the cited uniqueness theorem. This proves the group indecomposability
illustrated by the negative output. The examples are controls for the
integrality distinction; no novelty is claimed for them.

By comparison [x1,x2]=z1^2, [x3,x4]=z2^3 does split: saturation of the
two commutator lines gives the complementary central basis z1,z2.
The algorithm therefore does not confuse a nonprimitive derived
subgroup with failure of direct decomposability.

## Verification and artifacts

The fifteen fixtures comprise the trivial, cyclic and rank-two abelian
groups; ordinary and scaled H_3; H_3 with a central factor; two H_3
factors; the two obstructions above; the scaled product; H_5; and four
integral basis changes of the product/obstruction examples. The latter
use fixed unimodular changes on the quotient and center, preserving
the actual integral group, rather than just its rational completion.
One malformed full-center description is explicitly rejected.

The independent GAP replay performs the complete rational Lie check on
these fifteen new inputs using the unchanged function bodies from the
previous checker. It then constructs fourteen nontrivial group models
as native polycyclic groups, handling the trivial model directly. It
checks the center, torsion and Hirsch length. For every recorded branch
it verifies saturated quotient supports, their index, and the actual
group commutator defects. Its separate Smith-form calculation decides
the exact central containment problem, including the nontrivial-factor
conditions. For every negative answer it independently enumerates all
rational-support partitions and checks coverage of the saved list.

GAP verifies **33 branch decisions** and **six positive decompositions**.
For each positive it constructs the two subgroups and checks nontriviality,
commutation, trivial intersection and generation of the whole group.
These are selected input tests; the general correctness conclusion rests
on the written argument and credited structural results.

Artifacts are under `research/certificates/N5-class2-pipeline/`:
the JSON/GAP certificates retain the structure constants, all branches,
exact quotient bases and indices, central constraints and positive
generators. The combined GAP input retains the exact reused Lie-checker
function bodies and the new group checker, with the source versions
bound in `manifest-v1.json`.

During the run all commands use `scripts/run_recorded.py`. The saved
certificate can also be replayed directly from the repository root:

```sh
bin/gap -q --quitonbreak research/certificates/N5-class2-pipeline/sources/combined-gap-v2.g
```

The constructor refuses to overwrite its output directory; a new run
needs a fresh `--output` path. Replaying a saved GAP file is read-only.

## Failures and limits

The first Python run passed all mathematical assertions, but inspection
found that its GAP serializer emitted Python `None` for absent witnesses.
That unusable export is retained. A second run writes GAP `fail`; its
JSON and mathematical outputs are identical. Both took about 1.83 seconds.

The first GAP replay completed the rational Lie checks, then the external
`nq` program aborted on the cyclic input with an assertion in
`ElimGenerators`. No mathematical conclusion was taken from its zero
GAP exit status. The corrected checker uses `AbelianPcpGroup` for the
explicitly abelian models, and `nq` for the nonabelian ones. The exact
failed combined input and logs remain. All runs reserve one CPU and
8 GB, sequentially. The final GAP run passes in 2.08 seconds with empty
stderr. There are four terminal runs: three process passes and one
retained process failure; the first passing export has the separately
recorded serialization defect. Exact details are in the manifest.

The original N5 statement, its source/rendering audit and its whole-entry
candidate scope remain unchanged. Torsion-free decidability is already
prior work of Baumslag--Miller--Ostheimer. This implementation increases
the connected executable scope and tests two failure boundaries; it
does not establish novelty of N5, implement arbitrary groups with torsion,
or replace specialist proof review. Candidate counts are unchanged.
