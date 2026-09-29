# N9(a): an undecidable retract problem in one fixed nilpotent group

Candidate proof,29 September2026. Independent specialist review and novelty
assessment are outstanding. The accompanying [audit](audit.md) separates
the mathematical argument, prior results and finite computational checks.

**Theorem.** There exists a fixed finitely generated torsion-free group G
of nilpotency class two such that the following problem is undecidable:
given two noncommuting elements a,b of G, decide whether <a,b> is a
retract of G. Indeed, for fixed generators x0,x1,x2 of G, undecidability
already holds for the subgroups

    H_n = <x0, x1^(3n+1) x2^-1>,       n in N.

Thus the proposed answer to GroupWorld N9(a) is negative, with the
ambient group fixed. N9(b), concerning free nilpotent groups, is a
separate prior affirmative result. We make no new claim for part(b).

Throughout, [g,h]=g^-1 h^-1 g h. All matrix lattices and all existential
solutions below are integral; matrix rank is taken over Q.

## 1. A single fixed Diophantine equation

Choose a nonrecursive computably enumerable set S in N containing0 and1.
For example, add these two elements to a shifted copy of a fixed
nonrecursive computably enumerable set. The DPRM theorem provides a
fixed polynomial P with integer coefficients such that

    n in S  iff  there exist y1,...,ym in Z with P(n,y1,...,ym)=0.       (1)

The version with existential variables in N gives this version by
replacing each such variable with a sum of four squares. Only the
existential variables are replaced; n is still the free input parameter.
Both the polynomial and its number of variables are fixed.

Use a finite arithmetic circuit for P built from additions,
multiplications and integer constants. Give every input, constant and
gate output a distinct scalar label. Write p for its parameter label and
o for its output label. Negative coefficients may be implemented using
negative integer constants and multiplication. The circuit is fixed
once and for all, independently of n.

We use DPRM as a prior theorem. A precise effective parameter version is
Larchey-Wendling--Forster, *Hilbert's Tenth Problem in Coq (Extended
Version)*, Theorem8.3; Section9 gives the four-square conversion. The
fixed-polynomial quantifiers also appear in Jones, *Universal diophantine
equation* (1982). Source details and reading limits are in the audit.

## 2. A fixed lattice of alternating forms

Start with coordinate indices0,1,2,3. For each scalar label z introduce
two new distinct indices U_z,V_z, disjoint from all other indices. Let D
be the total number of coordinates. Define L to be the set of integral
alternating D-by-D matrices M satisfying the following homogeneous linear
equations.

For every label z:

    M[0,U_z]=0,   M[1,V_z]=0,
    M[1,U_z]+M[0,V_z]=0.                                      (2)

For a constant label z=c:

    M[0,V_z]=c M[0,1].                                        (3)

For addition and multiplication gates, respectively:

    z=x+y:   M[0,V_z]=M[0,V_x]+M[0,V_y],
    z=x*y:   M[U_x,V_y]=M[0,V_z].                             (4)

Require the output to vanish, and add four normalization equations:

    M[0,V_o]=0,
    M[0,3]=0,   M[1,2]=0,
    M[1,3]=M[0,2],   M[0,2]=3 M[0,V_p].                      (5)

These are linear equations in the upper-triangular entries of M, even
for a multiplication gate. Multiplication is recovered from the rank-two
condition, rather than imposed by a nonlinear equation defining L.

**Encoding lemma.** For any integer n, there exists M in L with rank two
and

    (3n+1)M[0,1]-M[0,2]=1                                  (6)

if and only if P(n,y)=0 has an integral solution.

**Proof.** First suppose M satisfies the stated conditions. Put
d=M[0,1], x=M[0,2] and t=3n+1. A rank-two alternating matrix has zero
four-by-four Pfaffians. On the indices0,1,2,3, equations(5) give

    d M[2,3]=x^2,        td-x=1.                            (7)

Since x=td-1, the first identity implies d divides1. More explicitly,

    d (M[2,3]-t^2 d+2t)=1.                                 (8)

Thus d=1 or d=-1; this also excludes d=0. By(5), x is divisible by3.
If d=-1, the second equation in(7) instead gives x=-3n-2, a
contradiction modulo3. Hence

    M[0,1]=1,    M[0,2]=3n,    M[0,V_p]=n.                  (9)

Define integral coordinates

    u_i=M[i,1],       v_i=M[0,i].

The rank-two Pfaffian identities and M[0,1]=1 give

    M[i,j]=u_i v_j-v_i u_j                                 (10)

for all i,j. In particular (u0,v0)=(1,0) and (u1,v1)=(0,1).
Equations(2) say that the coordinates at the two indices belonging to z
are

    (u_(U_z),v_(U_z))=(z,0),
    (u_(V_z),v_(V_z))=(0,z),       z=M[0,V_z] in Z.           (11)

Now(3) assigns the stated constants. The first equation in(4) gives
addition, and the second gives multiplication because
M[U_x,V_y]=x*y by(10)--(11). The output is zero. All gate values are
integers and the parameter is exactly n, so the circuit yields an
integral solution of P(n,y)=0.

Conversely, given such a solution, evaluate every gate over Z. Assign
the pairs in(11) to its scalar values, and assign

    (u0,v0)=(1,0),    (u1,v1)=(0,1),
    (u2,v2)=(0,3n),   (u3,v3)=(-3n,0).

Define M by(10). It is integral, alternating and has rank exactly two
since M[0,1]=1. Direct substitution verifies(2)--(5), and(6) is
(3n+1)-3n=1. This proves both directions. □

