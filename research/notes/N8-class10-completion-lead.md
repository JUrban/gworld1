# A route to all targets in class ten

Exploratory notes, 28 September 2026 approximately23:11--23:16 UTC.
**Unproved lead, not added to the candidate scope.**

The class-nine proof's linear tails already remain linear through class ten
for leading degree three, degree five, and degree seven (after the stated
finite normalizations). For type (1,6), the old degree-nine quadratic
obstruction first makes its offset-one parameter finite; then solve all
offset>=2 corrections jointly through degree ten, not a chosen particular
degree-nine lift. Gamma_8 is covered by the committed third-layer proof.

Missing kernels for a complete class-ten proof seem to be:

1. (1,3), offset three: L4 + L6 -> L7. Expected injective.
2. (2,2), offset three: L5 + L5 -> L7, independent leading C,D.
   Expected injective.
3. (1,5), offset two: L3 + L7 -> L8. Expected zero except
   D=delta^2 U for U in L3, when the kernel is Q*(U,-[U,delta U]).
4. (2,4), offset two: L4 + L6 -> L8. Expected Q*(D,0),
   normalized by the exact move x->yx.
5. (3,3), offset two: L5 + L5 -> L8, independent C,D.
   Expected injective.

Use the delta-stable free alphabet E,B,W,G,H,J of class9-proof.md.
For (1,3), length-one V_H vanishes. The E,G component kills V_EW;
the B,W equation and the antisymmetry of V_BB force U_W=V_BB=0.
Remaining [U_EE,D_B]+delta V_EEE=0: if D is outside delta E it
forces U=V=0. If D=delta T, project each other derivative letter;
the resulting derivations replacing a seed by a fresh letter force V
to use only T (replace that fresh letter back and use the Euler count).
Lie_3 on one letter is zero, finishing the proposed injection.

For (2,2), eliminate G components using independent C,D in E. For
each B letter b write U=[X,b], V=[Y,b]. Associative words beginning
with b give -X tensor D + Y tensor C=0, so X=Y=0. The (3,3) proof
is the same free-alphabet argument with one E and two B letters.

For (2,4), separate D_W from D_EE. When D_W is nonzero, U_W is
proportional to it; subtract that multiple of the Nielsen direction D.
The mixed three-letter injection of class8-proof.md kills the remaining
mixed terms. When D_W=0, the same injection removes all W terms;
the remaining equation is the previously proved (1,2), offset-one
kernel in the free algebra on E. Verify that exact prior lemma before
reusing it; the expected residual kernel is only Q*(D,0).

For (1,5), the length-two equation forces D_G=delta^2 U,
V_BW=-[U,delta U]; the E,H and W,W components give this by the
rank-one symmetric matrix condition. The length-three equation has
a unique E,E,W component from delta V_EEB, so V_EEB=0 and then
[U,D_EB]=0 forces D_EB=0. This classification needs a written proof
and checks, particularly for arbitrary sums of alphabet generators.

The exceptional parameter k first changes the factors in degrees 3,7.
Its only quadratic contribution through degree ten is proportional to
Q=[U,[U,delta U]]. Other corrections beginning in degrees 4,8 form
a joint linear tail through class ten, including the degree-nine layer.
Need prove Q survives modulo the full tail image at degree ten while
accounting for its degree-nine constraints and all fixed lower terms.
Survival modulo the homogeneous degree-ten image [L5,D]+[z,L9] is
necessary, but by itself does not control higher effects of the kernel
at degree nine. One possible repair is a sixth kernel lemma: for the
exceptional D=delta^2 U, the offset-three map L4+L8->L9 should be
injective. If true, its solution is affine in k and its final-layer
contribution is linear in k; the quadratic obstruction below survives.
This additional injectivity has not yet been proved or checked.

If U has a component in a degree-three seed, project to that seed's
delta-chain; in bracket length three, Q is nonzero whereas L9 has
only three equal degree-three letters (zero Lie component). The L5
term disappears in this projection. If U is in delta E, write U=delta T
and project to T's chain. Set T_i=delta^i T and use degree-ten basis

    X=[T0,[T0,T4]], Y=[T1,[T0,T3]], Z=[T0,[T1,T3]],
    W=[T2,[T0,T2]], R=[T1,[T1,T2]].

The three delta images are X+Y+Z, W+R+Y, R+Z. The additional
L5 bracket is Z-Y. The functional (2,-1,-1,0,1) kills these four
vectors and takes Q=R to 1. Thus a nonzero quadratic equation should
bound k to at most two integer values. A projection onto a chosen
seed chain also covers a sum U=delta T+S if S has a nonzero seed part.

Do not claim the full theorem until every kernel, integrality/gauge step,
joint-tail polynomial calculation, implementation and independent check
is complete. No additional literature search has yet been made for this
specific full-class-ten lead. Existing N8 scope and tally are unchanged.
