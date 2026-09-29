# Fifth- and sixth-from-last targets

29 September 2026. Candidate extension of the same partial N8(b) result.
The implementation and independent replay status are in
`fifth-sixth-layer-audit.md`. This does not decide every layer in arbitrary
class and does not claim specialist validation or established novelty.

**Proposed theorem.** Let N=F_r/gamma_(c+1), with finite rank r. Single-
commutator membership is decidable for every target with nonzero leading
degree d>=4 and c-d in {4,5}. A positive decision constructs its factors.
Combined with the four previous deepest layers, this covers gamma_(c-5)
for c>=9. The previous all-target class-three-through-ten results remain.
Ranks zero and one have only the identity as a commutator and are immediate.

Use [x,y]=x^-1 y^-1 x y. The previous leading-pair normalization and
enumeration are unchanged: for W in L_d enumerate every normalized
integral C in L_p,D in L_q, with p<=q, p+q=d and [C,D]=W. This retains
signed integral scales and all equal-weight oriented Hermite sublattices.
There are finitely many branches, and every solution has a representative
in one of them. These are the same credited leading-pair arguments as in
`third-layer-proof.md` and the earlier audits.

## 1. The correction maps needed here

For fixed C,D write

    A_t(U,V)=[U,D]+[C,V],  U in L_(p+t), V in L_(q+t).

The following rational statements are proved in full in
`../../research/notes/N8-general-offset-lead.md`, Sections 1--3 and the
final audit. They generalize the first-offset proof without assuming that
C,D or U are original degree-one free generators.

* If t<q-p, ker A_t has dimension at most one. For a nonzero kernel
  direction (U,V), the quadratic vector [U,V] has nonzero image modulo
  im A_(2t).
* If t=q-p>0, the kernel is exactly Q*(D,0).
* If a pre-Nielsen A_t has nonzero kernel, A_(t+1) is injective.
* If t>q-p (also for p=q), every kernel pair lies in Lie(C,D).

For clarity, the first statement uses the graded subalgebra

    Q*C + Q*U + direct_sum_(j>=p+t+1) L_j.

C,U extend to a homogeneous free basis. The prior inner-solution theorem
puts D,V in Lie(C,U). Two independent U directions would force D into
the intersection Q*C, which has the wrong degree. For the obstruction,
project to C,U and take the highest U-letter count of D. A correction
of weight p+2t contains at most one U letter, whereas [U,V] has two more
than that highest count. The cyclic-word double-primitive lemma then
contradicts the nonzero component of D. No assumption t<p is required.

For the consecutive-map statement, a next-offset direction U' can be
chosen as a new free generator in this graded subalgebra when p>=2.
For p=1 its only additional possibility is a multiple of [C,U]. In the
elimination alphabet U_j=ad_C^j U, simultaneous primitives of [U,D] and
[[C,U],D] would require the position polynomial P of each chain-length
component of D to satisfy, modulo S=x1+...+x_(m+1),

    P(x2,...,x_(m+1))=P(x1,...,xm),
    x1*P(x2,...,x_(m+1))=x_(m+1)*P(x1,...,xm).

Substitute x_(m+1)=-(x1+...+xm). Their difference forces
(2x1+x2+...+xm)P=0 in a polynomial domain, hence P=0. This contradicts
D!=0. The detailed note also justifies that the primitives belong to
the same elimination algebra.

These lemmas give a particularly short classification of A_2 for d>=4:

* q>p+2: zero kernel or one exceptional direction, with a nonzero
  quadratic obstruction at offset four and injective A_3.
* q=p+2: exactly the Nielsen line.
* q<p+2: injective.

For the last case, p=q>=3 has no weight p+2 component in Lie(C,D).
If p=q=2, U,V are multiples of [C,D], and [[C,D],D] and [C,[C,D]]
are independent. If q=p+1, d>=4 implies p>=2; only p=2 permits a
nonzero component, namely V proportional to [C,D], whose image is
nonzero. This accounts for every boundary case.

## 2. Retain finitely many first corrections

For each leading pair use integral Hall lifts x0,y0 and solve A_1 over
the integers for the degree d+1 residual. Reject an inconsistent branch.
A zero kernel supplies one correction. If q=p+1, retain every residue
of its primitive integral parameter modulo content(D), using the exact
commutator-preserving move x->y^k*x. The period is not assumed to be one.

Otherwise the full integral solution is v+nK. Its residual in degree
d+2 is integer-valued quadratic in n, with nonzero quadratic coefficient
modulo the rational span of im A_2. A rational cokernel coordinate gives
at most two integer roots. Retain exactly those passing the full integral
A_2 lattice test. This fixes finitely many first-corrected pairs x,y.
It does **not** fix an arbitrary second-layer representative.

