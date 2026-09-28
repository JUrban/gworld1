# Six kernels and an obstruction for a proposed class-ten algorithm

28 September 2026. This is a mathematical development of
`N8-class10-completion-lead.md`, not yet an extension of the claim ledger.
The group algorithm and its audit still need completion. The proposed
lemmas below are all-rank statements; finite rank checks only support them.

Use the rational, graded, delta-stable free alphabet of Section 1 of
`problems/N8/class9-proof.md`, with delta=ad_z for nonzero z in L1.
The alphabet-weight spaces are E,B,W,G,H,J in weights 2 through 7.
Each delta map on an alphabet-weight space is injective into the next.
In particular

    L4 = W + Lie_2(E),       L5 = G + [E,B],
    L6 = H + [E,W] + Lie_2(B) + Lie_3(E),
    L7 = J + [E,G] + [B,W] + Lie_(2E,B),
    L8 = K + [E,H] + [B,G] + Lie_2(W)
           + Lie_(2E,W) + Lie_(E,2B) + Lie_4(E).

All sums are direct; K is the weight-eight alphabet space. Bracket
length and the multiset of alphabet weights can be projected separately.
We use the previously proved generator centralizer, the mixed three-letter
injection (4) of class8-proof.md, and Kernel A of class5-proof.md.
All calculations below take place in the free associative algebra containing
this free Lie algebra, so projections onto specified word patterns are valid.

## Elementary projections

If a Lie polynomial contains exactly one letter e outside an alphabet B,
it is uniquely determined by its associative words beginning with e.
Indeed the iterated adjoints of B letters applied to e are a basis, and
their e-initial words have distinct reversely ordered B suffixes, up to sign.
We need this only with at most two B letters, where it follows directly
by expansion and Jacobi.

A derivation replacing one alphabet letter a by a new letter a' is injective
on the span of Lie monomials with a fixed positive number m of occurrences
of a: replacing a' back by a composes to multiplication by m. Separating
multidegrees proves that zero derivative means the polynomial contains no a.

For vector spaces B and delta B, the projection of delta Lie_2(B) to
B tensor delta B is the antisymmetric tensors, after identifying delta B
with B. A nonzero rank-one tensor cannot be antisymmetric over Q.

Write A_(p,q,j)(U,V)=[U,D]+[C,V] for fixed nonzero C in Lp, D in Lq.

## 1. Type (1,3), offset three, is injective

Here C=z, D lies in B, U lies in W+Lie_2(E), and V lies in L6.
Bracket length one kills V_H. The E,G component kills V_EW because
delta on W is injective. Now the B,W component is [U_W,D]+delta V_BB.
Projecting outside delta B first puts U_W in delta B; the antisymmetric
tensor observation then forces U_W=V_BB=0.

What remains is [U_EE,D]+delta V_EEE=0. If D has a component outside
delta E, projecting onto that direction forces U_EE=0, then V=0.
Otherwise D=delta T for nonzero T in E. Choose T as an E basis letter.
Project onto each derivative letter delta e with e different from T.
The fresh-letter derivation observation forces V_EEE to involve no such e.
It would then be a Lie polynomial of degree three on the single letter T,
so is zero. Thus [U_EE,D]=0 and the generator centralizer gives U_EE=0.

## 2. Type (2,2), offset three, is injective for independent C,D

Here C,D are independent in E. For U,V in L5, the E,G component kills
their G components. For each B letter b write the remaining components
U_b=[X,b], V_b=[Y,b], where X,Y belong to E. Associative words beginning
with b in the kernel equation give

    -X tensor D + Y tensor C = 0.

Independence of C,D implies X=Y=0. This proves the assertion.

## 3. Type (1,5), offset two

Here C=z, U is in B and D is in G+[E,B]. In V in L7, its J component
vanishes. The E,H component kills V_EG. The W,W component of delta V_BW
puts V_BW in B tensor delta B with a symmetric coefficient matrix: components
outside delta B vanish, and the antisymmetrization of the rest must vanish.

The B,G component is [U,D_G]+delta_W V_BW=0. If U is nonzero, this
puts D_G in delta^2 B, and the symmetric matrix is a rank-one tensor.
Consequently D_G=lambda delta^2 U and V_BW=-lambda[U,delta U].
Subtract this solution of the bracket-length-two equation.

