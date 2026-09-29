# A nonlinear single-commutator family in classes 11,15,19,...

Candidate extension, 29 September 2026, before the original deadline.
This extends the same partial N8(b) candidate; it is not a decision
procedure for all targets in arbitrary class. Independent specialist
review and a conclusive novelty assessment remain outstanding.
The original uncounted lead is preserved in
`research/notes/N8-odd-adjoint-family-lead.md`. The execution evidence
and proof audit are in [odd-adjoint-audit.md](odd-adjoint-audit.md).

## Statement and dependencies

**Proposed theorem.** Let h>=3 be odd and put c=2h+5, so c=11,15,19,... . In the rational
free Lie algebra L of any finite rank r>=2, choose nonzero z in L1,
T in L2 and rho in Q. Set delta=ad_z and

    V_h = ad_T^h(delta T),
    D_h = -sum_(i=0)^((h-1)/2) (-1)^i
                    [ad_T^i z, ad_T^(h-i) z].                 (1)

The weights of D_h and V_h are 2h+2 and 2h+3. There is an algorithm which
recognizes targets g in F_r/gamma_(c+1) whose nonzero leading term is

    w = rho [z,D_h(z,T)] in L_(c-2),                          (2)

and decides single-commutator membership for all such targets, allowing
arbitrary terms in the last two layers and constructing integral factors
on positive inputs. Inputs outside (2) must be reported as unsupported,
not as negative. The h=1 control is an already covered iterated-adjoint
family in class seven, not additional scope.

The argument uses the delta-stable free alphabet of L' constructed and
credited in `problems/N8/class9-proof.md`. Include T among its weight-two
seeds. Write T_j=delta^j T. The exact leading-pair Nielsen normalization
and integral Hall-coordinate machinery are those already used in the
previous N8 proofs. Commutators are x^-1 y^-1 x y.

## 1. The identity and its jet form

For any derivation A=ad_T and any element z, the derivation rule and
cancellation of consecutive summands give, for odd h,

    A sum_(i=0)^((h-1)/2) (-1)^i [A^i z,A^(h-i) z]
         = [z,A^(h+1)z].                                    (3)

The final middle bracket is zero. Since delta T=-A z, we have
V_h=-A^(h+1)z, and therefore

    delta V_h = [T,D_h].                                    (4)

There is also an expression for D_h using only the free letters T_j:

    D_h = A^(h-1) T_2
          +sum_(i=1)^(h-1) A^(i-1)[T_1,A^(h-1-i)T_1]
          +sum_(i=0)^((h-3)/2) (-1)^i
                                  [A^i T_1,A^(h-2-i)T_1].   (5)

To check it, differentiate A^h T_1. All summands except the i=0
summand visibly contain an outer A. The remaining
[T_1,A^(h-1)T_1] is an A-image by the even-power instance of (3).
Thus (5) has the same A-image as (1). Both belong to L', where T is a
free generator; their difference has weight 2h+2 and commutes with T,
so is zero. In particular D_h has bracket length h in the delta-stable
alphabet. Its coefficient on T_0^(h-1) T_2 is one. It is nonzero.

The first new case is

    h=3,  D_3=[T,[T,T_2]]+2[T_1,[T,T_1]],
          V_3=[T,[T,[T,T_1]]].                            (6)

## 2. Excluding leading factors both in L'

