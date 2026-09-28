# F34(a): uncounted positivity lead

Recorded 28 September 2026 around22:11 UTC after the F38(a) checkpoint.
A new application, not yet added to the tally.

If an injective homomorphism phi:F_r->F_s sends w to a positive word,
read that word as a closed positive path in the finite core graph of
phi(F_r). Choose a maximal tree and orient each non-tree edge by its
positive ambient label. Deleting tree edges reads w as a positive word
in the corresponding free basis of the image subgroup. Pull that basis
back through phi. Thus potential positivity is reflected by embeddings.

For F34(a), encode w(X_1,...,X_r)=V with V a word in the positive
ambient generators and all variables freely reduced. A solution with
nonzero abelianization determinant gives an injective endomorphism,
hence potential positivity; conversely an automorphism making w positive
has determinant +/-1. Existence of a nonzero determinant can be decided
by the full EDT0L relation and polynomial-span lemma of F38(a).

Need check the precise problem/background and prior rank-two/stability
results, write the graph reflection lemma and full decision proof, and
independently check a constructive pullback on bounded examples. No
full equation/recompression implementation should be claimed.
