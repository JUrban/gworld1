# General correction offsets and a possible next extension

29 September2026, approximately05:47--05:55UTC. **Written structural lead;
bounded independent tests completed, but not promoted to group-decision scope.**
The fourth-layer scope and audit are recorded separately. This note saves
a further argument rather than silently treating it as implemented.

Write A_t(U,V)=[U,D]+[C,V], with fixed nonzero homogeneous C in Lp,
D in Lq, p<=q, and U in L_(p+t), V in L_(q+t), t>=1.

## 1. Before the Nielsen offset

Suppose t<q-p. For nonzero U use the graded Lie subalgebra

    A=Q*C+Q*U+direct_sum_(j>=p+t+1) L_j.

It is closed because [C,U] has degree2p+t>=p+t+1. Its homogeneous
abelianization contains C,U independently, so a homogeneous free basis
can include both. Since q>=p+t+1, D,V belong to A. The prior inner-solution
theorem gives D,V in Lie(C,U). Using two independent U directions in the
same construction bounds dim ker A_t by1, as in the offset-one proof.

For a nonzero direction choose [C,V]=[U,D]. Project the homogeneous free
basis of A onto C,U. The image of L_(p+2t) contains at most one U letter:
two U letters already have weight2(p+t)>p+2t. Its pure-C part is zero
because a Lie algebra on one letter has no higher bracket. Hence it is
zero or a scalar multiple of ad_C^k(U), where kp=t.

Take the nonzero component D_m with the most U letters. The corresponding
V component has m+1 U letters. If

    [U,V] were in [L_(p+2t),D]+[C,L_(q+2t)],

the component with m+2 U letters after projection would give two successive
primitives in the free Lie algebra on C,U. The existing cyclic-word lemma
forces D_m=0, a contradiction, because q>p+t excludes length-one D.
Thus the nonzero quadratic obstruction holds at offset2t for every
pre-Nielsen exceptional direction, with no restriction t<p.

## 2. The Nielsen offset and subsequent kernels

At t=q-p>0, the kernel is exactly Q*(D,0). Use
A=Q*C+direct_sum_(j>=q) L_j: C and every basis element of Lq are free
basis elements. Killing C in the kernel equation gives [U,D]=0, hence
U is proportional to D; V=0 follows from the centralizer theorem.
The primitive integral period is content(D), as before.

For t>q-p, use A=Q*C+Q*D+direct_sum_(j>=q+1) L_j. It is closed and
C,D are free basis elements. Both U,V now belong to its high tail, so
the inner-solution theorem puts them in Lie(C,D). For p=q, use L_(>=p)
and reach the same conclusion for every t>=1. This describes the kernel
inside a two-generator weighted free Lie algebra; it does not assert its
dimension is at most one at all such later offsets.

## 3. Consecutive exceptional offsets cannot both occur

Suppose t<q-p and A_t has a nonzero kernel with direction U. The claim
is that A_(t+1) is injective. Work in A from Section1, with C,U included
in its homogeneous free basis; D belongs to Lie(C,U).

