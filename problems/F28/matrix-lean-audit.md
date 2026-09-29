# F28: formal verification of the integral matrix obstruction

29 September 2026, approximately 03:49–04:03 UTC. Same whole-entry
candidate, with no increase in counts or claim of established novelty.

## Exact theorem and relation to the problem

The final Lean declaration is `F28.integral_orbit_is_scalar` in
[MatrixLemma.lean](../../research/certificates/F28-matrix-lean/MatrixLemma.lean).
Here `Mat` is exactly `Matrix (Fin 2) (Fin 2) ℤ`, and
`Q=!![0,-1;2,1]`. Its hypotheses and conclusion are:

    orbit : ℕ → Mat
    det(orbit 0) = 1
    ∀ n, orbit(n+1) * Q = Q * orbit(n)
    ---------------------------------
    orbit 0 = I or orbit 0 = -I.

There is no boundedness, periodicity, computability, finite-range or
finite-generation hypothesis. Only the initial determinant is assumed.
The all-exponent centralizer lemma is also separately exposed as
`F28.determinant_one_periodic_is_scalar`.

For the written F28 proof, choose the exact rational conjugates
M_n=Q^n M Q^(-n). An invariant subgroup makes all these matrices
integral, because their determinant-one projective classes are represented
by integral matrices and differ only by sign. The formal theorem then
forces M=±I. The free-group Schreier bases, ping-pong faithfulness,
three defining generator identities, projective sign interpretation and
this bridge from subgroups to matrix sequences are **not formalized**.
Their written proof and earlier GAP/exact checks remain necessary.

## Elementary proof refinement

The positive energy is

    E([[a,b],[c,d]]) = (8a-4b+2c-d)^2
                       +7(4b+d)^2+7(2c-d)^2+49d^2.

Lean proves its invariance under NQ=QM, and bounds every matrix entry
between -E and E. The elementary inequality |t|<=t² for integers
bounds each linear form; they recover all entries. Finite integer
intervals and the pigeonhole principle give repeated terms. Injectivity
of left multiplication by Q propagates repetition back to time zero.
Induction then turns the return into commutation with a positive power
of Q.

The recurrence (u,v) -> (u+v,-2u), starting at (0,1), gives
Q^n=u_n Q+v_n I. For every positive n, u_n is odd, so never zero.
Commutation with Q^n therefore gives the same two entry relations as
commutation with Q. The determinant-one equation becomes
(2a-b)^2+7b²=4, forcing b=c=0 and a=d=±1.

The earlier SymPy probe derived the unscaled invariant
tr(adj(P) M^t P M), with P=[[4,1],[1,2]], and its exact LDL
decomposition. E is eight times that form. The probe's original source
is retained as `energy-probe.py` beside the Lean source, with its original
recorded output in `results/f28-energy-identity-v1`. It printed a zero
invariance difference; it was a derivation aid, not the formal proof.

## Verification record

All five exact Lean sources are retained in `versions/`, with the final
source equal byte-for-byte to v5. Runs used four cores, 8 decimal GB per
process and a 120-second timeout through the recorded runner.

| Run | Outcome |
|---|---|
| v1 | Failed before checking: obsolete Matrix.Notation import path. |
| v2 | All-exponent centralizer theorem passed; two unused-simp warnings. |
| v3 | Energy/orbit extension failed on reserved identifier `repeat`; axiom audit rejected the resulting `sorryAx`. |
| v4 | Failed on a looping rewrite `k=(k-1)+1`; axiom audit again rejected `sorryAx`. |
| v5 | Full orbit theorem and transitive axiom audit passed in 8.848 seconds; no warnings, empty stderr. |

No failed run is counted as verification. Both final theorems report only
`propext`, `Classical.choice` and `Quot.sound`. The source contains no
`sorry`, `admit`, new axiom, or external S5 theorem dependency. The source
hashes, original logs and process records are preserved in the certificate
manifest. No larger finite word sample was substituted for the theorem.

## Toolchain, reproduction and limits

Lean 4.24.0 reports commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. Mathlib is pinned to
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The existing ignored
`scratch/S5-Achxy-k-5-38` workspace supplies only Lean/Mathlib/dependency
infrastructure; none of its mathematical project modules is imported.
The toolchain, dependency pins and archive digest were checked in
[the S5 environment audit](../../research/notes/S5-prior-Lean-proof-audit.md).

To reproduce here, place the pinned Lean binaries on PATH, then run:

```sh
python3 scripts/run_recorded.py --name f28-matrix-lean-replay \
  --cores 4 --memory-gb 8 --timeout 120 \
  --expect 'PASS F28 all-exponent integer matrix lemma and axiom audit' \
  -- python3 scripts/check_f28_matrix_lean.py
```

For a separate machine, the source can be passed to `lake env lean`
inside a Mathlib workspace at the specified revision with its pinned
Lean toolchain and dependencies. The full source and proof are retained;
large toolchains and cached library artifacts are not committed.

The run used `--trust=0`, but this is **not** evidence that every cached
Mathlib artifact was rebuilt or independently rechecked. The pinned Lean
importer installs cached constant maps; the trusted environment boundary
from the S5 audit applies here too. Lean checks the new source and the
transitive axiom dependency audit rejects unapproved axioms. This is
formal verification in that environment, not an independent implementation
of the kernel or a complete formalization of the original group problem.

The full original free-group HTML and F28/GA5 background were reread;
`research/statement-audits/F28/statement.png` was actually viewed again.
The original all-subgroup quantifier is preserved. No new external
literature or novelty claim is needed for this elementary refinement.
