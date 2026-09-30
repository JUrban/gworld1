# N8: the exceptional power in the generated Lie subalgebra

30 September 2026, during the original experiment. This supplements the
[ordered-word dictionary](word-dictionary-audit.md) with the Lie condition
needed in Section 5 of [the general proof](general-proof.md). It adds no
problem count or established novelty claim.

## Exact Lie object and proof

The ambient associative algebra remains `Q[FreeMonoid N]`, with letters
E_i. The Lie bracket is the actual associative commutator `FG-GF`.
`N8Lie.generatedLie` is Mathlib's smallest rational Lie subalgebra
containing every E_i, defined using `LieSubalgebra.lieSpan`.

The algebra homomorphism `abelianImage` sends E_0 to X in Q[X] and all
E_i with i>0 to zero. Induction on the generated Lie subalgebra proves
that every Lie element maps to cX for some rational c. Generators have
this property, linear combinations preserve it, and every bracket maps
to zero because the target algebra is commutative.

If `c E_0^m` is in this Lie subalgebra and m is not one, comparing the
coefficient of X^m forces c=0. The converse is also proved, giving the
exact classification

    c E_0^m belongs to the generated Lie subalgebra
        if and only if c=0 or m=1.

This includes m=0: a nonzero scalar is not a Lie element here.

The existing global derivative E_i -> E_(i+1) is also proved to preserve
the generated Lie subalgebra. Its associative Leibniz rule gives the Lie
derivation identity; induction on Lie generation then proves closure.

## Positional separation corollary

Let D and V have respectively m and m+1 E letters, and suppose D is in
the generated Lie subalgebra. With delta the existing global derivative
and R the explicit positional polynomial restriction, the checked
implication is

    delta(V) = [E_0,D],  R([E_0,V]) = 0
        => V=0 and either D=0, or m=1 and D=c E_0.

In particular, if m!=1, both D and V vanish. Equivalently, a nonzero D
in such a component satisfying the derivative equation has
`R([E_0,V]) != 0`. These are universal theorems, not finite-dimensional
tests. No assumption that V is itself a Lie element is needed.

The m=1 exception is deliberately retained. In the written correction-
block application its scalar-E_0 possibility is excluded by the distinct
weight inequality q>p+t. This file does not introduce a formal model of
those weights or silently remove that hypothesis.

## Boundaries

There are ten new theorem declarations and 97 unchanged prerequisites
in the analytic, polynomial and ordered-word chain. The component is
[Lie.lean](../../research/certificates/N8-lie-exception/Lie.lean).

This formalization uses the concrete Lie subalgebra inside the associative
algebra. It does not prove an isomorphism from an abstract free-Lie
construction, the homogeneous subalgebra projections in Section 6, the
inner-solution theorem, arbitrary correction-block separation, exact
integral periods, or the entire terminating group algorithm. The full
arbitrary-rank/class solver remains unimplemented. The other formal
supplements retain their own precise scopes.

The earlier word-dictionary audit correctly described the scalar-power
exclusion as outside its component. This new supplement supplies that
step; its earlier bound files and manifests remain unchanged. The check
is same-agent formal work, not an independent specialist's review.

## Verification and reproduction

Jobs are sequential, recorded with one CPU, 16 decimal GB per-process
memory, a 180-second limit and `LEAN_NUM_THREADS=1`. The checker pins
Lean 4.24.0 revision `797c613eb9b6d4ec95db23e3e00af9ac6657f24b` and
Mathlib revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. It uses
`--trust=0`; transitive theorem axioms are restricted to `propext`,
`Classical.choice` and `Quot.sound`.

| Run | Result |
| --- | --- |
| `n8-lie-exception-v1` | FAIL, 64.23 s: polynomial simplification needed the explicit coefficient-of-X lemma for m!=1. The incomplete proof was rejected by the axiom audit. |

| `n8-lie-exception-v2` | PASS, 67.59 s: all ten new declarations and 97 unchanged prerequisites; empty stderr and no warnings. |

Both recorded PIDs were confirmed absent after termination, and the job
registry was empty. Exact combined/component snapshots were matched to
the run headers, and stdout/stderr to their terminal receipts. The final
input is [Combined-v2.lean](../../research/certificates/N8-lie-exception/Combined-v2.lean).
Every attempt is retained; [manifest-v1.json](../../research/certificates/N8-lie-exception/manifest-v1.json)
binds these exact files.

In a checkout with the pinned dependencies, choose fresh output paths:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name n8-lie-exception-replay --cores 1 --memory-gb 16 --timeout 180 \
  --expect 'PASS N8 generated Lie subalgebra exception' -- \
  python3 scripts/check_n8_lie_exception.py \
  --snapshot research/certificates/N8-lie-exception/Combined-replay.lean
```

The original runner enforces the experiment's deadline. Later reproduction
belongs in a separate review checkout and must not reset that clock.
