# B9: a verified failure of the height bound

29 September 2026, approximately 19:25–19:40 UTC. The main artifact is
[`problems/B9/height-counterexample.md`](../../problems/B9/height-counterexample.md):
a special beta in B5 with minimum term height six. Eleven distinct
examples have independent GAP certificates. This refutes the literal
height question in Dehornoy's *The Braid Shelf*, Question 3.19, but does
not answer GroupWorld B9's unrestricted counting question. No GroupWorld
candidate-count change or established-novelty claim.

## Discovery and exact checks

The earlier 1930 saved height-five representatives were reused from this
experiment, not from Kourovka. Their finite Burau images exhaust the
height-five image set; the braids themselves were only a certified lower
bound. At modulus 1000003 and parameter 2, consider pairs A,B in that set.
For the shelf product in dimension seven to be supported in the first six
coordinates, A and B must have identical last rows and identical last
columns of their inverses. Both shared vectors must have zero first entry.
This follows by multiplying the last-row and last-column identity
conditions by shift(A) and the other invertible factors in the product.
The program also checks the final full matrix support directly.

Grouping by these fingerprints reduces 3,724,900 parent pairs to 19,585
eligible pairs in544 buckets. The filter finds6664 distinct new matrices.
These are **necessary matrix conditions**, not by themselves braid
subgroup-membership proofs. All saved words have explicit special parents.

CBraid's left canonical form checks standard strand membership as follows.
Track the last strand through a word and delete all its crossings. If it
does not finish in its original position, membership fails. Otherwise
compare the original braid to the deleted word embedded back into the
same braid group. Equality is equivalent to membership in the standard
subgroup on one fewer strand: deletion is the retraction on the subgroup
fixing the last strand. Iterate this test. This is standard support,
not minimum strand number after conjugacy or Markov moves.

The CBraid stage finds6653 examples with minimum standard support6 and11
with support5. It also checks164 controls:52 old exact examples,12 explicit
pure/cancellation cases, and100 ten-letter random examples with seed
2026092919. The latter are compared to the independent faithful Python
Artin action, including equality of the returned shorter words.

The result of interest does **not depend on trusting CBraid**. The small
GAP fixture contains a self-contained41-node special-term DAG for all11
B5 examples. The independent checker validates every DAG relation as an
identity of free words, reconstructs the finite matrix sets from the
identity through all five heights, and checks each shorter B5 word against
its height-six word using the faithful Artin action on F7. All11 are
distinct, are absent from the1930-element image set, and move x5. Thus
each has minimum height6 and minimum standard support5. Witness4 also
has a written29-letter reduction using only distant commutations and
cancellations.

The initial GAP verifier used reversed free-group substitutions. It
confirmed six examples but timed out at180seconds while constructing
intermediate words for the seventh. Its exact source is retained as
`research/certificates/B9-strand-drop/check-height-v1-timeout.g`.
The revised verifier composes each generator on the right and updates
only its two affected images. It checks the same identities and all11
examples in4.68seconds. No search budget was increased; stderr is empty.

## Dependency and reproduction

Discovery dependency: [CBraid](https://github.com/jeanluct/cbraid), commit
`891fcaf7cf9af3ec9ca0f1b0e46b0f86cf461b78`, downloaded into ignored
`large-artifacts/tools/cbraid`. Its upstream code is not included here.
It credits Jae Choon Cha, Juan Gonzalez-Meneses and Jean-Luc Thiffeault;
the upstream license applies. A clean checkout built with
`make -C large-artifacts/tools/cbraid/lib -j4`.
The local wrapper compiled with:

```sh
g++ -O2 -std=c++17 -Ilarge-artifacts/tools/cbraid/include \
  scripts/check_b9_strands_cbraid.cpp \
  large-artifacts/tools/cbraid/lib/libcbraid.a \
  -o large-artifacts/tools/b9_strands_cbraid
```

The discovery executable SHA256 is
`9b4402e10476a35d693c8d450ea2408f0881d78c497fd96ffcfe2ae0dd2e212f`.
The independent result can be reproduced with the included GAP fixture
and `bin/gap -q scripts/check_b9_height_counterexamples.g`; no CBraid,
Python, original1930-record list or large discovery output is needed for
that verification. During the active run use the recorded runner.

Recorded jobs (all terminal):

| Job | Outcome |
|---|---|
| b9-strand-drop-matrix-v1 | Passed finite filter,5.69s |
| cbraid-build-v1 | Passed,2.73s,4CPU/6GB |
| b9-cbraid-checker-build-v1 | Passed,0.82s |
| b9-strand-drop-cbraid-v1 | Passed6664 tests and164 controls,8.50s |
| b9-height-counterexamples-export-v1 | Passed,0.32s |
| b9-height-counterexamples-gap-v1 | Timed out180s; first six passed |
| b9-height-counterexamples-gap-v2 | Passed all11 plus exhaustive image set,4.68s |

All mathematical runs use one CPU and at most6GB; no overlapping discovery
workers. Raw process metadata, stdout and stderr are retained under
`results/`. The matrix filter and exact checker output are about13MB and5MB,
respectively, below the repository blob limit. The independent fixture
is less than8KB.

## Bibliographic limits

The full original HTML, its actual rendered B9 paragraph and the archived
survey's printed page13 were re-inspected. Searches for special braids,
height, finite counting, infinitude, and Question3.19 mostly returned
the same primary surveys or unrelated uses of “special”. No prior
counterexample was located in this bounded check; novelty is not established.
The different positive family in *Unprovability results involving braids*
is not the monogenic braid shelf and is not used.

The old52 and1930 lists alone did not contradict Question3.19. The new
exact B5 membership **together with exhaustive lower-height matrix
exclusion** does. A fixed-strand infinitude or total-count argument is
still missing, and the broader B9 entry remains unresolved here.
