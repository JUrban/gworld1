# Audit of the odd-adjoint family

29 September 2026, before the original deadline. This is internal proof
review and independent software checking, not outside specialist review.
The candidate argument is [odd-adjoint-proof.md](odd-adjoint-proof.md).
The original uncounted lead and its failed structural run are preserved.

## Exact scope

The frozen N8 source paragraph was re-read and its rendered statement
viewed again during this audit. Only part (a) is starred. Part (b) asks
for all finitely generated free nilpotent groups. This extension covers
a specific recognizable family in classes11,15,19,..., in every finite
rank, with unrestricted coordinates in the two layers above its prescribed
leading term. It does not answer every target in these classes or the
whole of N8(b). It extends the existing partial candidate, adding no
problem count. The separate all-target result through class ten remains.

## Separate proof and implementation review

The leading-type exclusion uses a nonzero jet multidegree to force one
factor to be T, then a different associative word to contradict membership
in [T,L']. It does not assume that the factors are homogeneous in the
number of jet letters. Projection is applied to the full homogeneous
factors, and the single exceptional multidegree still forces their
original weights. The coefficient h+2 is nonzero for every odd h>=3.

The direction proof separates the two cases T'!=0 and T=[a,b]. In the
first, all non-a letters already occur inside the chosen inner word;
terms from [a,b] cannot contribute. In the second, the explicit coefficient
is -2^(h+1), not just a bounded observed nonzero value. Both arguments
survive arbitrary rational basis changes. The two outer quadratics
force the same one-dimensional direction in every rank.

The polarization convention was checked independently of the rank-two
tests. The implementation's columns are ordinary monomial coefficients,
computed by total-degree-h finite differences divided by alpha factorial.
Thus the solved coefficients are rho times monomials in T, without a
second multinomial factor. A nonzero diagonal determines T up to scale;
every remaining tensor entry is checked. This is a rational pure-power
test, not unrestricted rational equation solving. The rank-three sum-of-
two-cubes control would be invisible in a one-dimensional L2 test.

For the first kernel, the extra seed S is tracked separately. Its
projected [S,D] is independent of the S-jet variable, whereas the delta
image is divisible by the sum of all jet variables. This excludes every
other direction. The final obstruction is separated by bracket length
and minimal weight after projection to the single T chain. No finite
matrix rank substitutes for either universal argument.

All signed integral leading scales are retained. Nonintegral rational
leading data are distinguished from failure to recognize the family.
The full first integer solution lattice is used; its primitive kernel
generator need not equal the rationally normalized T,V direction.
The final residual has degree at most two by weights: the mutual first
correction is visible in degree c, while two low corrections acting on
the high leading factor first contribute in degree c+1. Its nonzero
rational cokernel component bounds the integer parameter set, after
which full integral lattice membership is still required.

No gap was found in this internal audit. Independent specialist review
and a conclusive novelty assessment remain outstanding.

## Completed computations

The earlier structural probe, now a dependency of this extension, checks
h=1,3,5,7 with separate untruncated associative arithmetic: four identities,
eight outer-square coefficients, the h+2 coefficients for h>=3, and the
obstruction coefficient. Rank-two/class-eleven Hall calculations found
only the two signed type(1,8) leading pairs, first nullity one among57
columns, and final ranks101 and102 before/after adjoining the obstruction.

Its first GAP replay timed out at120.018 seconds without confirming an
individual check. The revised replay first verified all412 Hall-word
trees and then passed in4.835 seconds. This failure and successful retry
remain separate. GAP checked the kernel direction, dimension and final
cokernel; it did not re-enumerate the complete leading-pair list.

The new group suite uses deterministic seed9292611. Its ten records are:

- four positive cases: the displayed pair, two pairs with nonzero kernel
  and higher corrections, and a nonprimitive pair with a negative scale;
- three negative cases: two final-layer perturbations and one preceding-
  layer perturbation;
- three unsupported controls: a different leading family of the same
  degree, the identity and a degree-one word.

Python completed in67.943 seconds with empty stderr. It retained four
group witnesses, ten first-layer linear decisions and eight polynomial
certificates, of which four have no admitted integer parameter.

GAP independently completed in16.874 seconds with empty stderr. It
verified all four witnesses, ten linear decisions (two negative), eight
polynomial decisions (four empty) and forty sampled affine group pairs.
For each of the eight polynomial branches it also checked the first
affine particular solution, a nonzero primitive kernel vector, and
rational nullity one. These prove that the affine line includes every
integral first-stage solution. The final checks recompute the Hermite
identity and unimodularity, rational residual, divisibility congruences,
complete quadratic root list, and actual group correction columns.
Samples alone are not used to prove the polynomial degree or root list.

A separate rank-three calculation completed in19.385 seconds with empty
stderr. It accepted a two-form not containing z and a mixed direction/
mixed form with negative scalar, and rejected a sum of two independent
cubes and a leading term nonzero in the metabelian quotient. These are
scope-recognition checks only: no rank-three group decisions or GAP replay
are claimed. No class15 or19 group decisions were run; those classes have
formal identity checks and the universal proof.

## Sources, execution and reproduction

The structural primary ingredients retain their citations from the earlier
N8 proofs, especially the delta-stable free alphabet in class9-proof.md.
No additional external theorem or Kourovka result is imported here.
A bounded current search for free-nilpotent single-commutator decision
results found no matching theorem for this family. This is not proof
of novelty. An indexed AMS1978 abstract by Kenneth W. Weston concerns
rank-two/class-two commutator equations; that previously solved scope
does not cover this extension. The PDF exceeded the downloader's20MiB
cap, so no full-PDF or proof inspection is claimed for that abstract.

Relevant new jobs are `n8-odd-adjoint-groups-rank2-v1`,
`n8-odd-adjoint-leading-rank3-v1` and
`n8-odd-adjoint-groups-rank2-gap-v1`. Each used one core and4 or8 GB
per-process memory. At most two ran concurrently. All completed normally;
there were no failed new group or recognition runs. The prior structural
timeout is retained under its original job name.

The implementation is `scripts/n8_odd_adjoint.py`. The group replay is
`scripts/check_n8_odd_adjoint_groups_gap.g`, using the new audited core
derived from the existing sparse GAP checker. The prior checker was not
modified. Exact executed sources, inputs, output hashes, actual return
codes and dependencies are indexed in
`research/certificates/N8-odd-adjoint/artifact-hashes.json`.
Use new output directories for reproduction; preserve the existing ones.

The original clock and frozen corpus are unchanged. All recorded jobs
are terminal. Counts remain four whole-entry candidates, four partial
candidates and zero established novel results. No external contacts,
agents or push occurred.
