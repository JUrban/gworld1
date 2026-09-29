# N8(b): exact substitutions and separated correction kernels

29 September 2026. Candidate extension of the existing partial result.
Specialist review and novelty assessment remain outstanding. The construction
of the exact substitutions is implemented and independently checked; the
complete branch algorithm below is proved but not implemented end to end.
See `universal-gauge-audit.md` for the precise computational scope.

**Candidate theorem.** In a free nilpotent group of any finite rank and
class, a normalized commutator branch is decidable whenever its exceptional
correction offsets before the Nielsen offset are separated: successive
nonzero offsets t,t' satisfy t'>=2t. In particular all branches with leading
weight gap at most five are decidable, and therefore all targets whose
first nonzero degree is at most seven are decidable in arbitrary class.
Together with the previous six-final-layer result, this gives all targets
in classes at most thirteen. Positive decisions construct factors.

This is still a partial answer to N8(b). No claim is made for unrestricted
overlapping exceptional offsets in arbitrary class. Part (a), concerning
general class-two groups, remains the separately credited negative prior
result. The free class-two case is also prior.

## 1. Setup and existing structural lemmas

Write N=F_r/gamma_(c+1), L for the full free rational graded Lie algebra,
and L_Z for its integral Hall lattice. Use [x,y]=x^-1 y^-1 x y. Fix nonzero
homogeneous C in (L_Z)_p and D in (L_Z)_q, p<=q, with [C,D]!=0. Put d=p+q
and n=c-d. The existing leading-pair enumeration gives finitely many
normalized integral choices C,D for a specified nonzero target leading
term. Every solution is represented after exact commutator-preserving
Nielsen moves. Signed scales and equal-weight oriented Hermite lattices
must all be retained; see `third-layer-proof.md` and its predecessors.

The correction at offset t has linear leading map

    A_t(U,V) = [U,D]+[C,V],
    U in L_(p+t), V in L_(q+t).                         (1)

Only t<=n can affect the commutator. The full ambient components in (1),
not only the subalgebra on C,D, are used to solve the correction equations.
The following lemmas were proved in `../../research/notes/N8-general-offset-lead.md`
and used in `fifth-sixth-layer-proof.md`:

1. For 0<t<q-p, ker A_t has dimension at most one. For a nonzero direction
   (U,V), [U,V] is nonzero modulo im A_(2t).
2. Such a nonzero pre-Nielsen kernel forces A_(t+1) to be injective.
3. At t=q-p>0 the kernel is precisely Q*(D,0).
4. For t>q-p, every kernel pair lies in Lie(C,D). If p=q this holds for
   every positive t.

The last assertion applies the prior two-coefficient inner-solution theorem
in Q*C+Q*D+L_(>=q+1), whose homogeneous free basis can include C,D. Both
correction components are in its tail. For equal weights use L_(>=p).
Thus it does not assume that C,D extend to a free basis of the ambient L
or of Q*C+L_(>p). A decomposable D in that latter algebra is allowed.

All these kernel tests are finite rational linear algebra. The underlying
free homogeneous basis and inner-solution theorems are credited prior
results, not new claims of this experiment.

## 2. A universal rational substitution fixing the group commutator

Let H be the free rational Lie algebra on formal a,b of positive weights
p,q, truncated above weight c. Its group realization uses finite BCH.
Set

    W = log(exp(-a) exp(-b) exp(a) exp(b)).              (2)

There is a filtered Lie automorphism sigma, with leading identity, such
that sigma([a,b])=W. Here is a finite construction. By Jacobi induction,
the derived Lie algebra is spanned by [a,H]+[H,b]. Consequently an error
in weight p+q+t can be written [U,b]+[a,V], where U,V have respective
weights p+t,q+t. Starting with images a,b, at each t>0 add U,V to the
current images to remove that homogeneous error. Their brackets with
previous higher corrections have larger weight and do not change earlier
equalities. Both W and the current bracket lie in the derived algebra,
so the required error is always in this span. The process ends at c.
The substitution has identity associated graded, hence an inverse by
finite successive correction.

This is the usual degree-by-degree symplectic-expansion construction in
a finite weighted form. Kuno's paper and its credit to Massuyeau are
recorded in the audit; no novelty is claimed for this ingredient. The
explicit recursion here uses our commutator convention.

Suppose U,V in H are homogeneous of weights p+t,q+t, t>0, and satisfy
[U,b]+[a,V]=0 in the full relevant homogeneous component. The derivation
delta defined by delta(a)=U, delta(b)=V raises weight by t and kills [a,b].
Its exponential is finite in H. Therefore

    alpha = sigma exp(delta) sigma^(-1)                (3)

