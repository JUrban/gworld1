# M0: finite-field Fox-matrix route

Derived during the active run, approximately 12:52–12:57 UTC on 28 September
2026. No Kourovka argument or code was imported. This is a candidate argument
under audit, not an established new theorem.

Let M be free metabelian of finite rank n. A primitive-preserving endomorphism
induces a primitive-preserving integer matrix on its abelianization, hence a
unimodular matrix. Composing with a tame automorphism reduces to an IA map.
Write R=Z[X_1^{+-1},...,X_n^{+-1}] and use **left** Fox derivatives, as columns.
For the Jacobian J of this IA map, the fundamental formula is lambda J=lambda,
where lambda=(X_1-1,...,X_n-1), and J(1)=I.

If det J is not a unit, its augmentation 1 implies that it has at least two
monomials. Reduce modulo a prime preserving two nonzero coefficients. The
reduced determinant is a nonunit of a Laurent polynomial ring over a finite
field, so it vanishes at a point of a finite extension field K with all
coordinates nonzero. The point is not (1,...,1).

The character chi:M -> K* at that point has finite cyclic image. Change the
free basis by Nielsen transformations so that chi(x_i)=1 for i<n and
chi(x_n)=t, where t generates the image. (Apply integer Euclid to the
exponents of the original character values.) The field K is F_p(t).
The singular Jacobian at this character has its kernel in
W=span(e_1,...,e_{n-1}), by lambda J=lambda.

Key orbit lemma: every nonzero vector of W is the Fox column of a primitive
word at chi when n>=3. Indeed, for i!=j<n and P(t)=sum a_k t^k, the free-group
automorphism

    x_i -> x_i product_k (x_n^k x_j^{a_k} x_n^{-k})

fixing the other generators preserves chi and acts on W as
I+P(t) E_{ji}. These realize all elementary transvections over K and hence
SL(W), which is transitive on its nonzero vectors. Their Fox matrices multiply
without a character twist because every automorphism used preserves chi.
For n=2, W has dimension one and singularity simply forces J e_1=0.

Choose the resulting primitive word w with nonzero Fox column in ker J.
Since the endomorphism is IA, the chain rule gives zero Fox column for phi(w)
at chi. A primitive element cannot have zero Fox column at any character:
it is a column of the invertible Jacobian of a basis automorphism. This is a
contradiction. Thus J is invertible and Bachmuth's classical metabelian inverse
function theorem makes phi an automorphism.

Audit priorities: conventions and basis-change similarity; the finite-field
orbit lemma lifted to actual words; explicit singular examples with individually
primitive generator images; earlier work on M0, especially Timoshenko 2020,
whose indexed author-uploaded text still calls ranks above two open.
