# G9: completing both horizontal boundaries of a bridge atom

30 September 2026, approximately 07:38–07:48 UTC, within the original
48-hour experiment. This supplements the [one-ended completion](horizontal-completion-proof.md)
and uses exactly the same 21,483 retained atom representatives.

**Improved candidate rank-two enclosure, standard generators:**

```
2.676836909 <= lambda_2 <= 2.943737759.
```

The exact constant remains undetermined; G9 stays a partial candidate.
The upper bound is unchanged. Neither optimality nor novelty is asserted,
and independent specialist review remains pending.

## 1. A two-parameter action on atoms

Use the faithful integral lattice-flow model and the atom factorization
theorem in the [flow proof](flow-growth-proof.md). Write a for the vertical
generator and b for the horizontal generator. A strict bridge starts at
(0,0), has positive height after the initial vertex, and ends at its
maximum height H. Its first letter is necessarily a. Its net vertical
flow at height zero is exactly the single edge from (0,0) to (1,0).
An atom has no internal level with just one nonzero vertical edge.

For H>=2, define

```
P_(k,l)(w) = a b^k a^-1 w b^l,       (k,l) in Z^2.
```

Cancel the displayed a^-1 against the initial a of w. The resulting
representative starts with a, walks k horizontally at height one, follows
the rest of w translated horizontally by k, and walks l horizontally at
height H. Its length as a displayed word is |w|+|k|+|l|. Free reduction
could shorten it; no global geodesicity is assumed.

This representative is a strict bridge of height H. Every internal
vertical-edge support is translated by k, so the atom property is
preserved. Moreover P_(k,l) P_(k',l') = P_(k+k',l+l') as operations on
group elements: the left multipliers multiply by cancellation of a^-1 a,
and the right multipliers are powers of b. Thus this is a Z^2 action.

## 2. Exact orbit classification

Given such an atom flow, delete its fixed initial vertical edge and every
horizontal edge at heights one and H. Among the remaining vertical edges
based at height one, let x be the smallest horizontal base coordinate
with nonzero coefficient. This set is finite and nonempty: its total
upward flux is one. Translate the horizontal coordinates of all remaining
edges by -x. Call the resulting flow, together with H, the **normalized
core**. If the endpoint was (H,y), record the coordinates

```
(x,z) = (x,y-x).
```

Under P_(k,l), the normalized core is unchanged and

```
(x,z) -> (x+k,z+l).                                  (1)
```

Indeed all retained edges translate horizontally by k, and the endpoint
changes from (H,y) to (H,y+k+l).

Conversely, suppose two atoms have the same normalized core. Use (1) to
make their two coordinates agree. Their remaining edges now agree, their
initial vertical edges agree, and their endpoints agree. The difference
of their full flows is therefore a finitely supported flow of boundary
zero supported on the two horizontal lines at heights one and H. These
lines are disjoint because H>=2. On each line, a finitely supported
circulation is zero: a line is a tree, or equivalently the edge
coefficients must be constant and vanish outside a finite interval.
The full flows consequently agree. Faithfulness of the metabelian flow
model gives equality of the group elements.

Thus **normalized cores classify these orbits exactly**, and each orbit
contains exactly one atom for every integer coordinate pair. In
particular the action is free: (1) forces k=l=0 for a stabilizer.
This proves disjointness of the infinite families; checking only finitely
many representatives would not prove that assertion.

Height one is separate. A strict bridge ending at height one has only
horizontal steps after its initial a, so it represents a b^m for one
integer m. These atoms form one disjoint family with cost 1+|m| and series

```
t + 2t^2/(1-t).                                      (2)
```

Their height distinguishes them from all the preceding families. The
two-line argument is never applied when its lines coincide.

## 3. Exact cost series of a complete orbit

For a normalized core, retain the old representative coordinates
(x_j,z_j) and their word costs c_j. At any integer (x,z), choose a
representative obtained by the action from one of these inputs, of cost

```
f(x,z) = min_j (c_j + |x-x_j| + |z-z_j|).             (3)
```

All minimizing choices give the same group element by the orbit theorem.
Let [L,U] x [D,V] be the smallest integer rectangle containing all the
retained coordinate pairs. Outside this rectangle, clamp each coordinate
to the corresponding interval. If (x',z') is the clamped point, then

```
f(x,z) = f(x',z') + |x-x'| + |z-z'|.                 (4)
```

Every retained point lies inside the rectangle, so the same additive
outside distance can be removed from every term of the minimum (3).
This proves (4) for arbitrary displacements, not just sampled controls.

The orbit series is the sum of three disjoint contributions:

