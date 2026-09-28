# F41: a candidate for words of primitivity rank at most two

28 September 2026, active experiment. This is a **partial candidate**,
not a full solution of F41. Independent mathematical and novelty review
remain outstanding. No Kourovka argument is imported.

## Statement and scope

Let F_r have a fixed free basis, r >= 2, and put q = 2r-1. For a subset S
write B_S(n) = #{w in S : |w| <= n}. Its ball exponential growth rate is
lim B_S(n)^(1/n), when the limit exists. We also obtain the corresponding
spherical limsup. We do not assert a spherical limit: parity can prevent it.

**Candidate theorem.** If 1 != w in F_r is nonprimitive in some subgroup
of rank at most two, then

    lim B_Aut(F_r).w(n)^(1/n) = sqrt(2r-1).

Equivalently, this covers primitivity rank pi(w) in {1,2}, where pi(w) is
the least rank of a subgroup containing w nonprimitively. In particular,
it covers every nontrivial nonprimitive word in a rank-two free factor.
The subgroup in the theorem need not be a free factor.

The identity is excluded explicitly: its orbit has growth 1. This is a
literal exception to the website wording, not our proposed contribution.
The remaining intended problem includes pi(w) >= 3.

The main estimate is more general: if a nonprimitive element u of a free
group F_k is not carried by a proper free factor, then the growth of its
injective images in F_r is bounded by the maximum of sqrt(q) and the
cyclic-orbit growth of u inside F_k. We prove this estimate below.

## Prior ingredients and credited scope

