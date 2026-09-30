# N5: a connected class-two algorithm including torsion

30 September 2026, within the original run. The rational and integral
stages now connect for general class-two **coordinate input**, including
finite torsion in both the center and the quotient by the center, and
nontrivial central power relations. This extends the implemented scope
beyond the [torsion-free pipeline](class2-pipeline-audit.md). It remains
the same N5 candidate, with no additional count or established novelty.

The implementation is `scripts/n5_class2_mixed.py`. It does not yet
convert an arbitrary finite presentation to these coordinates and does
not implement groups of class greater than two. Those boundaries must
not be obscured by calling it the full N5 implementation.

## 1. The input describes the whole class-two group

Specify finite lists of quotient orders d_i and center orders m_j, using
zero for infinite order and positive integers at least two otherwise.
Infinite coordinates come first in each list. There are quotient lifts
x_i and central generators z_j, with relations

    z_j central,       z_j^(m_j)=1 when m_j>0,
    [x_i,x_k] = beta(i,k) in Z,
    x_i^(d_i) = p_i in Z when d_i>0.

Here Z is the specified finitely generated abelian group on the z_j.
The commutator is x^-1 y^-1 x y. The inputs beta and p are integral
central-coordinate vectors. For an infinite quotient coordinate the
power vector is zero and there is no power relation.

The code checks alternation in Z, beta(i,i)=0, and the consistency
conditions d_i beta(i,k)=0 for every finite d_i. It also verifies that
the supplied Z is the **full** center: the integer solutions u of

    sum_i u_i beta(i,k)=0 in Z for every k

must all be relations of the specified quotient, meaning u_i=0 on
infinite coordinates and d_i divides u_i on finite ones. It computes
this integer kernel using Smith form and slack variables for the finite
central congruences. A nonzero central quotient class is rejected.

These conditions define a consistent group with underlying set K times Z,
where K is the indicated abelian quotient. Use canonical residues for
the finite coordinates. In multiplying (u,z) and (v,w), add the correction

    sum_(i>j) u_i v_j beta(i,j)

to z+w, and reduce each finite coordinate u_i+v_i modulo d_i, adding
floor((u_i+v_i)/d_i) p_i to the center. The carry identity proves the
power contribution is a cocycle. Reducing an argument in the bilinear
contribution changes it by a multiple of d_i beta(i,j), which is zero.
Thus multiplication is associative and realizes exactly the presentation.
The code implements this normal form, inverses and signed powers with
exact integer arithmetic.

Every finitely generated group of class at most two has such data:
choose independent generators of its finitely generated abelian center
and of the abelian quotient by that center, then choose quotient lifts.
Their powers and commutators give the vectors above. Computing those
data from arbitrary input presentations remains a separate interface
step; the current function takes them as its explicit input.

## 2. Rational support and all integral quotient splittings

Let f be the free rank of K and h the free rank of Z. The rational
Malcev Lie algebra has dimension f+h. Use the infinite quotient lifts
and the infinite central generators as a rational basis, with the free
central coordinates of beta as brackets. A finite-order quotient lift
has rational logarithm p_i/d_i in the center. Finite central coordinates
vanish. This explains why the finite quotient lifts are not extra
independent rational generators even when they have infinite order
in the original group.

Apply the [rational Lie decomposition](rational-lie-audit.md) and
enumerate partitions of its indecomposable factors. As in the original
proof, the credited rational uniqueness theorem makes these a complete
list of possible supports modulo the rational center. A partition
induces a projection q on Q^f. Compute the saturated integer image A
and kernel B. Retain it only when A direct-sum B=Z^f; equivalently q
is an integral idempotent. Different central rational partitions may
induce the same q, and are deduplicated.

Write K=Z^f direct-sum T, with T finite. Every decomposition of K
inducing q has the following form. Choose a finite-group idempotent
p on T, and a homomorphism b:Z^f -> T. Shear the product decomposition

    (A direct-sum im p) direct-sum (B direct-sum ker p)

by (u,t) -> (u,t+b(u)). Its projection matrix is

    [ q          0 ]
    [ bq-pb      p ].

Conversely every such quotient decomposition is obtained this way,
by the finite-torsion/free-shear argument in Section 4.1 of the original
N5 proof. Both choices are finite: enumerate all endomorphisms of the
finite abelian T and test idempotence, and enumerate T^f for b. Canonical
projection matrices modulo the finite row orders identify duplicates.
Thus no unbounded subgroup enumeration or search cutoff remains at this
stage for class-two input.

For each splitting K=Y_1 direct-sum Y_2, choose explicit generators
and lifts. If a cross commutator is nontrivial, reject it. Since the
commutators are central, changing the lifts by central elements cannot
repair this obstruction. Otherwise the preimages of the two factors
commute, as required by the general N5 lifting argument.

## 3. Power defects and complete abelian presentations

The generated Y_i need not have independent generators. Given their
coordinate-column matrix M in K, compute the full relation lattice

    R_i = {a in Z^k : Ma=0 in K}.

Adjoin slack columns for the finite quotient moduli, compute the full
integer kernel by Smith form, project to the first k coordinates and
take an integer Hermite basis. This keeps the exact lattice, not merely
its rational span. A finite presentation of Y_i consists of all pairwise
generator commutators and the ordered words from this lattice basis.

Evaluate those words in the actual class-two coordinate group. Their
values are central defects v_i; their exponent-sum rows form E_i.
Changing the k lifts by central values z changes the defects by exactly
E_i z. Feed these data into the earlier complete mixed-center solver:
find Z=Z_1 direct-sum Z_2 for which

    E_i z = -v_i in Z/Z_i.

