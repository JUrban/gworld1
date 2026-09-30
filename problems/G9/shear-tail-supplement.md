# G9: disjoint Nielsen-shear tails of the atom alphabet

30 September 2026, within the original experiment. This supplements the
[two-boundary completion](two-ended-completion-proof.md) and its
[shortened representatives](steiner-shortening-supplement.md), using the
same retained seeds. No larger bridge-word enumeration is performed.

**Current candidate enclosure, standard rank-two generators:**

```
2.676891785 <= lambda_2 <= 2.943737759.
```

The new lower endpoint improves 2.676880030. The independent upper bound,
general approximation theorem and partial status of G9 are unchanged.
The exact growth constant and novelty remain unresolved; the proof and
computational reconstruction still require outside specialist review.

## 1. Three commuting operations on atoms

Use the faithful integral lattice-flow model and the free atom-monoid
theorem from the [flow proof](flow-growth-proof.md). Write a for the
vertical generator and b for the horizontal generator. The two-boundary
operations are

```
P_(s,t)(w) = a b^s a^-1 w b^t.
```

Their displayed bridge representatives cancel a^-1 against the first a
of w. They form a Z^2 action preserving height and atom status.

For each integer k, let alpha_k be the Nielsen automorphism

```
alpha_k(a)=a b^k,       alpha_k(b)=b.
```

It descends to the free metabelian group and has inverse alpha_(-k).
On a lattice vertex of height h it changes the horizontal coordinate x
to x+hk. In particular, a vertical edge based at (h,x) becomes a vertical
edge based at (h,x+hk), with additional horizontal steps at height h+1.
For a downward letter, the horizontal steps precede the downward edge
and give the same edge transformation with the opposite orientation.

Thus alpha_k sends strict bridge words to strict bridge words of the
same height, translates each level's vertical flow support, and preserves
the atom condition. Cancellation of horizontal flow does not affect this
vertical-support assertion. If a chosen word has length c and V vertical
letters, its literal substituted word has length c+V|k|; reduction can
only improve that upper cost.

These operations commute because
alpha_k(a b^s a^-1)=a b^s a^-1 and alpha_k(b^t)=b^t.
Together they give a Z^3 action on atoms. We use only height H>=3 below.

## 2. A full-flow normal form for these orbits

Let x1 and x2 be the minimum horizontal base coordinates of nonzero
vertical flow at internal levels one and two. Both exist: the total
upward flux at each such level is one. If the endpoint is (H,y), put

```
d = x2-x1,
u = x1-d,
v = y-x1-(H-1)d.
```

Under P_(s,t), the triple (u,v,d) becomes (u+s,v+t,d). Under alpha_k,
we have x1 -> x1+k, x2 -> x2+2k and y -> y+Hk, so the triple becomes
(u,v,d+k). In particular the action is free.

Apply alpha_(-d) followed by P_(-u,-v) to the atom and retain its **full
integral flow**, together with H. Call this its normalized flow. All three
coordinates are then zero. Commutativity and the coordinate transformations
show that normalized flow is invariant on an orbit. Conversely, equality
of normalized flows implies equality of the normalized group elements by
the faithful flow model; undoing the two normalizations gives membership
in the same orbit. Hence the invariant classifies the Z^3 orbits exactly.
Each orbit contains one atom for every integer triple (u,v,d).

This argument keeps the full flow; it does not discard horizontal edges
on an extra internal line or assume that a finite sample proves orbit
distinctness. Height one and two are retained only in the old alphabet.

## 3. New tails disjoint from the entire old alphabet

The previous alphabet completes each retained two-boundary orbit in both
integer boundary directions. Inside a fixed shear orbit, each of those
old orbits is therefore exactly one plane d=d_j, with every u,v allowed.
There are finitely many occupied d_j, obtained from the retained seeds.
Let l and m be their minimum and maximum.

For a positive tail choose one seed with coordinates (u0,v0,d0), length c
and V vertical letters. For n>=0 apply the shear

```
k = m+1-d0+n.
```

