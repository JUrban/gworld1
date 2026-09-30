# B9: the four-strand permutation pattern does not extend by itself

30 September 2026, within the original 48-hour window. This records a
failed proof shortcut and exact obstructions for four explicit pairs.
It gives no additional four-strand special braid and does not change
the partial status of B9.

The [four-strand reduction](../../problems/B9/four-strand-underlying-reduction.md)
shows that if special u,v satisfy m(v)=4 and

    A=I1(u) S(I1(v)) in B3,

then pi(A)=1, epsilon(v)=2 and epsilon(u)=3. Here
I1(x)=x s1 S(x)^-1, and permutations are composed rightmost first.
The proposed shortcut was to extend the pure-permutation and
one-step exponent pattern to arbitrary underlying strand numbers
using the same permutation restrictions. Those restrictions alone
do not suffice, already at m(v)=5.

## 1. Complete necessary permutation sets and finite scope

Define upper bounds P(n,p) for permutations of special braids in B_n
of exponent p. Start with P(1,0)={1}. For n>=2 put

    P(n,0)={1},
    P(n,1)=J1(union_p P(n-1,p)),
    P(n,p)=Jp(S_(n-1)) for 2<=p<=n-1,

and retain only permutations f with nu(f)=p and f^-1(1) in {1,2}.
Here Jp is the permutation map of I_p, and
nu(f)=#{j: f(j+1)=j}. The containment follows from the credited
right-branch representation, strand-support lemma and special
permutation restrictions. Equality with the actual special permutation
image is not asserted beyond the previously proved small cases.

The last filter is necessary: Jp of arbitrary permutations need not
satisfy the special small-class condition. The first exploratory
implementation incorrectly asserted that it did; that failure is
retained. Specialness of the parameter H is not available for p>=2.

For g in P(q), c=J1(g), and an even a in S3, let

    b=a S(c)^-1.

The equation J1(f)=b is equivalent to f s1=b S(f), and implies

    f(2)=b(1),  f(1)=b(f(1)+1),
    f(i)=b(f(i-1)+1) for i>=3.

Enumerating f(1) and reconstructing the remaining positions therefore
finds every solution. The implementation rejects values outside
{1,...,q+1}, checks that the tuple is a permutation, verifies the full
original equation, and requires f in P(q+1). No incomplete recurrence
is accepted on its own.

The [Python inventory](../../scripts/probe_b9_general_permutations.py)
gives the following finite counts. The independently written
[GAP checker](../../scripts/check_b9_general_permutations.g) instead
enumerates every pair in the two necessary sets, reproducing the
rows through q=6 without using the recurrence or Python output.

| q | size P(q) | size P(q+1) | pairs with even pi(A) supported in S3 |
|---|---:|---:|---:|
| 3 | 4 | 9 | 5 |
| 4 | 9 | 24 | 6 |
| 5 | 24 | 83 | 8 |
| 6 | 83 | 376 | 16 |
| 7 | 376 | 2131 | 46 |

These sets allow braids on fewer than q or q+1 strands. Fixed final
positions do not determine the minimum strand number of a braid.
The rows are therefore necessary permutation cases, not counts of
solutions of a braid equation. The q=7 row has only the Python check.
No universal conclusion is extrapolated from this table.

## 2. An explicit surviving pattern with actual special lifts

For q=5 the necessary sets contain

    g=(1,4,5,3,2),        f=(1,2,5,6,4,3).

They satisfy

    nu(g)=nu(f)=1,
    J1(f) S(J1(g))=(2,3,1,4,5,6,7).

Thus the parameter permutation is supported on three positions but
is not pure, and the underlying exponents are equal. Both inputs
move their last positions. This is not merely a pair in an upper
bound with unknown special lifts. Define explicit special terms

    s=1 triangle 1,
    z=s triangle 1,
    w=z triangle 1,
    v=w triangle 1,
    u=(1 triangle w) triangle 1.

Their permutations are exactly g and f, respectively; their written
words use only generators through s4 and s5. The moved last positions
therefore prove m(v)=5 and m(u)=6. Both have exponent one by their
outer operation with right argument 1.

However, A=I1(u) S(I1(v)) is not in B3. In the seven-dimensional
unreduced Burau representation at -1, with generator block
[[2,-1],[1,0]], its last row is

    (0,19792,9720274,-13909026,2550488,1668004,-49531).

Every standard B6 braid has last row e7. This row therefore excludes
B6, while the displayed construction uses only generators through
s6. Consequently m(A)=7. Faithfulness of Burau is not needed for
this obstruction.

Three further first-input lifts were found by applying I1 to the
already retained 52-word height-four fixture. With the same v, they
have the same permutation pair, minimum strands (6,5), and parameters
of minimum strand number seven. Their exact words and last rows are
in [lifts-v3.json](../certificates/B9-general-permutations/lifts-v3.json).
The [GAP matrix check](../../scripts/check_b9_general_permutation_lifts.g)
reconstructs all four matrices natively. It also verifies the short
special term above against the fixture using literal free-word
cancellation, independently of the Python code. The other fixture
words retain their previously checked specialness certificates.

This demonstrates the limitation of the permutation-only shortcut.
It **does not** disprove the possible stronger statement that actual
membership A in B3 forces purity for all strand numbers. None of
these four pairs satisfies that membership hypothesis. A proof of
such a statement would need additional braid information.

## 3. Runs, failures and provenance

All nine jobs were sequential, each with one CPU, a 2 GB per-process
cap and a 60-second limit. The complete input versions, outputs and
terminal process records are bound by the
[manifest](../certificates/B9-general-permutations/manifest-v1.json).

- General inventory v1 failed on the incorrect automatic small-class
  assertion for arbitrary Jp images. Filtering by the necessary
  special conditions repairs the upper bound.
- Inventory v2 and v3 failed when the recurrence left the allowed
  range. Version 3 additionally made the nu filter explicit; it did
  not fix that programming error. Version 4 rejects out-of-range
  recurrences and passed in 0.270 seconds.
- The lift check v1 required witnesses in an unnecessarily narrow
  family of twice-applied I1 on known B4 words. That assertion failed.
  Version 2 used the existing full 52-word fixture and found four
  first-input lifts, but direct faithful Artin actions failed with
  MemoryError under the 2 GB address-space cap after 19.835 seconds. No action certificate
  or successful result is claimed for that run.
- Lift v3 uses the sufficient matrix obstruction above and passed
  in 0.122 seconds. The independent GAP permutation and matrix jobs
  passed in 2.277 and 1.825 seconds, respectively. Successful jobs
  had empty stderr; failed sources and errors are retained.

The full archived GroupWorld braid page and exact B9 fragment were
reread, and the retained statement rendering was actually viewed.
Dehornoy's small-class proposition and its proof were reread in the
retained text, and the [primary PDF](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf)
was reopened online. Other structural attributions are the ones
already documented in the small-strand proof. No new primary-page
rendering, novelty determination, external review, or Kourovka
transfer is asserted. The candidate tally and deadline are unchanged.
