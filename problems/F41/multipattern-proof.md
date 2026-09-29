# F41: a full-scope candidate via definable sets and piece covers

29 September 2026, active experiment. **Candidate proof, subject to
independent mathematical and novelty review.** This extends the earlier
primitivity-rank-at-most-two candidate. The principal imported results are
Kharlampovich--Myasnikov's description of definable sets and Pillay's
characterization of generic elements. They are credited dependencies;
the present argument does not reprove their underlying model theory.

## Exact statement

Fix a free basis of the nonabelian free group F_r, r >= 2, and put
q = 2r-1. For each nontrivial nonprimitive w in F_r, there are constants
C_w > 0 and an integer D_w >= 0 such that

    #{v in Aut(F_r).w : |v| <= n} <= C_w (n+1)^D_w q^(n/2).       (1)

Consequently its ball exponential growth rate exists and is sqrt(q).
The spherical exponential limsup is also sqrt(q). A spherical limit
is not asserted: parity can leave infinitely many spheres empty.

The identity has orbit {1}, hence ball growth 1, and is an explicit
exception to the website's literal wording. It is not counted as a new
negative solution. In rank one every automorphic orbit is finite, with
ball growth 1 = sqrt(2r-1). Thus the substantive intended scope is exactly
the nontrivial, nonprimitive words in finite rank r >= 2.

This does not prove the stronger cyclic-orbit conjecture in Puder--Wu,
Question 5.4, involving their invariant mu(w). It proves the full-word
orbit-growth conclusion asked in the frozen GroupWorld F41.

## 1. Two imported results

