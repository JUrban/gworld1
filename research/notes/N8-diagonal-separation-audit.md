# N8 diagonal separation: finite audit, general scope not yet adopted

29 September 2026, 18:05--18:16 UTC. The general argument is in
`N8-diagonal-separation-lead.md`. Current adopted scope remains the
three-exception/class26 partial result. This audit adds independent
evidence for the proposed separating functional; it is not specialist
validation or a novelty conclusion.

## Complete Lie spaces

Python/FLINT and GAP independently construct all free Lie spaces with
E-letter count m=1,...,4 and E-index sum k=0,...,10. They solve
delta V=[E_0,D] and compute the complete image of [E_0,V] on the
hyperplane x_last=x_first, sum x_i=0. Every one of the 44 dimension
vectors agrees. The largest compatible space has dimension 13;
the restriction has rank 13 there. The sole kernel is D=E_0,V=0.
Both implementations use Lyndon bases, but distinct algebra and linear
algebra implementations: sparse Python tensors/FLINT versus GAP's
native free associative algebra, recursive differentiation, rational
vector spaces and polynomial substitution.

These finite ranks neither prove the polynomial lemma for all m,k nor
establish a group decision algorithm. The averaging proof in the lead
supplies the proposed general lemma. The GAP script's final zero check
is only a trivial representation control, not additional mathematical
coverage or a non-Lie counterexample.

## Actual group with a nonzero later obstruction

Let a,e have weights 1,4, let E_i=ad_a^i(e), and use class 17. Put

    D=E_6,
    F=2[e,E_3]+3[E_1,E_2],
    V_F=2[e,[e,E_2]]-[E_1,[e,E_1]].

Exact tensor arithmetic verifies [a,V_F]=[e,F]. For
h(z)=(1-exp(-z))/z, set Z=D+F and Y=h(ad_a)^(-1)Z.
The rational coefficients used for h^(-1) through degree seven are

    1, 1/2, 1/12, 0, -1/720, 0, 1/30240, 0.

Collecting exp(Y) into Hall group coordinates gives denominator lcm
120960. Since Y starts in weight 10, all products of two such tails
have weight above 17; multiplying Y by that integer therefore gives
an actual integral group element. The base pair is

    x=exp(a),       y=exp(120960 Y).

The constructor checks integrality and
log[x,y]=120960[a,Z] exactly. A fixed integral correction vector then
plants a positive target. All first-factor coordinates from weights
4 through 6 and second-factor coordinates from 13 through 15 are
retained in the block; no selected-direction restriction replaces
the full integer system.

The group has Hirsch length 59. Its complete earlier block matrix is
24 by 22 with integer kernel rank two. The adapted first-parameter
steps are 2 and 1; the step 2 is retained. The last correction matrix
has 11 columns, rank 11, and no kernel. For B the later column and
q2 the first quadratic coefficient, the ranks are

    rank A = 11,
    rank [A,B] = 12,
    rank [A,B,q2] = 13.

Thus B is nonzero in the group cokernel and cannot absorb q2. This
addresses a case missing from the earlier actual group fixtures,
where the later-column cokernel rank was zero. It does not assert
that an absorbed branch exists: this example separates the columns.

Native GAP/nq constructs the actual weighted group from the retained
Hall commutators and boundary relations, checks its torsion-free
Hirsch rank, reconstructs every one of the 22 block columns and all
11 final columns at two parameter values, checks two joint block
controls, and verifies the complete integer lattice using an integral
unimodular Hermite certificate. It computes both obstruction ranks
independently and checks two full group witnesses. It reconstructs
the base from supplied integral Hall exponents; it does not independently
verify the explanatory h^(-1) formula for those exponents.

The seven native group parameter values determine all six coefficients
of a polynomial in T,S of total degree at most two: the exact evaluation
matrix on 1,T,S,T^2,TS,S^2 has rank six. The degree bound follows from
the first increment weights 4 and 13. Three increments require weight
at least d+3t=20, and two increments from the first factor together
with the second leading term require 2*4+10=18, both above class 17.
The corresponding second-factor bounds are larger. Hence this replay
checks the entire polynomial identity, including vanishing mixed and
S-squared coefficients, rather than only arbitrary numerical samples.

Separate existing GAP arithmetic and family verifiers reconstruct the
complete constant-matrix integer fibers and the finite first-parameter
root decisions for this new input. The general all-rank branch algorithm
is still not implemented end to end.

## Process evidence and failures

All jobs used the recorded wrapper and are terminal. Maximum concurrent
reservation was two CPU cores and 8 GB; other jobs were sequential.

| Run | Result | Seconds |
|---|---|---:|
| n8-diagonal-quadratic-v1 | Pass | 0.972 |
| n8-diagonal-quadratic-gap-v1 | Pass | 5.990 |
| n8-nonzero-column-block-v1 | Failed: source did not exist | 0.036 |
| n8-nonzero-column-block-v2 | Failed: obsolete required CLI option | 0.420 |
| n8-nonzero-column-block-v3 | Pass | 3.380 |
| n8-nonzero-column-block-gap-v1 | Pass | 2.677 |
| n8-nonzero-column-families-gap-v1 | Pass | 2.022 |
| n8-nonzero-column-arithmetic-gap-v1 | Pass | 2.076 |
| n8-diagonal-evidence-audit-v1 | Pass | 0.119 |

The first source-generation command used unavailable `python` instead
of `python3`; the subsequent recorded invocation therefore had no
source file to execute. The second run stopped in argument parsing
before mathematics; its exact executed source is archived in that
run directory. All successful runs have empty stderr. Failures are
retained, not reclassified as mathematical passes.

## Scope and remaining checks

The new group example still has leading D with one E letter and no
nonzero lower first-factor component to normalize. The complete Lie
space tests cover up to four E letters, but do not by themselves test
those two further steps in actual group coordinates. The written
normalization, highest-letter projection and block induction need
another adversarial read, together with the inherited leading-pair
enumeration and universal tail. No new literature novelty determination
was made in this checkpoint. Counts remain 8 whole candidates,
2 partial candidates, and 0 established novel results. No push,
contacts, subagents, parent-repository edits or clock changes occurred.
