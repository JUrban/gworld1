# Rank-two class-seven extension: audit and reproducibility

28 September 2026, approximately 14:27–14:47 UTC. Candidate proof in
`class7-rank2-proof.md`; no external review or established novelty.
This expands the existing N8(b) partial candidate and adds no entry
to the candidate count.

## Statement and scope

The complete original nilpotent page, exact N8 fragment and its rendered
paragraph were inspected earlier in the run; evidence remains in
`research/statement-audits/N8/`. Part (a) is separate and has a prior
negative answer. Part (b) quantifies over every finitely generated free
nilpotent group. The new result here covers **rank two, class seven**.
Together with preceding notes, the counted candidate scope is all
targets in classes three through six in every finite rank; all targets
in class seven in rank two; and the previously stated degree-two and
penultimate/central target strata in every class and finite rank.

## Proof checks

- The new (2,3) kernel uses a displayed four-column tensor minor of
  determinant -1. This is a complete rank-two linear-algebra proof.
  GAP separately confirms rank four using its own class-six quotient.
- The (1,4) kernel injects into L2, so has dimension at most one in
  rank two. No conclusion about arbitrary rank is taken from samples.
- Nielsen normalization uses the exact move x->yx, with y fixed.
  The initial exploratory lead's shorthand x->xy was wrong for the
  convention `[x,y]=x^-1*y^-1*x*y`; it is corrected explicitly in that
  note. The implemented normalization and this proof use x->yx.
- Simultaneous tail matching retains all degree-six freedom through
  degree seven. Integer Smith calculations decide the whole remaining
  affine lattice, rather than choosing a single degree-six solution.
- Degree counting bounds the one-parameter residual by a quadratic.
  Integral Newton coefficients avoid a hidden division-by-two error.
  Period 2 times the torsion exponent handles even moduli and negative
  parameter values. If any free-coordinate polynomial is nonzero,
  only its actual integer roots are candidates.
- All accepted words are rechecked in the original truncated group.
  Shortening a Smith particular solution subtracts an integer kernel
  combination, preserving the exact solution set.

## Computation and independent checks

All runs used one CPU slot and a 4 GB process memory limit. Arithmetic
is integral or exact rational; there are no floating-point decisions.
GAP 4.16.1/nq 2.5.11 supplies an independent polycyclic representation.
Python uses the existing Hall/Magnus code and SymPy 1.14 normal forms.

`n8-class7-kernel-probe-v1` (2.08 seconds, seed 9282620) records 51
bounded kernel examples in ranks two and three. It motivated the
argument but does not prove a general rank bound.

`n8-class7-rank2-checks-v2` (94.23 seconds, seed 9282621) passed:

- 67 target decisions, including 39 positive witnesses and 28 negatives;
- 20 constructed positives across factor weights and nonprimitive scales;
- nine positives in the nonzero (1,4) kernel direction;
- 24 perturbed middle-layer targets, 21 rejected;
- ten central perturbations in the quadratic direction, five rejected;
- four boundary/delegation cases;
- 196 exact linear lifting decisions and 32 quadratic branches;
- eight arithmetic controls for free equalities, nonintegral roots,
  torsion congruences, Newton coefficients and a zero lattice.

The group quadratic branches in this suite all have a nonzero free
equation; the finite-residue alternative is exercised by the arithmetic
controls. Selected quadratic parameters include -2,-1,0,1. Two
positive group cases require nonzero Nielsen residues modulo three,
so keeping only one arbitrary affine representative would fail.

`n8-class7-rank2-gap-v1` (6.48 seconds) independently verified all
39 witnesses, all 196 linear subgroup-membership decisions (89
negative), and all 40 arithmetic certificates (22 negative). It
checks the supplied Smith transformations by matrix multiplication
and unimodular determinants, recomputes integer roots or the residue
period, and checks every resulting congruence. For all 32 group
quadratic branches it checks the actual parameterized factors,
residual polynomial and fixed tail lattice at six parameters
(-2,-1,0,1,2,3): 192 sample checks. These samples support the separate
degree-count proof; they do not replace it. It also verifies the
degree-six rank-four injection in its own quotient representation.

The GAP run completed with one harmless parse-time warning about the
global S used by a lambda expression; S is assigned before that
expression is evaluated. The warning and all raw terminal bytes are
preserved. Python v2 and the kernel probe have empty stderr.

Commands:

```sh
python3 scripts/run_recorded.py --name n8-class7-rank2-checks-v2 \
  --cores 1 --memory-gb 4 --timeout 180 --expect 'PASS N8 rank2 class7' \
  -- .venv/bin/python scripts/check_n8_class7_rank2.py
python3 scripts/export_n8_class7_gap.py
python3 scripts/run_recorded.py --name n8-class7-rank2-gap-v1 \
  --cores 1 --memory-gb 4 --timeout 180 --expect 'PASS N8 class7 GAP' \
  -- bin/gap -q --quitonbreak scripts/check_n8_class7_gap.g
```

The generator refuses to overwrite an existing checks file; regenerate
in a separate work copy and use fresh run names. The recorded
`n8-class7-hall-export-v1` command supplies `hall7.json` for the GAP
export; its complete one-line command is in `process.json`.

Certificates are under `research/certificates/N8-class7/`. Each run's
`process.json` records the exact command, resource bounds and raw log
hashes. The current Python implementation is `scripts/n8_class7_rank2.py`;
the GAP verifier is `scripts/check_n8_class7_gap.g`.

## Preserved failure

`n8-class7-rank2-checks-v1` failed after 6.49 seconds. A valid Smith
particular solution had enormous coefficients, and expanding a
witness into a Python list raised `OverflowError`. The mathematical
commutator check had already succeeded; the failure was witness
representation, not a negative target decision. The exact failed
scripts and partial certificates are retained in `failed-v1/`, with
the original stdout/stderr in the run directory. The fix uses exact
LLL and nearest-plane subtraction of kernel vectors to shorten a
particular solution before expanding it. No failed record was erased.

## Bibliographic limits

The earlier primary Roman'kov survey and cited Hall/IA material remain
the background. Additional searches on 28 September for “commutator
free nilpotent class seven”, “commutator problem nilpotent decidability”,
and “single commutator nilpotent algorithm” found no matching theorem.
Results about operator commutators, arbitrary class-two nilpotent
groups or systems of equations do not decide this free-group case.
This is a targeted search, not proof of novelty. No Kourovka argument
or code was imported.
