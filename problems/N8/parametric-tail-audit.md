# Audit of the overlapping-kernel tail

29 September 2026. Work in progress; the class-18 boundary replay is pending.
The claims ledger has not yet adopted the general extension in
`parametric-tail-proof.md`. This file distinguishes the symbolic argument,
complete arithmetic decisions, and actual group checks.

## Fixtures and what they represent

The constructor uses the weighted free nilpotent group on a,e of weights
1,4, truncated at weighted class 15 or 18. It chooses leading factors
C=u*a and D=v*ad_a^4(e), of weights 1,8. Their correction kernels have
dimensions 1,0,1 at offsets 3,4,5, so they exhibit a real overlap beyond
the previous separation criterion. The whole correction spaces of this
weighted two-generator algebra are used, rather than just the two kernel
directions. These are not enumerations of every ambient rank-two component
when e is realized in ordinary degree four.

The first factor is an actual generator power. The second has pure
logarithm v*ad_a^4(e); v is a sufficient coefficient-denominator multiple
found from the proved finite-degree Hall coordinate polynomials. It is
not asserted minimal. The class-15 case has u=2, v=15120 and Hall rank 35.
The class-18 case has u=1, v=4989600 and Hall rank 76. Both retain the
first kernel's complete integer parameter and solve the successor layer
jointly before retaining every higher correction coordinate.

The class-15 fixture has 13 tail coordinates and a 22-row polynomial
system. Its complete allowed parameter set is {-6,6}; the algorithm
constructs factors at -6, while the planted construction used +6.
Increasing one final target Hall coordinate produces a negative answer
for this fixed lower-coordinate branch. It is **not** a proof that the
modified target has no other leading branch or no commutator expression.

The polynomial interpolation degree is justified by weight, not guessed
from stable samples: it is floor(c/4), giving four class-15 samples and
five class-18 samples. Each polynomial sample includes two full vectors
of simultaneous positive and negative correction exponents. Exact finite
collection of the relative error takes place in an abelian tail, so its
Hall coordinates are linear and satisfy the same polynomial degree bound.

## Independent GAP group replay

`scripts/check_n8_parametric_tail_gap.g` constructs each weighted group
afresh with `nq`, using free-group Hall relators beyond the cutoff. It
checks the resulting Hirsch length and torsion-freeness, reconstructs the
Hall words, and independently confirms all three complete kernel dimensions
in the native rational free associative algebra. No Python tensor engine
is imported.

The strengthened checker also tests completeness of the integral successor
line inside the actual group. In its abelian successor tail, native
polycyclic exponent vectors compute the rank of the joint columns modulo
the higher tail. Their kernel has rational dimension one. Both the supplied
point and its translate by the supplied primitive direction solve the
successor equations. Since that direction is primitive as an integer
vector and its first coordinate is nonzero, every integral solution in
the rational affine line is an integral translate of it. This verifies the
full parameter lattice, not only selected values of the first parameter.

For all interpolation values GAP compares every polynomial correction
column and target residual against direct group commutators. It checks
the two simultaneous correction vectors, the negative target change, the
exact matrices passed to the arithmetic verifier, and both known and
computed factors. It also reconstructs the computed factors directly from
the arithmetic witness. All admissible tail coordinates are explicitly
checked to be present.

Class-15 replay totals: **52 polynomial columns, 8 joint controls, 4
negative-target comparisons, 3 complete kernels, 1 complete integral line,
and 2 group witnesses**. Its constructor passes in 14.918898 seconds; the
strengthened GAP replay passes in 29.422313 seconds. The initial, successful
group replay before adding the complete-line check is also retained.
The final checker additionally verifies the actual polynomial coefficient
degrees and completeness of the successor coordinates; its class-15 replay
passes in 27.157889 seconds with the same totals and empty stderr.

Independent arithmetic replay for class 15 checks both full finite
parameter sets, 4 finite decisions, 42 fixed-parameter specializations and
1 positive witness, in 2.228003 seconds. A negative decision is a complete
integer-lattice decision on the recorded branch, not a bounded non-hit.
These successful runs have empty stderr.

## Performance failures and the arithmetic implementation change

Class-18 v1 completed all five sets of group samples but timed out after
600.229289 seconds before producing a complete arithmetic certificate.
It is an incomplete run, not a negative decision. Its exact source is
retained alongside the logs. No final fixture from this run is claimed.

