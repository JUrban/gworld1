# N8: from the group block to the weighted word theorem

30 September 2026, within the original experiment. This supplies the
coefficient dictionary between Section 6 of [the general proof](general-proof.md)
and [the weighted word theorem](weighted-block-audit.md). It is a written
supplement, not a formalization of Hall coordinates, BCH, free-Lie
projection or the complete algorithm. The original proof and the earlier
formal inputs remain unchanged. No candidate count or novelty claim changes.

## 1. The fixed data and the integral block

Work over Q in the untruncated free graded Lie algebra, truncating only
when evaluating the nilpotent group. Let C,D be the fixed noncommuting
leading factors, of positive weights p,q. Let t be the first remaining
exceptional offset, so

    0 < t < q-p,        d=p+q,        N=d+2t <= c.

All factor coordinates below offset t are fixed. Solve jointly all
commutator equations at offsets t,...,2t-1 in the original integral
Hall coordinates. When this affine integer system is nonempty, choose
an integral parametrization of its entire solution lattice. If its
first-offset component varies, adapt the parameter basis so that

    first-offset pair = (P,Q) + b T (U,V),      b != 0,

and every other parameter has zero component at offset t. Here (U,V)
is a primitive integral generator of the one-dimensional integer kernel,
viewed also over Q,

    [U,D]+[C,V]=0.

The actual integer step is retained: b need not be 1. The fixed
particular pair (P,Q) need not lie in Lie(C,U). Nothing below assumes
that it does. If the first-offset component is constant, the algorithm
fixes it and restarts, without using this separation argument.

Every earlier block equation is an identity in the free integer
parameters: all those parameter values describe solutions of the
earlier affine system. Its coefficients are therefore zero. Since
the equations are affine, this follows already by comparing the
zero parameter vector and each unit vector; no extra density assumption
or extension of the integral solution set is being used.

## 2. Why the required expressions are affine

Write X=log x and Y=log y. A Hall-coordinate factor of weight w enters
as exp(a H), where H is the fixed rational logarithm of its group Hall
generator and has leading weight w. H need not be homogeneous: its
higher-weight terms only strengthen the bounds used here.
Collection followed by logarithm is a finite rational Lie polynomial.
A term of parameter degree at least two uses at least two occurrences
of varying factor coordinates. Since their first weights are p+t in
x and q+t in y, their respective weights are at least

    2(p+t) > p+2t,       2(q+t) > q+2t.

Consequently X through weight p+2t and Y through weight q+2t are affine
in all the block parameters and in new coordinates at offset 2t.
Arbitrary fixed lower coordinates only enter their rational coefficients.
This assertion concerns these finite prefixes, not the entire logarithms.

In L_(>=p), extend C to a homogeneous free basis. Replacing that basis
element by the fixed prefix of X through weights below p+t and fixing
the other basis elements defines a filtered substitution with identity
associated graded. Its inverse, computed to weight N, sends X to a
series whose components at offsets 1,...,t-1 vanish. This substitution
is fixed independently of every block parameter. It is a linear Lie
map on elements, so it preserves affine parameter dependence. Its
degree-leading action fixes C,D,U,V.

For the convention [x,y]=x^-1 y^-1 x y, the part of log[x,y] with
exactly one Y occurrence is

    (1-exp(-ad_X))Y = [X,Z],
    Z=h(ad_X)Y,       h(z)=(1-exp(-z))/z,       h(0)=1.

Indeed exp(-X)exp(-Y)exp(X)=exp(-exp(-ad_X)Y); the part linear in Y
of its BCH product with exp(Y) is Y-exp(-ad_X)Y. Every remaining term
contains at least two Y occurrences and at least one X occurrence.
A parameter-dependent such term has weight at least p+2q+t>N.
Those terms can have nonzero fixed parts at weights at most N; subtract
the fixed parts from the target instead of discarding them.

The expression Z is affine through weight q+2t as well. A term with
two varying X occurrences and a Y has weight at least q+2(p+t)>q+2t.
A term with varying X and varying Y has weight at least p+q+2t>q+2t.
Terms with one varying occurrence remain linear. At offset t, the
coefficient of T in Z is exactly bV: the identity term h(0)Y gives it,
and all contributions from varying X, or from a positive power of
ad_X applied to varying Y, have strictly greater weight.

Thus, after a fixed change of coordinates and subtraction of fixed
BCH terms, the required coefficient calculations come from [X,Z]
with affine X and Z. These changes are used to prove a rational
separation statement. The algorithm still solves the original integral
Hall systems.

## 3. The projection and its weight restrictions

Use the graded subalgebra

    A = Q C + direct_sum_(w>=p+t) L_w.

It contains the normalized X and Z components in question, since
q>p+t. The degree-(p+t) component is independent modulo [A,A]:
[C,C]=0 and every bracket involving a tail component has degree
greater than p+t. Extend C,U to a homogeneous free basis of A,
then let pi:A->Lie(C,U) kill every other basis generator.

The imported inner-solution theorem applies to that actual free basis
and [U,D]+[C,V]=0; hence D,V belong to Lie(C,U), and pi fixes them.
The whole degree-(p+t) component was included in A, so pi is also
defined on every possible particular solution P,Q. No projection of
the original solution lattice onto an integral sublattice is performed.

Put u=p+t, E_j=(ad_C)^j U and delta=ad_C. Lazard elimination makes
the ideal generated by U free on the E_j. Its associative word
realization assigns E_j weight u+pj, and E-letter count is a grading.
Homogeneous components in that grading remain Lie elements: expansion
of a Lie expression in homogeneous generators decomposes its brackets
by additive letter count. The weight and letter-count projections
commute.

