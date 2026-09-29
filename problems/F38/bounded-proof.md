# F38(c): bounded translation equivalence from conjugacy stabilizers

29 September 2026. Candidate complete answer to part (c), subject to
specialist review. The proof imports Sela's graded shortening theorem,
Whitehead peak reduction, and Handel--Mosher aperiodicity. None of these
deep results is proved by the computational checks. Novelty is unverified.
The earlier necessary-condition and exponential-envelope notes retain
their historical, deliberately weaker conclusions.

## Statement

Fix a basis of the finite-rank free group F_r. Write ||w|| for cyclic
length, and H_w for the stabilizer of the **oriented** conjugacy class
[w] in Out(F_r). For nonidentity u,v the following are equivalent:

1. There is a constant C such that ||alpha(v)|| <= C ||alpha(u)|| for
   every alpha in Aut(F_r).
2. H_u has a finite orbit on [v].

Consequently u,v are boundedly translation equivalent, in exactly the
ambient-automorphism sense of the frozen F38(c), if and only if H_u and
H_v are commensurable. This condition is decidable uniformly in finite
rank. Rank one is immediate. Identity inputs have undefined ratios and
are excluded; alternatively the two-sided inequalities extend naturally
to give true for two identities and false for exactly one identity.

This is not a replacement of the problem's quantifier by all injections
or all tree actions. In rank two Lee's pair a, a^2 b a^-1 b^-1 is bounded
under automorphisms and unbounded under injections. The precise restricted
injection lemma needed below has an additional free-factor hypothesis.

Necessity is elementary: restrict alpha to H_u. Bounded cyclic length
leaves only finitely many conjugacy classes. The work is sufficiency.

## A quantitative relative-shortening lemma

Let A=F(a_1,...,a_k), k>=2, and let u!=1 lie in no proper free factor of
A. Fix a target free group F_r, r>=2, with its basis. There exists a
constant K=K(u,k,r) such that for every injection f:A -> F_r, one can
choose c in F_r and theta in Aut(A), theta(u)=u, satisfying

    max_i |c f(theta(a_i)) c^-1| <= K ||f(u)||.             (1)

Here |.| is ordinary reduced length. The constant is existential; the
decision algorithm below does not need its value.

We give the reduction to the exact graded shortening theorem, including
the issues of relative free indecomposability, shortness and the kernel
of the limiting action.

Adjoin a generator z and put G=A*<z>, P=<u,z>. The subgroup P is free of
rank two. The intersection of two free factors of a free group is a free
factor of each, by the Kurosh subgroup theorem. Hence G has no nontrivial
free-product decomposition with P in one factor: a free factor B
containing P has A intersect B containing u, so A intersect B=A, whence
B contains both A and z and equals G. Conjugating a proposed factor does
not change this argument.

Every automorphism of G fixing P pointwise preserves A. Indeed A and
its image A' are free factors of equal rank; their intersection contains
u and is a free factor of A, so A is contained in A'. It is also a free
factor of A'; equality of ranks gives A=A'. Thus

    Aut(G/P) = {extensions of theta in Aut(A/u) fixing z}. (2)

Conjugate f in F_r so f(u) is cyclically reduced, then minimize

    M(f) = max_i |f(theta(a_i))|

over theta in Aut(A/u). An integer minimum exists; no claim of efficient
minimization is needed. Replace f by such a minimizing map. Extend it
to h:G -> F_r*<z> by h(z)=z. This extension is injective. It is shortest
under Aut(G/P), for the basis (a_1,...,a_k,z), and therefore under the
graded modular subgroup, which fixes P pointwise. Including u among
the generating set does not affect shortness when M(f)>|f(u)|.

Suppose (1) fails. Choose these minimizing maps f_m so that

    M_m > 2^m (1+||f_m(u)||), m>=1.                       (3)

The based images of the two parameters u,z then have lengths o(M_m).
With P as parameter subgroup and no coefficients, G is rigid or solid
in the terminology of Sela, Definition 10.2. To check the latter point,
if its graded JSJ is nontrivial, minimize any one embedding G -> F_r*<z>
in its graded modular orbit. Its constant sequence is a graded
shortening sequence with quotient isomorphic to G. That quotient
dominates every quotient of G, so is the unique maximal one up to the
stated equivalence. Constant sequences are allowed: this is used
explicitly in Sela's Proposition 5.6 proof, and in the free-group
example immediately before Definition 10.2. If the graded JSJ is
trivial, G is rigid by definition.

