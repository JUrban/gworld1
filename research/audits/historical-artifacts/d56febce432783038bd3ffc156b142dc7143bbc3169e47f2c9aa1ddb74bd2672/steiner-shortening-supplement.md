# G9: better connections between flow components

30 September 2026, within the original experiment. This supplements the
[flow-shortening construction](flow-shortening-supplement.md) and the
[two-ended atom completion](two-ended-completion-proof.md).

**Current candidate enclosure:**

```
2.676880030 <= lambda_2 <= 2.943737759.
```

The lower endpoint improves from 2.676871486 by finding 34 additional
shorter representatives in the same atom families. The upper bound and
the general computability argument are unchanged. The exact constant and
novelty remain unresolved; G9 stays one partial-entry candidate.

## 1. A finite connection problem

For a strict bridge flow f of height H, let its required vertices be the
endpoints of its nonzero edges. Let xmin,xmax be their minimum and maximum
horizontal coordinates. Use the finite grid with vertices

```
{(0,0)} union { (h,x) : 1<=h<=H, xmin<=x<=xmax }.
```

The origin has only its required initial upward edge. Contract each
connected component of the nonzero-flow support. These contracted vertices
are the required terminals. Every remaining grid edge has unit cost and
represents a possible zero-flow connector. Parallel edges may be replaced
by one retained original edge: they connect the same support components
and have the same cost. Edges within a contracted component are unnecessary.

Find a minimum set of connector edges joining the terminals in this finite
graph. If k such edges are selected, retain all signed nonzero-flow edges
with their multiplicities and add both directions of every connector.
Exactly as in the preceding supplement, a directed Euler trail then gives
the original flow with length

```
sum_e |f(e)| + 2k.                                           (1)
```

It stays a strict bridge: its only visit to height zero is the origin,
and its endpoint remains at height H. Hence it represents the same atom.

The old traversed-path connector choice supplies a comparison. If it leaves
the displayed horizontal interval, clamp its horizontal coordinates into
that interval. Required vertices and support edges stay fixed; connector
edges either remain edges or collapse, and the resulting network still
connects all required components. Discarding duplicates and cycles cannot
increase its cost. Thus the finite minimum cannot be worse than the previous
connector choice. The implementation also checks this against each actual
previous cost.

## 2. The finite subset recurrence

After contraction, all graph edges have unit cost. For a nonempty subset S
of terminals and graph vertex v, let D(S,v) be the minimum number of edges
in a connected subgraph containing S and v. A singleton row is a shortest
path calculation. For larger S, merge two proper nonempty subsets at a
common vertex u and then apply shortest-path closure:

```
D(S,v) = min_{S=A disjoint-union B, A,B nonempty, u}
               D(A,u) + D(B,u) + distance(u,v).               (2)
```

Any construction on the right is a connected network for the left, after
discarding duplicate edges, so D(S,v) is no larger. For the reverse
inequality take a minimum tree spanning the required vertices and v.
Starting at v, either v is a terminal or one reaches a first terminal or
branch vertex u. Split the remaining terminal set there into two nonempty
parts, using the singleton terminal at u as one part when necessary.
The two subtrees and the path to v partition this tree's edges. Their
lengths dominate the three terms in (2), proving the reverse inequality.

The [implementation](../../scripts/g9_steiner_shortening.py) stores merge
and path predecessors and reconstructs the connector edges. It explicitly
checks their number, connectivity, literal Euler word and full flow.
Finite caps reject oversized graphs; they never imply a negative answer.
The recorded graphs have at most 21 contracted vertices and four required
components, well inside those caps.

This exactness concerns the displayed finite graph. The growth certificate
below only needs the literal representatives and their lengths; it does
not require the optimality of this recurrence, or a global group-geodesic
claim. There is no claim that the resulting rational alphabet is optimal.

## 3. Retained representatives and bound

The calculation uses the same 62,003 central orbit elements:

| Nonzero support components | Elements |
| --- | ---: |
| 1 | 39,648 |
| 2 | 19,800 |
| 3 | 2,551 |
| 4 | 4 |

It retains all 286 earlier improvements and finds 34 more. All 320
shorten their original representatives by two letters and still have
length greater than 14. The certificate binds each literal word to its
original seed index, orbit coordinate, old cost, previous best cost and
selected connector edges. There is no expansion to longer enumerated
bridge words or new normalized atom cores.

Add these 320 seeds to the original 21,483. Recomputing the same minimum
Manhattan envelopes gives 21,803 seeds in the same 3,239 two-parameter
orbits, plus the original height-one family. The rectangle/strip/quadrant
formula remains

```
F(t) = C(t) + S(t)/(1-t) + Q(t)/(1-t)^2.
```

The ascending coefficients of N(t)=(1-t)^2 F(t) are

```
[0,1,0,-1,0,0,4,16,25,46,88,259,744,1955,4795,5497,
 1357,-849,-655,-297,-216,-77,31,-54,224,-18,81].
```

The coefficients through degree 14 still match the original exhaustive
certificate. Degrees 15 and 16 now have 26,459 and 41,245 alphabet elements.
Exact rational evaluation gives

```
F(1000000000/2676880030) >= 1,
F(1000000000/2676880031) < 1.
```

Thus the reciprocal alphabet root lies in [2.676880030,2.676880031).
The existing free-concatenation argument gives the stated group lower
bound. The upper endpoint of this root interval is not a group-growth
upper bound; 2.943737759 comes from the separate earlier certificate.

## 4. Checks and limitations

Before processing the words, the subset routine is compared with exhaustive
edge-subset search on all 64 simple graphs on four vertices and all 15
nonempty terminal sets: 960 controls, including disconnected inputs. The
entire 62,003-word pass then verifies flows and strict-bridge properties.

The [GAP replay](../../scripts/check_g9_steiner_completion.g) does not run
or trust the connection algorithm. It checks all 320 literal replacements
against their original full flows, the original seed prefix, all 21,776
height-at-least-two seed orbit equalities, 27 height-one seeds, 62,003 central
representatives, 83,144 strip controls, 25,912 quadrant controls and 3,239
action controls. It separately reconstructs all coefficients and rational
inequalities. This uses a distinct native GAP flow implementation.

Four sequential jobs, each one CPU and a 6 GB per-process limit, passed
with empty stderr:

| Job | Seconds |
| --- | ---: |
| `G9-steiner-shortening-v1` | 18.281 |
| `G9-steiner-seeds-v1` | 0.921 |
| `G9-steiner-completion-v1` | 14.168 |
| `G9-steiner-completion-gap-v1` | 11.808 |

The exporter and completion checkers are preserved variants of the previous
shortening pipeline, with fresh paths. Older proofs, certificates and source
versions remain intact. The original problem page, exact G9 fragment and
background were reread, and the retained statement rendering was viewed.

This is an internally derived refinement with separate computational
reconstruction. It does not constitute outside mathematical review, a
complete solution of G9, or an additional counted problem.