**KM.** Olga Kharlampovich and Alexei Myasnikov, *Definable sets in a
hyperbolic group*, International Journal of Algebra and Computation 23
(2013), 91--110, [arXiv:1111.0577v5](https://arxiv.org/abs/1111.0577),
Definitions 5--6 and Theorem 13. For every definable P contained in F_r,
either P or its complement is a sub-multipattern. The language may
contain constants from the group.

Here a piece of a reduced word p is a nonempty word occurring at two
distinct positions, possibly with opposite orientation and possibly
overlapping. A one-variable parametrization is given by a finite system
of noncancelling equalities

    p = w_j(y_1,...,y_m), j=1,...,k,

with fixed group coefficients and nonempty variable values, in which
each variable occurs at least twice in the system and every variable
appearing in w_1 is a piece of p. A multipattern is a finite union of
such sets, allowing empty and singleton sets; a sub-multipattern is any
subset. Only the first equality and its piece condition are used below.
In particular we do **not** assume a variable occurs twice in w_1.

**Pillay.** Anand Pillay, *On genericity and weight in the free group*,
Proceedings of the American Mathematical Society 137 (2009), 3911--3917,
[arXiv:0812.1692](https://arxiv.org/abs/0812.1692), Fact 1.10 and
Theorem 2.1(i), with the definition on printed page 6. There is a complete
parameter-free generic type p_0. Basis elements realize p_0, and every
realization of p_0 in a finite-rank free group is primitive. A generic
element has the following defining property: every parameter-free
definable set containing it has finitely many left translates covering
the group.

“Generic” here means finite-translate generic, not density one in word
balls. We will use an elementary counting argument to rule out this
property for sub-multipatterns.

## 2. Counting a fixed cover by repeated pieces

Consider reduced words of length n split, in a prescribed order, into
t nonempty variable blocks and fixed coefficient blocks containing a
total of C coefficient letters. Suppose each variable block has a
second occurrence, in either orientation, somewhere in the whole word.
The second occurrence may overlap the first or cross block boundaries.
All constants t,C and the coefficient words are fixed, independently
of n.

Choose the lengths of the t variable blocks. There are at most
(n+1)^t choices; this determines the positions of every block and every
coefficient letter. For each variable block choose the starting position
and orientation of a second occurrence. There are at most (2n)^t such
choices. Identifications between different occurrences of the same
formal variable, and the remaining equations of the parametrization,
may be discarded for an upper bound. Thus it suffices to count words
for one of these polynomially many positional schemes.

Make a signed graph on the n letter positions. If a chosen repeated
block starts at a and its second occurrence starts at b, both of length
l, then add the equalities

    p[a+j] = p[b+j]              (same orientation),
    p[a+j] = inverse(p[b+l-1-j])  (opposite orientation),

for 0 <= j < l, with consistent zero-based indexing. The first case has
a != b. In the second case, any self-identification with inverse sign
makes the scheme impossible, since no free-basis letter equals its
inverse. More generally an inconsistent signed cycle makes the scheme
impossible and can be discarded.

In a remaining scheme every nonconstant position is joined to a
different position. Indeed it belongs to one of the variable blocks,
and its chosen repeated occurrence supplies that edge. Consequently
every singleton component consists of a coefficient position. If c is
the number of components, at most C of them are singletons and all the
others have size at least two. Hence

    c <= (n+C)/2.                                                  (2)

Signed consistency means that the letter at every vertex of a component
is determined by one alphabet letter assigned to that component, together
with a fixed sign. Consecutive positions in the word supply a further
constraint: their letters must not be inverses.

Collapse the components in the path of consecutive positions. Its
quotient graph is connected, since the original path is connected.
Choose a spanning tree of this quotient, omitting loops. Assign a
letter to a root component in at most 2r ways. For every other component,
the edge to its parent excludes exactly one of the 2r possible letters:
the one that would create cancellation at that consecutive pair of
positions, after accounting for the two signs. There are at most q
remaining choices. Ignore every other adjacency constraint and every
fixed-coefficient value for an upper bound. Therefore the number of
reduced words for this scheme is at most

    2r q^(c-1) <= 2r q^((n+C)/2).                                 (3)

The n=0 case is a separate singleton. Multiplying (3) by the number of
positional schemes proves

    count at length n <= K (n+1)^(2t) q^(n/2),                     (4)

where K may depend on r,t,C but not on n. Summing over lengths at most
n changes only the constant or polynomial factor. The proof handles
overlaps, inverse occurrences, occurrences crossing coefficient blocks,
and coefficients tied to other positions. It does not assume disjoint
repetitions or independently assign every repeated block.

## 3. Consequence for sub-multipatterns

The first equality in a one-variable parametrization is precisely a
fixed concatenation of the form in Section 2: every variable occurrence
is a piece, and an inverse variable value is a piece as well. If there
are no variable occurrences, there is at most one output word. Thus (4)
applies to each parametrization. A finite union and then an arbitrary
subset preserve an upper bound of the form

    B_S(n) <= K_S (n+1)^D_S q^(n/2).                              (5)

It follows that **no sub-multipattern is finite-translate generic**.
For fixed g, left multiplication gives

    B_(gS)(n) <= B_S(n+|g|).

Any finite union of translates still has exponential upper rate at most
sqrt(q). It cannot cover F_r, whose balls have exponential rate q,
since q > sqrt(q) for r >= 2.

This is the quantitative step used here. KM Lemma 17 and Proposition 20
state a weaker density-zero conclusion from a single long repeated
piece. Our bound uses the repeated-piece coverage of the entire first
pattern, outside its fixed coefficient positions. A single repeated
piece without that coverage would not suffice.

## 4. Put a nonprimitive orbit in one sub-multipattern

Let w be nonprimitive. By Pillay's Theorem 2.1(i), w does not realize
p_0. Hence some parameter-free formula phi(x) in p_0 is false at w.
Let

    P = {v in F_r : not phi(v)}.

Every automorphism preserves parameter-free formulas, so P contains
the entire automorphic orbit of w. A basis element a realizes p_0,
so phi(a) holds, and the definition of generic element says that
F_r minus P is finite-translate generic.

By KM, P or its complement is a sub-multipattern. Section 3 rules out
the complement, because it is generic. Thus P is a sub-multipattern.
The orbit bound (1) follows from (5).

No definability of the orbit, no definability of the primitive set, and
no formula defining “is an automorphism” are assumed. The formula phi
depends on w, which is allowed because an individual fixed orbit is
being counted. Its existence suffices; no effective construction of
phi or of the constants in (1) is claimed. If genericity is formulated
in an elementary extension, a cover by a fixed finite number of left
translates is expressed by an existential-universal first-order sentence
and descends to F_r by elementarity.

## 5. Matching lower bound

Replace nontrivial w by a cyclically reduced conjugate v, in the same
automorphic orbit, and write l=|v|. For m >= 1 choose a reduced word t
of length m whose last letter is neither the inverse of the first letter
of v nor the last letter of v. At most two of the 2r letters are forbidden.
There are at least (2r-2)q^(m-1) such t. Each t v t^-1 is reduced as
written, of length 2m+l. Distinct t give distinct words, since their
first m letters recover t. These conjugates are automorphic images.

For balls choose m=floor((n-l)/2), for all sufficiently large n. This
gives a constant times q^(n/2) lower bound. Together with (1), it proves
the ball limit sqrt(q). Taking the subsequence n=2m+l gives the same
spherical limsup. This standard conjugacy lower bound is prior material.

## Status and limits

The proof is a candidate consequence of the two cited theorems and the
piece-cover counting lemma above. It covers all finite ranks, including
words with primitive abelianization and primitivity rank greater than
two. It subsumes the earlier F41 partial candidate without adding a
second entry. Known special cases remain credited in
[the earlier proof](rank-two-proof.md).

Myasnikov--Roman'kov, *On Asymptotic Properties of Verbal Subsets in a
Group* (2015), [doi:10.1134/S1995080215040113](https://doi.org/10.1134/S1995080215040113),
is another relevant predecessor. For nonprimitive abelianization, the
proper verbal-value set gives a definable superset and hence the same
kind of counting route using KM. When exponent sums have gcd one the
verbal-value set is the whole group; Section 4 avoids that limitation.
No novelty is asserted merely from failing to find a matching paper.

Finite checks audit the counting mechanism, not the imported infinite
theorems or the existence of phi. Exact scope, failures, source-reading
limits and checks are recorded in [the audit](multipattern-audit.md).
