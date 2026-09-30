# B9 — Mapping class groups

[Offline statement](statement.html) · [Complete archived page](../../sources/raw/probBr.html) · [Publisher](https://shpilrain.ccny.cuny.edu/gworld/problems/probBr.html)

Source begins at line 59; byte range [2636, 3037). The raw fragment is stored in `source-fragment.html`.

Heading star: False. Starred subparts: none detected. Hall of Fame entries: 0. Linked background sections indexed: 0.

A [candidate infinite family](infinite-family-proof.md) gives countably
infinitely many special braids in every B_N with N>=5. Its
[audit](infinite-family-audit.md) includes symbolic integer matrices and
independent faithful-action checks. This is one partial candidate; the
four-strand count and external review remain outstanding. The
[small-strand supplement](small-strand-proof.md) deduces the exact counts
1, 2 and 4 in B1, B2 and B3 from Dehornoy's prior results and isolates
the remaining B4 sector of exponent sum two. Its
[audit](small-strand-audit.md) credits these dependencies and records
the new right-power checks. A further
[parameter reduction](positive-parameter-reduction.md) classifies all
positive parameters and proves uniqueness of a terminal special pair in
each represented coset; possible additional negative terminal pairs
remain unresolved. The earlier
[height-bound counterexample](height-counterexample.md) and
[bounded counts](../../research/notes/B9-bounded-enumeration.md) remain
development records and are not additional candidates.
The [exponent-two parameter follow-up](exponent-two-parameter-reduction.md)
gives an adjacent-strand restriction, rules out the smallest underlying
strand cases, and records a counterexample to a proposed general rigidity
lemma. Its 268-case filtered probe yields no new B4 example.
The [fixed-first-color reduction](fixed-first-color-reduction.md) proves
uniqueness of the second color outside B3. It excludes every first color
on all four known parameter rays, for arbitrary special second colors,
and implements an exact eight-comparison test for those families.
First colors outside those families still leave the B4 count unresolved.
The machine-readable source evidence is in `data/problems.json`; the
extracted text below is a search aid, not an authoritative transcription.

```text
(B9) (P. Dehornoy) Say that a braid is special if it can be obtained
from the trivial braid by using iteratively the self-distributive exponentiation
a \wedge b = a S(b) sigma_1 S(a)^{-1}, where
S is the shift endomorphism that maps \sigma_i to \sigma_{i+1}
for every i. How many special braids are there in B_n?
```
