# N5: higher-class native-group input

30 September 2026, within the original 48-hour window. Implement a missing
interface of the existing N5 candidate, without changing its count or novelty
assessment. This is not a claim to implement the entire higher-class algorithm.

For a native nilpotent pcp group G, compute its finite torsion subgroup T and
Q=G/T. Rebase Q along its upper central series in Smith normal form. Check that
every new relative order is infinite: abstract torsion-freeness does not imply
that an arbitrary pcp presentation has no finite relative orders. Retain and
check the direction of the rebasing isomorphism rather than relying on the
manual's description of its `bijection` field.

Apply Polycyclic's faithful unitriangular matrix representation to the rebased
group. Use finite rational matrix logarithms, check their linear independence,
dimension equal to Hirsch length, and closure under matrix commutators. Export
the resulting exact rational structure constants to the existing rational Lie
decomposition algorithm. Check exponential/logarithm round trips and native
group words. Treat the trivial rational completion separately.

Include abelian and finite controls, free nilpotent groups of classes three and
four, a product with different nilpotency classes, noncentral finite torsion,
and a torsion-free presentation that has a finite relative order. Use a second
implementation of the matrix series and coordinate recovery in Python, and
native GAP checks of the returned projection identities and ideal conditions.
Retain failed versions and negative controls. All mathematical runs go through
the bounded recorder; first budget one CPU, eight GB and 180 seconds per run.

The general rational-support preimages, finite-index search and integration
with the central-lifting solver remain separate tasks. Do not describe this
input interface as a full higher-class direct-decomposition decision program.
