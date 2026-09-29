# F37: the determinant shortcut still needs a reflection theorem

29 September 2026. Unsuccessful extension attempt; no candidate answer.

The F34(a) and F38(a) decision arguments do not automatically apply to
primitive length. They replace certain automorphism questions by
existential nonzero-determinant endomorphism questions only after proving
the relevant property reflects through the resulting injections.

For primitive length one, there is a reflection lemma. If an injection
phi:F_r->F_s sends w to a primitive p, the cyclic subgroup <p> is a free
factor of F_s. For H=phi(F_r), the subgroup theorem for free products
makes H intersect <p> a free factor of H. Since p lies in H this
intersection is <p> itself, so p is primitive in H and w is primitive
in F_r.

For a product p_1...p_k lying in H, the factors p_i need not lie in H.
The preceding argument therefore supplies no factorization of its
preimage by k primitives. The spanning-tree positivity argument of
F34(a) has a different hypothesis and does not supply this missing step.

One cannot assert reflection of primitive length through arbitrary
embeddings of different ranks. Under the free-factor inclusion
F_r -> F_r * <z>, every w has primitive length at most two, using

    w = (w z) z^-1.

Both factors are primitive; the first is the image of z under the
automorphism fixing F_r and sending z to w z. In contrast, finite-rank
free groups of rank at least two have unbounded primitive length by
Bardakov--Shpilrain--Tolstykh, *On the palindromic and primitive widths of
a free group*, arXiv:math/0311257 (published J. Algebra285(2005),574--585).
Its primary abstract and the frozen F37 background record that theorem.
No matching lower bound for a particular word was computed here.

This rank-increase example does **not** disprove reflection for an
endomorphism F_r->F_r with nonzero abelianization determinant. That is
the narrower missing statement needed for the proposed shortcut; it
was neither proved nor disproved in this pass. Even such a statement
would still require an effective full equation-language encoding of
the simultaneous primitive-factor constraints. Neither is supplied.

The previously recorded rank-two reduction via Nielsen's commutator
criterion and Makanin remains prior. No higher-rank algorithm, new
partial result, mathematical computation or novelty claim is recorded.
