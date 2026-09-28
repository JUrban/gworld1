# Every gamma_8 target in free nilpotency class ten

Candidate extension, 28 September 2026. This extends the same partial
N8(b) investigation. It does not decide every class-ten target or the
arbitrary-class problem. Independent specialist and novelty review remain
outstanding. The initial lead is retained separately.

**Theorem claimed.** In N=F_r/gamma_11(F_r), with any finite rank r,
single-commutator membership is decidable for every input g in gamma_8(N),
and positive answers come with integral group factors.

Use [x,y]=x^-1 y^-1 x y and the free integral Hall Lie ring L associated
to the lower-central series. Ranks zero and one and the identity are
immediate. The previous central/penultimate algorithms cover gamma_9,
so assume that g has nonzero degree-eight leading term w.

The normalization and finite integral leading-pair enumeration in
`penultimate-target-proof.md` reduce the problem to finitely many pairs
C in L_p, D in L_q, with [C,D]=w and

    (p,q) = (1,7), (2,6), (3,5), or (4,4).

In the last case C,D are independent. Unequal-weight enumeration retains
all signed divisors of the content of the second factor; equal-weight
enumeration retains all oriented leading-plane sublattices modulo exact
commutator-preserving Nielsen moves. No rational group factors are used.

The new step is to classify the first correction kernels

    A_(p,q): L_(p+1) + L_(q+1) -> L9,
             (U,V) |-> [U,D]+[C,V].                    (1)

All Lie-algebra reasoning below is over Q. The lifting algorithm then
uses full integral solution lattices.

## 1. A fresh-letter fact

Let T be the free associative algebra on old letters including a, and
let t be a new letter. If P belongs to T and

    [t,P] belongs to [a,T(old letters,t)],

then P belongs to Q[a]. Here [a,T] denotes the image of the linear
commutator map, not the two-sided ideal it generates.

Project onto words with exactly one t. The vector-space quotient by
[a,T] has a basis of word classes under moving an initial a to the end
or the inverse move. A canonical representative is obtained by moving
the whole initial a-run to the end. Equivalently, the ordered string
of non-a letters and every intervening a-run are fixed, and the two
exterior a-runs are replaced by their sum at the end. This proves both
existence and uniqueness of these representatives.

Every monomial in tP is already canonical and keeps its separate
coefficient. If a monomial of P contains any old letter other than a,
the canonical representative of its contribution to Pt starts with
that other letter. It cannot cancel a tP representative, which starts
with t. Thus all such coefficients of P vanish. Pure a powers give
the same representatives on both sides and impose no restriction.
This proves the fact. In particular, if P is a homogeneous Lie element
of bracket length greater than one in the old alphabet, then P=0.
Extra letters in the presumed preimage can be removed by projection
to their count-zero components.

## 2. Free-alphabet conventions

Use a homogeneous free basis of the derived Lie algebra L', with spaces
E,B,W,G,H,J of free generators of original weights 2,3,4,5,6,7. Thus

    L2 = E,                       L3 = B,
    L4 = W + Lambda^2 E,           L5 = G + [E,B],
    L6 = H + [E,W] + Lambda^2 B + Lie_3(E),
    L7 = J + [E,G] + [B,W] + Lie_(2E,1B).

These are direct decompositions by free-alphabet length and letter
weights. The homogeneous free-basis result is credited and proved in
the earlier class-seven/nine arguments; it is not inferred from finite
computations here.

When C=z lies in L1, use the delta-stable basis from Section 1 of
`class9-proof.md`, where delta=ad_z. Its generators consist of seeds
and all their successive delta images. Delta preserves alphabet length
and seed counts and raises a jet index by one. The construction uses
the credited torsion-free free-metabelian module theorem and homogeneous
Shirshov freeness. In particular any chosen nonzero U in E can be made
a seed by a rational basis change in E.

We use two elementary free-alphabet observations: a free generator
commutes with no homogeneous Lie word of bracket length greater than
one; and commuting equal-length associative tensors are proportional
(split the product into its two equal-sized blocks). Both also hold
after a linear basis change in one free-generator space.

## 3. Complete classification of type (1,7)

