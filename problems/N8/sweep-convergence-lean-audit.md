# N8: a concrete convergent word of half-transfers

29 September 2026, approximately 23:35–23:43 UTC. This supplements the
[general proof](general-proof.md), the [analytic check](averaging-lean-audit.md)
and the [positional bridge](polynomial-bridge-lean-audit.md). It gives a
simpler independent justification of the reachability/convergence hypothesis
used by the maximum principle. Here independent means a different argument
within this same research effort, not external specialist review.

The proof works in every finite dimension. It uses successive blocks of
adjacent half-transfers, rather than positivity of a fixed product of
stochastic matrices. The earlier matrix argument is retained unchanged.
No new problem count or novelty claim is introduced.

## 1. The concrete word and a uniform bound

Let l>=2, and let T_i, for 0<=i<l-1, halve coordinate i and add the
other half to coordinate i+1. These are among the clockwise cyclic
transfers already used in the general proof. For k>=0 put q=2^(-k).
On the affected pair,

    T_i^k(a,b) = (q a, b+(1-q)a).                         (1)

This follows immediately by induction, including k=0. Apply these blocks
in the order i=0,1,...,l-2, each exactly k times. Denote the resulting
map by

    W_k = T_(l-2)^k ... T_1^k T_0^k.                     (2)

It is a word of k(l-1) permitted half-transfers. It is not necessary
that the words for different k be nested or powers of one fixed word.
The previously formalized maximum principle requires each point to be
reachable by some finite word, which (2) supplies.

For y=(y0,...,y_(l-1)), define

    a0=y0,       a_(i+1)=y_(i+1)+(1-q)a_i.

Then the result is exactly

    W_k y = (q a0, q a1, ..., q a_(l-2), a_(l-1)).        (3)

For any real q in [0,1], replacing a,b by qa,b+(1-q)a preserves their
sum and does not increase their combined absolute value. The remaining
unprocessed tail likewise has norm at most the initial norm: in particular
|a_i|<=||y||_1. Therefore the absolute values of the first l-1 output
coordinates sum to at most (l-1)q||y||_1. If sum(y)=0, the last output
coordinate is the negative of the sum of the others. Consequently

    ||W_k y||_1 <= 2(l-1) 2^(-k) ||y||_1 -> 0.           (4)

Every intermediate half-transfer preserves the zero-sum hyperplane and
its closed l1 balls. There is no division by a coordinate sum, no
positivity assumption on the coordinates, and no dimension cutoff.
For l=1 the zero-sum space consists only of zero; the formal statement
also treats an empty list. At q=0 the sweep merges everything into the
last coordinate; this limiting map is used to explain the construction,
not asserted to be a finite word of half-transfers.

## 2. Consequence for the polynomial separation argument

Let f be the restriction of the positional polynomial to
H={sum(y)=0}. Its cyclic invariance and origin averaging identity were
derived in the preceding bridge. Rotating those identities gives, at
every coordinate, an average of the two neighbouring half-transfers.

Fix a closed l1 ball in H. At a maximum point of f, both terms of every
averaging identity also attain that maximum, since both remain in the
ball. Thus every W_k of that point has the same value. By (4) these
points tend to zero. Continuity shows that the maximum equals f(0).
Apply the argument to -f to get the corresponding minimum. Hence f is
constant on the ball, and therefore on H. The coordinates y1,...,ym
range freely on H, so the original polynomial P is constant.

This recovers precisely the implication used in Section 5 of the general
proof. It does not change the group-lifting algorithm or require a new
imported theorem. The qualitative version is to take repeated half-transfers
to their full-transfer limits and successively eliminate coordinates;
(2)–(4) give a single explicit approximating sequence with a convergence
bound, avoiding nested limits.

## 3. Exact formal scope

[Sweep.lean](../../research/certificates/N8-sweep-lean/Sweep.lean) uses
finite lists of arbitrary real numbers. Its recursive `sweepFrom` implements
(3), freezing each retained coordinate before proceeding to the next pair.
Nineteen declarations pass the transitive axiom audit:

- `halfPair_iterate` proves (1) for every natural k and every real a,b.
- Length and sum preservation, the decomposition into retained coordinates
  and the final residue, and the l1 bounds are proved for arbitrary lists.
- `zero_sum_sweep_bound` proves (4) with general q in [0,1].
  `zero_sum_sweep_tendsto` substitutes q=(1/2)^k and proves the limit.
- `HalfReach` is generated only by identity, one adjacent half-transfer,
  adding an unchanged prefix coordinate, and composition. It has no
  full-transfer, inverse-transfer or limit constructor.
- `sweep_reachable` proves that every concrete sweep is `HalfReach`-reachable.
  Further lemmas verify length/sum preservation and l1 nonincrease for
  every such reachable point.
- `exists_zero_sum_half_reachable_sequence` assembles these conclusions:
  for any finite zero-sum real list, it supplies reachable lists of the
  same length and zero sum, staying in the original l1 ball, whose l1
  norms tend to zero. This includes the empty list.

Thus the concrete transfer sequence and its convergence are now checked
universally; they are not inferred from finite-dimensional examples.
The formal output is l1 convergence for fixed-length lists. Identifying
those lists with vectors in R^l, relocating the origin averaging identity
by cyclic rotation, and applying the earlier maximum-principle theorem
are still written connections between the separate formal files. The
free-associative/Lie encoding and the original group algorithm also remain
outside this check. No claim of a fully formal N8 solution is made.

## 4. Runs, trust and reproduction

Pinned tools remain Lean4.24.0, revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, and Mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The checker uses `--trust=0`,
checks the Mathlib revision, and rejects transitive axioms except
`propext`, `Classical.choice`, and `Quot.sound`. It imports no other
experimental theorem. Six sequential one-CPU jobs, each limited to120s:

| Run | Memory cap | Outcome |
| --- | ---: | --- |
| n8-sweep-lean-v1 | 8GB | 1.32s failure: named a nonexistent List.Sum module |
| n8-sweep-lean-v2 | 8GB | 4.44s failure: Lean reported out of memory |
| n8-sweep-lean-v2-memory12 | 12GB | 7.59s failure: a triangle-inequality lemma required three arguments; resulting sorryAx rejected |
| n8-sweep-lean-v3 | 12GB | 8.20s pass: thirteen bounds/convergence declarations, empty stderr |
| n8-sweep-lean-v4 | 12GB | 9.25s failure after adding reachability: `prefix` conflicted with a keyword in case alternatives; sorryAx rejected |
| n8-sweep-lean-v5 | 12GB | 10.00s pass: all nineteen declarations, empty stderr; one nonsemantic unnecessarySimpa linter warning in stdout |

Every source version and raw log is retained. The two v2 runs use the
same source, with a changed memory cap. The final source is exactly v5;
it is not a subsequently edited version of the checked file. The resource
caps are the runner's per-process address-space limits, not measured peak
resident usage or a process-tree memory cap. No jobs remain running.

With the pinned binaries on PATH and `LEAN_NUM_THREADS=1`, replay with a
fresh recorded-run name:

```sh
python3 scripts/run_recorded.py --name n8-sweep-lean-replay \
  --cores 1 --memory-gb 12 --timeout 120 \
  --expect 'PASS N8 concrete half-transfer sweep convergence' \
  -- python3 scripts/check_n8_sweep_lean.py
```

The versioned manifest binds this audit, all formal sources, related
controlling arguments and the six run records. No passed finite Lie/group
fixture was repeated. This strengthens one ingredient of the existing N8
candidate; correctness of its full application and novelty still require
specialist review.
