# Audit of the all-target class-ten candidate

28 September 2026, before the original deadline. The argument is in
[class10-proof.md](class10-proof.md). This is internal mathematical review
and independent software checking, not outside specialist validation.

## Scope and statement fidelity

Re-read the frozen N8 HTML and viewed its existing screenshot again around
23:31 UTC. Only part (a), concerning arbitrary class-two groups, is starred.
Part (b) asks about all finitely generated free nilpotent groups. The new
proof covers all targets in class ten, in every finite rank, extending
classes three through nine and subsuming the earlier class-ten gamma_8
and nonlinear-family results. The older arbitrary-class special strata
remain part of the same candidate. Arbitrary class is not settled.

The tally remains four whole-entry candidates, four partial candidates,
zero established novel results. There is no extra count for this extension.

## Mathematical review

Six kernel arguments cover the missing low leading-degree cases. The
main new exception has leading factors z in L1, D=ad_z^2(T) in L5,
T in L3, and a one-dimensional second-correction kernel. Its next
correction is injective. Joint integer equations leave no parameter,
one integral point, or one complete integral affine line. In the latter
case a nonzero degree-ten quadratic obstruction leaves at most two roots.
The proof treats both degree-three seed directions and derivatives of
degree-two seeds, with an explicit five-dimensional cokernel functional.

The internal audit checked the one-letter associative projections,
symmetric/antisymmetric rank-one conditions, old mixed injection and
Kernel A, integral kernel periods, exact Nielsen move x->yx, and the
nonzero slope of the coupled parameter. No rational particular solution
is substituted for the full integral solution set. The type(1,6) branch
retains the entire class-ten tail after its old degree-nine obstruction.

All final tails are linear by the explicit weight inequalities. A real
implementation omission was exposed by the first group test: the old
class-nine optimization discards conjugation of [x,h] by [x,y]. For leading
type(1,2), that conjugation contributes in degree ten. The new tail routine
retains the term; its second iterated conjugation is beyond degree ten.
The original class-nine code and failed run are preserved.

The delta-stable homogeneous free basis, ordinary homogeneous Shirshov
lemma, metabelian module fact, finite integral leading-pair enumeration,
and existing class-nine/gamma_8 algorithms remain cited dependencies.
The proofs, not bounded dimensions, supply the all-rank conclusion.

## Structural computations

`probe_n8_class10_completion_kernels.py` checked 14 rank-two and 17
rank-three exact Hall-coordinate matrices, including derivative seeds,
independent degree-three seeds, mixed directions, pure E,E and E,B cases,
and explicit kernel directions. Python/FLINT passed both complete suites
in 0.821 and 92.409 seconds respectively, with empty stderr.

GAP independently reconstructed all 14 rank-two maps in nilpotent group
quotients and checked their Hirsch ranks and proposed directions in
5.286 seconds, with empty stderr. Two rank-three GAP attempts timed out
after 180 seconds: the full suite and its degree-at-most-eight subset.
Neither prints an individual completed-case record, so no rank-three GAP
case is claimed verified. Their empty stderr does not change that status.
The rank-three Python suite is complete; its GAP counterpart is incomplete.

An initial fixture-export command imported a script whose command-line
parser ran immediately and failed before export. No GAP job was launched
from missing fixtures. The dedicated exporter was then written and used
before all three actual kernel replays.

## Group computations and independent replay

The primary rank-two suite covers all ten unequal/independent leading
types available there in degrees three through seven, two genuinely
different exceptional directions, final-layer perturbations, identity
and an abelian obstruction. Rank-two L2 is one-dimensional, so the
independent type(2,2) is covered by the all-rank proof and rank-three
structural Python checks, not by these group examples. Gamma_8 targets
delegate to the previously verified class-ten procedure.

The supplemental suite exercises inconsistent coupled systems, a unique
coupled solution, the older type(1,6) quadratic branch followed by a
complete two-layer tail, and a nonprimitive type(2,4) Nielsen normalization.

| Suite | Python records | Independent GAP evidence |
| --- | ---: | --- |
| Main v2 | 20:13 positive,7 negative | 13 witnesses;72 linear decisions (17 negative);6 coupled affine lines;6 polynomial decisions (4 empty);30 polynomial samples |
| Supplemental | 7:3 positive,4 negative | 3 witnesses;39 linear decisions (15 negative);7 coupled decisions (6 inconsistent,1 singleton);3 polynomial decisions;15 samples |

Thus GAP independently checked 16 witnesses,111 linear decisions,13 coupled
systems and9 complete polynomial certificates. The 45 sampled parameter
values check the group expansions; exact degree bounds and the HNF/cokernel
certificates, not samples alone, justify the full root lists.

The new GAP verifier recomputes group increments, compares them with the
recorded Hall-coordinate columns, checks integer solvability, and proves
completeness of a one-dimensional integral kernel by nullity and primitive
gcd. It ties late polynomial parameters back to the full coupled lattice.
The existing independent HNF, congruence and quadratic-root checker is reused.
It does not independently enumerate the complete leading-pair list; that
completeness remains part of the mathematical proof.

All four successful group jobs had exit zero, expected markers and empty
stderr. Main Python v2 took60.719s and GAP11.055s; supplemental Python
took39.248s and GAP5.085s. The first main Python run failed after47.529s
at the conjugation-range assertion, after four completed exceptional
records. Its exact executed sources, output and partial artifacts remain.
The successful rerun has a distinct output directory. Later module changes
are docstrings only; executed copies are retained in the result directories.

Every job used one core and4 or8 GB per-process limits. At most two of
these jobs ran concurrently. All jobs are terminal at this checkpoint.

## Sources, novelty and reproduction

A bounded web search on 28 September around23:30 UTC used
`"free nilpotent" "commutator problem" algorithm` and
`"free nilpotent" "single commutator" decidability`. It returned the
previously credited class-two and general-nilpotent work, not a matching
class-ten theorem. This does not establish novelty. The primary Roman'kov,
Truss and structural sources already archived remain the credited context;
no new theorem is imported from a search snippet.

Run commands, limits, actual exit codes, hashes and logs are in:

- `results/n8-class10-completion-kernels-rank{2,3}-v1/`;
- `results/n8-class10-completion-kernels-rank2-gap-v1/`;
- both saved rank-three kernel GAP attempts;
- `results/n8-class10-rank2-v1/` (failed) and `-v2/` (passed);
- `results/n8-class10-rank2-gap-v1/`;
- `results/n8-class10-supplemental-v1/` and `-gap-v1/`.

Use new output/job directories on reproduction: the runners and generators
refuse to overwrite prior evidence. The primary and supplemental GAP drivers
read the retained fixtures directly. The kernel drivers reuse the old
class-nine generic kernel checker, hence its historical success-marker name.
Artifact and dependency hashes are in
`research/certificates/N8-class10-completion/artifact-hashes.json`.
No source snapshot, original clock, prior certificate or Kourovka artifact
was altered. No external review, agents, push or contact occurred.
