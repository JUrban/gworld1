# B9: bounded special-braid enumeration

28 September 2026, approximately 14:04–14:15 UTC. Exploratory verified
lower bounds, **not a solution of B9 and not an additional counted
partial candidate**. The original full HTML, exact B9 paragraph and
rendered paragraph have been inspected. No Kourovka code or argument
was imported.

## Exact conventions and question

In the standard inclusion Bn <= B_(n+1), write

`a triangle b = a shift(b) sigma_1 shift(a)^(-1)`.

Special braids are the closure of 1 under this operation. The question
asks how many lie in Bn, not how many have a bounded expression height.
A term has height 0 at the leaf 1 and height `1+max(h(a),h(b))` at an
operation node. A height-h term lies in B_(h+1), by induction. This
gives finite subsets; it does not give exhaustion at any fixed n.

## Exact bounded enumeration through height four

`scripts/b9_special_braids.py` enumerates all terms of height at most
four, identifying braids by their faithful Artin action on F5. Positive
generator i maps `x_i -> x_i x_(i+1) x_i^-1` and `x_(i+1) -> x_i`.
Products act as composition `rho(uv)=rho(u) o rho(v)`.

| Height bound | Exact number at that height or below | Ambient group |
|---|---:|---|
| 0 | 1 | B1 |
| 1 | 2 | B2 |
| 2 | 4 | B3 |
| 3 | 10 | B4 |
| 4 | 52 | B5 |

All pairs of previously enumerated elements suffice, since equal
braids have equal shelf products. Pairs used earlier need not be
repeated. Equality of freely reduced basis images is exact braid
equality by faithfulness of the Artin representation.

Among these 52 records, respectively 1,2,4,10,52 belong to B1,...,B5.
To test the standard Bn, the action must fix x_(n+1),...,x5 and
preserve F_n. The complementary normal closure is fixed by the
automorphism and its inverse, so the induced map on F_n is an
automorphism. It preserves the boundary product and conjugacy classes
of the individual generators; Artin's characterization then identifies
it as an n-braid. These counts concern the bounded set only.

The JSON certificate includes exact signed words and parent indices.
Its hash is
`3134e7bcaae4f1cf5b8d174b29a6a78b25d457e3b4e96f47754bdbca576ac4c4`.

GAP independently checks parent expressions and all four closure
stages using free-group substitutions. It additionally separates all
52 records by unreduced Burau matrices over GF(1000003), at t=2.
Distinct images prove distinct braids regardless of whether this
representation is faithful.

## Height five: certified lower bound 1930 in B6

The full Artin enumeration exceeded its 120-second limit because
freely reduced images grow rapidly. That failed run is preserved, and
no height-five Artin certificate was written.

Instead `scripts/b9_burau_lower_bound.py` evaluates all 52^2 shelf
products of the previous records in the finite Burau representation.
Together with the leaf, it finds **1930 distinct images**, hence at
least 1930 special braids in B6, all of term height at most five.
Colliding matrix images are discarded without asserting braid
equality, so 1930 is not asserted to be the exact height-five count.
It is also not the total number of special braids in B6.

The unreduced generator matrix is the identity outside its i,i+1
block, which is `[[1-t,t],[1,0]]`. Here t=2 and p=1000003; all
arithmetic is exact modulo p. A separate GAP verifier checks p is
prime, the braid relations, all 1930 recursive parent **free-word**
identities (not merely matrix identities), height bounds, strand
support, and pairwise distinctness by full matrix multiplication.
Thus each word is certified special independently of any faithfulness
claim. The certificate hash is
`3f64808069568bc6691b7d7273344beacf5edf6a18a7d0f968a23ea12bd8c920`.

## Relation to the literature

Patrick Dehornoy, [*The Braid Shelf*, arXiv:1711.09794](https://arxiv.org/abs/1711.09794),
Section 3.2, concerns the same notion of specialness. Proposition 3.15
gives decidable specialness, and Lemma 3.17 classifies the positive
special braids. Decidable membership is not a stopping bound for
enumerating the whole intersection with Bn.

Printed p.13, inspected visually and saved in `literature/figures/`,
defines minimum term height c, claims c(beta)<=n implies beta in Bn,
and asks the converse in Question 3.19. Under the standard strand
convention the forward bound is B_(n+1): sigma_1 already has height 1.
The following printed sentence gives `2^n` as a prospective upper
bound on the number in Bn. The certified 52 elements in B5 exceed
2^5=32, so this printed numerical bound cannot hold. The image really
does print `2^n`; it is not an extraction of `2^(2^n)`.

This exposes a numerical/indexing issue, **not a disproof of the
height-converse question itself**. All certified examples have small
height; none supplies arbitrarily large minimum height at fixed n.
No novelty is claimed for these finite counts. Searches for special
braid counting and Dehornoy's height question did not locate a
complete answer, but that is not evidence of current openness.

## Recorded computations

All runs used one CPU slot and a 4 GB per-process limit.

| Run | Outcome |
|---|---|
| `b9-height4-v1` | Passed, 52 exact bounded records, 0.12 s |
| `b9-height4-gap-v1` | Passed, independent Artin and Burau checks, 2.33 s |
| `b9-height5-v1` | Timed out at 120 s; no completed certificate |
| `b9-height5-burau-v1` | Passed, 1930 distinct images, 0.37 s |
| `b9-height5-burau-gap-v1` | Passed, all 1930 independent checks, 14.11 s |

Commands, process status, raw output and hashes are retained under
`results/`; the signed-word JSON and GAP fixtures are under
`research/certificates/B9/`. Successful runs have empty stderr.
There is no random seed: the enumeration is deterministic.