Version 2 uses the previously derived exact tail-column identities from
`scripts/n8_deep_tail.py`, with every required weight inequality asserted.
It also saves the polynomial input before solving it. Timed stack dumps
identified the costly operation as SymPy's **integer** Smith decomposition
for a fixed-parameter solve, after the polynomial Smith reduction. It was
intentionally interrupted through the recorded runner after 270.741136
seconds once that diagnosis was available. The saved polynomial input,
diagnostic stack log and exact source are retained. Stack-dump messages
labelled `Timeout` are diagnostic alarms; the run metadata distinguishes
the actual interruption from a wrapper timeout.

The integer step now uses `n8_component_linear.py` / `n8_component_hnf.py`,
the existing exact FLINT Hermite implementation. It verifies each complete
unimodular transformation and retains the full integer kernel. The
mathematical reduction is explained in `parametric-integer-proof.md`.
Q[T] Smith reduction and the finite/periodic decision proof are unchanged.

After this change the 24-system arithmetic suite passes again in 1.673457
seconds and independent GAP replay in 2.226381 seconds, with the same
268 finite decisions, 352 residue decisions, 2040 specializations and
19 witnesses. Both stderr files are empty. The older integer-Smith source
is preserved in the successful original arithmetic run as well as the
group run snapshots; the earlier manifest corresponds to commit `2a01612`.

Class-18 v3 completed the five polynomial samples with ten simultaneous
correction controls and reached a positive `finite_zero_row` decision after
the Hermite replacement. Repeatedly recomputing the polynomial decomposition
while selecting a negative fixture was then expensive. That run was
intentionally interrupted after 336.847572 seconds, with the exact
polynomial input and source retained. Its unfinished final certificate is
not counted as a successful run. The subsequent constructor explicitly
reuses this saved input and checks its dimensions and proved degree bound;
GAP still has to compare every column with actual group operations. This
reuse is recorded in the fixture and is not described as another Python
sampling pass.

Class-18 v4 completes in 166.606471 seconds, using the saved v3 polynomial
input. It has 50 tail coordinates, 63 equations and generic matrix rank
48. Its complete allowed parameter set is {12}; with the recorded affine
origin this means the original offset-three kernel parameter is 6. The
proposed shift in Hall coordinate 34 also has a positive arithmetic answer,
so no class-18 negative certificate is counted. Only that one proposed
shift was tried in v4; the class-15 negative fixture supplies the separate
negative control. V4 performs zero new polynomial samples, which its record
states explicitly, and reconstructs and checks its positive group factors.
Its stderr is empty; the retained diagnostic file contains one timed stack
dump, not a process failure.

The independent class-18 arithmetic replay passes in 3.279843 seconds with
empty stderr. Its full parameter set and witness are verified separately
from the still-pending actual group replay.

## Strict boundary control

At weighted class 19 with p=1,q=8 and s=5, choose nonzero Hall directions
U of weight 6 on the first factor and V of weight 13 on the second. The
four actual commutators with each correction absent/present have mixed
tensor difference exactly [U,V], nonzero in weight 19. The recorded
constructor checks all four group expressions and their exact difference;
it passes in 7.092644 seconds. A separate GAP free-associative-algebra
calculation reconstructs the Hall brackets and verifies all 54 nonzero
coefficients in 2.026091 seconds. Both stderr files are empty.

Thus the unqualified linear-tail formula really fails at c-d=10. This is
a scope control, not a counterexample to decidability or to the existence
of some other algorithm in class 19. GAP checks the leading Lie identity;
the four actual group expansions were checked by the rational Python
tensor constructor. These two scopes are not conflated.

## General scope and limits

The proposed theorem is a complete mathematical branch algorithm, not a
full end-to-end implementation over every normalized leading pair and every
ambient rank. The tested weighted groups do not substitute for that proof.
The required leading-pair finiteness, one-dimensional exceptional kernels,
injective successors and exact universal substitutions remain explicit
dependencies on the earlier candidate arguments and credited structural
Lie results. Specialist review is pending for those and this application.

The original frozen nilpotent page, exact N8 fragment and full linked
background were reread, and the actual archived statement image re-viewed.
Part (a) and Roman'kov's free class-two result are kept separate. A targeted
search for free-nilpotent commutator decidability and commutator-equation
algorithms returned the prior class-two material and general equation
undecidability results, not a precise match for this application. This is
not a novelty guarantee; no additional full literature proof was read.
The one-parameter arithmetic theorem is prior and remains explicitly
credited in its separate proof/audit.

No imported Kourovka argument, subagent, push, or external contact. Jobs
reserve one core and 8 GB each; at most two have run concurrently during
this work period. The original 48-hour deadline is unchanged.
