# N8: three remaining exceptional offsets — audit

29 September 2026. Candidate partial extension with completed finite
audit. This is internal mathematical review plus independently implemented
calculations, not external specialist review. Novelty is unverified.

## Scope and original statement

`three-exception-proof.md` treats branches with at most three remaining
pre-Nielsen exceptional offsets in arbitrary class. The weight bounds give
leading gaps at most10 and leading target degrees at most12 in arbitrary
class. Combining this with the fourteen-final-layer theorem gives all
targets through class26. This extends the same N8(b) partial candidate;
general N8 is unresolved and no additional entry is counted.

Reread the complete frozen `sources/raw/probnil.html`, the exact N8
paragraph and its linked `Back2.html` background. Actually viewed the
archived statement rendering again in this work period. Part(a) concerns
arbitrary finitely generated class-two groups and has a prior negative
answer. Part(b) concerns free nilpotent groups; its class-two answer is
already credited to Roman'kov2016. Neither prior scope is counted here.

## Proof audit

The proof retains the full integer block lattice, all torsion cosets and
the actual gcd step of the first exceptional parameter. Quotienting only
the rational span of universal translations would be insufficient. A full
integer Smith decomposition supplies every finite residue and the integral
free parameters. The first nonzero components of the free directions lie
at exceptional offsets, since universal offsets begin only afterward.

At the first quadratic layer the remaining equation is
`q(T)+B S+C R=0`, with constant later columns and a fixed nonzero quadratic
coefficient in T. The rank-zero, one-column, rank-two and rank-one cases
are all included. In the last case an integer Bezout change removes one
later coordinate from the linear map without discarding its integral scale.
The remaining R starts at a later exceptional offset and has a constant
nonzero first direction. Its first quadratic therefore has a fixed nonzero
coefficient in R squared.

If the target ends before that delayed quadratic, all retained equations
and fixed congruences are affine in R; a univariate polynomial integer-
matrix system decides them. This affine hypothesis is explicit. Arbitrary
extra disequalities are not smuggled into that fallback. If the quadratic
is reached, the constrained-curve lemma keeps every later polynomial
condition and fixed-modulus congruence. Universal normalization periods
depend on the fixed leading pair and class, not on the varying parameters.

The supporting arithmetic lemma is in
`../../research/notes/N8-constrained-curve-lemma.md`. Its squarefree
degree-at-least-three case imports the effective height bound of
Berczes--Evertse--Gyory2013, Theorem2.2. The low-degree cases have explicit
finite or periodic arguments, including complete Pell orbits. The theorem's
statement and hypotheses were checked, but its full proof was not audited;
the enormous high-degree enumeration is not implemented. The earlier
independent finite arithmetic audit is retained separately.

All-rank leading-pair enumeration, ambient Lie-kernel assertions and the
general exact-substitution construction remain inherited dependencies.
Their applications and the new assembly require specialist review.

## Two placements of the third exception

Actual weighted group blocks use leading inputs2a and3ad_a^6(e).

| weights | class | exceptions | block matrix | integral free steps | terminal kernel |
|---|---:|---|---|---|---:|
|(1,5)|20|4,6,8|31 by28|16,4|1|
|(1,6)|23|5,7,9|37 by35|32,8,2|0|

Independent GAP reconstructs the torsion-free quotients of Hirsch lengths
65 and73, checks every block column, complete integral kernels and adapted
bases, quadratic samples, terminal columns and two witnesses per fixture.
Separate GAP checks replay their complete polynomial integer fibers and
arithmetic decisions. In total these group fixtures check63 block columns,
24 terminal columns and15 quadratic samples. Both have later-column
cokernel rank0 and one finite first-parameter family. They are not examples
of a surviving unbounded absorbed-quadratic branch.

## Delayed quadratic followed by a universal kernel

The larger fixture has weights(1,4), leading weights(1,10), class26 and
Hirsch length680. Earlier exceptions3,5 are fixed. The full block7..13
contains the remaining exception7 and universal kernels9,11,13. Its
330 by273 integer system has complete kernel rank4 with adapted steps
128,1,4,2. The terminal matrix has291 rows and237 columns, including both
offsets14 and15; its complete kernel has rank1 at15.

The Python constructor passes in1041.789 seconds. It includes the quadratic
at weight25 and the possible same-input quadratic at weight26. Its block
unit-column shortcut is used only through weight24, where the stated
weight inequalities justify it. The largest certificate is75046692 bytes,
below the90000000-byte limit.

The successful independent group verifier is
`scripts/check_n8_delayed_quadratic_poly_gap.g`. It uses the native NQ group
and its integral Pcp coordinates, not Python tensor multiplication. Errors
from the base commutator start at weight18 and hence form an abelian subgroup
in class26. Their coordinates are additive.

The full commutator polynomial in the273 input correction coordinates has
degree at most two: the minimum weights for three occurrences are34,33,42
and52, according to which inputs contain them. A mixed quadratic can occur
only when the two input weights sum to at most26. A quadratic from one
input alone additionally includes the other leading weight. The verifier
therefore reconstructs **all60 possible quadratic coefficients**, using
unit changes and one doubled coordinate, rather than evaluating huge powers
at a selection of full parameter values. No possible coefficient is omitted
by a sample cutoff.

