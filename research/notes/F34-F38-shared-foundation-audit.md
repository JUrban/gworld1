# F34(a)/F38(a): shared foundation audit

28 September 2026, approximately 22:31–22:35 UTC. This is an internal
audit and an additional finite-bound observation, not another problem
resolution or an independent specialist review.

## Dependencies checked separately

The two candidates share the constrained full EDT0L solution relation
and its polynomial-identity test. F34(a) additionally uses positivity
reflection through a spanning-tree basis; F38(a) additionally uses KLSS
Corollary 1.4. Neither application needs the other's group-theoretic
lemma. Their shared implementation tests therefore are not two independent
validations of the imported equation-solving theorem.

Re-read the complete F38(a) argument and the F34(a) reduction. The checks
in this pass concern these specific possible failure points:

- Nonzero determinant guarantees injectivity via the rank of the image
  and Hopficity. It does not assert surjectivity or characterize all
  injections. The determinant is allowed to have absolute value greater
  than one.
- Cancellation triangles preserve the full projected tuple relation,
  including the generator-image variables. Mere equisatisfiability would
  not suffice to evaluate the desired polynomial on every endomorphism.
- Counts must remain separated by output component. Reversing the
  control automaton deals with function-composition order; taking the
  Parikh vector of one concatenated output would lose the required data.
- The constant monomial is retained, and empty outputs and an empty
  accepted language have their usual meanings. If terminal filtering is
  required, the finite support product must be taken before span closure.
- This decides existence of a nonzero polynomial value, not existence
  of a zero. No determinant-one constraint or general Diophantine
  length-equality constraint has been introduced.

No gap was found at these points in this internal pass. The full
recompression theorem remains imported rather than implemented or
reproved. The source and implementation evidence is in the original
candidate audit files; no existing certificate or failed run is replaced.

## A finite path-length bound after the grammar is supplied

This gives a second finite termination description for the polynomial
stage. It is not a useful complexity bound for the complete free-group
decision procedures.

Let Q be the finite set of control states after any support product.
Let N be the dimension of the lift to all monomials of degree at most d,
so N = binomial(D+d,d) for D separately tracked count coordinates.
Assume there is at least one initial state. Work in

    V = direct_sum_(q in Q) Q^N,       R = dim(V) = |Q| N.

For each edge e:q->q', define a linear operator on V which kills all
blocks except q and sends that block to q' by the lifted edge matrix.
Place the initial lifted vector in each initial-state block separately.
These vectors are nonzero because the constant monomial has value one.
Let V_m be the span of the block vectors from all paths of length at
most m starting at any initial state. Invalid edge sequences contribute
only zero and do not affect the span. Then

    V_(m+1) = V_m + sum_e L_e(V_m).

If V_m = V_(m+1), this space is invariant under every edge operator and
all later V_j are equal. Otherwise the dimension increases by at least
one. Since dim(V_0)>=1 and dim(V)<=R, stabilization occurs by m=R-1.
More precisely it occurs by R-dim(V_0).

For each final state q, let the linear functional ell_q evaluate the
desired polynomial on its block and vanish on other blocks. If there
is any accepted path with a nonzero value, ell_q is nonzero on the
eventual span for some final q. Since V_(R-1) is that span, one of the
actual paths of length at most R-1 already has a nonzero value. Thus
bounded enumeration of all accepted control paths through length R-1
is another exact decision procedure. Span closure is normally preferable.
If there are no initial states, the relation is empty and the identity
holds vacuously. Identity-labelled epsilon edges can be counted as edges;
their presence does not alter the argument.

The bound is on control-path length, not on the lengths of its output
words. Expanding morphism compositions can make the latter much larger.
The size and construction cost of the imported solution automaton have
not been combined with this observation into a whole-algorithm bound.

## A boundary: this does not settle F39(a)

Replacing positivity by membership in a prescribed finitely generated
subgroup breaks the reflection argument. In F(a,b), let

    S = <a^2,b^2>,       w=a,
    phi(a)=a^2,          phi(b)=b^2.

The determinant is four, so phi is injective, and phi(w) belongs to S.
But S contains no ambient primitive element: every element has both
abelianization coordinates even, while the abelianization of a primitive
element is a primitive integer vector. Hence no automorphism can send
w into S. An existential determinant-nonzero endomorphism test would
return a false positive for F39(a).

F34(a) avoids this obstruction through the special spanning-tree
positivity lemma. F38(c), which asks for bounded ratios, also does not
follow from a polynomial-identity test. Both limits remain explicit.

## Counting and follow-up

This note adds no candidate and no test count. The current tally stays
four whole-entry candidates, four partial candidates, zero established
novel results. Return to a different unresolved mathematical lead;
additional finite samples of the existing polynomial stage are not
needed in the absence of a new failure hypothesis.
