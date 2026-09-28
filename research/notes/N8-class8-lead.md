# N8 class eight: proposed all-rank extension

28 September 2026, first argument approximately 16:14–16:18 UTC.
**Proof lead only, not yet added to the candidate scope.**

Class eight adds six small homogeneous correction-kernel questions.
The class-seven exceptional (1,4) branch should remain univariate:
its next correction is injective, so a quadratic congruence parameter
is followed by a cubic lattice test. Exact integral lifting, a prototype
and independent checks are still required before promoting this lead.

The intended proof uses the already credited homogeneous Shirshov lemma
and the existing finite homogeneous-factor enumeration. No Kourovka
argument or code is imported.

## Graded notation

Work over Q in the free Lie algebra L. Let E=L2, B=L3 and choose
homogeneous free generators for L' so that W complements [E,E] in L4
and G complements [E,B] in L5. Thus

    L''5 = E tensor B,
    L''6 = (E tensor W) + Lambda^2 B + Lie_3(E),
    L''7 = (E tensor G) + (B tensor W) + L_(2E,1B).

All displayed sums are direct. The last term consists of free Lie words
with two E generators and one B generator. These are decompositions by
the types of free generators, not by arbitrary associative tensors.

For z in L1 nonzero, delta=ad_z induces injections

    f:E->B, g:B->W, h:W->G,

where g,h include projection onto the indicated complements. The
metabelian module map mu proves these: multiplication by the nonzero
linear polynomial ell_z is injective, and mu is injective on E,B,W.
The earlier degree-four/five kernels establish the last assertion.

We also need ker(mu|L6)=L''6. The syzygy calculation used earlier gives
dim mu(L6)=r*binomial(r+4,5)-binomial(r+5,6). With e=dim E, b=dim B,
w=dim W=dim L4-binomial(e,2), Witt's formula gives

    dim L6-dim mu(L6) = e*w+binomial(b,2)+(e^3-e)/3.

This is exactly the dimension of the included L''6 above; hence equality.
This identity and the following kernels are to be checked exactly.

## A small free-Lie injection

Let c be a nonzero generator direction in E and b a nonzero independent
generator direction in B. The map

    (T,S) -> [b,T]+[c,[S,b]],  T in Lambda^2 E, S in E

is injective. Expand in the free associative algebra on E and b and
project onto words starting with b. The equation becomes T+S*c=0
inside E tensor E. A pure tensor S*c cannot be alternating in
characteristic zero unless S=0. Then T=0. Components in other B
directions separate, so the same argument applies to one chosen
nonzero B direction inside a larger B.

## Proposed correction kernels

1. For nonzero D in B, the map (U,V) in B+L5 -> L6 given by
   [U,D]+delta V has kernel Q*(D,0). Applying mu gives V in E tensor B.
   Projection of delta V to E tensor W is (id tensor g)V, so V=0.
   The exterior-square injection on B then gives U proportional to D.
   This is the second correction for type (1,3).

2. For independent C,D in E, the map L4+L4 -> L6 given by
   [U,D]+[C,V] is injective. Projection to E tensor W first puts U,V
   in Lambda^2 E. Set C=c,D=d in a free basis of E. Setting c=0
   gives [Ubar,d]=0, so Ubar=0 and U=[c,S]. In the associative
   expansion of [[c,S],d]+[c,V], project to words neither starting
   nor ending in c. The remaining expression is -S*c*d-d*c*S,
   after discarding the c-component of S. Coefficients of s*c*d
   for basis directions s distinct from c,d, and of d*c*d, force
   every remaining component of S to vanish. Then [c,V]=0 implies
   V=0. This is the second correction for type (2,2).

3. For nonzero D in L4, the map B+L6 -> L7 given by
   [U,D]+delta V is injective. Applying mu puts V in L''6. Projection
   to E tensor G first kills its E tensor W component, using h.
   The B tensor W equation is

       U tensor Dbar + (id tensor g)A = 0, A in Lambda^2 B.

   If Dbar!=0 and U!=0, this forces Dbar=g(T) and A=-U tensor T,
   contradicting alternation of a nonzero pure tensor. Thus that case
   is impossible. If U=0, delta V=0 implies V=0 directly.
   It remains to consider D in Lambda^2 E, A=0, V in Lie_3(E).
   B components outside f(E) force U to lie in f(E). Write U=f(T)
   and take T as the first basis vector of E. In delta V, replacing
   any other E basis vector e_i by its distinct copy f(e_i) gives
   zero, since the right side [U,D] only uses f(T). Replacing that
   copy back by e_i shows that each multihomogeneous component of V
   containing e_i has zero coefficient. Hence V lies in Lie_3(QT)=0.
   Then [U,D]=0 forces U=0. This is the second correction for (1,4).

4. For nonzero D in L5, the map E+L6 -> L7 given by
   [U,D]+delta V is injective. Again V lies in L''6. If U!=0,
   projection to E tensor G makes D_G=h(T), V_EW=-U tensor T.
   The B tensor W equation then gives

       -f(U) tensor T + (id tensor g)A = 0.

   Alternation forces T=A=0 by the same pure-tensor argument.
   Thus D belongs to E tensor B and V to Lie_3(E). Components
   outside f(E) eliminate the corresponding part of D. Let epsilon
   be the derivation sending f(e_i) to e_i and killing E. Applying
   epsilon to delta V=-[U,D] gives 3V=-[U,epsilon D]. Hence V=[U,T]
   for some T in Lambda^2 E. Substitution gives

       [f(U),T]+[U,delta T+D]=0.

   Separating B components and applying the small injection above
   forces T=0 and D=0, a contradiction. This is the first correction
   for (1,5).

