# Audit of the fourth-from-last extension

29 September2026, completed06:13UTC. This is an internal proof audit with
independent software checks, not specialist review or a novelty certification.
The scope below is promoted within the existing partial candidate.

## Scope and completeness concerns

The proposed scope is exact leading degree c-3 in every finite rank,
for c>=7. Combined with the earlier deepest layers, it gives gamma_(c-3).
The original all-target results for classes3--10 remain available.
Other lower leading layers in arbitrary class are unresolved, so this
is an extension of the same partial N8(b) candidate.

The complete original N8 HTML, linked background and actual statement
rendering were checked during this derivation. Part(a)'s arbitrary
nilpotent class-two group question remains separate. The commutator
convention throughout is x^-1 y^-1 x y.

The first-map theorem is used in the quotient of class c-1. Its quadratic
obstruction restricts first parameters; it does not pretend the full
class-c residual has degree two. Equal leading weights give a zero
first kernel, and adjacent weights give an exact Nielsen line with
every residue modulo content(D) retained. The complete leading-pair
enumeration and its normalized signed scales are unchanged.

After a first parameter is fixed, the entire offset-two and offset-three
tail is solved jointly over the integers. Its cross interactions have
weight at least p+q+4>c, and repeated corrections on one side have still
larger weight. Fixed lower corrections remain in the actual columns.
The residual subgroup is additive in this range. These weight arguments
give the uniform theorem; no bounded computation proves all ranks.

A rank-two/class-eleven control demonstrates why choosing one particular
second-layer solution is insufficient. Let C be the first Hall word of
weight3, R the last of weight5, and y=R^3 times the first Hall word of
weight6. The target is [C*R,y]. Relative to the fixed pair (C,y), the
offset-two affine kernel has dimension1. The chosen shortened particular
solution does not lift using offset-three corrections alone; the joint
offset-two/three system does. Its positive witness and all three integer
decisions are included in the independent GAP replay.

The imported homogeneous free-basis and inner-solution theorems keep
their Bryant--Kovacs--Stohr, Remeslennikov--Stohr and Altassan credits,
as detailed in `third-layer-proof.md`. No new external mathematical
source or Kourovka argument was imported for this extension.

## Completed group checks

The class-eleven suite covers types(3,5),(4,4), and an exceptional type(1,7)
whose D has two occurrences of the weight-two correction direction.
It includes signed nonprimitive leading scales, perturbed negative
targets, the joint-tail control above, and unsupported identity/degree-one
inputs. The class-ten suite covers types(2,5),(3,4),(1,6), including
nonprimitive Nielsen periods. Unsupported inputs return None, never False.

Final rank-two certificates use the v2 directories. GAP reconstructs
group commutators, integral membership decisions, first-map nullities,
Nielsen periods and polynomial roots/congruences independently. It does
not independently enumerate all possible leading pairs; their complete
enumeration remains a proof dependency.

| Suite | Python targets | GAP witnesses | Integer decisions (negative) | Polynomials (empty) | Samples | First nullities | Nielsen periods |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rank2/class11 v2 |15|8|39(11)|6(2)|30|18|0|
| Rank2/class10 v2 |15|6|61(33)|6(2)|30|22|10|
| Rank3/class8 v4 |11|4|48(28)|6(2)|30|16|10|

Python times were58.920 and19.283seconds; GAP times19.284 and6.793seconds.
Rank-three Python completed in200.331seconds and GAP in42.813seconds.
It covers types(2,3),(1,4), signed nonprimitive leading coefficients,
both obstruction layers, positive corrected factors and unsupported inputs.
Across these three suites there are41 target records:18 positive,
17 negative and6 unsupported. GAP checks18 witnesses,148 integer decisions
(72 negative),18 polynomial certificates(6 empty),90 parameter samples,
56 first-map nullities and20 Nielsen periods.

All six final jobs have actual exit0, their required markers and empty
stderr. The preceding v1 rank-two Python runs also completed; their
artifacts and original tail implementation are retained separately.

## Runtime failures and exact arithmetic changes

Three rank-three/class-eight Python attempts hit their180second wall
limits. They have actual returncode-9, no success marker and empty stderr;
their completed prefixes and exact executed sources are retained. These
are incomplete suites, not negative mathematical answers. Input words and
expected answers were not weakened between attempts.

The initial tail used ordinary integer Hermite reduction. The next
version used the already verified support-component reduction. A further
version replaced rational nearest-plane shortening by an exact FLINT
Gram-data implementation. Forty-two deterministic comparisons, seed9292801,
agree exactly with the earlier SymPy routine; the new routine explicitly
verifies the integer kernel change. That comparison passed in0.771seconds.

A saved thirty-second diagnostic profile instead identifies Hermite
reduction as the dominant remaining cost:32.776 of38.499 profiled seconds
were in the affine solver,32.586 within its Hermite routine. The diagnostic
alarm waited through a native call. It is deliberately not a completed
decision. The earlier tentative attribution to particular-solution
shortening was not supported by this profile, and the shortening change
is not claimed to have fixed the runtime. The unchanged rank-three suite
was then given a bounded900second allowance in v4 and completed, followed
by its successful GAP replay. The larger allowance, rather than a claimed
algorithmic speedup, enabled this suite to finish.

## Related structural lead and limitations

`research/notes/N8-general-offset-lead.md` extends the kernel/obstruction
argument to arbitrary pre-Nielsen offsets and proves that the next kernel
is zero. Independent Python/GAP weighted-Lie checks cover six kernels and
their successors, with five nonzero quadratic obstructions and an explicit
post-Nielsen dimension-three control. Those are separate structural checks,
not a completed fifth/sixth-layer group solver. No such scope is promoted.

All computations use exact integer/rational arithmetic and recorded
resource limits. Each mathematical job reserves one CPU and8GB.
Outside specialist review, matching-theorem literature review and all
arbitrary-class lower layers remain outstanding. Counts remain six whole
candidates, three partial candidates and zero established novel results.

## Reproduction

Final certificates are under `research/certificates/N8-fourth-layer-`
with suffixes `r2-c11-v2`, `r2-c10-v2` and `r3-c8-v4`. Exact executed
Python versions, GAP sources, fixtures and SHA-256 manifests are retained.
The rank-two versions intentionally retain the earlier nearest-plane
import actually used in those runs. Recorded commands and process outcomes
are in `results/n8-fourth-layer-*`; the common live driver accepts a new
output directory and refuses to overwrite an existing checks.json.
The GAP frontend names the appropriate final certificate directory.

The three timed-out prefixes, two earlier successful rank-two runs,
diagnostic profile, general-offset controls and nearest-plane comparison
also have separate manifests and source snapshots. The latter comparison
preserves the tested source; the general-offset driver's later edit only
corrects its docstring, and the pre-edit executed version remains included.
No oversized omitted artifact is needed. Raw GAP log whitespace and the
profiler's terminal blank lines are kept to preserve the recorded hashes;
source/document whitespace checks exclude those exact raw outputs.
No subagents, contacts, push or new
Kourovka transfer occurred; the original deadline and frozen inputs remain.
