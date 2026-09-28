# A decidable third-from-last-layer family in arbitrary class

Candidate extension, 28 September 2026. The first argument is retained in
`research/notes/N8-iterated-adjoint-stratum-lead.md`. **Under audit; not yet
added to the counted scope.** No full answer to N8(b), external specialist
review or established novelty is claimed.

**Theorem.** Let N=F_r/gamma_(c+1)(F_r), with finite r>=2 and c>=6. There
is an algorithm recognizing the following class of inputs and deciding
single-commutator membership, with constructive witnesses, on this class:
the target g has nonzero leading term w in degree c-2, and in the rational
free Lie algebra L this term has the form

    w=ad_z^(c-4)(T), z in L1 nonzero, T in L2 nonzero.       (1)

The two later homogeneous coordinates of g are unrestricted. Rational
z,T in the recognition condition do not authorize rational group factors:
all factors returned by the algorithm belong to the original integral
free nilpotent group. Unsupported inputs are explicitly distinguished
from negative decisions.

We use [x,y]=x^-1*y^-1*x*y and the integral Hall group coordinates, with
their associated graded integral free Lie ring. The previous central and
penultimate proofs give exact Nielsen normalization of leading factors,
the block-quadratic factor method, and finite integral leading scales.
Section 1 of `class9-proof.md` constructs a homogeneous free basis of L'
on which delta=ad_z shifts generators. Its two structural sources are the
ordinary homogeneous Shirshov lemma and torsion-freeness of the derived
module of the free metabelian Lie algebra; see that proof for precise credit.

## 1. The leading direction is unique

The image of T in M=L'/L'' is nonzero, and delta is injective on M.
Consequently the image of w in M is nonzero. A bracket whose factors both
have weight at least two lies in L'', so after the earlier exact Nielsen
normalization every possible pair has leading weights (1,q), q=c-3.

The direction of its first factor must be the direction of z. Here is an
explicit proof, also useful for recognizing (1). Make a rational linear
change of degree-one coordinates with z=a, and write

    T=a wedge b+T0,

where b is in the span of the other letters, and T0 uses only other
letters. Put k=c-4>=2. In the free associative algebra,

    ad_a^k(T)=sum_(i=0)^k (-1)^i binomial(k,i) a^(k-i) T a^i.

Fix an inner word J of length k and collect coefficients of the words
u*J*v, allowing the two outer letters to vary, into a commutative
quadratic Q_J. If w=[C,D] with C of degree one, then Q_J is divisible
by the linear polynomial C: the two products C*D and D*C each supply
that factor after making the outer variables commute.

If T0 has a nonzero coefficient t_bc on distinct other letters b,c,
take J=a^(k-2)*b*c. The inner word already has two non-a letters, so
the only possible outer letters are a,a. The coefficient is -k*t_bc,
nonzero. Thus Q_J is a nonzero multiple of a^2. If T0=0, choose a
letter with nonzero coefficient in b and take J=a^(k-1)*b. The same
calculation with ad_a^(k+1)(b) gives coefficient -(k+1) times that
coefficient, again a nonzero multiple of a^2. Every possible C is
therefore proportional to a. The argument is invariant under the
chosen rational change of basis.

To recognize (1), form all Q_J in the original basis and factor any
nonzero one over Q. Its linear factors give a finite list of possible
directions. For each primitive integral representative C0, solve

    ad_C0^(c-4)(T0)=w, T0 in L2(Q).

This is a rational linear system with injective linear map. It has at
most one solution, and there is at most one successful direction by
the preceding uniqueness argument. If none succeeds, the input is
outside this theorem's scope. This recognition precedes any integral
factor test; failure of integral factorization cannot be mistaken for
failure of rational scope recognition.

For a successful direction put D0=ad_C0^(c-5)(T0). If D0 has a
nonintegral Hall coordinate, there is no integral leading pair: such
a pair would have C=k*C0 with nonzero integer k and D0=k*D integral.
Return a negative decision in that case. Otherwise let h be the gcd
of the coordinates of the nonzero integral D0. Enumerate all signed
divisors k of h and the pairs

    C=k*C0, D=D0/k.

These are all integral leading pairs. Writing delta=ad_C for this
branch and n=c-5, we have D=delta^n(T) for T=T0/k^(n+1). T may be
rational. No bounded search for z or T, and no primitive-scale
assumption on the proposed factors, has been used.

## 2. The first correction kernel depends on parity

Fix one branch, and choose Hall group lifts x0,y0 of C,D. The next
homogeneous correction is the integer system with rational underlying map

    A: L2 + L_(q+1) -> L_(q+2),
       (U,V) |-> [U,D]+delta V,       D=delta^n T.          (2)

Use the delta-stable free alphabet of L' and choose T as a degree-two
seed. U has free-alphabet bracket length one and D is one generator.
Since delta preserves bracket length and is injective on L', a kernel
vector can have V only of bracket length two.

