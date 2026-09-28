# N8(b): the penultimate lower-central layer in every class

Candidate extension, 28 September 2026. For every finite rank r and class c,
there is a constructive algorithm deciding `[x,y]=g` in
`N=F_r/gamma_(c+1)(F_r)` whenever `g` belongs to `gamma_(c-1)(N)`.
Use `[x,y]=x^-1 y^-1 x y`. Identity, abelian and rank-one boundary cases
are immediate. Targets in `gamma_c` use the preceding
[central-target algorithm](central-target-proof.md).

The new case is a target with nonzero leading Lie term
`W in L_d`, where `d=c-1` and `L` is the free integral Lie ring. All
integer lattices and homogeneous brackets below are computed in Hall
bases. This extends the same partial N8 candidate; it is not a full
answer to N8(b). Independent review and fuller novelty checks remain due.

## 1. Exact normalization of a putative solution

Suppose `[x,y]=g != 1`. The elementary transformations

    (x,y) -> (yx,y),       (x,y) -> (x,xy)

and their inverses preserve this commutator exactly. Their actions on any
common leading homogeneous layer generate SL_2(Z). One exact rotation is

    (x,y) -> (y^-1, y^-1*x*y),

which also preserves the commutator and has leading action `(C,D)->(-D,C)`.
Thus we may arrange that the first weights satisfy p<=q.

If p=q and the leading terms are rationally dependent, write them aE,bE
with E primitive integral. An integral determinant-one Euclidean operation
changes their coefficients to `(gcd(a,b),0)`. Its exact group realization
leaves the commutator unchanged and raises the weight of one factor. The
other still has weight p, so the resulting weights are unequal. Neither
factor can become trivial, since g is nontrivial.

The preceding central-target proof establishes two facts: nonzero
homogeneous Lie elements of different weights do not commute, and
equal-weight homogeneous elements commute only when rationally dependent.
The first uses the properly credited rotation consequence of Klyachko's
Lie idempotent theorem; the second is the exterior-square injection.
Consequently, after normalization the leading bracket is nonzero and
`p+q=d`. There are finitely many weight types to consider.

## 2. A finite complete list of integral leading pairs

### Unequal weights

Fix p<q with p+q=d. Section 2 of the central-target proof constructs block
quadratics Q_J(W). If all vanish, no such bracket is possible. Otherwise
choose one nonzero quadratic and factor it over Q. Every possible first
factor C lies on one of its at most two rational linear-factor lines.
Keep only lines in L_p and choose a primitive integral representative C0
on each. The equation

    [C0,D0] = W,   D0 in L_q,

is an integer linear system. Its homogeneous kernel is zero by the
different-weight noncommutation lemma. Thus it has at most one rational
solution, and integer solvability is decidable.

If C=k*C0 and D are any integral factors of W on this line, then
`D0=k*D`. In particular D0 must be integral, and the nonzero integer k
divides the gcd of its Hall coordinates. Conversely every signed divisor
k of that nonzero gcd gives the integral pair `(k*C0,D0/k)`.
This is a finite **complete** list. In contrast with the central case,
one must retain all these scalings: the final correction may distinguish
them. The implementation includes both signs directly.

### Equal weights

Fix p=q, so d=2p. The map `Lambda^2 L_p -> L_(2p)` is injective: in the
associative tensor algebra it is the injection
`C wedge D -> C tensor D - D tensor C` after splitting words into equal
blocks. Compute the unique integral exterior preimage of W, if it exists.
It must have rational alternating rank two; otherwise reject this type.

Let P be its rational support intersected with L_p, a primitive rank-two
lattice. Choose its orientation so that, for a basis e1,e2 of P, the
exterior preimage is `h*e1 wedge e2` with h>0. Any integral pair C,D with
this exterior product is an oriented basis of an index-h sublattice of P.
There are only finitely many such sublattices. Their column Hermite bases,
in coordinates of e1,e2, are

    [[a,b], [0,e]],    a*e=h, a,e>0, 0<=b<a.

Any two positively oriented bases of the same lattice differ by SL_2(Z).
Section 1 realizes the necessary basis change by exact commutator-preserving
operations on the group factors. The resulting higher terms are unrestricted
and will be handled below. Hence one oriented Hermite basis per sublattice
is a complete finite list of leading pairs for this weight type.

## 3. One final integer lifting system

For each listed pair C,D choose group lifts x0 in gamma_p and y0 in
gamma_q, using Hall words. Their commutator has leading term W, so

    delta = [x0,y0]^-1*g

lies in gamma_c and is central. Let its Lie coordinate be Z in L_c.
All group elements with these fixed leading terms have the form
`x=x0*u`, `y=y0*v`, with u in gamma_(p+1), v in gamma_(q+1). Modulo
gamma_(c+1), the commutator identities give exactly

    [x0*u,y0*v] = [x0,y0] * [u,y0] * [x0,v].

Indeed `[u,v]` has weight at least p+q+2=c+1. Conjugating `[x0,y0]`
by u or v also changes it only in weight at least c+1. The other two
displayed commutators have weight c and are central. Only the leading
coordinates U in L_(p+1), V in L_(q+1) matter. The required condition is
therefore the integer linear system

    [U,D] + [C,V] = Z.

Smith normal form decides solvability and returns integral U,V on a
positive answer. Their Hall lifts give the required group factors.
Arbitrary higher coordinates of u,v cannot affect this system or the
commutator in class c.

If any branch succeeds, output its verified factors. If all branches
fail, the completeness in Sections 1–2 proves that no solution exists.
Every stage has finite effective input and a finite search space, proving
termination. No efficiency claim is made.

## 4. Why this remains partial

The argument applies to gamma_(c-1), including the already covered central
targets. For an earlier leading term, two simultaneous corrections can
contribute in a surviving degree; the single linear lifting step above is
then insufficient. No termination or completeness claim for those layers
is inferred from this proof.

The new implementation is `scripts/n8_penultimate.py`. It retains all
unequal-weight integral scale allocations and all equal-weight Hermite
branches. The earlier central and class-five algorithms have not been
changed. The recorded Python suite passed 85 records in 58.56 seconds,
including 14 comparisons with the separate class-five implementation.
GAP independently verified all 49 positive word witnesses and all 187
central subgroup-membership branches in 120.23 seconds; 140 branches
were negative. See [the audit](penultimate-audit.md) for scope and limits.
