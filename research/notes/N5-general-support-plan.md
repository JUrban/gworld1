# N5: rational-support preimages in arbitrary class

Continue the higher-class integration after a83f132. Given a rational centroid
projection P on the Malcev Lie algebra L, the desired subgroup of G is the
kernel of the homomorphism

    g -> exp(ad((1-P) log(gT))).

Its Lie kernel is im(P)+Z(L). Compute this map exactly on native pcp generators,
triangularize it using the descending image filtration of the adjoint algebra,
and clear denominators by diagonal conjugation. Conjugation, not plain
transposition, must preserve group multiplication. Convert its integral upper
unitriangular image to pcp form and calculate its kernel in GAP. Then map this
kernel to K=G/Z(G). Check the zero/full projection boundaries, the finite torsion
kernel, and the fact that complementary supports intersect in T(K).

Test all partitions on known direct products, comparing with native factor
projections rather than merely comparing Hirsch lengths. Include a finite-index
diagonal congruence subgroup of a product: a rational decomposition must not be
mistaken for an integral direct product. Preserve failed sources and version
all outputs. Use one CPU/eight decimal GB/180 seconds initially. This remains
an implementation supplement to the existing N5 candidate; no new result count.