Project L' onto the free Lie algebra on the single seed chain T_j,
killing all other seed chains. The component of delta D_h with one
T_3 and h-1 copies of T_0 is A^(h-1)T_3. It is nonzero. In a bracket
of two homogeneous elements of weights at least two, a contribution
to this component requires one factor to contain T_3 and the other to
use only T_0. A nonzero Lie polynomial on just T_0 is a multiple of
T_0. Consequently one of the two projected leading factors would
have to have weight two, and their bracket would lie in [T_0,L'].

But the coefficient of the associative word

    T_1 T_0^(h-2) T_2

in delta D_h is h+2, which is nonzero. This word neither starts nor
ends with T_0, so it cannot occur in [T_0,L'].

Here is a direct coefficient derivation. In (4), the coefficient of
T_0 T_1 T_0^(h-2) T_1 comes only from differentiating the two possible
T_1 positions in A^h T_1; its value is h+1. Because this word ends
with T_1, equation (4) says that the coefficient of
T_1 T_0^(h-2) T_1 in D_h is h+1. Its derivative contributes h+1 to
the desired word. Differentiating the first T_0 in
T_0^(h-1)T_2 contributes one more. There are no other contributions.

Thus every normalized leading pair for (2) has weights (1,2h+2), up
to interchanging the factors and the corresponding sign. The finite
signed-scale enumeration below absorbs that interchange as in the
earlier N8 arguments.

## 3. The degree-one direction is unique

Make a rational change of degree-one basis with z=a, and write
T=[a,b]+T', with T' involving only the other degree-one letters. For
each fixed inner associative word J of length 2h+1, form the
commutative outer quadratic Q_J from coefficients of uJv in w.
If w=[C,D] with C in L1, then C divides every Q_J. It suffices to
exhibit one nonzero Q_J proportional to a^2.

In the formal associative algebra on a and T, expansion of (1) gives
the following useful coefficient formula:

    coefficient_(T^r a T^s a T^t)(D_h)
          = (-1)^s binomial(h+1,s),    r+s+t=h.             (7)

Indeed, the two products in each bracket combine into
the sum over all i=0,...,h of binomial(i,r)binomial(h-i,t), with sign
(-1)^(r+t+1). Vandermonde's identity and oddness of h give (7).

If T' has a nonzero coefficient tau on uv, for distinct other basis
letters u,v, take J=(uv)^(h-1) a (uv). Its 2h non-a letters force
every occurrence of T to come from T', so both outer letters must
be a. Formula (7), applied to a T^(h-1) a T a in [a,D_h], gives

    Q_J = -rho binomial(h+2,2) tau^h a^2 != 0.             (8)

If T'=0, choose b as another basis letter, so T=[a,b]. Take
J=b(ab)^(h-1)a^2. All h occurrences of b are in J, so again both
outer letters must be a. The coefficient of (ab)^h a^3 in [a,D_h]
is -2^(h+1): the coefficient in D_h of b(ab)^(h-1)a^3 is -1,
whereas that of (ab)^h a^2 is
sum_(s=0)^h binomial(h+1,s)=2^(h+1)-1. Hence

    Q_J = -rho 2^(h+1) a^2 != 0.                          (9)

Every degree-one first factor is therefore proportional to z.
For each such nonzero factor, its adjoint is injective in weight
2h+2, so the second leading factor is determined.

## 4. Scope recognition and finite integral leading pairs

Factor a nonzero outer quadratic over Q and examine its finitely many
rational linear factors, represented by primitive integral vectors C0.
Solve ad_C0(D0)=w by rational linear algebra. Then decide whether D0
is a scalar multiple of D_h(C0,T) for some T in E=L2.

Polarize the homogeneous degree-h map in T to obtain

    Phi_h: Sym^h(E) -> L_(2h+2).

This linear map is injective. In the jet alphabet, the coefficients of
the words (e_i1)_0 ... (e_i(h-1))_0 (e_ih)_2 recover the symmetric
tensor entries: in (5) only A^(h-1)T_2 contributes to this jet pattern,
and only its first associative product places T_2 at the end. Fix a
consistent symmetric-tensor normalization when implementing the map.

Solve for the symmetric tensor and test whether it is a nonzero scalar
multiple of a pure h-th power. This test is rational and finite:
all flattenings must have rank one, a nonzero rational tensor fibre
supplies T, and direct substitution determines and checks rho. The
scalar rho absorbs any putative h-th-root obstruction; no decision
oracle for unrestricted rational polynomial equations is being used.
Alternatively check one rank-one flattening, recover its common
one-dimensional factor, and verify the full pure-power identity.

Uniqueness of the direction shows that at most one direction succeeds.
If D0 is nonintegral, there is no integral leading pair. Otherwise all
integral leading pairs are

    C=k C0, D=D0/k,   k a signed divisor of content(D0).  (10)

Changing C0 to kC0 multiplies D_h by k^2, so each branch still has
D=sigma D_h(C,T) for a nonzero rational sigma. Every scale is retained.

## 5. The first correction kernel

For a branch of (10), the map

    L2 + L_(2h+3) -> L_(2h+4),
    (U,W) |-> [U,D]+delta W                            (11)

has kernel Q*(T,-sigma V_h).

Equation (4) supplies this line. To exclude all other directions,
include T in a basis of E. For another seed S, project associative
words to seed sequence S,T,...,T, retaining their jet indices.
Encode those indices by variables u,t1,...,th. The derivation delta
acts as multiplication by u+t1+...+th. The projected [S,D] is a
nonzero polynomial independent of u; its T_0^(h-1)T_2 coefficient
is sigma. It is not divisible by u+t1+...+th. Thus the coefficient
of S in U vanishes. Each S is separated by its seed count, and U
has no other degree-two components. Finally delta is injective on
L', so W is uniquely determined once U is proportional to T.

## 6. The quadratic obstruction

Put Q=[T,V_h]=ad_T^(h+1)T_1 in L_c. This element is outside

    [L3,D]+delta L_(c-1).                               (12)

Project again to the single chain T_j. The first summand in (12)
has bracket length h+1, whereas Q has length h+2. The component
of L_(c-1) with length h+2 has the minimal possible weight
2(h+2)=c-1, so it uses only T_0. A Lie polynomial of that length
on a single letter is zero. Its delta-image therefore cannot
contribute to Q. The associative word T_0^(h+1)T_1 in Q has
coefficient one, so Q is nonzero. This argument applies in every
finite rank, not only in the structural test rank.

## 7. Finite integral group lifting

Lift each pair (10) by integral Hall group words. Match degree c-1
by the complete integer solution lattice of (11). If soluble, its
solutions form an affine line v+nK, n in Z, where K generates the
entire integral kernel. Thus K is a nonzero rational multiple of
(T,-sigma V_h), and no rational solutions are substituted for
integral ones.

After applying these corrections, the degree-c residual is an
integer-valued polynomial of degree at most two in n. The variable
factor corrections have weights two and c-2, so their mutual
bracket first appears in weight c. Two weight-two corrections with
the weight-(c-3) leading second factor first interact in weight c+1.
The quadratic coefficient modulo (12) is therefore a nonzero scalar
multiple of Q. A rational cokernel functional yields a nonzero
quadratic equation, with at most two integer roots. Test each against
the full integral final correction lattice and construct factors
when it passes. This is the same integral lifting mechanism already
implemented for the earlier third-from-last-layer family.

All branching is finite. Every group solution has a normalized leading
pair in (10), then a point in the complete first integral affine line.
Its parameter must pass the final rational obstruction and the full
integer lattice test. Conversely, every admitted parameter constructs
factors whose commutator is the target. This proves completeness and
termination for the stated family.



## 8. Effective polarization and implementation

The code `scripts/n8_odd_adjoint.py` is parameterized by h and rank.
It solves the linear system for ad_C0 composed with Phi_h directly;
this is equivalent to the two injective inversions in Section 4 and
avoids constructing a much larger adjoint matrix.

Here are explicit coordinate conventions. Let alpha be a multi-index
of total degree h and K_alpha the coefficient of t^alpha in
D_h(C0,sum_i t_i e_i). This coefficient is computed exactly by

    K_alpha = (1/product_i alpha_i!)
               sum_(0<=beta<=alpha) (-1)^(h-|beta|)
                   product_i binomial(alpha_i,beta_i)
                   D_h(C0,sum_i beta_i e_i).

The finite difference kills every other degree-h monomial. Each
K_alpha has integral Hall coordinates. The unknown coefficient
S_alpha in sum K_alpha S_alpha is the symmetric tensor entry with
multiplicities alpha, so a pure tensor has S_alpha=rho product t_i^alpha_i.
No additional multinomial factor is applied to S_alpha.

Choose a nonzero diagonal S_(h e_i). Any nonzero pure tensor has one.
Set rho=S_(h e_i), t_i=1 and

    t_j = S_((h-1)e_i+e_j)/rho.

Check every identity S_alpha=rho product t_j^alpha_j. Passing these
finitely many rational equalities proves pure-power recognition;
failing them rejects this scope. Zero tensors and absent nonzero
diagonals cannot represent a nonzero pure power. The scalar absorbs
both signs and the original scale of the chosen coordinate.

The integral lifting code uses full integer affine systems, exact
Magnus expansions and the existing Newton-polynomial lattice solver.
Its general parameterization does not mean that high classes have
been computationally benchmarked. Group decisions and independent
GAP replay were completed for rank two/class eleven; rank-three tests
cover recognition only. Formal identities were also checked at h=5
and h=7, corresponding to classes fifteen and nineteen. The all-rank,
unbounded-class-family conclusion rests on Sections 1--7.
