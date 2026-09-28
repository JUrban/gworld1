# A second decidable family in unbounded nilpotency class

Candidate extension, 28 September 2026. The first argument is retained in
`research/notes/N8-degree-two-iterated-adjoint-lead.md`. This belongs to the
same partial N8(b) investigation. Independent specialist review and novelty
assessment remain outstanding; arbitrary-class N8(b) is not settled.

**Theorem.** Let c=2n+7 with n>=1, and let N=F_r/gamma_(c+1)(F_r), with
finite r>=2. There is a terminating algorithm recognizing inputs g whose
nonzero leading term, in degree c-2 of the rational free Lie algebra L, is

    w=ad_C^(n+1)(T),  0 != C in L2,  0 != T in L3.       (1)

On these inputs it decides whether g is a single commutator and returns
integral group factors when the answer is positive. The two later layers
of g are unrestricted. Rational C and T are allowed in the recognition
condition, but the requested factors belong to N, not its rational hull.
An input outside this family is distinguished from a negative decision.

Use [x,y]=x^-1*y^-1*x*y, integral Hall coordinates and the associated
graded free Lie ring. Put delta=ad_C, D=delta^n T, and q=2n+3=c-4.
Thus the proposed leading factor weights are (2,q).

Dependencies from the earlier proofs are explicit: exact Nielsen
normalization and enumeration of integral leading scales are in
`penultimate-target-proof.md`; the block-quadratic method and its rotation
lemma, deduced from Klyachko's Lie idempotent theorem, are in
`central-target-proof.md`. The homogeneous free basis used below is from
Section 1 of `class9-proof.md`, using the ordinary homogeneous Shirshov
lemma and torsion-freeness of the free-metabelian derived module. The
archived primary sources and precise statements are credited there.

## 1. Excluding degree-one factors

Fix any nonzero z in L1. Write partial=ad_z and use the partial-stable
homogeneous free alphabet of L' constructed in `class9-proof.md`.
Its weight-two and weight-three generator spaces are E=L2 and B=L3.
Partial shifts generators, preserves bracket length in this alphabet,
and is injective on L'. In this paragraph k=n+2, so w has alphabet
length k and original degree 2k+1.

Suppose w=[z,V]. Since partial is injective and preserves alphabet
length, V must have length k. Its original degree is 2k, the minimum
possible for that length. Consequently V lies in Lie_k(E). Its derivative
has exactly one B letter, belonging to partial E. Projecting B modulo
partial E shows that T must belong to partial E: otherwise the projection
of w is the nonzero free Lie word ad_C^(k-1)(Tbar), whereas that of
partial V vanishes. Write T=partial S with S in E.

Replace each partial E letter by its E antecedent. The image of partial V
is kV, since every one of its k letters is differentiated once. The image
of w is ad_C^(k-1)S. Hence necessarily

    V=(1/k)*ad_C^(k-1)S.                                (2)

If S is proportional to C, this is zero, a contradiction. Otherwise
include C,S in a basis of E; partial C and partial S are independent
B letters. In the associative expansion of
partial(ad_C^(k-1)S), the word

    (partial C) C^(k-2) S

has coefficient one. It comes from differentiating the first C in
C^(k-1)S; every other term has a different position for S or the
differentiated letter. But k*ad_C^(k-1)(partial S) has no partial C
letter. This contradicts (2). No nonzero degree-one z can therefore be
a leading factor of w.

## 2. The only leading type and direction

Apply the earlier exact commutator-preserving Nielsen normalization to
any group solution. The leading bracket is nonzero, so its weights p<=q'
sum to c-2. Section 1 excludes p=1; both leading factors lie in L'.

Choose a homogeneous free basis of L' containing C and T as generators
of weights two and three. Project onto the free Lie algebra on C,T,
killing all other generators. The target survives and has T-count one.
A homogeneous element of original degree greater than two has either
zero projection or positive T-count, since the free Lie algebra on C
alone is just QC. If both leading weights were greater than two, their
bracket would have T-count at least two, impossible. The weights are
therefore precisely (2,q).

If w=[C',D'] and C' in L2 is not proportional to C, quotient the free
algebra L' by the generator direction C'. Choose the E basis to contain
both C and C', and the B basis to contain T. The target (1) remains
nonzero while [C',D'] becomes zero. This contradiction proves that C'
is on the line QC. Its partner D' is then uniquely determined, since
ad_C is injective in degrees greater than two.

## 3. Effective recognition and all integral scales

For a target leading term of degree c-2, form the block quadratics
Q_J of the central-target proof with outer blocks of length two. For
any leading pair (C,D) they have the factor C. At least one is nonzero:
otherwise D would be invariant under a proper rotation of its tensor
positions, contradicting the credited rotation lemma.

Factor a nonzero Q_J over Q. Each rational linear factor gives a possible
line, which is tested for membership in L2. On each surviving line choose
the primitive integral Hall representative C0 and solve the finite rational
linear system

    ad_C0^(n+1)(T0)=w,  T0 in L3.

Injectivity gives at most one T0 per line, and Section 2 gives at most one
successful line. If there is none, the input is outside the theorem's
scope. This test is independent of integrality of the eventual factors.

Put D0=ad_C0^n T0. If D0 is not integral, no integral leading pair exists:
such a pair would require C=kC0 with nonzero integer k and D0=kD.
Otherwise let h be the positive gcd of D0's Hall coordinates. The full
list of integral pairs is

    (C,D)=(kC0,D0/k),  k a signed divisor of h.

For this branch write T=T0/k^(n+1), so D=ad_C^n T. This T can be rational.
Both signs and all scale allocations are retained.

