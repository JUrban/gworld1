# Class eight: scope, checks and reproduction

28 September 2026. The candidate argument is in `class8-proof.md`.
The six kernel arguments were first written approximately 16:14–16:18
UTC, and the stronger quadratic obstruction approximately 16:23 UTC.
The chronological lead, including an abandoned cubic/progression
route, remains in `research/notes/N8-class8-lead.md`.

This extends the same partial N8(b) candidate to all targets in class
eight, in every finite rank. It is not an arbitrary-class result and
adds no entry to the candidate count. No external specialist review
or exhaustive novelty certification has occurred.

## Statement and proof audit

The full original nilpotent-group page, its N8 paragraph, linked
background and rendered statement were inspected in the preceding
N8 work. The evidence remains in `research/statement-audits/N8/`.
Part (a)'s prior negative answer is separate. Part (b) quantifies over
all finitely generated free nilpotent groups, so the class-eight
result is still partial scope.

The proof supplies six all-rank correction-kernel calculations using
the homogeneous free generators of the derived Lie algebra. The
homogeneous Shirshov lemma remains the standard, explicitly credited
dependency introduced in the class-seven proof. The new degree-six
metabelian kernel is proved by a syzygy-image calculation and an
explicit Witt-dimension identity. Numerical ranks do not replace these
arguments.

For type (1,4), the earlier first correction has either zero kernel
or the line `(T,-[T,delta T])`, where D=delta^2 T. The next correction
on L3+L6 is injective. More strongly, `[T,[T,delta T]]` lies outside
its rational image. This is the nonzero quadratic coefficient of the
remaining parameter obstruction, up to a nonzero scalar. Consequently
there are at most two integer parameters to try. Each must satisfy
all integral divisibility conditions; its degree-seven correction is
then unique, and its degree-eight correction is a fixed integer
linear system.

The written proof checks all leading weight types, the joint-tail
weight bounds, rational versus integral kernels, finite signed scales
and exact Nielsen residues. In particular, the commutator-preserving
move is x->yx, with y fixed. The kernel normalization is not allowed
to discard a nonzero residue. The earlier finite homogeneous-factor
enumeration and arbitrary-class boundary procedures remain explicit
dependencies.

## Implementations and certificates

`scripts/n8_class8.py` implements the new middle strata, using the
existing exact Magnus/Hall arithmetic and leading-factor routines.
`scripts/n8_polynomial_lattice.py` reduces integer-valued univariate
Newton polynomials modulo a fixed integer lattice with a checked
Hermite transformation H=U*B, det(U)=+/-1. It computes every integer
root of a nonzero free polynomial and checks all congruences. Its
more general periodic branch is tested arithmetically but is never
needed by the class-eight exceptional branch: the new proof forces
a nonzero free quadratic coefficient.

The certificate verifier independently checks the Hermite identity,
unimodularity, echelon pivots, full column rank, rational polynomial
reduction, integrality congruences, the complete root list, and every
accepted integer parameter. GAP/nq also checks actual group lifts,
parameter samples, correction columns and positive commutator words.
This is an independent computational representation, not an
independent mathematical proof review.

One certificate-generation correction preserves the original input
word for the target instead of expanding the target into a much
longer Hall-normal-form word. The rank-three diagnostic stacks exposed
the redundant round-trip expansion. This changes the recorded word
representation, not the target, branch procedure or decision.

The new `scripts/n8_class8_tail.py` also reduces the width of exact
joint-tail systems. If the tail starts in gamma_s with 2s>8, its
truncated Magnus augmentation ideal is additive, with integral basis
h-1 for Hall group generators of weights at least s. Select the
independent leading Hall pivot rows in each degree. On this span the
resulting matrix is block triangular with invertible diagonal blocks,
so the projection is injective over Q. Applying it to both sides of
an integer system preserves its **entire integer solution set**;
no saturation assumption is needed. Positive solutions are checked
again in every original tensor coordinate. GAP independently checks
both positive and negative subgroup decisions for the actual group
columns. The older, wider tail routine remains unchanged for prior
artifacts and for the saved comparison run.

`scripts/n8_class8_magnus.py` preserves the same integer series but
expands long words by balanced products with a bounded local cache.
`n8-class8-expansion-v1` passed 52 records in 54.85 seconds, one
CPU/8 GB, seed 9282633, with empty stderr. These include every Hall
word through class eight in ranks two and three, 24 comparisons with
the original sequential word expansion, and 12 repeated-commutator
power checks. The change retains the actual word round-trip checks.

An exact integral-kernel translation also shortens the particular
solution before polynomial sampling. `n8-class8-parameter-size-v1`
checked both exceptional leading branches in 25.86 seconds, one
CPU/12 GB, with empty stderr. It verifies the integer shift explicitly.
The measured word lengths changed only from 1144 to 1110 in one
branch and stayed at 2182 in the other; this small reduction is not
presented as the explanation of the main speed improvement.