Fix nonzero z in L1 and D in L7. Suppose [U,D]+delta V=0 with U in E
and V in L8. If U=0, injectivity of ad_z on L' gives V=0. Otherwise
choose U as a weight-two seed and write U_i=delta^i U. Decompose D by
free-alphabet length, which is at most three.

For fixed ordered seed sequence, encode associative jet words by
commuting monomials in one variable per position. Delta then becomes
multiplication by the sum of those variables. Consequently every
component of [U,D] must be divisible by that sum. This is a necessary
condition in the full associative algebra, not an assertion about
sufficiency for a Lie preimage.

For length-one D, a seed S other than U gives the U,S sequence with
a polynomial independent of the first jet variable. It cannot be
divisible by their sum unless zero. The only remaining possibility
is a multiple of U_5. Its commutator polynomial is v^5-u^5, which
does not vanish at v=-u and hence is not divisible by u+v. Thus this
part of D vanishes.

For length-two D, first consider a component using no U seed. The
U,S,T sequence in [U,D] has coefficient polynomial independent of the
first variable, and is therefore zero. This includes S=T. A component
using one U seed and one other seed S is excluded in exactly the same
way by the U,U,S sequence: its coefficient is the U,S polynomial of D,
independent of the first variable. No term of -DU contributes to either
of these selected sequences. Thus D uses only two copies of the U seed.
Its original weight seven gives the basis

    [U_0,U_3], [U_1,U_2].

The possible corresponding V has length three, weight eight, and only
the U seed. Its basis is

    A=[U_0,[U_0,U_2]],       B0=[U_1,[U_0,U_1]].

In the degree-nine basis

    X=[U_0,[U_0,U_3]],
    Y=[U_1,[U_0,U_2]],
    Z=[U_0,[U_1,U_2]],

the derivation rule and Jacobi identity give delta A=X+Y+Z and
delta B0=2Y-Z. Therefore c0 X+c1 Z has a Lie preimage exactly when
c1=3c0/2. This forces the surviving part of D to be proportional to

    P_z(U)=2[U_0,U_3]+3[U_1,U_2].                     (2)

It remains to exclude length-three D. Its partner V has length four
and weight eight, so belongs to Lie_4(E). Work one E-seed multidegree
at a time; delta and the equation preserve seed counts. Every nonzero
component of V uses at least one seed other than U, because Lie_4(Q U)
is zero. In the equation substitute delta U -> 0, delta S -> S for
every other E seed, and kill unrelated weight-three seeds. Leave E
itself unchanged. The derivative of V becomes mV, where m>0 counts
its non-U letters. Thus V=[U,A0] for some A0 in Lie_3(E).

