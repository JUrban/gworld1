# N8: checking the full-block non-absorption implication

29 September 2026, approximately 23:10–23:17 UTC. This supplements
[Sections 6–7 of the general proof](general-proof.md). It checks the
universal linear argument following the Lie projection and diagonal
restriction. It is not a formalization of that projection, its
group-coordinate interpretation, or the complete N8 decision procedure.
No candidate scope or count changes.

## The exact implication checked

The formal source is
[Block.lean](../../research/certificates/N8-block-separation-lean/Block.lean).
It works over an arbitrary field K, with arbitrary K-vector spaces M,W.
No finite dimension or bound on the number of later columns is imposed.
For a natural number t, a nonzero scalar b, vectors F_j in W and
linear operators C_jk on W, assume the triangular equations

    b F_j + sum_(k<j) C_jk(F_k) = 0          for every j<t.    (1)

`triangular_vanishes` proves F_j=0 for all j<t, by strong induction.
`later_column_vanishes` then proves that every expression

    sum_(t<i<=2t) D_i(F_(2t-i))                             (2)

vanishes, for arbitrary linear operators D_i. The strict index bound
2t-i<t is part of the checked proof. In particular the endpoint i=2t
uses F_0; it is not silently omitted.

Let phi:M->W be linear, A a correction subspace, and B_s any indexed
family of later columns. Assume A is annihilated by phi, and every
phi(B_s) has form (2). `block_annihilated` proves

    A + span_K{B_s} is contained in ker(phi).                 (3)

If phi(q)=b^2 Q with Q nonzero, `block_quadratic_not_mem` proves

    q is not in A + span_K{B_s}.                             (4)

Thus the conclusion concerns the whole correction span and every
later column simultaneously. It does not merely test the columns
one at a time against q.

Two further theorems prove the finite branching consequence.
`quadratic_three_roots` says that if q!=0 and

    x^2 q + x l + c = 0,

then among any three roots at least two coincide. Its proof subtracts
two equations, cancels the nonzero difference of distinct roots,
then subtracts the resulting linear equations. It applies to a
vector-valued polynomial, without first choosing a scalar functional.
`three_liftable_parameters` gives the same conclusion when the displayed
polynomial need only lie in a subspace S contained in ker(phi), provided
phi(q)!=0. Applying this to (3) gives at most two rational values for
the first parameter; integral solutions are a subset of these.

All six theorem declarations, including their dependencies, pass the
restricted transitive axiom audit.

## Matching the written group argument

Here the field is Q and W is the rational polynomial space produced
by the diagonal restriction R in the fixed E-letter count m+2.
The coefficient of each earlier first-parameter equation is

    b R([E_0,F_j]) + sum_(k<j) C_jk(R([E_0,F_k])) = 0.

Each C_jk is multiplication by the appropriate scalar times a power
of the first positional variable, or the zero map if the degree is
incompatible. **These multipliers are polynomials, not generally
rational scalars.** Accordingly the final Lean theorem uses arbitrary
Q-linear endomorphisms of W as coefficients. Polynomial multiplication
is such an endomorphism. This matches the application without passing
to a fraction field or extending the rational correction space.

In the notation of the general proof, set the formal F_j equal to
R([E_0,F_j]) there. The leading D has at most m E letters, so the
m+1-letter component F_0 is zero. The coefficient b is the nonzero
integer step of the *complete* surviving block lattice, regarded as
a rational number. It need not be one.

Every other parameter begins at an offset i>t. At degree d+2t its
first-factor components can pair only with fixed second-factor
offsets 2t-i<t. The positional identity

    R([E_k,F]) = z_1^k R([E_0,F])

puts each resulting contribution in (2). Its second-factor components
pair either with C, whose adjoint image is killed by R, or with a
fixed first-factor offset below t, which normalization made zero.
The final correction image is A; the quadratic image is b^2 Q,
where Q=R([E_0,V_(m+1)]) is nonzero by the diagonal separation lemma.
Equations (1)–(4) therefore express exactly the induction and span
exclusion used in the written proof.

This matching is an audited written argument, not a Lean instantiation
from the original free group. In particular the six formal theorems
assume the displayed triangular equations and later-column formulas;
they do not certify that an arbitrary input group produces them.

## Rechecked normalization and degree boundaries

