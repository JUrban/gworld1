# Audit of the fifth/sixth-layer extension

29 September 2026, completed around 07:01 UTC, before the original deadline.
The candidate proof is `fifth-sixth-layer-proof.md`. This is a scope extension
of the existing partial N8(b) candidate, with no new problem count and no
established novelty or specialist validation.

## Scope and implementation

`scripts/n8_fifth_sixth_layer.py` accepts exactly nonidentity targets with
leading degree d>=4 and c-d in {4,5}, in rank at least two. It returns
`answer=None` outside that stratum. Ranks zero/one and identity targets are
handled by the surrounding earlier theory, not asserted as negative here.
Together with the previous four layers this covers gamma_(c-5), c>=9.
The existing all-target classes three through ten remain included.

Every normalized leading pair is enumerated by the existing exact Hall
machinery. The first correction retains all permissible quadratic roots
or all Nielsen residues. Each second system is then solved afresh. An
exceptional second line is coupled with the injective third correction;
the complete integer affine point/line is retained. Its nonzero parameter
step is never rounded or replaced by one. All offsets remaining after a
finite normalization are kept in one joint tail. Positive factors are
verified by exact Magnus multiplication.

The structural lemmas and their bounded independent weighted-Lie checks
were already retained in `../../research/notes/N8-general-offset-lead.md`
and `research/certificates/N8-general-offsets/`. Those checks include
decomposable directions and offsets beyond one; they are not a substitute
for the uniform proof. The present work supplies the previously missing
group implementation, exact coupled lifting and independent replay.

## Completed recorded suites

| Certificate directory under `research/certificates/` | Python seconds | GAP seconds | Final target records |
|---|---:|---:|---:|
| `N8-fifth-sixth-r2-c11-v1` | 121.684 | 37.898 | 30 |
| `N8-fifth-sixth-r2-c12-v1` | 419.826 | 380.732 | 34 |
| `N8-fifth-sixth-r3-c8-v2` | 126.600 | 21.843 | 11 |
| `N8-coupled-lifts-v1` | 73.518 | 20.539 | 6 |
| `N8-coupled-nonunit-v1` | 76.721 | 10.756 | 1 |

All ten final mathematical jobs exited zero, had empty stderr, completed
inside their recorded limits, and produced the expected final marker.
The complete results were inspected, not inferred from the marker alone.
All used one core and at most 16 GB per process under `run_recorded.py`;
at most three mathematical jobs were running together.

The 82 final target records comprise **44 positive, 32 negative, and six
outside-scope controls**. Independent GAP checks total:

* 44 complete word witnesses;
* 424 integral linear decisions, including 153 negative decisions;
* 227 first/second correction nullities;
* 40 complete Nielsen periods;
* 25 coupled systems: eight empty, six isolated points, eleven lines;
* three lines with nonunit projected parameter step (all step 6);
* 27 quadratic certificates, eleven late and eight with no integral
  parameter, together with 135 independently recomputed group samples.

The tested leading types include equal weights, both Nielsen offsets,
generic injective maps, first exceptional kernels and second exceptional
kernels, at both new depths. Leading coefficients include signs and
nonprimitive scales. The rank-three/class-eight suite checks the d=4
boundary. Its class-eight scope overlaps the older all-target theorem;
its purpose is to test the new generic dispatch and boundary cases.
Full-group tests at arbitrarily large ranks/weights are not claimed.

## Independent replay

`export_n8_fifth_sixth_gap.py` only serializes retained records. The GAP
checker constructs free nilpotent quotients independently using `nq`.
The common group/Hermite prefix comes from the already audited class-ten
checker; the added code uses general p,q and correction offsets.

GAP evaluates the actual words, recomputes group correction increments,
and decides their integral membership in an independently constructed
polycyclic abelian tail. It checks the full correction nullities, primitive
one-dimensional kernels, affine particular solutions and exact Nielsen
periods. For each coupled system it independently checks A_3 injectivity,
all exported residual samples and full integer solvability. A primitive
kernel with the correct nullity certifies the whole integral line.

For each quadratic, GAP verifies the unimodular Hermite transformation,
the entire rational cokernel reduction, all integral congruences and the
complete integer root list. It recomputes the underlying group residuals
and correction columns; these are not accepted merely as Python matrices.
For late quadratics it also matches and verifies the preceding coupled
line. Such bounded independent checks support the implementation; the
uniform statements still depend on the written mathematics and imports.

## Controls and preserved failure

The first rank-three suite, `n8-fifth-sixth-r3-c8-v1`, exited one after
125.041 seconds because an assertion required at least one negative
target, but every chosen perturbation had a positive witness. No algorithm
assertion failed. The full records, source copies, logs and process record
are preserved. No positive fixture was removed or relabeled as negative.

The final suite retains those inputs and adds a mathematically motivated
negative control. Its leading term has only equal-weight (2,2) pairs,
but its added top iterated adjoint has nonzero metabelian image. A
commutator of two gamma_2 elements cannot have that image. The algorithm
rejects it and GAP independently verifies the failed integral branch.
GAP also verifies all eight positive witnesses from the original suite.

The six targeted corrected examples force isolated coupled points, so
the line-only path is not the only one exercised. The final single
control uses z=a, T=[b,a], U=[a,T], D=[a,[a,U]], with input factors

    x=a^2 U^2,
    y=D^3 [a,D] H,

where H is the last Hall word of weight nine in the stored basis. The
exact input is retained in `checks.json`. Across its normalized leading
branches, the derivative first correction gives three coupled lines
whose projected parameter step is 6. Two corresponding quadratic systems
are empty and the third yields a verified solution. This directly checks
that nonunit integral steps are retained without admitting extra parameters.

No new suite produced two distinct integral quadratic roots; the verifier
nevertheless checks completeness of each exported root list, and the
uniform proof treats every possible root. No claim of exhaustive test
coverage is made. The preliminary shell command `python ...` did not
launch because only the repository `.venv/bin/python` exists; it produced
no mathematical run or output directory.

## Reproduction and integrity

Each directory retains `checks.json`, the full compressed audit,
Hall words, witnesses, GAP fixtures, its `check.g` driver and exact source
versions. A manifest records SHA256 hashes and corresponding process
records under `results/`. Each process record contains the actual command,
resource reservation, exit code, elapsed time and raw output hashes.
Regenerate into a new directory using the recorded Python command, run
the exporter, and invoke its GAP driver through `run_recorded.py`.
Do not overwrite the retained evidence. The targeted nonunit run uses
`--case nonunit`; the other targeted suite uses the default point controls.

The original N8 full HTML/background were reread and its actual captured
statement viewed. The prior class-two theorem does not settle these
classes. The attribution and remaining lower-layer limitation in the
proof are essential. No Kourovka transfer, full N8 resolution, new count,
practical complexity bound or established novelty is asserted.
