# N5: an implemented rational Lie decomposition stage

30 September 2026, during the original experiment. The rational direct
decomposition used in Section 1 of [the N5 proof](proof.md) now has a
general exact implementation for an input nilpotent Lie algebra over Q.
It is established algebraic machinery, not another proposed resolution
or a claim of a new decomposition theorem. This does not implement the
complete nilpotent-group algorithm: obtaining the rational Lie algebra
from an arbitrary group presentation, rational subgroup intersections,
and general bounded-index support enumeration remain separate steps.

The implementation is `scripts/n5_rational_lie_decomposition.py`.
Its input is a finite three-dimensional array of rational structure
constants, with column-vector coordinates. It checks dimensions,
alternation, Jacobi and nilpotency. Its output includes rational
projections onto nonzero, directly indecomposable ideals whose sum is
the whole input. The zero algebra returns no factors. No search cutoff
is interpreted as indecomposability.

## 1. Split off the abelian direct factor

Let L be the input, D=[L,L] and Z=Z(L). Choose a vector-space complement
A to Z intersect D in Z, then a complement B to A in L containing D.
Since all brackets are in D, B is an ideal; A is central and

    L = B direct-sum A,        Z(B) contained in [B,B].

Indeed Z is contained in D+A, so an element of Z intersect B lies in D.
Also [B,B]=[L,L], as A is central. Split A into one-dimensional ideals.
All these choices require only rational row reduction. The remaining
algebra B has no nonzero abelian direct factor. This reduction is
essential: the centroid of an abelian algebra is a full matrix algebra,
so its semisimple quotient need not be commutative.

## 2. Compute the centroid and its radical

For nonzero B of dimension d, compute the unital associative algebra

    C = {T in End_Q(B) : T[x,y]=[Tx,y]=[x,Ty] for all x,y}.

These are linear equations on the d-by-d matrix entries. An idempotent
in C gives a direct sum of its image and kernel as commuting Lie ideals;
conversely the projection of a Lie direct decomposition lies in C.

Put J=Hom_Q(B/[B,B], Z(B)), viewed as endomorphisms of B. Every such
map lies in C. It is a two-sided ideal, and J^2=0 because Z(B) is
contained in [B,B]. Moreover C/J is commutative. For S,T in C,

    ST[x,y] = [Tx,Sy] = TS[x,y],
    [(ST-TS)x,y] = (ST-TS)[x,y] = 0.

Thus ST-TS kills the derived algebra and has image in the center,
which is exactly the condition for membership in J.

Let N be the preimage of the nilradical of the finite-dimensional
commutative algebra C/J. Its nilradical is nilpotent: choose a finite
basis of nilpotent generators and expand sufficiently long products.
Since J^2=0, N too is nilpotent. The quotient

    C/N = K_1 times ... times K_s

is a product of number fields, by the usual structure of reduced finite
commutative Q-algebras. These standard algebra facts, rather than a new
Lie classification, are the structural ingredients of this computation.

N is computable as the kernel of the trace pairing on the given faithful
matrix representation:

    beta(S,T)=trace_B(ST).

Here is a direct proof. Its kernel K is a two-sided ideal by cyclicity
of trace. If S is in N, every ST is in the nilpotent ideal N, so has
trace zero; hence N is contained in K. Conversely, for S in K,
trace(S^j)=0 for every j>=1, using T=S^(j-1), including T=1. Newton's
identities in characteristic zero give characteristic polynomial t^d,
so S is nilpotent. Its image in the commutative C/J is therefore in
the nilradical, and S belongs to N. This proves K=N.

Consequently the rank delta of the rational Gram matrix of beta is
dim_Q(C/N). This computes the necessary semisimple dimension without
finding a number field embedding or extending the coefficient field.

## 3. A finite separating-element search

