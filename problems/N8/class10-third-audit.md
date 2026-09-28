# Audit: the complete gamma_8 stratum in class ten

28 September 2026, before the original deadline. This records internal
checks and independent software representations, not outside specialist
review. The authoritative candidate argument is `class10-third-proof.md`.

## Statement and scope

Re-read the exact archived N8 fragment and viewed its existing screenshot
again at approximately 22:49 UTC. Part (a), for arbitrary class-two
nilpotent groups, is starred; part (b) asks about every finitely generated
free nilpotent group. The present extension concerns only gamma_8 targets
in class ten, in every finite rank. The gamma_9 and gamma_10 cases were
already covered; the new range is nonzero degree-eight leading terms.

It subsumes the earlier nonlinear class-ten family. It is the same one
partial N8(b) candidate and adds no whole-entry or separate partial count.
General lower intermediate layers in class ten and arbitrary class remain
unresolved here. The original frozen source and its rendering are retained
in the older statement audit; no publisher bytes were edited.

## What changed mathematically

The earlier proof verified one exceptional type-(1,7) family. The new
proof classifies **all** type-(1,7) first kernels, then proves injectivity
for types (2,6), (3,5), and independent type (4,4). A fresh-letter
associative-algebra argument excludes a residual length-three component.
It is a vector-space quotient by the image of ad_a, not a quotient by a
two-sided ideal. Its canonical representatives are spelled out in the
proof to prevent that possible confusion.

Internal checks covered the separate free-alphabet weight types, the
fresh-letter projection, the absence of other seed patterns in the
exceptional kernel, complete integral leading scales, and the bounds
s+t=10, 2s+q>10, p+2t>10. The previously proved nonlinear cokernel
obstruction is reused with its original coefficients and integral
parameter convention. No arbitrary rational kernel choice substitutes
for the full integral lattice.

The delta-stable free basis, Klyachko rotation argument, finite leading
enumeration, and final polynomial lattice machinery remain explicit
dependencies on the earlier proofs. The all-rank result rests on these
proofs; finite ranks in the computations do not establish it.

## Exact structural probes

`scripts/probe_n8_class10_third_kernels.py` builds free Hall Lie layers
inside exact Magnus expansions and computes integer-matrix ranks with
FLINT. It retains C,D, expected and actual nullities, and an explicit
exceptional kernel vector.

- `n8-class10-third-kernels-rank2-v1`: passed in 1.02 seconds, 24 records.
  There are 23 normalized cases and one dependent-leading-pair control.
  The latter deliberately has a six-dimensional kernel and is outside
  the type-(4,4) independence hypothesis. Other controls include the
  nonlinear exception, a wrong coefficient ratio, mixed alphabet
  lengths, Hall elements, and derived-alphabet components.
- `n8-class10-third-kernels-rank3-v1`: **timed out after 180.03 seconds**.
  Nine records completed, all type (1,7): one one-dimensional exception,
  seven zero-kernel controls, and a rank-two polarization control with
  zero kernel. The next mixed-seed case and all later cases did not
  complete. This is an incomplete probe, not a successful rank-three
  suite and not independent GAP evidence. Its partial JSON, logs and
  exact source are preserved.
- `n8-class10-third-kernels-rank2-gap-v2`: passed in 12.85 seconds.
  GAP independently forms the corresponding group commutators in the
  degree-nine central layer and computes subgroup Hirsch ranks. It
  verifies all 24 nullities and the explicit exceptional direction.
  It does not import the Python tensor expansion or matrix ranks.

The GAP checker is the unchanged generic class-nine kernel checker with
the new dataset path. Its historical success marker still says class9;
all new leading weights sum to eight and offset j=1, so the quotient
class nine is exactly the first-correction layer required here.

## Complete rank-two group decisions

`n8-class10-third-rank2-v1` passed in 16.93 seconds. The deterministic
seed recorded by the fixture generator is 9282618; the current fixture
selection is fixed and does not depend on a random draw. Sixteen records
comprise fourteen supported decisions and two outside-scope controls:

- Seven positive nonzero degree-eight targets: all four leading types
  with later corrections, two nonprimitive scale cases, and the nonlinear
  exceptional branch.
- Five negative degree-eight targets: four last-layer perturbations and
  an independently justified non-bracket leading term.
- Two previously covered positive boundaries: one gamma_9 target and
  the identity.
- Two lower-layer inputs returning None, not False.

The independently justified negative leading term is
ad_a^7(b)-2 ad_b^7(a). The metabelian projection from the central-target
proof gives the Eisenstein polynomial s^6+2t^6: there is no rational
linear factor, whereas a degree-one factor would force one. A bracket
of two derived elements has zero projection. Thus no homogeneous
factorization, and hence no group commutator, is possible.

`n8-class10-third-rank2-gap-v2` passed in 7.09 seconds, with empty stderr:
**9 witnesses, 44 linear decisions (23 negative), 1 polynomial certificate,
and 5 group samples**. The one new polynomial certificate has a nonempty
parameter list; negative exceptional-family certificates are in the older
nonlinear audit and are not newly counted here. GAP checks exact word
identities, integer subgroup membership for the linear decisions, and the
retained polynomial certificate using its independent nilpotent quotient.
It does not by itself certify that every leading case has been enumerated;
that completeness is part of the proof and Python algorithm audit.

## Failed setup attempts and exact-source history

The first ad hoc kernel export imported a nonexistent serializer name
`gap` instead of `gap_value`; it failed before writing the fixture. Both
initial GAP replays were then launched before their required exports:

- `n8-class10-third-kernels-rank2-gap-v1` failed because
  `kernel-fixtures.g` did not exist.
- `n8-class10-third-rank2-gap-v1` failed because
  `polynomial-fixtures.g.gz` did not exist.

Both GAP processes returned zero, but printed an error and lacked their
success marker. The recorded runner correctly marks them failed. They
are preserved, not replaced with the successful v2 outcomes. Corrected
exports were checked before the v2 replays; no mathematical algorithm
change was needed. The successful original Python sources and every GAP
wrapper/common checker are copied into their result directories. The
current Python module and fixture script differ from their saved versions
only in docstrings changing the lead status to candidate; no rerun is
claimed for this documentation-only change.

All recorded jobs used one core each and 4 GB memory, except the incomplete
rank-three probe, which requested 8 GB. At most two were concurrent.
Every process is terminal. No broad benchmark or failed fixture attempt
is represented as completed validation.

## Bibliography and novelty

Repeated bounded searches for `free nilpotent single commutator algorithm`
and `nilpotent commutator problem decidable class` found the already
credited class-two and general-nilpotent results, not a matching class-ten
stratum theorem. This does not certify novelty. Roman'kov's negative
result for some general class-two groups concerns a different class from
the relatively free groups here. Earlier class-two algorithms and the
structural Lie theorems remain credited in the existing N8 audits.

The exact argument, implementation, all successful and failed process
records, complete/partial datasets and prior dependency manifest are
listed in `research/certificates/N8-class10-third/artifact-hashes.json`.
No new Kourovka mathematics or code was imported, and no external review,
push, or author contact occurred.
