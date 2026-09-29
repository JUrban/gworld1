# N8: branches with at most two remaining exceptional offsets

29 September 2026. **Candidate extension with completed finite audit.**
This extends the method, not the number of candidate entries. See
`two-exception-audit.md` for the independent arithmetic/group checks and
their limits. Complete branch enumeration is not implemented end to end.
The inherited structural lemmas and novelty require specialist review.

## Candidate statement

In a finite-rank free nilpotent group of any class, a normalized commutator
branch is decidable if it has at most two remaining pre-Nielsen exceptional
offsets. Earlier coordinates have already been fixed. The proposed
consequences are every leading weight gap <=8, every target of leading
degree <=10 in arbitrary class, and, together with the ten-final-layer
argument, every target in class <=20. General N8 remains unresolved and
novelty is unverified.

Use the notation and imported lemmas of `universal-gauge-proof.md`:
leading terms C,D have weights p<=q, d=p+q, n=c-d, and

    A_s(U,V)=[U,D]+[C,V].

An exceptional offset is a nonzero kernel at 0<s<q-p. It is one-dimensional,
its successor is injective, and for a nonzero direction (U,V),
[U,V] is nonzero modulo im A_(2s). At the Nielsen offset and later, complete
integer kernel lattices have finite-index sublattices supplied by exact
universal group substitutions. The substitutions preserve the commutator
and first act by their specified homogeneous kernel translations.

All components of A_s are the full ambient free Lie components. No
assumption that C,D or an exceptional direction extend to ambient free
generators is made. The earlier finite leading-pair enumeration is an
explicit dependency, as are its signed scales and lattice normalizations.

## 1. A polynomial family with only universal kernels remaining

Suppose every lower Hall coordinate of a pair is a rational polynomial
in an integer parameter T and is integral for every T in Z. Suppose also
that every future nonzero correction kernel has an exact universal
substitution. Then this family can be decided completely.

At the next offset s the equation is

    A_s w = r(T),                                    (1)

where A_s is constant and r is a rational polynomial vector. This follows
from finite Hall collection: the new coordinates enter linearly at their
first degree, and the already chosen coordinates are polynomial. Compute
a rational left kernel of A_s. If one compatibility polynomial is nonzero,
every possible T belongs to its finite, exactly computable integer root
set. Retain every root satisfying all equations and divisibility conditions;
then use the ordinary finite-residue algorithm with T fixed.

Otherwise every rational compatibility equation is an identity. Clear
constant denominators in A_s and all coefficients of r, and compute an
integer Smith form P A Q=D. The forced transformed coordinates are
f_i(T)/D_ii, where f_i have integer coefficients and D_ii are fixed
nonzero integers. The unused coordinates are free integers. Integrality
of the forced coordinates is periodic in T with an effective common
period M (the product of the nonzero |D_ii| suffices; use M=1 in rank zero).
Enumerate every residue r modulo M. For each accepted residue, substitute
T=M Z+r and set the unused transformed coordinates to zero. This gives
a polynomial integral particular solution w_0(Z), and all solutions are

    w=w_0(Z)+K v,       v in Z^k,                    (2)

where the columns of K form the complete integer kernel. No saturation
or rational kernel representative replaces this integer lattice.

For this kernel choose a fixed full-rank period lattice Lambda from the
exact universal substitutions. Its periods depend only on C,D, the
direction and the class. On every pair in the family, the first change
is that same fixed homogeneous translation: inserting a higher correction
in a universal word increases its weight, so cannot change the first
translation. Thus Lambda is independent of Z and of the already fixed
higher coordinates. Enumerate every coset of Z^k/Lambda and put its
constant representative into (2). An original solution can be normalized
to one of these representatives by exact substitutions; the changes to
later coordinates are allowed because those coordinates remain unfixed.

There are finitely many residues and cosets at each of finitely many
offsets. The integer period search terminates by the earlier integral-power
lemma, not a finite cutoff. At the final offset every surviving unrestricted
parameter family provides a witness, for example at Z=0. Finite branches
are checked directly. This proves both termination and completeness of
this continuation procedure, not a complexity bound.

## 2. The full block below the first quadratic obstruction

Zero or one remaining exceptional offset is covered by the earlier
separated-offset theorem. For two offsets t<t', that theorem also applies
if t'>=2t. Assume therefore

    t<t'<2t.

If n<2t, every still-variable coordinate starts at offset at least t, so
all remaining equations are jointly affine linear; solve the full integer
system and finish. Assume n>=2t and retain every coordinate at offsets
t through 2t-1. Their equations are jointly affine linear: mixed variable
increments first occur at offset 2t, and nonlinear increments from one
factor alone require the additional positive leading weight of that
factor. Fixed earlier terms affect the linear columns, not this bound.

The complete solution set is an empty set or an affine integral lattice S.
Let k be the integer coefficient of the primitive kernel at offset t.
The image of S in the k-coordinate is a point or k_0+mZ, m!=0.

For every universal kernel in this block, record the exact substitution's
translation on the whole block. Each such offset s is greater than t'
(universal kernels begin at the Nielsen offset). Since s+t>2t, dependence
on a still-variable coordinate occurs beyond the block. These translations
are therefore constant integer vectors preserving S and k. They generate
a lattice Lambda_0 inside the difference lattice of S.