Let C_0,...,C_(q-1) be the computed rational basis of C, where q=dim C.
Over an algebraic closure, C/N has delta distinct characters. Every
one appears among the diagonal characters of its action on B. To see
this, take a composition series of the C-module after scalar extension.
The nilpotent ideal N annihilates every simple factor, and the simple
modules of the resulting product of copies of the field are
one-dimensional. A missing character would make the trace pairing
degenerate on C/N, contradicting the preceding calculation, which
also holds after scalar extension.

Consider the single-parameter family

    T(k) = sum_(i=0)^(q-1) k^i C_i.

For two different characters, the difference of their values on T(k)
is a nonzero polynomial of degree at most q-1: they differ on some
basis vector. At most

    binomial(delta,2) (q-1)

values of k can cause any collision. Thus the integers from zero
through this bound include a separating value. The implementation
tests them in order. The exact test is that the squarefree part of
the characteristic polynomial of T(k) has degree delta. All its
eigenvalues are character values, so this condition is both necessary
and sufficient for separation.

This proves a finite bound for this search, including delta=1, where
k=0 already suffices. Coefficient sizes can be large; there is no
practical complexity claim.

## 4. Rational idempotents, retaining the nilpotent part

Factor the characteristic polynomial over Q as

    chi(t) = product_i f_i(t)^(e_i),

with distinct monic irreducible f_i. Since all absolute characters have
different values, the distinct rational irreducible factors correspond
exactly to the number-field factors of C/N. Apply the Chinese remainder
theorem to the full powers f_i^(e_i): construct p_i congruent to one
modulo f_i^(e_i), and zero modulo all the other powers. Cayley--Hamilton
gives pairwise orthogonal idempotents p_i(T) with sum 1 in C.

The Lie image of each is directly indecomposable over Q. Its centroid
is the corresponding corner of C; modulo its nilpotent ideal the corner
is the field K_i, with no nontrivial idempotents. An idempotent lying
in a nilpotent ideal is zero, and an idempotent equal to one modulo that
ideal is one. Hence the corner itself has no nontrivial idempotents.
This proves indecomposability, rather than just exhibiting some factors.

The implementation evaluates these polynomials as rational matrices and
transports their projections, together with the one-dimensional central
projections, back to the original input basis. It checks idempotence,
orthogonality, sum 1 and the centroid identities exactly.

Using only the squarefree polynomial in the CRT would be wrong. For
example, on H_3 direct-sum H_3 let T=N_0 direct-sum (1+N_1), where
each N_i maps the first Heisenberg generator to its central commutator
and kills the other basis vectors. These maps are in the centroid,
N_i^2=0, and the two eigenvalues are 0 and 1. The naive polynomial t
does not give an idempotent: T^2-T=-N_0 direct-sum N_1 is nonzero.
The corrected polynomial 3t^2-2t^3, using the repeated factors, gives
exactly the second-factor projection. GAP checks this control.

## 5. What was checked

There are 19 deterministic fixtures: twelve displayed models and seven
rational changes of basis of the last seven. The latter use seed
9302605, 2n integral column shears with coefficients in {-2,-1,1,2},
then divide the first column by two. These changes preserve the Lie
algebra but exercise denominators and noncoordinate factors.

| Base model | Dimension | Expected indecomposable dimensions |
| --- | ---: | --- |
| Zero and abelian Q^3 | 0, 3 | none; 1+1+1 |
| Heisenberg H_3 | 3 | 3 |
| Class-three filiform, [e1,e2]=e3, [e1,e3]=e4 | 4 | 4 |
| Heisenberg H_5 | 5 | 5 |
| H_3 over Q(sqrt(2)), restricted to Q | 6 | 6 |
| H_3 over Q[e]/(e^2) | 6 | 6 |
| H_3 over Q[z]/(z^2-1) | 6 | 3+3 |
| H_3(Q(sqrt(2))) plus H_3(Q(sqrt(3))) | 12 | 6+6 |
| Two copies of H_3(Q(sqrt(2))) | 12 | 6+6 |
| H_3(Q(sqrt(2))) plus Q^2 | 8 | 6+1+1 |
| H_3 plus the filiform algebra plus Q | 8 | 3+4+1 |