The E,E,W component of the remaining equation comes only from applying
delta to the B letter of V_EEB; this replacement is injective. Hence
V_EEB=0. Now [U,D_EB]=0, so D_EB=0 by the generator centralizer.
If U=0, delta V=0 gives V=0 directly.

Thus the kernel is zero unless D=delta^2 T for a nonzero T in B=L3.
In that exceptional case T is unique and the kernel is exactly

    Q*(T,-[T,delta T]).

The converse is the derivation identity delta[T,delta T]=[T,delta^2 T].

## 4. Type (2,4), offset two

Here C is a nonzero E letter after a basis change, D=D_W+D_EE,
U=U_W+U_EE and V lies in L6. The E,H and E,B,B components kill V_H
and V_BB. If D_W is nonzero, the W,W component makes U_W a multiple
of D_W. Subtract that multiple of the kernel vector (D,0), so U_W=0.
For each W direction the E,E,W component is the mixed three-letter
injection from class8-proof.md, and forces U_EE=V_EW=0. The remaining
equation [C,V_EEE]=0 gives V_EEE=0.

If D_W=0, the same mixed injection, separately in each W direction,
forces U_W=V_EW=0. The residual equation lies in the free Lie algebra
on E: C has alphabet degree one, U and D degree two, V degree three.
Kernel A of class5-proof.md applies and gives U=lambda D, V=0.

In both cases the kernel is precisely Q*(D,0). The exact group move
x->yx translates the corresponding integral affine line by the nonzero
period given by the content of D. Enumerate residues in the full integral
kernel, as in the earlier proof; later corrections absorb higher terms.

## 5. Type (3,3), offset two, is injective for independent C,D

Now C,D are independent B letters after changing basis in B. The B,G
component kills the G components of U,V in L5. For each E letter e
write U_e=[e,X], V_e=[e,Y] with X,Y in B. The e-initial associative
words give X tensor D-Y tensor C=0, forcing X=Y=0.

## 6. Type (1,5), offset three, is injective when D is in G

This includes every exception in Section 3. U lies in W+Lie_2(E),
V lies in L8 and D is a nonzero alphabet vector in G.
The length-one, E,J and B,H components kill V_K,V_EH,V_BG respectively.
The W,G component is [U_W,D]+delta V_WW. If D is outside delta W,
projection kills U_W. If D=delta R, the antisymmetric tensor observation
also kills U_W and V_WW.

At bracket length three the equation is

    [U_EE,D]+delta(V_EEW+V_EBB)=0.

The E,E,G component forces U_EE=0 if D is outside delta W, finishing
that case. Otherwise D=delta R and V_EEW=-[U_EE,R]. After substitution,

    delta V_EBB = [delta U_EE,R].

The right side has no associative words of pattern E,W,B: its E-initial
words have pattern E,B,W. On the left, E,W,B is obtained by replacing the
first B in the E,B,B coefficients of V_EBB. This is injective on those
coefficients; the one-E observation above gives V_EBB=0. Thus
[delta U_EE,R]=0. The two-letter polynomial delta U_EE uses E,B,
whereas R is a nonzero W letter, so the generator centralizer gives
delta U_EE=0, hence U_EE=0. Finally delta V_EEEE=0 kills V_EEEE.

## 7. The exceptional quadratic obstruction

Suppose D=delta^2 T with nonzero T in B. Then

    Q=[T,[T,delta T]] in L10

is outside [L5,D]+delta L9. If T has a nonzero component in a degree-three
seed (rather than delta E), project to that seed's delta-chain, killing all
other seeds. Choose that component as one seed by a rational basis change.
The three-letter weight-nine Lie space on this chain is zero: it would
use three copies of its weight-three first letter. Therefore its delta
image is zero. The projected [L5,D] term has bracket length two. Q, a
nonzero three-letter word, survives.

Otherwise T=delta S for nonzero S in E. Choose S as a degree-two seed
and project to its chain S_i=delta^i S. The weight-ten three-letter space
has basis

    X=[S0,[S0,S4]], Y=[S1,[S0,S3]], Z=[S0,[S1,S3]],
    W=[S2,[S0,S2]], R=[S1,[S1,S2]].

