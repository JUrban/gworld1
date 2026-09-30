# N8: ordered words and the positional polynomial dictionary

30 September 2026, during the original experiment. This supplement connects
the [rational polynomial theorem](positional-polynomial-audit.md) to an
actual rational free associative algebra. It strengthens the formal support
for Section 5 of [the general proof](general-proof.md), without changing
the candidate count or establishing novelty.

## Exact setting and conclusion

Let `Words m` be finite rational linear combinations of ordered m-tuples of
natural numbers. A tuple `(i_0,...,i_(m-1))` represents the word
`E_(i_0)...E_(i_(m-1))`. The ambient algebra is Mathlib's monoid algebra
`MonoidAlgebra Q (FreeMonoid N)`. Its basis is ordered words, not commutative
monomials. The map `realize m` into this algebra is proved injective.

The positional encoding `encode m` is a rational linear equivalence from
`Words m` to polynomials in m commuting variables. It sends each word to
`X_0^i_0 ... X_(m-1)^i_(m-1)`. It is not an algebra homomorphism.

The file defines a global linear operator `assocDeriv` by the recursive
derivative rule on words. It proves the Leibniz identity and
`assocDeriv(E_i)=E_(i+1)`, and proves that its restriction to each word-length
component agrees with summing the increment of each tuple coordinate.
Under `encode`, this becomes multiplication by the sum of the positional
variables. Prefix and suffix insertion are proved to be actual left and
right multiplication by `E_j` in the ambient algebra.

For every natural m, let D have m letters and V have m+1 letters. The main
checked implication is

    delta(V) = E_0 D - D E_0,
    R(E_0 V - V E_0) = 0
        => D = c E_0^m for some rational c, and V = 0.

Here the equalities involving delta and products hold in the actual free
associative algebra. R is the existing explicit polynomial substitution
of `(a,Z_0,...,Z_(m-1),a)` with `a=-sum(Z_i)/2`, applied after positional
encoding. The conclusion includes m=0. There is no upper bound on m,
indices, degree, support size or rational coefficients.

Additional checked identities are

    R(delta(F)) = 0,
    R([E_j,F]) = a^j R([E_0,F]).

The derivation is injective on every positive word-length component;
injectivity on constants is not claimed. The proof that V vanishes uses
this injectivity after identifying D with a power of E_0.

## Scope and remaining steps

There are 39 new theorem declarations, with 58 unchanged analytic and
polynomial prerequisites. They form one dependent proof chain. The new
component is [Words.lean](../../research/certificates/N8-word-dictionary/Words.lean).
This supersedes the earlier audit's statement that the ordered-word
dictionary and its associative operations were entirely outside Lean.
The earlier files and their manifests remain unchanged.

The exclusion of nonzero powers `c E_0^m` from the Lie subalgebra when
`m != 1` is not proved in this component. Neither are the free-Lie
projection, the full correction-block application, complete leading-pair
enumeration, exact integral period lattices or the full terminating
nilpotent-group algorithm. No arbitrary-rank/class solver is supplied.

This is a check by the same research agent and a proof assistant, not an
external mathematical review. The original candidate's remaining
structural and bibliographic review requirements still apply.

## Verification record

All jobs use `scripts/run_recorded.py` sequentially, one CPU, 16 decimal
GB per-process memory, a 180-second timeout, and `LEAN_NUM_THREADS=1`.
Lean 4.24.0 revision `797c613eb9b6d4ec95db23e3e00af9ac6657f24b` and
Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` are pinned. Compilation
uses `--trust=0`. Each component audits the transitive axioms of its
declared theorems, allowing only `propext`, `Classical.choice` and
`Quot.sound`.

Each invocation saves its exact complete combined input and current word
component into fresh files. Earlier failed attempts remain available:

| Run | Result |
| --- | --- |
| `n8-word-dictionary-v1` | FAIL, 32.23 s: dependent tuple insertion, map coercions, finite-index injectivity arguments and word realization tactics needed correction. |
| `n8-word-dictionary-v2` | FAIL, 34.89 s: a list identity needed an explicit rewrite; a redundant tactic ran after its goal had closed. |
| `n8-word-dictionary-v3` | FAIL, 40.75 s: the extension to the global operator supplied one extra argument to a Mathlib lemma. |
| `n8-word-dictionary-v4` | FAIL, 47.96 s: the Leibniz proof needed scalar commutativity, and polynomial coefficient notation incorrectly required polynomial division. |
| `n8-word-dictionary-v5` | FAIL, 49.78 s: the last polynomial factorization needed explicit rational coefficient and polynomial types. |

| `n8-word-dictionary-v6` | PASS, 49.99 s: all 39 new declarations and unchanged prerequisites, empty stderr and no warnings. |

All six recorded PIDs were confirmed absent after termination, and the job
registry was empty. Exact component and combined-input hashes were checked
against each run header, and stdout/stderr against each terminal receipt.
The final input is [Combined-v6.lean](../../research/certificates/N8-word-dictionary/Combined-v6.lean).
File bindings are retained in [manifest-v1.json](../../research/certificates/N8-word-dictionary/manifest-v1.json).

To reproduce in a checkout with the pinned toolchain and Mathlib workspace,
choose a fresh snapshot path and run:

```sh
PATH=/project/gworld1/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH \
LEAN_NUM_THREADS=1 python3 scripts/run_recorded.py \
  --name n8-word-dictionary-replay --cores 1 --memory-gb 16 --timeout 180 \
  --expect 'PASS N8 ordered-word positional dictionary' -- \
  python3 scripts/check_n8_word_dictionary.py \
  --snapshot research/certificates/N8-word-dictionary/Combined-replay.lean
```

This command concatenates the retained components after hoisting their
imports. It does not fetch dependencies or overwrite earlier snapshots.
