# N8: a possible arithmetic route past the linear-tail boundary

29 September 2026, approximately 15:09--15:16 UTC. **Unverified lead;
not part of the adopted candidate scope.** First finish the pending
class-24 group audit. This note proposes a different next step, not an
assertion that the strict linear-tail bound can be ignored.

## The supporting arithmetic question

Consider integer T,R satisfying

    a R^2+b(T)R+c(T)=0,       a!=0 a fixed integer,       (1)

together with finitely many polynomial equalities and congruences of
fixed modulus. Clearing fixed denominators is allowed. Completing the
square gives

    Y=2aR+b(T),    Y^2=F(T):=b(T)^2-4ac(T),
    Y=b(T) modulo 2a.                                  (2)

The coefficient a being constant matters: reconstruction of R adds only
a fixed-modulus condition. Do not silently extend this claim to arbitrary
rational functions or to an equation with a varying leading coefficient.

There is a prior effective arithmetic theorem available for the main
case. Berczes--Evertse--Gyory, *Effective results for hyper- and superelliptic
equations over number fields*, [arXiv:1301.7168v1](https://arxiv.org/abs/1301.7168),
Theorem 2.2, gives explicit height bounds for f(x)=b y^2 over S-integers
when f has no multiple roots and degree at least three. Taking K=Q and
S to consist of the infinite place gives a complete finite search bound
for integral solutions. This is prior number theory, not a new result.

The 2013 PDF is archived under
`literature/raw/N8-Berczes-Evertse-Gyory-hyperelliptic-2013.*`, SHA256
`6f0c3522bec1af5548ddd4fcb3bd7fc3bc02a2e4294276abc6219289ee94334c`.
The introduction, notation and theorem statements through printed page 4
were read; page 4 was rendered and actually viewed. The 31-page proof
was **not** fully audited. A 2023 multiple-root extension, arXiv:2310.09704,
was also located, but its theorem/proof was not read and is not used here.

For a nonzero F in Z[T], factor over Z as

    F=A(T)^2 G(T),

where A is integral and G has no repeated roots; a constant content may
remain in G. At an integer T with A(T)!=0, A(T)^2 divides Y^2, so A(T)
divides Y. Put Z=Y/A(T); then Z^2=G(T). Integer roots of A are a separate
finite set and must be checked directly. The extra equalities and fixed
congruences remain polynomial conditions in T,Z after substitution.

The proposed complete treatment is:

- For deg G>=3, use the cited effective bound, enumerate the finite
  integer points and check every other condition exactly.
- For deg G=0, either there is no square root or Z is one of at most two
  constants. The remaining conditions are univariate equations and fixed
  congruences. Handle F=0 separately with Y=0.
- For deg G=1, solve T=(Z^2-v)/u. All denominators are fixed constants;
  integrality/congruences reduce to finitely many residue classes of Z,
  and a nonzero further equality gives a finite root set.
- For deg G=2, complete the square to a generalized Pell equation
  X^2-u W^2=N with N!=0, and retain reconstruction congruences. If u<0,
  elementary bounds give a finite search. If u is a positive square,
  factorization of the nonzero N gives finitely many possibilities.
  For positive nonsquare u, find an integral norm-one unit epsilon>1.
  Multiplication by epsilon and its inverse preserves the integer lattice.
  Every norm-N element can be moved into a bounded real interval, giving
  a finite, effectively enumerable list of orbit seeds. On each orbit,
  fixed congruences are periodic because the unit matrix is invertible
  modulo the modulus. A further polynomial equality either holds on
  the whole conic or cuts out finitely many points, found by exact
  elimination. Removed roots of A must still be treated separately.

This is a proof plan, not an implemented complete arithmetic solver.
The Pell seed bounds, sign cases, simultaneous congruences, resultant
exceptions and reducible cases need a careful written audit. Mere
finiteness of integral points is not a stopping rule; the cited effective
bound and the explicit low-degree procedures are essential.

## Why this might apply to another exceptional offset

Suppose a polynomial integral family in a parameter T is fixed below
one remaining exceptional offset s, with leading C,D constant. Introduce
its primitive kernel parameter R. Before offset 2s all equations are
linear in R, with polynomial coefficients in T. Constant-matrix integral
lifting imposes only fixed-denominator polynomial congruences. These can
be handled by retaining every residue pair for T,R and reparametrizing;
the leading step of R remains a fixed nonzero integer.

A nontrivial earlier rational compatibility equation linear in R may
already express R as a rational function of T. Polynomial division then
either produces a polynomial family with fixed congruences or a finite
integer range, using the previous proper-fraction argument. Exceptional
integer roots of its denominator cannot be discarded.

If R survives to offset 2s, its quadratic coefficient in the cokernel is
the constant nonzero class of [U_s,V_s] times the square of its integral
step. Higher R corrections cannot contribute another R^2 term at that
first degree. A nonzero scalar projection thus suggests (1), with a
constant nonzero a and polynomial b,c. All other compatibility equations
must remain present, not be inferred from this scalar projection.

After the last exceptional offset, the exact universal substitutions
would leave only finite residue choices at each layer. One would need
to show explicitly that each branch then imposes polynomial equations
and fixed congruences on the same curve, and that no new unrestricted
parameter is introduced by these normalizations.

## Prospective three-exception block argument

For a branch with at most three remaining exceptional offsets, retain
the full integer block below the first quadratic. Its quotient by exact
universal translations has free rank at most three. With first parameter
T, the first cokernel equation has the shape

    q(T)+B S+C R=0,

where B,C are constant vectors and q has a nonzero quadratic coefficient.
If that coefficient survives modulo span(B,C), T has finitely many
possibilities and the existing two-exception theorem can be restarted.
If the later-column rank is two, solving the constant linear system
should leave one polynomial parameter. If the rank is one, it should
leave a polynomial parameter and one remaining free exceptional
direction, the proposed arithmetic situation above. Every integer
torsion coset and parameter step must be retained. Cases in which the
third exception is exactly at or after the first quadratic need their
own explicit treatment.

If all of these reductions hold, at most three exceptions after offsets
1 and 2 would cover leading gaps<=10 and leading degrees<=12 in arbitrary
class. Combined with a completed fourteen-final-layer result, the
prospective all-target consequence would be class<=26. **None of these
new bounds is adopted here.** General N8 remains unresolved.

The next work is the complete integral curve lemma and the group-family
reduction, with actual group examples and independent arithmetic controls.
The failed compatible-deformation probe does not supply an unbounded
absorbed-parameter example and must not be used as one.
