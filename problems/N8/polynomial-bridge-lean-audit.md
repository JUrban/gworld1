# N8: a division-free positional averaging bridge

29 September 2026, approximately 22:55–23:03 UTC. This supplements
[Section 5 of the general proof](general-proof.md) and the earlier
[analytic formalization](averaging-lean-audit.md). The candidate scope
and counts are unchanged. This is a formal check of further universal
ingredients, not a formal proof of the complete N8 algorithm.

## The simplified derivation

Let P be a function on m-tuples and V a function on (m+1)-tuples,
with real values and m>=1. In the intended application these are the
positional polynomials encoding D and V in the free associative algebra.
The derivation uses only the following evaluation identities:

    (sum w_i) V(w) = P(tail w) - P(init w),                  (D)

and, for every (m+2)-tuple w of sum zero with equal first and last entries,

    V(tail w) = V(init w).                                  (R)

Here tail deletes the first entry and init deletes the last. Condition
(D) is the encoded equation delta V=[E_0,D]. Condition (R) is precisely
vanishing of the encoded [E_0,V] on the diagonal used in Section 5.
The opposite sign in Section 6 is handled by replacing V with -V.

Put S=sum z_i and a=-S/2. Apply (R) to (a,z,a):

    V(z,a) = V(a,z).

Apply (D) separately to (z,a) and (a,z). Both left sides have the
same coefficient S+a and the same V-value. Equating the right sides gives

    2P(z) = P(tail(z),a) + P(a,init(z)).                     (1)

**No division by S, a, or S+a occurs.** In particular, S=0 is covered
by the identical calculation. The original argument through a nonzero
open set and polynomial extension is valid but unnecessary here.

Let z^+ be z with a added to its first coordinate, and z^- be z
with a added to its last coordinate. The tuples (z^+,a) and (a,z^-)
have sum S+2a=0. Applying (D) to them gives, respectively,

    P(tail(z),a)=P(z^+),       P(a,init(z))=P(z^-).

Substitute into (1):

    2P(z)=P(z^+)+P(z^-).                                    (2)

This proof works for arbitrary functions satisfying (D) and (R);
polynomiality and continuity are not used in this algebraic step.
The later maximum principle still needs continuity and compactness.

## Exact formal scope

[Bridge.lean](../../research/certificates/N8-polynomial-bridge-lean/Bridge.lean)
uses arbitrary natural-number dimensions, represented by `Fin`, rather
than a bounded collection of polynomial examples. The final axiom audit
covers twenty theorem declarations, including their helper lemmas.

- `cyclic_boundary` derives P(tail w)=P(init w) on the zero-sum
  hyperplane directly from (D). `cyclic_invariance` proves invariance
  under the explicit left rotation of the whole tuple.
- `diagonal_midpoint`, `boundary_average`, `transfer_average` and
  `transfer_average_half` prove the preceding derivation, with every
  tuple deletion, insertion and sum checked by Lean.
- `clockwise` and `counterclockwise` explicitly halve coordinate zero
  and add its other half to coordinate one or the last coordinate.
  `origin_average` proves the averaging identity for these two maps
  on the zero-sum hyperplane.
- `sum_clockwise` and `sum_counterclockwise` prove preservation of
  the coordinate sum. `l1_clockwise` and `l1_counterclockwise` prove
  that neither map increases the sum of absolute coordinate values.
  These statements apply to all real tuples, not just zero-sum ones.

For m=1 the two neighbours coincide; the definitions and all proofs
still apply. A nonzero constant P with V=0 satisfies both hypotheses,
so the intended conclusion is constancy, not vanishing. For comparison,
at m=1 the nonconstant P(z)=z^2 and V(u,v)=v-u satisfy (D), but violate
(R) at (1,-2,1): the two V-values are 3 and -3. Thus the diagonal
hypothesis is substantive. These two examples are elementary written
controls, not additional recorded computational runs.

The link from free-associative coefficient arrays to (D) and (R) is
still a written argument. So are conjugating the origin transfer by
every cyclic rotation, constructing a strictly contracting finite
transfer word, and instantiating the earlier abstract maximum principle.
The latter construction has the quantitative two-cycle proof in the
earlier analytic audit. This file does not silently assume those steps
have been assembled into one formal theorem. The free-Lie projection,
full-block column elimination, integral recursion and full decision
algorithm remain outside the formalization.

## Verification, failures and reproduction

Lean 4.24.0, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, checked
the source with `--trust=0` against Mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Every listed theorem's
transitive axioms must belong to `propext`, `Classical.choice` and
`Quot.sound`. No `sorryAx` or extra axiom is accepted. This uses the
existing ignored S5 toolchain only as infrastructure and imports no
experimental S5 theorem or earlier N8 theorem.

All four jobs reserved one CPU and 8 decimal GB, with a 120-second
bound and `LEAN_NUM_THREADS=1`. They ran sequentially through the
recorded runner and are terminal.

| Run | Outcome |
| --- | --- |
| n8-polynomial-bridge-lean-v1 | Failed in 4.74 seconds: dependent tuple notation lacked explicit real codomains. Exact source and diagnostics retained. |
| n8-polynomial-bridge-lean-v2 | Passed the nine-theorem division-free bridge in 6.59 seconds, empty stderr and no warnings. |
| n8-polynomial-bridge-lean-v3 | The extended source failed in 8.65 seconds: real division definitions needed `noncomputable`, and two sum rewrites targeted the wrong occurrence. The axiom audit rejected the resulting `sorryAx`; exact source retained. |
| n8-polynomial-bridge-lean-v4 | All twenty declarations passed in 10.30 seconds, empty stderr and no warnings. This source is the final `Bridge.lean`. |

The fixes changed notation, compilation annotations and proof scripts,
not hypotheses or conclusions. No finite Lie or group fixture was rerun.
With the pinned binaries on PATH and `LEAN_NUM_THREADS=1`, replay using
a fresh job name:

```sh
python3 scripts/run_recorded.py --name n8-polynomial-bridge-lean-replay \
  --cores 1 --memory-gb 8 --timeout 120 \
  --expect 'PASS N8 division-free positional averaging bridge' \
  -- python3 scripts/check_n8_polynomial_bridge_lean.py
```

On another machine the standalone Lean file can be checked with
`lake env lean --trust=0` in the pinned Mathlib environment.
The [manifest](../../research/certificates/N8-polynomial-bridge-lean/manifest-v1.json)
binds this audit, final and historical sources, prior dependencies and
raw logs. No independent specialist review or novelty certification
is implied. No result count, original deadline, or source statement
has changed.
