# F37: finite quotients cannot detect every primitive-length lower bound

30 September 2026. An obstruction to a proposed approach, **not an answer
to F37 and not an additional candidate result**. The deduction below uses
credited prior theorems; its novelty has not been established.

## Statement and scope

Let F = F_r have the fixed free basis x_1,...,x_r, where 2 <= r < infinity,
and let P be its set of primitive elements. Write P_{<=k} for products of
at most k elements of P, including the empty product. There is a constant
C(r) such that, for **every** finite quotient pi:F -> G,

    pi(P_{<=C(r)}) = G.

Nevertheless, P_{<=k} is a proper subset of F for every fixed k. In
particular, for every k >= C(r), P_{<=k} is dense and not closed in the
profinite topology of F. Thus a method seeking a finite quotient with
pi(w) outside pi(P_{<=k}) cannot supply every negative answer to the
primitive-length-at-most-k question.

Here pi(P) means images of primitive **words in this marked F**. No
identification with a separate notion of primitive elements of G is used.
The factorization in a quotient may depend on that quotient.

## Imported theorem, with its required hypotheses

Nikolov--Segal, [Generators and commutators in finite groups; abstract
quotients of compact groups](https://arxiv.org/pdf/1102.3037v6),
Theorem 1.2, states that for a finite group G, a symmetric generating set
Y = {y_1,...,y_s}, and H normal in G,

    [H,G] = ([H,y_1] ... [H,y_s])^{*f_1(s,d(G))}.

Here [H,y] is the set of h^-1 y^-1 h y with h in H, d(G) is the minimum
number of generators, and the exponent denotes a bounded set product.
The function f_1 depends only on s and d(G). The finiteness assumption
is stated at the start of Section 1.1, not repeated in the theorem's
displayed paragraph. The symmetric-set hypothesis must be retained.
This is imported deep prior work; the full proof is not audited here.

Define the integer

    F(r) = max { f_1(s,d) : 1 <= s <= 2r, 1 <= d <= r },
    C(r) = 4r F(r) + 2.

It suffices to take ceilings if needed. No numerical value for this
constant or complexity claim is supplied.

## Deduction for a marked finite quotient

The trivial quotient is immediate. Otherwise take H = G and let Y be
the set of distinct elements among pi(x_i) and pi(x_i)^-1, with the
identity removed if present. This is a nonempty symmetric generating
set of size at most 2r, and d(G) <= r.

For each y in Y choose i and epsilon in {1,-1} with y = pi(x_i^epsilon).
If h = pi(u), the commutator in the source's convention is

    [h,y] = pi(u^-1 x_i^-epsilon u) pi(x_i^epsilon).

Each displayed free-group factor is primitive: inverses and conjugates
of basis elements are primitive. The theorem therefore writes every
element of G' as an image of a product of at most 4r F(r) primitives.
The bound concerns the prescribed generators, which is why a bound on
arbitrary commutator width alone would not suffice for this argument.

It remains to handle abelianization without a word-length-dependent
bound. Given w with exponent vector (a_1,...,a_r), put

    p_1 = x_1^(a_1-1) x_2,
    p_2 = x_1 x_2^(a_2-1) x_3^a_3 ... x_r^a_r.

Both are primitive. For p_1, replace x_2 by x_1^(a_1-1)x_2 while fixing
the other generators; for p_2, replace x_1 by x_1 times the displayed
word in the other generators. Each substitution has the evident inverse
obtained by reversing that multiplication. These assertions hold for
arbitrary integer exponents, including zero and negative exponents.

The exponent vector of p_1 p_2 is exactly that of w. Hence
w(p_1 p_2)^-1 lies in F', and its image lies in G'. Apply the preceding
bound to that image and append pi(p_1), pi(p_2). This proves the claimed
uniform bound C(r), for every w and every finite quotient.

## Properness, density, and an explicit prior family

Bardakov--Shpilrain--Tolstykh,
[On the palindromic and primitive widths of a free group](https://arxiv.org/pdf/math/0311257v1),
Theorem 2.1 proves unbounded primitive width in finite nonabelian rank.
More explicitly, their Lemma 2.4 gives

    w_k = (x_1^2 ... x_r^2)^(4k),   primitive length(w_k) > k

for every positive integer k. This family and its lower bound are
**prior**, not constructions or lower bounds newly proved in this run.
For each k >= C(r), w_k lies outside P_{<=k}, while its image lies in
pi(P_{<=k}) for every finite quotient pi.

Every basic profinite open set is a coset of a finite-index normal
subgroup, so surjecting onto every finite quotient is precisely what is
needed for density. It also covers simultaneous tests in finitely many
quotients: use the quotient by the intersection of their kernels.
No conclusion about a single compatible factorization in F follows.

This leaves other algorithmic approaches to F37 open. In particular,
the rank-two equation-based decision already recorded in the literature
ledger is entirely compatible with this obstruction. The argument does
not address the narrower embedding-reflection question in
[the previous note](F37-embedding-reflection-gap.md), or claim that every
fixed-k product set fails to be closed. Rank one is excluded throughout.

## Evidence and limits

The original F37 paragraph in the full archived `probfree.html`, the
linked `Back.html` paragraph, and the local exact fragment were reread.
The original rendered paragraph in `research/statement-audits/F37/`
was actually viewed again. The question asks for the primitive-length
algorithm; its background distinguishes length relative to conjugates
of a fixed basis, which is a different invariant.

The controlling Nikolov--Segal source is **v6**, SHA-256
`ac4ed5f591cad20efc879b3c5cd5400297d95f8fd93afef527430fa51b0d0057`.
Its introduction and Theorem 1.2 were read as extracted text, including
the preceding global finite-group hypothesis. The actual printed page 3
was rendered and viewed. The separately archived v3 was retrieved first;
it is retained but does not control this citation. No full 80-page proof
audit or independent verification of its classification-dependent input
is claimed.

The Bardakov--Shpilrain--Tolstykh source is **v1**, SHA-256
`70ac5475a1f1edfc7b312e5ddbcd3cc0661c015786b8dab67862de172f053864`.
Section 2 and the proof of Lemma 2.4 were read, and actual printed pages
8 and 9 were rendered and viewed. The rest of the paper and the imported
Whitehead/Stallings input were not independently audited. PDF rendering
emitted font bounding-box warnings; the displayed pages remain legible.

The author-hosted `width1.pdf` download was refused; a guessed arXiv v2
URL returned 404. The arXiv version history then identified v1, downloaded
successfully with retrieval metadata. An initial shell invocation used
an unavailable `python` alias and was corrected to `python3`.

Bounded searches on 30 September used `"primitive width" "finite"
"Nikolov"` and `"primitive" "width" "profinite" free groups`.
No matching published formulation was identified in those results;
this is not evidence of novelty. No assertion about closure of P itself
is needed here. No mathematical computation or finite test is offered
as verification of the universal theorem. This is a written deduction,
with imported dependencies and no external referee.
