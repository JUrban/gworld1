# Class-six N8 lead, 28 September 2026

Derived after the 13:32 UTC checkpoint. Not yet in the claim ledger.

The key new fact is that the bracket map L2 tensor L3 -> L5 is injective.
Embed its domain in V tensor^5. If its image bracket vanishes, the tensor
is fixed by rotation by two positions, hence by every cyclic rotation.
It is antisymmetric in its first two positions, so cyclic conjugation
makes it antisymmetric in every adjacent pair: it is totally alternating.
But alternation on the last three positions annihilates L3. Thus it is
zero in characteristic zero.

The standard metabelian module map mu has kernel in degree four exactly
[L2,L2]=Lambda^2 L2. One proof counts dimensions: its image consists of
the degree-three polynomial vectors (P_i) with sum t_i P_i=0, generated
by quadratic multiples of the Koszul vectors t_i e_j-t_j e_i. Its
dimension is r*C(r+2,3)-C(r+3,4). Subtraction from Witt's dimension of
L4 gives C(dim L2,2), already supplied by the exterior injection.

Put E=L2, f=ad_z:E->L3 for z nonzero in L1. Under the L2 tensor L3
injection, ad_z on Lambda^2 E is id tensor f on the alternating tensor.
This proves the following injective correction maps over Q, hence zero
integral kernels:

1. (U3,V4) -> [U3,Y2]+[z,V4], for Y2!=0.
   Applying mu puts V4 in Lambda^2 E. Then the equation says an
   alternating tensor equals the pure tensor Y2 tensor f^-1(U3).
   The latter must vanish.
2. (U2,V4) -> [U2,Y3]+[z,V4], for Y3!=0.
   The same argument either forces U2=0 modulo f(E), or reduces to a
   nonzero pure alternating tensor, which is impossible.
3. (U3,V3) -> [U3,D2]+[C2,V3], for independent C2,D2.
   The tensor equation is -D2 tensor U3+C2 tensor V3=0, so both vanish.

For class six, the leading-degree-three branch first uses the previously
proved one-dimensional kernel and finite Nielsen residue normalization
in degree four. The new first map makes degree five unique; degree six
is a final linear correction. The leading-degree-four branches use the
second/third map in degree five, then a final linear degree-six correction.
Leading degrees two, five and six are already covered by the all-class
IA, penultimate and central methods. Thus these lemmas propose a complete
class-six algorithm in all finite ranks.

There is no general zero-kernel assertion. For C=a, U=[a,b],
D=[a,[a,U]], V=-[U,[a,U]], Jacobi gives [U,D]+[C,V]=0. These have
weights (C,D)=(1,4), (U,V)=(2,5), and affect degree six. The quadratic
term [U,V] can survive in degree seven. This obstruction must be retained
when considering further generalization.

Outstanding: full proof write-up, exact kernel checks in several ranks,
class-six implementation with negative controls, independent GAP word
checks and primary-literature comparison. No new candidate is counted yet.

Update, approximately 13:45 UTC: the proposed scope is now proved as a
candidate in `problems/N8/class6-proof.md` and checked. The kernel suite
passed 44 records, the group suite 63 records, and GAP independently
checked 40 witnesses and 133 lifting steps (76 negative). The completed
audit is in `problems/N8/class6-audit.md`. This is the same single partial
N8 candidate; earlier intermediate layers in higher classes remain open
here. The original lead above is retained as a chronological record.
