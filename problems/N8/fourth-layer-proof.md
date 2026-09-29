# Every fourth-from-last target

29 September2026. Candidate extension of the same partial N8(b) entry.
Implementation/check status is recorded in `fourth-layer-audit.md`.

**Proposed theorem.** For every finite rank r and class c>=7, membership
in the single-commutator set is decidable for targets whose nonzero
leading term has degree c-3. Together with the previous three deepest
layers this covers gamma_(c-3). Other lower layers in arbitrary class
remain outside this theorem; low-class all-target results are retained.

Use the same complete normalized integral leading pairs C in Lp,D in Lq,
p<=q, p+q=c-3, and the convention [x,y]=x^-1 y^-1 x y. Their enumeration,
including signed scales and equal-weight Hermite sublattices, is unchanged.
The new step is to keep all remaining corrections together rather than
choose one solution in a lower-class quotient.

## 1. Finitely many first corrections

The uniform first-map results in `third-layer-proof.md` are independent
of the ambient truncation. For each leading pair solve its integral
first correction (U,V) of weights p+1,q+1.

If inconsistent, reject the branch. If its kernel is zero, retain its
unique integral solution. Equal leading weights have this property.
For adjacent leading weights the exact move x->y^k*x preserves the
commutator and normalizes the affine parameter to the finitely many
residues modulo content(D). Changes in higher coordinates caused by the
move will be retained in Section2.

Otherwise q>=p+2 and the full first solution set is a primitive integral
line v+nK. Consider only the residual in degree p+q+2=c-1. It is an
integer-valued polynomial of degree at most two in n. Its quadratic
coefficient has nonzero image modulo

    [L_(p+2),D]+[C,L_(q+2)],

by the previously proved uniform obstruction. That argument is applied
in the quotient of class c-1, not incorrectly to the full residual in
class c. A rational cokernel coordinate restricts n to at most two
integer roots. Test all integral second-layer congruences and retain
all roots passing them. Each is a possible first correction, not yet a
solution of the original equation.

This gives finitely many fixed first-corrected pairs (x,y) covering every
possible solution up to exact Nielsen transformations. No arbitrary
particular second correction is chosen. Its entire solution lattice
must remain available for the next step.

## 2. The complete remaining tail is linear

For one fixed (x,y), allow right corrections h to x of weights at least
p+2, and k to y of weights at least q+2. Keep their Hall coordinates
through weights p+3 and q+3 respectively; all later coordinates have no
effect on the commutator through class c=p+q+3.

Their cross interaction first has weight

    (p+2)+(q+2)=p+q+4>c.

Interactions of two corrections to x with the opposite leading factor
have weight2(p+2)+q>c, and symmetrically p+2(q+2)>c. These inequalities
also discard nonlinear Hall-power terms. Consequently the full change
of commutator through degree c is linear in ALL these correction
coordinates together. Fixed lower coordinates can contribute to the
linear columns; they are not replaced by leading Lie terms alone.

The residual is in gamma_(c-1), which is central enough that its coordinates
add: 2(c-1)>c. Compute the exact group increment for each unit Hall
correction, express it in integral tail coordinates, and solve one integer
linear system for the whole residual. Smith/Hermite normal form decides
this and constructs all needed corrections when soluble. Every relevant
coordinate is included, so inconsistency rules out this fixed first pair.

The implementation uses `n8_deep_tail.py`, retaining the weight-guarded
formulas from `n8_class10_tail.py` with component-wise integral Hermite
reduction and exact nearest-plane shortening. Its formulas explicitly
assert the inequalities above for the supplied class. The independent
GAP replay computes its columns from actual group
commutators and solves their integral membership problem.

## 3. Why a selected quotient witness is insufficient

A second-layer solution may have a nontrivial kernel. Its different
representatives can give different top-layer obstructions, even though
they agree in the quotient of class c-1. Thus the rule "solve in class
c-1, keep one witness, then correct only the centre" is not justified.
Section2 retains the second-layer kernel automatically in the joint
system. The audit includes an explicit class11 example where the chosen
particular representative fails the final correction but the joint system
has a solution.

There are finitely many leading branches and finitely many retained
first parameters per branch; each remaining integer system terminates.
Positive outputs are verified by exact multiplication in N. This proves
the proposed decision procedure for the stated stratum.

## Attribution and scope

The proof depends on the uniform first-map/obstruction argument, the
previous finite leading-pair machinery and standard integral nilpotent
coordinates. Its imported homogeneous Shirshov and Remeslennikov--Stohr
inner-solution theorems retain their explicit prior credits. The joint
linear-tail argument was already used in our lower-class work and is
reused here with a uniform weight bound. No new Kourovka material is used.

Full original N8 HTML/background and its actual rendering were checked
again this turn. No full arbitrary-class N8 answer, practical complexity
bound, specialist validation or established novelty is claimed.
