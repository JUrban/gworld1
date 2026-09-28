# Single commutators in class nine, all finite ranks

Proposed extension, first written 28 September 2026, approximately
19:14 UTC. The bounded computational audit and independent GAP replay
were completed approximately20:36 UTC; see `class9-audit.md`. This extends
the same partial N8(b) candidate. Independent specialist review and novelty assessment remain
outstanding. The original problem and all earlier qualifications are
unchanged: arbitrary nilpotency class is not settled here.

**Proposed theorem.** For every finite rank r, single-commutator
membership in F_r/gamma_10(F_r) is decidable, with factors constructed
on positive inputs. Ranks zero and one are immediate. We work with
r>=2, the convention [x,y]=x^-1 y^-1 x y, and integral Hall group
coordinates. Rational Lie arguments classify kernels; all subsequent
equations and solution lattices in the algorithm remain integral.

We use the finite leading-pair enumeration, including integral scales
and oriented sublattices, from `penultimate-target-proof.md`, the
arbitrary-class degree-two procedure, and the class-seven/eight kernel
lemmas. The new ingredients are given below.

## 1. A homogeneous free basis on which delta shifts generators

Let L be the free Lie algebra over Q on r degree-one generators,
L'=[L,L], L''=[L',L'], and M=L'/L''. Fix nonzero z in L1 and set
delta(v)=[z,v]. The derived ideal M of the free metabelian Lie algebra
is a torsion-free module over Q[X1,...,Xr]. In particular delta is
injective on M. This standard result is Theorem 4.3 of
Poroshenko--Timoshenko, *Universal equivalence of partially commutative
metabelian Lie algebras*, arXiv:1107.0430, printed p.8. The exact PDF
and its proof have been archived and the page visually inspected.
The sign difference between right and left adjoint actions is harmless.

For each d>=2 choose a basis S_d of a complement to delta M_(d-1)
in M_d. By induction on d, using injectivity of delta, the vectors

    delta^j s,  s in S_d, j>=0,

form a homogeneous Q-basis of M. Lift each seed s homogeneously to
L', and lift its shifts by taking the actual iterates delta^j(s).
These lifts generate L': their images span M, and any remaining
homogeneous element belongs to L'', hence is a sum of brackets of
strictly lower-weight elements, handled by induction. Their independent
images in M make this generating set irredundant. The homogeneous
Shirshov lemma therefore makes it a free generating set. The precise
ordinary-Lie version and primary source were recorded in Section 1 of
`class7-proof.md` (Bryant--Kovacs--Stohr, 2005, introduction).

Thus delta acts on a homogeneous free alphabet by shifting each
generator one step along its seed's chain. It preserves bracket
length in this alphabet and the number of occurrences of each seed.
This construction uses the grading explicitly; it does not assert
that every infinitely generated torsion-free module over a PID is free.

Write E,B,W,G,H,J for the spans of the free generators of weights
2,3,4,5,6,7 respectively. Then E=L2, B=L3 and

    L4 = W + Lambda^2 E,
    L5 = G + [E,B],
    L6 = H + [E,W] + Lambda^2 B + Lie_3(E),
    L7 = J + [E,G] + [B,W] + Lie_(2E,1B).

Every displayed sum is direct. Here delta E is contained in B,
delta B in W, delta W in G, delta G in H, delta H in J, and all
these restrictions are injective. Unlike arbitrary complements, these
inclusions hold exactly, without decomposable correction terms.

We use the elementary free-generator centralizer fact proved in the
class-five note: a free generator commutes with no nonzero Lie
polynomial of bracket length greater than one. Any nonzero vector in
one alphabet-weight space can be made a free generator by a rational
change of basis in that space. For equal original homogeneous degrees,
commuting tensors U,D are proportional: UD=DU says U tensor D equals
D tensor U after splitting each associative word into two equal blocks.

## 2. Five correction kernels

For leading terms C in Lp and D in Lq, the correction at offset j is

    A_(p,q,j): L_(p+j) + L_(q+j) -> L_(p+q+j),
    (U,V) |-> [U,D]+[C,V].                              (1)

All leading terms in this section are nonzero. Direct decompositions
refer to the free alphabet just constructed when p=1; for the other
cases any homogeneous free generating set of L' suffices.

### 2.1 Type (1,2), offset three

For C=z and D=T in E the kernel of L4+L5 -> L6 is exactly

    Q*(delta^2 T, [T,delta T]).                         (2)

The length-one component forces V_G=0. The E tensor W component
then gives U_W=delta B0 and V=[T,B0] for some B0 in B. The
Lambda^2 B component is [delta T,B0]=0, so B0=lambda delta T.
Finally the Lie_3(E) component says [U_(EE),T]=0 and forces
U_(EE)=0 by the generator-centralizer fact. Conversely (2) lies in
the kernel by the derivation rule.

This line comes from an exact group operation. For any pair x,y
put c=[x,y] and simultaneously conjugate both factors by c:

    (x,y) |-> (c^-1 x c, c^-1 y c).                    (3)