Separate the components by their seed counts. For distinct degree-two
seeds S,T, identify [delta^i S,delta^j T] with s^i*t^j. Delta acts as
multiplication by s+t. A component of U along S would require t^n
to be divisible by s+t, which is impossible. Thus U is proportional
to T. All other seed-pair components of V vanish by injectivity.

For the same seed T, identify [delta^i T,delta^j T] with
s^i*t^j-s^j*t^i. The vector [T,delta^n T] corresponds to t^n-s^n.
It is divisible by s+t exactly when n is even. The resulting quotient
is antisymmetric and represents an actual length-two Lie polynomial.
It follows that:

- For odd n, the kernel of (2) is zero.
- For n=2m, m>=1, it is the line Q*(T,-V_m), where

      V_m=sum_(i=0)^(m-1) (-1)^i [delta^i T,delta^(2m-1-i)T].

  The telescoping identity delta V_m=[T,delta^(2m)T] verifies the
  line directly. Injectivity of delta proves that there is no second
  independent kernel vector.

This is a proof in every rank and class, not an extrapolation from
the finite jet computations.

## 3. A uniform quadratic obstruction

For even n=2m, define Q_m=[T,V_m]. We claim that it is outside the
rational image of the final correction map

    B: L3 + L_(q+2) -> L_(q+3),
       (U,V) |-> [U,D]+delta V.                          (3)

Define a homomorphism from the free Lie algebra L' to the free Lie
algebra on A,B by sending each T_j=delta^j T to A+(-2)^j B and all
other seed chains to zero. It preserves free-alphabet bracket length
and intertwines delta with the derivation partial defined by
partial(A)=A, partial(B)=-2B. In the length-three part, take the
coefficient of [A,[A,B]]. Its partial eigenvalue is 1+1-2=0, so
this functional kills every delta V. It also kills [U,D]: L3 consists
of free generators of L', making that bracket length two.

Telescoping, or applying partial to delta V_m=[T,delta^(2m)T], gives

    image(V_m)=(1-4^m)[A,B].

Indeed partial acts by -1 on [A,B], whereas the image of the right
side is (4^m-1)[A,B]. Therefore the selected coefficient of the image
of Q_m is 1-4^m, nonzero. This proves the claim for every m>=1.
For m=2 it agrees with the separate degree-nine obstruction.

## 4. The group lifting is finite and complete

Solve the first integral correction system. If it is insoluble,
reject this leading branch. For odd n its rational kernel is zero,
so any solution is the unique integral solution. Apply it and solve
the final integral system (3). Any solution there constructs factors;
its kernel is immaterial because no further layer remains.

For even n, the full integral first solution set is v+k*K, k in Z,
where K is a primitive generator of the integral kernel. For some
nonzero rational rho, K=rho*(T,-V_m). Use ordered integral Hall lifts
to form x(k),y(k). Their commutators agree with the target through
degree c-1. The degree-c residual of [x(k),y(k)]^-1*g is an
integer-valued polynomial R(k) of degree at most two.

For clarity, the first correction weights are 2 and q+1. Their cross
term first occurs in weight q+3=c. Two weight-two corrections with
the weight-q base first contribute in q+4>c; two weight-(q+1)
corrections with the degree-one base first contribute in 2q+3>c.
The nonlinear terms of the ordered weight-two Hall lift have weight
at least four and also start affecting the commutator after c.
Thus the sole quadratic contribution through c is the cross term,
whose coefficient is, up to sign, rho^2*[T,V_m].

By Section 3 this coefficient survives modulo the rational image of
(3). A rational cokernel functional therefore gives a nonzero
quadratic equation in k, leaving at most two integer possibilities.
Integer Hermite/Smith reduction computes the full membership
conditions in the image lattice, including divisibility congruences;
checking rational membership alone is insufficient. Test the integer
roots against every condition and solve the final system for each
survivor. Recheck the produced commutator exactly.

There are finitely many leading scales and at most two first-kernel
parameters per exceptional branch. Every remaining operation is
effective rational/integer linear algebra or integer root finding.
The leading normalization and full solution lattices show completeness;
there is no arbitrary discarded choice from an infinite kernel.
This proves the stated terminating decision procedure, subject to
the explicitly cited earlier structural dependencies.

## 5. Evidence and limits

`scripts/n8_iterated_adjoint.py` implements scope recognition separately
from integral leading-pair enumeration and the two correction layers.
The homogeneous jet checker verifies parity and obstruction identities
for n=1,...,16; group checks and independent GAP replay are being
recorded in the accompanying audit. These finite checks support the
implementation and cannot establish the all-rank theorem by themselves.

The theorem covers only leading terms of form (1). It does not solve
all of gamma_(c-2), still earlier layers, or arbitrary-class N8(b).
It would extend the same single partial candidate, not add an entry.
