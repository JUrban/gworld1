# Every third-from-last target, arbitrary class and finite rank

Candidate extension derived29 September2026, approximately05:33--05:37UTC.
Implementation and independent checks are complete in
`third-layer-audit.md`; the scope below is promoted within the same partial candidate. This is still partial N8(b), not an all-layer solution.

**Proposed theorem.** In N=F_r/gamma_(c+1), c>=6, one can decide whether
any target with nonzero leading term in degree c-2 is a single commutator,
and construct its factors when it is. All finite ranks are included;
ranks0--1 have no such nonidentity target. Combined with the previous
central and penultimate algorithms, this covers every target in gamma_(c-2).
The older low-class algorithms cover the smaller-class boundary cases.

Use [x,y]=x^-1 y^-1 x y. The existing complete leading-pair enumeration,
including signed integral scales and equal-weight oriented Hermite
sublattices, gives finitely many normalized pairs C in Lp,D in Lq,
p<=q, p+q=c-2, [C,D]=W. All Lie kernel arguments below are rational;
all actual group systems and final lattices remain integral.

## 1. A short graded-subalgebra reduction

Let L be the free rational graded Lie algebra on the original degree-one
space. Any graded Lie subalgebra A has a homogeneous free generating set
obtained by lifting a homogeneous basis of A/[A,A]. The lifts generate by
induction on degree and are irredundant; the homogeneous Shirshov lemma
makes them free. This is the previously credited ordinary free-Lie theorem,
not a new structural result about arbitrary Lie algebras.

Fix nonzero C in Lp and a nonzero U in L_(p+1). The graded vector space

    A = Q*C + Q*U + direct_sum_(j>=p+2) L_j              (1)

is a Lie subalgebra: [C,C]=[U,U]=0 and [C,U] has degree2p+1>=p+2.
The classes of C,U are independent in A/[A,A], even for p=1 (the sole
possible degree2 bracket is [C,C]=0). Thus they can be selected as two
members of a homogeneous free basis of A.

For q>=p+2, D in Lq and V in L_(q+1) belong to A. If

    [C,V]=[U,D],                                      (2)

the prior Remeslennikov--Stohr two-coefficient inner-solution theorem
implies D,V belong to Lie(C,U). The accessible exact statement is
Altassan2013 Theorem3.3: coefficients which are members of a free basis
have only inner solutions, in any finite or infinite free rank. It is
applied to A, NOT by pretending that C,U are original free generators
of L. This distinction removes the apparent decomposable-U obstruction
in the earlier degree-three investigation.

If two independent U1,U2 in L_(p+1) gave (2), replace (1) by the subalgebra
with all three low-degree generators C,U1,U2 and the same high-degree tail.
The same argument makes them free basis elements. D would lie in
Lie(C,U1) intersect Lie(C,U2)=Q*C. Since q>p and D!=0 this is impossible.
Also U=0 forces V=0 by the free-Lie centralizer theorem. Consequently

    ker((U,V) -> [U,D]+[C,V]) has dimension at most one. (3)

No bound on p or q is involved.

## 2. Nonzero quadratic obstruction when q>=p+2

Assume first p>=2. For a nonzero kernel direction use the sign in (2).
In a homogeneous free basis of A containing C,U, project all other
basis elements to zero. This fixes D,V and commutes with ad_C. The image
of L_(p+2) is zero: the only degree-one basis words in C,U have weights
p,p+1; the first nonzero bracket has weight2p+1>p+2. For p=2 the only
potential weight4 bracket is [C,C]=0, so the statement still holds.

If [U,V] lay in [L_(p+2),D]+[C,L_(q+2)], projection would give

    [C,V]=[U,D],     [C,Z]=[U,V]                     (4)

inside the free Lie algebra on C,U. The cyclic-word double-primitive
lemma, proved in `type1-third-proof.md`, says that every ordinary
word-length>=2 component of D,V,Z is zero. But D has weight q>p+1,
so cannot have any word-length-one component. This contradicts D!=0.
Thus

    [U,V] not in [L_(p+2),D]+[C,L_(q+2)].             (5)

