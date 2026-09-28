# A4: a prior algebraic cyclicity algorithm

28 September 2026, approximately 15:18–15:21 UTC. This is a routine
consequence of prior results, excluded from discovery counts.

The full original algorithmic page, exact A4 fragment, linked background
and rendered paragraph were inspected. The question asks for an
algebraic decision whether a knot group is cyclic. We use the usual
classical-knot meaning and a finite presentation promised to present
such a group; no recognition of the promise is required.

Hass, [*Algorithms for recognizing knots and 3-manifolds*](https://arxiv.org/abs/math/9712269),
section 6 and Theorem 10, gives a two-process unknot algorithm. Its
negative branch enumerates homomorphisms to finite symmetric groups,
using residual finiteness of knot groups; its positive branch searches
for a geometric disk. Read the full section and proof. The source is
archived as `literature/raw/A4-Hass-math9712269.pdf`, SHA-256
`d85b4f4867bced1c6fd3f8324f75de1e07d69a736771b3a5d3065569d806317c`.

For the presentation-only version, replace the positive branch by
enumeration of formal consequences proving that every pair of
presentation generators commutes. There are finitely many such pairs;
this branch terminates exactly when the presented group is abelian.
A classical knot group has abelianization Z, so in this promised class
being abelian is equivalent to being infinite cyclic.

Concurrently enumerate all maps of the presentation generators to S_n,
for n=1,2,..., retain maps satisfying all relators, and stop negatively
if the image is nonabelian. For a nonabelian knot group some generator
commutator is nontrivial. Residual finiteness supplies a finite quotient
where it survives, and that quotient embeds in a symmetric group.
Thus precisely one of the two searches eventually stops.

This is an algebraic procedure on the presentation. Its termination
uses the established residual-finiteness theorem; no claim of a
purely algebraic proof of that background theorem or an efficient
complexity bound is made. No mathematical computation was needed.