This uses integer Smith arithmetic, finite torsion splittings, free
primitive-lattice constraints and the finite congruence search already
proved and tested in the N5 center-splitting work. A zero Y_i requires
a nonzero Z_i. On success the solver returns both central summands and
actual corrections to every lift. Their corrected lifts and the assigned
central generators generate the two factors of G.

This is precisely the original proof's central-extension criterion.
All loops are finite, and a negative answer excludes every rational
support, every compatible finite quotient splitting and every central
lifting. A positive answer includes explicit generator coordinates.
Consequently it is a connected decision/constructor for the stated
class-two input, rather than a test of one proposed decomposition.
The general theorem still requires independent specialist review.

## 4. Why both torsion features matter

The fixtures include D8, Q8 and the order-sixteen group with

    Z=<z | z^4=1>,  K=C2 direct-sum C2,
    [x,y]=z^2,       x^2=z,       y^2=1.

Discarding the central power vectors would change these groups. The
native GAP reconstruction checks their relations, full centers,
quotient invariants and finite-group decomposition decisions.

There are also the infinite groups

    G_m=<a,b,t | [a,b]=t, t^m=1, t central>,  m=2,3,4.

In the supplied coordinates K=C_m direct-sum C_m and
Z=<a^m,b^m,t>=Z^2 direct-sum C_m. Thus finite quotient lifts have
infinite order in G_m. The indecomposability argument is retained in
the [original audit](audit.md): a nontrivial finite direct factor would
lie in the cyclic derived group and be killed by retraction; two infinite
factors would each have cyclic torsion-free quotient and central torsion,
hence be abelian. Their nonabelian product is a contradiction.

A separate positive fixture starts with H_3 times D8, then uses quotient
generators u,v,a,b and central z,t with

    [u,v]=z,       [a,b]=t,       [u,a]=t,       t^2=1.

All other cross commutators and a^2,b^2 are trivial. The quotient shear
replacing u by ub removes [u,a]. In the original coordinates the two
direct factors require a nonzero finite component on an infinite quotient
generator. The returned projection is checked to have that nonzero block;
the actual group factors are separately verified in GAP. This guards
against retaining only product splittings of Z^f and T.

The remaining fixtures cover abelian groups with free/finite centers,
direct products with central factors, H_3, and the previously proved
quotient and central gluing obstructions. There are twenty fixtures in
all, nine positive. Three invalid coordinate descriptions are rejected:
an incompatible power/commutator pair, an incomplete specified center,
and a power relation attached to an infinite quotient coordinate.

## 5. Independent checks and their exact limits

Python records 129 quotient branches: 96 cross-commutator rejections,
24 central-lifting rejections and nine successful decompositions. Two
additional rational quotient-support obstructions occur in the gluing
fixture. It also records eight deterministic arithmetic controls per
group, using seed 9302606, including negative coordinates and powers.

GAP reconstructs all twenty rational Lie stages with the unchanged
previous checker functions. It builds the class-two groups independently
from the presentations, using native polycyclic abelian models where
appropriate and GAP/nq otherwise. Full-center equality, free ranks and
torsion orders of the center and quotient verify the coordinate models.
It then checks:

- 480 native group equalities for products, inverses and signed powers;
- all 96 saved nontrivial cross-commutator witnesses;
- 102 central relator defects evaluated as actual group words;
- completeness of every saved abelian relation lattice, using its Smith
  invariants and the corresponding native quotient subgroup;
- all nine positive decompositions, including corrected-lift binding,
  nontriviality, commutation, trivial intersection and generation;
- complete quotient-projection coverage for every negative fixture,
  using direct enumeration of idempotent endomorphisms with each allowed
  free block, rather than the Python shear parametrization;
- agreement with GAP's separate `DirectFactorsOfGroup` algorithm for
  all eight finite fixtures.

The new GAP checker does **not** independently run the general mixed
central-splitting algorithm for all 24 rejected branches. The infinite
negative fixtures retain their written arguments: G_m above, H_3, and
the two gluing examples. The preexisting mixed-center tests and proof
remain relevant with their own limits. Neither finite-group agreement
nor positive subgroup checks are presented as proof of the universal
negative direction or of novelty.

## 6. Process record and reproduction

Both new jobs pass on their first recorded runs, with empty stderr:
Python in 1.37 seconds and GAP in 2.23 seconds. Each uses one CPU and
an 8 GB reservation, sequentially. No new failed source or process
occurred in this batch; older failures remain in their own directories.
All output files are below one megabyte individually.

Sources, exact combined GAP input, certificates and process logs are
bound by `research/certificates/N5-class2-mixed/manifest-v1.json`.
JSON retains integer coordinates, rational data, every branch and every
arithmetic control. GAP input uses `fail` for absent witnesses and row
transposes where required by the previous rational checker. Fresh
constructor output directories are mandatory.

To replay the saved certificate from the repository root:

```sh
bin/gap -q --quitonbreak research/certificates/N5-class2-mixed/sources/combined-gap-v1.g
```

The original N5 source and rendering audit remain unchanged and bound.
The same credited rational uniqueness and effective algebra ingredients
are used; no new bibliographic result is inferred from this implementation.
There is still no independent specialist review or established novelty
determination. The full arbitrary-presentation, arbitrary-nilpotency-class
N5 pipeline remains unimplemented. Counts and the original deadline are
unchanged, and nothing has been pushed or sent to other people.