1. For every integer point of the rectangle, include t^f(x,z).
2. For each point on each of the four sides, include
   t^(f(x,z)+1)/(1-t) for the exterior strip normal to that side.
3. For each of the four corners, include
   t^(f(x,z)+2)/(1-t)^2 for its exterior quadrant.

The strips include only points whose other coordinate remains in its
closed interval. The quadrants have both coordinates strictly outside.
These conventions prevent boundary overlap. If an interval has width
zero, its two opposing exterior directions still give distinct strips;
the same convention applies to its corners.

Add these series over all distinct normalized cores, and add (2). The
result is the exact cost series of a specified alphabet of distinct
atoms, with actual representatives:

```
F(t) = C(t) + S(t)/(1-t) + Q(t)/(1-t)^2.              (5)
```

C,S,Q are finite polynomials with nonnegative integer coefficients.
This is an atom-alphabet cost series, not the group's growth series.
The full one-ended completion is included, because its representatives
are the special case k=0. The new choice of costs can only shorten the
available representative for each of its elements.

All these atoms freely generate a monoid by the earlier factorization
theorem. The finite-subalphabet exhaustion argument in the one-ended
proof therefore applies without change: if R in (0,1) is the unique
root F(R)=1, then lambda_2 >= 1/R. Nonnegative coefficients make F
strictly increasing, and already (2) diverges as t approaches one.

## 4. The finite certificate and numerical inequality

The original inputs comprise 27 height-one atoms and 21,456 others.
The latter split into **3,239 distinct two-parameter orbits**. Their
central rectangles contain 62,003 integer points. Including the
height-one family, the coefficients through degree 14 agree exactly
with the original exhaustive atom certificate. In degrees 15 and 16
the completed alphabet has respectively 26,417 and 41,097 letters.
No larger bridge-word enumeration was performed.

The [certificate](../../research/certificates/G9-two-ended-completion-v1/certificate.json)
retains every normalized core, original representative index, coordinate,
central cost and chosen representative, together with C,S,Q. As a compact
additional specification, the coefficients of

```
N(t) = (1-t)^2 C(t) + (1-t) S(t) + Q(t)
```

in ascending degree order, including zeros, are

```
[0,1,0,-1,0,0,4,16,25,46,88,259,744,1955,4795,5455,
 1293,-811,-575,-257,-264,-113,63,-54,224,-18,81].
```

Some coefficients of N are negative because of the denominator clearing;
the defining C,S,Q and the actual series coefficients remain nonnegative.
Both implementations establish with exact rational/integer arithmetic

```
F(1000000000/2676836909) >= 1,
F(1000000000/2676836910) < 1.
```

Thus 1/R lies in [2.676836909,2.676836910). Only its lower endpoint gives
a lower bound for the group growth constant. The upper endpoint of this
short root interval is **not** a group-growth upper bound. The group upper
bound 2.943737759 still comes from its separate forbidden-subword proof.

## 5. Independent implementation checks and limitations

The [Python exporter](../../scripts/certify_g9_two_ended_completion.py)
recomputes the original flows, verifies atom conditions, and constructs
the finite orbit data. It checks the full-flow equality from an orbit's
first input to each of its retained inputs, every central representative,
two controls along each exterior strip, two controls in each exterior
quadrant, and an action-composition control for every orbit.

The [GAP checker](../../scripts/check_g9_two_ended_completion.g) separately
reconstructs flows directly from signed generator words and checks the
complete partition and distinctness of cores. It reproduces all 21,456
full-flow orbit equalities, 27 height-one inputs, 62,003 central atoms,
83,144 strip controls, 25,912 quadrant controls and 3,239 composition
controls. It also recomputes every finite coefficient, the degree-14
comparison and the two rational inequalities. The original atom words
retain their earlier native Magnus-polynomial verification.

Both jobs passed on their first invocation, with empty stderr. The Python
job took 14.116 seconds and GAP took 11.506 seconds; they ran sequentially,
each with one CPU and a 6 GB per-process limit. Their commands, exit
statuses, timestamps and output hashes are retained in
`results/G9-two-ended-completion-v1/` and
`results/G9-two-ended-completion-gap-v1/`.

The finite controls check implementation and artifact consistency. The
infinite orbit classification, geometric sums and growth implication
depend on the written arguments above and the preceding atom theorem.
The proofs were audited by the same research agent, not an outside
specialist. No full formal verification, new problem count, exact growth
constant, exhaustive literature clearance or general nonabelian-deck
extension of this particular completion is claimed. The original
statement and existing bibliographic audit remain controlling.
