# N8 fourteen-layer audit

29 September 2026. **Audit in progress; upper-bound group replay pending.**
The argument is in `fourteen-layer-proof.md`. General N8(b), specialist
validation and novelty remain unresolved. The all-rank branch algorithm
is not implemented end to end.

## Statement and proof scope

The full frozen `sources/raw/probnil.html`, the exact N8 fragment and the
linked N8 background were reread, and the actual archived paragraph image
was viewed. Part (a) is starred and has Roman'kov's prior negative answer;
the prior free class-two result is also explicitly excluded from novelty.
The new proposal concerns part (b), all targets with c-d<=13. Combined
with the existing leading-degree<=10 theorem, it would cover class<=24.
It remains the same partial entry, not a whole-entry solution.

The additional proof obligations are addressed as follows:

- The t=3 block can contain exceptions only at 3 and 5. In the unbounded
  elimination case, the injective offset 6 admits a polynomial lift on
  each retained integrality residue. All future coordinates start at 7,
  where their products exceed the claimed class bound.
- The t=4 block can contain at most one further exception, at 6 or 7.
  After elimination, every coordinate at 8 and above stays free. There
  is no assumption that offset 8 is injective or universal.
- Fixing the earlier parameter allows a restart with only lower
  coordinates fixed. This can duplicate or enlarge intermediate families,
  but every accepted result must solve the entire original equation, and
  every solution in the former family remains available.
- Quotienting a block uses only kernels in that block, so the prior
  two-exception construction does not assert an absence of later kernels.
  Integer steps, torsion cosets and all congruence residues are retained.
- Nonlinear parameter exponents require the new degree bound
  floor(c*rho), rho=max(deg(f_i)/weight(h_i)). The older linear-exponent
  bound is not reused. This follows from finite weighted products and
  inverses; collection in the comparison tail is linear.

The finite tests below support these reductions. They do not prove the
earlier all-rank leading-pair enumeration, free-Lie kernel lemmas or the
general branch argument. Those remain explicit structural dependencies.

## Complete three-exception Lie range

Use the free Lie algebra on generators of weights (1,4,5), with C=a and
D=ad_a^6(e), of weights (p,q)=(1,10). The extra weight-five generator is
included in every homogeneous domain, not discarded as unused support.
Python enumerates complete Lyndon bases and performs exact elimination;
GAP independently builds its own words, bases and rational spans.

For offsets 1 through 8 the kernel dimensions are

    0, 0, 1, 0, 1, 0, 1, 0.

All three explicit kernel identities pass. Runs
`n8-three-exception-range-v1` and `n8-three-exception-range-gap-v1`
take 0.169944 and 2.277939 seconds. These are eight complete finite
homogeneous calculations, not a proof for all ranks and weights.

## Actual nonlinear polynomial group families

Use weighted generators of weights (1,4), leading weights (p,q)=(1,10),
and the actual base pair (a^2,h_D^3). Here h_D is the right-nested Hall
word [e,a,a,a,a,a,a], whose leading Lie term is ad_a^6(e).
Insert the complete primitive offset-3 kernel with exponent T and the
complete primitive offset-5 kernel with exponent T^2. Retain every later
correction on both factors from offset 7 onward, including the third
exception at 7 and all later kernel directions.

This is deliberately an **arbitrary polynomial family**, not an example
of an unbounded normalized B!=0 elimination branch. All early compatibility
rows remain in the final system; they can and do restrict T. The previous
failed perturbation is not used as positive evidence for such a branch.

The target is formed at T=2 with a deterministic simultaneous tail
correction j mod 3 minus one. A second joint control uses 2 minus j mod 5.
There is no random sampling or bounded search over the parameter.
Here rho=1/3. The proved bound is seven in class 21 and eight in class 24.

The class-21 constructor gives a 150-by-93 matrix in a group with 171
Hall generators. A zero row has residual 12-6T, so T=2 is the complete
parameter candidate set. At T=2 the integer matrix has rank 92 and a
one-dimensional complete integer kernel. The reconstructed pair solves
the full original commutator equation. Its final constructor run is
`n8-polynomial-group-tail-c21-v2`, 69.347022 seconds.

