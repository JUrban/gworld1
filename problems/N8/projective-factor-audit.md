# N8: an alternative finiteness argument for central targets

29 September 2026. Supplement to `central-target-proof.md`, not a new
problem or a larger candidate scope. This gives an alternative decision
argument for unequal-weight homogeneous factors without Klyachko's Lie
idempotent or the rotation lemma. It does not replace the stronger
two-direction bound or its faster implementation in the original proof.

## 1. A finite-fibre lemma

Let U,V,W be finite-dimensional vector spaces over an algebraically
closed field k. Suppose a bilinear map beta:U x V -> W has no zero
divisors: beta(u,v) != 0 when u,v are both nonzero. Then

    P(U) x P(V) -> P(W),  ([u],[v]) |-> [beta(u,v)]

has finite fibres.

Indeed, the Segre embedding identifies its source with a projective
variety X in P(U tensor V). The linear map B:U tensor V -> W inducing
beta has centre P(ker B) disjoint from X. A fibre over a point [w]
is X intersect P(B^-1(k w)). If the latter linear space is nonempty,
P(ker B) is a hyperplane in it (with the zero-kernel case immediate).
A positive-dimensional closed projective variety meets every hyperplane
in its ambient projective space. Thus a positive-dimensional fibre
would meet P(ker B), a contradiction. Every fibre is a zero-dimensional
projective variety, so has finitely many geometric points.

This is the standard linear-projection argument. Its hypotheses refer
to the algebraic closure, not just rational points; a rational bilinear
map with no rational zero divisors alone is insufficient.

## 2. Application to the free Lie bracket

Let L be the free Lie algebra on r generators over a characteristic-zero
field, and write L_j for its degree-j part. For p != q, the bracket

    beta:L_p x L_q -> L_(p+q)

has no zero divisors after scalar extension to the algebraic closure.
To see this, suppose nonzero C,D commute. They are linearly independent
because their degrees differ, and their span is then a two-dimensional
abelian Lie subalgebra of L. This contradicts the Shirshov--Witt theorem:
a Lie subalgebra of a free Lie algebra is free, whereas an abelian Lie
algebra that is free as a Lie algebra has dimension at most one.
Consequently every nonzero
target W has only finitely many pairs of projective homogeneous factors.

The Shirshov--Witt theorem is a classical imported result. An exact
primary-source restatement appears in Bryant--Kovacs--Stohr,
*Subalgebras of free restricted Lie algebras*, Bull. Austral. Math.
Soc.72(2005),147--156, opening paragraph; this paper was already archived
as `literature/raw/N8-Bryant-Kovacs-Stohr-2005.pdf`. Its ordinary free-Lie
statement, not the restricted-Lie variant in positive characteristic,
is used here.

## 3. Effective rational and integral factors

Work in rational Hall coordinates. For each index i in a basis of L_p,
consider the equations

    C_0=...=C_(i-1)=0,  C_i=1,  [C,D]=W,

in the remaining coordinates of C and all coordinates of D. These
charts partition the possible first-factor directions. Their complex
solution sets are finite: a projective factor pair determines C by the
normalization and then determines the scale of D from [C,D]=W. They
are therefore empty or zero-dimensional affine algebraic sets.

Here is a terminating exact procedure to find all rational points of
each chart; it avoids an unbounded search over rational coordinates.
Compute a Groebner basis over Q. If the ideal is the unit ideal the
chart is empty. Otherwise its quotient algebra A has finite dimension
over Q. Compute its standard monomial basis and the rational matrix
M_j of multiplication by each coordinate variable. At any rational
point, that variable's value must be a rational root of the
characteristic polynomial of M_j: evaluation at the point is a nonzero
linear functional satisfying ev composed with M_j = value_j * ev.

Factor these finitely many characteristic polynomials over Q, retain
their rational roots, enumerate their finite Cartesian product, and
test the original chart equations. Every rational solution is tested;
testing the original equations removes spurious combinations. Nilpotents
in A cause multiplicities, not missing rational points. No polynomial
complexity claim is made.

For each rational solution (C,D), let C_0 be the primitive integral
Hall vector on the line of C, oriented with first nonzero coordinate
positive. Write C_0=t C for a nonzero rational t. Put D_0=D/t, so
[C_0,D_0]=W. Accept this direction exactly when D_0 is integral.