Let U' in L_(p+t+1) occur in a kernel at the next offset. For p>=2,
this component of A contains only free basis letters: [C,U] has larger
weight, and pure-C brackets vanish. Thus U', if nonzero, can be selected
as another free basis element. The inner-solution theorem would also
put D in Lie(C,U'), whose intersection with Lie(C,U) is Q*C. This is
impossible for q>p. This argument also covers the boundary q=p+t+1.

For p=1, write U'=lambda[C,U]+B, where B lies in the degree-(t+2)
free basis-letter space of A. If B!=0, select B as a free generator and
replace it by B+lambda[C,U]. This triangular free-Lie change of basis
again makes C,U,U' free basis elements, giving the same contradiction.
If B=0, any nonzero U' is proportional to [C,U]. The next equation then
says both [U,D] and [[C,U],D] lie in the image of ad_C.

These simultaneous divisibilities are impossible for nonzero D in the
ideal on U inside Lie(C,U). To prove this, use the free chain alphabet
U_j=ad_C^j(U), whose elimination construction was already credited.
For each chain-letter length m>=1 encode D by its coefficient polynomial
P(x1,...,xm), one commuting variable for each position. The derivation
ad_C acts by multiplication by S=x1+...+x_(m+1) on length m+1.
The two divisibilities say S divides both

    P(x2,...,x_(m+1))-P(x1,...,xm),
    x1*P(x2,...,x_(m+1))-x_(m+1)*P(x1,...,xm).

Eliminating the first expression shows that modulo S,

    (x1-x_(m+1))*P(x1,...,xm)=0.

After substituting x_(m+1)=-(x1+...+xm), the factor is the nonzero
polynomial2x1+x2+...+xm over Q. The polynomial ring is a domain, so
P=0. Every chain-length component vanishes, a contradiction.
The auxiliary primitives also belong to Lie(C,U): any component in the
complementary free-generator ideal commuting with C is zero by the
centralizer theorem. Their pure-C components have the wrong weight.
This justifies applying the chain encoding, rather than assuming it.

Thus the next correction map is injective whenever the preceding
pre-Nielsen map has a nonzero kernel. Section5 records fresh bounded
independent tests; neither the tests nor this lemma alone promote scope.

## 4. Suggested fifth/sixth-layer algorithm, not yet implemented

For leading degree d=c-4 or c-5, first use the offset-one quadratic
obstruction at degree d+2 to retain finitely many first parameters, or
normalize its exact Nielsen direction. Do not choose one second-layer
representative when passing to the next stage.

For each first-corrected pair solve A_2. For d>=4 its kernel appears to
have only these cases, all requiring a written scope audit:

- q>p+2: dimension<=1 with nonzero obstruction at offset4;
- q=p+2: the exact Nielsen line;
- q<=p+1: zero, by Section2 and the small weight possibilities in
  Lie(C,D). The boundary(2,2) requires the independence of the two
  degree-three brackets [[C,D],D] and [C,[C,D]].

For an exceptional offset-two line k, the degree d+3 residual is affine
in k. Section3 makes A_3 injective. Solving this layer jointly with k
therefore yields an empty set, one point, or an integral affine line
with k=k0+mt and m!=0. On that line the degree d+4 residual is quadratic
in t, with nonzero quadratic coefficient modulo A_4 by Section1;
offset-three corrections depend only affinely and cannot create a new
quadratic term through offset4. Thus only finitely many t remain, all
checked against the complete integral lattice.

Once the offset-two parameter is fixed, corrections from offset3 onward
are jointly linear through offset5 because 3+3>5. This suggests a finite
complete algorithm for both fifth- and sixth-from-last targets. Exact
integrality, complete affine lines, multiple roots, signed leading scales,
Nielsen periods, and the new converse/scope claims must be audited and
independently replayed before promoting anything. No assertion here
extends the currently implemented fourth-layer scope.

For deeper layers, nonconsecutive exceptional kernels may coexist. Do
not assume one quadratic at a time settles arbitrary many layers: a later
free parameter can enter an earlier obstruction linearly through fixed
higher coefficients. That remains a separate unresolved issue.

## 5. Independent bounded checks and subsequent proof audit

`check_n8_general_offsets.py` computes complete weighted Lyndon bases in
the free associative algebra over Q. `check_n8_general_offsets_gap.g`
independently enumerates and brackets these bases in GAP's native free
associative algebra. It imports expressions, dimensions and expected
answers, not Python matrices. Both recorded jobs passed with empty stderr
in1.374 and5.137seconds, respectively.

Six cases check a correction kernel and its successor. Five exceptional
cases check a nonzero quadratic obstruction as well: offsets2,2,2,3 with
(p,weight(U))=(1,3),(2,4),(3,5),(1,4), and a nonlinear D case at offset2.
The latter uses D=2[U,ad_C^3 U]+3[ad_C U,ad_C^2 U], with U of weight3;
the explicit primitive is 2[U,[U,ad_C^2 U]]-[ad_C U,[U,ad_C U]].
Two of the offset-two cases and the offset-three case use decomposable U.
Every exceptional kernel has dimension1, every successor has dimension0,
and adjoining the proposed quadratic vector increases the final rank by1.

The sixth control has p=q=1 and t=4. Its kernel has dimension3. This is
outside the pre-Nielsen hypotheses and deliberately rules out the false
extension that all correction kernels have dimension at most one.
These finite controls are not a proof of the uniform statements.
Certificates and exact sources are retained in
`research/certificates/N8-general-offsets/`; the process records are
`results/n8-general-offsets-v1/` and `results/n8-general-offsets-gap-v1/`.

The subsequent written audit checks the small-weight assertion in
Section4. When q=p and d>=4, p>=2. For p>=3 the weight p+2 component of
Lie(C,D) is zero. For p=2 it is Q[C,D], but the two resulting columns
[[C,D],D] and [C,[C,D]] are independent. When q=p+1 and d>=4, p>=2;
the only nonzero possibility is p=2, V proportional to [C,D], whose
image [C,[C,D]] is nonzero. Thus A_2 is indeed injective in these cases.

For the coupled third layer, injectivity of A_3 means its integral
solution set together with k projects injectively to the k coordinate.
It is therefore empty, a point or a primitive integral affine line;
the nonzero k step may have absolute value greater than1 and must never
be replaced by1. On this line the offset-four quadratic coefficient is
the nonzero obstruction from Section1 multiplied by the square of that
step. Fixed first corrections and varying third corrections contribute
only linearly at this degree. These observations sharpen the proposed
algorithm, but its group implementation and independent replay remain
outstanding. No fifth/sixth-layer decision scope is counted here.


## Completed group extension, 2026-09-29T07:03:56.815798+00:00

The proposed fifth/sixth-layer scheme above is now implemented and independently
replayed. The complete candidate proof and its exact scope are in
`problems/N8/fifth-sixth-layer-proof.md`; the audit records all successful
and failed runs. This supersedes the earlier implementation-pending status,
without extending the claim to arbitrary deeper layers.
