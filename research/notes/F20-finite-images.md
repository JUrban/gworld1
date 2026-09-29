# F20: complete pair tests in seven finite ambient groups

Recorded 2026-09-29T23:31:56.543036+00:00. This bounded counterexample search found no surviving
weight-seven Hall commutator. It does not prove F20 and is not counted as
a new partial result. The original statement and prior-source audit remain
in [the rewriting note](F20-bounded-rewriting.md).

## Exact scope

Let P be the group on a,b with all nine basic Hall commutators of exactly
weight six imposed as relators. For each of the seven groups below, the
search tests every homomorphism P to that group, modulo simultaneous
conjugation of its two generator images. It asks whether any of the
18 weight-seven Hall commutators survives. There is no assumption that
a,b generate the ambient finite group. A surviving target would disprove
the rank-two, weight-six instance; no such target was found.

| Ambient group | Order | First-generator classes | Pairs tested | Commuting pairs | Noncommuting pairs satisfying all nine relators |
| --- | ---: | ---: | ---: | ---: | ---: |
| S6 | 720 | 11 | 7920 | 901 | 144 |
| S7 | 5040 | 15 | 75600 | 5579 | 464 |
| PSL2_7 | 168 | 6 | 1008 | 197 | 20 |
| PSL2_11 | 660 | 8 | 5280 | 716 | 0 |
| PSL2_13 | 1092 | 9 | 9828 | 1163 | 0 |
| PSL2_17 | 2448 | 11 | 26928 | 2558 | 120 |
| PSL2_19 | 3420 | 12 | 41040 | 3554 | 0 |

Totals: 167604 tested pairs, 14668 commuting pairs,
and 748 accepted noncommuting pairs.
Every accepted pair kills all 18 targets. These are counts after reducing
the first generator to a conjugacy representative, not counts of all raw
ordered pairs or of distinct homomorphisms up to full simultaneous conjugacy.
The ambient groups are nonnilpotent; no claim is made that accepted images
are nonnilpotent, nor that this list exhausts finite images of P.

## Construction and independent replay

The Python implementation constructs S6 and S7 from a cycle and a
transposition. For each listed prime p, it constructs PSL(2,p) on the
projective line using x -> x+1 and x -> -1/x. It enumerates the generated
permutation group and conjugacy classes from those generators. Permutations
act on the right; multiplication means apply the first, then the second.
The commutator convention is [u,v]=u^-1 v^-1 u v.

Hall generators are ordered a<b, then by weight, then by parent indices.
A word [i,j] is admitted when i>j and the right parent of i is at most j.
The numbers in weights one through seven are 2,1,2,3,6,9,18. Only weight
six is killed. Commuting pairs are skipped since every weight-at-least-two
commutator vanishes. Two actual imposed relators,
[b,a,a,a,a,a] and [b,a,b,b,b,b], provide an early filter. Every pair that
passes is checked against all nine relators, then all eighteen targets.

The GAP replay independently constructs native free-group Hall words and
uses MappedWord to evaluate them. It verifies the complete ambient group
element list, each conjugacy-class size, disjointness and completeness of
the first-generator representatives, and the full list of accepted pair
indices and nontrivial target indices. Thus matching summary counts alone
are not the verification criterion. It also checks directly that both
pruning words belong to the relator list.

For each group the original generating pair has at least one nontrivial
weight-seven target when the relators are not imposed. Both implementations
verify this omitted-relator control. No randomness or floating arithmetic
is used. JSON uses zero-based indices; the generated GAP fixture converts
all permutation entries, pair indices and Hall indices to one-based values.

## Runs, artifacts and limits

All three recorded runs reserve one CPU and 4 GB, with a 180-second limit.
The Python search passes in 5.69 seconds. GAP's first replay passes in
2.58 seconds with empty stderr, but its output called gap-checks-v1.json
contains GAP line continuations and is not valid JSON. That exact source,
output and process record are preserved. The second replay only changes
serialization to an unformatted output stream and a new versioned path;
it passes with empty stderr. The v2 output parses as JSON and agrees with
the Python summary. This is an artifact-format correction, not a change
to the mathematical result.

The manifest binds both versions, scripts, fixtures and raw run logs.
Scripts refuse to overwrite their outputs: replay in a fresh checkout
without generated outputs, or change to new output paths and run names.
Independent implementation here means a separately constructed computation
by the same research agent, not an external mathematical referee.

This probe differs from the earlier nilpotent-cover homology search, but
its finite non-hit has the same limited logical force. Do not increase
these group bounds without a new structural reason. The general F20
question and the rank-two weight-six presentation remain unresolved here.
