# Audit of the weighted free-generator reduction

29 September 2026, before the original 48-hour deadline. This is an
internal mathematical audit plus independent software arithmetic, not
independent specialist review. The candidate theorem is in
[weighted-orbit-proof.md](weighted-orbit-proof.md).

## Exact new scope

The branch algorithm permits arbitrary nilpotency class and arbitrary
tails of both factors, provided their nonzero leading terms C,D satisfy
the stated free-generator criterion. It includes every equal-weight
branch and every unequal type p<q<=2p. For other unequal weights, membership
of D outside [Q*C+L_(>p),Q*C+L_(>p)] is a finite rational test.

Consequently every target with first nonzero lower-central term in degree
three is decidable in every class. All normalized leading branches then
have type (1,2). The degree-two stratum was already covered. This adds
scope beyond the previous all-target class-ten bound and the six final
layers; it is still the same partial N8(b) candidate. A failure on covered
branches does not settle a target with an uncovered leading branch.

## Points checked in the proof

1. The graded-tail spaces used are Lie subalgebras. C,D are included in
   an actual homogeneous free basis only after checking their nonzero
   independent abelianization classes. The homogeneous Shirshov lemma is
   credited explicitly. It is not applied directly to arbitrary ambient
   Lie elements as if they were original basis letters.
2. The rational Lie algebra of the integral subgroup K is exactly the
   stated truncated graded-tail algebra. Its product coordinates consist
   of the actual lifts x0,y0 and the complete ambient Hall tail. They are
   unique even when the leading terms have nonunit contents.
3. Replacing homogeneous free generators by log(x0),log(y0) gives a
   filtered isomorphism by its associated graded map. This is the reason
   that the rational substitutions are genuine automorphisms.
4. Rational unipotent matrix powers are polynomial in the integer
   exponent. BCH and triangular collection give rational polynomial K
   coordinates with integer constant terms. Clearing nonconstant
   denominators makes BOTH positive and negative powers preserve K.
   This proves termination of the factorial search; the finite bound
   used in tests is not substituted for that proof.
5. The first pair increments are diagonal at simultaneous offset t,
   including unequal p,q. Higher tails cannot contribute to these first
   increments. All integral residue classes are retained.
6. The action group is finitely generated and nilpotent. The prior
   elementary orbit algorithm applies to the ambient weight filtration
   restricted to K; its kernel construction terminates by the explicit
   nilpotency bound. There is no invocation of a general equation oracle.

The complete leading-pair enumeration is an earlier dependency, with
its signed scales, oriented equal-weight sublattices and exact Nielsen
normalizations retained. No new finiteness claim about those pairs is
inferred from a bounded computation.

## Exact construction tests

`scripts/n8_weighted_automorphisms.py` uses rational coefficients in the
truncated free associative algebra with group generators exp(X_i).
This is a separate representation from the preceding integral 1+X_i
Magnus scripts. It constructs the ambient Hall basis, homogeneous free
generators of the graded-tail algebra, their actual filtered lifts,
rational substitutions, and integral powers with inverse images.

It does **not** implement the whole finite-union orbit decision procedure.
That procedure is proved in the accompanying argument. No high-class
end-to-end execution or practical complexity bound is claimed here.

The deterministic cases are:

| Ambient rank/class | Leading weights | Contents and purpose | Maps |
| --- | --- | --- | ---: |
| 2/4 | 1,2 | Primitive; every basis correction in every offset | 11 |
| 2/5 | 1,2 | Contents 2,3; integral-power obstruction | 7 |
| 3/5 | 2,2 | Contents 2,3; equal-weight subgroup | 6 |
| 2/6 | 2,3 | Contents 2,3; unequal weights | 7 |
| 2/6 | 1,3 | D=[[b,a],b] times 2; beyond q<=2p | 8 |
| 2/7 | 3,4 | Contents 2,3; deeper leading factors | 7 |

For cases other than the first, one Hall correction per permissible
degree and per factor is selected; these are not exhaustive map lists.
All 46 constructed maps pass 398 Lie-bracket identities, 2,412 integral
forward/inverse image checks, diagonal first-increment checks on pairs
with nontrivial tails, and commutator transport. The records retain 88
rejected smaller powers across these successful cases. These are actual
fractional K coordinates, not floating-point failures.

The initial case-1 run reached the deliberately imposed 8! search bound
and correctly returned inconclusive. It did not return a negative
mathematical answer. Increasing the test bound to 12! allowed all maps
to finish; the largest selected power was 9!=362880. This is an
inefficient sufficient exponent, not a claim of minimality. The first
source version and its partial records are retained separately.

There are nine scope controls across the successful cases: the ambient
generator outside K is rejected in every case, and the decomposable
D=[[b,a],a] is rejected as a would-be independent free generator in the
three applicable rank-two degree-one cases. In particular, the theorem
does not silently claim all degree-four target branches.

## Independent GAP checks

`scripts/check_n8_weighted_gap.g` rebuilds the free nilpotent quotients
using GAP/nq, evaluates the compact Hall products as group elements, and
constructs K as an actual subgroup. It verifies that every supplied image
belongs to K, calls `GroupHomomorphismByImages` for both directions, and
checks both compositions on all K generators. It then verifies the two
commutator witnesses and their transport in each case.

All 46 maps, 2,412 inverse-image equalities and 92 commutator witnesses
pass in 44.065 seconds. Five GAP parser warnings concern global variables
inside lambdas; the log is retained, and contains no runtime error.

The separate `scripts/check_n8_weighted_negative_gap.g` fixes a and
z=[b,a] but attempts to move d=[z,a] independently by the nontrivial
central factor [d,a]. GAP rejects the alleged homomorphism because
d=[z,a] is a genuine relation. The identity map is accepted. This tests
the essential freeness restriction independently of the Python basis
selection. It passes in 1.925 seconds with empty stderr.

Commands, timings, resource reservations, exit codes, markers and log
hashes are in `results/n8-weighted-*`. Each job used one CPU core and
8GB, except the main GAP replay which reserved 12GB. The five parallel
construction jobs together reserved at most five cores/40GB. All jobs
are terminal. No other computation was running.

## Statement, sources and limits

The original N8 HTML fragment, complete background paragraph and actual
archived statement rendering were reread/viewed. The full nilpotent
page and its statement metadata were already inspected in earlier N8
audits. Part(a)'s known negative result is not confused with free groups
in part(b). The old website's class-two status is not treated as a
current exhaustive literature search.

Bryant--Kovacs--Stohr2005 printed p147 was re-viewed: the exact ordinary
homogeneous Shirshov lemma is the imported structural ingredient. The
source is [the authors' archived paper](https://archives.maths.anu.edu.au/people/Kovacs/K110.pdf).
The proof of that classical lemma, and the classical Hall/Malcev
background, are not re-proved by these checks. The specific integral-power,
finite-pair and orbit arguments are written out.

Targeted current searches for free-nilpotent commutator equations,
same-weight factors and homogeneous free bases located the known class-two
results and the same ordinary Lie theorem; no precise matching extension
was located. This leaves novelty unverified. No Kourovka mathematics or
code was imported. Counts remain six whole-entry candidates, four partial
candidates, zero established novel results.
