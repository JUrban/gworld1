# N8: a general first-correction support lemma

29 September 2026, within the original run. A new structural argument,
not a new solved entry or an extension of the current group-decision scope.
Independent specialist review and novelty assessment are outstanding.

## 1. Free differential Lie algebra

Let A be the alphabet consisting of letters s_j, where s ranges over a set
of seeds and j>=0. Work over Q, and let delta be the derivation of the free
Lie algebra Lie(A) defined by delta(s_j)=s_(j+1). The same derivation acts
on the free associative algebra Q<A>. Choose one seed t and put T=t_0.

**Support lemma.** If D,V are Lie polynomials and

    [T,D] = delta V,                                         (1)

then D and V belong to the free Lie algebra on the single chain
T,delta T,delta^2 T,... .

Here is a coefficient proof that does not depend on a degree bound.
For each fixed ordered sequence of seed names (s1,...,sm), encode the
coefficients of a noncommutative polynomial P on words

    (s1)_j1 ... (sm)_jm

by the ordinary polynomial

    P_(s1,...,sm)(x1,...,xm)
       = sum coefficient((s1)_j1 ... (sm)_jm) x1^j1 ... xm^jm.

There is a distinct commuting variable for every **position**, not every
seed. No order of the noncommuting letters is forgotten. On each such
component, delta acts by multiplication by x1+...+xm. In particular delta
is injective on all polynomials with zero constant term.

Suppose the first seed s1 in a component of D is not t. Look at the
seed sequence (s1,...,sm,t) in (1). The product TD contributes nothing,
and -DT contributes exactly

    -D_(s1,...,sm)(x1,...,xm),

independent of x_(m+1). Since the right side is divisible by
x1+...+x_(m+1), substituting x_(m+1)=-(x1+...+xm) proves that this entire
component of D is zero. Similarly, looking at (t,s1,...,sm) shows that
all components ending with a seed other than t vanish.

It remains to use the Lie condition: a nonzero Lie polynomial involving
an outside-chain letter cannot have every associative word start in the
t-chain. Split it by the multiplicity of each individual alphabet letter.
Every component is still a Lie polynomial. In a component involving an
outside letter, order all occurring outside letters before the t-chain
letters. The least associative word of a nonzero component is a Lyndon
word, by the standard triangular Lyndon basis. It starts with the least
letter occurring in its fixed multidegree, hence with an outside letter.
This contradicts the preceding coefficient vanishing. Thus D uses only
t-chain letters. Since delta preserves every seed sequence and is injective,
(1) then forces the same support restriction on V. This proves the lemma.

The standard facts about Lyndon bases used in this step are prior:
Lalonde–Ram, *Standard Lyndon Bases of Lie Algebras and Enveloping Algebras*,
Trans. AMS347 (1995),1821–1830, equations(1.2)–(1.3), printedp1822,
https://math.soimeme.org/~arunram/Publications/1995TAMSv347n5p1821.pdf.
The paper credits Reutenauer/Lothaire for these facts. The first two printed
pages were read as text and page1822 was actually viewed. The full paper
was archived but its later sections were not audited. The support lemma
above is our present derivation from those standard facts; no novelty is
asserted for it.

## 2. Consequence for the actual free Lie correction map

Let L be the rational free Lie algebra on a finite-dimensional degree-one
space, let z be nonzero in L1, and let delta=ad_z. Use the homogeneous
free delta-chain alphabet of L' constructed in Section1 of
`problems/N8/class9-proof.md`. Its degree-two seed space is all of L2.
That construction and its imported metabelian-module/Shirshov ingredients
remain dependencies; the present note does not replace them.

For every nonzero homogeneous D in Lq, q>=2, define

    A_D: L2 + L_(q+1) -> L_(q+2),
         (U,V) |-> [U,D]+delta V.                            (2)

**Corollary.** The rational kernel of A_D has dimension at most one.
If it contains a nonzero pair (U,V), then U!=0 and D belongs to the
free Lie algebra on U,delta U,delta^2 U,... .

Indeed U=0 implies V=0 by injectivity of delta. For nonzero U, change
the basis of the degree-two seed space so that U is one seed, shifting
all its descendants by delta. Equation(2) and the support lemma, applied
to -V, give the claim about D. If two kernel pairs had independent first
coordinates U1,U2, choose them simultaneously as two seed basis vectors.
Then D would lie in the intersection of the Lie algebras on two disjoint
chain alphabets. That intersection is zero in the ambient free associative
algebra, contrary to D!=0. Projection of the kernel to U is injective,
so this proves the dimension bound.

