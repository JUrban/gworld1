# A decision procedure for one commutator in free nilpotent groups of class five

**Candidate extension of N8(b), 28 September 2026.** This proof is being checked during the run; see the dated claim ledger for the verified scope. Bibliographic novelty remains provisional and no external review has occurred.

**Theorem.** For every finite rank r, there is an effective algorithm deciding whether a given element of N=F_r/gamma_6(F_r) is a single commutator. On a positive instance the algorithm constructs two factors. The procedure is uniform in r.

We use [x,y]=x^-1 y^-1 x y. The rank-zero and rank-one cases are immediate. All remaining computations use integral Hall collection coordinates, or equivalently the integral Magnus expansion through degree five. The Lie layer gamma_i/gamma_(i+1) is the degree-i piece L_i of the free Lie ring on V=Z^r. We write L_i(Q) for its rationalization. Polynomial factorization over Q and Smith normal form over Z are effective.

The original N8(b) asks about every nilpotency class, so this theorem is a partial answer to that question, not a whole-entry resolution.

## 1. Normalization and elementary linear facts

The moves (x,y)->(yx,y) and (x,y)->(x,xy), together with their inverses, preserve the commutator exactly. They induce the elementary determinant-one column operations on any additive layer in which the two factors lie. Thus dependent integral leading vectors can be normalized to (z,0). If their exterior product is nonzero, the [primitive-plane/Hermite enumeration](class3-proof.md) supplies all possibilities up to these moves: for w=u wedge v, its rational support plane P has a computable primitive integral lattice, w=d p wedge q for a chosen oriented basis and d>0, and the index-d sublattices have bases given by matrices [[a,b],[0,c]] with ac=d and 0<=b<a. This is a finite list.

The map Lambda^2 L_2(Q) -> L_4(Q), C wedge D -> [C,D], is injective. Indeed L_2 embeds into V tensor V, and this bracket is precisely the antisymmetric tensor C tensor D-D tensor C inside (V tensor V) tensor (V tensor V). The integral image can be checked by exact coordinate reconstruction. In particular [C,D]=0 for C,D in L_2(Q) if and only if C,D are dependent.

For nonzero z in L_1(Q), the map ad_z:L_m(Q)->L_(m+1)(Q) is injective for m>=2. Change rational basis so that z=X_1. In the associative tensor algebra, a homogeneous polynomial Y commuting with X_1 is a multiple of X_1^m: comparison in X_1Y=YX_1 shows all its words end in X_1; factor off that final letter and induct. The one-generator free Lie algebra has no degree-m component for m>=2, so the multiple must be zero.

## 2. Three correction kernels

Here is a short model that makes the kernels explicit. Let S=Q[t_1,...,t_r], M be its free module with basis e_1,...,e_r, and let the abelian space of linear polynomials act on M by multiplication. In the resulting semidirect Lie algebra, send X_i to (t_i,e_i). Denote the module component of a Lie element by mu. Then

    mu([X_i,X_j]) = t_i e_j-t_j e_i,
    mu([z,D]) = ell_z mu(D)        for D in L_m, m>=2,
    mu([C,D]) = 0                 for C,D in L',

where ell_z is the linear polynomial with coefficient vector z.

The map mu is injective on L_2 and L_3. The first assertion is immediate. For the second, present L_3 as V tensor Lambda^2 V modulo Jacobi tensors. Write a tensor with coefficients A_ijk antisymmetric in its last two slots. The vanishing of its module image imposes A_iik=0 from coefficients e_k t_i^2, and A_ijk+A_jik=0 from e_k t_i t_j for distinct indices. Thus A is fully alternating, precisely the Jacobi kernel. This also proves injectivity without any higher-degree metabelian embedding theorem.

Every derived module image satisfies sum_i t_i P_i=0 when written sum_i e_i P_i. In degree two, the module vectors with this property are exactly mu(L_2): the coefficient matrix of the linear P_i is skew-symmetric.

**Kernel 0.** If u,v in L_1(Q) are independent, the map

    L_2 + L_2 -> L_3,   (C,D) -> [C,v]+[u,D]

is injective. In the module model ell_v mu(C)=ell_u mu(D). The independent linear polynomials are relatively prime, hence mu(C)=ell_u T and mu(D)=ell_v T for a constant module vector T. The relation sum_i t_i T_i=0 forces T=0. Injectivity of mu on L_2 finishes the proof.

**Kernel A.** For z in L_1(Q) and Y in L_2(Q), both nonzero, the kernel of

    L_2 + L_3 -> L_4,   (C,D) -> [C,Y]+[z,D]

