# F38 primitive-power classification: audit and reproduction

29 September 2026. Companion to `primitive-power-proof.md`.

## Exact scope

Ambient rank at least three, two nonidentity inputs, at least one input
a power of a primitive element. The procedure recognizes that promise
by taking the maximal cyclic root and applying classical Whitehead
minimization. It tries either input and records any swap. Outside that
scope it returns an explicit unsupported status, not a negative answer.
The theorem is about cyclic lengths under ambient automorphisms.

The new implementation is `scripts/f38_primitive_power.py`. It has no
numerical search cutoff. On a positive case it gives a normalizing
automorphism with inverse and the two exponents; their absolute ratio
is the exact length ratio. On a negative case it gives the same
normalization, a selected Nielsen twist, its growth profile, and the
transported automorphism theta with inverse. The profile contains all
cyclic gaps, slopes, eventual slope delta>0, threshold T and intercept
beta. The maximum length of a basis image under normalization converts
the normalized exact growth formula to a lower bound for theta iterates.

This is a separate small implementation. The existing full stabilizer
and common-filling-carrier classifier is unchanged. It already detects
these negative and positive cases by more general machinery; no new
decision coverage for that classifier is asserted.

## Finite checks

The Python control script exhausts reduced cyclic rotation classes in
the following ranges, without identifying a word and its inverse:

| Rank | Maximum length | Nonempty cyclic words |
| ---: | ---: | ---: |
| 3 | 5 | 868 |
| 4 | 4 | 780 |
| 5 | 3 | 310 |

For every word it tests all r Nielsen automorphisms in the proof's
finite family, producing 7,274 exact formula records. It compares the
formula with free substitution at powers -3,-1,0,1,2,5: 43,644 checks.
For each word the common zero-growth condition agrees with being a
power of the first generator.

Eighteen full normalization cases add nontrivial basis changes,
conjugation, a negative primitive root, a reversed input order, positive
common powers and negative examples. For each of ranks 3,4,5 there are
two positives and four negatives. Negative cases include the higher-rank
version of Lee's rank-two pair, a commutator in other basis letters,
and a distinct primitive. The Python check also compares iterates of
the transported witness at n=0,1,3,7 with the exact normalized formula
and verifies the length-transfer inequality. Separate controls require
unsupported results for rank two and for two nonprimitive commutators.

The independent GAP checker uses native free-group words and constructs
the relevant Nielsen maps directly. It evaluates all 7,274 formula
records at the six listed powers and at T+1,T+7, for 58,192 substitutions.
For the 18 normalizations it checks the following exact identities:

- Both compositions of each supplied automorphism and inverse are the
  identity on every basis generator.
- The normalized fixed word is a^p; positive cases have moved word a^q.
- For every negative case, mu theta = sigma mu on every basis generator,
  theta fixes the designated conjugacy class, and the normalized moved
  word has positive eventual slope with the claimed sampled lengths.

There are six positive normalization certificates and twelve negative
transport certificates. GAP also independently builds the product of
the three two-vertex carrier graphs and prunes leaves. For ranks 3,4,5,
respectively, it obtains eight vertices, 12/14/16 directed edges and
4/6/8 surviving directed core edges. This checks the graph calculation
used in the general proof, including the separate a-loop component.

These are independent computations in different word implementations,
not independent authorship or specialist validation. The general
argument, including the exact all-integer Nielsen formula and its
carrier interpretation, is written in the proof; finite samples alone
do not establish it.

## Recorded evidence

| Run | Elapsed seconds | Actual exit | Stderr | Required marker |
| --- | ---: | ---: | --- | --- |
| `f38-primitive-power-v1` | 2.075853 | 0 | empty | present |
| `f38-primitive-power-gap-v1` | 2.476759 | 0 | empty | present |

Both jobs used one core, a 6 GB per-process reservation and a 180-second
timeout. They finished before the original experiment deadline. There
were no failed mathematical jobs for this new suite. Complete commands,
timestamps and output hashes are in their `results/` process records.

`research/certificates/F38-primitive-power/` contains `checks.json`,
the GAP fixtures, exact source snapshots and a hash manifest covering
the proof, audit and recorded runs. The generator refuses to overwrite
its evidence. To reproduce, use a separate disposable checkout, remove
only its generated certificate files there, and replay the recorded
Python then GAP commands through `scripts/run_recorded.py` with fresh
job names. Existing GAP fixtures can also be checked directly without
regenerating them.

The original statement rendering and prior Lee source are included by
hash in the manifest. The external prior rank-two exception remains an
essential negative control on the theorem's rank scope. Targeted
searches located no explicit prior copy of the restricted theorem, but
novelty is unverified. Counts remain six whole-entry candidates, three
partial candidates and zero established novel results.
