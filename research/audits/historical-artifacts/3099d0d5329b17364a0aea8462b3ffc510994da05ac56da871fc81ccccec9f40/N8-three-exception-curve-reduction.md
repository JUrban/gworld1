# Three exceptional offsets: a curve reduction to audit

29 September 2026. **Unadopted group-theoretic proof draft.** The arithmetic
lemma is in `N8-constrained-curve-lemma.md`. That lemma and its finite
tests do not by themselves establish this reduction. N8's adopted
candidate range remains fourteen final layers / class24.

The next proposed extension is at most three remaining exceptional
offsets in arbitrary class. All leading-pair enumeration, full ambient
Lie kernel lemmas and exact universal substitutions remain dependencies
of `problems/N8/two-exception-proof.md` and its predecessors.

## 1. A delayed quadratic family

Consider a partial family of pairs with fixed leading C,D and parameters
T,R. Coordinates have been fixed through some offset h. Assume:

1. Coordinates are rational polynomials in T,R, with all integrality
   requirements retained as polynomial congruences of fixed modulus.
2. Below offset s they do not depend on R. At s the R coefficient is
   a fixed nonzero integral multiple of a primitive exceptional kernel
   (U_s,V_s). All fixed coordinates through h are affine in R, with
   coefficients polynomial in T.
3. s<=h<2s, and every still-unfixed nonzero kernel after h is universal.
4. All lower compatibility equations are retained as polynomial
   conditions on T,R, rather than silently assumed to be identities.
5. If n<2s, these retained equations and congruences are affine in R.
   This holds in the intended block applications; it is an explicit
   hypothesis of the early-truncation case.

The proposal is that such a family is decidable. A one-parameter family
with just one future exception is a special case: solve layers before
that exception polynomially, introduce its full integer kernel parameter
R at s, and set h=s. Earlier compatibility conditions depending only on
T are retained throughout.

At each new offset the correction matrix A_k is constant. Smith form
gives a rational-polynomial particular solution, polynomial compatibility
equations, fixed-denominator congruences, and its full constant integer
kernel lattice. Normalize each universal kernel by the fixed full-rank
period lattice of exact substitutions, retaining every residue. These
periods depend on C,D and the class, not on T,R or higher coordinates.
There are finitely many branches at each of finitely many offsets.

Before offset 2s all residual equations are affine in R: two R-bearing
increments have offsets at least s each. Two increments within one
factor require an additional positive leading weight. Constant-matrix
lifting and constant kernel representatives preserve affine dependence
in R through 2s-1, although their coefficients may be polynomial in T.
Earlier polynomial conditions need not be solved or discarded yet.

If n=c-d<2s, combine R and every remaining unfixed coordinate into one
integer vector z. Their joint contribution is linear, with polynomial
coefficients in T. The earlier complete univariate integer-matrix solver
decides this system. Fixed-modulus congruences can be written as linear
equations by adding integer quotient variables. Initial conditions in
this application are affine in R, so they fit this reduction as well.
Do not extend this last assertion to arbitrary extra polynomial
conditions of degree greater than one in R.

If n>=2s, project the equation at offset 2s modulo im A_(2s). The R^2
coefficient is the fixed nonzero class of m^2[U_s,V_s]. No later affine
R correction contributes a second quadratic term at this first degree.
A fixed rational scalar projection, followed by clearing fixed
denominators, gives

    a R^2+b(T)R+c(T)=0,       a a fixed nonzero integer.

Continue every later layer using the universal residue procedure, keeping
all other polynomial equations and congruences. The residual expressions
can have higher R-degree after 2s; the constrained-curve lemma allows
arbitrary further polynomial conditions. It then decides every final
branch, with reconstruction tested in the original group equation.

**Audit point:** the general formulation needs the n<2s branch's
initial compatibility conditions to be affine in R. This holds for
the block constructions below and for a newly introduced last exception;
it must be an explicit hypothesis, not inferred from an arbitrary
polynomial constraint set. The n>=2s argument permits arbitrary ones.