is {(lambda Y,0):lambda in Q}. Applying mu kills [C,Y], so ell_z mu(D)=0 in a free module over a domain. Therefore D=0. The injective exterior-square map on L_2 then forces C to be proportional to Y. The converse is immediate.

**Kernel B.** For independent u,v in L_1(Q), put w=[u,v]. The kernel of

    L_3 + L_3 -> L_4,   (C,D) -> [C,v]+[u,D]

is Q([u,w],[v,w]). As above, polynomial divisibility gives mu(C)=ell_u T and mu(D)=ell_v T, now with linear polynomial coordinates in T. The syzygy condition implies T=mu(W) for W in L_2. Injectivity in degree three gives C=[u,W], D=[v,W]. Jacobi reduces the original equation to [w,W]=0. Hence W is proportional to w by the exterior-square injection. Conversely the displayed vector is in the kernel. It is nonzero by injectivity of ad_u and ad_v on L_2.

These statements describe rational kernels. Their integral kernels are computed by Smith normal form. A one-dimensional rational kernel intersects the full coordinate lattice in Z k_0 for a computable primitive vector k_0; no rational solution is silently treated as integral.

## 3. Finite factor tests in the leading layer

We need to factor a nonzero homogeneous tensor g as [C,D], with degree(C)=p and degree(D)=q, in the cases p=1<q and (p,q)=(2,3). Use independent commuting variables T_I indexed by **ordered** words I of length p. For each word J of length q-p form

    Q_J(T) = sum_(I,K) g_(I,J,K) T_I T_K.

If g=CD-DC, then

    Q_J(T) = C(T) (sum_K D_(J,K) T_K-sum_I D_(I,J) T_I).

At least one Q_J is nonzero whenever this factorization exists. Otherwise, since C(T) is nonzero and the polynomial ring is a domain, D_(J,K)=D_(K,J) for every J,K. For p=1 this is invariance under a one-place cyclic rotation of D. For (p,q)=(2,3), rotation by two places also generates all rotations of a three-letter word. In either case D is cyclically invariant. Yet cyclic symmetrization annihilates every homogeneous Lie bracket of degree q>=2: UV and VU have the same cyclic symmetrization. Thus it annihilates D, whereas invariance would give qD. This contradiction proves the assertion.

If all Q_J vanish, reject this factorization type. Otherwise factor one nonzero homogeneous quadratic over Q. It has at most two distinct rational linear factors, so there are at most two possible directions for C. Test that each resulting tensor belongs to L_p(Q), and select a primitive integral representative C_0 in the Hall lattice. Solve [C_0,D_0]=g as an integer linear system in L_q.

This decides integral factorization: any integral C in the direction of primitive C_0 is kC_0 with nonzero integer k, and [kC_0,D]=[C_0,kD]. Thus an integral solution for some scaling exists precisely when the primitive test has one. This assertion does not require uniqueness of D.

When the leading factors must be fixed before higher layers are matched, we use the p=1 case. Here D_0 is unique by injectivity of ad_(C_0). All integral leading pairs in that direction are

    C=k C_0,   D=D_0/k,

where k ranges over the positive and negative divisors of the nonzero content of D_0. This is another finite list. If the unique rational D_0 is not integral, no integer scaling k can make D_0/k integral, so the direction is rejected.

## 4. The group-layer correction rule

After fixing the lower coordinates of x,y, write new factors as xc,yd. In the first degree where these corrections affect the commutator, its change is [C,Y]+[X,D], where X,Y,C,D are the appropriate leading Lie components. Terms of higher weight do not affect that matching step. All layers are free abelian, so matching one layer is an integer linear system.

This rule can be obtained by expanding the group identity for [xc,yd], or by multiplying the truncated Magnus series. In the final degree-five steps below, all omitted terms have weight at least six, so the linear correction is exact. At earlier steps we choose actual group lifts and recalculate their entire commutator before proceeding; no higher term is discarded from the target discrepancy.

## 5. First nonzero target component in degree two

Let g_2 be nonzero. It must be a decomposable integral exterior tensor. If not, reject. Otherwise enumerate the finite list of leading abelianization pairs u,v from Section 1. For each pair choose lifts x_0,y_0.

Matching degree three uses corrections in L_2+L_2. Kernel 0 gives at most one solution, and integer linear algebra decides its existence. Incorporate that solution into the lifts. Every possible solution with the chosen u,v now differs from these lifts by elements of gamma_3.

Matching degree four uses L_3+L_3. By Kernel B its integral solutions are either empty or

    q_0 + Z k_0.

There are only finitely many cases to retain. Simultaneously conjugating an **actual solution pair** by the target g preserves its commutator g exactly. On the degree-three corrections it adds

    K=([u,g_2],[v,g_2])=t k_0

