# F41: uncounted multipattern/generic-type lead

29 September 2026, active run. This records the initial **unproved lead**.
The later completed candidate argument and audit are now in
`problems/F41/multipattern-proof.md` and `multipattern-audit.md`.
The remainder is retained as the original route and checks to perform.

Proposed chain: Kharlampovich--Myasnikov, arXiv:1111.0577v5,
Definitions 5--6 and Theorem 13, say that a one-variable definable set
or its complement is a sub-multipattern. Pillay's characterization of
generic elements as primitive elements may put each nonprimitive
automorphic orbit inside a parameter-free nongeneric definable set.
If all one-variable sub-multipatterns have growth at most sqrt(2r-1),
this would give the full intended F41 upper bound.

Proposed counting lemma: fix the first noncancelling pattern, with C
coefficient letters and m variables. Choose variable lengths and a
second occurrence (position and orientation) of every variable image
in the output word. These choices have polynomial multiplicity in
output length n. Every nonconstant position is then equated, possibly
with inverse orientation, to a different position. Collapse these
signed equalities; inconsistent inverse cycles are impossible. There
are at most (n+C)/2 components. The position path induces a connected
graph on the components. Its spanning tree bounds reduced assignments
by 2r(2r-1)^(components-1), giving polynomial times (2r-1)^(n/2).

Must audit: the exact meaning of a piece; overlapping and inverse
occurrences; all copies of variables in the first pattern; constant
positions and empty/singleton exceptional sets; the spanning-tree
count with signed constraints; the exact primary generic-type theorem;
the passage from a nongeneric realization to a parameter-free formula;
why the complement cannot be a sub-multipattern; and current prior
literature. The generic-type and definability theorems are substantial
imported dependencies, not established by local finite tests.

The existing rank-two/low-primitivity-rank candidate remains the only
counted F41 scope until this chain has been checked. The prior verbal-set
paper by Myasnikov--Roman'kov (2015) may already cover nonprimitive
abelianization after a counting refinement; it does not cover primitive
abelianization by the word-values argument because those word maps
are surjective.
