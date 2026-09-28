# M0 internal audit

28 September 2026. Candidate only; no independent specialist review yet.

## Statement fidelity and counting

The original M0 refers to F3 and replaces free groups by free metabelian
groups. F3 explicitly requires finite rank and preservation of every
primitive **element**. Both rendered paragraphs were inspected. The proof
uses precisely these hypotheses. It does not assume preservation of
primitive tuples, surjectivity, or tameness of all automorphisms.

Count as one whole-entry candidate, with ranks at least three the potentially
new range. Do not count the already known rank-two answer, F3, or the
bibliographically identical Kourovka 14.85 as additional discoveries.

## Main points checked

1. Abelianization alone only proves that the induced integer matrix is
   unimodular. The subsequent Fox argument is needed for the group map.
2. The determinant at augmentation is one in the IA case. A nonunit thus has
   at least two monomials; choosing a prime that retains them prevents its
   reduction from accidentally becoming a unit.
3. The residue field is finite because the Laurent ring is finitely generated
   over F_p. Its multiplicative group is cyclic. This finiteness is essential
   to arranging all but one character value to be one.
4. Integer Euclid on the character exponents produces d coprime to the image
   order m, not necessarily d=1. That suffices: s^d generates the same cyclic
   group and hence the same field. No unjustified prescribed-generator
   Nielsen equivalence is needed.
5. Basis change at a fixed character gives similarity for an IA map. For a
   general map the two characters would differ, so the IA reduction must
   come first.
6. In (5), i,j,n are distinct. The appended word omits x_i, which makes the
   operation an actual free-group automorphism. The derivative in the x_n
   direction cancels; there is no discarded cross-coordinate term.
7. The polynomial P need only have nonnegative exponents: a finite algebraic
   extension F_p(t) equals F_p[t]. Integer coefficients map onto F_p.
8. Evaluated Jacobians form a representation on the character stabilizer.
   Otherwise a composition would twist the evaluation. Every operation (5)
   is in that stabilizer.
9. SL_{n-1}(K) is transitive on nonzero vectors only when n>=3. The proof
   explicitly treats n=2 by the kernel-line argument.
10. Only the necessary Fox condition for primitive elements is used.
    No converse column-completion assertion is needed. The full square
    Jacobian criterion at the end is the classical metabelian theorem.

## Explicit singular examples

Here [u,v]=uvu^-1v^-1, and Fox derivatives are left derivatives as columns.
These examples test the proof mechanism; they are not counterexamples to M0.

For M_3=<x,y,z>, set

    phi(x)=x[y,z],    phi(y)=y[x,z],    phi(z)=z.

Every individual generator image is primitive (append a word in the other
generators). At the character (x,y,z) -> (1,1,2) in F_3, the Fox matrix is

    [ 1 -1  0 ]
    [-1  1  0 ].
    [ 0  0  1 ]

The primitive word xy has column (1,1,0)^t. Its image has zero column at this
character and therefore is not primitive in M_3. This shows why testing only
the basis generators would be insufficient.

For a proper field-extension test, let K=F_4 and t^2+t+1=0. Put

    psi(x)=x z^2[y,z]z^-2,    psi(y)=y[x,z],    psi(z)=z.

At (1,1,t), its matrix is

    [ 1 t^2 0 ]
    [ t  1  0 ].
    [ 0  0  1 ]

The primitive word w=xzyz^-1 has column (1,t,0)^t in its kernel. Again
D(psi(w)) evaluates to zero. This checks that polynomial coefficients over
a genuine extension field, rather than only prime-field coefficients, are
being realized by actual primitive words.

The test suite also conjugates the singular endomorphisms by free-group
automorphisms and changes the character accordingly, to exercise basis
changes with more than one nontrivial character value. Positive controls
use explicit free-group automorphisms whose Jacobians remain invertible.

## Evidence limitations

The Python and GAP checks are independent implementations of finite-field
arithmetic and word evaluation. GAP checks complete two-sided inverse-basis
certificates in a free group. They do not prove the universal orbit lemma or
novelty; those require the argument and literature audit respectively.

Initial GAP run `m0-gap-v1` failed because this installation has no
`KroneckerDelta`. The runner correctly marked it unsuccessful despite GAP's
zero exit code. The only code correction for `m0-gap-v2` was to compare the
indices explicitly. All 177 records then passed with empty stderr.

The primary 2020 paper explicitly distinguishes the unresolved individual
element question in higher rank from earlier results on primitive systems.
An apparent positive abstract about “systems” must not retire M0 without
checking its tuple-length hypothesis. Further searches beyond the sources
currently recorded may still reveal a prior complete answer.