is a rational filtered automorphism fixing W. Its first increments on
a,b are U,V at offset t, and it has no lower increments. Conjugation by
a map with leading identity does not change this first positive-degree
part. Equations (2)--(3) supply exact commutator preservation, including
all higher BCH terms.

## 3. Integral powers and universal evaluation

Use the group Gamma_(p,q,c) generated by A,B of weights p,q, obtained
from the free group by killing the Hall commutators of weighted degree
greater than c. Weighted Hall collection gives a unique ordered product
in the retained basic commutators with integral exponents. To see why
discarding coordinates is legitimate, commutators with a discarded term
have still larger weight, and collection does not reduce weight. Thus
the discarded tail is normal; the retained Hall coordinates are independent
over Z, and the quotient is torsion-free. Its rational Malcev Lie algebra
is exactly H, with a=log A and b=log B. This is classical Hall/Malcev
coordinate theory, not an additional freeness hypothesis on an ambient pair.

For the automorphism alpha in (3), alpha^k=sigma exp(k delta) sigma^(-1).
The images of a,b are rational polynomials in the integer k. Finite BCH
and triangular conversion to Hall group coordinates show that the
coordinates of exp(alpha^k(a)) and exp(alpha^k(b)) are rational polynomials
in k as well. Their constant terms, at k=0, are integral. Choose M>0
divisible by every denominator of every nonconstant coefficient. At both
k=M and k=-M, all coordinates are integral. Hence alpha^M and its inverse
send A,B into Gamma, and alpha^M is an actual group automorphism of Gamma.
It fixes [A,B] exactly. Searching factorial powers and testing both images
and inverse images terminates by this denominator argument. A fixed finite
search cap alone would not prove termination.

Now take any pair x in gamma_p(N), y in gamma_q(N). Every discarded
weighted commutator evaluates into gamma_(c+1)(N)=1. Thus evaluation
A->x,B->y is a homomorphism Gamma->N. The two words supplied by alpha^M
give a reversible substitution of the pair x,y which fixes its commutator
exactly. On a pair with leading C,D its first increments are

    M U(C,D), M V(C,D),                               (4)

at offset t. There is no assertion that this substitution extends to an
automorphism of N.

Noncommuting C,D freely generate their two-generator Lie subalgebra.
Indeed that subalgebra is free; its generating rank cannot be one, so
the two independent generators give a free basis (equivalently apply
the graded free-basis lemma). Therefore Lie(a,b)->Lie(C,D) is injective.
For every post-Nielsen integral kernel basis vector in (1), find its
rational homogeneous expressions in C,D by finite linear algebra. Their
preimages satisfy the kernel equation in H, not merely after an accidental
specialization. Applying (3)--(4) supplies an integer multiple of each
basis direction. These increments span a full-rank, finite-index sublattice
of the integral kernel.

At the Nielsen offset one may instead use x->y^k*x, which preserves
[x,y] with our convention. If D is nonprimitive, its period in the
primitive kernel direction is content(D); it need not be one.

Consequently, after solving a layer over Z, every solution is equivalent
under exact substitutions to one of finitely many kernel residues. Every
residue is retained. The substitution can alter higher corrections, which
remain free variables at subsequent stages. Reducing to just a rational
representative would not be complete.

## 4. Separated exceptional offsets

Call a nonzero kernel at 0<t<q-p exceptional. Suppose successive such
offsets satisfy t'>=2t. At layers with zero kernel solve the integral
linear equation uniquely, or reject. At Nielsen and later layers use
the finite residue procedure above. This settles every branch with no
exceptional kernel. We describe how to pass an exceptional offset while
retaining completeness.

All coordinates below the current exceptional offset t have already been
fixed. The integral solutions at t, if any, are v+kK, k in Z, where K is
a primitive integral generator of ker A_t. Write its components U,V.
If 2t>n, all still-variable corrections have offsets at least t, so their
pairwise interactions lie beyond c. Solve the entire remaining integer
linear system jointly and finish this branch. Do not fix an arbitrary
representative at one of those layers.

Assume 2t<=n. Keep k and every correction coordinate at offsets t+1
through 2t-1 as variables. All commutator equations through offset 2t-1
are jointly affine linear in these variables. Two variable corrections
cannot interact below offset 2t; nonlinear same-factor terms occur still
higher. The fixed earlier coordinates contribute to the linear columns.
Clearing rational denominators gives one exact integer linear system.
Its solution set S is empty or an affine integral lattice.

