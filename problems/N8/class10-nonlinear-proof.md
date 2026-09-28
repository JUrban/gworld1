# A nonlinear third-from-last-layer family in class ten

Candidate extension, 28 September 2026. This is an extension of the same
partial N8(b) investigation, not a solution for every class-ten target or
for arbitrary nilpotency class. The first lead is preserved in
`research/notes/N8-class10-nonlinear-kernel-lead.md`. Independent specialist
and novelty review remain outstanding.

**Proposed theorem.** Let N=F_r/gamma_11(F_r), with finite r>=2. There is
an algorithm recognizing the following targets g and deciding whether
they are single commutators in N, with constructive integral factors:
the nonzero leading term w of g has degree eight and, in the rational
free Lie algebra L, has the form

    w = rho [z, P_z(T)],   0 != z in L1, 0 != T in L2, 0 != rho in Q,
    P_z(T) = 2[T,ad_z^3 T] + 3[ad_z T,ad_z^2 T].            (1)

The degree-nine and degree-ten target coordinates are arbitrary.
The rational recognition condition does not permit rational group
factors. Inputs outside (1) are distinguished from negative decisions.

Use [x,y]=x^-1 y^-1 x y and the associated integral Hall Lie ring.
The exact Nielsen normalization of leading group factors is the one in
`penultimate-target-proof.md`: every nontrivial commutator admits leading
terms C,D with [C,D] nonzero. The finite leading-scale argument is also
reused below. The homogeneous delta-stable free alphabet of L' is
constructed and credited in section 1 of `class9-proof.md`. These are
dependencies on the earlier N8 arguments, not new external theorems.

## 1. The leading type and direction are forced

Put delta=ad_z and T_j=delta^j T. The derivation rule gives

    w/rho = 2[T_0,T_4] + 5[T_1,T_3].                     (2)

In the delta-stable free alphabet of L', choose T as a weight-two seed.
Its jets T_j are independent free generators of weights 2+j. Expression
(2) has nonzero bracket-length-two components of alphabet weight types
(2,6) and (3,5). If both C,D had original weights at least two, then
their bracket-length-two component would come from their length-one
components, and have only the one weight type (weight(C),weight(D)).
It cannot equal (2). Thus normalized leading factors have weights (1,7).

Their degree-one direction is uniquely Qz. To prove this, make a rational
change of degree-one basis with z=a and write T=[a,b]+T', where b and T'
use only the other degree-one letters. For a fixed inner word J of length
six, collect the coefficients of u J v into a commutative quadratic Q_J
in the two outer letters. If w=[C,D] with C of degree one, then C divides
every Q_J: this follows separately for the products CD and DC.

If T' has a nonzero coefficient t_bc on distinct other letters b,c,
choose J=a b c a b c. Every monomial of (2) contains four explicitly
inserted a letters. J already contains four non-a letters, so its outer
letters must both be a. Expanding the derivations gives

    Q_J = -15 rho t_bc^2 a^2 != 0.                       (3)

Only the formal monomial a^2 T a T a can contribute; its coefficient
in (2) is -15. Terms using [a,b] instead of T' cannot contribute, by
the non-a-letter count. If T'=0, choose b as a new basis letter, so
T=[a,b]. Then (2) is 2[ad_a b,ad_a^5 b]+5[ad_a^2 b,ad_a^4 b].
For J=a b a^3 b its outer quadratic is

    Q_J = 20 rho a^2 != 0.                              (4)

For example, the coefficient of a^2 b a^3 b a is
2(-10)+5(8)=20. Its two b letters already occur in J. Again no other
outer letters can occur. Equations (3)–(4) force every C to be
proportional to a. This conclusion is invariant under the rational
basis change. For a fixed nonzero C in L1, ad_C is injective on L7,
so D is also determined.

## 2. Recognition uses linear algebra and a rank-one test

Compute the outer quadratics in the original basis and factor any
nonzero one over Q. Each rational linear factor supplies a possible
direction, represented by a primitive integral vector C0. The preceding
argument ensures a nonzero quadratic exists for every target in (1).

For each direction solve ad_C0(D0)=w over Q. This is an injective linear
system. To recognize D0 as a scalar multiple of P_C0(T), polarize the
quadratic map P_C0 on E=L2:

    Phi: Sym^2(E) -> L7,   Phi(t tensor t)=P_C0(t).

This map is injective. Choose any basis e_i of E as the weight-two seeds
of the delta-stable alphabet. The coefficient of the associative word
(e_i)_0 (e_j)_3 in Phi(S) is 2 S_ij, with the symmetric-matrix convention
S_ij=t_i t_j on t tensor t. The other summand of P has jet pattern (1,2)
and cannot cancel this coefficient. Thus all entries of S are recovered.

Compute S by a rational linear system. A nonzero symmetric S represents
rho t t^T with rational rho,t exactly when rank(S)=1. Indeed, choose a
nonzero diagonal entry S_ii, put rho=S_ii and t_j=S_ji/S_ii. A nonzero
symmetric rank-one matrix has such a diagonal entry, and S=rho t t^T.
No decision oracle for arbitrary rational quadratic equations is used.
The scalar rho permits both signs and avoids a spurious rational-square
restriction. There is at most one successful degree-one direction.