## Completed kernel and arithmetic checks

| Run | Scope | Seconds | Resources |
| --- | --- | ---: | --- |
| `n8-class8-kernels-v1` | 39 kernel records in ranks 2,3; symbolic degree-six dimension identity | 12.26 | 1 CPU, 8 GB |
| `n8-class8-obstruction-v1` | 8 quadratic cokernel records in ranks 2,3; 40 comparisons with the earlier Smith polynomial solver | 6.19 | 1 CPU, 8 GB |
| `n8-class8-kernel-gap-v1` | All 39 kernel ranks and 8 cokernel rank increases independently checked in nilpotent quotients | 67.82 | 1 CPU, 8 GB |

Seeds are 9282627 and 9282628 respectively. The first suite includes
derived-only cases, independent equal-weight leading pairs, and the
previous exceptional D=delta^2 T. The second suite retains z,T,D,Q
and the exact rank increase from adjoining Q to the correction image.
The arithmetic comparison uses 40 small random integer systems and
compares solubility with the preceding Smith implementation; it is
not an exhaustive arithmetic test.

The two Python runs have empty stderr. The GAP kernel run has three
syntax warnings about globals used in anonymous functions before
their top-level assignments. They are warnings, not failed checks;
the final marker and normal termination are present. The original
stderr bytes are preserved.

## Rank-two group checks

`n8-class8-rank2-v1` passed 19 targets in 6.94 seconds, one CPU/8 GB,
seed 9282631. It includes the seven possible rank-two middle leading
types, constructed higher corrections, two exceptional positive
parameters (-1 and 2), a nonprimitive (1,3) example, perturbations,
identity and nonzero abelianization. The nonprimitive example has
Nielsen period three and succeeds at residue one. Its independent
GAP run `n8-class8-rank2-gap-v2` passed in 4.84 seconds, checking
13 witnesses, 67 linear decisions (30 negative), six polynomial
decisions and 30 group parameter samples. The verifier reports one
harmless global-variable syntax warning, retained in the raw log.

The focused rank-two suite `n8-class8-focused-rank2-v1` passed 14
targets in 4.28 seconds on one CPU/8 GB, using the same seed with a
different target-generation sequence. It covers the new correction
types and perturbations in both degrees seven and eight. Its GAP
run `n8-class8-focused-rank2-gap-v1` passed in 3.73 seconds, checking
11 witnesses, 33 linear decisions (nine negative), ten polynomial
decisions and 50 parameter samples. Both runs have empty stderr.

These suites overlap in mathematical examples; their record counts
are not counts of distinct theorems or necessarily distinct inputs.
Neither rank-two suite contains an empty polynomial parameter list;
their negative cases fail linear or leading-factor conditions. The
general polynomial arithmetic and the written obstruction proof
remain separate evidence.

After the arithmetic changes, `n8-class8-pivot-rank2-v1` repeated
the original 19 targets in 6.19 seconds; its independent GAP check
passed in 4.93 seconds. The final combined suite
`n8-class8-final-rank2-v1` then passed 22 targets in 6.34 seconds,
including both degree-seven and degree-eight perturbations.
`n8-class8-final-rank2-gap-v1` independently checked its 15 witnesses,
75 linear decisions (32 negative), ten polynomial decisions and 50
samples in 5.34 seconds. These four runs used one CPU/8 GB apiece
and have empty stderr. Their overlapping records add no theorem count.

## Rank-three group checks

The focused rank-three rerun and its independent verification are
recorded below when complete. Until then the rank-three group checks
are incomplete; the completed all-rank proof and bounded rank-three
kernel checks should not be described as a completed group suite.

## Preserved unsuccessful runs

`n8-class8-rank2-gap-v1` stopped at a GAP syntax error after 1.92
seconds: Python-style `expression not in Integers` was invalid GAP
syntax. It was replaced by `not IsInt(expression)`. The runner
correctly rejected the run for a missing marker despite GAP's zero
exit code. The failed checker is retained beside its raw logs. The
successful version-two checker is also retained before a later
warning-only global declaration adjustment.

`n8-class8-rank3-v1` reached its 500-second limit before completing
its first target, of type (1,2). It used one CPU and a 12 GB process
limit. No diagnostic profile was enabled, so the dominant cost of
that particular run is not claimed to be known. Its initial Hall
file, raw logs and exact relevant script snapshots are preserved.

`n8-class8-focused-rank3-v1` was deliberately interrupted after
286.21 seconds, one CPU/12 GB. It had completed five positive targets
of types (2,2),(1,4),(1,5),(2,4),(3,3). Scheduled stack snapshots then
identified an expensive round-trip expansion of the target for its
polynomial certificate. The five partial records, Hall words,
fixtures and script snapshots remain in that run's `certificates/`
and `scripts/` directories. It is not a completed validation.