The nonzero quadratic term is [U,V], up to a nonzero scalar and sign.
Pure second powers in either factor require degree at least d+p+2
or d+q+2, above d+2. Fixed higher coefficients affect only the constant
and linear terms. Thus the previous quadratic argument applies in the
quotient of class d+2 even though the current ambient class is larger.

## 3. The second correction and its coupled successor

For each fixed first-corrected pair solve the complete integral A_2
system. Reject inconsistency. If its kernel is zero, apply the unique
correction and go to the joint tail starting at offset three (Section 4).
For q=p+2, normalize the Nielsen line by **all** residues modulo
content(D), then use that same joint tail for each residue. The exact
Nielsen move changes no already fixed lower offset; every change above
offset two remains among the tail variables.

In the exceptional case q>p+2, write the full second correction as
v+kK. Let pair(k) be its Hall group lift, and let r0+k*r1 be the
degree d+3 residual. It is affine: interactions of two offset-two
corrections begin in degree d+4. A_3 is injective by Section 1.
The **joint integral system** is

    A_3 Z - k*r1 = r0.                                  (1)

An integer Hermite calculation gives either no solution, one point,
or a complete primitive integral affine line. Indeed the rational kernel
projects injectively to the k coordinate because A_3 is injective, so
its dimension is at most one. For a line, write

    Z=Z0+t*J,       k=k0+m*t,       t in Z, m!=0.         (2)

The integer m can have absolute value greater than one. Keep its exact
value; replacing it by one would add invalid lifts. A point from (1)
fixes the offset-two and offset-three corrections and proceeds to the
joint tail starting at offset four.

For a line apply both corrections (2) and compute the degree d+4
residual as a polynomial in t. It is at most quadratic. Its quadratic
coefficient modulo im A_4 is m^2 times the nonzero obstruction of A_2.
Here two offset-two corrections are the only quadratic interaction:
offset-two/offset-three interactions start at d+5, two offset-three
corrections at d+6, and nonlinear terms involving two corrections on
the same factor start strictly beyond d+4. Varying offset-three
corrections and fixed first corrections therefore contribute only linearly
at this degree. Consequently a rational cokernel coordinate again gives
at most two integer t values. Test every integral A_4 congruence.

For each surviving t retain the corrected pair and solve the **entire**
remaining tail starting at offset four. In class d+5 this includes
offsets four and five together. Selecting one offset-four witness and
trying to correct only the final layer is not justified.

## 4. Exact joint tails and termination

For a fixed pair, corrections starting at offset s>=3 are jointly linear
through class c<=d+5. Their cross interaction has degree at least

    (p+s)+(q+s)=d+2s>d+5.

The corresponding same-factor bounds are 2(p+s)+q=d+p+2s>d+5
and p+2(q+s)=d+q+2s>d+5. These also exclude nonlinear Hall-power terms.
Retain all Hall coordinates of offsets s,...,c-d on both factors and
compute the exact commutator increment for each unit correction. Their
fixed lower coefficients contribute to the columns and are not discarded.
The residual and increments lie in gamma_(d+s), an abelian tail since
2(d+s)>c. One complete integer lattice membership calculation therefore
decides all remaining corrections simultaneously and constructs them.

The implementation uses the weight-guarded `n8_deep_tail.py` formulas.
Every claimed witness is checked by exact Magnus multiplication. The
independent GAP replay computes the columns from actual commutators in
a separately constructed free nilpotent group and solves their integral
membership problem in its polycyclic coordinates.

All leading branches, Nielsen residue lists, and quadratic root lists
are finite. Every linear or polynomial lattice calculation is exact and
terminates. Each normalization preserves the commutator, and every later
correction coordinate is retained. The union of the branches is thus
complete for the stated target stratum, proving the proposed theorem.

## Attribution and limits

The homogeneous free-basis theorem and the two-coefficient inner-solution
theorem are prior: Bryant--Kovacs--Stohr (2005), printed p147, and
Remeslennikov--Stohr (2007), with the accessible statement and proof in
Altassan (2013), Theorem 3.3, pp24--25. Their archived sources and the
previous cyclic-word argument are credited in `third-layer-proof.md`.
The general-offset argument, finite lifting and scope above remain
candidate mathematics awaiting independent specialist review. The frozen
N8 statement, complete HTML, and linked background were checked again
during this extension. No Kourovka argument was imported.

The proof does not extend automatically to arbitrarily deep layers.
Nonconsecutive exceptional kernels may coexist, and a later parameter
can enter an earlier obstruction through fixed higher coefficients.
Solving one quadratic at a time without controlling those interactions
would be an additional, unproved assertion. No complexity bound is given.