For p=1 the projection of L3 is Q*[C,U], rather than zero. The same
highest-U-count argument as the earlier type-one proof applies directly:
write D as a sum by the number of U letters and choose its highest
nonzero component D_m. It has m>=1. Equation(2) makes the corresponding
V component have m+1 copies of U. The bracket [U,V] has m+2, whereas
[[C,U],D] has at most m+1. Taking U-count m+2 in a purported relation
contrary to(5) gives precisely the two equations(4) for D_m and its
associated components. The double-primitive lemma again contradicts
D_m!=0. This recovers the prior type-one obstruction with the simpler
subalgebra reduction (1).

## 3. The two boundary leading types

If q=p+1, necessarily p>=2 in our c>=6 range. Take the subalgebra
A=Q*C + direct_sum_(j>=p+1) L_j. Its weight-(p+1) component is a space
of free generators (no bracket has this weight). Choose a basis including
D. Project a first-kernel equation [U,D]+[C,V]=0 by killing C and all
other free generators outside L_(p+1). It gives [U,D]=0 in the free
algebra on L_(p+1), so U is a scalar multiple of D. Then [C,V]=0
forces V=0 because deg V=p+2 differs from deg C. Conversely (D,0)
is a kernel vector. Thus the integral kernel is generated by

    (D/content(D), 0),                               (6)

up to sign. This is the exact Nielsen direction, not a nonzero quadratic
obstruction. The move x -> y^k*x preserves [x,y] exactly and shifts its
first affine parameter by plus or minus content(D). All remaining changes
in x have degree>=p+2 and are among the final correction variables;
y is unchanged. Retain every residue 0,...,content(D)-1 and solve the
final integer system for each. This is finite and complete, even for
nonprimitive leading D. An arbitrary single affine representative would
be insufficient.

If p=q, then p>=2. In the graded subalgebra direct_sum_(j>=p) L_j,
C,D are independent degree-p free generators. The inner-solution theorem
places every first-kernel U,V in Lie(C,D). These have weight p+1,
which is not a positive multiple of p when p>=2. Hence U=V=0.
The first correction is injective; the final one is an ordinary integer
linear system. No injectivity of the final system is needed.

## 4. Finite integral lifting

For every complete leading pair take integral Hall lifts x0,y0. The
first correction uses weights p+1,q+1. Solve its full integer affine
system. Reject inconsistent branches. A zero kernel gives one integral
first correction, followed by the final integer system with image
[L_(p+2),D]+[C,L_(q+2)]. The adjacent-weight case is treated by all
Nielsen residues as in Section3.

Otherwise q>=p+2 and the full first solution set is a primitive integral
line v+nK. Its final central residual is integer-valued quadratic in n.
The only quadratic interaction through c=p+q+2 uses corrections of
weights p+1 and q+1. Interactions involving two first-factor corrections
and D have weight2(p+1)+q>c, and the symmetric bound is the same.
Nonlinear Hall-power terms and conjugation corrections have weights beyond
c. Fixed higher coordinates affect only the constant and linear terms.
The final correction lattice is independent of n.

Modulo its rational span the quadratic coefficient is a nonzero scalar
multiple of [U,V], by(5). A rational cokernel coordinate therefore gives
a nonzero quadratic polynomial. Enumerate its at most two integer roots;
for every root test the ENTIRE integral final lattice, including all
congruences, and verify the constructed factors in N. This covers every
integer solution of the original branch and terminates.

There are finitely many complete leading branches. Their union decides
the stated target stratum. The proof does not decide arbitrary lower
leading layers, assert a practical complexity bound, or certify novelty.

## Dependencies and audit limits

The homogeneous Shirshov source is Bryant--Kovacs--Stohr2005, introduction
on printedp147, already archived/read/viewed for earlier N8 arguments.
Altassan2013 Theorem3.3 and its complete proof on pp24--25 were previously
read; it credits Remeslennikov--Stohr2007. Neither the inner-solution theorem
nor the support principle is claimed as new. The elementary double-primitive
proof is retained in full in the earlier note; its novelty is unverified.
The new ingredient here is the graded-tail application(1), its uniform
correction consequences, and their combination with integral lifting.

The original N8 HTML and linked background were reread and the actual
rendered statement viewed again during this derivation. The background's
old class-two-only status is not treated as a current literature survey.
No Kourovka argument was imported. Independent specialist review and a
matching-theorem literature audit remain necessary before novelty claims.
