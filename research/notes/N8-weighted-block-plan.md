# N8 weighted word-block instantiation

30 September 2026, within the original window. The previous turn made
concrete progress through a9f77c7, c133fa2, 953d3d7 and 00820dc. The active
clock, clean worktree and empty registry were revalidated at 03:25 UTC.

The remaining bridge has two bounded parts. First give E_j weight u+p*j
and define homogeneous word combinations by their actual coefficients.
For a nonzero homogeneous Lie D of weight q>u, exclude the m=1 scalar-E_0
case explicitly and deduce a nonzero diagonal image of [E_0,V].

Then instantiate the abstract block argument using actual ordered-word
commutators and derivative images. Earlier relations have the form
b[E_0,F_j] + sum_(k<j) c_jk[E_(n_jk),F_k] = delta(G_j).
Applying the concrete restriction gives the already proved triangular
system. Later columns have the corresponding sum over t<i<=2t, plus a
derivative image. Prove that restriction kills their complete span, but
not b^2[E_0,V], and derive the at-most-two-parameter conclusion.

This supplies a concrete associative-word block interface. It still
assumes that the written homogeneous projection/group-coordinate argument
produces those relations. Mathlib's pinned FreeLieAlgebra source expressly
separates its abstract quotient from the associative Lie-span model and
notes the PBW boundary. No formal identification or group algorithm will
be inferred from a successful block check. Preserve every attempted input
and audit transitive axioms as in the preceding components.