Let m be the largest E-letter count in D and D_m its nonzero component.
It has weight q>u. There is no pure-C part of D, since a Lie polynomial
in C alone is a scalar multiple of C of weight p. In E-letter count
m+1 the kernel equation is

    delta V_(m+1) = -[E_0,D_m].

For higher positive letter counts the right side is zero. Injectivity
of delta on each positive word-length component shows that V has no
components above m+1. To use the positive-sign convention of
WeightedBlock.lean, its input D is **-D_m**, while its V is V_(m+1).
Negation preserves nonzeroness, weight and generated-Lie membership.
The weighted theorem therefore gives

    R([E_0,V_(m+1)]) != 0.

Every projected X component at a positive offset i<=2t has weight
p+i<=p+2t<2u, so it contains at most one E letter. Its pure-C part
is zero by weight. It is a scalar multiple of E_((i-t)/p) when
i>=t and p divides i-t, and is zero otherwise. This holds for
fixed particular components and for all parameter directions.

Let pr_(m+2) denote projection onto E-letter count m+2. In that
component the final homogeneous correction map has the form

    pr_(m+2) pi([H,D]+[C,K]) = delta(pr_(m+2) pi(K)).

The first term vanishes because pi(H) has at most one E letter and
D has at most m. Thus the complete original correction image maps
into the derivative image used in the formal theorem.

## 4. Exact earlier relations before applying R

Let Z_j^0 be the fixed coefficient of Z at offset j. Define

    F_j = pr_(m+1) pi(Z_j^0),                 0<=j<t.

In particular F_0=0, since Z_0^0=D. Write the projected coefficient
of T in the X component at offset i as a_i E_((i-t)/p), interpreting
a_i=0 if the required index is not an integer. At i=t it is bE_0.

Take the coefficient of T in the earlier equation at offset t+j,
where 0<=j<t, then project to E-letter count m+2. A varying Z component
paired with a positive-offset fixed X would require that X offset
to be at most j<t, where it vanishes. Pairing varying Z with C gives
delta H_j. The remaining terms are therefore exactly

    delta H_j + b[E_0,F_j]
      + sum_(i=t+1)^(t+j) a_i [E_((i-t)/p),F_(t+j-i)] = 0.      (1)

These are identities in the word space, before applying R. The
quadratic parameter terms start at offset 2t and cannot contribute
here. Reindexing k=t+j-i gives k<j. Thus (1) is the formal theorem's
`heq`, with G_j=-H_j, c_jk=a_(t+j-k), and n_jk=(j-k)/p on
the nonzero terms. On a zero coefficient term choose any natural
index, for example 0. No fractional E index is introduced.

Applying R to these identities gives the triangular induction and
R([E_0,F_j])=0 for every j<t. In particular the formal argument does
not require us to assume that the restriction vanishes for arbitrary
fixed lower Z components; it obtains that fact from compatibility
of the complete surviving group block.

## 5. Every later column and the quadratic coefficient

Fix any other parameter s. Its first nonzero offset exceeds t.
At offset 2t its varying Z component paired with C contributes a
derivative image. Pairing varying Z with a positive-offset fixed X
would require an X offset below t, so contributes zero. Its varying
X components pair only with fixed Z offsets 2t-i<t. After the same
projection, its full column is consequently

    B_s = delta W_s
      + sum_(i=t+1)^(2t) d_si [E_(e_si),F_(2t-i)].             (2)

Again a term whose weight gives no integral index has zero coefficient.
The endpoint i=2t is harmless because F_0=0. Formula (2) also permits
zero columns and universal kernel directions; no classification of
the other parameters is required.

In contrast, the coefficient of T^2 at offset 2t can only pair the
two first-offset T components. The projected result is

    Q_2 = b^2 [E_0,V_(m+1)].

All other pairs of varying offsets are greater than 2t. Earlier
same-factor logarithmic and h(ad_X) terms of parameter degree two
were excluded by the strict weight bounds in Section 2. The fixed
particular first-offset pair may contribute to the constant and linear
terms; it cannot change this quadratic coefficient.

The formal weighted theorem applied to -D_m,V_(m+1), (1), and (2)
now says that Q_2 is outside the sum of the derivative image and
the span of **all** later columns. This proves the required stronger
separation, not only nonmembership in the last correction image.

## 6. Returning to the actual group equation

For each vector in the earlier integral solution lattice, the original
target error begins in degree N=d+2t. Its leading Hall coordinate and
leading logarithmic coordinate agree. Equivalently, log([x,y])-log(g)
and log([x,y]g^-1) agree in degree N because their additional BCH
brackets have greater degree. The fixed prefix normalization acts as
the identity on that leading graded piece.

Composing normalization, pi, pr_(m+2), positional realization and R
therefore gives a rational linear map on the actual degree-N error
space. It kills every correction column and every later free block
column but not the T-squared coefficient. If a scalar functional is
needed, choose a nonzero coefficient of that last polynomial image;
all spaces at the fixed weight are finite-dimensional. This is an
effective rational operation and uses no unknown analytic functional.

It follows that every original solution in this branch has T among
the at most two integer roots of a nonzero scalar quadratic. The
algorithm keeps these necessary values and restarts after the fixed
first-offset prefix, leaving higher coordinates free. Original solutions
are retained, and accepting a branch still requires the complete
original group commutator test. This supplement does not replace the
separate proofs of finite leading-pair enumeration, exact integral
universal periods, or termination of that recursion.

## Verification boundary

This is a same-agent written derivation of the formal theorem's
hypotheses from the existing candidate's structural ingredients. The
unchanged weighted word checker already passed; no finite fixture or
Lean suite was rerun for this text. The free-basis and inner-solution
theorems, Lazard elimination, effective Hall/Malcev coordinates and
their use above remain mathematical proof dependencies. No external
review, complete formalization or new implementation is asserted.