## 4. A free alphabet shifted by ad_C

Write a homogeneous free basis of L' as {C} union S. Let J be the ideal
generated by S. It is free on the jets delta^j s, s in S and j>=0.
Here is a direct justification sufficient for the argument.

The Lie subalgebra generated by the jets contains S and is stable under
delta. Its sum with QC is a Lie subalgebra containing every generator of
L', so it is all of L'. The ideal is consequently precisely the jet
subalgebra. For freeness, embed in the associative algebra on {C} union S.
On the finite alphabet involved in any proposed relation, order C below
the S letters and use degree-lexicographic order. The leading word of
delta^j s is (-1)^j s C^j. Products of these words have unique decoding
at their non-C letters. Distinct products of jets therefore have distinct
leading words; taking the largest one in any finite relation proves
associative freeness, hence Lie freeness.

All homogeneous components of original degree other than two belong to
J; in degree two the complement is QC. Delta shifts the jet alphabet and
preserves its bracket length and seed counts. It is injective on J:
the centralizer of the free generator C in the free Lie algebra L' is QC,
as follows directly by commuting associative words with C.

## 5. The first correction kernel

Choose integral Hall group lifts x0,y0 of one leading pair. The first
correction has underlying rational map

    A: L3 + L_(q+1) -> L_(q+3),
       (U,V) |-> [U,D]+delta V,  D=delta^n T.             (3)

In the jet alphabet, U is a linear combination of weight-three seeds,
and D is one T-jet. Injectivity and preservation of alphabet length show
that a kernel vector has V only of length two. Separate seed counts.
For distinct weight-three seeds S,T, identify
[delta^i S,delta^j T] with s^i t^j. Delta is multiplication by s+t;
t^n is not divisible by s+t. Thus U has no component outside QT.
Components of V on other seed pairs vanish by injectivity.

For the T,T pair, identify the bracket with s^i t^j-s^j t^i.
The expression [T,delta^n T] corresponds to t^n-s^n. This is divisible
by s+t exactly for even n. The quotient is antisymmetric and hence an
actual length-two Lie polynomial. Therefore the kernel of (3) is zero
for odd n. For n=2m>=2 it is exactly the line Q*(T,-V_m), where

    V_m=sum_(i=0)^(m-1) (-1)^i [delta^i T,delta^(2m-1-i)T].

The identity delta V_m=[T,delta^(2m)T] also verifies this line by
telescoping. This proves the parity statement in every finite rank.

## 6. The final quadratic obstruction

For even n=2m, the final correction map is

    B: L4 + L_(q+2) -> L_(q+4)=Lc,
       (U,V) |-> [U,D]+delta V.                          (4)

Send the free jet generators T_j=delta^j T to A+(-2)^j B in the free
Lie algebra on A,B, and all other seed jets to zero. This homomorphism
intertwines delta with the derivation partial(A)=A, partial(B)=-2B.
Take the coefficient of AAB in the associative expansion of the image.
Partial multiplies that coefficient by 1+1-2=0, so it kills every
delta V. It also kills [U,D] for U in L4. Indeed a surviving single
T-jet has odd original degree 3+2j, and two such jets have degree at
least six; no element of original degree four has a nonzero image.

The image of V_m is (1-4^m)[A,B]. This follows either by telescoping or
by applying partial to delta V_m=[T,delta^(2m)T]: partial has eigenvalue
-1 on [A,B], and the image of the right side is (4^m-1)[A,B]. Consequently
the selected AAB coefficient of [T,V_m] is 1-4^m, which is nonzero.
Thus [T,V_m] is outside the rational image of (4).

## 7. Finite integral lifting

Solve the first correction over the full integral Hall lattice. If it
is insoluble, reject this leading branch. For odd n its kernel is zero;
apply the unique solution and solve the final integer system (4).

For even n, the integral first solution set is v+kK, k in Z, with K a
primitive generator of its integral kernel. Write K=rho*(T,-V_m) for
nonzero rational rho. Ordered integral Hall lifts give x(k),y(k), whose
commutators agree with g through degree c-1. Their degree-c residual is
an integer-valued polynomial R(k) of degree at most two.

The first correction weights are 3 and q+1. Their cross term has weight
q+4=c. Two weight-three corrections interacting with the weight-q base
first occur in weight q+6>c; two weight-(q+1) corrections with the
weight-two base occur in weight 2q+4>c. Nonlinearities inside an ordered
weight-three Hall lift start in weight six, also too late. Conjugating
the leading commutator by a first correction starts beyond c. Thus the
only quadratic term through c is the cross term, with coefficient,
up to sign, rho^2[T,V_m].

Section 6 gives a rational cokernel functional producing a nonzero
quadratic equation in k, leaving at most two integer possibilities.
Hermite or Smith reduction checks all lattice congruences, as well as
rational membership; it is not enough to test the latter alone. For
each survivor solve the full final integer system, allowing its entire
kernel, and recheck the resulting group commutator exactly.

There are finitely many leading scales and at most two exceptional
parameters per scale. All other operations are finite rational/integer
linear algebra or integer root finding. Exact leading normalization
and use of full correction lattices prove completeness. This establishes
the stated algorithm, with the earlier structural dependencies above.

The restriction n>=1 is intentional: n=0 is the older type-(2,3) Nielsen
kernel and has V_0=0, so the present obstruction does not apply. The
theorem covers a particular family in every odd class c>=9, not every
target in gamma_(c-2). Its class-nine instance overlaps the earlier
all-target result; classes eleven and above extend the partial scope.
