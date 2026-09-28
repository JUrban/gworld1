# F38(c): automorphisms and injections give different boundedness questions

Recorded 28 September 2026. This is a scope audit using a prior example,
not a new answer to F38(c). The F38(a) equality argument is unchanged.

The frozen F38(c) quantifies over automorphisms of the specified free group.
Lee, arXiv:0802.0584, Definition 1.4 and its preceding example, and
Lee--Ventura, *Volume equivalence of subgroups of free groups*, J. Algebra
324 (2010), 195--217, Definition 1.1, use that same convention.
In contrast, KLSS, arXiv:math/0409284, Problem 8.4, quantifies over all
free discrete actions on real trees. These boundedness conditions differ.

Use explicit words in F(a,b): u=a and v=a^2 b a^-1 b^-1.
Lee--Ventura's page 2 states that every automorphism alpha satisfies

    ||alpha(v)|| = ||alpha(u)|| + 4.

Thus their ratio lies between 1/5 and 1. Their commutator convention is
confirmed by the explicit expansion on page 9, [a,b]=aba^-1b^-1.
Using instead the convention in our N8 code would change this example.
The universal assertion here is credited to that prior source, not inferred
from the finite check below.

For each n>=1, the homomorphism a->a, b->b^n is injective: its two images
freely generate <a>*<b^n>. Its abelianization determinant is n, yet its
images have cyclic lengths 1 and 2n+3. Hence the nonzero-determinant
replacement used for equality in F38(a) is invalid for F38(c).
The weighted rose with a-edge length 1 and b-edge length n has the same
lengths, proving failure of the all-real-tree boundedness condition too.

In F(a,b,c), the automorphism a->a, b->bc^n, c->c has inverse obtained
by replacing n by -n. The two lengths are 1 and 2n+5. Bounded equivalence
over automorphisms is therefore not preserved by free-factor inclusion.
This example gives no general algorithm in rank three or higher.

## Evidence and reading limits

Read the original HTML and viewed its existing screenshot again. Read
KLSS Problem 8.4, Lee's introduction and Lee--Ventura's introduction;
viewed Lee--Ventura page 2. Their entire papers were not proof-audited.
The author-hosted Lee--Ventura PDF, text, retrieval record and viewed image
are retained under `literature/raw/F38-LeeVentura-volume2010.*` and
`literature/figures/F38-LeeVentura-page2.png`.

`scripts/check_f38_bounded_boundary.py` generated 96 automorphisms of F2
by Nielsen moves with fixed seed 9282638 and depths 0--12, and the two
explicit families for n=1,2,3,5,10,25. All 108 cyclic-length records passed.
`scripts/check_f38_bounded_boundary.g` independently replayed the words
using GAP free groups and cyclic reduction. Both actual exit codes were
zero, expected markers present, stderr empty: Python 0.068 seconds,
GAP 1.825 seconds, each with one core and a 2 GB per-process limit.
The GAP replay checks word lengths, not the Nielsen histories or the
universal prior theorem. Process evidence is in the two
`results/f38-bounded-boundary*-v1/` directories. No failed mathematical
run preceded these two checks; a draft Python import name was corrected
before execution. No result count changes.