Every intermediate kernel at s with t<s<2t is either zero or one of the
exact universal kernels: separation excludes a new exceptional kernel
there. The exact substitutions act on this block as constant integral
translations. Their first offset is s>t; any dependence on a still-variable
correction first appears at offset s+t>2t. Thus their translations depend
only on the already fixed lower coordinates, not on k or other block
variables. They preserve k and S.

These translations span the rational kernel of the projection S->k.
For a difference vector with k=0, take its first nonzero offset s. The
homogeneous equation there is A_s=0. A rational combination of the
available exact translations removes that component and changes only
later components. Repeat to the end of the finite block. This proves
the spanning assertion. Their integral lattice T therefore has finite
index in the integral fiber kernel K_0.

The quotient is completely effective by Smith/Hermite operations. If
the image of S->k is a point, S/T is finite. Otherwise that image is
k_0+mZ with m!=0; choose an integral lift of its generator. For each of
the finitely many cosets K_0/T, all representatives take the form

    block = block_0 + z*J,   k=k_0+mz, z in Z.         (5)

The actual step m is retained. This yields a finite list of points or
integer affine lines, not a continuous or rational quotient. Exact
substitutions show that every full solution has a representative on one
of them, with all higher coordinates still available.

At offset 2t, the residual along a line (5) is at most quadratic in z.
Modulo im A_(2t), its quadratic coefficient is, up to the fixed sign
convention, m^2[U,V], which is nonzero by Section 1. Only the two
offset-t corrections can make a quadratic term at this degree. A variable
at a strictly higher offset interacts too late, and two corrections on
the same factor have the extra positive leading weight p or q.
Choose a rational cokernel functional nonzero on [U,V]. The resulting
nonzero quadratic polynomial has at most two integer roots, found exactly.
Retain every root satisfying the full integral A_(2t) equation, including
all congruence conditions. Points in (5) are checked by that same equation.

After this finite filtering, all block coordinates below 2t are fixed.
Restart the procedure at 2t. In particular, if a new exceptional kernel
occurs exactly at 2t, keep its full parameter and treat it as the next
exceptional stage. It was not part of the intermediate quotient and
cannot remove the preceding quadratic obstruction. This boundary case
is essential to the claimed separation condition with a weak inequality.

Every stage fixes more coordinates and retains a finite list. The number
of offsets is finite; the unbounded factorial search for each exact
substitution terminates by Section 3. All integer lattice operations and
quadratic root tests terminate. Exact normalization preserves solutions
in both directions, so this proves the candidate branch decision theorem.

## 5. Uniform consequences and limits

If q-p<=5, all pre-Nielsen offsets lie in {1,2,3,4}. By the absence of
consecutive exceptional kernels, any two present offsets are separated:
the only possible pairs are (1,3), (1,4), and (2,4). Thus the branch theorem
applies. Equal weights and gap one have no pre-Nielsen offsets at all.
For a target of leading degree d<=7 every normalized leading pair has
q-p=d-2p<=5, proving the arbitrary-class consequence.

For c<=13, a nonidentity target has either d<=7, handled above, or d>=8,
when c-d<=5. The latter lies in the existing six-final-layer scope.
Targets outside the derived subgroup are rejected immediately; the identity
and ranks zero/one are immediate. This accounts for all targets and all
finite ranks. No additional candidate entry is counted.

For larger gaps, exceptional offsets such as 3 and 5 can violate separation.
Then the later unresolved parameter can enter the earlier obstruction
linearly through fixed higher coordinates. The fiber reduction used above
does not apply to that additional exceptional kernel. No general decision
claim, complexity estimate, or all-class N8(b) solution follows here.

## Attribution

The homogeneous free-basis argument uses the classical Shirshov lemma, in
the form stated by Bryant--Kovacs--Stohr (2005), printed p147. The
inner-solution theorem is due to Remeslennikov--Stohr (2007), with the
accessible statement/proof in Altassan (2013), Theorem 3.3, pp24--25.
The symplectic-expansion ingredient is classical; see Kuno,
*A combinatorial construction of symplectic expansions*, arXiv:1009.2219v2,
Theorem 1.1 and the preceding credit to Massuyeau's Lemma 2.16. Our finite
weighted recursion, integral-power argument, and separated-offset assembly
are written explicitly above. These credits do not establish novelty of
the assembled decision result. No Kourovka argument was imported.
