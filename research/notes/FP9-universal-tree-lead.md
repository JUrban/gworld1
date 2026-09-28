# FP9: a countable universal-group reduction, with an effectivity gap

28 September 2026, approximately 13:55–14:01 UTC. Exploratory observation,
not a solution or a counted partial candidate. The original FP9 HTML was
read; no separate visual statement audit is claimed in this note.

The question is whether every countable locally linear group embeds in
a finitely presented group. The bounded-degree case is already reported
as a theorem of Baumslag–Cannonito–Miller (1977) in Kourovka 5.16; the
unbounded case must not be inferred from it.

## Abstract universal group

There are only countably many finitely generated linear groups up to
isomorphism. Indeed, the entries of a finite generating tuple of matrices
and their inverses lie in a finitely generated commutative ring over Z.
Such a ring is a quotient of Z[t_1,...,t_m] by a finitely generated ideal.
There are countably many such presentations and countably many finite
matrix tuples over them. This assertion is about countability, not an
effective enumeration of faithful representations or embeddings.

More generally, let C be any countable collection of representatives of
countable finitely generated groups, including the trivial group.
For each pair of representatives there are only countably many
monomorphisms, since images of a finite generating set specify a map.

Form a rooted tree whose vertices are finite chains of monomorphisms
starting at the trivial group, and label each vertex by the final group
of its chain. Extending a chain by one monomorphism gives an edge. Give
that edge the parent group, embedded identically in the parent and by
the chosen monomorphism in the child. This is a countable tree of groups.

The usual normal-form theorem for amalgamated free products implies
that all vertex groups, and the direct limit along every rooted ray,
embed in the fundamental group U of this tree of groups. One can see
this by taking the directed union of the groups of finite subtrees;
each inclusion is injective. U is countable.

If a countable group G is an increasing union of groups isomorphic to
members of C, choose representatives and transport its inclusions.
This gives a ray of the tree with direct limit isomorphic to G. Thus
U contains every such G. Taking C to be all finitely generated linear
groups gives a countable group containing every countable locally linear
group. No claim that U is itself locally linear is needed or made.

## Why this does not answer FP9

To apply an effective Higman embedding construction to this particular
U, one would need a recursive presentation. The abstract countability
argument does not supply one. In particular, it does not supply a
recursive enumeration of the injective maps used in the tree.

Even given two finitely generated matrix groups with word-problem
algorithms and a proposed assignment of generators, these algorithms
only let us test each word separately for preservation of equality and
inequality. A finite list of successful tests does not certify a
well-defined injective homomorphism on all words. No method for the
required simultaneous certification was established here.

The effective version would be useful: a recursively enumerated family
of recursive presentations, together with a recursively enumerated
diagram of known injective maps given on generators, has a recursive
tree-of-groups presentation. Standard effective group embedding then
places that recursively presented countable group in a finitely
presented group. The unresolved step for this approach is producing
such a diagram with enough rays to contain **all** the desired groups.

Do not count the abstract universal group as a solution, and do not
assume that word-problem decidability supplies the missing diagram.
No novelty claim is made for the universal-tree observation itself.
