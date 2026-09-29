# N8: the weight bound and the first overlapping offsets

29 September 2026, developed approximately12:21--12:26UTC. This is a
refinement of the same partial N8(b) candidate, not another candidate
entry. Specialist review and novelty remain unverified. The underlying
branch algorithm in `universal-gauge-proof.md` is unchanged and remains
unimplemented end to end; its exact substitutions have independent
finite group checks.

## 1. A lower weight bound

Use the notation of `universal-gauge-proof.md`: C,D have weights p<=q,
and A_t(U,V)=[U,D]+[C,V]. Suppose 0<t<q-p and ker A_t is nonzero.
Then

    q >= 3p+t,  equivalently t <= q-p-2p.             (1)

Indeed a nonzero kernel direction has U!=0, since the homogeneous
centralizer of C contains no element of weight q+t>p. The existing
inner-solution argument puts D and V in the free Lie algebra on C,U,
whose generator weights are p and p+t. Since q>p+t, D has neither a
pure-C component nor a component proportional to U. A nonzero Lie
monomial with at least two U letters has at least one C letter, hence
weight at least3p+2t. A monomial with exactly one U is an iterated C-adjoint
of U. Thus if q<3p+t the only possible nonzero D is a scalar multiple
of [C,U], of weight2p+t.

But then [U,D] has C,U multidegree(1,2). In [C,V] that component would
have to come from the multidegree(0,2) part of V, which vanishes in the
free Lie algebra on one letter U. The nonzero [U,[C,U]] cannot be canceled.
This contradiction proves (1). Equality is possible: D=ad_C^2(U), with
V=-[U,[C,U]], gives an actual kernel direction for our plus-sign convention.

If q-p<=6, (1) puts every exceptional offset in {1,2,3,4}. The existing
no-consecutive-exceptions lemma then implies separation t'>=2t, exactly
as in the previous gap-five argument. The universal branch theorem
therefore covers **all weight gaps <=6**, hence **all nonzero leading
target degrees <=8 in arbitrary class**. For c<=14, a target has either
d<=8 or c-d<=5, so the union with the previous deepest-six-layer theorem
covers **all targets in classes <=14**, in every finite rank.

No additional computation is needed to change the branch algorithm: the
new point is a sufficient hypothesis for the already proved separation
criterion. The finite checks below test the sharp weight boundary and
the first excluded offset pattern. They do not implement the full decision.

## 2. All later exceptional directions lie in one two-generator algebra

Here is a further structural lemma, not a claim that the overlap is solved.
Let t be the first nonzero pre-Nielsen offset, with direction(U,V).
For every later pre-Nielsen kernel direction(U',V'), both components lie
in B=Lie(C,U).

The prior argument gives a homogeneous free basis of

    A=Q*C+Q*U+direct_sum_(j>=p+t+1) L_j

which contains C,U, and puts D in B. A later U' belongs to A. Applying
the same inner-solution theorem at its own offset gives
D,V' in Lie(C,U'). Write D=P(C,U'), where the nonzero free Lie polynomial
P has a component involving its second variable; D has the wrong weight
to be a scalar multiple of C.

Grade the free algebra A by the number of letters outside its free basis
subset {C,U}. Suppose the highest such degree of U' is e>0, with nonzero
component E. The elements C,E do not commute: a centralizer of C is Q*C,
whereas E has positive outside degree. Consequently they freely generate
a two-generator Lie algebra. If k>0 is the largest number of second-variable
letters in P, the outside-degree ke component of P(C,U') is P_k(C,E),
which is nonzero by that freeness. This contradicts D in B. Therefore
U' has outside degree zero, so U' lies in B, and then V' does as well.

Every expression uses finitely many basis letters, so this highest-degree
argument also applies when the homogeneous free basis is infinite.
It is a support restriction only. It supplies neither an exact integral
substitution for an exceptional direction nor a solution of the resulting
coupled parameter equations.

## 3. An actual overlap, not just a hypothetical pattern

Take independent free Lie generators C,E of weights1,4 and put

    E_i=ad_C^i(E),       D=E_4  (weight8).

There are nonzero correction directions at offsets3 and5:

    offset3:  U=E,    V=-[E,E_3]+[E_1,E_2],
    offset5:  U=E_2,  V=-[E_2,E_3].

The derivation identity gives

    [C,[E,E_3]-[E_1,E_2]]=[E,E_4],
    [C,[E_2,E_3]]=[E_2,E_4].

Thus both pairs solve A_t=0. The intervening offset4 is injective by
the previous consecutive-offset lemma. Offsets3 and5 are therefore
successive exceptional offsets, and5<2*3. These kernels lie in the same
two-generator algebra, as Section2 predicts, but fail the separation
hypothesis.

This is also an example inside an ordinary free Lie algebra on a,b:
take C=a and E=[b,[b,[b,a]]]. Their different weights and nonzero bracket
make them free generators of their Lie subalgebra. The identities above
remain nonzero there. Thus the weighted example is not an artifact of
unavailable generator weights. Its target leading bracket has degree9.
We are not asserting that such a target has no solution; taking actual
group commutators of lifts already gives positive examples. The example
exhibits the obstruction to applying the current separation criterion.

## 4. Exact finite checks and audit limits

`scripts/check_n8_exceptional_boundary.py` independently enumerates all
weighted Lyndon bases, forms the complete correction matrices in the free
associative algebra over Z, and computes exact ranks with FLINT. An extra
free generator is included in every test so the kernels are not restricted
in advance to the two coefficients' Lie subalgebra.

| Weights of three generators | p,q | Complete tested offsets | Nonzero kernels |
|---|---|---|---|
| 1,3,4 | 1,7 | 1 through5 | 2,4 |
| 1,4,5 | 1,8 | 1 through6 | 3,5 |
| 2,4,5 | 2,6 | 1 through3 | none |
| 2,4,5 | 2,8 | 1 through5 | 2 |

Every nonzero kernel has dimension one. Five explicit directions, including
both overlapping ones, pass exact bracket identities. The constructor
passes in0.120seconds. `scripts/check_n8_exceptional_boundary_gap.g`
independently enumerates the bases and computes all19 ranks and5 identities
using GAP's native rational associative algebra. It imports the coefficient
expressions and expected dimensions, not Python matrices. It passes in
1.975seconds with empty stderr. The Python stderr is empty too; no failed
run occurred. Both jobs used1core/8GB sequentially and are terminal.

The finite inputs, dimensions, directions and SHA256 manifest are in
`research/certificates/N8-exceptional-boundary/`; the executed commands,
resource reservations and log hashes are in `results/n8-exceptional-boundary-*`.
These are weighted-Lie checks, not new group witnesses or a full overlap
decision algorithm. The symbolic embedding into the ordinary rank-two
free Lie algebra is justified above; no new complete rank-two matrix
enumeration is claimed.

The full frozen N8 HTML and linked background were reread in the preceding
universal-substitution work period, including an actual rendering view;
the source scope has not changed. The classical homogeneous free-basis,
centralizer and inner-solution dependencies retain their credits and
reading limits in that audit. No new literature proof or novelty guarantee
is asserted for this elementary weight refinement or support observation.
No Kourovka argument was imported. Counts stay8 whole/2 partial/0
established novel, under the original experiment deadline.
