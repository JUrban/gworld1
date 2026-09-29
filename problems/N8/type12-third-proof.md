# Third-from-last targets with leading types one or two

Candidate extension,29 September2026. This extends the same partial N8(b)
entry and the [type-one theorem](type1-third-proof.md). Independent specialist
review and novelty assessment remain outstanding. See the separate
[type-one/two audit](type12-third-audit.md) for executed checks.

**Proposed theorem.** Let N=F_r/gamma_(c+1)(F_r), with finite rank r and
c>=8, and let g have nonzero leading term W in L_(c-2). If every normalized
integral leading pair [C,D]=W, with weights p<=q, has p<=2, there is a
terminating algorithm deciding whether g=[x,y] in N, constructing x,y
when the answer is affirmative. The hypothesis is decidable. An empty
leading-pair list gives a negative answer. All integral leading types
p>=3 cause the implementation to return unsupported.

The complete finite list uses the previous block-quadratic/exterior-square
algorithm, every signed scale and the equal-weight Hermite sublattices.
Its normalization and completeness proof is in `penultimate-target-proof.md`;
the independent projective-fibre alternative is in `projective-factor-audit.md`.
No new finite-factorization claim is hidden in this theorem.

Type(1,q) branches are covered by `type1-third-proof.md`. It remains to
prove the type(2,q) lifting claim, for q=c-4>3. Work over Q for kernel
arguments and over the integral Hall lattice for every group decision.
The convention is [x,y]=x^-1 y^-1 x y, and delta=ad_C.

## 1. Eliminate a weight-two free generator

The graded Lie algebra L' is free on a homogeneous alphabet whose
weight-two letters form a basis of L2. A rational basis change selects
the nonzero C as one of these letters. Let J be the ideal of L' generated
by the other letters. Lazard elimination gives a free basis for J:

    delta^j s, j>=0, s any other alphabet letter.       (1)

This is the ordinary elimination theorem, with one eliminated generator,
not an assertion about arbitrary derivations. An accessible precise
statement is Altassan2013, Theorem2.1, p.19, crediting Bourbaki II.2,
Proposition10. It applies equally to the countable alphabet of L'.
The quotient L'/J is the one-dimensional Lie algebra on C, concentrated
in weight two. Therefore all the spaces used below lie in J.

Delta raises original weight by two. Every element of L3 is a linear
combination of the weight-three **seed** letters of (1): products and
positive delta-shifts have weight at least four. Consequently any nonzero
U in L3 can be chosen as a seed by a rational change of basis among those
letters.

## 2. First-kernel dimension and final obstruction

The first correction is

    A_D: L3 + L_(q+1) -> L_(q+3),
         (U,V) |-> [U,D]+delta V.                     (2)

If (U,-V) is a nonzero kernel direction, U!=0 by injectivity of delta
on J. The free-chain support lemma forces D,V into the U-chain. This
lemma follows from the prior Remeslennikov--Stöhr2007 inner-solution theorem;
the precise embedding and an alternative coefficient proof are recorded in
`research/notes/N8-general-first-kernel.md`, Sections1 and7.

Two independent U directions could be chosen simultaneously as seeds in
(1); their chain subalgebras have zero intersection. D!=0 excludes this.
The primitive V is unique for U. Hence the rational kernel of(2) has
dimension at most one.

For a nonzero such direction, we claim

    [U,V] not in [L4,D]+delta L_(q+2).                (3)

Project J onto the U-chain, killing the other chains. This commutes with
delta. It annihilates L4: its possible single-letter weights are3,5,7,...,
and its words of length at least two have weight at least six. A relation
contrary to(3) would therefore yield two successive primitives inside the
U-chain:

    delta V=[U,D],   delta W=[U,V].                   (4)

Embed this chain in the free Lie algebra on z,t by delta^j U -> ad_z^j(t),
with weights z=2,t=3. The embedding is injective by Lazard elimination,
or by the uniquely decipherable least words t*z^j. Equations(4) contradict
the cyclic-word double-primitive lemma in `type1-third-proof.md`, Section3:
all ordinary length>=2 components of D,V,W would vanish. A nonzero D of
weight q>3 cannot have a length-one component. This proves(3).

The q=3 exception is deliberate: D can be proportional to U and V=0,
which is an exact Nielsen direction. It occurs below our c>=8 range and
is already treated in the earlier low-class arguments. We do not infer
(3) in that case.

## 3. Complete integral lifting

Fix a listed integral leading pair and choose Hall group lifts x0,y0.
Solve the first integer affine system associated to(2). Inconsistency
rejects this branch. A zero kernel gives a unique integral choice, followed
by a final integer system with image [L4,D]+[C,L_(q+2)].

Otherwise retain the **full** primitive integral solution line v+nK,
n in Z. The first corrections have weights3 and q+1; the final corrections
have weights4 and q+2. The residual in the top central layer, of weight
c=q+4, is an integer-valued polynomial of degree at most two in n.
Its only quadratic interaction has weights3+(q+1)=c. Two first-factor
corrections interacting with D have weight q+6>c. Conjugation by a first
correction has weight at least q+5>c. Fixed higher coordinates of the
leading lifts affect only the constant and linear terms. Powers of an
individual Hall generator do not create another quadratic term in these
weights.

The quadratic coefficient modulo the final rational image is, up to a
nonzero scalar/sign, [U,V], nonzero by(3). Thus one rational cokernel
coordinate gives a nonzero quadratic equation in n. It has at most two
integer roots, all effectively enumerable. For each root test the full
integral final correction lattice, retaining every denominator/congruence
condition. A passed test constructs factors, whose equality is verified
in N. Every other higher factor coordinate has weight too large to matter.

Each branch therefore terminates. The leading-pair list is finite and
complete; combining both leading types gives the stated algorithm.
The implementation is `scripts/n8_type12_third.py`. It returns unsupported
for other types or layers, not a negative answer. There is no claim here
for all targets of arbitrary class, no efficiency theorem, and no novelty
claim for the imported free-Lie support/elimination results.
