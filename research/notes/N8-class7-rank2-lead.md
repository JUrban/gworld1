# N8(b): proposed rank-two class-seven extension

Derived 28 September 2026, approximately 14:27–14:29 UTC. Initially
an unvalidated proposal. Update at approximately 14:47 UTC: the proof
and independent computational checks are now in
`problems/N8/class7-rank2-proof.md` and `class7-rank2-audit.md`.
Correction to the exploratory shorthand below: the exact preserving
move is **x->yx**, not x->xy, for our commutator convention. The full
proof and implementation use the former. The original proposed
work list is retained below as provenance.

The previous class-six proof covers all leading layers but leaves a
nonzero degree-six correction kernel for factors of weights (1,4).
Its quadratic interaction first appears in degree seven. In rank two,
the kernel has dimension at most one: its projection into L2 is
injective, because the centralizer of a nonzero degree-one Lie element
has no degree-five part, and dim L2=1. Thus the remaining condition is
a univariate integer-valued quadratic lying in a fixed integer lattice.
Smith normal form decides this: nonzero equations in the free quotient
give finitely many integer roots; if all vanish identically, finitely
many residue classes modulo twice the torsion exponent suffice.

Other middle layers:

- Leading degree three: normalize the first correction by exact
  Nielsen moves, then use the proved degree-five injection. Corrections
  from degree six onward are jointly linear through class seven:
  factor correction weights start at 4 and 5, so their interaction and
  all repeated-correction terms are beyond degree seven.
- Leading degree four: the degree-five correction is unique. The
  remaining corrections start at weights (3,5) or (4,4), so their
  interactions are again beyond degree seven. Solve degrees six and
  seven jointly over the integers.
- Leading degree five, factor weights (2,3): the first correction
  map L3+L4 -> L6 has only the Nielsen direction (D,0). Indeed,
  [L3,L3] intersects [L2,L4] trivially, and both centralizer conditions
  then force U proportional to D and V=0. A proof can use homogeneous
  free generators of the derived free Lie algebra: its degree-three
  generators are independent of degree-two and degree-four ones.
  In rank two, this can also be verified by an explicit four-column
  tensor minor, yielding a short finite-dimensional proof. Enumerate
  the finitely many integral residues modulo the exact move x->xy.
  The final degree-seven correction is linear.
- Leading degrees six/seven use the existing penultimate algorithm;
  nonzero degree two uses the existing all-class IA procedure.

The bounded kernel probe in `scripts/probe_n8_class7_kernels.py`
checks examples in ranks two and three. Its samples do not establish
the all-rank (1,4) kernel bound. Restrict the proposed new complete
scope to rank two unless that additional theorem is proved.

Still needed: explicit quadratic-polynomial coefficient and periodicity
audit; full implementation; negative and nonprimitive examples;
independent GAP checks; a written proof and novelty review.