The quadratic-field examples guard against accidentally decomposing over
an algebraic closure. The split quadratic and repeated-field examples
guard against merging distinct rational factors. The dual-number example
has a nontrivial nilpotent coefficient algebra but remains indecomposable.
Three malformed/nonpromised inputs are rejected: wrong array dimensions,
a failed Jacobi identity, and a nonnilpotent two-dimensional Lie algebra.

The independent checker, `scripts/check_n5_rational_lie_gap.g`, builds
native GAP Lie algebras from the original constants. It checks Jacobi
explicitly, rather than trusting the constructor's Lie-algebra flag,
and computes the nilpotency class. It reconstructs the complete centroid
using the common commutant of the native right-adjoint matrices, a
different linear formulation from the Python generator. It checks the
central/stem split, the trace matrix and its rank, and directly verifies
that the trace kernel is a nilpotent two-sided ideal containing all
centroid commutators. Finally it factors the selected characteristic
polynomial independently over Q, verifies separation, evaluates the CRT
polynomials and checks the returned original-basis projections.

The certificate contains both JSON and literal GAP input, original
structure constants, centroid bases, trace matrices, selected operators,
factorizations, CRT polynomials and the projections. Rational numbers in
JSON are integers or strings such as "3/2"; polynomial coefficient
lists run from constant term upward. Recorded irreducible factors may be
primitive integral scalar multiples of their monic versions; the checker
normalizes them and verifies their product against the monic characteristic
polynomial. These scalars do not change the CRT ideals. Matrices act on
columns. GAP explicitly transposes them to its row convention.

## 6. Recorded runs and limits

The initial Python run passed all 19 fixtures and three rejections in
13.01 seconds, with empty stderr. The first GAP run stopped after twelve
fixtures because it compared rational factors literally across the two
systems. A second run normalized GAP factors only and failed at the same
point. A third diagnostic run established the precise cause: SymPy had
returned 169t^2-598t+511, while GAP returned its monic associate
t^2-(46/13)t+511/169. This is a representation issue, not a disagreement
about irreducibility or the Lie factors. The final checker normalizes
both sets to monic form and verifies their products before comparison.
All three failed sources and logs remain; their zero process exit statuses
were not accepted as passes. The final GAP run passed all 19 fixtures,
34 factors and the repeated-factor control in 3.53 seconds, with empty
stderr. Thus there are five terminal runs: two passes and three retained
comparison failures. The constructor and its output were not changed
after the first Python pass.

All jobs use one CPU and an 8 GB reservation, sequentially, through the
recorded runner. Fresh Python output directories are required; the saved
certificate is never overwritten. Reproduction commands are recorded in
`results/n5-rational-lie-*/process.json`. The manifest binds exact source
snapshots, both certificate formats and the successful and failed logs.

The original N5 statement and the existing universal proof are unchanged.
The full archived nilpotent-problem HTML and exact N5 fragment were reread,
and the retained N5 rendering was actually viewed during this work period.
There is no linked background paragraph for this entry.
Baumslag--Miller--Ostheimer, Proposition 13, already credits rational
decomposition algorithms, referring to de Graaf, Section 1.15. That
retained passage was reread; this supplement does not claim to reproduce
de Graaf's particular implementation or to supply a new theorem. The
centroid/idempotent, finite-algebra and polynomial machinery is standard.
The brief trace-kernel and finite separating-parameter proofs above make
the implemented version reviewable without an opaque decomposition call.

The broader N5 support-partition completeness still uses the credited
rational decomposition uniqueness theorem. The full algorithm for an
arbitrary finitely presented nilpotent group remains unimplemented end
to end. There has been no external specialist review or established
novelty determination, and no new candidate is counted.