The independent GAP replay constructs a native NQ quotient from compact
Hall relators. It checks Hirsch length, torsion-freeness, boundary relations,
both group witnesses, full homogeneous kernels, axes/row completeness,
and the proved interpolation bound. Every polynomial column is compared
against exact group commutator identities at all required samples. The
two joint controls retain every conjugation and mixed commutator. Native
polynomial factorization gives the complete integer candidate set; native
integer solving checks it, and a unimodular Hermite certificate proves
completeness of the entire remaining integer kernel.

Class-21 run `n8-polynomial-group-tail-gap-c21-v3` passes in 27.664682
seconds: 744 polynomial columns, 16 joint controls, two direct identity
controls, three complete homogeneous kernels, one complete finite
decision, one complete integer fiber and two actual group witnesses.

The output rows include every Hall coordinate from weight 14 onward,
including the early compatibility equations below the tail's first
possible change at weight 18. Thus the deliberately unnormalized test
family does not hide those restrictions by dropping zero rows of P.

Class-24 construction and independent replay are pending. The final audit
will state their terminal results before adopting any scope change.

## Strict upper boundary of this linear-tail reduction

In the same weighted alphabet take x=a, y=[a,[a,...,[a,e]...]] with six
copies of a, and corrections u,v with four and thirteen copies respectively.
Their leading weights are 8 and 17. At c=25, d=11, s=7, compute all four
actual group commutators in exact truncated rational tensor coordinates.
The mixed difference is exactly

    [ad_a^4(e), ad_a^13(e)] != 0,

with 115 nonzero coefficients, all of weight 25. It vanishes after
truncation to 24. Python's four full group calculations pass in 6.542955
seconds; the independent GAP leading-Lie reconstruction passes in
2.126290 seconds. GAP here checks the leading bracket, not all four group
products. Thus 2s>n cannot simply be weakened to equality. This does not
prove undecidability, or rule out other methods, in class 25 or beyond.

## Retained failures and representation changes

- Class-21 constructor v1 reached two samples but hit its 600-second
  limit (600.014920 seconds). Its source is retained. Version v2 skips
  impossible tensor weight products and builds only combinatorial Hall
  descriptions beyond the truncation degree; the equations are unchanged.
- Class-21 GAP v1 fails in NQ construction with `Exponent too large`
  (3.781286 seconds). Declaring the heavier generator first changes the
  elimination order and allows the same presented group to be constructed.
  No NQ package source or overflow threshold was modified.
- GAP v2 then rejects the checker's initial base-word comparison
  (18.432811 seconds). It had compared the Hall group word with a different
  nesting that has the same leading Lie term. Correcting that comparison
  gives v3. Both failed verifier sources and raw logs are retained.
- Class-24 constructor v1 was intentionally interrupted after four
  successful samples (406.165739 seconds). Repeated stack traces locate
  the bottleneck in ordinary Hall collection of a square-zero tail.
  Its executed constructor is retained. The replacement uses exact
  linear subtraction in that tail, justified by twice its minimum weight
  exceeding c; it does not change the sample count or equations.
- Class-24 constructor v2 completes all nine group samples and reaches
  its second Hermite certificate, but times out in the subsequent SymPy
  rational-rank calculation (600.047013 seconds). Its executed source
  is retained. Version v3 uses FLINT integer rank, caches identical
  coordinate conversions, and saves the polynomial input before the
  arithmetic stage. Its run is still pending at this checkpoint.

All completed successful runs listed above have empty stderr. Diagnostic
stack dumps in the interrupted class-24 run are preserved separately;
their periodic 'Timeout' labels are diagnostic alarms, not runner timeouts.
Resource reservations stayed well below 20 cores and 100 GB. All work
is local; nothing was pushed and no external contact was made.

## Reproduction and provenance

Constructors and independent verifiers are:

    scripts/check_n8_three_exception_range.py
    scripts/check_n8_three_exception_range_gap.g
    scripts/check_n8_polynomial_group_tail.py
    scripts/check_n8_polynomial_group_tail_gap.g
    scripts/check_n8_polynomial_tail_boundary.py
    scripts/check_n8_polynomial_tail_boundary_gap.g

Each recorded run's `process.json` gives its exact invocation, limits,
timestamps, return status and log hashes. Constructor/checker revisions
superseded during this audit are saved beside their run logs. The final
hash manifest will bind the current proof, fixtures, dependencies, source
snapshots and terminal run records. Earlier manifests remain historical.
