# An uncounted nonlinear first-kernel lead for class ten

Derived during the 28 September2026 evening proof review; recorded
approximately21:17 UTC. No implementation or independent check yet.
This is not a new scope claim and not a classification of class ten.

Put delta=ad_z for nonzero z in L1 and T in L2. With T_j=delta^j T,
consider the degree-seven element

    D=2[T_0,T_3]+3[T_1,T_2]

and the degree-eight element

    V=2[T_0,[T_0,T_2]]-[T_1,[T_0,T_1]].

The derivation rule and Jacobi give delta V=[T_0,D]. Thus (T_0,-V)
lies in the first-correction kernel for type(1,7), in class ten.
Unlike the previous uniform family, D is nonlinear in the free alphabet
of L'. Its target leading term is

    [z,D]=2[T_0,T_4]+5[T_1,T_3].

In the z-stable free alphabet this has nonzero length-two components
of weight types(2,6) and(3,5). A bracket with both factors in L' and
fixed homogeneous original weights cannot have both those length-two
types. This appears to exclude leading weights(2,6),(3,5),(4,4),
leaving(1,7), but a full leading-direction recognition argument is
still needed.

For the final map L3+L9 -> L10, send T_j to A+(-3)^j B and other
seed jets to zero. Delta becomes the derivation with eigenvalues1,-3.
The associative AAAB coefficient kills its image and also kills
[L3,D], which has free-alphabet length three. Direct expansion gives

    image(V)=20[A,[A,B]]+4[B,[A,B]],

so the AAAB coefficient of [T_0,V] is20, nonzero. This suggests the
same quadratic-obstruction mechanism as before.

Remaining work: verify all displayed identities independently; prove
the full first-kernel statement in arbitrary rank; recognize every
possible degree-one leading direction; retain all integral scales and
lattices; build actual positive/negative group cases and GAP replays.
Other degree-seven D and other lower target layers in class ten remain
outside this lead. Nothing in this note establishes full N8(b).
