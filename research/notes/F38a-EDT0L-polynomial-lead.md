# F38(a): an uncounted EDT0L polynomial-identity lead

First developed during the 28 September 2026 continuation after the
21:43 UTC checkpoint; recorded at 2026-09-28T21:47:26.274355+00:00.
Not yet a candidate: the exact primary equation-solution representation,
component labels, rational constraints and proof details need verification.

For an endomorphism phi of F_r, nonzero determinant on abelianization
implies injectivity: its image has rank at least r and at most r, and
an epimorphism between rank-r free groups is an isomorphism. KLSS
Corollary 1.4 equates translation equivalence with equality of cyclic
lengths under every injective endomorphism. Since automorphisms have
nonzero determinant, F38(a) is equivalent to the universal vanishing of

    det(Ab(phi)) * (cyclic_length(phi(u))-cyclic_length(phi(v)))

over all endomorphisms phi. This is not a test requiring det=1.

Introduce free-group equations and regular constraints expressing that
U,V are cyclically reduced conjugates of u(X_1,...,X_r),v(X_1,...,X_r).
Their lengths and the abelianization entries of the X_i are linear in
component-labelled Parikh counts. The displayed expression is therefore
a polynomial of degree r+1 in these counts.

An effectively EDT0L set with rational control appears to admit a
polynomial-identity test: lift the incidence matrices of its finitely
many morphisms to monomials of bounded total degree, and compute the
reachable rational-vector-space span at each control-automaton state.
A polynomial vanishes on every output exactly when its linear functional
vanishes on that finite span. Terminal-alphabet filtering is handled by
a finite support automaton. Component labelling must be justified from
the actual primary representation, not assumed as an arbitrary closure
property of EDT0L.

Possible route to a full F38(a) algorithm in every finite rank. No F38(c)
bounded-ratio algorithm follows from this identity test. No count yet.