Independence follows from shift multisets, with two dimensions for {0,1,3}
and one each for {0,0,4},{0,2,2},{1,1,2}. The three delta images from
weight nine are X+Y+Z, W+R+Y, R+Z. The only possible [L5,D] term in
this component is [[S0,S1],S3]=Z-Y. The functional taking these five
basis vectors to (2,-1,-1,0,1) annihilates all four images and takes Q=R
to 1. This proves the obstruction for every nonzero T.

## 8. Finite integral completion of the exceptional branch

Fix the leading pair and its unique offset-one correction. The offset-two
integral solution set, when nonempty, is v+kK with K a primitive integral
kernel vector and k in Z. K=rho*(T,-[T,delta T]) for nonzero rational rho.
The resulting factors x(k),y(k) match the target through weight eight.

The degree-nine residual is affine in k, since the two variable corrections
have weights three and seven and their first interaction has weight ten.
The offset-three map of Section 6 is injective. Solve its equations jointly
with k by integer linear algebra. The complete solution set is empty, a
single point, or an affine integral line. In the line case write k=k0+mt
and the offset-three correction as w0+tW, with m a nonzero integer. A
zero m would contradict injectivity of the offset-three map.

Apply those integer corrections. The degree-ten residual is an integer-valued
polynomial of degree at most two in t. The offset-three corrections are
affine, and cannot interact with the offset-two variable corrections before
weight eleven (3+8 and 4+7). Their contribution through weight ten is linear.
Two weight-three corrections with the weight-five leading factor first
interact in weight eleven. Thus the quadratic coefficient, up to sign, is
rho^2 m^2 Q. By Section 7 it is nonzero modulo the final offset-four image
[L5,D]+[z,L9]. A rational cokernel functional therefore yields a nonzero
quadratic equation, with at most two integer roots. Check each root against
all integral last-layer equations. The singleton case is simply one linear
last-layer problem. This is a finite, constructive procedure.

## 9. Proposed completion table through class ten

Use the finite leading-pair list and all earlier integral normalizations.
Relative offsets refer to leading weights p,q.

| Leading degree | Operations before a joint linear tail |
| --- | --- |
| 1 | Reject. |
| 2 | Existing arbitrary-class algorithm. |
| 3: (1,2) | Class-nine normalizations; tail offset four. |
| 4: (1,3),(2,2) | Class-nine normalizations through offset two; Section 1/2 unique offset three; tail offset four. |
| 5: (1,4),(2,3) | Existing class-nine finite choices and unique second correction; tail offset three. |
| 6: (1,5) | Unique first step; Section 3 second step; if unique, tail offset three; if exceptional, Section 8. |
| 6: (2,4) | Unique first step; Section 4 finite second-step residues; tail offset three. |
| 6: (3,3) | Unique first step; Section 5 unique second step; tail offset three. |
| 7: (1,6) | Previous quadratic gives finitely many first-step parameters; solve the entire remaining tail starting at offset two. |
| 7: (2,5),(3,4) | Previous unique first step or finite Nielsen residues; tail offset two. |
| 8--10 | Committed gamma_8/class-ten procedure. |

Every listed tail has starting weights s,t with s+t>10, 2s+q>10 and
p+2t>10; its increments commute through class ten. Use the full joint
integral system. In particular, for (1,6) do not fix an arbitrary degree-nine
particular solution before matching degree ten. All branching is finite.

Implementation detail exposed by the first group run: for b=[x,y],
the increment on changing y to yh is [x,h]^b[b,h]. With leading weights
(1,2) and h of weight six, conjugating [x,h] by b contributes in degree
ten. The class-nine optimized routine omitted that contribution under an
assertion valid through class nine. The class-ten routine must retain it;
it remains linear in the correction coordinates. The original failed
run is preserved, and the old verified class-nine routine is unchanged.

The proof structure now supplies a proposed all-rank, all-target class-ten
algorithm. Its implementation and full artifact audit remain outstanding;
no broader candidate scope or established novelty is asserted at this point.


Update approximately23:33 UTC: the completed candidate and bounded audit
are in problems/N8/class10-proof.md and class10-audit.md. This file preserves
the pre-audit development and is not the current status record.
