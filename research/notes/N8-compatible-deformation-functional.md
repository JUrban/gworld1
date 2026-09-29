# A separating functional for an early-compatible Lie deformation

29 September 2026, approximately 16:33--16:40 UTC. A supporting algebraic
lemma and an unadopted research lead. This is not a solution of general
N8 or an additional candidate. No novelty is asserted for the lemma.

The earlier single deformation probe left open whether *some other*
compatible fixed deformation could absorb the same quadratic. A complete
seven-case calculation suggests a simple uniform obstruction in this
restricted model. The argument below proves that obstruction without
extrapolating from the finite ranks.

## Lemma

Let L be the free Lie algebra over Q on E0,E1,..., embedded in its free
associative algebra. Let delta be the derivation delta(Ei)=E(i+1), and
let Lj mean the subspace with exactly j occurrences of the generators E.
For an even integer k>=2 put

    V = sum_(i=0)^(k/2-1) (-1)^(i+1) [Ei,E(k-1-i)],
    Q = [E0,V].

Thus delta(V)=-[E0,Ek]. If F1,...,Fr belong to L2 and

    [E0,Fj] belongs to delta(L3)       for every j,

then Q does not belong to

    delta(L3) + span_Q{[E(n_j),Fj] : j=1,...,r},

for any nonnegative integers n_j. Homogeneous matching degrees can be
imposed if desired; the separating functional works without that restriction.

## Proof

Identify a tensor E_i E_j E_l with the commutative monomial x^i y^j z^l
as a *linear vector-space encoding*. This is not an algebra homomorphism
from the whole noncommutative tensor algebra. On tensors of length three,
delta becomes multiplication by x+y+z. Consequently evaluation at

    (x,y,z)=(1,-2,1)

defines a rational linear functional ell that vanishes on delta(L3).

A length-two Lie polynomial F is encoded by an antisymmetric polynomial
f(x,y). The encoding of [E0,F] is f(y,z)-f(x,y). Its assumed membership
in delta(L3) implies

    f(-2,1)=f(1,-2).

Antisymmetry makes both values zero. More generally the encoding of
[En,F] is x^n f(y,z)-z^n f(x,y), so its ell-value is zero for every n.

The encoding of V is

    v(x,y)=(x^k-y^k)/(x+y).

This is a polynomial because k is even; expanding the alternating
geometric sum gives exactly the stated V. The encoding of Q is
v(y,z)-v(x,y), and hence

    ell(Q)=v(-2,1)-v(1,-2)=2(1-2^k) != 0.

The proposed span is annihilated by ell, whereas Q is not. This proves
the lemma. In particular every rational linear combination of all
compatible deformation columns is excluded, not only one selected column.

## Exact scope of the weighted test

Use the free Lie algebra on a,e with weights(1,4), and Ei=ad_a^i(e).
For q=8,10,...,20 take D=E(q-4), C=a. The first exceptional offset is3,
and the next one is5. The fixed next component F=D1 has weight q+1.
Its part with two e's has E-index sum q-7. The first successor condition
in its three-e component is

    [E0,F] + ad_a(V4)=0.

The two-e part of the first-coordinate correction cannot contribute to
this equation: that input has weight5<8, so it contains at most one e.
Likewise, at the quadratic offset6 the first-coordinate input has
weight7<8. Thus the three-e part of the full correction image there is
precisely ad_a of the corresponding three-e component. The later offset5
column contributes [E2,F]. The lemma separates the quadratic Q from the
entire space of these compatible columns for every even q>=8, not just
the seven values tested.

This is a statement about this Lie deformation model. It does not show
that an arbitrary actual group branch has precisely these inputs. Fixed
earlier components of the first factor, propagation through several
intermediate layers, other exceptional offsets and full integral group
normalization need separate treatment. In particular it does not establish
that quadratic absorption is impossible in general. The existing three-
exception proof still retains and treats that possibility.

## Independent finite evidence

GAP uses the native rational free associative algebra on a,e and complete
multidegree Lyndon bases. It computes the entire kernel of the first-
successor system, projects it to the deformation space, and compares all
resulting later columns with the full relevant correction image.

Python independently uses tensors in the formal E_i generators, the shift
derivation, exact rational kernels and FLINT ranks. This representation is
different from expanding each E_i into a,e words. It reconstructs all seven
spaces, agrees with the GAP dimensions/ranks, and checks ell on every late
image and every compatible column.

| q | two-e deformation dimension | compatible dimension | ranks A, A+Q, A+B, A+B+Q |
|---|---:|---:|---|
|8|1|0|2,3,2,3|
|10|2|1|5,6,6,7|
|12|3|1|9,10,10,11|
|14|4|1|15,16,16,17|
|16|5|2|22,23,24,25|
|18|6|2|30,31,32,33|
|20|7|2|40,41,42,43|

The GAP run takes5.79 seconds and the independent Python run0.87 seconds,
each with one core/4GB and empty stderr. Records are under
`results/n8-successor-compatible-space{,-python}-v1/`; certificates are
`research/certificates/N8-successor-compatible-space-v1.g` and
`research/certificates/N8-successor-compatible-space-python-v1.json`.
Both runs pass. No actual group witness, complete branch decision or
additional result count follows from this probe.
