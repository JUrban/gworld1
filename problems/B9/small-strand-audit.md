# B9 small-strand audit

29 September 2026, approximately 20:44--20:54 UTC. This audit supplements
the earlier infinite-family audit; it does not change those hash-bound
historical files. Proof: [small-strand-proof.md](small-strand-proof.md).

## Scope and prior work

The exact original B9 statement and full frozen braid page were previously
read and rendered in this run. No convention has changed: special means
closure of 1 in the monogenic braid shelf, and B_N is the standard subgroup.
This follow-up proves the small counts 1, 2 and 4 as consequences of
Dehornoy's established results. It isolates the unclassified B4 sector
epsilon=2. It does not promote B9 to a whole-entry candidate or assert
novelty for these deductions.

The archived primary *Strange Questions About Braids* was read further:
Section 2.1 on colorings and specialness, Lemma 4.3, and Sections 5.2--5.3,
especially Lemma 5.6 and Propositions 5.8--5.9. The actual printed page 26
was rendered, viewed and saved. The full 32-page paper was not audited.
Its Proposition 5.9 already states the strand/right-power equation; an
initial independent deduction from Lemma 1.9 was therefore not new.

Two indexing slips in printed intermediate formulas are avoided explicitly:
the permutation-set transformation shifts D(g) by one, and the k-th right
power of I_p(A) is I_(p+k-1)(A), including k=1. The printed support proof
also shifts the highest generator index relative to its stated minimal
strand count. The final structural statements used here agree with the
standard strand convention and are supplied with the subgroup-intersection
and direct-expansion arguments in the proof. These are not reasons to
discard the cited propositions.

Targeted searches on special B3/B4 braids again returned the primary
Dehornoy material and the different positive special-braid construction
from ordinal-descent work. A B3-to-SL2(Z) kernel source was located while
exploring a matrix route but is not imported into the final proof. That
route is unnecessary. No current-openness or novelty guarantee follows
from this bounded search.

## Proof checks

- Epsilon is a nonnegative integer on special terms, with zero only at
  the unit. The independent permutation recurrence bounds it by N-1.
- Every exponent-one special term is a▷1 with a special. The support
  lemma forces a into B_(N-1); it concerns the final braid, regardless
  of the original term's height.
- Injectivity of I_1 follows from the exact equality criterion modulo
  B1, not from a nonfaithful matrix representation.
- Maximal exponent N-1 has a unique possible braid tau_(N-1), either
  by the right-power equation with exponent one or by the I_p formula.
- Hence all three possible exponents in B3 are exhausted. This supplies
  the missing justification that finite enumeration alone did not give.
- In B4, exponents zero, one and three are exhausted. Exponent two is
  exactly the special-pair/coset condition in equation (10). The four
  displayed cosets are a lower bound, as in the source, not an exhaustion.
- The necessary root equation is explicitly insufficient: sigma2 is
  a root but is excluded from specialness by the positive-special theorem.
- The new B5 family still supplies countably infinite cardinality for
  N>=5. No part of this follow-up alters its universal cancellation or
  separating-matrix proof.

The consecutive-strand parabolic intersection property and the established
braid-shelf results are mathematical dependencies. The finite checks below
do not replace them. External specialist review remains outstanding.

## Recorded computations and limits

`b9-three-strand-matrix-v1` (one CPU, 3 GB, 0.52 s) passed. The SymPy script
conjugates a general SL2 matrix into the unreduced three-strand Burau
representation at t=-1, embeds it in dimension four, and computes the
necessary square-root equations. Its Groebner basis is

    a-c^2+c-1, b-c+1, d-1.

The family s1^k s2^(1-k) satisfies these equations symbolically. This is
only an exploratory necessary-condition certificate: the script neither
classifies special braids nor supplies braid faithfulness. The final
small-strand proof does not depend on this computation.

`b9-small-strands-gap-v1` failed on a GAP lambda syntax error before any
checks. It returned exit zero, but stderr and the missing success marker
correctly made the recorded result a failure. The exact failed source is
retained as `research/certificates/B9-small-strands/check-gap-v1-syntax.g`.

Replacing the two unsupported two-argument lambda expressions with GAP
functions gave `b9-small-strands-gap-v2`: one CPU, 5 GB, 1.93 s, passed
with empty stderr. The independent faithful free-group action checks:

- all 52 earlier bounded fixtures against the new strand/right-power
  equation and exponent bound;
- distinction of the four B3 braids, four B4 exponent-one braids and
  four B4 exponent-two lower-bound examples;
- the right-square equation for those four exponent-two examples;
- beta_n▷beta_n=tau_4 for the six parameters n=3,...,8 of the infinite
  family;
- fourteen roots s1^k s2^(1-k), k=-5,...,8, and an incorrect-target
  negative control.

The universal statements come from the written proof, not these finite
samples. The jobs are deterministic, all terminal, with no random seed.
No Kourovka code was imported. The new manifest binds sources, proof,
audit, scripts, fixtures and raw process evidence. Older manifests and
their bound files remain unchanged.