The argument used the full integer lattice, not rational points on the
same linear section. The integral unit in(8) and the congruence modulo3
are essential to this distinction.

## 3. Construct one fixed group

As a subgroup of a finite-rank free abelian group, L has an integral
basis B1,...,Bs, effectively obtainable as the full integer kernel of
the fixed linear system(2)--(5). Smith or Hermite normal form supplies
such a basis. Clearing denominators separately in a rational nullspace
would not in general suffice: every M in L must be an **integral**
linear combination of the B_l.

Let G have generators x0,...,x_(D-1),z1,...,zs and presentation

    [xi,xj]=product_l zl^(B_l[i,j])       (i<j),
    [xi,zl]=1,       [zl,zk]=1.                              (12)

This is a finitely presented torsion-free group of class at most two.
Here is a direct justification, including consistency of the presentation.
On Z^D times Z^s put

    (a,c)(b,e) = (a+b, c+e-sum_(i<j) a_j b_i B[i,j]),        (13)

where B[i,j]=(B1[i,j],...,Bs[i,j]). Bilinearity of the last term
gives associativity, and identities and inverses follow directly.
The standard basis elements satisfy(12). Conversely, those relations
collect every word uniquely as x0^a0 ... x_(D-1)^a_(D-1) z1^c1 ... zs^cs:
collection gives existence, and its image in(13) gives uniqueness.
Thus(13) realizes the presentation exactly. An element of finite order
first has a=0 by its Z^D coordinate, then c=0 by its central coordinate.

Only the fixed circuit and its fixed integer kernel determine G. No
generator, relation, quotient or lattice basis is changed when n changes.

Put a=x0 and b_n=x1^(3n+1)x2^-1. Their commutator c_n=[a,b_n]
has central coordinate vector

    q_n[l]=(3n+1)B_l[0,1]-B_l[0,2].                         (14)

This vector is nonzero for every n in N. To see this, use0 in S to
obtain by the encoding lemma a matrix M0 in L with M0[0,1]=1 and
M0[0,2]=0. Write M0=sum_l mu_l B_l with integral mu_l. Then

    sum_l mu_l q_n[l]=3n+1 != 0.                            (15)

In particular G has class exactly two, and a,b_n never commute.

The subgroup H_n=<a,b_n> is the free nilpotent group of rank two and
class two, with central generator c_n. Indeed its words collect as
a^r b_n^s c_n^k. If such a word is1, commuting it with a and b_n
forces s=r=0 because c_n has infinite order; then k=0. The same
calculation shows Z(H_n)=<c_n>.

## 4. Retractions are exactly the encoded solutions

We prove

    H_n is a retract of G  iff  n in S.                     (16)

For necessity, let rho:G->H_n be a retraction. Since it is onto H_n,
every rho(z_l) is central in H_n, hence equals c_n^lambda_l for
some integer lambda_l. Write

    rho(x_i)=a^r_i b_n^s_i c_n^k_i.

Preserving the commutator relations(12) gives

    sum_l lambda_l B_l[i,j]=r_i s_j-s_i r_j.                 (17)

Set M=sum_l lambda_l B_l. It belongs to L and has rank at most two
by(17). Since rho fixes c_n, (14) gives

    1=sum_l lambda_l q_n[l]=(3n+1)M[0,1]-M[0,2].             (18)

So M is nonzero and has rank exactly two. The encoding lemma now
gives an integral solution of P(n,y)=0, and(1) yields n in S.

For sufficiency, suppose n in S. The encoding lemma supplies a rank-two
M in L satisfying(6); write M=sum_l lambda_l B_l with lambda_l in Z.
Use u_i=M[i,1],v_i=M[0,i] as in(10). Define images of the generators by

    rho(x_i)=a^u_i b_n^v_i,
    rho(z_l)=c_n^lambda_l.                                 (19)

Their commutators agree with(12) by(10), and every central relation
holds because c_n is central in H_n. Thus(19) defines a homomorphism
G->H_n. Equations(5) and(9) give

    (u0,v0)=(1,0),    (u1,v1)=(0,1),    (u2,v2)=(0,3n).

Consequently rho(a)=a and

    rho(b_n)=rho(x1)^(3n+1) rho(x2)^-1
             =b_n^(3n+1) b_n^(-3n)=b_n.

So rho is a retraction. No central correction or further divisibility
condition is required for this particular pair of generators. This
proves(16). □

The computable map n -> [x0,x1^(3n+1)x2^-1] therefore reduces membership
in the fixed nonrecursive set S to the retract problem in the one fixed
group G. A decision algorithm for that group would decide S, proving
the theorem. Writing the power as an ordinary repeated word is already
an effective reduction; no compressed-word convention is needed.

## 5. Scope and limitations

All H_n are abstractly the same rank-two free class-two group; their
embeddings in G vary. They are not assumed to be retracts during the
construction. This avoids the equation-reflection obstruction in the
earlier unsuccessful attempt to vary already known retracts of a fixed
base group.

The argument proves existence of an effectively constructible fixed
presentation from any suitable DPRM polynomial. We have not expanded a
universal polynomial into its full numerical group presentation. The
implemented fixture instead uses the small equation(y+1)^2=n and checks
all construction stages, including integer-kernel saturation and actual
GAP homomorphisms. Those finite checks support implementation details;
undecidability follows from the general proof and the imported DPRM
theorem, not from experiments.

This is a candidate full answer to the previously unresolved part(a).
Together with the prior part(b), it gives proposed whole-entry coverage
of N9. It is not a second proof of the prior uniform theorem counted as
a new result. Novelty and correctness still require external review.
