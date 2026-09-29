# N9(a): proposed fixed-ambient undecidability construction

First structural lead:29 September2026, approximately20:02–20:04 UTC.
**Unadopted until construction, integrality, scope and source audits are
complete.** The preceding general criterion is in
`research/notes/N9-Heisenberg-rank-two-criterion.md`; its positive group
maps have already passed independent GAP/nq checks. The present universal
encoding was initially unchecked. Subsequent checks at20:10--20:12 UTC
compile the toy equation(y+1)^2=p into a single fixed group and independently
verify its saturated lattice and seven actual retractions in GAP. These
finite checks do not establish the universal undecidability assertion.

Proposed theorem: there is a fixed finitely generated torsion-free group
G of nilpotency class two for which deciding whether a subgroup generated
by two supplied noncommuting elements is a retract is undecidable.
This would answer N9(a) negatively; N9(b) remains the separately credited
prior free-nilpotent positive result.

## 1. Fixed Diophantine data

Fix a nonrecursive computably enumerable set S contained in N with at
least two elements. By the DPRM theorem there is one fixed polynomial
P(n,y1,...,ym) with integer coefficients such that, for n in N,

    n in S iff there exist integers y1,...,ym with P(n,y)=0.

The usual nonnegative-variable version suffices: replace each existential
nonnegative variable by a sum of four squares. The polynomial, its finite
arithmetic circuit, and every object built from that circuit below are
fixed once and for all. The integer n alone is input.

Choose a finite circuit using additions, multiplications and integer
constants whose output is P. Each input, constant and gate output has
a scalar label z. One label is the parameter n, denoted p below.

## 2. Encode the circuit in a fixed integral linear space of alternating matrices

Let the coordinate indices begin with0,1,2,3. For every scalar label z
introduce two further distinct indices U_z,V_z. Let L_Z be the lattice
of alternating integral matrices M satisfying the following homogeneous
linear equations. All coefficients and indices are fixed.

For each scalar label z impose

    M[0,U_z]=0,   M[1,V_z]=0,
    M[1,U_z]+M[0,V_z]=0.                                    (2)

For a constant label z=c impose M[0,V_z]=c M[0,1].
For an addition gate z=x+y impose

    M[0,V_z]=M[0,V_x]+M[0,V_y].

For a multiplication gate z=xy impose

    M[U_x,V_y]=M[0,V_z].                                   (3)

Finally impose M[0,V_output]=0.

The parameter-normalization block consists of

    M[0,3]=0,   M[1,2]=0,
    M[1,3]=M[0,2],
    M[0,2]=3 M[0,V_p].                                    (4)

Suppose M has rank two and M[0,1]=1. Write
M[i,j]=u_i v_j-v_i u_j with

    (u0,v0)=(1,0),   (u1,v1)=(0,1).

This expression is obtained integrally from u_i=M[i,1], v_i=M[0,i].
Equations(2) then mean

    (u_(U_z),v_(U_z))=(z,0),
    (u_(V_z),v_(V_z))=(0,z),

where z=M[0,V_z] is an integer. Equation(3) is precisely z=xy,
and the other circuit equations have their stated arithmetic meanings.
The last equation forces P(p,y)=0. Conversely, an integer circuit
solution gives an integral rank-two M by these coordinate vectors and

    (u2,v2)=(0,3p),   (u3,v3)=(-3p,0).

All its entries satisfy(2)--(4), the circuit equations and M[0,1]=1.

## 3. The input-dependent normalization forces M[0,1]=1

For input n put t=3n+1. Consider a rank-two integral M in L_Z with

    t M[0,1]-M[0,2]=1.                                    (5)

Write d=M[0,1] and x=M[0,2]. The four-by-four Pfaffian on0,1,2,3
vanishes. By(4) it says

    d M[2,3]=x^2.

Equation(5) gives x=td-1. Hence d divides1, so d=+1 or -1;
d=0 is separately impossible from the same two equations.
Also x is divisible by3 by(4). If d=-1, then x=-3n-2, which is
not divisible by3. Therefore d=1 and x=3n. The scalar parameter
p=M[0,V_p] is exactly n.

Consequently

    n in S iff there exists integral M in L_Z of rank two
                    with t M[0,1]-M[0,2]=1.                (6)

Both directions are integral. A rational solution is not substituted
for an integer solution. In particular the square block together with
the congruence, not just an affine chart chosen without justification,
forces the unit normalization.

## 4. One fixed torsion-free class-two group

Compute an integral basis B1,...,Bs of L_Z, the integer kernel of its
finite homogeneous linear system. Use the **full integer kernel**, not
arbitrarily scaled rational nullspace vectors: every integral matrix
in L_Z must have integral coordinates in this basis.

For its fixed dimension D, define G with generators x0,...,x_(D-1),
z1,...,zs and presentation

    [xi,xj]=product_l zl^(B_l[i,j]),
    [xi,zl]=[zl,zm]=1.

This is finitely presented and torsion-free of class at most two. An
explicit model is Z^D times Z^s, in normal coordinates x^a z^c,
with product

    (a,c)(b,e)=(a+b, c+e-sum_(i<j) a_j b_i (B_l[i,j])_l).

The bilinear central cocycle gives associativity and exactly the
displayed presentation. The coordinates prove torsion-freeness.

For input n, let

    h1=x0,     h2=x1^(3n+1) x2^-1,     H_n=<h1,h2>.

Their commutator vector q_n has entries

    q_n[l]=(3n+1)B_l[0,1]-B_l[0,2].

The earlier Heisenberg criterion says that, when q_n is nonzero,
H_n is a retract iff there is an integral lambda with

    lambda dot q_n=1,    rank(sum_l lambda_l B_l)=2.

Because B1,...,Bs are a basis of the whole integer kernel, this is
exactly(6). Thus a decision algorithm for retracts in this single G
would decide S.

There are two ways to handle the noncommuting hypothesis rigorously.
For the algorithmic reduction it is enough to compute q_n first: if
q_n=0, equation(6) is impossible, so answer no without consulting the
retract algorithm. Alternatively, q_n is in fact nonzero for all n:
two distinct parameters m1,m2 in S produce matrices in L_Z with
(M[0,1],M[0,2])=(1,3m1) and(1,3m2). A functional
t M[0,1]-M[0,2] cannot vanish on both. This also shows that G has
class exactly two, not merely at most two.

## 5. Audit targets before any promotion

- Verify the full lattice basis, including saturation, in an implemented
  small circuit rather than using independently cleared denominators.
- Check multiplication-gate signs and the rank-two coordinate recovery.
- Check the normalization block at d=0, negative d and nonunit d, and
  verify that removing the factor3 would admit a wrong parameter branch.
- Build the resulting fixed group for a small parameterized equation
  and verify positive retractions in native GAP, with negative parameter
  cases proved from the reverse extraction, not from a bounded search.
- Keep G and its basis fixed while n changes; only the supplied subgroup
  generators may vary.
- Match the original source's fixed/uniform distinction and retain the
  prior free-nilpotent theorem. The universal construction is generally
  not a free nilpotent group.
- Check DPRM's precise fixed-polynomial quantifiers in a primary source;
  search for a matching prior fixed-group retract theorem.

Unlike the older failed construction, this does not put variable copies
of a base group into a fixed ambient group as known retracts while fixing
one common target element. The entire family is tested for retraction;
its central commutators q_n vary. The criterion supplies equivalence,
not just a necessary equation-reflection condition.
