# N9: infinitely many automorphism orbits of retracts in one fixed group

29 September 2026. An obstruction to a proposed finite-orbit shortcut,
**not an answer to N9(a)** and not an additional candidate. No novelty
is asserted for this elementary example.

Let G be the direct product of two integral Heisenberg groups, with
generators a,b and c,d respectively. Thus G is torsion-free of class two,
G' = Z(G) = <[a,b],[c,d]> is free abelian of rank two, and all cross-factor
commutators vanish. For every positive integer m put

    v_m = a c^m,               H_m = <v_m>.

Each H_m is a retract. The map a -> v_m and b,c,d -> 1 defines a
homomorphism G -> H_m, because its image is cyclic, and fixes v_m.
The element v_m has infinite order, as seen in G/G'.

Nevertheless the H_m belong to pairwise distinct Aut(G) orbits. Here is
an intrinsic way to recognize the two coordinate planes, so this does
not assume that every automorphism visibly preserves the given factors.
Write V=(G/G') tensor Q=V_1 direct-sum V_2 and Z=G' tensor Q, and let
B:Lambda^2 V -> Z be the commutator form. For a nonzero vector v, the
linear map B(v,-):V -> Z has rank one exactly when v belongs to V_1
or V_2; it has rank two when both components are nonzero. Therefore any
automorphism preserves the union V_1 union V_2 and permutes its two
maximal linear subspaces. A linear subspace contained in the union of
two subspaces over Q must be contained in one of them; applying this
also to the inverse gives the permutation assertion.

Intersecting with the integral abelianization lattice gives the two
primitive lattices Z^2 and Z^2. The induced maps on them are integral
unimodular maps, possibly exchanged. Such a map preserves the content
of a vector, that is, the gcd of its coordinates. Consequently the
unordered pair of contents of the abelianization of a generator of
H_m is an automorphism invariant. It is

    {1,m}.

An isomorphism from one infinite cyclic subgroup onto another takes a
generator to a generator or its inverse; the sign does not alter the
contents. Hence an automorphism taking H_m to H_n forces m=n.

This rules out a general algorithm justified merely by finitely many
Aut(G) orbits of retract subgroups. It does not rule out infinitely many
effectively parametrized orbits, finitely many *isomorphism types*, or
a different fixed-ambient decision procedure. All H_m here are
isomorphic to Z and all are plainly decidable positive examples.
It also does not turn the earlier uniform undecidability construction
into a fixed-ambient construction.

`scripts/check_n9_cyclic_retracts.g` independently constructs the
class-two product in GAP/nq and checks its Hirsch length and absence of
torsion. It checks actual retractions for m=1,2,5,17. Three abelianization
shears which would change the second content are rejected as group
homomorphisms: they violate the cross-factor relation [a,d]=1.
The universal separation of all m is the rank/content proof above,
not a bounded list of failed automorphism searches.

The original fixed-group question and the source limitations for the
2016 uniform construction remain as recorded in
`N9-fixed-ambient-and-coproduct.md`. The frozen full original nilpotent
page and N9 background were reread for this pass; the previously viewed
statement image was actually viewed again. The GAP run
`n9-cyclic-retract-orbits-v1` passed in 1.873 seconds with empty stderr,
using one CPU slot and 4 GB. Its exact command and log hashes are in
the recorded run directory.

An additional primary-source scope check located Konyrkhanova, Nurizinov,
Tyulyubergenev and Khisamiev, *Retracts of group of unitriangular matrices
over the ring*, KazNU Bulletin 3(91) (2016), pp.32--44. The issue PDF is
archived under `literature/raw/N9-Konyrkhanova-2016-issue.*`.
Read the abstract/introduction and Section4's opening theorem and
corollaries; viewed printedp39. Its UT3(Z) decision assertion is a
restricted prior case, not the general fixed-group answer. The printed
classification wording omits the trivial and whole-group retracts;
we do not import that blanket literal assertion. Its full proof is not
audited or used in the example above.
