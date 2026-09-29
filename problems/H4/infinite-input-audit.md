# H4 infinite-input extension: internal audit

29 September 2026, approximately 00:28--00:34 UTC. Same-agent mathematical
review with independent GAP computations; no external specialist review.
This strengthens the existing H4 candidate and adds no candidate count.

## Scope and proof review

Re-read the full frozen hyperbolic-groups page and H4 fragment, and viewed
the existing original-statement screenshot. No finite, torsion-free,
non-elementary or fixed-generator restriction appears in the question.
The new argument covers infinite non-elementary virtually free inputs
as well as the previous finite inputs. It still allows torsion and uses
explicit output words. The clock and frozen source bytes are unchanged.

The following potential mistakes were checked separately:

- A minimal representative is minimized over its entire conjugacy class,
  not just over words representing a fixed element. This justifies
  shortening a segment crossing the seam of a power of the word.
- The shortening segment has length at most L. Assuming the representative
  has length at least L makes it fit inside a single cyclic rotation.
  The argument does not require the segment to lie within a fixed copy.
- Identity contributes one class, represented by the empty word. Both
  the word count and the orbit formula include it. The no-relator case
  cannot produce the nontrivial finite-order subgroup in this family.
- Distinct powers of x need not be nonconjugate: count their complete
  doubling orbits. The bound is M/Q, not M. The finite group model and
  its exact order were proved and checked in the original candidate.
- Passing to the free product preserves conjugacy between elements of
  the finite factor. An arbitrary embedding would not justify this.
- The explicitly described free kernel has finite index |K_n| and
  rank |K_n|. Its rank is at least six, excluding virtually cyclic groups.
- The original acyclicity argument for a finite group's irreducible-word
  automaton is not applied to the infinite groups. The new bound concerns
  torsion conjugacy classes only.
- The bound m log_2(2m)>2^n-n-1 holds for every allowed output generating
  set. Its exponential consequence in n remains superpolynomial in the
  O(n log n) input bit length. No P versus NP hypothesis is needed.

No gap was found in this internal check. Novelty remains unverified.

## Primary source and credit

Archived Michael Batty, after Panagiotis Papasoglu, *Notes On Hyperbolic
and Automatic Groups*, dated 21 October 2003, from
https://www.math.ucdavis.edu/~kapovich/280-2020/hyplectures_papasoglu.pdf.
Read Theorem 3.27 and its complete proof, and viewed p.29 as
`research/statement-audits/H4/torsion-conjugacy-theorem.png`.
The short-representative lemma is precisely prior material. The remaining
notes were not audited. The archived file name uses Papasoglu as a source
key; both names are credited in the proof and here.

Bounded searches for `Dehn presentation torsion element conjugate length
relator half`, `hyperbolic group polynomial Dehn presentation output finite
torsion conjugacy classes`, `Dehn presentation virtually free polynomial`,
and `Dehn presentation torsion size lower bound` found the classical lemma
and related hyperbolicity-certification work, but no matching complete
conversion lower bound. This is not an exhaustive novelty determination.
The original finite-group strategy's 2012 attribution remains in
`audit.md`. No Kourovka mathematical result or code was imported.

## New bounded checks

`h4-torsion-classes-v1` passed in 2.878 seconds with empty stderr,
one core and a 4 GB per-process limit. It checks:

- Eight exact integer Burnside sums, n=1,...,8, against the divisor
  formula, with input sizes and the strict logarithmic lower bound.
- Four complete doubling-orbit partitions, n=1,...,4, on sets of sizes
  3,15,255,65535. Their class counts are 2,5,35,4115 respectively.
  These are counts of classes inside the normal cyclic subgroup,
  not counts of all classes in K_n.

`h4-torsion-classes-gap-v1` passed in 2.176 seconds with empty stderr,
one core and a 4 GB per-process limit. GAP independently constructs the
finite affine permutation groups and their full conjugacy classes for
n=1,2,3. It checks that the classes lying in <x> form the advertised
partitions, and verifies every exported representative. Their total
group class counts are 3,9,48; the normal cyclic counts are 2,5,35.
It also verifies the conjugate-powers control x~x^2.

For n=1,2 GAP starts with the original input relators plus the free
generator z, constructs the retraction to K_n, and computes a presentation
of its kernel. Simplification yields respectively 6 and 60 generators
with no relators. This independently checks two finite-index free-kernel
presentations. It is not a computational proof of the general free-product
normal form or the all-n theorem.

Both jobs succeeded on their first runs. Earlier H4 jobs, including their
recorded warning-bearing first GAP run, are retained unchanged. The new
data, exact checker sources and run records are hashed in
`research/certificates/H4-torsion-classes/artifact-hashes.json`.
