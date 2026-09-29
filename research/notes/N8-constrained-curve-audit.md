# Constrained-curve arithmetic audit

29 September 2026. This supports the arithmetic lemma in
`N8-constrained-curve-lemma.md`. It does not promote the prospective
three-exception group argument or change N8's candidate scope/count.
The construction is an application of prior effective arithmetic, not
an arithmetic novelty claim.

## Proof audit

The reduction keeps the leading quadratic coefficient constant and
nonzero. Completing the square therefore reconstructs the second
integer variable with a fixed denominator. Repeated polynomial factors
are extracted integrally; integer roots of the extracted square factor
are retained separately. Constant and zero discriminants have their own
branches. Every additional congruence is multiplied by the appropriate
denominator power **and its modulus by the same factor**.

For squarefree residual degree>=3, Berczes--Evertse--Gyory2013 Theorem2.2
supplies an explicit bound. The source's common hypotheses and its
logarithmic-height convention were checked. Its full proof is imported,
not independently established here. No high-degree height-bound
enumeration is implemented or claimed to have run.

For residual degrees0 and1, fixed-denominator substitution leaves
univariate equations and periodic congruences. For degree2, the nonzero
discriminant makes the positive-definite and split cases finite and
the nonsquare norm conic irreducible. Further equalities either vanish
on that conic or give a nonzero elimination resultant. Disequalities
remove only finitely many points unless they reject the entire conic.

For nonsquare positive norm coefficient, an integral norm-one unit and
a proved finite seed box cover every solution, including both signs
of the norm and both signs of each coordinate. Its matrix is invertible
modulo each fixed modulus, so complete finite residue cycles also cover
negative unit powers. Every allowed cycle gives an infinite sequence
of distinct actual integer points. A finite set of exclusions therefore
cannot turn such a positive decision into a negative one.

The lemma permits rational coefficients only with fixed denominators;
it does not supply a decision algorithm for arbitrary integer curves.

## Exact implementations and independent checks

`scripts/check_n8_curve_arithmetic.py` constructs the finite evidence.
`scripts/check_n8_curve_arithmetic_gap.g` replays it with native GAP
integer and polynomial arithmetic; it imports no Python solver.

The final certificate is `research/certificates/N8-curve-arithmetic/v2/`.
It contains244 complete Pell decisions:49 positive and195 negative.
The norm coefficients are2,3,5,6,7,10,11,12,13,17; every nonzero norm
between-12 and12 is included, along with four extra controls. Thus
positive coefficients containing a square factor are included too.
Fixed congruence moduli are drawn from1,2,3,4,5,8,12. There is no random
seed or parameter-search cutoff in the complete decisions.

Python enumerates the proved seed boxes by the second coordinate;
GAP independently enumerates them by the first. They agree on all706
seeds and463 complete modular states. GAP checks every transition,
every cycle closure, disjointness, the seed-to-cycle association and
every accepted/rejected residue. All49 positive witnesses are rebuilt
as actual unit powers and checked in the original norm equation with
their congruences and finite exclusions. Five initial candidate points
are skipped because they were deliberately excluded. Negative decisions
come from complete seed/orbit exhaustion, not a bounded witness search.

Eleven polynomial records independently check square completion,
integral square-factor removal, squarefreeness, the complete integer
roots of the removed factor, and the reconstruction identities. There
are1137 congruence equivalence checks on integer reconstructed values;
these grid checks supplement the exact polynomial identities and are
not a claim that a finite grid proves the general lemma.

The wrong-modulus control is an actual curve point: a=5, b(T)=10T,
c(T)=5T^2-5, T=0, R=1. The extra polynomial h=R^2+TR+2 equals3.
Multiplication by(2a)^2 gives300. Reducing that result modulo5 alone
would incorrectly accept it; reduction modulo500 correctly rejects it.

Seven conic controls use X^2-2W^2=7 with additional equalities. GAP
independently reduces each polynomial modulo the conic and constructs
its Sylvester determinant by the exact Leibniz formula. It agrees on
all complete integer root lists and ten finite intersection points,
including empty intersections, a constant nonzero resultant and an
equality that vanishes on the whole conic. This checks these controls,
not an exhaustive implementation of every low-degree branch.

## Runs and retained implementation failure

- `n8-curve-arithmetic-v1`: pass,0.971545 seconds. Initial244 Pell
  decisions, ten polynomial records and1122 congruence controls.
- `n8-curve-arithmetic-gap-v1`: pass,1.975408 seconds. Independent
  replay of that initial suite.
- `n8-curve-arithmetic-v2`: pass,1.021588 seconds. Adds the eleventh
  polynomial record, wrong-modulus control and seven intersections.
- `n8-curve-arithmetic-gap-v2`: fail,1.927215 seconds. GAP's default
  determinant method does not accept the mixed integer/polynomial
  matrix representation. Its executed source and raw error are retained.
  GAP returns status0 after this error, but the recorded runner correctly
  rejects the missing success marker; exit status alone is not a pass.
- `n8-curve-arithmetic-gap-v3`: pass,1.976183 seconds. The independent
  checker uses the Leibniz determinant for matrices of size at most5.
  No equation or test case was removed.

All successful stderr files are empty. Superseded executed sources are
saved beside their run records. All jobs are terminal; this arithmetic
work used one reserved core and4GB. No push or external contact.

## Literature and remaining group work

The archived Berczes--Evertse--Gyory2013 statement-reading limits remain
those of the lemma. Conrad's *Pell's equation, II* was archived from his
university page, SHA256
`9b434917be414d647f537428721118ee783602e216aa93daec36713365b539e6`.
Sections1--3 through the proof of Theorem3.3 on printed page6 were read;
actual page5 viewed. The elementary seed proof is supplied in the lemma
using a deliberately looser integer box. Later examples not audited.

`N8-three-exception-curve-reduction.md` is a separate, unadopted draft.
In particular its early-truncation branch needs all initial constraints
to be affine in the second parameter; this is now explicit. Complete
integer block quotients, an actual delayed quadratic group family,
and subsequent universal-residue normalization still need a focused
audit. No leading-degree12, arbitrary-class three-exception or class26
candidate extension is adopted from these arithmetic tests.
