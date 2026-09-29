# Audit of the two-exception branch extension

29 September 2026. `two-exception-proof.md` is a candidate extension of the
same partial N8(b) result: at most two remaining exceptional offsets,
leading gaps <=8, leading degrees <=10 in arbitrary class, and all targets
through class 20 with the earlier ten-final-layer theorem. General N8,
specialist review and novelty remain unresolved. Full ambient branch
enumeration is not implemented end to end.

## Proof scrutiny

The full integral block lattice is retained below the first quadratic
obstruction. Universal substitutions give constant translations there;
every torsion coset remains. A basis adapted to the first exceptional
coordinate leaves at most two free parameters, with their actual integer
steps. Weight gives the cokernel equation q(T)+S B=0, where q has a nonzero
quadratic coefficient and B is constant. There are no TS or S^2 terms at
this layer. If B=0, all integer roots for T are retained and the last
exception is processed separately. If B!=0, S is polynomial in T, with
all compatibility equations and integer congruences retained.

Later homogeneous matrices are constant. Their complete congruence classes
and every residue of universal kernel substitutions yield finitely many
polynomial families. The periods depend on the fixed leading pair, not
on the parameter or higher terms. The proof treats rank-zero/one parameter
quotients, a fixed first parameter, an early class cutoff, and the Nielsen
kernel at the quadratic boundary. Restarting after fixing the first
parameter may duplicate solutions, but solves the entire equation again.

The finite leading-pair enumeration, homogeneous kernel lemmas, nonzero
quadratic obstruction and exact universal substitutions remain inherited
dependencies. Their classical ingredients retain the earlier credits.
Finite fixtures and internal scrutiny do not replace specialist review.

## Complete polynomial arithmetic families

`scripts/n8_polynomial_families.py` specializes the audited one-parameter
solver to a constant matrix. It returns every finite parameter or periodic
residue, a polynomial integral particular solution, and the complete
integer kernel certified by a unimodular Hermite transformation. This is
prior arithmetic, not a novelty claim.

The final suite has 11 systems and 671 fixed specializations: zero rank,
free kernels, rational inputs, an integer-valued polynomial, finite
positive/negative cases, and positive/negative quadratic-absorption cases.
The positive absorption control has two unbounded residue classes. Empty
matrix dimensions have trivial mathematical reductions, but are not tested
in this suite.

The final Python constructor passes in 1.575728 seconds. Independent GAP
arithmetic replay passes in 2.225208 seconds: 11 complete systems, 4 finite
decisions, 413 residue decisions, 671 specializations and 8 witnesses. A
separate GAP checker verifies all 11 complete integer kernels and all 67
polynomial or point sections in 1.975616 seconds, using polynomial identities.
Together they check complete parameter sets and complete solution fibers.

The first family checker decoded constants as constant-polynomial objects
and failed its own type check after 2.125880 seconds. Its exact source and
error remain. The corrected decoder changes no mathematical input. An
earlier successful ten-system constructor is also retained; the final
suite adds a positive absorption control.

## Actual group blocks

Fixtures use weighted free nilpotent groups on a,e of weights (1,4) and
(1,5). With D=ad_a^4(e), the actual initial pair is (a^2,h_D^3), where h_D
is a Hall group commutator. Every correction coordinate in the block is
included. Targets are actual commutators with a deterministic correction
vector; no random seed or bounded witness search is involved.

| Exceptions | Weighted class | Hall rank | Block matrix | Rank | First parameter step |
|---|---:|---:|---|---:|---:|
| 3,5 | 15 | 35 | 14 by 14 | 12 | 8 |
| 4,6 | 18 | 41 | 19 by 19 | 17 | 16 |

GAP constructs both groups independently with NQ and verifies their ranks,
torsion-freeness and Hall relators. Every block column and right side is
checked in the group modulo the terminal central layer. The full Hermite
transformation and unimodular parameter basis change retain the entire
rank-two integer lattice, including the nontrivial steps 8 and 16.

Class-15 replay passes in 2.477680 seconds: 14 block columns, 14 terminal
columns, 6 quadratic samples, 3 complete block kernels, the complete
parameter lattice and 2 group witnesses. Class-18 replay passes in
2.878537 seconds: 19 block columns, 16 terminal columns, 6 quadratic
samples, 4 complete block kernels, the complete lattice and 2 witnesses.
The proved weight bound supplies the polynomial identity beyond samples.

The terminal map is injective in the first case. In the second, its
one-dimensional kernel is the Nielsen direction at offset 8. GAP verifies
four exact substitutions with exponents -2,-1,1,2, the chosen leading
period 3, and all residues 0,1,2. This period is sufficient, not asserted
minimal. Thus the intermediate offset 7 and Nielsen boundary are tested.

The complete accepted first-parameter sets are {-7} and {7} in the recorded
lattice coordinates; the remaining integer kernels have ranks one and two.
Each fixture has separate arithmetic replay (one complete system, one
finite decision, 41 specializations, one witness) and complete-kernel/point
replay. Each takes about 2.23 seconds (2.278417 for the second arithmetic
replay). These check the v1 arithmetic/family files, whose bytes equal the
v2 copies. All successful final runs have empty stderr.

The initial Python constructors passed, but serialized a GAP record field
named `end`, a reserved word. Both first group replays failed to parse,
after 2.172751 and 2.176311 seconds. Their exact sources and logs remain.
Renaming the field to `corrections` fixes the format; v2 constructors pass
in 6.339990 and 13.663412 seconds. Mathematical inputs and separately
checked arithmetic are unchanged.

## Limits, sources and resources

Both actual group fixtures have B=0 modulo the terminal image. The B!=0
case has an algebraic proof and complete synthetic arithmetic controls,
but no surviving group fixture here. The earlier example with proportional
late Lie obstructions fails an earlier compatibility condition; that saved
failure is not reclassified as positive evidence.

The class-20 conclusion follows from the general proof and its union with
the tail theorem. These weighted group tests have classes 15 and 18; they
are not an ambient class-20 computation or an enumeration of every free-Lie
component. No separate negative group target is claimed here. The earlier
class-19 mixed term still bounds the linear-tail method; this new argument
uses a different reduction.

The full frozen nilpotent HTML, exact fragment and linked background were
reread; the archived statement rendering was actually viewed. Part (a),
general class-two undecidability, and the prior free class-two answer remain
separate. A fresh targeted search again returned Roman'kov's class-two work
and the 2016 Miasnikov slides, not a precise match for this assembly. This
does not certify novelty; no new full external proof was audited.

All computations used the recorded runner, one core and 8 GB apiece, with
at most four concurrent jobs. All are terminal. No subagent, imported
Kourovka argument, push or external contact. Original deadline unchanged.