`n8-class8-focused-rank3-v2` failed after 97.00 seconds at the
factor-word round-trip assertion. The fault was a mutable list alias
in the test fixture: taking a stored degree-two Hall word and using
`+=` to append a second word modified the stored basis word, while
leaving its algebraic expansion unchanged. Copying that word before
modification fixes the fixture. Five earlier positive records and
the exact scripts remain with the failed run. Neither the proof nor
the group-arithmetic routines required correction for this failure.

`n8-class8-collect-diagnostic-v1` was interrupted after 138.99 seconds.
Its initial reproducer used a fresh concatenated word and therefore
did not recreate the bad alias; it is not reported as a successful
diagnosis. Its script and process record are retained.
`n8-class8-collect-diagnostic-v2` deliberately restored the bad alias
and reproduced the failure in 28.91 seconds, with empty stderr. Its
saved record identifies the altered Hall word, its unchanged group
value, the twelve-letter failed output word and all 668 differing
tensor coordinates. Both internal collection and multiplication
agree on the original series; only the mutated word is inconsistent.
The diagnostic's PASS marker means the expected failure was reproduced,
not that the intentionally corrupted fixture is valid.

Three later incomplete runs preserve the performance investigation:

| Run | Outcome | Completed target records |
| --- | --- | ---: |
| `n8-class8-focused-rank3-v3` | 400.04-second timeout with corrected fixture and original wide tail matrices | 6 |
| `n8-class8-pivot-rank3-v1` | Interrupted after 359.25 seconds; reduced tail matrices but sequential word expansion | 9 |
| `n8-class8-focused-rank3-v4` | Interrupted after 208.98 seconds; reduced matrices and parameter shortening, sequential expansion | 5 |

All used one CPU/12 GB. Their exact scripts and partial certificates
are retained with the result directories. Scheduled stack snapshots
in the focused runs locate substantial remaining work in certificate
word expansion, including the final witness conversion. The printed
`Timeout (0:01:00)!` snapshots are diagnostics; the authoritative
timeout/interruption outcomes are the process records above. The
balanced expansion comparison passed before these runs were replaced
by the final combined suite. None is counted as completed validation.

## Reproduction

All mathematical computations used `scripts/run_recorded.py`, with
exact commands, resource settings, seeds, limits, return codes and
raw-output SHA256 hashes retained in `results/NAME/process.json`.
No computation exceeded the shared 20-CPU/100-GB requested budget.

For example, in a separate work copy with fresh output paths:

```sh
python3 scripts/run_recorded.py --name n8-class8-kernels-v1 \
  --cores 1 --memory-gb 8 --timeout 300 \
  --expect 'PASS N8 class8 kernel checks' \
  -- .venv/bin/python scripts/check_n8_class8_kernels.py
python3 scripts/run_recorded.py --name n8-class8-obstruction-v1 \
  --cores 1 --memory-gb 8 --timeout 120 \
  --expect 'PASS N8 class8 quadratic obstruction' \
  -- .venv/bin/python scripts/check_n8_class8_obstruction.py
.venv/bin/python scripts/export_n8_class8_kernel_gap.py
python3 scripts/run_recorded.py --name n8-class8-kernel-gap-v1 \
  --cores 1 --memory-gb 8 --timeout 300 \
  --expect 'PASS N8 class8 kernel GAP' \
  -- bin/gap -q --quitonbreak scripts/check_n8_class8_kernel_gap.g
```

Target generators refuse to overwrite an
existing `checks.json`. `export_n8_class8_gap.py --rank R --directory
PATH` translates saved group certificates into GAP literals without
redoing mathematical work. Set `N8C8Directory` to PATH before reading
`scripts/check_n8_class8_gap.g`. Use the exact commands in successful
process records to reproduce the respective suites.

## Bibliographic limits

Targeted searches on 28 September for free-nilpotent single commutator
algorithms, class eight, and commutator equations found no matching
full higher-class decision theorem. This does not certify novelty.
The known class-two answer and general-system undecidability have
different scopes. A primary historical abstract by Kenneth W. Weston,
AMS Notices January 1978, abstract 752-20-34, printed p.A-75, also
distinguishes systems from single equations in rank two/class two.
Only that abstract was read online; an attempted full-issue archive
was refused by the downloader's 20-MiB limit, and no full-paper proof
audit is claimed. See `literature/LEDGER.md` for its link and scope.

No Kourovka mathematical argument or code was imported. Specialist
review and a fuller novelty audit remain outstanding. Classes nine
and higher still have uncovered intermediate target layers.
