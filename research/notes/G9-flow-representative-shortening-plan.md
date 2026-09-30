# Next possible G9 improvement: shorten representatives inside the same orbits

30 September 2026. This is a research plan, not an additional bound.

The successful two-ended completion assigns a word cost by inserting
horizontal powers into retained bridge words. Its central rectangles
contain 62,003 actual representatives, some longer than the original
length-14 search. These can have cancelling detours in their lattice
flows. No new orbit or larger exhaustive ball is needed to investigate
whether those costs can be lowered.

For one representative, retain its full traversed undirected edge graph
and its integer net flow. Start with the directed multigraph containing
each nonzero-flow edge in its prescribed direction and multiplicity.
If its underlying support is disconnected, add both directions of a
selection of zero-flow edges from the original traversed graph sufficient
to connect the support. A spanning forest, with irrelevant leaves pruned,
always supplies such a selection. Every such edge already appeared at
least twice in the original word, so this construction does not increase
the word cost. Nonzero-flow edges need no extra cancelling pairs.

The directed degree imbalance is still exactly the original endpoint
minus the origin. Connectedness therefore supplies an Euler trail with
the same net flow. All chosen edges come from the original strict bridge
strip; the origin has only its initial upward edge, so the trail is also
a strict bridge. It represents the same atom by flow faithfulness.
This is a constructive shortening procedure, not a global geodesic
algorithm or a solution to a Steiner optimization problem.

First check whether this shortens any of the existing central words. If
it does, retain every new representative and exact full-flow equality,
then minimize the Manhattan cost envelope over the enlarged finite seed
set. The same normalized cores and rectangle/strip/quadrant formula apply.
Recompute exact coefficients and rational inequalities, verify that the
original counts through degree 14 are unchanged, and separately reconstruct
the new finite evidence in GAP before claiming another improvement.

Do not assume connected nonzero support, discard necessary connectors,
or equate a raw absolute-flow norm with the length of a realizable word.
The special height-one family remains separate. Preserve the already
successful two-ended certificate and bound in all cases.
