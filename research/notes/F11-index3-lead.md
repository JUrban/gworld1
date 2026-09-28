# F11: cyclic retract and an index-three subgroup

Active-run scratch argument, 2026-09-28. Not yet counted; source audit and literature check pending. Developed before checking the current F11 literature.

Let F=<a,b> and w=a^2 b a^{-1} b^{-1}. R=<w> is a retract: the map a -> w, b -> 1 fixes w, since its a-exponent sum is 1.

Let S be the stabilizer of vertex 0 in the right-action labelled graph with vertices {0,1,2}, a fixing 0 and swapping 1,2, and b cycling 0->1->2->0. The word w interchanges 0 and 1 and fixes 2. Hence w is outside S and w^2 is in S; R intersect S=<w^2>.

Compute the signed edge chain of the based loop w^2. It equals twice the a-loop at vertex 0: the non-loop edges traversed in its two halves cancel as integer chains. In H_1(S;Z), therefore, [w^2]=2[a]. If a retraction S -> <w^2> existed, its induced map on abelianization would send the primitive generator [w^2] in the target Z to twice an integer, impossible. Thus the cyclic intersection is not a retract.

Audit tasks: confirm right-action conventions; express w^2 in an explicit Schreier basis to expose a visibly even exponent vector; independently verify by GAP. A Hall of Fame comment mentions Snopce, Tanushevski and Zalesskii for F11, so known prior resolution is particularly likely.

## Literature check outcome

Snopce, Tanushevski and Zalesskii, arXiv:1902.02378, Theorem A(ii) and Example 3.5, already give negative answers. Their construction uses the same cyclic-retract word, under their commutator convention; the rank-four finite-index version matches the mechanism above. This is a **rediscovery**, not a new solution. The paper is archived locally.