Their commutator remains c exactly. If the leading weights are 1,2,
the first changes in the factors have weights 4,5 and terms
[z,[z,T]]=delta^2 T and [T,[z,T]]=[T,delta T]. Thus (3) preserves
all lower choices and translates the parameter on (2) by a nonzero
integer period relative to the primitive generator of the full
integral kernel. Enumerating residues modulo that period is complete.
The conjugator is the current pair's commutator, not a target word
that is only approximately matched.

### 2.2 Type (2,3), offset two

For C in E, D in B, the map L4+L5 -> L7 is injective.
The B tensor W and E tensor G components first force U_W=V_G=0.
Now U is in Lambda^2 E and V is in [E,B]. Separate the B directions
using a basis containing D. For directions other than D, the
generator-centralizer fact kills the corresponding part of V.
The remaining equation is

    [U,D]+[C,[S,D]]=0.

The elementary injection (4) in Section 2 of `class8-proof.md`, with
the sign of its first argument adjusted, gives U=S=0.

### 2.3 Type (1,6), offset one

For C=z and D in L6 the map E+L7 -> L8 has zero kernel unless

    D=delta^4 T for some nonzero T in E.                (4)

In that exceptional case its kernel is the line

    Q*(T,-V0),
    V0=[T,delta^3 T]-[delta T,delta^2 T].              (5)

The element T in (4) is unique; it need not be integral. Notice
delta V0=[T,delta^4 T], so (5) is indeed a kernel vector.

For completeness, suppose [U,D]+delta V=0. If U=0, injectivity of
ad_z on L7 gives V=0. Otherwise the length-one component kills V_J.
Use the decompositions in Section 1. The E tensor H component gives

    D_H=delta G0,       V_(EG)=-[U,G0].

The B tensor G component then gives

    G0=delta W0,        V_(BW)=[delta U,W0].

The Lambda^2 W component is [delta^2 U,W0]=0. Hence
W0=lambda delta^2 U, D_H=lambda delta^4 U, and the two displayed
parts of V equal -lambda([U,delta^3 U]-[delta U,delta^2 U]).
Subtract this explicitly verified kernel contribution. It remains
to consider D in [E,W]+Lambda^2 B+Lie_3(E) and V in Lie_(2E,1B).

The bracket-length-four component forces D_(EEE)=0. In the E,E,W
component, directions of W outside delta B cannot be cancelled by
delta V; the centralizer fact forces them to vanish. Therefore
D_(EW)=delta_B R for a unique R in [E,B], where delta_B replaces
the B letter by its delta image and leaves E fixed. This replacement
is injective on the one-B-letter component. The same equation gives
V=-[U,R]. The remaining equation is

    [delta U,R]+[U,delta_E R-D_(BB)]=0,                (6)

where delta_E acts on E and leaves B fixed.

Choose U as an E basis vector and set that generator to zero in
the free algebra on E+B. Equation (6) becomes [delta U,Rbar]=0;
the B generator delta U is still nonzero in this quotient. Its
centralizer forces Rbar=0, so R=[U,S] with S in B. Project (6) in
the associative algebra to words of form B,U,B. Only the first
bracket contributes, giving

    delta U tensor S + S tensor delta U = 0.

Over Q this forces S=0. Thus R=V=0, and (6) then gives D_(BB)=0.
No residual component remains. Consequently D=lambda delta^4 U,
which proves (4)--(5) and the one-dimensional assertion.

### 2.4 Type (2,5), offset one

For C in E and D in L5, the map B+L6 -> L8 is injective.
Write D=D_G+D_(EB). The E tensor H component kills V_H. If
D_G is nonzero, the B tensor G component forces U=0, then V=0.
Otherwise D=D_(EB). The E,E,W and E,E,E,E components kill V_(EW)
and V_(EEE) respectively, using the generator-centralizer fact.
Thus V belongs to Lambda^2 B.

If U is nonzero, setting the E generator C to zero in
[U,D]+[C,V]=0 gives Dbar=0, so D=[C,S] for S in B. Projection
to associative words B,C,B gives U tensor S+S tensor U=0.
This forces S=0, contradicting D nonzero. Therefore U=V=0.

### 2.5 Type (3,4), offset one

For C in B and D in L4, the kernel of L4+L5 -> L8 is exactly
Q*(D,0). The B tensor G component forces V_G=0. The E,B,B
component is then [C,V_(EB)]=0 and forces V_(EB)=0. The remaining
equation [U,D]=0, with U,D of equal homogeneous degree four,
implies U is proportional to D by the tensor observation above.
The exact Nielsen operation (x,y)->(yx,y) supplies the nonzero
integer period content(D); later corrections absorb its higher terms.

## 3. The new exceptional quadratic obstruction

Under (4), put

    Q0=[T,[T,delta^3 T]-[delta T,delta^2 T]] in L9.

Then Q0 does not belong to the rational image of

    A9: L3+L8 -> L9, (U,V) |-> [U,D]+delta V.          (7)