After tensoring with Q, quotienting by these translations leaves dimension
at most two. Indeed, a difference vector's first nonzero offset must be
a homogeneous kernel. Its component is removed by a universal translation
unless the offset is t or t'. Each exceptional kernel contributes at most
one dimension. Triangular elimination over the finitely many offsets proves
the assertion and supplies an effective quotient calculation.

Use Smith/Hermite form to write S/Lambda_0 as finitely many torsion cosets,
each with an integral lift of a free lattice of rank r<=2. Every original
block solution is equivalent under exact substitutions to one of these
lifted representatives, with all coordinates from 2t onward still free.
No torsion coset is discarded. Their coordinates are affine functions of
the free integer parameters.

If k is fixed in one such family, all coordinates below t' are fixed as
well: before t' there is no additional kernel or universal translation.
Restart the complete one-exception algorithm at t', allowing all higher
coordinates. This can repeat valid solutions across cosets but introduces
no false positive, since the entire original commutator equation is solved
again. Every solution of the old family is retained. This also handles
rank-zero families without needing a second parameter.

Suppose k varies. Choose an integral basis of the free quotient adapted
to its map to Z. For rank one write k=k_0+mT. For rank two choose lifts
J_1,J_2 so that

    block = block_0+T J_1+S J_2,
    k = k_0+mT,          m!=0.                       (3)

The second direction has zero component below t' and a nonzero component
at t'. Otherwise its first nonzero component could be removed by universal
translations, contradicting its nonzero free-quotient class. All integral
steps, including m, are retained. A rational reparametrization to m=1 is
not used.

## 3. Eliminate or fix a parameter at offset 2t

Evaluate the group commutator along a representative (3), and project its
offset-2t residual modulo im A_(2t). This is a rational vector equation

    q(T)+S B=0,                                      (4)

where q has degree at most two and B is constant. A term involving T and S
needs offsets at least t+t'>2t. Two S increments need 2t'>2t. Two increments
of T at the first offset t give, up to the fixed sign convention, the
quadratic coefficient m^2[U,V]. Increments at a later offset cannot add
another quadratic contribution at 2t. Terms using two increments from
one factor have the extra leading weight and also occur too late.
Consequently q has a nonzero quadratic coefficient in this cokernel.

For a rank-one family there is no S and a nonzero scalar projection of q
has finitely many integer roots. Test all of them against the full integral
equation at 2t, normalize its universal kernel, and continue. No exceptional
offset remains after t', so Section 1 with the parameter fixed applies.

For rank two and B=0, the same quadratic root test fixes T to finitely many
possibilities. Below t' the coordinates are then fixed independently of S.
Restart the complete one-exception algorithm at t' as in Section 2, without
discarding any solution or assuming that S already has a finite range.

For B!=0, choose a nonzero coordinate B_i. Equation (4) forces

    S=-q_i(T)/B_i,                                   (5)

a rational polynomial. Substituting (5) into all remaining coordinates
of (4) gives polynomial compatibility equations. A nonzero one restricts
T to its finite integer root set, checked completely. Otherwise all are
identities. Substitute (5) in the **full** offset-2t equation, including
its new correction coordinates, and impose S integral along with their
integrality. The fixed-matrix procedure of Section 1 supplies every
allowed residue of T and polynomial integral particular coordinates.
Every kernel at 2t is universal, because the only two remaining exceptions
are t,t'<2t. Retain all its finite residues.

The resulting families have one integer parameter and only universal
kernels at future offsets. Section 1 completes them in every fixed class.
This conclusion does not require that the B!=0 case actually occurs in
a particular weighted test fixture. It does require all earlier block
compatibility conditions; a late Lie relation alone is insufficient.

Each transformation used above either enumerates an exact finite set,
retains a complete integer lattice, or applies a reversible group
substitution preserving the target commutator. Every returned witness
therefore solves the original equation, and every original solution has
a retained representative. This proves the proposed two-exception branch
algorithm subject to the explicitly inherited structural lemmas.

## 4. Uniform consequences and their bounds

For q-p<=8 the weight bound t<=q-3p puts every pre-Nielsen exception at
an offset <=6. Exceptions cannot be consecutive. Offset 1, if present,
can be processed before any later exception by its quadratic at 2.
Offset 2, if present, can be processed by its quadratic at 4; a new
exception exactly at 4 is retained, as in the separated-offset proof.
After these steps, at most two nonconsecutive exceptions remain among
3,4,5,6. The only nonseparated pairs are (3,5) and (4,6); all remaining
cases satisfy the proposed theorem or the older separated theorem.

For d<=10 every normalized pair has q-p=d-2p<=8, giving the proposed
arbitrary-class leading-degree consequence. For c<=20, either d<=10 or
d>=11, when c-d<=9 and the ten-final-layer theorem applies. Identity,
abelian/rank-zero cases and targets outside the derived subgroup are
handled as in the preceding proof. Nothing here asserts general N8(b).

The (4,6) pair is a genuine extra case: it has an intermediate
offset 7, and the first quadratic is at offset 8, which can be the Nielsen
offset. That kernel must be normalized by its full integer period. The
new arithmetic and group fixtures cover these features explicitly; the
audit states their precise scope.
