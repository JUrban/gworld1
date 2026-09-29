# B9 infinite-family audit

29 September2026. Structural family discovered approximately20:27--20:28
UTC from the earlier finite counterexample; exact symbolic check completed
20:28:23, independent GAP replay20:31:07. Candidate proof:
[infinite-family-proof.md](infinite-family-proof.md). All work is inside
the original48-hour run. No Kourovka argument or code is imported.

## Source and mathematical scope

The complete frozen `sources/raw/probBr.html` and the exact B9 fragment
were reread. Its actual archived screenshot was viewed again, as was
Dehornoy's actual printed survey page13. Both use the closure of1 under
a▷b=a S(b) s1 S(a)^-1. The source asks for the number in every B_N.

The candidate gives the exact infinite cardinality for **all N>=5**.
It does not establish all small-N counts, so this changes B9 from an
uncounted related height result to one counted partial candidate. It
does not increase the whole-entry count. The older statements that no
fixed-strand infinite family had been obtained are historical checkpoints.

Patrick Dehornoy, [*The Braid Shelf*, arXiv1711.09794v2](https://arxiv.org/abs/1711.09794v2),
Section3.2, Definition3.9 and Question3.19, supplies the exact terminology
and related height question. The primary PDF is archived as
`literature/raw/B9-Dehornoy-1711.09794.pdf`; the printed page is
`literature/figures/B9-Dehornoy-page13.png`. The proof above uses the
definition and elementary Artin relations; it does not import the
survey's difficult freeness or braid-ordering results. The survey's
indexing and printed numerical-bound issues were previously recorded;
this infinite family does not depend on resolving those issues.

The older author copy [*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf)
was also archived. Section1.3, including Lemma1.9 and Question1.12, and
the end of Section5.3 were read. The same height question appears there;
its displayed small extended-braid examples are explicitly not an
exhaustion theorem. No small-B_N classification is imported from them.
The full32-page paper was not audited.

## Internal proof audit

- The recurrence u_(n+1)=u_n▷u_(n-1) starts with u0=1,u1=s1. This
  proves specialness at every n without assuming the shorter words special.
- The induction u_n S(u_(n-1))=s1^n is exact. Expanding it three times
  puts the inverse shifted tail before s2^(1-n); those factors commute
  because the tail starts at generator4. This yields equation(4).
- The expansion of v_n includes both s2^2 and s3^-1. In the final shelf
  product its fourth shifted tail moves past s2 s1 only; it is not moved
  past s3 or s4. Its support starts at5, so the stated commutations hold.
- The order in the final inverse is
  S^4(q_n)^-1 S(u_n)^-1=(S(u_n) S^4(q_n))^-1. Reversing that order
  would be an error; the proof retains the correct order.
- The two tail cancellations leave a word on generators1 through4 for
  all n>=3. There is no extrapolation from the earlier n=5 example.
- Burau at-1 is used only to distinguish braids. Its unipotent generator
  formula is valid for negative exponents. The handwritten fifth-row
  calculation agrees with two independent exact polynomial implementations.
- The entry n(n-1) proves all parameters distinct and excludes standard
  B4 membership. A finite-modulus matrix alone would not give this
  infinitude argument; here the coefficients are unbounded integers.
- B_N is countable. Thus a constructed infinite family proves the stated
  exact cardinality for N>=5 without classifying every special braid.

The argument passed this internal audit; independent external review is
still required. No claim of established novelty is made.

## Computation and retained failure

`scripts/probe_b9_parametric_family.py` constructs the exact five-dimensional
matrices over Z[n] using SymPy. It checks the Artin relations and the
square-zero generator increments, multiplies all ten powered blocks, and
saves the full symbolic matrix. It passed in0.67seconds with empty stderr.

`scripts/check_b9_parametric_family.g` independently reconstructs the
same representation over the rational polynomial ring in GAP, verifies
the Artin relations and the universal separating entry, and then uses
faithful free-group Artin actions in rank10 to check:

- seven special recurrence identities, n=2,...,8;
- six complete special-term-to-B5 identities, n=3,...,8;
- exact support in B5 and movement of the fifth generator;
- six negative controls omitting the first s4^-1 factor.

These finite faithful-action checks support the algebraic construction.
The handwritten proof of specialness and cancellation is valid for every
n; finite sampling alone would not justify that universal claim.

The first GAP job stopped at a determinant comparison: the constant
polynomial1 is not equal to the bare rational integer1 in this comparison.
It returned exit0 but produced an error and no success marker, so the
recorded job correctly reports failure. Its exact source is preserved as
`research/certificates/B9-parametric/check-gap-v1-determinant.g`.
Using `One(ring)` fixes the type comparison. The second run prints the
determinant1 and passes all checks in1.98seconds, with empty stderr.

The three recorded jobs are `b9-parametric-symbolic-v1`,
`b9-parametric-gap-v1` and `b9-parametric-gap-v2`. All are terminal;
each used one CPU and at most5GB. They are deterministic with no random
seed or mathematical search cutoff. The faithful-action sample range is
explicitly bounded; the polynomial identity is symbolic.

The GAP verifier has no dependence on Python, CBraid, the earlier1930
images or any downloaded braid package. It can be run directly from its
source; during the active run use the recorded wrapper. The symbolic
generator refuses to overwrite its output directory. Use a fresh output
directory or clean checkout for regeneration.

`research/certificates/B9-parametric/manifest-v1.json` binds the proof,
audit, scripts, symbolic output, failed verifier source, process records
and statement/source evidence. All artifacts are below the repository
blob limit.

## Novelty and remaining work

Targeted primary-source searches on29 September used "special braids"
with "infinitely", "B_5", "finite", "braid shelf" and "3.19".
They returned the same surveys and unrelated meanings of special braid;
no matching infinite family was located. The positive-braid family in
*Unprovability results involving braids* is not the monogenic shelf and
is not used. Failure to find prior work is not proof of novelty.

Remaining mathematical scope: determine the small-strand intersections,
particularly B3 and B4, without inferring their exhaustion from bounded
height tables. Remaining validation: external specialist and novelty
review. The separate N9 and other candidates are unaffected.
