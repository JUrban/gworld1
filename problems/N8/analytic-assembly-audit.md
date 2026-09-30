# N8: the positional constancy implication assembled in Lean

30 September 2026. This closes the previously written cyclic-coordinate
connection between the [positional bridge](polynomial-bridge-lean-audit.md)
and the [energy maximum principle](energy-maximum-audit.md). It verifies
one complete analytic implication used in Section 5 of
[the general proof](general-proof.md). It does not formalize the full
free-Lie argument or the group decision algorithm.

## The exact conclusion now checked

For any natural m, let

    P : R^m -> R,       V : R^(m+1) -> R.

Assume P is continuous; no continuity of V is required. Assume also

    (sum_i w_i) V(w) = P(tail(w)) - P(init(w))             (D)

for every (m+1)-tuple w, and

    V(tail(w)) = V(init(w))                               (R)

for every (m+2)-tuple w with sum zero and equal first and last entries.
Here `tail` deletes the first coordinate and `init` deletes the last.
The final theorem proves

    P(z) = P(0)  for every z in R^m.

This is `N8Assembly.positional_constant` in the self-contained
[Combined-v3.lean](../../research/certificates/N8-analytic-assembly/Combined-v3.lean).
It has no polynomial-degree cutoff, averaging hypothesis at other
indices, reachability hypothesis, or convergence assumption. The
zero-dimensional case is included; positive dimensions use the energy
proof on m+1 coordinates. In the two-coordinate case the two cyclic
neighbours coincide, and the definitions still agree.

## How the components fit together

The previously checked bridge derives cyclic invariance and origin
averaging directly from (D) and (R), without division by a coordinate
sum. The new source proves the missing coordinate identities explicitly.

On a tuple with l=n+2 coordinates, indices belong to the cyclic additive
group `Fin l`. A shift by k is y(i) -> y(i+k). Finite-sum invariance,
the relation between this shift and the earlier `rotate`, and invariance
of the positional function under every shift are all proved.

The concrete half-transfer T_(i->j) satisfies

    shift_k(T_(i->j)y) = T_(i-k->j-k)(shift_k y).

The source checks this equality of coordinate-update functions, then
identifies the prior origin maps exactly with T_(0->1) and T_(0->-1).
Consequently the origin identity on a shifted tuple gives the required
averaging identity at every index of the original tuple. It also proves
that successor and predecessor have no fixed point for l>=2, and that
successor iterates reach every index.

The energy theorem can then be applied with f(y)=P(tail(y)). Finally,
embed any z into the zero-sum hyperplane as (-sum(z),z). The conclusion
f(y)=f(0) becomes exactly P(z)=P(0). Continuity of f follows from
continuity of P and the coordinate projection; this step is checked too.

There are fifteen new declarations in
[Assembly.lean](../../research/certificates/N8-analytic-assembly/Assembly.lean),
plus the unchanged twenty-declaration bridge and ten-declaration energy
source. The combined check audits all forty-five declarations and the
transitive axioms of the final theorem. These are one chain of formal
evidence, not forty-five separate mathematical results or independent
reviews.

## What remains outside this formal statement

In the intended N8 application, P and V are positional encodings of
finite free-associative coefficient arrays. The equation delta V=[E_0,D]
gives (D), and the zero diagonal restriction of [E_0,V] gives (R).
Polynomials give continuous real functions. Those encoding facts and
the passage from constancy as a function to constancy of the rational
coefficient polynomial remain written mathematics.

The free-Lie exclusion of a nonzero constant encoding except for the
single E_0 case, the homogeneous free-basis projection, the full-block
application, leading-pair enumeration, exact Nielsen periods and integral
recursion also remain outside this check. The separate abstract block
formalization has its own stated scope. **Neither the complete N8
theorem nor its decision algorithm is formally verified here.**

Earlier audit files accurately described their then-unassembled pieces.
Their statements that cyclic relocation and analytic assembly remained
written are now superseded by this supplement; their immutable sources
and manifests have not been edited. Counts and novelty status are
unchanged.

## Sources, failures and exact reproduction

The checker combines the exact prior `Bridge.lean`, exact prior
`Energy.lean`, and the new `Assembly.lean`. It collects their import
lines at the top and otherwise preserves their bodies. It writes the
entire combined input to a new, non-overwritable snapshot before checking
it. The run record prints each component hash and the combined hash.
Thus the final snapshot can also be checked directly without this
assembly script.

The unchanged prior component SHA-256 hashes are:

- Bridge: `ad4697b0313dd3ba7cb18bf63ca9b4825b29d93e3d749e310447c1d6b77ccf10`.
- Energy: `63ae082e726df82e198f6a64478d91d443b868a3477f024e017baba9883123d0`.

The accepted combined v3 SHA-256 is
`05cf25384137a1173e2d17ed14a086cf8b9f4f0c0396df198e1dfadbe804da7e`.
All checks used Lean 4.24.0 revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, and `--trust=0`.
Only `propext`, `Classical.choice` and `Quot.sound` are allowed.

| Run | Outcome |
| --- | --- |
| `n8-analytic-assembly-v1` | FAIL, 17.78 s: a permutation-sum name collision, finite-index cast scope, coordinate simplifications and two nonexistent helper names. |
| `n8-analytic-assembly-v2` | FAIL, 18.23 s: the zero-shift base proof and a scalar-multiple/cast identification still needed explicit proofs. |
| `n8-analytic-assembly-v3` | PASS, 19.48 s: complete constancy implication, empty stderr and no warnings. |

Both rejected inputs failed the final axiom audit as well as ordinary
elaboration. All exact component versions, combined inputs and logs
are retained. Runs were sequential, one CPU, 16 GB per-process memory
cap, 180-second timeout, `LEAN_NUM_THREADS=1`; all are terminal. The
combined run rechecks dependencies because the new theorem uses them.
No finite nilpotent/Lie example suite was repeated.

With the pinned binaries and mathlib workspace installed, choose both
a fresh job name and a fresh snapshot path:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name n8-analytic-assembly-replay --cores 1 --memory-gb 16 --timeout 180 \
  --expect 'PASS N8 assembled positional identities imply constancy' \
  -- python3 scripts/check_n8_analytic_assembly.py \
     --snapshot scratch/N8-analytic-assembly-replay.lean
```

Alternatively, run `lake env lean --trust=0` directly on a preserved
`Combined-v*.lean` in the pinned mathlib environment. That also reproduces
the failed versions without replacing any current source.

No source from Kourovka or theorem from A5/S5 is imported. This remains
an internal formalization in the same research effort, not an independent
specialist review or a novelty determination.
