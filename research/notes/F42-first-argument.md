# F42: first extremal graph argument

Recorded during the active run on 28 September 2026, approximately 10:09 UTC. This is an unverified research note, not a counted solution. Literature and rendered-source checks are pending.

Let r >= 2 and q=2r-1. Tentative answer for both sphere and ball:

- n=2m+1: maximum r q^m;
- n=2m, m>=1: maximum q^m.

For r=1 the answer is 1 when n>=1; for n=0 it is 0.

Take an independent set of words of length <=n and its folded based core graph. Its rank equals the size of that set, since the words are a free basis of their subgroup. The graph is covered by the corresponding based loops. Every vertex is within floor(n/2) of the basepoint.

Odd upper bound: the number of vertices is at most 1+2r(1+q+...+q^{m-1}); degree at most 2r gives rank <=(r-1)V+1 = r q^m.

Odd construction: take the full radius-m tree in the free-group Cayley graph. All missing labelled incidences lie on its outer sphere. For each generator match missing outgoing edges to missing incoming edges arbitrarily. This produces a finite connected covering of the rose, with every extra edge joining two leaves. The tree is a spanning tree. Every fundamental generator has reduced length 2m+1, and there are r q^m such generators.

Even upper bound: write a for the vertices at distance <m, b for the vertices at distance m, t for edges internal to the first set and c for cross edges. There are no edges between distance-m vertices, since an edge in a based loop of length <=2m must have one endpoint at distance <=m-1. The inner induced graph is connected, so t>=a-1; its degrees give 2t+c<=2ra; outer degrees give c<=2rb. Thus
rank=t+c-a-b+1 <= t+(1-1/(2r))c-a+1 <= ((r-1)(2r-1)/r)a+(2r-1)/r.
The ball bound a<=(r q^{m-1}-1)/(r-1) gives rank<=q^m.

Even construction: take the full radius-(m-1) tree. There are q^{m-1} missing outgoing slots, and the same number of missing incoming slots, for each of the r labels. Add q^{m-1} new vertices. Bijections attach one outgoing/incoming slot of each label at every new vertex. All new edges join the old boundary to the new vertices, and the graph is a connected covering. Choose one incident edge per new vertex to extend the old tree to a spanning tree. All non-tree edges then yield reduced based words of length 2m. Their number is q^m.

Items to check: loop coverage after folding/core trimming, based tails, reducedness of Schreier basis words, n=1 and n=2 construction endpoints, exact formula for missing slots, literature on maximum free independent subsets of balls/spheres, possible known result or prior formulation by Dotsenko.

## Literature check outcome

The full answer was already published as a preprint before this run: Lucy Koch-Hyde and Éamonn Olive, arXiv:2609.00382v2 (3 September 2026), Theorem 1.9. The formula agrees exactly. A GAGTA 2026 abstract also explicitly announces a solution to F42. Our first graph argument was recorded before reading their proof, but is a **rediscovery**, not a new solution. The archived paper is `literature/raw/F42-KochHyde-Olive-2609.00382.pdf`. No claim of novelty is made.