Then complete both boundary directions using P_(s,t), s,t arbitrary
integers. The resulting coordinates and literal costs are

```
(u0+s, v0+t, m+1+n),
c + V(m+1-d0+n) + |s| + |t|.
```

Every letter lies outside every old plane. For the negative tail use
k=l-1-d0-n, with cost c+V(d0-l+1+n)+|s|+|t|. The two tails are disjoint,
and different normalized flows give disjoint families. Unoccupied planes
between l and m are not added; their omission has no effect on this lower
bound. A seed is selected once per tail, minimizing its initial cost among
the retained choices; global optimality is not needed.

Writing L for that initial cost, one tail contributes exactly

```
t^L/(1-t^V) * ((1+t)/(1-t))^2                         (1)
```

to the chosen alphabet's cost series. The two horizontal factors count
all integers with cost their absolute value. Distinctness comes from the
orbit theorem, so (1) is an exact specified-alphabet series, not a count
of possibly coincident representatives or of all group elements.

## 4. Certificate and rational inequality

Of the 21,803 retained seeds, 27 have height one, 8,658 have height two,
and 13,118 have height at least three. The latter represent 2,803 old
two-boundary orbits, grouped into 1,453 shear orbits. The 2,906 selected
tails have these parameters:

| V | L | Number of tails |
| ---: | ---: | ---: |
| 7 | 19 | 80 |
| 7 | 20 | 236 |
| 7 | 21 | 1,658 |
| 9 | 22 | 68 |
| 9 | 23 | 448 |
| 10 | 22 | 6 |
| 10 | 23 | 48 |
| 10 | 24 | 362 |

Let F_old(t) be the complete shortened series in the preceding supplement.
The new series is

```
F(t) = F_old(t) + ((1+t)/(1-t))^2 * (
        (80t^19 + 236t^20 + 1658t^21)/(1-t^7)
      + (68t^22 + 448t^23)/(1-t^9)
      + (6t^22 + 48t^23 + 362t^24)/(1-t^10)).
```

All added coefficients are nonnegative; the first addition is 80 letters
of cost 19. In particular the original exhaustive counts through degree
14 are unchanged. Exact rational arithmetic gives

```
F(1000000000/2676891785) >= 1,
F(1000000000/2676891786) < 1.
```

The reciprocal root therefore lies in [2.676891785,2.676891786).
Every finite subset of this distinct atom alphabet generates a free
monoid. Exhausting the alphabet by finite subsets gives lambda_2 at least
the reciprocal root, as in the earlier completion proof. Only the lower
endpoint bounds group growth from below. The upper endpoint of this root
interval is not a group-growth upper bound.

## 5. Separate reconstruction and limits

The [Python certificate generator](../../scripts/certify_g9_shear_tails.py)
retains full normalized flows, every relevant seed and its coordinates,
every old-orbit assignment, chosen tail seeds, costs, series and exact
rational evaluations. It checks tail parameters n=0,1,3 with boundary
shifts (0,0),(-2,1),(1,-2), and action composition/inversion controls.

The [GAP checker](../../scripts/check_g9_shear_tails.g) computes integral
flows separately from literal words, without calling Python. It checks
every normalized seed, complete coverage of the old height-at-least-three
orbits, uniqueness of their occupied coordinates, every selected tail
cost, 26,154 literal tail/boundary controls and 2,906 shear composition
controls. It reconstructs the rational series, its first 41 added
coefficients and both rational inequalities. The infinite disjointness
and growth implications remain the written arguments above.

The two sequential jobs each reserve one CPU and a 6 GB per-process limit.
Python passes in 14.820 seconds and GAP in 11.607 seconds, both with empty
stderr. Their source, input, output and process bindings are retained in
the [manifest](../../research/certificates/G9-shear-tails-v1/manifest-v1.json).
The full original growth page, exact G9 fragment and background were
reread, and the archived statement rendering was actually viewed.

The flow model, atom argument and credited prior support-connection
construction retain their earlier attributions. This supplement adds
specified atom families; it claims neither a new general geodesic theorem
nor novelty clearance, full resolution of G9 or external validation.