This is complete over the integral Lie ring. Any integral first factor
on the same line is k C_0 for a nonzero integer k. The second factor is
necessarily D_0/k, since ad(C_0) is injective on L_q. If that second
factor is integral, D_0 itself is integral; conversely (C_0,D_0) is
then already an integral solution. Thus the primitive normalization
does not introduce an unbounded divisibility search.

## 4. Relation to the group argument and boundary controls

Equal weights remain covered by the exterior-square argument in
`central-target-proof.md`. The unequal-weight noncommutation fact just
proved also suffices in that file's leading-degree reduction: a
nontrivial central group commutator must, after its exact Nielsen
normalization, have factor weights p+q=c. Integral Lie solutions lift
to group commutators because all higher terms vanish in class c.
Therefore these ingredients give an alternative full decision proof
for central targets in every finite rank and class.

Finiteness must not be asserted for equal weights. If C,D of the same
degree have nonzero bracket, all pairs (C,D+s C), s in k, have that
same bracket and infinitely many second-factor directions.

Finiteness also does not mean uniqueness or rationality. With
Z=[a,b], Jacobi gives

    [a,[b,Z]] = [b,[a,Z]],

so a type-(1,3) target has two distinct first-factor directions. In the
basis of degree-four elements

    A=[a,[a,Z]],  B=[a,[b,Z]],  C=[b,[b,Z]],

the type-(1,3) factor problem is ordinary binary quadratic factorization:
[x a+y b, u[a,Z]+v[b,Z]] has coordinates (x u, x v+y u, y v).
The rational target A-2 C has two algebraic factor directions but no
rational ones, because s^2-2 t^2 has no rational linear factor. These
are useful independent controls for a computational implementation.

This audit changes neither the N8 candidate scope nor any novelty
assessment. General intermediate target layers in unbounded class are
still outside the current candidate. The geometric argument cannot
make their successive nonlinear integral lifting problems finite.

## 5. Implementation, checks, and limits

`scripts/n8_projective_factors.py` implements the normalized charts,
standard-monomial quotient algebra, multiplication matrices, rational
coordinate enumeration and primitive integral scaling. It does not
import the older central-factor routine. It shares the exact Magnus/Hall
basis implementation used elsewhere in the experiment.

The checker compares decisions with the separate block-quadratic
algorithm and validates every integral factor, not just the first one.
It passed 13 Lie cases: eight type-(1,3) targets in rank two and five
generated cases of types (1,2), (2,3), (3,4) in rank two and (1,2),
(2,3) in rank three. The cases include the two-direction Jacobi example,
an irrational-factor negative, and a repeated-root positive. Two
additional affine controls check a nonreduced finite scheme and require
a positive-dimensional system to be rejected as unsupported rather
than misreported as having no rational solutions.

All 16 resulting central group witnesses passed an independent GAP/nq
evaluation. This replay checks the positive lifts, not completeness of
the algebraic negative decisions. Those rest on the argument above;
the two binary-quadratic negatives also have elementary irreducibility
obstructions. A finite test suite does not verify arbitrary-rank or
arbitrary-class termination.

Recorded runs, one CPU and 4 GB per process:

- `results/n8-projective-factors-v1`: failed before recording a case
  because direct conversion from a SymPy rational to the FLINT-backed
  QQ type was unsupported. The original source is retained as
  `solver-v1-failed.py`; this failure is not a passed check.
- `results/n8-projective-factors-v2`: explicit `QQ.from_sympy` conversion;
  all 13 cases and two controls passed, empty stderr, 2.026 seconds.
- `results/n8-projective-factors-gap-v1`: all 16 group witnesses passed,
  empty stderr, 2.126 seconds.

Exact scripts, input/output records, the viewed primary-source page and
an artifact hash manifest are retained under
`research/certificates/N8-projective-factors/`. The checker deliberately
refuses to overwrite its existing generated records. For reproduction,
use a disposable copy of the repository with just that copy's generated
`checks.json` and `fixtures.g` removed, then run the Python checker and
the GAP checker. Retain the originals for comparison. The recorded
commands in each `process.json` specify the actual experiment executions.
Post-deadline replay is verification, not a new discovery run.

Source audit: re-read the frozen N8 paragraph and viewed its archived
rendering. Read and viewed Bryant--Kovacs--Stohr's printed p147 (PDF p5),
which states Shirshov--Witt over a field; its deeper proof is imported.
The finite-projective-fibre argument and rational-point algorithm are
written out here. No specialist review or novelty certification has
occurred. The existing Klyachko argument is retained, not withdrawn.
