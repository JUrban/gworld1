# An effective one-parameter integer linear solver

29 September 2026. Supporting arithmetic for N8, **not a new resolution**.
One-parameter linear Diophantine decidability is prior work. The group
application in `research/notes/N8-parametric-tail-lead.md` is still a lead;
this note alone does not extend the counted N8 scope.

## Statement and credit

For a rational polynomial matrix P(T) and vector b(T), one can compute
the entire set

    S = { t in Z : P(t) z = b(t) for some z in Z^n }.

It is a union of finitely many full residue classes with finitely many
exceptions, and an integral witness can be constructed when S is nonempty.
All dimensions and polynomial degrees are finite. No complexity bound or
minimal period is claimed.

Schuster's 2007 thesis, *On Algorithmic and Heuristic Approaches to Integral
Problems in the Polyhedron Model with Non-linear Parameters*, Section 4.1.6
and Theorem 71, gives a more detailed parametrization of solutions:
https://www.infosun.fim.uni-passau.de/cl/arbeiten/schuster-d.pdf.
Bozga, Iosif and Lakhnech, *Flat Parametric Counter Automata*, Fundamenta
Informaticae 91 (2009), 275–303, also establishes one-parameter Diophantine
decidability: https://journals.sagepub.com/doi/10.3233/FI-2009-0044.
We do not claim priority for this statement or that these are its earliest
sources. The elementary Smith argument below is supplied to expose exactly
what the implementation and proposed group application require.

## Polynomial reduction

Clear one constant denominator in P,b. This does not change integral
solutions. Compute a full Smith decomposition over the Euclidean domain
Q[T], retaining U,V:

    U P V = D = diag(d_1,...,d_r,0),    beta = U b.

Here U,V are square polynomial matrices with nonzero constant determinant,
so both and their inverses specialize invertibly at every integer. Their
existence and effective computation are ordinary polynomial Smith theory.
With y=V(t)^(-1)z the equations are D(t)y=beta(t). Separately collect and
test every integer root of each nonzero d_i by integer Smith reduction.
Call this finite rank-drop set E.

There is a positive integer M such that all coefficients of M V^(-1) are
integral. Consequently every integral z gives y in (1/M)Z^n. This fixed
denominator condition is necessary even though V need not preserve Z^n.

If beta_j is nonzero for any j>r, every solution parameter is an integer
root of beta_j. Rational polynomial factorization finds the complete list
of such roots; irrational real roots are irrelevant. The implementation
conservatively adds E and tests all listed integers directly. This already
decides the problem in this case.

Henceforth suppose every beta_j with j>r is identically zero. For t outside
E the first r coordinates are forced:

    y_i = beta_i(t)/d_i(t).

## A proper fraction leaves only finitely many parameters

Suppose beta_i = q d_i + rem with rem nonzero and deg(rem)<deg(d_i).
Choose N>0 clearing the rational coefficients of M q, and put

    R = N M rem.

If an integral solution exists, N M y_i and N M q(t) are integers, hence
R(t)/d_i(t) is an integer. It is a nonzero proper rational function.

An explicit safe bound is as follows. Write d_i with leading coefficient
a, let L be the sum of the absolute values of its lower coefficients, and
let H be the sum of absolute values of all coefficients of R. If its
leading coefficient is e, put

    rho = 1 + (sum of absolute lower coefficients of R)/|e|,
    B = ceil(max(1, 2L/|a|, 2H/|a|, rho)).

For |t|>B the leading term gives

    |d_i(t)| > |a| |t|^deg(d_i) / 2,
    |R(t)| <= H |t|^deg(R),

so |R(t)/d_i(t)|<1. The elementary Cauchy root bound |t|<=rho for
roots of R ensures R(t) is nonzero. Thus 0<|R(t)/d_i(t)|<1, contradicting
integrality. Check every integer in [-B,B], together with E. This is a
proved exhaustive finite range, not a chosen search cutoff.

The argument works for constant nonzero remainders and for both signs of
t. d_i has positive degree in this case. It is enough to use the first
nonpolynomial forced ratio; there is no need to intersect several bounds.

## Polynomial forced coordinates give a fixed congruence

Otherwise every beta_i/d_i is a polynomial q_i in Q[T]. Let

    y_0=(q_1,...,q_r,0,...,0)^tr,
    z_0=V y_0,                  W=V_free/M.

For t outside E every integral solution has the form

    z = z_0(t) + W(t) ell,      ell in Z^(n-r).

Indeed the free y coordinates have denominator dividing M. Conversely
any integral vector of this displayed form solves the original equation;
no converse assertion about arbitrary lattice denominators is needed.

Choose K>0 clearing all coefficients of z_0 and W, and set Z=K z_0,
L=K W. These are integer polynomial matrices. The necessary and sufficient
condition is the finite congruence system

    L(t) ell = -Z(t) mod K.

Its coefficients depend only on t mod K. For every residue 0<=a<K, decide
the integer equation [L(a) | K I] v=-Z(a). Save one free-coordinate residue
ell modulo K if possible, or a negative decision. These K decisions give
the complete allowed residue set outside E. Test E directly to include
any additional solutions and reject any exceptional failures.

For any retained residue choose a representative t outside E (successive
additions of K terminate), and compute z=(Z(t)+L(t)ell)/K. This constructs
an integral witness. Every successful rank-drop test already has its own
witness. Empty S is therefore decidable too.

Rank zero and rectangular matrices cause no change. If there are no
equations every t works with z=0; if there are no z coordinates the problem
is exactly b(t)=0. These trivial dimensional reductions justify the general
mathematical statement. The independent computational suite below uses
positive matrix dimensions, including zero-rank matrices; it does not
claim explicit zero-dimensional test coverage.

## Implementation boundary

`scripts/parametric_integer_linear.py` implements the proof using full
Q[T] Smith transformations, integer Hermite transformations, rational
coefficients and complete integer-root lists. Its output contains all finite or residue decisions,
not only a witness. `check_parametric_integer_linear_gap.g` independently
checks the polynomial identities, root lists, finite bound, complete
congruence list, and integer decisions using GAP. See the companion audit.

The initial integer Smith implementation is preserved at commit `2a01612`
and in the later run snapshots. A larger group fixture exposed severe
coefficient growth in that integer step; the current implementation uses
the experiment's previously checked component Hermite routine. If
H=U A^tr with U integral unimodular and H in row Hermite form, integer
division along its nonzero pivots gives the unique constrained coordinates.
The zero rows of H correspond to the remaining rows of U, which form a
complete integral kernel basis after transposition. The implementation
checks H=U A^tr and det(U)=+/-1, so this does not replace the lattice by its
rational saturation. The full 24-system suite and independent GAP replay
were repeated after the change; see `parametric-tail-audit.md`.

The reduction of the remaining *group* variables to a matrix linear in
all but one parameter is a separate obligation. In particular a term
involving the product of two remaining group corrections would invalidate
that application. Nothing in this arithmetic theorem proves its absence.
