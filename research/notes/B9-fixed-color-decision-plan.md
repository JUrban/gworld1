# Fixed-color decision without a cutoff on the other color

30 September 2026. Pending implementation and independent reconstruction.

For a given braid a in B_m, m>=3, seek every special c with a S(c) in B3.
Delete all strands of a except those starting at positions 1,2,3; relabel
the retained endpoints in order and call the resulting three-braid A0.
Test whether a^-1 A0 lies in S(B_(m-1)) by deleting its first strand and
checking the complete braid equality after shifting the result back.

This product-membership test is complete. If a=A h with A in B3 and
h in S(B_(m-1)), the first factor preserves the retained set and survives
deletion unchanged. The deleted h can braid only the two retained strands
other than the first, so deletion(a)=A sigma2^k. Therefore
a^-1 deletion(a)=h^-1 sigma2^k is shifted. The converse is immediate.
No assertion that strand deletion is a homomorphism on all B_m is used.

If the test fails, no c exists. Otherwise let c0=S^-1(a^-1 A0).
The parabolic intersection B3 intersect S(B_(m-1))=<sigma2> shows that
all possible second braids, before imposing specialness, are exactly
c0 sigma1^k, k in Z. Every special c lies in B_(m-1), hence has exponent
between0 andm-2. Only k=-epsilon(c0),...,m-2-epsilon(c0) need inspection.
Use Dehornoy's existing terminating specialness algorithm to decide each.
This is at most m-1 tests; word sizes/runtime need not be small.

Implement specialness via a positive/negative fraction obtained by Artin
word reversing, followed by the partial coloring action from units.
At negative crossings solve left division by exact shifted-subgroup
membership. The free-LD division closure and fraction-domain completeness
are credited source inputs, not inferred from finite controls. Any
resource cap means incomplete, never nonspecial or an empty fibre.

Apply the procedure to the existing 52 height-four first colors, with no
new enumeration of special terms, and verify all finite decisions in GAP.
Additional structural controls must test deletion as a groupoid operation,
wrong multiplication order, shifted membership, fraction equality and
failed left divisions. A general parabolic double-coset theorem was found
in arXiv1402.5541v4 during the source check, but the elementary deletion
argument above makes it unnecessary for this particular product.

Even complete fixed-color decisions do not exhaust the infinite set of
first colors and do not decide whether B4 has further special braids.
