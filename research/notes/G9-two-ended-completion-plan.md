# Possible next G9 extension: two independent boundary displacements

30 September 2026, after the successful terminal-horizontal completion.
This is a proposed next construction, not an established numerical bound.

For a strict rank-two bridge word w of height H>=2, its first letter is a.
Consider

```
P_(k,l)(w) = a b^k a^-1 w b^l.
```

Cancel the adjacent a^-1 a in this displayed representative. The path
first goes to height one, walks k horizontally, follows the original
remaining path translated by k, then walks l horizontally at height H.
It remains a bridge atom: every internal vertical-edge support is merely
translated. The representative cost is |w|+|k|+|l|.

Delete the fixed initial vertical edge and all horizontal edges at heights
one and H. The remaining flow includes the nonempty vertical flow across
level one. Let x be the minimum horizontal base coordinate among its
nonzero level-one vertical edges. Normalize all remaining horizontal
coordinates by subtracting x. Retain H and this normalized core.
Record two coordinates (x, y-x), where (H,y) is the terminal endpoint.

The proposed orbit classification is: equal normalized cores are exactly
the P_(k,l) orbits. The operation translates those two recorded coordinates
independently by k and l. Once the internal edges and endpoints agree,
the difference of two flows is supported on the two disjoint boundary
horizontal lines; the boundary equation should force each to be a
finitely supported circulation and hence zero. H=1 must be separate:
there is just the familiar family a b^m, with cost 1+|m|.

For finitely many retained representatives in one orbit, with coordinate
pairs (x_j,z_j) and costs l_j, use

```
f(x,z) = min_j (l_j + |x-x_j| + |z-z_j|).
```

On the bounding rectangle, enumerate these finite costs. Each of the four
exterior strips contributes a geometric tail with denominator 1-t; each
of the four exterior quadrants contributes a double tail with denominator
(1-t)^2. This would give a rational generating function for the full
two-parameter alphabet, and another certified lower bound using the same
original atoms. No larger bridge enumeration is needed.

Before any claim, verify exact core classification, the rank-one boundary
exception, independence of the two actions and every overlap convention.
Check that the coefficients through degree 14 match the original finite
certificate. Independently reconstruct orbit records, selected actual
representatives and rational inequalities in GAP. Retain the successful
one-ended bound and evidence regardless of this proposal's outcome.
