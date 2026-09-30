# N5: connect the general native-group stages

After de4f238, connect rational-support kernels to the existing central-lifting
solver. For each complementary support pair in K=G/Z(G), reject failure to
generate K, then enumerate subgroups of each support of index at most |T(K)|.
Only subgroups normal in K can be direct factors. GAP's low-index routine
returns conjugacy-class representatives; this is complete for normal subgroups
because each has a singleton conjugacy class. Explicitly check normality in K
and K_i=Y_i T(K), rather than silently treating class representatives as all
subgroups. Retain only commuting direct products K=Y_1 x Y_2.

Check that their full preimages commute. Present each quotient factor, lift
generators, and extract central relator defects and exponent sums. Feed these
to the already tested exact abelian splitting/lifting solver. For positive
answers, reconstruct actual native factors and verify nontriviality, trivial
intersection, commutation and generation. Preserve every finite branch list
for negative answers; a timeout is not a negative decision.

Use the twelve support fixtures, with known positive products and negative
free nilpotent/finite/diagonal-gluing controls. Record one-CPU/eight-GB jobs with
180-second initial limits, escalating neither the experiment clock nor global
resource budget. A successful pipeline still starts from a native pcp group;
arbitrary promised-nilpotent finite-presentation conversion remains a separate
interface. No change to theorem count or novelty assessment.
