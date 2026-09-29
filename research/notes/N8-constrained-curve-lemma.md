# Effective integer curves with a constant quadratic coefficient

29 September 2026. Arithmetic lemma for the N8 follow-up. This is an
assembly of prior effective arithmetic, **not an additional group-theory
claim or a novelty claim**. The prospective group reduction needs its own
audit. The current N8 scope remains c-d<=13 / class<=24.

## Statement

Given a nonzero integer a, polynomials b,c in Z[T], finitely many
polynomial equalities and disequalities in Z[T,R], and polynomial
congruences with fixed positive integer moduli, existence of integers
T,R satisfying all those conditions and

    a R^2+b(T)R+c(T)=0                                  (1)

is decidable. A positive decision constructs a witness. Rational
polynomial coefficients with fixed denominators are also allowed after
clearing them correctly. Finite unions of such systems are decidable.
The leading coefficient a must be a fixed nonzero integer.

No practical complexity bound is asserted. The squarefree degree>=3
case invokes a prior explicit height bound; that enormous enumeration
is not implemented in the accompanying finite audit.

## 1. Integral reduction and repeated roots

Put Y=2aR+b(T) and F=b^2-4ac. Then (1) is equivalent to

    Y^2=F(T),       Y=b(T) mod |2a|,
    R=(Y-b(T))/(2a).                                  (2)

If F=0, set Y=0. Every condition becomes univariate with fixed
denominators. A nonzero equality has a finite computable set of integer
roots. If all equalities vanish identically, enumerate a common period
of all integrality/congruence conditions. An identically zero forbidden
polynomial rejects the branch. All other forbidden polynomials remove
only finitely many integers, so an allowed residue contains a witness.
An exact search along that residue then terminates. This is also the
univariate procedure used below.

Suppose F!=0. Factor it over Z and write F=A^2 G with A,G integral and
G having no repeated roots. One can put every even power of a primitive
irreducible factor into A and leave the entire nonzero constant content
in G; factoring that content is unnecessary. Constant G is allowed.

Every integer root t of A is a separate finite case: Y=0 and (2)
determines R, which is tested against all original conditions. For the
remaining cases A(T)!=0. Since A(T)^2 divides Y^2, valuations at each
prime imply A(T) divides Y. Set Z=Y/A(T). The exact remaining system is

    Z^2=G(T),       A(T)!=0,
    A(T)Z=b(T) mod |2a|,       R=(A(T)Z-b(T))/(2a).    (3)

No divisibility by a varying polynomial is left in reconstructing R.

Here is the rule for translating an additional congruence h(T,R)=0
mod m. If e is at least the R-degree of h, form

    H(T,Z)=(2a)^e h(T,(A(T)Z-b(T))/(2a)) in Z[T,Z].

Given the reconstruction congruence in (3), the original condition is
equivalent to H=0 mod m*|2a|^e. Equalities and disequalities use the same
nonzero multiplier. Thus all transformed moduli are fixed. This rule
also handles any earlier fixed denominators; simply multiplying an
equality's polynomial while keeping its congruence modulus would not
in general preserve the condition.

## 2. Squarefree degree at least three

Apply Berczes--Evertse--Gyory, *Effective results for hyper- and
superelliptic equations over number fields*, Theorem 2.2, equation (2.6),
with K=Q, S={infinity}, f=G and their coefficient b=1. The hypotheses
are exactly integral coefficients, degree at least three and no repeated
roots; irreducibility is not required. Their explicit expression bounds
the logarithmic heights of T and Z. Here the degree/discriminant of K,
the size of S and Q_S are all one; the coefficient height is the logarithm
of max(1,|coefficients of G|).

Compute an integer B strictly above that explicit height bound. For
integer t, h(t)=log max(1,|t|), so |T|,|Z|<=3^B is a valid finite
integer search bound. Enumerate it and check every condition in (3).
This is an effective stopping rule, unlike a bare appeal to Siegel's
finiteness theorem. It is not proposed as an efficient computation.

Primary source: https://arxiv.org/abs/1301.7168, archived as
`literature/raw/N8-Berczes-Evertse-Gyory-hyperelliptic-2013.pdf`.
Introduction/notation/theorem statements through printed page4 read;
actual page4 viewed twice to check the formula's context. The full
31-page proof was not audited; the theorem is explicitly imported.

## 3. Constant and linear G

For constant nonzero G, compute its integer square roots, if any. For
each of these at most two Z-values, use the univariate procedure on T.
Negative or nonsquare constants give no solutions.

For G=uT+v, u!=0, use T=(Z^2-v)/u and impose Z^2-v=0 mod |u|.
Substitute in all conditions and clear fixed powers of u using the
congruence rule in Section1. The result is again the complete univariate
procedure, this time in Z. No bounded search replaces its infinite
periodic branches. Polynomial disequalities either vanish identically
and reject, or exclude finitely many parameter values.

## 4. Quadratic G and finite cases