To prove this, choose T as one of the degree-two seed generators
in Section 1. Project to bracket length three and to Lie words
using only the seed T and its shifts. The term [U,D] has bracket
length two, so projects to zero. Since delta preserves both counts,
only the following two-dimensional part of V can contribute:

    V1=[T,[T,delta^2 T]],    V2=[delta T,[T,delta T]].

An independent basis in the degree-nine target is

    X=[T,[T,delta^3 T]],
    Y=[delta T,[T,delta^2 T]],
    Z=[T,[delta T,delta^2 T]].

Here X has shift multiset {0,0,3}; Y,Z are the two-dimensional
multilinear component with shifts {0,1,2}. The derivation rule and
Jacobi identity give

    delta V1 = X+Y+Z,       delta V2 = 2Y-Z,
    Q0 = X-Z.

The functional taking (X,Y,Z) to (-3,1,2) kills both delta images
and takes Q0 to -5. Hence Q0 is outside (7), as claimed.

Suppose the first integral correction system has solutions v+kK,
k in Z, with K a primitive generator of its full integral kernel.
For a nonzero rational rho, K=rho*(T,-V0). Apply ordered integral
Hall lifts of the corrections of weights two and seven to obtain
x(k),y(k). Their commutators agree with the target through weight
eight. The degree-nine residual

    R9(k) = degree_9([x(k),y(k)]^-1 g)

is an integer-valued polynomial of degree at most two. Indeed two
weight-two corrections interacting with the weight-six base first
occur in weight ten, while two weight-seven corrections with the
degree-one base start in weight fifteen. The only quadratic term
through weight nine is the interaction of one correction of each
kind. Nonlinear terms in the ordered weight-two lifts start in
weight four, again too late to interact with the base before ten.
The quadratic coefficient is, up to the discrepancy convention,
rho^2 Q0, nonzero in the rational cokernel of (7).

Consequently a rational cokernel functional gives a nonzero
quadratic equation in k. There are at most two integer possibilities.
Integer Hermite/Smith reduction gives this equation and all remaining
linear congruence conditions exactly; enumerate the integer roots,
then test all conditions. For each surviving k, solve the entire
last-layer integral affine system (7). Its kernel need not be zero:
there are no later layers, so any integral solution suffices.

## 4. Completion through all leading weights

A joint correction tail with starting weights s,t for the two
factors is linear through class nine whenever

    2s+q>9,     p+2t>9,     s+t>9.

All tails listed below satisfy these inequalities, and their
commutator increments have weight at least seven, so they commute.
Use the exact joint integer system, retaining its entire kernel.
No arbitrary intermediate choice from an infinite kernel is allowed.

| Leading weight/type | Corrections preceding the linear tail |
| --- | --- |
| 1 | Reject by abelianization. |
| 2 | Existing arbitrary-class IA algorithm. |
| 3: (1,2) | Earlier first Nielsen period and injective second step; Section 2.1 supplies a third finite period; tail starting in weights (5,6). |
| 4: (1,3) | Earlier unique first step and second Nielsen period; tail (4,6). |
| 4: (2,2) | Earlier unique first and second steps; tail (5,5). |
| 5: (2,3) | Earlier first Nielsen period; Section 2.2 gives unique second step; tail (5,6). |
| 5: (1,4) | The class-eight quadratic obstruction leaves at most two first-step parameters when exceptional. In every case solve the injective second step, then tail (4,7). |
| 6: (1,5),(2,4),(3,3) | Existing injective first steps; tails (3,7),(4,6),(5,5). |
| 7: (1,6) | Section 2.3 gives a unique first step or the exceptional line; Section 3 reduces that line to at most two parameters; final linear layer. |
| 7: (2,5) | Section 2.4 gives unique first step; final linear layer. |
| 7: (3,4) | Section 2.5 gives a finite Nielsen period; final linear layer. |
| 8,9 | Existing penultimate/central algorithms. |

In the nonexceptional (1,4) case one must still fix the unique second
correction before taking the tail. The earlier class-eight tail
starting at (3,6) is not linear through class nine, since 3+6=9.
The table deliberately handles this extra step.

For every rationally injective step, retain it only if the unique
solution is integral. For every period, compute its size using the
actual primitive integral kernel vector, not a rational scaling.
Exact Nielsen operations and (3) preserve the target and the already
fixed lower coordinates, so the residue enumerations lose no solution.

The identity is a positive instance. The leading-pair enumeration is
finite and complete, and every subsequent branch is a finite list,
an integral linear system, or a quadratic integer-root computation.
Every accepted branch constructs exact factors; rejecting all branches
therefore decides a negative instance. Subject to the earlier cited
dependencies, this proves the proposed class-nine theorem.

## 5. Scope and evidence boundary

This is a partial N8(b) result, not an answer in arbitrary class.
The all-rank claims rest on the proofs, not bounded matrix ranks.
Computational support, failures, independent replays and literature
checks are recorded in `class9-audit.md`. The proof supplies the all-rank
argument; the bounded checks are supporting evidence.
The two credited structural ingredients are ordinary homogeneous
Shirshov freeness and the torsion-free free-metabelian derived module.
No mathematical result or code from the Kourovka run is newly imported.
