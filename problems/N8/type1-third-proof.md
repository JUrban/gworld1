# Third-from-last targets with only type-one leading factors

Candidate extension,29 September2026. Implementation and independent
software replay are documented in `type1-third-audit.md`. No outside
specialist review or established novelty is claimed. This extends the same
partial N8(b) entry; arbitrary targets in arbitrary class remain unresolved.

Let N=F_r/gamma_(c+1)(F_r), r finite and c>=6, and use
[x,y]=x^-1 y^-1 x y. Let L be its associated integral free Lie ring, using
its rational extension when discussing kernels and supports. Suppose g has
nonzero leading term W in L_(c-2). Enumerate all normalized integral leading
factor pairs [C,D]=W of weights p<=q, p+q=c-2, as in the earlier
`penultimate-target-proof.md`.

**Proposed theorem.** If this finite list has no pair with p>=2, there
is a terminating algorithm deciding whether g is a single commutator in N,
and constructing factors on positive inputs. Empty lists are allowed and
give negative decisions. The input condition itself is decidable.

In particular the theorem applies when W has nonzero image in L'/L'':
any bracket whose two factors both have degree>=2 lies in L''. This gives
a simple sufficient condition, not a necessary condition for our algorithm's
scope. Integral leading pairs of other types cause the implementation to
return unsupported, not a negative answer.

The earlier central and penultimate target algorithms handle gamma_(c-1).
Thus this is progress on the next layer, under the stated leading-type
condition, in every finite rank and every class. It includes and goes beyond
the previously recognized pure iterated-adjoint and odd-adjoint families.

## 1. Complete finite leading choices

Exact Nielsen moves preserving [x,y] put any solution into one with
nonzero leading bracket and p<=q. If equal-weight leading factors are
rationally dependent, a determinant-one integral Euclidean move cancels
one leading term and raises its weight. Homogeneous centralizers in a free
Lie algebra are one-dimensional, so unequal nonzero leading degrees cannot
commute. The resulting p+q is exactly c-2.

For p<q, the earlier block-quadratic method gives at most two possible
rational first-factor directions. On each line use its primitive integral
representative C0, solve [C0,D0]=W, and retain **every signed divisor k**
of content(D0), giving C=k C0 and D=D0/k. Reject a direction when D0 is
not integral. The alternative finite-projective-fibre method in
`projective-factor-audit.md` establishes finiteness and an independent exact
rational algorithm without the rotation bound.

For p=q, the exterior-square method and finite oriented Hermite sublattices
supply the complete normalized list. We use this to test the scope condition,
not to solve additional higher-type branches. The full proofs of finite
normalization and integral scale completeness remain the earlier credited
N8 ingredients. Once the condition passes, every possible solution must
have leading type(1,q) with q=c-3>2.

## 2. A first correction has at most one parameter

Fix a leading pair (C,D), set delta=ad_C, and choose integral Hall group
lifts x0,y0. Matching degree q+2=c-1 requires an integer linear equation
with homogeneous map

    A_D: L2 + L_(q+1) -> L_(q+2),
         (U,V) |-> [U,D]+delta V.                         (1)

The rational kernel of this map has dimension at most one. Here is the
argument, with the complete coefficient details in
`research/notes/N8-general-first-kernel.md`.

The homogeneous free delta-chain alphabet for L' from
`class9-proof.md`, Section1, makes delta shift each seed along its chain.
Every nonzero U in L2 can be selected as a degree-two seed. In the free
associative algebra, encode coefficients at a fixed sequence of seed names
by a polynomial in distinct variables for the successive derivative indices.
Delta then multiplies by the sum of those position variables.

If [U,D] is a delta-image, an associative word of D starting with another
seed yields, after adjoining U at the end, a polynomial independent of that
last position variable but divisible by the sum of all position variables.
It is zero. The same applies at the other endpoint. Lyndon triangularity
then shows that D involves only U and its delta-iterates: any nonzero Lie
component involving another letter has a least associative word beginning
with such a letter when those letters are ordered first.

Thus two independent U directions would force D into the free Lie algebras
on two disjoint chain alphabets, whose intersection is zero. Since D!=0,
there is at most one U direction; delta-injectivity makes V unique for U.
The zero U direction has V=0. Hence the kernel has dimension at most one.

The delta-chain construction imports the torsion-free metabelian module
and homogeneous Shirshov facts already credited in `class9-proof.md`.
Lyndon basis triangularity is prior; Lalonde–Ram1995, equations(1.2)–(1.3),
is archived and precisely cited in the supporting note.

## 3. A uniform nonzero quadratic obstruction