It then checks the saved family at nine parameter values. The same weight
bounds show that this family consists only of a constant, T, T squared and
three later linear parameters, so these include a determining set and joint
controls. Every terminal correction is checked at the base: terminal
offsets14/15 cannot interact with block offsets at least7 through target
offset15, making those columns independent of all block parameters.

The native replay passes in105.778 seconds with empty stderr:

- 273 complete block columns and joint controls;
- 60 complete quadratic coefficients and9 family evaluations;
- 237 terminal columns;
- 7 complete homogeneous block kernels and both terminal kernel dimensions;
-the full integer rank4 affine lattice and its actual steps;
- 2 actual group witnesses and the arithmetic witness reconstruction.

Independent complete-family and arithmetic replays pass in3.433 and59.578
seconds. They check the complete finite decision, integer fibers and41
specializations. This fixture also has a finite first-parameter fiber and
later-column cokernel rank0. The group is a weighted free quotient, not
the full ordinary rank-two free nilpotent group of class26. The all-rank
theorem comes from the proof, not extrapolation from this computation.

## Exact periods and every residue

Four formal maps in weights(1,10),class26 were first constructed at offsets
9,11,13,15 by exact polynomial-denominator clearing. The first two resulting
periods were sufficient but unnecessarily large. The final version uses
the exact left Nielsen map `x -> yx` at9, conjugation of both inputs by
`[x,y]` at11, and the previously constructed maps at13,15.

GAP independently checks the formal maps, both inverse compositions,
commutator preservation and every defining boundary relation:4 maps,
16 inverse equalities,704 image boundary relations and a rejected wrong
right-Nielsen control. The compact-map replay passes in2.679 seconds.

The specialized native ambient replay
`n8-delayed-periods-gap-v5` passes in65.990 seconds. It checks16 exact
map specializations:both signs on the base pair and on a pair with a unit
correction in each input at offset7. Every case checks its inverse
composition, exact commutator preservation and prefix translation.
It also verifies the full integer period lattice against the block kernel.

The final block-period columns are diagonal in the later adapted kernel
coordinates, with steps3,3,1816214400. A complete residue box therefore has
order16345929600, leaving the first block parameter fixed. The final
one-dimensional terminal kernel has period479001600. Its translation
divided by the gcd of its coordinates is a primitive integer kernel basis.
Every residue in both quotients is retained in the proof and certificate
description. These huge finite sets were **not enumerated**.

The earlier larger period certificates are preserved. They are alternate
sufficient lattices, not additional mathematical examples or minimality
claims.

## Failures, provenance and limits

The final manifest lists50 terminal runs in this follow-up:27 successful
and23 unsuccessful. The latter comprise one bounded-factorial search cap,
11 intentional performance interruptions, three collector-flag assertion
failures, two success-marker configuration errors and six timeouts. The
two marker errors occurred after the mathematics printed the correct PASS
line and exited0; the wrapper expected the wrong singular word. They remain
configuration-rejected records. No mathematical counterexample was found.

Superseded sources are preserved with failed/interrupted runs or at their
recorded commits. Generic polynomial Smith arithmetic was replaced by an
exact constant-matrix reduction, with all existing arithmetic suites replayed
independently. Small native groups benefited from Hall multiplication
polynomials. The full class26 polynomial build timed out twice; it is not
required by the successful small-exponent coefficient replay. Period replay
was made practical by constructing only used Hall words and reusing the two
prefix-tail subgroups. All requested equations and residues remain checked.

The independently constructed native quotient was cached in the ignored
local workspace `large-artifacts/N8-class26-workspace/quotient.ws`, size
91776352 bytes, SHA256
`9497ee7df283fd6f203d3e47fb5b3481d79862b9fe44d9c6e079da283baa3346`.
This cache is not committed. Its constructor and exact presentation are
included in `scripts/probe_n8_delayed_quotient.g`; the cache is saved before
the optional-for-replay polynomial build. The group verifier also has an
uncached reconstruction path. Cache use does not import Python group data:
presentation equality, boundary relations, full Hirsch length and absence
of torsion are checked in native GAP. See the interim audit for the exact
regeneration command and recorded timed-out preflight.

The full all-rank and arbitrary-class branch algorithm is not implemented
end to end. No surviving unbounded absorbed-quadratic group fixture has
been exhibited. The separate separating-functional lemma excludes absorption
only in its restricted Lie deformation model and is not used to delete
rank cases from this proof. Deep structural dependencies, the curve-theorem
application and novelty still require specialist review.

All jobs are terminal. Recorded overlap peaked at7 CPU cores and48GB of
reserved memory. The original48-hour deadline is unchanged. No push,
external contact, subagent or parent/preparation-repository change occurred.
Counts remain8 whole-entry candidates,2 partial candidates and0 established
novel results.
