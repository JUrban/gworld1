# N8: fixed and nonunit exceptional parameters in the full recursion

30 September 2026, during the original run. This is a targeted addition to
the [general implementation audit](general-implementation-audit.md), covering
two branches not exercised by its initial controls. The solver itself was
unchanged. The general proof and novelty still require specialist review.

In F(a,b)/gamma_11, put z=[b,a], U=[b,z] and D=[a,[a,U]], using group
commutators x^-1 y^-1 x y. Run the complete leading-pair enumeration and
integral recursion on these three known commutators:

1. [a z U^2,D];
2. [a^2 U^2,D^3];
3. [a^2 z U^2,D^3].

All three are recovered, with full final commutator checks. In the first and
third controls, the affine block at exceptional offset two fixes the first
parameter completely. The solver takes its fixed-prefix branch and restarts
at the next offset. In the second control the first parameter still varies,
but its integer step after adapting the full block lattice is two. The scalar
quadratic is solved in that lattice parameter, without replacing step two by
a rationally normalized step one. The third control also rejects two earlier
normalized leading branches by integer obstructions before finding a witness.

A separate GAP calculation compares the full integer nullspace of each of
the three block matrices with the exported kernel, using native integral
nullspaces and canonical Hermite forms. The lattices agree exactly. In both
fixed cases all first-offset components of the complete kernel vanish. In
the varying case the change between original and adapted bases is integral
with determinant +/-1, later columns have zero first-offset component, and
the first column has coordinate gcd two, agreeing with the recorded step.
Thus the check includes lattice completeness and the nonunit step, not just
rational spans or final witness acceptance.

All three affine block matrices have 86 rows and 53 columns. Their integer
kernel ranks are respectively zero, one and zero. The varying case gives
-84-52T-8T^2=-4(2T+7)(T+3), whose only integer root is -3; the other rational
root is -7/2. The integer parameter restriction is therefore visible in the
actual exported quadratic, rather than only in an abstract discussion.

The existing native group checker then reconstructs all three positive
witnesses, 464 actual correction columns in eight affine blocks, and one
exceptional quadratic at six integer parameters. It verifies the full later
column annihilation, scalar coefficients and complete integer root list.
The bounded trace is evidence about these interfaces, not an all-rank proof.

Both recorded jobs requested one CPU/eight decimal GB and ran sequentially.
Python took 20.437 seconds; GAP took 7.945 seconds. Both succeeded with empty
stderr. Log hashes and terminal PIDs were checked. The process observation
found 728 terminal receipts, an empty registry and no remaining workers in
its stated scope. Sources and outputs are bound in
`research/certificates/N8-general-lattice-branches/manifest-v1.json`.

The original N8 statement was rechecked in the preceding implementation turn;
it and the controlling proof were not changed here. No new candidate, novelty
claim, deadline change or outside mathematical review is asserted.
