# F25: equal frequencies obstruct a direct degree-sorting extension

Status: a certified obstruction to one proof strategy, **not a solution of
F25(a)** and not a counterexample to Lee's theorems. Derived during the
original run on 29 September 2026. No novelty claim for this auxiliary fact.

## Statement and prior scope

The original [F25](https://shpilrain.ccny.cuny.edu/gworld/problems/probfree.html#(F25))
asks for a uniform polynomial bound, for fixed rank, on the number of
ordinary elements of minimum length in one automorphic orbit. Part (b)
asks for a uniform quadratic bound in rank two and is marked solved.
The original HTML paragraph, its full linked background and the actual
browser screenshot were inspected. The source hash and screenshot are in
`research/statement-audits/F25/`; the source bytes were not changed.

For a minimum word of length L, all minimum representatives are cyclically
reduced: otherwise an inner automorphism shortens them. A cyclic conjugacy
class contributes at most L ordinary words. Thus a uniform polynomial
bound on minimum **cyclic words** suffices, with at most one extra degree.
The two counting conventions must not be silently identified.

[Lee, arXiv:math/0311410v3](https://arxiv.org/pdf/math/0311410v3), Hypothesis
1.1, assumes distinct positive unsigned generator frequencies. Theorem 1.4
sorts type-II Whitehead moves by nondecreasing degree after a suitable
choice of minimum representative (Hypothesis 1.3). Lemma 3.1 sorts a
descending pair. Lemma 2.2 supplies the strict frequency inequality used
in that proof. The source PDF pages 2, 7 and 8 were visually inspected;
the introduction, definitions, theorem statements and this initial proof
step were read, not the entire proof of the paper.

The sharper [Lee, arXiv:math/0401269v3](https://arxiv.org/pdf/math/0401269v3),
Theorem 1.2, gives degree 2n-3 for cyclic words under the same frequency
hypothesis. Its introduction and theorem statements were read as extracted
text. This does not give the unrestricted F25(a) bound. The previously
archived [Shpilrain survey](https://arxiv.org/abs/2510.00889), Section 3,
still formulates the general counting problem. Source retrieval metadata
and bytes for both Lee papers are archived in `literature/raw/`.

## Explicit obstruction

Work in F(a,b,c). Uppercase letters below denote inverses, and cyclic
words are identified by rotation but **not** inversion. Set

    u = CBcbaBaacBcA
      = c^-1 b^-1 c b a b^-1 a^2 c b^-1 c a^-1.

It has length 12 and unsigned frequencies (4,4,4). Its complete
length-preserving type-II Whitehead component has the following 12
vertices. The last column gives the degree of **every** move to the next
vertex in this cyclic ordering, for a < b < c. Self-loops are omitted.

| Vertex | Word | Next vertex | Degree |
|---|---|---|---|
| 0 | CBcbaBaacBcA | 1 | 2 |
| 1 | CBcbaBCaacBA | 3 | 3 |
| 3 | CBcaCaacBBAb | 5 | 2 |
| 5 | CBAbCBcaCaaB | 7 | 3 |
| 7 | CBcaCbaaBCAb | 9 | 2 |
| 9 | CCAcbCBabaaB | 11 | 3 |
| 11 | CBabaaCbCAcb | 10 | 2 |
| 10 | CBabcaaCbAcb | 8 | 3 |
| 8 | CacaaCbbABcb | 6 | 2 |
| 6 | CacaabcbABcb | 4 | 3 |
| 4 | CacBaabcABcb | 2 | 2 |
| 2 | CBcbaBaabccA | 0 | 3 |

The underlying graph is a 12-cycle with alternating degrees 2 and 3.
There are two type-II representatives of each directed edge; all 96
parameter choices, including identities and inner moves, are included
in the certificate. Every one of their 1152 images of the twelve words
has cyclic length in {12,14,16,18}. No shorter image occurs. Whitehead's
classical minimization theorem therefore proves global minimality of u.
All equal-length images appear in the table, and connectivity proves
that these are exactly the vertices of this type-II component.

From any vertex, a path with nondecreasing degrees can reach only four
vertices: itself, either neighbour, and the vertex obtained by first taking
a degree-2 edge and then a degree-3 edge. Traversing a single-degree
matching repeatedly adds no further vertices. Thus choosing a different
basepoint cannot make all minimum images accessible by sorted chains.
Direct checking for all six orders of a,b,c gives exactly four reachable
vertices from every basepoint in every case.

In particular, let sigma fix a,b and send c to bc, and let tau fix a,c
and send b to bC. These are type-II moves of degrees 3 and 2 respectively.
They follow the path 0 -> 2 -> 4, preserving length at both steps.
There is **no** nondecreasing-degree type-II chain from vertex 0 to
tau sigma(u), even though degree 3 is allowed. Consequently Lemma 3.1's
conclusion cannot be extended simply by deleting Hypothesis 1.1(ii).
This fails even for equality on this one cyclic word; Lee's original
lemma asserts the stronger equality of outer automorphisms.

Signed permutations conjugate type-II moves to type-II moves. The union
of the signed-permutation images of this component has 144 cyclic words;
it is closed under all length-preserving Whitehead moves. Peak reduction
identifies it with the full minimum cyclic orbit. Inversion of basis
letters does not change degrees, and a permutation merely changes the
basis order, already checked above. Thus passing to a different minimum
representative anywhere in the full orbit cannot repair this specific
sorting assertion either.

The same obstruction holds for u^k for every positive integer k.
Cyclic length satisfies ||phi(u^k)|| = k ||phi(u)||, and taking kth
powers is injective on conjugacy classes in a free group. Therefore the
labelled minimum graph is carried bijectively to that of the kth powers.
This is an arbitrarily long family of obstructions to degree sorting,
**not** a growing family contradicting a polynomial bound: the cyclic
orbit size in this family remains 144.

## Reproduction and independence

`scripts/probe_f25_degree_order.py` exhausts finite type-II plateaux,
checking minimum length and unsigned-frequency preservation. The bounded
exploratory suite uses seed 2026092901, eight balanced random inputs for
each frequency 3,4,5,6, plus five structured inputs. Duplicate plateaux
are skipped; a configured 12000-vertex limit would produce an explicit
truncated status. Nonminimal inputs are recorded with shortening moves.
No random sample is used as evidence for a universal asymptotic bound.

`scripts/certify_f25_degree_obstruction.py` extracts the complete small
certificate and its graph table. It uses the earlier free-word routines
from this same run; those are not an independent implementation.

`scripts/check_f25_degree_obstruction_gap.g` independently constructs all
subsets A and multipliers using Lee's definition, uses GAP free-group
substitution/reduction, recomputes every edge and every length, checks
connectedness and the alternating cycle, verifies all 72 start/order
reachability sets, and independently counts the signed-permutation closure.
It reads explicit fixtures, not Python routines or search predicates.

Final recorded runs:

- `f25-degree-probe-v1`: 6.691 seconds, pass.
- `f25-degree-certificate-v1`: 0.119 seconds, pass; its source is retained.
- `f25-degree-gap-v1`: 1.925 seconds, pass; its source is retained.
- `f25-degree-certificate-v2`: 0.119 seconds, pass; adds cycle and full
  signed-permutation counts.
- `f25-degree-gap-v2`: 1.974 seconds, pass; independently checks that
  additional structure. Empty stderr; actual exit 0 and required marker.

All jobs reserved one core and 4 GB, sequentially. Certificate files,
source copies and logs have hashes in the accompanying manifest. The
classical Whitehead and free-group root theorems are imported, not proved
by these finite computations. No specialist review has occurred.

## What remains

The weak inequality in Lee's cut argument survives equal frequencies,
but the strict inequality and the resulting degree sorting do not.
An argument grouping equal-frequency generators together would need a
new bound for those groups of moves; the computation supplies no such
bound. Likewise the F41 candidate bounds one fixed orbit with constants
depending on its word, and does not supply the required uniform F25 bound
as the minimum word varies. F25(a) remains unresolved here; part (b)
remains credited prior work. Candidate counts are unchanged.