Suppose a nonzero first-kernel direction is (U,-V), so delta V=[U,D].
Then, for every q>2,

    [U,V] not in [L3,D]+delta L_(q+2).                    (2)

The following elementary fact supplies the key obstruction. In the free
Lie algebra on z,t over Q, if

    [z,V]=[t,D],   [z,W]=[t,V],                          (3)

then every ordinary word-length component>=2 of D,V,W is zero.
To prove it, write P=z P_z+t P_t for each P. Comparing first letters in
(3) gives

    V=V_z z-D_z t,  D=D_t t-V_t z,
    W=W_z z-V_z t,  V=V_t t-W_t z.

The two expressions for V imply
(V_z+W_t)z=(D_z+V_t)t, hence V_z=-W_t and D_z=-V_t.
Substitution shows P=P_z z+P_t t for P=D,V,W: each polynomial is invariant
under cyclic rotation of associative words. A Lie polynomial of length>=2
has coefficient sum zero on each cyclic orbit, because every bracket is
zero in the cyclic-word quotient. Constant coefficients with zero sum on
each finite orbit vanish over Q. This proves the fact.

Embed a single differential chain by t_j -> ad_z^j(t). This is injective:
with t<z its least associative words are (-1)^j t z^j, and products of
these words decode uniquely. It intertwines delta with ad_z. Give z weight1
and t weight2. A nonzero D of weight q>2 cannot be of ordinary length one;
therefore (3) rules out two successive primitives

    delta V=[U,D],  delta W=[U,V].                       (4)

For completeness, to deduce(2), take the greatest bracket-length component
D_m in the U-chain. Its corresponding primitive V_(m+1) is nonzero, since
a free generator commutes only with its scalar multiples and q>2.
Projection onto the U-chain sends L3 into Q*delta U. Consequently the
projected [L3,D] has length at most m+1. Cancellation of [U,V] modulo the
space in(2), in length m+2, would give a forbidden pair of successive
primitives for D_m. Thus(2) holds.

The Lie and characteristic-zero hypotheses are essential: D=t^n,V=W=0
is an associative counterexample to the corresponding statement without
the Lie condition. The q=2 Nielsen exception belongs to the earlier
class-five argument and is not included in this step.

## 4. All integral branches terminate

Solve the first inhomogeneous integer system using a full Hermite or Smith
calculation. An inconsistent branch has no solution. If its kernel is zero,
its integral solution is unique. Apply it and solve the final integer linear
system with image [L3,D]+[C,L_(q+2)].

If the first system has a one-dimensional kernel, retain its entire integral
solution line v+nK, n in Z, with K a primitive generator of the integral
kernel. Both factors are changed by Hall group words with these integer
coordinates. Their commutator now agrees with g through degree c-1.

The remaining central residual is an integer-valued polynomial R(n) of
degree at most two. The only surviving quadratic interaction is between
the two variable corrections, of weights2 and q+1, whose sum is c=q+3.
Two weight-two corrections interacting with the weight-q leading factor
first appear in weight q+4>c. Squares of the second correction are higher
still. Conjugation of the initial commutator by the first correction can
contribute in weight c, but is linear in n. Fixed higher terms in the chosen
leading lifts likewise affect only the linear and constant coefficients.

The quadratic coefficient modulo the final linear correction image is a
nonzero rational multiple, up to sign, of[U,V]. It is nonzero by(2).
A rational cokernel coordinate gives a nonzero polynomial equation of
degree at most two and therefore at most two integer roots. Enumerate every
root and test the full integral final-layer system. Denominators and finite
congruences are retained; rational solvability alone is insufficient.

Every surviving root constructs group factors. All other higher coordinates
of the factors either occur in these final corrections or have weight too
large to affect the commutator. Thus every solution in this leading branch
is included. The number of leading branches is finite and complete, and
every branch terminates. Exhaustion therefore gives a valid negative answer
within the recognized scope.

## 5. Implementation boundary

`scripts/n8_type1_third.py` implements this procedure with explicit unsupported
results outside the stated layer/type condition. The exact integer Hall
representation of the leading-pair equations is in
`scripts/n8_leading_pairs_hall.py`; it changes the linear coordinates, not
the factorization criterion or retained integral scales.

The universal argument rests on Sections1–4. Bounded tests do not replace
the proof. The independent GAP replay verifies witnesses, integer branch
membership, first-kernel nullities, complete primitive affine lines, exact
quadratic root/congruence certificates and selected metabelian scope
exclusions. It does not independently re-enumerate all possible leading
factor directions; that completeness remains a mathematical dependency.
See the separate audit for actual runs, the preserved timeout, exact scope,
and limits. No new result or code from Kourovka is imported.