for a nonzero integer t. All lower coordinates remain fixed. Hence every solution can be normalized to one of the residues q_0+n k_0, 0<=n<|t|, by a positive or negative power of this conjugation. The higher coordinates changed by the move will be covered at the next step.

For each retained residue choose actual lifts of its degree-three corrections and recompute the degree-five discrepancy. Correct it by L_4+L_4 through

    (C_4,D_4) -> [C_4,v]+[u,D_4].

This is an integer linear system. A positive answer yields the required factors. A negative answer for every residue and every leading pair is conclusive.

## 6. First nonzero target component in degree three

The abelianization vectors are dependent, and exact Nielsen moves normalize them to (z,0), with z nonzero. Both cannot vanish because then the commutator starts in degree four. Write the second factor's degree-two part as Y. We have g_3=[z,Y]. Section 3 gives finitely many integral leading pairs (z,Y), including all nonprimitive scalings.

For each pair fix lifts x_0,y_0, with y_0 in gamma_2. Matching degree four uses corrections C in L_2 and D in L_3. Kernel A says its integral kernel is generated by (Y/content(Y),0). The exact move (x,y)->(yx,y) adds Y to the degree-two correction of x and leaves y unchanged. Thus the affine solution parameter can be reduced modulo content(Y). Keep those finitely many residues.

For each, choose lifts and correct the remaining degree-five discrepancy by L_3+L_4 through

    (C_3,D_4) -> [C_3,Y]+[z,D_4].

All such terms have weight five, and all further corrections are irrelevant in N. Again the higher coordinates altered by normalization are precisely among those allowed here.

## 7. First nonzero target component in degree four

There are two possibilities.

**A nonzero abelianization survives.** Normalize to (z,0). The second factor has no degree-two part, since ad_z is injective and g_3=0. Hence g_4=[z,Y_3]. Section 3 gives a finite list of integral leading pairs, including all allowable scalings. For each pair, the degree-five correction is linear in L_2+L_4:

    (C_2,D_4) -> [C_2,Y_3]+[z,D_4].

**Both abelianizations vanish.** Then g_4=[C_2,D_2]. Recover its alternating tensor in Lambda^2 L_2 using Section 1. Unless it is an integral decomposable rank-two tensor, reject this branch. Otherwise enumerate all primitive-plane/Hermite pairs C_2,D_2 up to exact Nielsen moves, now applied to elements of gamma_2. The degree-five correction is linear in L_3+L_3:

    (C_3,D_3) -> [C_3,D_2]+[C_2,D_3].

The two branches together cover every solution.

## 8. Pure nonzero degree five

If a nonzero abelianization survives normalization to (z,0), successive injectivity of ad_z on L_2 and L_3 forces the second factor into gamma_4. Thus g_5=[z,Y_4], decided by Section 3. Any Lie factors lift immediately to group factors because their bracket has weight five and all errors have higher weight.

Otherwise both factors are in gamma_2. Since g_4=0, their degree-two vectors commute and therefore are dependent. Exact Nielsen moves normalize them to (C_2,0). The first vector cannot also vanish: a commutator of two gamma_3 elements is trivial in N. The remaining case is exactly g_5=[C_2,D_3], again decided by Section 3 and lifted without additional corrections.

## 9. Termination, completeness and evidence

Reject an element with nonzero abelianization and accept the identity. Every remaining target belongs to exactly one of Sections 5–8. Each branch uses finite leading-factor lists, integer linear systems, and, in Sections 5–6, finitely many residues whose periods are explicit nonzero integers. All procedures terminate. Every accepted branch constructs actual factors. The exact normalization moves and the full integer-kernel descriptions ensure every possible solution is represented in one of the branches. This proves both positive and negative correctness.

The prototype is `scripts/n8_class5.py`. Its deterministic checks and the separate GAP witness evaluation are recorded under `results/n8-class5-*`; these supplement, rather than establish, the general proof. The source audit and novelty qualifications remain those of the N8(b) candidate, with an additional class-five literature check in `literature/LEDGER.md`.

One new negative control has an independent short explanation. In rank two let

    h = ad_a^4(b) + ad_b^4(a) in L_5.

Its multidegrees are (4,1) and (1,4), whereas [L_2,L_3] has only multidegrees (3,2) and (2,3). Thus it is not a bracket of type (2,3). For type (1,4), the outer quadratics for middle words aab and bba are respectively -4 t_a^2 and -4 t_b^2. They have no common nonconstant factor, so no degree-one first factor is possible either. Lifting the two displayed Lie brackets to weight-five group commutators gives a noncommutator in N.
