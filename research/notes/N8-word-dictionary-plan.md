# N8 ordered-word interface: closing formalization plan

30 September 2026, during the original run. This addresses a specific
remaining interface in Section 5 of the existing candidate; it adds no
problem or novelty count. The preceding goal turn made concrete progress
through commits dfefbc1, a14c92e, 1521fc9 and 3bcc92f.

Use finite rational linear combinations of ordered m-tuples of natural
indices as the homogeneous m-letter word component. Embed a tuple into
the free monoid by its ordered list, then into the rational monoid algebra.
Prove this embedding injective. The positional polynomial encoding is a
linear equivalence using the finite-index exponent-vector equivalence;
it is not asserted to preserve ordinary algebra multiplication.

Prove prefix/suffix insertion corresponds to actual multiplication by
E_j in the free associative algebra, and encode those insertions by the
appropriate variable power and renaming. Incrementing each tuple position
in turn is the homogeneous action of the derivation E_i maps to E_(i+1).
Check its encoding as multiplication by the sum of positional variables.

Connect these identities to the already checked rational polynomial
theorem, with no bound on dimension or degree. Seek the stronger explicit
conclusion that the original D is a scalar multiple of the all-zero word,
and that V vanishes. Also connect the component increment operator to an
actual global free-associative derivation by a recursive word rule and
its Leibniz identity, if completed within the current window.

The free-Lie exclusion of E_0^m, homogeneous Lie projection, arbitrary
correction-block instantiation, leading-pair enumeration, exact integral
periods and the full nilpotent-group algorithm remain separate tasks.
Do not claim that a successful dictionary check verifies those steps.
Retain exact failed source versions and report only the formal theorem
that actually compiles without unapproved axioms.
