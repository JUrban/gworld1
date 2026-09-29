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

## 29 September follow-up: commutator length does not fill the gap

Archived Danny Calegari and Alden Walker, *Isometric endomorphisms of
free groups*, New York J. Math. 17 (2011), 713–743:
https://nyjm.albany.edu/j/2011/17-31v.pdf . The PDF SHA-256 is
`6311674abf5f8a7255ee27777e94c42d2b7a046feeda116a393e1db565e235ac`.
The introduction, Question2.1/Example2.2, Examples2.3–2.7 and the
rank-two conjecture discussion were inspected as extracted text.
No full proof audit or visual inspection of that PDF is claimed.

Example2.2 constructs a rank-four self-embedding decreasing commutator
length, by factoring through a rank-three free group. Example2.7 uses
proper finite-index inclusions and subsequent embeddings. For the
resulting self-embeddings, this lower-rank factorization makes the
abelianization determinant zero. Thus these examples do not establish
failure of reflection under the nonzero-determinant hypothesis needed
above. This determinant observation is our direct inference from the
factorizations, not a theorem attributed to the paper.

These invariants are commutator length and stable commutator length,
not primitive length. The paper's rank-two injective isometry assertion
is Conjecture4.1, not a general proved theorem there; its current status
has not been checked in this pass. No F37 algorithm or counterexample
follows. The original full F37 HTML/background was reread and the actual
publisher paragraph was rendered and viewed in
`research/statement-audits/F37/`. Its fixed-basis conjugate-length
background result is also distinct from primitive length.