## 2. The full block below the first quadratic

Let t be the first of at most three remaining exceptional offsets. If
n<2t, all remaining coordinates enter jointly linearly and the branch
is already decidable. Otherwise take the full integer solution lattice
of every correction equation through 2t-1. Quotient its universal
translations exactly as in the two-exception proof, retaining every
torsion coset and integral parameter step.

The free quotient rank r is at most the number of exceptional offsets
in this block, hence at most three. If the first exceptional parameter
is fixed, all coordinates below the next exception are fixed; restarting
the prior at-most-two-exception theorem retains every solution. If it
varies, choose an integral basis adapted to its map into Z and write
that first coefficient k=k0+mT, m!=0. Every later free direction starts
at a later exceptional offset. At offset 2t the cokernel equation is

    q(T)+B S+C R=0,                                   (1)

with absent columns/parameters omitted when r<3. The coefficients B,C
are constant, q is quadratic, and its quadratic coefficient is nonzero
by the inherited exceptional-kernel lemma. This follows from the same
strict weight calculation as in the two-exception block.

## 3. Rank cases

- With r<=1, or with all later columns zero, a nonzero scalar quadratic
  fixes T to finitely many integers. Restart the existing two-exception
  theorem for each retained first parameter, solving the full target.
- With r=2 and B!=0, solve S=-q_i(T)/B_i. Keep all compatibility
  polynomials, integrality conditions and residues. If a nonzero
  compatibility polynomial restricts T, use its full integer root set
  and restart as above. Otherwise the block is polynomial in one
  parameter. At most one exceptional offset can remain at or beyond
  2t. Apply the delayed-family argument at that last exception. An
  exception exactly at 2t is introduced there; it must not be replaced
  by a universal kernel assumption.
- With r=3 and rank(B,C)=2, solve the constant full-rank system for S,R
  as rational polynomials in T, retaining all conditions and residues.
  All three exceptions lie below 2t, so only universal kernels remain.
  The previous one-parameter continuation suffices.
- With r=3 and rank(B,C)=1, an integral unimodular change of the two
  later coordinates puts the map into one nonzero column and one zero
  column. This uses the primitive integer row defining that rational
  rank-one map and retains its scale. The forced coordinate is a
  rational polynomial in T; the other is a free integer R. The
  transformed block is polynomial in T and affine in R.

In the last case R's direction has zero first-exception component. Its
first nonzero component is at a later exceptional offset s<2t: a
direction with every exceptional component zero would lie in the
rational span of universal translations and would be zero in the free
quotient. The leading R direction is fixed, independent of T, and is
a nonzero integer multiple of that primitive kernel. All three
exceptions lie below 2t, so future kernels are universal. Set h=2t-1;
then s<=h<2s. The delayed-family argument applies.

Finite compatibility roots can always be handled by fixing only the
lower coordinates and restarting the old two-exception algorithm. This
may forget higher-coordinate restrictions and repeat valid solutions,
but every accepted branch solves the complete original equation and
every old solution is still represented. No false positive follows
from this enlargement.

## 4. Proposed consequences and remaining work

For leading gap q-p<=10, the existing bound t<=q-3p puts exceptions at
offsets<=8. Process offsets1 and2 by their isolated quadratics, retaining
a new exception exactly at the quadratic layer. At most three mutually
nonconsecutive exceptions remain among3,...,8. Thus a completed proof
above would give leading degrees d<=12 in arbitrary class. Combined
with c-d<=13 it would give all targets in class<=26.

**These consequences are not adopted yet.** The next audit must inspect
the exact integer block quotient in each rank case, the affine-R
hypothesis in the early-truncation branch, full fixed-denominator
congruence lifting, the constant nonzero quadratic coefficient in an
actual group family, and the universal residue normalization after it.
The old Lie perturbations still do not exhibit a surviving unbounded
absorbed branch. A polynomial identity in a Lie algebra alone is not an
actual normalized group fixture. The inherited all-rank leading-pair
and kernel assertions also remain specialist-review dependencies.
