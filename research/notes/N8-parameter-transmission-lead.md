# N8: passing one parameter through the first overlap

29 September 2026, approximately 13:41 UTC. **Unverified lead, not counted.**
This would be a different extension from the finite-tail argument. It needs
an exact integral proof, an independent obstruction calculation, and actual
group fixtures before any scope update.

Consider a normalized branch with leading weights (p,q)=(1,8), hence
d=9. The weight bound and no-consecutive-exceptions lemma put its
pre-Nielsen exceptions among offsets 1,...,5. The only nonseparated pair
remaining after processing offsets 1 and 2 is (3,5). Offsets 4 and 6 are
injective, and every kernel from offset 7 onward has an exact universal
commutator-preserving substitution. The proposed consequence would be all
leading degrees <=9 in arbitrary class, then all targets in class <=19
using the ten-final-layer argument. Neither consequence is adopted yet.

Fix all lower coordinates. The offset-3 kernel and offset-4 equations
give the previously proved complete integral affine line, with parameter
T and nonzero step in the first kernel coordinate. At offset 5 all equations
are affine linear in T and the new coordinates. Integer Smith reduction
of the fixed homogeneous matrix gives either finitely many fixed T, or
finitely many congruence classes T=M z+r with a polynomial integral
particular solution and one free primitive kernel parameter S. Every
coordinate through offset 5 is then affine in z,S. The first exceptional
parameter still has nonzero slope in z.

At offset 6, project the residual to the cokernel of A_6. The equation is

    q(z) + S B = 0,

where q has degree at most two and B is a constant rational vector. A
mixed zS term would first occur at offset 3+5=8, and S^2 at offset 10.
The quadratic coefficient of q is the nonzero first-kernel obstruction,
multiplied by the square of its retained nonzero integral step. Offset-4
and offset-5 corrections cannot contribute another quadratic term at 6.

If B=0, a nonzero scalar projection of q has finitely many integer roots.
Keep every one satisfying the other cokernel equations and the full
integer lifting conditions; S becomes the sole remaining parameter.
There are then no further pre-Nielsen exceptions, so the separated-kernel
algorithm can finish from offset 5 with the earlier parameter fixed.

If B!=0, one scalar equation expresses S as a rational polynomial in z
of degree at most two. Substitution into the other cokernel equations
either gives a finite integer root set, or identities. In the identity
case, A_6 is injective, so its unique rational solution is polynomial in z.
All integrality conditions are congruences of rational polynomials with
fixed denominators. Enumerating a common denominator modulus and replacing
z by M u+r gives finitely many polynomial integral branches, each retaining
one unrestricted integer parameter u. No bounded search over u is involved.

At each subsequent layer, the fixed homogeneous matrix has a polynomial
right side in u. Its cokernel equations are polynomial: a nonzero one
gives finitely many integer roots; otherwise its fixed Smith form gives
polynomial particular coordinates and constant-denominator congruences.
All remaining kernel directions are universal. Their integral substitution
periods depend only on the fixed leading pair, class, and direction, not
on u or earlier corrections. Retaining their entire finite residue set
therefore gives finitely many polynomial branches for the next layer.
Higher corrections changed by the normalization have not yet been fixed.
This seems to give termination in every fixed class.

Points requiring explicit scrutiny:

- Prove the asserted degrees and constant B in actual ordered Hall group
  coordinates, with every earlier fixed term retained.
- Explain the Smith-congruence branching without choosing a rational
  representative that misses integral solutions.
- Check that a universal substitution's leading translation is constant
  even on a polynomial family of already chosen lower coordinates.
- Exhibit a nonzero B that really absorbs the earlier quadratic obstruction;
  the existing pure-leading fixtures have B=0 and do not test this case.
- Test the two branches independently and retain any finite-cutoff cases.

A candidate nonzero-B fixture in the weighted Lie algebra on a,e of
weights 1,4 uses D=ad_a^4(e) and a fixed next component D_1=[e,[a,e]].
The offset-5 first component is U_5=ad_a^2(e), so B is the class of
[U_5,D_1] modulo im A_6. Compare it with the offset-3 obstruction
[e,-[e,ad_a^3(e)]+[[a,e],ad_a^2(e)]]. This is a proposed exact test,
not a claimed identity or nonzero result.

## First exact check

The proposed weighted Lie test now passes independently in Python/SymPy
and GAP's native rational free associative algebra. The complete offset-6
map has dimensions 1+6 -> 8 and rank 7. Both Q and B are outside its image,
and Q=-5B modulo that image. GAP constructs a full Lyndon basis independently
of the Python Hall basis. The two offset-3/5 kernel identities also pass.
Run times are 0.470641 and 2.026302 seconds, with empty stderr; no failed
run occurred. See `research/certificates/N8-parameter-transmission/checks.json`
and `results/n8-parameter-transmission-lie{,-gap}-v1/`.

This tests the absorption mechanism but is not an actual group fixture or
a proof of the general parameter algorithm. The scope remains uncounted.

There is an immediate compatibility concern with the suggested D_1:
already at offset 4, the first kernel parameter contributes
[e,[e,[a,e]]], whose three-e multidegree may lie outside im A_4. Thus the
same fixed perturbation that makes B nonzero could fix the first parameter
before reaching the overlap. The Lie test must not be called an example
of a surviving two-parameter group branch. Check this earlier obstruction
before investing in its group lift or claiming that the B!=0 case occurs.

This concern is now confirmed, not merely suspected. Python v2 and GAP v2
independently find rank(A_4)=4 and augmented rank 5 for this additional
column. They pass in 0.471624 and 2.026614 seconds with empty stderr. The
original v1 source snapshots and records are retained. Thus the fixture
does **not** preserve a free first parameter; its later Lie proportionality
does not establish that the quadratic-absorption case can arise on a
surviving branch. The abstract two-parameter elimination argument may still
be valid, but requires its own proof and suitable group tests.

## Possible generalization of the lead

The same argument may cover a branch with just two exceptional offsets
t<t'<2t. Keep the full linear block below 2t and quotient only the universal
kernel translations, as in the separated-kernel proof. A rank-two integral
parameter lattice should admit coordinates in which the first kernel
parameter is k0+mT and the second is l0+aT+bS, with m,b nonzero. At offset
2t the equation still has the form q(T)+SB: two increments of the first
parameter contribute the nonzero quadratic term; the later parameter
enters linearly with constant coefficient. If B is nonzero, eliminate S;
if B is zero, fix T by the nonzero quadratic and continue with the last
exceptional parameter. Rank-zero/one lattices need their own explicit cases.

For leading gaps <=8, the weight bound puts every exception at an offset
<=6. After treating offsets 1 and 2, the only nonseparated pairs are (3,5)
and (4,6); no third exceptional offset can accompany either pair in this
range. If the block argument is completed, this would cover leading degrees
<=10 in arbitrary class and combine with the ten-final-layer result to
cover class <=20. This larger consequence is a lead only. In particular
the (4,6) block, its intermediate layer, and its Nielsen boundary have not
yet been checked in group coordinates.