In the original algebra, delta V=[delta U,A0]+[U,delta A0]. Hence
[delta U,A0] belongs to ad_U(L'). The letter delta U is a fresh free
generator relative to E. Section 1 gives A0=0. Thus V=0, and then
[U,D]=0 forces the length-three component of D to vanish. This finishes
the exclusion of every other component.

Conversely the identity

    delta(2[U_0,[U_0,U_2]]-[U_1,[U_0,U_1]])=[U_0,P_z(U)]

shows that (2) is exceptional. For a fixed nonzero D of this form the
kernel is exactly one-dimensional: the proof in Section 3 of
`class10-nonlinear-proof.md` excludes every direction in E independent
of U by its ordered-seed polynomial. The polarization there also gives
effective recognition. Thus (1) is injective unless D=sigma P_z(U),
sigma nonzero; in that case the previously established kernel line and
quadratic obstruction apply.

## 4. Type (2,6) is injective

Here C belongs to E and U belongs to B. If U=0 then V=0 by the
free-generator centralizer fact. Suppose U is nonzero and make it a
B-basis letter. Separate the free-alphabet weight types in (1).

The B,H component first kills D_H; the E,J component kills V_J.
The B,B,B component says [U,D_(BB)]=0, so D_(BB)=0. The E,E,G
component similarly kills V_(EG). The E,B,W component remains

    [U,D_(EW)]+[C,V_(BW)]=0.

Set the E-basis letter C to zero. Centralizing the free B letter U
forces D_(EW)=[C,S] for some S in W. In [U,[C,S]], the internal-C
words U C S and S C U cannot occur in [C,V_(BW)], whose C is at an
end. Their distinct letter types force S=0, then V_(BW)=0.

The remaining equation is [U,D_(EEE)]+[C,V_(EEB)]=0. Apply Section 1
with fresh letter U, old letter C and old alphabet E. It gives
D_(EEE)=0. We have forced D=0, a contradiction. The kernel is zero.

## 5. Type (3,5) is injective

Here C is in B. Write D=D_G+D_(EB), U=U_W+U_(EE), and decompose V
as in Section 2. If D_G is nonzero, the disjoint W,G and E,E,G
components force both parts of U to vanish, hence V=0. Otherwise
D=D_(EB) is nonzero and V_H=0.

If U_W is nonzero, the E,B,W component, after setting C=0, forces
D=[S,C] with S in E. The internal-C words W C E and E C W then
force S=0, a contradiction. Thus U_W=0, and V_(EW)=V_(BB)=0 by
their separate components and the centralizer of C.

Only [U_(EE),D_(EB)]+[C,V_(EEE)]=0 remains. If U_(EE) is nonzero,
split D along a B-basis containing C. Each other B direction gives
a degree-two free-alphabet tensor commuting with U_(EE). Equal-length
commuting tensors are proportional, and these E,B tensors have a
different letter type from U_(EE), so they are zero. Hence D=[S,C].

In [U,[S,C]], the internal-C terms are -U C S and -S C U. They put
C in different positions (third and second), so cannot cancel each
other, and neither occurs in [C,V]. Thus U tensor S=0. This again
contradicts nonzero U and D. Consequently U=V=0.

## 6. Type (4,4) is injective for independent C,D

The bracket map from

    (W + Lambda^2 E) tensor (G + [E,B])

is injective. Its four summands have distinct alphabet weight types.
For W tensor G this is immediate. For W tensor [E,B] and
Lambda^2 E tensor G, look at coefficients with the distinguished
single letter at an end. For Lambda^2 E tensor [E,B], use the
injection of the exterior square of the degree-two free Lie space
into two-block associative tensors. The two tensor factors are
disjoint subspaces of that degree-two space, so their cross tensor
also injects.

Equation (1) is therefore C tensor V-D tensor U=0. Independence of
C,D gives U=V=0.

## 7. The integral algorithm

For each enumerated leading pair, choose ordered integral Hall lifts
x0,y0 and solve the degree-nine discrepancy by the full integer
linear system (1). Discard insoluble systems. In each injective case
there is a unique integral correction. Fix it and solve the full
degree-ten discrepancy by the final map

    L_(p+2)+L_(q+2) -> L10,
    (S,T) |-> [S,D]+[C,T].

There are no later coordinates, so any integral solution suffices.

In the only exceptional case, Section 3 identifies exactly the family
already covered by `class10-nonlinear-proof.md`. Its first solution
lattice is an affine integer line. The degree-ten discrepancy is a
polynomial of degree at most two in its integral parameter. The earlier
proof supplies a nonzero quadratic coefficient in the rational cokernel
of the last map, leaving at most two integer possibilities. Test every
remaining integral lattice condition and construct factors on success.

The weight checks are uniform over the four types: the first variable
corrections have weights s=p+1 and t=q+1. Since p+q=8,

    s+t=10,       2s+q=10+p>10,       p+2t=10+q>10.

Thus the first correction equation is linear, and through class ten
the only quadratic interaction is between one correction of each
factor. Once they are fixed, the last correction is linear. No
uncontrolled infinite choice is discarded.

Every actual solution has a normalized enumerated leading pair and
appears in the complete correction lattices. Conversely every successful
branch verifies the exact commutator in N. The finite enumeration,
integer linear systems and at most quadratic integer-root step all
terminate. This proves the claimed candidate algorithm, subject to the
explicit earlier structural dependencies.

## 8. Scope and implementation

`scripts/n8_class10_third.py` implements this procedure and returns None
outside gamma_8 in class ten. It delegates gamma_9 to the earlier
penultimate algorithm and the sole nonlinear exception to the existing
family algorithm. The proof is for all finite ranks; the completed group
tests and independent GAP replay are rank two. A larger rank-three
structural probe timed out and is recorded as incomplete. Full details,
including failed fixture-loading attempts, are in `class10-third-audit.md`.

This is an extension of the same one partial N8(b) candidate. It does
not add another resolved problem, establish novelty, or assert a full
class-ten or arbitrary-class algorithm.