For q=2 the kernel is exactly Q*(D,0), the familiar Nielsen direction.
For q>2 a nonzero kernel has V!=0: a free generator U commutes only with
its scalar multiples, and D has different homogeneous weight. The condition
that D uses one chain is necessary, not sufficient. For example D=delta U
has no nonzero first correction kernel: [U,delta U] is not a delta-image
in the relevant homogeneous Lie component.

This removes a potential multi-parameter problem at the **first** correction
for leading type(1,q), in arbitrary q and finite rank. It says nothing about
later correction kernels, other leading types, integrality of particular
solutions, or termination of the whole commutator decision problem.

## 3. The remaining obstruction question

For a nonzero exceptional direction use the sign convention

    delta V=[U,D].

In a third-from-last-layer lifting problem the quadratic term is, up to a
nonzero scale/sign, Q=[U,V]. The relevant final correction space is

    [L3,D] + delta L_(q+2) inside L_(q+3).                   (3)

The support lemma alone does not show that Q is outside (3).
A useful sufficient statement would be:

    delta V=[U,D], delta W=[U,V]
    in the one-chain free Lie algebra implies D is a scalar U.   (4)

No degree-uniform proof of (4) has been obtained here. It must not be
silently assumed. It is stronger than the support lemma.

To see why (4) would help, decompose D by bracket length in the delta-chain
alphabet and choose its nonzero component D_m of greatest length. V has
corresponding component V_(m+1). If q>2, the free-generator centralizer and
injectivity of delta ensure V_(m+1)!=0. Then [U,V_(m+1)] has length m+2.
Project all other seed chains to zero. L3 projects into Q*delta U, so
[L3,D] has length at most m+1. Consequently cancellation in (3) at length
m+2 would give a double primitive in (4). This reduction is a possible
route to a uniform quadratic obstruction, not yet a proof of it.

Even such an obstruction would not automatically cover every N8 input:
all normalized leading pairs and the other leading types still require
complete treatment, as do subsequent layers in the general problem.

## 4. Exact bounded checks and their limits

Two deterministic structural scripts use weighted Lyndon bases inside the
free associative algebra, with every seed of weight2 and delta raising weight
by1. Standard bracketing uses the longest proper Lyndon suffix. All possible
words at each tested weight are enumerated, so these are finite-dimensional
linear calculations, not random samples.

`probe_n8_common_first_kernel.py` checks two independent seed chains for
q=2,...,10. The simultaneous equations

    [T,D]=delta V,  [S,D]=delta W

have zero kernel at all nine weights. For one fixed direction T the
dimensions of allowable (D,V) are respectively

    1,0,1,0,1,1,2,1,4.

These latter dimensions vary D; they must not be confused with the
at-most-one kernel dimension for a **fixed nonzero D** in Section2.
They include nonzero-kernel controls and show why universal injectivity
of the first map would be false. The actual general corollary rests on
the coefficient proof, not these nine dimensions.

`probe_n8_double_primitive.py` checks all D,V,W in the one-chain weighted
components for q=2,...,14. The double-primitive dimensions are1 at q=2
(the scalar-U case) and0 at q=3,...,14. These are finite evidence for (4),
not an all-degree theorem. Its auxiliary sign conventions are equivalent
by negating V; the existence dimensions are unaffected.

`scripts/check_n8_differential_kernels_gap.g` independently enumerates the
weighted Lyndon words, brackets in GAP's native free associative algebra,
differentiates each bracket by the Leibniz rule, and computes rational
span dimensions. It confirms all nine common-direction systems, their
single-direction controls, and all thirteen double-primitive systems.
It does not import Python's matrices or word lists. Two additional free
letters distinguish the direct-sum equation components.

All three jobs completed with exit0, expected marker and empty stderr;
runtimes were0.821,0.369 and3.430seconds. Each used one core and a6GB
per-process bound. The exact executed versions, JSON records, and process
logs are retained in `research/certificates/N8-common-first-kernel/`,
`research/certificates/N8-double-primitive/`, and
`results/n8-{common-first-kernel,double-primitive,differential-kernels-gap}-v1/`.
These checks concern rational Lie equations only. They are not group-level
commutator decisions or an outside mathematical review.

## 5. Scope and next action

The full frozen N8 HTML was reread and the actual original paragraph image
viewed. N8(b) asks about every finitely generated free nilpotent group, with
no class bound. The group-decision candidate retains its existing scope:
all targets through class10 plus the previously stated arbitrary-class
special families. No new group scope or problem count is added here.

A worthwhile next step is to prove or disprove (4), using the explicit
one-chain polynomial formulation, rather than accumulating larger instances.
A counterexample would identify the missing higher-order branch; a proof
would give a uniform quadratic obstruction for first exceptional corrections.
The existing all-rank delta-alphabet construction should be reviewed alongside
any such use. No new Kourovka mathematics/code is imported.
