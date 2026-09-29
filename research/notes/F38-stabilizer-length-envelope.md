# F38(c): what the stabilizer condition actually decides

29 September 2026. Supplement to `F38-stabilizer-obstruction.md`.
**A weaker comparison property, not a solution of F38(c).**

The stabilizer condition has a precise interpretation. For nonidentity
u,v in F_r, the following are equivalent:

1. Stab_Out(F_r)([u]) has a finite orbit on [v].
2. There is some function f: N -> N such that

       ||phi(v)|| <= f(||phi(u)||)

   for every automorphism phi.
3. There is an effectively obtainable constant D>0 such that

       ||phi(v)|| <= D 3^(||phi(u)||)

   for every automorphism phi.

Thus the implemented two-sided test decides comparison by arbitrary
functions, and indeed by effective exponential bounds. The original
question asks for linear comparison. No implication from this weaker
property to linear comparison is proved here.

## Proof with explicit constants

(3) implies (2). If (2) holds, applying it to the stabilizer of [u]
bounds the cyclic lengths in its orbit on [v] by f(||u||). Only finitely
many conjugacy classes have those lengths, giving (1).

Suppose (1) holds. Use Whitehead reduction to choose an automorphism mu
such that u0=mu(u) has minimal cyclic length m in the orbit of u. Let
v0=mu(v), and let H0 be the outer stabilizer of [u0]. Conjugation by mu
identifies the original finite stabilizer orbit with H0.[v0]. Put

    M = max { ||z|| : [z] in H0.[v0] }.

This finite orbit is effectively obtainable by the mod-three procedure
in the preceding note. Let V be the number of vertices in the finite
length-preserving Whitehead component of [u0]. It too is computable.

Fix an arbitrary automorphism phi, put psi=phi mu^-1, and write
N=||phi(u)||=||psi(u0)||. Whitehead reduction gives a product delta of at
most N-m strictly length-decreasing Whitehead moves taking [psi(u0)]
to a minimal class [z]. The bound counts a decrease of at least one at
each step; no length-preserving steps are needed to find a shorter word.

Peak reduction says [z] lies in the length-m component of [u0]. Choose
a shortest edge path from [z] to [u0], with product gamma. Its length
is at most V-1. Consequently h=gamma delta psi belongs to H0, so

    [phi(v)] = [psi(v0)] = [delta^-1 gamma^-1 h(v0)].

Every Whitehead move, and its inverse, sends each basis letter to a
word of length at most three. It therefore multiplies cyclic length by
at most three. It follows that

    ||phi(v)|| <= M 3^(N-m+V-1).                       (*)

For example, D=M 3^(V-1) is a convenient integer constant for (3).
No claim that it is sharp or practical is intended. The argument uses
only classical Whitehead reduction in addition to the finite orbit
already computed; it does not invoke a compactness assertion about
Outer space.

Applying the equivalence in both directions shows that commensurable
conjugacy stabilizers are equivalent to mutual bounds by some functions,
and are sufficient for mutual effective exponential bounds. The factor
3^N in (*) cannot simply be replaced by a multiple of N: the proof
allows up to N-m successive expanding inverse Whitehead moves.

## The exact finite envelope is computable after a passed test

There is also a direct, slower description. Define E(N) as the maximum
of ||phi(v)|| over automorphisms with ||phi(u)||<=N, taking E(N)=0 if
there are none. Enumerate the finitely many cyclic words w of length
at most N. Whitehead's algorithm decides which are in the orbit of [u]
and produces, for each such w, an automorphism t_w taking [u] to [w].
If O=H_u.[v] is the computed finite orbit, all possible accompanying
classes are exactly

    { [t_w(z)] : [z] in O }.

Indeed, any automorphism taking [u] to [w] has the form t_w h with
h in H_u, up to inner representatives. Taking the maximum over this
finite collection computes E(N). Finiteness and computability of E are
therefore settled by the new test. Whether E(N)=O(N), simultaneously in
both directions, is the remaining F38(c) issue.

## Status and limits

This is a short consequence of the same prior Whitehead machinery,
recorded to isolate the missing quantitative step. No novelty is asserted,
no candidate scope or count is enlarged, and no additional numerical
samples are needed for this elementary argument. The existing code does
not implement the exact-envelope enumeration or output the bound (*).

An exploratory search for finite automorphism orbits, algebraic closure
and length bounds located Ould Houcine--Vallino, *Algebraic and definable
closure in free groups*, DOI10.5802/aif.3071, and Kharlampovich--Vdovina,
arXiv:1107.2843 (quadratic-equation estimates). Only indexed excerpts
and abstracts were consulted; neither is a dependency or a proof of the
needed linear implication. In particular, statements about finite orbits
of elements under pointwise stabilizers cannot silently replace finite
orbits of conjugacy classes under outer stabilizers.