If D0 has a nonintegral Hall coordinate, return a negative decision:
an integral leading pair would have C=k C0, D=D0/k, where k is a nonzero
integer, forcing D0 integral. Otherwise let h be the gcd of its coordinates.
All integral leading pairs are precisely

    C=k C0, D=D0/k,     k a signed divisor of h.          (5)

Each branch still has D=sigma P_C(T) for a nonzero rational sigma:
changing C0 to k C0 multiplies P by k^3, while D is divided by k.
We therefore retain every integral scale and can use the structural
argument below with delta=ad_C. Rational scope recognition takes place
before this integral test.

## 3. The first correction kernel is one-dimensional in every rank

Fix a branch and write D=sigma P_C(T), T_j=delta^j T. Put

    V=2[T_0,[T_0,T_2]]-[T_1,[T_0,T_1]].                 (6)

Leibniz and Jacobi give delta V=[T_0,P_C(T)]. For completeness,
the derivative of the first summand is
2[T_1,[T_0,T_2]]+2[T_0,[T_1,T_2]]+2[T_0,[T_0,T_3]];
the derivative of the second is
-[T_2,[T_0,T_1]]-[T_1,[T_0,T_2]]. Jacobi combines the remaining two
terms into a third copy of [T_0,[T_1,T_2]], giving the identity.

The first correction map is

    A: L2 + L8 -> L9,   (U,W) |-> [U,D]+delta W.

Its kernel is exactly Q*(T,-sigma V). Here is the exclusion of all
other directions, which does not rely on the rank-two test. Include T
in a basis of E=L2 and consider any other seed S in that basis. Project
the associative expansion onto words with seed sequence S,T,T, allowing
arbitrary jet indices. Identify these words with monomials u^i s^j t^k.
The derivation delta becomes multiplication by u+s+t. The component of
[S,P_C(T)] becomes

    2(t^3-s^3)+3(st^2-s^2t)
       = (t-s)(2t+s)(t+2s),                             (7)

a nonzero polynomial independent of u. It is not divisible by u+s+t,
as substitution u=-s-t shows. Thus the coefficient of S in U must be
zero. Different S give independent seed-count components, and U has no
other components since it has degree two. Therefore U is proportional
to T. Identity (6) gives the partner W, uniquely because delta is
injective on L'. This proves the asserted one-dimensional kernel.

## 4. The quadratic obstruction survives the last correction

The final homogeneous correction map is

    B: L3 + L9 -> L10,   (X,Y) |-> [X,D]+delta Y.

We claim [T,V] is outside its rational image. Map the free Lie algebra
on the delta-stable alphabet to the free Lie algebra on A,B by

    T_j |-> A+(-3)^j B,

and kill all jets of every other seed. This intertwines delta with
the derivation Delta(A)=A, Delta(B)=-3B. In the enveloping free
associative algebra, let ell be the coefficient of AAAB after this map.
Delta kills that coefficient, since 3-3=0. Every L3 element has
alphabet length one, so [L3,D] maps to length three and also has
zero ell. Hence ell vanishes on image(B).

Direct expansion of (6) gives

    image(V)=20[A,[A,B]]+4[B,[A,B]],
    ell([T,V])=20 != 0.                                (8)

Multiplying by the nonzero scalar sigma does not change the obstruction.
These evaluations and the identity in (6) have also been checked using
a separate, untruncated associative-word implementation.

## 5. Complete integral lifting is finite

Lift each integral pair (5) by ordered Hall group words x0,y0. Match the
degree-nine target by the integral linear map A, using a full integer
lattice calculation. If it is insoluble, discard the branch. Otherwise
its solutions form one affine integral line, parameterized by k in Z
using a generator of the entire integral kernel, not a saturated
approximation or an arbitrarily chosen rational kernel vector.

Apply those corrections as ordered Hall words. The degree-ten residual
is a vector-valued rational polynomial R(k), integer-valued on Z, of
degree at most two. This follows by weights: the variable corrections
have weights two and eight, so their mutual bracket is the only
quadratic contribution of weight at most ten. Two weight-two corrections
and the weight-seven second factor already have weight eleven. Effects
involving the fixed weight-one factor are linear at this stage.

The quadratic coefficient modulo image(B) is a nonzero scalar multiple
of [T,V], by the kernel in section 3. Section 4 proves it is nonzero.
Consequently a rational linear functional annihilating image(B) yields
a nonzero quadratic equation in k. It has at most two integral roots,
all effectively computable. For each, decide membership of R(k) in the
full integral image lattice of B and construct corrections if possible.
All operations terminate. Every group solution has a normalized leading
pair (5), occurs in a full first-correction lattice, and passes the final
lattice test, so no solution is lost.

The implementation is `scripts/n8_class10_nonlinear.py`. It uses exact
Magnus expansions for group arithmetic, complete integer Hermite
transformations, and Newton-polynomial lattice certificates. It returns
`None` outside (1), rather than incorrectly answering `False` there.
Bounded tests are evidence about the implementation and are not a proof
for untested ranks or inputs. See the accompanying audit for their scope.