Each h_m also satisfies the no-free-product-factorization condition in
Definition 10.3(ii): a factorization through an epimorphism of G onto
a nontrivial free product, with P in one factor, would have injective
first map because h_m is injective. It would therefore give the relative
free splitting already excluded above. As usual for quotient
factorizations, unused extra free factors in a larger target are not
such a factorization. Since the source ball of radius m contains its
basis, (3) implies the precise 2^m ball inequality in that definition.
Thus (h_m) is a flexible graded sequence.

For completeness, its limiting tree quotient is G itself; this is not
an unexamined identification of a stable kernel with an action kernel.
Rescale the target trees by M_m and use the identity as basepoint.
Pass to a convergent subsequence, as in Sela, Section 1. Here is an
explicit nontriviality and faithfulness check.

Let n=|u| in the fixed source basis, D_m(x) the maximum displacement of
x by h_m(a_i),h_m(z), and t=d(x,1) in the unscaled target. The axes of
h_m(u) and z intersect precisely at 1: the first lies in the F_r
subtree, is cyclically reduced, and the second uses only z edges.
At least one of their axes is distance t from x. The displacement
formula for a hyperbolic tree isometry consequently gives

    n D_m(x) >= 2t,       D_m(x) >= M_m-2t,
    hence D_m(x) >= M_m/(n+1).                            (4)

This uniform bound prevents a global fixed point in the limiting action.
After a subsequence, choose a fixed i with |f_m(a_i)|=M_m. The three
orbit points

    f_m(a_i),       z f_m(a_i),       z^-1 f_m(a_i)

have pairwise distances 2M_m+1, 2M_m+1, and 2M_m+2, respectively.
They yield a nondegenerate tripod in the limit. An element in the
action kernel fixes this tripod. The elementary tripod argument in
Sela, Lemma 1.3(iii), says its images are eventually trivial. All h_m
are injective, so the element was the identity. Thus the action kernel
is trivial and its quotient is G.

Sela, Lemma 10.4(ii), says that a flexible graded quotient of a rigid
or solid graded limit group is proper. This contradicts the preceding
paragraph and proves (1). This use of the deep graded shortening
result is the main imported structural step of the candidate proof.
The ordinary bounded-parameter relative shortening statement by itself
would not justify (3); the graded theorem is essential here.

## Finite orbits give linear comparison in a free-factor-filling source

Continue with u lying in no proper free factor of A. Suppose its
conjugacy stabilizer has finite orbit on [v] in A. The group Aut(A/u)
has the same action on conjugacy classes as that outer stabilizer:
adjust a representative fixing [u] by an inner automorphism to fix u.
Take shortest representatives v_1,...,v_s of its finite orbit and put
B=max_j |v_j|.

For any injection f:A -> F_r, choose theta,c from (1), and define
psi(x)=c f(theta(x)) c^-1.
The class of theta^-1(v) has a representative v_j. Consequently

    ||f(v)|| = ||psi(theta^-1(v))||
              <= B max_i |psi(a_i)| <= BK ||f(u)||.       (5)

All constants depend on the fixed inputs and ranks, not on f.

## Proper free factors in ambient rank at least three

Choose a free factor A of smallest rank containing a representative of
u, and choose an ambient basis extending a basis of A. Then u lies in
no proper free factor of A. Simultaneous automorphic normalization of
u,v does not change either condition of the theorem.

Suppose first rank(A)>=2. For a complementary basis letter b and two
different basis letters a_1,a_2 of A, the Nielsen maps

    b -> b a_1,       b -> b a_2

fix u. If H_u[v] is finite, both iterated length sequences of v are
bounded. The exact Nielsen formula in `primitive-power-proof.md` says
zero growth under b -> b a_j forces every positive b to be followed
by b^-1 across a pure a_j run, and every negative b to have such a
predecessor. A cyclically reduced word containing b cannot satisfy
both requirements: the intervening word would have to be both a pure
a_1 run and a pure a_2 run, hence empty, giving adjacent inverse
letters. Thus v has no b letters. Apply this to every complementary
letter: v is conjugate into A.

The finite ambient orbit then restricts to a finite Aut(A/u) orbit.
Conjugacy of nonidentity elements of a free factor in the ambient group
is the same as conjugacy in that factor, by free-product normal forms.
Each ambient alpha restricts to an injection A -> F_r; (5) proves the
required bound. If A is all of F_r, (5) applies directly.