The prefix normalization is fixed before the block parameters are
chosen. On the free graded tail L_(>=p), replacing the basis element C
by C plus its fixed higher prefix is a filtered Lie map with identity
associated graded. In a finite truncation its difference from the
identity raises degree, hence is nilpotent as a linear operator.
Its finite geometric-series inverse is a linear inverse; because the
original map is a Lie homomorphism, this inverse also preserves the
bracket. No integral group automorphism is asserted.

The following bounds explain why a full affine integer block remains
affine in the relevant logarithmic coordinates. All variable increments
begin at offset t, and p,q>0.

| Possible nonlinear term | Lowest weight | Required coordinate cutoff |
| --- | --- | --- |
| Two varying first-factor increments in X | 2(p+t) | p+2t |
| Two varying second-factor increments in Y | 2(q+t) | q+2t |
| Two varying X increments in h(ad_X)Y | q+2(p+t) | q+2t |
| One varying X and one varying Y in h(ad_X)Y | p+q+2t | q+2t |

Every left entry strictly exceeds its cutoff. Fixed factors add
positive weight and cannot spoil the inequalities. Nonlinear group
commutator terms with at least two Y occurrences that depend on any
block parameter have weight at least p+2q+t>d+2t; q>p+t suffices.
Their lower surviving terms are fixed and are subtracted, not discarded.

After all equations below degree d+2t hold, the residual begins in
that degree. Logarithm, Hall coordinates and the fixed filtered
normalization have the same associated-graded residual there.
Consequently a nonzero diagonal image gives non-membership in the
actual rational span of the group correction matrix and later columns.
The algorithm can find a scalar annihilating row by rational linear
algebra on those matrices; it does not need to compute the abstract
free-Lie projection itself.

The full block, its integer step b and all integer congruences remain
in the algorithm. The rational proof does not authorize accepting a
rational correction as an integral solution. Restarting after a first
parameter is fixed may revisit unnecessary higher continuations, but
retains every genuine solution and still increases the fixed offset.
These coordinate and recursion assertions remain written proof obligations.

## Why the full compatibility hypothesis matters

An elementary model shows why checking only some earlier equations
would not suffice. Take t=2, W=Q, b=1, all C_jk=0, F_0=0 and F_1=1.
The j=0 equation holds; the j=1 equation fails. The single later term
with i=3 and D_3 the identity is F_1=1, so it can absorb a quadratic
coefficient 1 through T^2+S=0. Restoring the omitted compatibility
equation forces F_1=0 and eliminates that mechanism.

This is a written boundary example, not a claimed actual free-nilpotent
group branch. It illustrates exactly which hypothesis the earlier
unrestricted deformation probes lacked. No finite Lie or group fixture
was repeated or enlarged for this audit.

## Process evidence and limitations

Both jobs used Lean 4.24.0, commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, `--trust=0`, and Mathlib
revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The allowed
transitive axioms are `propext`, `Classical.choice` and `Quot.sound`.
The existing ignored S5 environment supplies infrastructure only.

- `n8-block-separation-lean-v1` failed in 7.79 seconds. A rewrite did
  not unfold membership in the set coercion of a linear-map kernel;
  the axiom audit rejected the resulting `sorryAx`. Its exact source
  and diagnostics are retained. This first version also used scalar
  coefficients, too narrow to directly model the positional multipliers.
- `n8-block-separation-lean-v2` passed all six declarations in 8.15
  seconds, with empty stderr and no warnings. It makes kernel
  membership explicit and generalizes coefficients to linear operators.
  This is the final `Block.lean`.

Both jobs were sequential, reserved one CPU and 8 decimal GB, used
`LEAN_NUM_THREADS=1`, and had a 120-second bound. Both are terminal.
With the pinned tools on PATH, replay under a fresh name:

```sh
python3 scripts/run_recorded.py --name n8-block-separation-lean-replay \
  --cores 1 --memory-gb 8 --timeout 120 \
  --expect 'PASS N8 full-block separation and two-parameter-value bound' \
  -- python3 scripts/check_n8_block_separation_lean.py
```

The [manifest](../../research/certificates/N8-block-separation-lean/manifest-v1.json)
binds this audit, final and failed sources, prior written dependencies
and raw logs. The full N8 algorithm is not implemented or formally
verified by this work. Independent specialist review and novelty remain
pending; the original deadline is unchanged.
