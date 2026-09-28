# A possible arbitrary-class third-layer stratum for N8(b)

First argument approximately 19:47--19:52 UTC, 28 September 2026.
**Uncounted proof lead.** Written while the class-nine computational audit
continues. It needs a separate proof audit, implementation and exact checks.
It is not a full arbitrary-class answer to N8(b).

The proposed scope is class c>=6, targets with leading degree c-2 whose
leading Lie term is

    w=ad_z^(c-4)(T),   z in L1 nonzero, T in L2 nonzero.     (1)

The correction analysis appears uniform in c. Put n=c-5>=1 and q=n+2=c-3.
Then w=[z,D] with D=ad_z^n T. Use the delta-stable free basis of L'
proved in the class-nine note, with T a degree-two seed.

## Only the leading direction z can occur

The image of w in L'/L'' is nonzero by torsion-freeness, so no leading
factorization has both factors of degree at least two. After the existing
exact Nielsen normalization, every possible pair therefore has type(1,q).

Take a rational basis with z=a and write T=a wedge b+T0, where T0 uses
only the other degree-one letters. Put k=c-4>=2. Expand

    ad_a^k(T)=sum_(i=0)^k (-1)^i binomial(k,i) a^(k-i) T a^i.

The leading-factor method associates a quadratic Q_J to each fixed inner
word J of length k, by allowing its two outer letters to vary. If a
coefficient t_bc of T0 is nonzero, choose J=a^(k-2)bc. The only possible
outer letters are a,a, and Q_J=-k*t_bc*a^2 is nonzero. Terms of T with
only one non-a letter cannot contribute. If T0=0, choose a nonzero
coefficient of b in T=a wedge b; then w=ad_a^(k+1)b and an inner word
a^(k-1)b similarly gives a nonzero multiple of a^2. Thus every possible
degree-one factor, which must divide Q_J, is proportional to a.

For each retained integral scale C, injectivity of ad_C on Lq makes D
unique, and it has the form ad_C^n(T') for a rational nonzero T' in L2.
Consequently all the finitely enumerated leading branches have the form
needed below. No unrestricted integral choice of z or T is required.

## First correction kernel for D=delta^n T

The map is (U,V) -> [U,D]+delta V on L2+L_(q+1).
The first bracket has length two in the free alphabet of L'. Since delta
preserves bracket length and is injective, V can have only length two.
Choose a degree-two seed basis containing T. In a component with distinct
seeds S,T, identify [delta^i S,delta^j T] with s^i t^j. The derivation is
multiplication by s+t. A component of U along S would require t^n to be
divisible by s+t, which is impossible. Therefore U is proportional to T.

In the same-seed component, identify [delta^i T,delta^j T] with
s^i t^j-s^j t^i. The target [T,delta^n T] corresponds to t^n-s^n.
This is divisible by s+t exactly when n is even. For n odd the kernel
is zero. For n=2m, m>=1, it is the line

    Q*(T,-V_m),
    V_m=sum_(i=0)^(m-1) (-1)^i [delta^i T,delta^(2m-1-i) T],
    delta V_m=[T,delta^(2m) T].                          (2)

Components involving any other seed pair vanish by injectivity of delta.

## Uniform quadratic obstruction when n is even

Let Q_m=[T,V_m]. It is outside the image of the final correction map

    L3+L_(q+2) -> L_(q+3), (U,V)->[U,D]+delta V.          (3)

Here is a uniform functional. Send every T-jet delta^j T to
A+(-2)^j B in the free Lie algebra on A,B, and every other seed chain
to zero. This intertwines delta with the derivation partial having
partial(A)=A and partial(B)=-2B. Project the resulting Lie polynomial
to the coefficient of [A,[A,B]]. This component has eigenvalue
1+1-2=0, so the functional kills delta V. It also kills [U,D], whose
free-alphabet bracket length is two, whereas the retained component
has length three.

The image of V_m is (1-4^m)[A,B]: this follows either by summing (2)
or applying partial, which has eigenvalue -1 on [A,B]. Hence Q_m has
coefficient 1-4^m, nonzero. This proves the obstruction in (3).
For m=2 the functional is three times (-3,1,2) on the class-nine
basis X,Y,Z, agreeing with that calculation.

## Intended finite lifting algorithm

There are precisely two correction layers after the leading target
degree c-2. For n odd, the first correction is unique if integral,
then the last layer is an integer linear system. For n even, retain
the full primitive integral first kernel, v+kK. The final residual is
an integer-valued quadratic in k, with nonzero rational cokernel
coefficient by (3). There are at most two integer values to test,
followed by the full last-layer integer system. Its kernel is harmless
because there are no later layers.

The group weight estimates are the same in every class: the two first
correction weights are 2 and q+1, so their cross term has weight q+3=c.
The first self-interaction with the opposite base has weight q+4>c,
and the other self-interaction has weight 2q+3>c. Nonlinear terms of
ordered weight-two Hall lifts also start too late. Thus the degree
bound and nonzero quadratic coefficient do not depend on a low-class
calculation.

Pending: audit the leading-direction argument, implement the complete
integral branch enumeration for this scope, test c=10,11 (at least),
and obtain independent word/lattice checks before updating any claim.