If rank(A)=1 and r>=3, the elementary primitive-power theorem already
proved in `primitive-power-proof.md` applies. Its finite family of
Nielsen maps fixes u=a^p and has common bounded conjugacy classes
exactly the powers of a. Finiteness of H_u[v] therefore forces v
conjugate to a^q. Their length ratio is exactly |q/p|.

## The rank-two primitive case

The only remaining case is F_2=<a,b>, u=a^p, p!=0. Bounded iterates
under b -> ba imply that v is conjugate into

    K=<a, b a b^-1>.

This is the exact two-vertex zero-growth graph proved in the same
Nielsen note. Fix an expression v=w(a,bab^-1) of length L in these
two generators and their inverses.

For alpha in Aut(F_2), put A=alpha(a), B=alpha(b), C=BAB^-1 and
ell=||A||=||C||>=1. The classical rank-two Nielsen identity says that
alpha preserves the conjugacy class of [a,b] or its inverse. Thus

    ||A C^-1|| = ||A B A^-1 B^-1|| = 4.

If the axes of A and C are disjoint with distance d, the tree product
formula gives 4=2ell+2d, so d<=1. If they meet, put d=0. Choose a
vertex on the axis of A nearest to the axis of C (or in their
intersection). At this basepoint, the displacements of A,C are ell
and ell+2d, both at most ell+2. Therefore

    ||alpha(v)|| <= L(ell+2) <= 3L ell
                 = (3L/|p|) ||alpha(u)||.

This argument uses the fact that alpha is an ambient rank-two
automorphism. It is deliberately not asserted for arbitrary injections.
Together with the preceding cases it proves the one-sided theorem.

## A terminating decision procedure

For r>=2 compute generators of H_u and H_v by Whitehead minimization
and the finite graph of all length-preserving Whitehead moves on
minimum representatives. Retain every loop label and parallel edge;
peak reduction gives the full stabilizer. This is the classical
Whitehead/McCool construction, not a new algorithmic ingredient.

Put I=ker(Out(F_r) -> GL(r,F_3)). Handel--Mosher's aperiodicity theorem
says that an element of I with a periodic conjugacy class fixes that
class. For any finitely generated H<=Out(F_r), H[w] is finite if and
only if H intersect I fixes [w]. This condition has a finite test:
explore the finite mod-three matrix image of H, retaining an actual
automorphism representative and its image of [w] at each matrix.
If two paths to the same matrix give different classes, their quotient
is in H intersect I and moves [w], certifying an infinite orbit.
Otherwise the finite graph closes consistently and its stored classes
form an H-invariant finite set. No word-length search cutoff is used.

Apply this test to H_u[v] and H_v[u]. Return YES precisely when both
are finite. Equivalently H_u intersect H_v has finite index in each,
which is the advertised commensurability condition. A NO answer has
an explicit automorphism fixing one input class and moving the other
aperiodically, whose iterates have unbounded cyclic length.

The software uses this finite procedure. It does not compute a JSJ
decomposition or the constant in (1). The shortening theorem establishes
why a successful finite-orbit test is sufficient, while the finite
algorithm establishes termination. No practical complexity bound is
claimed for large ranks or long input words.

## Sources and status

- Sela, *Diophantine geometry over groups I: Makanin--Razborov diagrams*,
  Publications mathematiques de l'IHES 93 (2001), 31--105,
  [DOI 10.1007/s10240-001-8188-y](https://doi.org/10.1007/s10240-001-8188-y).
  The primary imported result is Lemma 10.4(ii), with Definitions
  10.1--10.3. Section 1 and Proposition 5.6 specify the limit and
  constant-sequence conventions. Relevant text and actual printed
  pages 89--90 were inspected; the exponent is 2^m. The complete
  JSJ/Rips shortening machinery has not been independently re-proved.
- Whitehead/McCool stabilizers and Handel--Mosher, Theorem 4.1, are
  credited precisely in `research/notes/F38-stabilizer-obstruction.md`;
  their archived primary sources and previous checks remain in place.
- Lee's rank-two decision and Lee--Ventura's example are prior, as
  documented in `research/notes/F38-bounded-scope-boundary.md`.
- Ould Houcine--Vallino (2016), Theorem 2.15, was consulted, but its
  bounded-parameter statement is **not** being substituted for the
  graded theorem above. It is not an additional proof of (1).

The frozen full F38 paragraph, its background, and its actual rendering
were inspected again during this work period. Part (b) was already
starred/known; part (a) has the separate existing candidate argument.
This proof is an internally checked candidate for the remaining part
(c), not a claim of independent specialist acceptance or established
novelty. Computational evidence and its limits are recorded separately
in `bounded-audit.md`.