1. Puder, *Expansion of Random Graphs: New Proofs, New Results*,
   [arXiv:1212.5216](https://arxiv.org/abs/1212.5216), Lemma 4.1:
   if a finitely generated subgroup H is a proper algebraic extension
   of <w>, the loop for w traverses every edge of its core graph at
   least twice. The proof below repeats this elementary argument to
   make its precise role transparent; this lemma is **prior work**.
2. Erlandsson--Souto, *Counting Curves in Hyperbolic Surfaces*,
   [arXiv:1508.02265](https://arxiv.org/abs/1508.02265), Theorem 1.1:
   on a once-punctured hyperbolic torus, each fixed mapping-class orbit
   of nonperipheral closed curves which are not proper powers has
   O(L^2) elements of hyperbolic length at most L. Their word
   "primitive" means not a proper power, and must not be confused with
   belonging to a free basis. We need only the upper bound.
3. The classical identification Out(F_2) = GL(2,Z) with the extended
   mapping class group of a once-punctured torus. In particular each
   automorphism preserves the peripheral commutator up to conjugacy
   and inversion. One can check surjectivity using the Nielsen
   generators (interchange, inversion, and a Dehn twist); the kernel
   of Aut(F_2) -> GL(2,Z) consists of inner automorphisms.
4. Standard finite core graphs for finitely generated free subgroups,
   and the basis associated with a maximal tree.

Puder's Proposition 4.3 already bounds the growth of **all** words of
primitivity rank m by max(sqrt(2r-1),2m-1). Thus pi(w)=2 in ambient
rank r >= 5 already has the asserted orbit rate, by the conjugacy
lower bound. Ambient rank two is also prior, from ingredient 2 (and
earlier rank-two literature). Proper powers are elementary prior scope.
The potentially new part of the displayed theorem is therefore
pi(w)=2 in ambient ranks **three and four**, to the extent it is not
already covered by other results. We make no novelty claim for all
the special cases contained in that range.

## 1. Rank-two cyclic orbits grow polynomially

For fixed 1 != u in F_2, let A_u(N) count its cyclically reduced
automorphic images of word length at most N, as actual words rather
than conjugacy classes. Then

    A_u(N) <= C_u (N+1)^3.                            (1)

Choose based loops representing the two free generators on a fixed
once-punctured hyperbolic torus. There is a constant K such that a word
of length N has a representative loop of hyperbolic length at most KN;
its geodesic representative is no longer. No lower comparison between
the cusped metric and word length is required here.

First suppose u is not a proper power and is not peripheral. Its
Aut(F_2) conjugacy-class orbit is covered by finitely many mapping-class
orbits, allowing both orientations of the surface and of the curve
(a factor of at most four suffices). Theorem 1.1
therefore bounds the number of these conjugacy classes with word length
at most N by O(N^2). Each has at most N cyclically reduced representatives
of length at most N, since such representatives are cyclic rotations.
This gives (1).

If u is a power of a nonperipheral word z which is not a proper power,
take the automorphic images of z first and then their fixed powers.
The same upper bound applies (even the weaker bound at radius N
suffices). If u is conjugate to a nonzero power of [a,b], its conjugacy
orbit has at most two elements, and its cyclic-word orbit is finite.
These cases exhaust all nontrivial u.

## 2. A transfer estimate for injective images

Let k >= 2 and let 1 != u in F_k be nonprimitive and not lie in any
proper free factor of F_k. Let I_r(u) be the set of all psi(u), for
injective homomorphisms psi:F_k -> F_r. This set is conjugacy invariant.
Let C_r(n) count its cyclically reduced words of length exactly n,
and let A_u(L) count the cyclically reduced Aut(F_k) images of u of
length at most L. There is a polynomial P, depending on k,r,u only,
such that

    C_r(n) <= P(n) sum_{L=1}^n A_u(L) q^((n-L)/2).    (2)

Here are all the counting steps.

Take v = psi(u) cyclically reduced, and let H = psi(F_k). Remove any
basepoint stem in its core graph. In fact a nonempty stem would be
traversed initially and inversely at the end of the reduced word v,
contrary to cyclic reduction. We may consequently use the finite
leaf-free core of rank k. Suppress vertices of degree two to obtain
an unlabelled topological graph Gamma. Every vertex now has degree
at least three, so Gamma has at most 2k-2 vertices and 3k-3 edges.
There are finitely many such multigraphs, allowing loops and bridges.

The loop for v uses every edge. Otherwise its supporting connected
subgraph gives a proper free factor containing v, contrary to the
assumption on u. (A proper connected subgraph of a finite leaf-free
core carrying the loop cannot have the same rank without leaving a
tree attachment with a leaf.) Moreover each topological edge occurs
at least twice in the loop: a bridge occurs an even positive number
of times; for any nonbridge occurring once, choose a maximal tree
avoiding it. The resulting basis expression has one generator
occurring exactly once, making v primitive in H, a contradiction.
This is precisely the argument of Puder's Lemma 4.1.

Move the starting point of the loop to a topological vertex. This
changes v by a cyclic rotation, whose inverse recovery costs at most
n possibilities. Fix the graph Gamma, the starting vertex, orientations
of its E edges, and a maximal tree T. All these have only finitely many
possibilities, bounded in terms of k.

Let P be the resulting reduced closed edge path, of topological length
L, and let m_e be the number of traversals of each unoriented edge e.
Thus L = sum_e m_e and each m_e >= 2. Collapse T and write the path
in the associated rank-k basis. The result is a cyclically reduced
word z of length at most L in Aut(F_k).u. To see cyclic reduction,
two successive non-tree edges cannot be inverse: the intervening
reduced tree path would then be a closed path in a tree, hence empty,
contradicting the reduced cyclic path P. The same applies at its join.
Composing the marking psi with the basepoint-change isomorphism and
the tree-basis identification gives an isomorphism F_k -> F_k. Thus z
belongs to the specified automorphic orbit even when the
basepoint-moving path does not represent an element of the original
based subgroup.

For this fixed pointed graph and tree, z determines P uniquely:
each fundamental-group element has a unique reduced based edge loop.
It follows that at most A_u(L) paths P of topological length L need
be counted. We are not counting all reduced graph paths indiscriminately.

Now give topological edge e a nonempty reduced ambient label of length
ell_e. Immersion of the labelled core ensures no cancellation along P,
so its ambient length satisfies

    n = sum_e m_e ell_e,
    n-L = sum_e m_e(ell_e-1) >= 2 sum_e(ell_e-1).      (3)

There are at most (n+1)^E choices of positive lengths. For fixed
lengths, the number of label assignments is at most

    product_e [2r q^(ell_e-1)]
       <= (2r)^E q^((n-L)/2).                        (4)

We have deliberately overcounted by allowing labels that fail the
immersion condition. Only the valid ones are used in (3); the bound
(4) is valid for their superset. Multiplying by the finite choices,
the rotation factor n, and summing over L proves (2).

In particular, if A_u(L) <= C(L+1)^d, then

    C_r(n) <= C' (n+1)^D q^(n/2)                    (5)

for some constants C',D. More generally, if beta is the limsup
exponential growth rate of A_u(L), (2) bounds the cyclic rate by
max(beta,sqrt(q)); use A_u(L) <= C_epsilon(beta+epsilon)^L and let
epsilon tend to zero. This general estimate is supplementary; only
the polynomial case is needed for the candidate theorem.

## 3. Restore conjugators and obtain the lower bound

Every reduced word of length n is uniquely of the form t v t^-1
without cancellation, where v is cyclically reduced and |v|+2|t|=n.
For each possible |t| there are at most a constant times q^|t|
choices. Substitution of (5), followed by summation over lengths,
therefore bounds the full spherical and ball counts by a polynomial
times q^(n/2).

For the reverse inequality take a fixed cyclically reduced, nontrivial
word v in the given automorphic orbit, of length d. For every m >= 1,
choose reduced t of length m whose final letter is neither the inverse
of the first letter of v nor the last letter of v. These are at most
two forbidden final letters out of 2r. There are at least

    (2r-2) q^(m-1)

such t. All words t v t^-1 are reduced of length 2m+d, and distinct
t give distinct words because their first m letters are t. They are
in the orbit. Taking m = floor((n-d)/2) gives a constant times
q^(n/2) lower bound for the ball count for all sufficiently large n.
Together with the upper bound this proves its asserted limit and
the spherical limsup.

## 4. Apply the estimate to primitivity rank two

Suppose pi(w)=2. Fix a subgroup H of rank two in which w is
nonprimitive and identify H with F_2, writing w as u. The element w
is not a proper power, because otherwise its primitivity rank would
be one. Therefore u cannot lie in a rank-one free factor of H:
an element in such a factor is either a proper power or primitive
in H. Thus u meets every hypothesis of Section 2.

For every alpha in Aut(F_r), its restriction H -> F_r is injective.
Consequently Aut(F_r).w is contained in I_r(u). Section 1 supplies
the polynomial bound required in Section 2, and Section 3 proves
the exact orbit rate.

If pi(w)=1, write w=z^d with |d| >= 2. Its orbit is contained in
the set of d-th powers. A cyclically reduced d-th power of length n
has a cyclically reduced root of length n/|d|, so its cyclic count is
at most a constant times q^(n/|d|) <= constant times q^(n/2).
Restore conjugators as above. The same lower bound proves equality.

For a concrete example in the possibly new ambient ranks, take
w=a^2 b^3 in a standard rank-two free factor of F_3 or F_4. It is
not primitive in <a,b>: its one-relator quotient maps onto the
noncyclic group S_3 by sending a to a transposition and b to a
three-cycle, whereas killing a primitive element of F_2 gives an
infinite cyclic quotient. It is not a proper power, since its
abelianization (2,3) has relatively prime coordinates. Thus pi(w)=2.

## 5. Boundaries of the claim

The injectivity condition in Section 2 is essential. For example,
a^2 b^3 is nonprimitive in F_2, but its **arbitrary homomorphic**
images include every g, by sending a to g^-1 and b to g. These maps
have cyclic image and do not satisfy the hypotheses. No estimate of
the full word-value set is claimed.

Likewise nonprimitivity and the filling hypothesis are essential to
the path-counting step. A primitive word can traverse an edge only
once; a word in a proper free factor can leave entire edges unused.
Both are included as negative controls in the finite graph audit.

The conjectured more precise cyclic rate in Puder--Wu, Question 5.4,
is not proved here. Neither is F41 for general pi(w) >= 3. The
growth counts concern individual words in an orbit, not the number
of distinct automorphic orbits meeting a ball.