Write G=uT^2+vT+w, u!=0. Since G has no repeated roots,

    N=v^2-4uw != 0.

The substitution

    X=2uT+v, W=2Z

gives the equivalent norm equation

    X^2-uW^2=N,       X=v mod |2u|, W=0 mod 2,       (4)
    T=(X-v)/(2u), Z=W/2.

All conditions become polynomial conditions in X,W with fixed
denominators/moduli. The reconstruction congruences must be retained.

If u<0, (4) is positive definite: N<0 gives no solution, and N>0
gives |X|<=floor(sqrt(N)), |W|<=floor(sqrt(N/|u|)). Check this full box.
The case N=0 is excluded by squarefreeness, not silently ignored.

If u=k^2>0, then (X-kW)(X+kW)=N. Enumerate every signed divisor pair
r*s=N, retain those with X=(r+s)/2 and W=(s-r)/(2k) integral, and
check every other condition. Again N!=0 makes this finite.

## 5. Positive nonsquare u: complete Pell orbits

Lagrange's theorem supplies positive integers h,j with h^2-u*j^2=1.
Searching j=1,2,... and testing whether 1+u*j^2 is a square therefore
terminates. Minimality of this unit is unnecessary. Put epsilon=h+j*sqrt(u)>1.
Its multiplication matrix is

    M=[[h,u*j],[j,h]],       det M=1.

Both M and its inverse preserve the integer norm equation. For every
alpha=X+W*sqrt(u) of norm N, alpha!=0. Multiplying by a suitable integer
power of epsilon places |alpha| in

    [sqrt(|N|), epsilon*sqrt(|N|)).

The conjugate has absolute value |N|/|alpha|<=sqrt(|N|). Consequently
the resulting integer pair satisfies

    |X| < (epsilon+1)*sqrt(|N|)/2,
    |W| < (epsilon+1)*sqrt(|N|)/(2*sqrt(u)).           (5)

For an entirely integer, deliberately loose box let

    E=h+j*ceil(sqrt(u)), K=ceil(sqrt(|N|)),
    B=ceil((E+1)*K/2).

Every orbit has a representative with |X|,|W|<=B. Enumerating all norm-N
pairs in this box produces a complete finite seed list. Duplicated
orbits are harmless. It also gives a terminating negative decision
when there are no seeds. Signs of X,W and of N are all retained.

This is the standard finite-seed argument. Conrad's *Pell's equation,
II*, Sections2--3, proves existence of the unit and a sharper seed bound.
The proof above records the looser box actually used in the finite
controls. Source: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn2.pdf.
Sections1--3 through the proof of Theorem3.3 on printed page6 were read;
actual page5 viewed. The isolated extra `log` in the displayed expression
for L(u) on page5 is not used: its following coordinates and the norm
identity give the stated vector directly. Later examples not audited.

## 6. Additional equations, congruences and forbidden points

Let Q=X^2-uW^2-N, with u>0 nonsquare and N!=0. This is absolutely
irreducible: its projective quadratic form has rank three, whereas a
product of two linear forms has rank at most two. Thus a polynomial H
either vanishes on the entire conic (Q divides H over Q), or meets it in
finitely many points. This can be decided by exact polynomial division.

If any further equality is not divisible by Q, compute the nonzero
resultant in W of H and Q. It is a nonzero polynomial in X because
Q is irreducible and does not divide H. Enumerate all of its integer
roots X, then all integer W with X^2-uW^2=N. Test all original
conditions. Constant nonzero resultants give the empty set. There is
no lost leading-coefficient case: Q has constant nonzero leading
coefficient in W, and every common solution is a resultant root.

Otherwise every equality holds identically on the conic. A disequality
whose polynomial is divisible by Q rejects the branch. Each remaining
disequality excludes only finitely many conic points.

Take a common multiple m of every fixed congruence modulus, including
all reconstruction moduli and denominator factors. The invertible
matrix M permutes the finite set (Z/mZ)^2. For each seed, iterate it
until its starting residue returns; every intermediate state is distinct.
These states describe **all** positive and negative unit powers modulo m.
Evaluate all polynomial congruences at every state.

If no seed orbit has an allowed state, the answer is no. An allowed
state with period ell yields infinitely many distinct integer points
M^(k+ell*z)seed, z>=0: alpha!=0 and epsilon>1 prove distinctness.
Only finitely many are excluded by the disequalities. An exact search
along this progression therefore constructs a witness and terminates.
In particular removing the finitely many roots of A cannot destroy an
otherwise infinite allowed orbit. This proves the arithmetic lemma.

## Limits and intended use

The finite controls check complete Pell seed boxes and residue orbits,
positive/negative decisions, finite exclusions, and exact polynomial
reconstruction identities. They cannot validate the imported height
theorem or establish the proposed N8 group reduction. General integer
curves, variable leading quadratic coefficients and a general
Diophantine decision algorithm are not claimed.
