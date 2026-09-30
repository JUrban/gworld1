# F34(a)/F38(a): universal span argument checked in Lean

30 September 2026. A shared dependency audit of the existing candidates,
not another result or an independent mathematical review.

[Span.lean](../../research/certificates/F34-F38-span-lean/Span.lean)
contains fifteen accepted universal declarations. They verify the
finite-dimensional span argument and soundness of closed-span certificates
for a directed control graph. The concrete polynomial lift, the full
equation-solution construction, and the group-theoretic applications
remain outside this formalization.

## Formal statements

Let V be a vector space over a field K, let T_e be linear endomorphisms
indexed by E, and let S be a set of starting vectors. Neither a finite
list of examples nor a matrix-size cutoff is assumed. The source uses
function-composition order:

    run([], x) = x,
    run(e::w, x) = T_e(run(w,x)).

Thus the rightmost letter acts first. This convention is explicit and
does not silently identify the two orders of noncommuting edge maps.
Define the increasing sequence of subspaces

    W_0 = span(S),
    W_(n+1) = W_n + sum_e T_e(W_n).

The formal proof establishes:

1. W_n is exactly the span of actual vectors run(w,x), with x in S and
   word length at most n. It contains no vectors that arise solely from
   an unjustified reachability assumption.
2. If W_n = W_(n+1), then every later space equals W_n, and every actual
   orbit vector belongs to W_n.
3. A linear functional vanishes on all orbit vectors if and only if
   it vanishes on a stabilized space. If there is any nonzero orbit
   value, an actual word of length at most n has a nonzero value.
   Nonzero evaluation on a span therefore gives a real path witness,
   not merely a linear-combination artifact.
4. If V has dimension R, there is a stable stage n <= R, and W_R is
   stable. Testing all starting vectors and words through length R
   suffices for universal vanishing.

The last proof handles empty and zero starting sets without extra
hypotheses. It uses the strict increase of subspace dimension whenever
a consecutive pair differs. The earlier written
[foundation audit](../../research/notes/F34-F38-shared-foundation-audit.md)
gives the sharper R-1 bound when the initial span is nonzero. **The Lean
file verifies the uniform R bound, not that sharper bound.** This loses
no decision or termination claim.

There are also three explicit directed-graph declarations. Reachability
is an inductive predicate with only an initial-vector constructor and
an edge constructor from its specified source to its specified target.
For a family of subspaces indexed by states, initial inclusion and
closure under every edge imply inclusion of every reachable vector.
Vanishing on the final-state spaces then implies vanishing on every
accepted path. Finally, vanishing on accepted paths is equivalent to
vanishing on their exact statewise spans.

## Connection to the candidates and remaining boundary

In F34(a) and F38(a), counts for each output component are retained
separately. Lifting these counts to all monomials of bounded total degree
turns every morphism incidence matrix into a linear map, and turns the
determinant or determinant-times-length polynomial into a linear
functional. The monomial expansion and its compatibility identity are
written in [F38(a)'s proof](part-a-proof.md), Section 3. They are not
constructed in this Lean file.

The finite control graph can be encoded in a direct sum of one lifted
space per state: an edge kills all source blocks except its own and
maps that block to the target. Invalid edge sequences then give zero.
Applying the formal dimension bound gives a path bound R = |Q| N,
where N is the monomial-space dimension. The direct-sum encoding and
its correspondence with the concrete implementation are written
connections here, not additional formally checked declarations.

Alternatively, the formal directed-graph certificate theorem directly
matches the checks performed by the earlier independent GAP replay:
initial-vector membership, closure of every state span under outgoing
edge maps, and final-functional evaluation. The Python/GAP code itself
has not been formally verified. No finite fixture suite was rerun.

These universal statements are mathematical correctness implications.
Effective saturation additionally uses the candidates' finite control
graph, finite list of rational matrices, and exact Gaussian elimination.
The general Lean theorem permits arbitrary index and seed sets, so it
does not by itself assert an algorithm for infinite input descriptions.

Terminal support filtering, reversal of a supplied control automaton,
the concrete EDT0L relation and component-count extraction, the
group-to-monoid cancellation reduction, the positivity reflection lemma,
and KLSS's injective-endomorphism equivalence remain written or imported
parts of the two candidate proofs. In particular, this is **not a formal
verification of either entire free-group decision algorithm**. Both
candidates share this one piece of evidence; it is not counted twice as
an independent validation.

## Exact runs, versions, and reproduction

Lean 4.24.0, revision `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`;
mathlib revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
The checker pins the mathlib revision, invokes `--trust=0`, and audits
all fifteen declarations transitively. Only `propext`, `Classical.choice`
and `Quot.sound` are allowed. No `sorryAx` is accepted.

| Recorded run | Exact source | Result |
| --- | --- | --- |
| `f34-f38-span-lean-v1` | `Span-v1.lean` | FAIL, 6.29 s: an underspecified submodule inclusion and an associativity rewrite in the wrong direction. The resulting incomplete proofs also failed the axiom audit. |
| `f34-f38-span-lean-v2` | `Span-v2.lean`, identical to `Span.lean` | PASS, 7.79 s: all fifteen declarations accepted, empty stderr. |

Both jobs ran sequentially with one CPU, a 12 GB per-process memory
limit and a 120-second wall-clock limit. Both are terminal. The rejected
source and full process logs are retained; no earlier result is erased.

For the final version, with the pinned toolchain and mathlib workspace
installed, choose a fresh run name:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name f34-f38-span-lean-replay --cores 1 --memory-gb 12 --timeout 120 \
  --expect 'PASS controlled-span universal reachability and finite dimension bound' \
  -- python3 scripts/check_f34_f38_span_lean.py
```

The generic workspace is reused from earlier Lean checks; no A5/S5
theorem or Kourovka argument is imported. To reproduce v1, put its
snapshot at the checker's `Span.lean` path in a separate checkout.
The manifest binds both versions, checker, original candidate arguments,
shared foundation audit and the exact run records.

The experiment remains at ten whole-entry candidates, two partial-entry
candidates and zero established novel results. Correctness and novelty
still require specialist review.
