# G9: shorter representatives in the completed atom families

30 September 2026, within the original experiment. This supplements the
[two-ended completion](two-ended-completion-proof.md); its orbit theorem,
infinite-alphabet argument and independent upper bound are unchanged.

**Current candidate enclosure:**

```
2.676871486 <= lambda_2 <= 2.943737759.
```

The improvement from 2.676836909 is small and concerns representative
costs within exactly the same infinite atom families. The exact constant,
optimality and novelty remain unresolved; G9 remains a partial candidate.

## 1. Removing flow-cancelling detours

Let w be a strict bridge representative and let f be its integral edge
flow. Retain the finite undirected graph of all edges traversed by w,
including edges whose net coefficient is zero. The absolute-flow norm

```
sum_e |f(e)|
```

need not by itself be the length of a representative: its nonzero support
can be disconnected. Necessary connections must not be discarded.

Start instead with the directed multigraph having |f(e)| copies of each
nonzero edge, oriented with the sign of f(e). Contract its undirected
connected components and retain the other vertices of the original
traversed graph. The remaining zero-flow edges connect this finite graph.
Choose a spanning tree there, then prune any leaf vertex that contains no
nonzero-flow support. Equivalently, the implementation first unions all
nonzero edges, adds zero-flow edges by a deterministic spanning-forest
procedure, and prunes irrelevant leaves.

For every selected connector edge, add both directions to the directed
multigraph. Its underlying graph is now connected and its vertex
imbalances still equal the original endpoint minus the origin. It has
an Euler trail from the origin to the endpoint. One way to see the usual
directed Euler criterion here is to add an edge from the endpoint to the
origin: the balanced weakly connected directed graph is strongly connected
on its nonisolated vertices, so it has an Euler circuit. Removing the
extra edge gives the desired trail.

This trail has length

```
sum_e |f(e)| + 2 * (number of selected connector edges).       (1)
```

Every selected zero-flow edge was traversed at least once in each
direction by w, and every nonzero edge was traversed at least |f(e)|
times. Thus (1) is at most |w|. The new trail has the same flow as w.

Every used edge belongs to the original strict bridge strip. The origin
has only its initial upward edge; no added connector meets height zero.
Consequently the new trail also remains strictly above zero after its
first step and ends at the original maximum height. It is a bridge with
the same flow, hence the same atom and group element.

This gives a valid shortening construction. It is not asserted to solve
a shortest Steiner-connection problem, to find globally shortest group
words, or even to improve every nonminimal representative.

## 2. Finite replacements and complete families

The [shortening program](../../scripts/g9_flow_shortening.py) was applied
to all 62,003 central representatives from the preceding completion.
It retained necessary connectors in 22,355 cases and shortened 286
representatives by two letters each. The other 61,717 costs did not
improve under this procedure. All full-flow equalities and strict-bridge
conditions were checked.

The 286 improved representatives all have length greater than 14. Each
is retained with its old orbit, coordinate, original word index, old
cost, new cost, literal signed word and connector list. They are added
as seeds to the original 21,483 words; they introduce no new normalized
core. The resulting 21,769 seeds still give 3,239 two-parameter orbits
and the single height-one family.

Recompute the minimum Manhattan cost envelope over this enlarged finite
seed set. The same rectangle/strip/quadrant argument gives

```
F(t) = C(t) + S(t)/(1-t) + Q(t)/(1-t)^2.
```

The integer rectangles are unchanged because every added seed lies in
an old central rectangle. Some best central and exterior representatives
improve. The coefficients through degree 14 still agree exactly with
the original exhaustive certificate. Degrees 15 and 16 now have 26,453
and 41,213 letters respectively.

The [new certificate](../../research/certificates/G9-shortened-completion-v1/certificate.json)
retains all finite orbit data and C,S,Q. The coefficients, in ascending
degree order, of N(t)=(1-t)^2 F(t) are

```
[0,1,0,-1,0,0,4,16,25,46,88,259,744,1955,4795,5491,
 1337,-839,-635,-301,-216,-77,31,-54,224,-18,81].
```

Exact arithmetic gives

```
F(1000000000/2676871486) >= 1,
F(1000000000/2676871487) < 1.
```

The reciprocal root of F(t)=1 therefore belongs to
[2.676871486,2.676871487). Free concatenation of the distinct atom
alphabet gives the stated group-growth lower bound. As before, the
upper endpoint of this root interval is not a group-growth upper bound.

## 3. Verification and reproducibility

Four sequential recorded jobs, each one CPU and a 6 GB per-process limit,
passed with empty stderr:

| Job | Scope | Seconds |
| --- | --- | ---: |
| `G9-flow-shortening-probe-v1` | All 62,003 central words; preserve support connections and verify flows | 13.666 |
| `G9-shortened-seeds-v1` | Bind the 286 replacements to their original representatives | 0.922 |
| `G9-shortened-completion-v1` | Recompute the entire rational cost envelope and inequalities | 14.265 |
| `G9-shortened-completion-gap-v1` | Independently reconstruct all seed flows, costs and inequalities | 11.809 |

The [GAP checker](../../scripts/check_g9_shortened_completion.g) reads the
original words and old orbit record as well as the new certificate. It
verifies that the original 21,483 words are unchanged and checks every
new word against the full flow of its specific old representative.
It does not trust the Python shortening heuristic or connector choices.
It then checks all 21,742 height-at-least-two seed orbit equalities,
27 height-one seeds, 62,003 central words, 83,144 strip controls,
25,912 quadrant controls, 3,239 action controls, all finite coefficients
and the exact rational inequalities.

The exporter and GAP envelope-checker variants reuse the corresponding
two-ended implementations, with separate preserved source files and
input paths. Their independence is between the Python and GAP flow
implementations, not between two unrelated experimental teams. The older
certificates and bounds remain intact.

Replay the four scripts through `scripts/run_recorded.py` in the order
shown, using fresh output directories and updating dependent input paths
consistently. The source manifests retain the exact successful paths and
commands. The retained words allow a reviewer to verify the improved
bound without accepting the optimality of any shortening procedure.
There is no new exhaustive word search, formal proof, external review,
novelty clearance or additional counted problem in this supplement.
