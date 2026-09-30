# N8: a shorter energy proof of the analytic lemma

30 September 2026. This is an alternative proof of the continuous
half-transfer implication used in Section 5 of [the general
candidate](general-proof.md). It removes the need to construct a
convergent transfer sequence. It is not another candidate result or
an external review, and no novelty is claimed for the analytic method.

## The argument

Let l>=2, let H be the zero-sum hyperplane in R^l, and let f be a
continuous function satisfying, at every cyclic index i,

    2 f(y) = f(T_(i->i+1)y) + f(T_(i->i-1)y),

where T_(i->j) replaces the distinct coordinates a=y_i,b=y_j by
a/2,b+a/2. It preserves the sum and does not increase the l1 norm.
We prove f(y)=f(0) for every y in H.

Fix a closed l1 ball S in H. It is compact. The set K of points of S
where f is maximal is nonempty and compact. Choose y in K minimizing

    E(y) = sum_i y_i^2.

The averaging equation and invariance of S imply that both neighbouring
half-transfers of every point of K remain in K. Consequently
E(y)<=E(T_(i->i+1)y) for every i. Direct calculation gives

    E(T_(i->j)y)-E(y) = -y_i^2/2 + y_i y_j.                (1)

If y_i>0, this nonnegative difference forces y_(i+1)>0. Repeatedly
following the cycle would make every coordinate positive, contradicting
sum(y)=0. On the other hand, a nonzero zero-sum vector has at least one
positive coordinate. Hence y=0, and the maximum of f on S is f(0).
Apply the same argument to -f to obtain the minimum. Thus f is constant
on S, and the radius was arbitrary.

Equivalently, a nonzero zero-sum vector has a positive coordinate whose
cyclic successor is nonpositive, and its transfer strictly decreases
E. This includes intervening zero coordinates. The sum/l1 preservation
keeps the transfer inside S; squared norm itself need not decrease for
every transfer. Assuming that stronger assertion would be incorrect.

No limiting map, positive stochastic matrix, nested limit or convergence
rate is used. The earlier [stochastic argument](averaging-lean-audit.md)
and [explicit sweep](sweep-convergence-lean-audit.md) remain valid separate
proofs; they are retained unchanged.

## Exact formal scope

[Energy.lean](../../research/certificates/N8-energy-lean/Energy.lean)
checks ten declarations, universally over finite index types. The
transfer is defined explicitly by two coordinate updates. Its sum,
l1 bound and exact energy change (1) are proved from finite sums.

The successor map sigma has no fixed point, and its iterates reach
every index from every other. The final theorem permits a second map
tau with no fixed point; tau need not be the inverse of sigma. The
hypothesis is the displayed averaging equation with transfers to sigma(i)
and tau(i). In N8 they are the two cyclic neighbours. For l=2 the
neighbours coincide, which is permitted.

`energy_minimum_forces_zero` proves the sign-propagation argument from
the exact energy inequalities. `compact_harmonic_constant` implements
the maximum-set/minimum-energy proof on a compact invariant subset of
H containing zero. `compact_zeroBall` proves the needed compactness:
the closed zero-sum l1 ball is a closed subset of a finite coordinate
box. The final `hyperplane_harmonic_constant` instantiates these facts
for arbitrary radii and proves f(y)=f(0) on the entire hyperplane.

Unlike the earlier abstract maximum principle, this theorem has **no
reachability or convergence assumption**. It proves the whole analytic
implication from the all-index averaging identity for the concrete
half-transfers. It does not assume a fixed finite dimension or a degree
bound for f; only continuity is required.

For the N8 application, put f(y)=P(y_1,...,y_m), l=m+1. The
[division-free positional bridge](polynomial-bridge-lean-audit.md)
proves the origin averaging identity and cyclic invariance from the
delta and diagonal identities. Rotating the origin identity gives the
all-index hypothesis above. The new proof therefore implies that P is
constant, precisely the conclusion needed in Section 5.

The correspondence between rotations and indexed coordinate updates,
and the application of those separately checked bridge declarations,
are still written connections, not assembled into one Lean theorem in
this file. Free-associative coefficient encoding, the Lie projection,
full-block separation and the integral algorithm likewise remain outside
this analytic check. No complete formal verification of N8 is claimed.

## Reproducibility and retained failures

Lean 4.24.0 revision `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`,
mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, `--trust=0`.
All ten declarations have a transitive axiom audit accepting only
`propext`, `Classical.choice`, and `Quot.sound`.

| Run | Source | Outcome |
| --- | --- | --- |
| `n8-energy-lean-v1` | `Energy-v1.lean` | FAIL, 6.09 s: a function-update simplification and implicit set-membership inequalities needed explicit forms. Incomplete proofs also failed the axiom audit. |
| `n8-energy-lean-v2` | `Energy-v2.lean`, identical to `Energy.lean` | PASS, 9.10 s, empty stderr and no warnings. |

Both sequential runs used one CPU, a 12 GB per-process cap and a
120-second timeout. Exact sources and logs, including the first failure,
are retained. No earlier finite group/Lie or transfer suite was rerun.
The checker reuses the pinned ignored mathlib workspace as infrastructure;
it imports no theorem from A5, S5 or Kourovka.

With the pinned toolchain installed, replay with a fresh run name:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name n8-energy-lean-replay --cores 1 --memory-gb 12 --timeout 120 \
  --expect 'PASS N8 concrete half-transfer energy maximum principle' \
  -- python3 scripts/check_n8_energy_lean.py
```

The manifest binds the two exact sources, checker, run records, written
argument and previous relevant dependencies. Counts, novelty status and
the original deadline are unchanged.
