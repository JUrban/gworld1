# N8: formal checks of two analytic ingredients

29 September 2026, approximately 22:30–22:35 UTC. This supplements
[the general proof](general-proof.md), Section 5. It changes neither
the candidate's scope nor the experiment's tally. It is **not** a
formalization of the polynomial separation lemma as a whole, the
free-Lie argument or the general N8 decision procedure.

## Exact formal statements

[Averaging.lean](../../research/certificates/N8-averaging-lean/Averaging.lean)
contains two principal theorems, with their intermediate lemmas.

`N8.stochastic_contraction` uses an arbitrary finite index type, a real
matrix A, a real number e and a real vector v. Under the hypotheses

    A_ij >= e for every i,j,
    sum_i A_ij = 1 for every column j,
    sum_j v_j = 0,

it proves

    sum_i |(Av)_i| <= (1 - card(I)*e) sum_j |v_j|.

No positivity assumption on e is needed for this inequality itself.
Strict contraction requires e>0 and a nonempty index set, along with
the displayed stochastic hypotheses. The proof subtracts e from
every matrix entry, uses the zero coordinate sum, and bounds the
remaining nonnegative matrix by its column sums. It does not assume
that all individual transfers strictly contract.

`N8.harmonic_constant` concerns a continuous real-valued function f
on an arbitrary topological space X and a nonempty compact subset S
containing a distinguished base point. For families of maps A_i,B_i
that preserve S, assume

    2 f(x) = f(A_i(x)) + f(B_i(x))     for every i and x in S.

Assume also that, from every x in S, there is a sequence of points
reachable by finite compositions of these maps which converges to
the base point. The conclusion is

    f(x) = f(base)                    for every x in S.

Reachability is defined inductively in the source. Its preservation
of a maximum is proved from the averaging equality and the two upper
bounds; it is not an added hypothesis. Compactness gives a maximum,
continuity identifies its value with f(base), and the same argument
applied to -f gives the minimum. The convergence of reachable points
is an explicit hypothesis, not a fact about arbitrary averaging maps.

## Connection to the concrete transfers

Here is a more quantitative written justification of that convergence
hypothesis for the transfers used in the general proof. This part is
**not formalized in the Lean file**.

Put l=m+1>=2. On R^l, T_i halves coordinate i and sends its other
half to coordinate i+1 modulo l. Each transfer is a nonnegative
column-stochastic matrix, preserves the zero-sum hyperplane H and
does not increase the l1 norm. The last claim follows from

    |a/2| + |b+a/2| <= |a| + |b|

on the two affected coordinates.

Let C=T_(l-1) ... T_1 T_0; the rightmost transfer acts first. Following
one unit of mass gives the complete formula for its columns:

    C_00 = 1/2 + 2^(-l),
    C_i0 = 2^(-(i+1))                      for 1<=i<l;

    C_0j = 2^(-(l-j))                      for 1<=j<l,
    C_ij = 0                              for 1<=i<j<l,
    C_ij = 2^(-(i-j+1))                    for 1<=j<=i<l.

For column j>0 the mass waits unchanged until step j, then retains
half at each successive coordinate; the final outgoing half returns
to coordinate zero after T_0 has already acted. For column zero,
the initial retained half and the final returning part add at zero.
This proves the formula for every l, without a finite-rank extrapolation.

Every entry of column zero and row zero of C is at least 2^(-l).
Consequently B=C^2 satisfies

    B_ij >= C_i0 C_0j >= 4^(-l)            for all i,j.

Two full cycles therefore suffice; the longer word used in the
original proof also works. Applying the formal contraction inequality
to the written B gives, on H,

    ||By||_1 <= q ||y||_1,
    q = 1-l/4^l,                          0<q<1.

Thus ||B^k y||_1 <= q^k ||y||_1 tends to zero. On every closed l1
ball in H, the points B^k y remain in the ball and are reachable by
the clockwise transfers. Such balls are compact because H is finite
dimensional. This supplies the reachability/convergence hypothesis of
the formal maximum principle. The other branch of each averaging
identity is the counterclockwise transfer, which also preserves the
same ball. When l=2 the two branches coincide, with no exception to
the argument.

The general proof derives those averaging identities from the
positional polynomial encoding and cyclic invariance. That derivation,
the use of real polynomial identities for rational Lie coefficients,
and the identification of every later column in the group-lifting
problem remain written arguments outside this formal check.

## Trust, failures and reproduction

Lean 4.24.0, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, ran with
`--trust=0` and Mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The checker verifies the
Mathlib revision. It uses the existing ignored S5 toolchain workspace
only as infrastructure; no S5 theorem or other experimental proof is
imported.

Both runs used one CPU, 8 decimal GB per process, a 120-second bound
and `LEAN_NUM_THREADS=1`, through the recorded runner:

| Run | Outcome |
| --- | --- |
| n8-averaging-lean-v1 | Failed in 5.34 seconds: `linarith` did not unfold the set-membership form of two maximum inequalities. The axiom audit rejected the resulting `sorryAx`. Exact first source and logs are retained. |
| n8-averaging-lean-v2 | Passed in 6.24 seconds after explicitly typing the two inequalities. Both principal theorems and both intermediate lemmas passed the transitive axiom audit; empty stderr and no warnings. |

The second source does not change a theorem's hypotheses or conclusion.
The permitted transitive axioms are exactly `propext`, `Classical.choice`
and `Quot.sound`; no `sorry`, new axiom or unchecked experimental
declaration is accepted. Earlier failed files remain evidence of a
failed run, not accepted formal proofs.

With the pinned Lean binaries on PATH and `LEAN_NUM_THREADS=1`, use a
fresh run name:

```sh
python3 scripts/run_recorded.py --name n8-averaging-lean-replay \
  --cores 1 --memory-gb 8 --timeout 120 \
  --expect 'PASS N8 stochastic contraction and harmonic maximum principle' \
  -- python3 scripts/check_n8_averaging_lean.py
```

On a separate machine the standalone file can be checked using
`lake env lean --trust=0` in the same Mathlib revision. The
[manifest](../../research/certificates/N8-averaging-lean/manifest-v1.json)
binds sources, this note, the controlling general proof and raw logs.
The checks strengthen two universal analytic ingredients. They do
not constitute independent specialist review or establish novelty.
