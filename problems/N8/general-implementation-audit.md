# N8: complete integral recursion in the group model

30 September 2026, during the original run. The general algorithm of
[the candidate proof](general-proof.md), including its
[group-block interface](group-block-supplement.md), is now connected in
`scripts/n8_general_solver.py` for integral Magnus group inputs in arbitrary
finite rank at least two and class at least two. This implements the existing
candidate; it is not another result or a changed novelty assessment. A public
word-input command and the elementary rank/class boundary cases remain to be
packaged. The structural proof still requires specialist review.

## Algorithm and completeness dependencies

The solver enumerates every normalized leading weight type and the complete
projective/signed-divisor or exterior/Hermite lists. It works in actual Hall
group coordinates. At each zero-kernel layer it solves the full integer
equation. Once the remaining tail is jointly linear, it solves that entire
integer system, retaining all intermediate freedoms.

At a universal layer it uses a full integer kernel basis and one exact period
in each direction. Every residue in the resulting finite-index period lattice
is considered. The Nielsen period retains the content of the second leading
factor. Other periods use the existing weighted symplectic-expansion and
coefficient-clearing construction from `check_n8_delayed_gauges.py`, now in
`n8_exact_universal_periods.py`. An integral power one is accepted only after
forward/inverse and commutator checks. Otherwise every coefficient of the
finite Hall-coordinate polynomial is cleared, using the proved degree bound
floor(c/s). There is no bounded factorial search in this decision path.

At a pre-Nielsen exceptional offset s, the solver solves the whole affine
block through 2s-1 and uses an integral unimodular change of its full parameter
lattice. It preserves the possibly nonunit first-parameter step. The next
error is projected against every later block and fresh-layer column. The
nonzero scalar quadratic has all its integer roots enumerated exactly.
Only the prefix through s is then fixed before restarting. Assertions reject
a failure of the written kernel/separation hypotheses; such failure is not
reported as a negative decision.

Every positive answer is checked against the full original Magnus target.
A negative answer requires exhaustion of every normalized branch. Timeouts,
resource errors and interrupted traces are incomplete runs, never negatives.
Finite checks cannot prove the general projective-finiteness, universal-period,
free-Lie kernel or full-block separation arguments. Those remain dependencies
of the written general proof, with its cited structural theorems.

## Controls and separate native reconstruction

The initial eight integration controls and two period controls passed. The
expanded suite has ten core controls, one delayed-exception control and one
negative-quadratic control: nine positive and three negative decisions.

Controls cover the identity and abelianization boundaries; a central target;
the earlier scale-sensitive class-five example whose primitive branches fail;
equal leading weights; nonprimitive Nielsen and universal periods; a rank-three
target; a rank-four nondecomposable exterior target; and a genuine exceptional
quadratic at class seven. The delayed example is in rank two and class ten:
U=[b,[b,a]], D=[a,[a,U]], g=[a U^2,D]. Its first exceptional offset is two.
These are finite interface controls, not a verification of all ranks/classes.

The class-seven negative control perturbs the positive target by a central
Hall generator. For its first normalized branch the obstruction changes from
(3T-T^2)/2 to (1+3T-T^2)/2, with discriminant 13. Both leading branches are
rejected, and the other leading weight type has no pair. The full trace is
retained; rejection of just one planted branch would not decide the target.

The standalone fractional universal-direction control requires period 72;
the other uses period one. GAP/nq independently constructs their weighted
nilpotent presentations and verifies both automorphisms, all eight inverse
compositions, exact commutator preservation and two wrong-Nielsen controls.

For the twelve integrated group controls, a separate GAP/nq checker constructs
native free nilpotent groups from the rank and class. It reconstructs all nine
positive witnesses from compact Hall coordinates, 287 actual group correction
columns in 16 affine blocks, and their right-hand sides. Native subgroup
membership reproduces positive and negative integer lift decisions without
using the Python integer solver. It also checks four exceptional quadratics
at six integer parameters each, every projected later column, the separating
functionals, the exact scalar coefficients and complete integer root lists.
The original negative exterior/abelian cases and projective leading-list
completeness rely on their existing arguments and audits, not this GAP replay.
This is a same-agent implementation audit with a separate computational
representation, not outside mathematical review.

## Execution and preserved versions

Eight recorded jobs passed, each requesting one CPU and eight decimal GB.
Maximum overlapping reservations were three CPUs and 24 GB. The longest was
the expanded delayed control, 6.692 seconds; the native integrated replay took
4.082 seconds. All stderr files are empty. Receipt log hashes were checked and
all recorded PIDs were absent after completion. Read-only process closure
observed 719 terminal receipts, an empty job registry and no remaining workers
in its stated scope. This is a checkpoint, not the deadline freeze.

The initial and expanded source versions are preserved in `inputs-v1` and
`inputs-v2`. Before native replay, the generic export helper was found to emit
Python `None` instead of GAP `fail`. The original exports remain unchanged;
`fixtures-native.g` was generated from the saved exact JSON, and the checker
now exports `fail` correctly. No mathematical computation had failed or was
rerun for this formatting correction. To regenerate a native fixture, call
`gap_native` from the checker on its saved JSON; all mathematical jobs use fresh
output paths. The earlier core/delayed reruns added group-prefix certificates
and the missing nonprimitive-period controls, rather than repeating unchanged
tests merely for volume.

The source page and N8 paragraph were reread and the retained original-statement
rendering was viewed. The archive still asks about every finitely generated
free nilpotent group in part (b); part (a)'s general class-two negative answer
remains explicitly prior. No new source or novelty conclusion is asserted.
Exact commands, inputs, outputs and source hashes are bound in
`research/certificates/N8-general-solver/manifest-v1.json`.
