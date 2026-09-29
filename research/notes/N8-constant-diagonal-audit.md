# Constant-matrix arithmetic and class26 performance checkpoint

The first delayed-quadratic constructor reached the quadratic group samples
and then stalled in the generic polynomial Smith routine. Its1200-second
timeout, diagnostics and exact constructor/arithmetic source are retained.
The first independent GAP quotient preflight constructed the torsion-free
weighted quotient of Hirsch length680 but reached its600-second limit while
building native multiplication polynomials. It is not a passed preflight.

For a constant rational matrix, every nonzero polynomial Smith invariant is
a unit. The new n8_constant_diagonal.py computes equivalent diagonal ones by
exact rational row reduction of [A|I], followed by a pivot-column permutation
and an invertible shear. It verifies U A V=D and nonsingularity exactly with
FLINT. The integer decision algorithm still uses the original integer matrix;
this optimization does not replace any integer lattice by its rational span.
The family constructor also uses the existing checked FLINT rank/determinant
identities rather than repeating large SymPy calculations.

The existing24-system integer suite passes2040 specializations; its independent
GAP replay passes. The11-system complete-family suite passes671 specializations;
independent GAP checks its full integer kernels/sections and complete arithmetic.
All5 new arithmetic runs pass. These repeats are regression checks for a changed
arithmetic implementation, not additional mathematical examples.

The second class26 constructor uses this optimization and saves its arithmetic
input before the family decision. The second native group preflight saves its
quotient workspace before multiplication-polynomial construction and has a
1800-second cap. Those two runs are live at this checkpoint. Workspace files
are ignored local caches under large-artifacts; no omitted cache is described
as a committed certificate. Their hashes and regeneration command will be
recorded once a complete cache exists.

The three-exception draft now spells out the full Smith quotient, every torsion
coset, the first-exception gcd step and the rank-one integer Bezout change.
A specialized ambient period-lattice constructor and independent native GAP
checker are prepared but not yet run. Neither these sources nor the five
arithmetic passes promote N8 scope. Current adopted partial scope remains
fourteen final layers/all targets through class24 and earlier arbitrary-class
families; the class26/three-exception proposal is still unadopted.
