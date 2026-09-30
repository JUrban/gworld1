# N8: rational positional polynomials checked in Lean

30 September 2026, during the closing audit. This extends the
[analytic assembly](analytic-assembly-audit.md) from real-valued functions
to actual multivariate polynomials over Q, with an explicit diagonal
substitution. It checks an additional interface in Section 5 of
[the general argument](general-proof.md). The full N8 theorem and
algorithm remain outside the formalization.

## Exact theorem

For every natural m, let P be a rational polynomial in m variables and
V one in m+1 variables. Define

    delta(V) = (X_0 + ... + X_m) V,
    bracket0(P) = P(X_1,...,X_m) - P(X_0,...,X_(m-1)).

For a polynomial Q in m+2 variables define its restriction by substituting

    (X_0,...,X_(m+1)) = (a,Z_0,...,Z_(m-1),a),
    a = -(Z_0+...+Z_(m-1))/2.

The theorem `N8Polynomial.rational_diagonal_constant` proves

    delta(V) = bracket0(P) and restriction(bracket0(V)) = 0
        imply P = constantCoeff(P).

The conclusion is an equality of rational coefficient polynomials, not
just agreement on a selected set of points. There is no bound on degree,
number of monomials, or finite dimension. The m=0 boundary is included.
Definitions use Mathlib's `MvPolynomial`, variable renaming, and polynomial
evaluation; the two hypotheses are polynomial equalities.

## Connection to the existing analytic proof

Evaluation of `delta` gives multiplication by the coordinate sum.
Evaluation of `bracket0` gives the difference between tail and initial
tuple evaluations. These facts instantiate the earlier functional
identities directly. Polynomial evaluation is continuous. The previous
maximum principle therefore gives a constant real-valued function;
polynomial extensionality over R and injectivity of Q into R give
equality of the original rational polynomials.

The new restriction is a polynomial substitution over Q. The proof
checks its evaluation after embedding coefficients into R and proves
that **every** real tuple of sum zero with equal first and last entries
has this form. Thus a zero restricted polynomial supplies exactly the
diagonal functional hypothesis used in the analytic theorem. This step
does not assume a density or generic-point assertion, or divide by a
possibly zero coordinate; the only denominator is the constant two.

There are thirteen new checked theorem declarations and forty-five
unchanged declarations in the prerequisite bridge, energy proof, and
analytic assembly. They form one proof chain, not separate independent
validations. The final complete input is
[Combined-v4.lean](../../research/certificates/N8-positional-polynomials/Combined-v4.lean);
the new component alone is
[Polynomial.lean](../../research/certificates/N8-positional-polynomials/Polynomial.lean).

## Remaining boundary

For the intended application, a word E_(i1)...E_(im) in the free
associative algebra corresponds to the positional monomial
Z_1^i1...Z_m^im. The derivation E_i -> E_(i+1) becomes `delta`, and
the bracket with E_0 becomes `bracket0`. This linear coefficient
identification and its compatibility with the free-associative operations
remain written mathematics; this file does not formally construct a free
associative or free Lie algebra.

The exclusion of a nonzero constant encoding in a free-Lie component
with more than one E letter, the homogeneous subalgebra projection, the
full correction-block application, the complete leading-pair algorithm,
integral period lattices and terminating group recursion also remain
outside this check. The other formal supplements have their own stated
boundaries. No general solver has been implemented by this addition.

The earlier analytic audit's statement that polynomial continuity and
the return from functional constancy to rational coefficient constancy
were unformalized is superseded by this supplement. Its source and
manifest remain unchanged. There is no result-count or novelty change.

## Verification and reproduction

All four runs were sequential through `scripts/run_recorded.py`, with
one CPU, 16 decimal GB per-process memory, a 180-second timeout, and
`LEAN_NUM_THREADS=1`. Lean 4.24.0 revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b` and Mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` were pinned. Checks use
`--trust=0` and reject every transitive axiom outside `propext`,
`Classical.choice`, and `Quot.sound`.

| Run | Result |
| --- | --- |
| `n8-positional-polynomials-v1` | FAIL, 22.39 s: simplification did not identify the explicit tail/init functions. Axiom audit also rejects the resulting incomplete proof. |
| `n8-positional-polynomials-v2` | PASS, 23.60 s: eight-theorem polynomial interface with a diagonal evaluation hypothesis; empty stderr and no warnings. |
| `n8-positional-polynomials-v3` | FAIL, 26.16 s: extension used the wrong evaluation-composition lemma name and a rewrite changed both endpoint occurrences. Exact source and logs retained. |
| `n8-positional-polynomials-v4` | PASS, 27.16 s: all thirteen new theorems, including explicit restriction and rational coefficient conclusion; empty stderr and no warnings. |

Each run writes its entire combined input to a fresh non-overwritable
file. Exact earlier component versions are recovered from those inputs
and checked against the hashes printed by their own run. The final
snapshot SHA-256 is
`613f55c7179efa5e7bff4fb35f02cb0fa4255c115bae0f73ccc4a32025b7598d`.
No earlier finite Lie/group suite was rerun. All four processes have
terminal receipts and the process registry is empty.

With the pinned toolchain and Mathlib checkout, use a fresh name and
snapshot path:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name n8-positional-polynomials-replay --cores 1 --memory-gb 16 \
  --timeout 180 --expect 'PASS N8 rational positional polynomial constancy' \
  -- python3 scripts/check_n8_positional_polynomials.py \
     --snapshot scratch/N8-positional-polynomials-replay.lean
```

Alternatively check the standalone combined input with
`lake env lean --trust=0` in the pinned Mathlib environment. The manifest
binds this audit, source versions, prerequisite files, current general
proof and all four process records and logs. This remains same-agent
work; no independent mathematical referee or novelty validation occurred.