5. For nonzero C in E and D in L4, the map B+L5 -> L7,
   (U,V)->[U,D]+[C,V], is injective. Its E tensor G component puts
   V in E tensor B. If Dbar in W is nonzero, its B tensor W component
   forces U=0, and then V=0. Otherwise D belongs to Lambda^2 E.
   If U!=0, separate its B direction and apply the small injection
   with c=C,b=U,T=D to obtain a contradiction. This is the first
   correction for (2,4).

6. For independent C,D in B, the map L4+L4 -> L7,
   (U,V)->[U,D]+[C,V], is injective. The B tensor W component puts
   U,V in Lambda^2 E. The map (Lambda^2 E) tensor B -> L_(2E,1B)
   given by bracketing is injective by its associative words ending
   in B. Independence of C,D now forces U=V=0. This is the first
   correction for (3,3).

All zero-centralizer assertions here concern a free generator direction
or unequal homogeneous degrees, as established in the earlier proofs.
No numerical kernel rank is being promoted to the all-rank argument.

## Intended class-eight lifting

- Leading degree 2: existing arbitrary-class procedure.
- Leading degree 3, type (1,2): existing first two normalizations, then
  joint linear tails starting in weights (4,5); their cross weight is 9.
- Leading degree 4, type (1,3): unique first correction, then the
  Nielsen line in item1. Normalize its full integral affine kernel by
  the exact move x->yx and finitely many residues; linear tails (4,6).
- Leading degree 4, type (2,2): unique first and second corrections,
  using item2; linear tails (5,5).
- Leading degree 5, type (2,3): existing first Nielsen normalization;
  tails (4,5) remain linear through class eight.
- Leading degree 6: items4–6 give a unique integral first correction,
  followed by a final linear layer.
- Leading degrees 7 and 8: existing penultimate/central procedures.

For the exceptional type (1,4), the first correction through degree6
is either unique or an integral affine line v0+kK by the class-seven
kernel classification. The degree7 discrepancy is quadratic in k.
Item3 makes its next correction, in L3+L6, unique when soluble.
The integral-solubility conditions are univariate polynomial equalities
and congruences. If a nonzero equality occurs there are finitely many
integer roots to try. Otherwise they are periodic, and we retain a
finite union of progressions k=a+M*t.

On each progression the unique correction has rational polynomial
coordinates of degree at most two, integral at every integer t. Its
ordered Hall lift is used in the actual group. The degree8 discrepancy
then has degree at most three: the new products are weight3 by weight5
and weight2 by weight6, so their parameter degrees are at most 2+1.
Repeated weight2 terms with the opposite weight4 base give degree two;
all higher interactions exceed weight eight. The final correction
lattice [L4,D]+[z,L7] is independent of t.

Univariate integer-valued polynomial membership in a fixed integer
lattice is decidable: rational normal forms give finitely many
polynomial equalities and congruences. A nonzero equality has finitely
many computable integer roots. If all equalities vanish, degree d
Newton polynomials modulo e are periodic with period d!*e. Thus the
remaining search is finite. This is a termination argument, not a
polynomial-time assertion. The proposed prototype must preserve full
integral lattices and every allowable progression.

## Stronger obstruction found at approximately 16:23 UTC

The cubic/progression branch above is unnecessary. For the exceptional
first kernel, D=delta^2 T and its direction is a nonzero scalar times
(T,-[T,delta T]). The quadratic coefficient of the degree7 discrepancy
is a nonzero scalar times

    Q=[T,[T,delta T]].

It lies outside the rational image of the degree7 correction map
(U,V)->[U,D]+delta V with U in B, V in L6. To prove this, Q has only
the (2E,1B) component and mu(Q)=0. In a proposed preimage, the E tensor G
projection forces V_EW=0. The B tensor W projection gives
U tensor Dbar+(id tensor g)A=0. Here Dbar=g(f(T)) is nonzero,
so the pure-tensor/alternation argument forces U=A=0. We would then
have delta V=Q with V in Lie_3(E). Choose T as a basis direction in E.
All other f(e_i) components vanish, and the letter-count argument
forces V in Lie_3(QT)=0. But Q is nonzero in the free Lie algebra on
the distinct free generators T and f(T), a contradiction.

Therefore a nonzero quadratic equality always survives in the rational
cokernel. There are at most two possible integer values of the first
parameter. Each is checked for integrality of the unique degree7 lift,
then for solvability of the final degree8 integer linear system.
No infinite progression needs to be retained. The earlier cubic route
is preserved above as derivation history; the prototype has been
simplified to this finite-root procedure before its first group test.

## Later scope and next obstruction

The full candidate argument is now written in
`problems/N8/class8-proof.md`; the computational audit is maintained
separately in `class8-audit.md`. Do not infer completion of the
rank-three group suite from this chronological lead.

For a future higher-class investigation, there is already a concrete
obstruction to extrapolating the injective (1,5) first correction.
For every m>=1 and nonzero T in E, put

    D=delta^(2m) T,
    V=sum_(i=0)^(m-1) (-1)^i [delta^i T,delta^(2m-1-i) T].

Applying delta telescopes to delta V=[T,D]; the remaining middle
bracket is zero. Thus (T,-V) is a nonzero first-correction kernel
for leading type (1,2m+2). The m=2 case already occurs for type
(1,6), with V=[T,delta^3 T]-[delta T,delta^2 T]. This is only an
elementary kernel family, not a classification or a further decision
algorithm, and adds no candidate scope or count. No numerical probe
or novelty claim is based on this observation.
