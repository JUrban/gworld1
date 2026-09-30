# G9: a stronger lower bound from complete horizontal families

30 September 2026, approximately 07:21–07:28 UTC, within the original
experiment. This supplements the earlier flow proof and atom certificate.
It does not enumerate any larger ball or larger bridge-word radius.

**Candidate numerical enclosure, standard generators, rank two:**

```
2.668423113 <= lambda_2 <= 2.943737759.
```

The new lower endpoint replaces 2.658596558 from the earlier finite
alphabet. The upper endpoint is the unchanged forbidden-subword
certificate. The exact growth constant, optimality of the bounds, novelty
and independent specialist validation remain unresolved. G9 stays one
partial candidate.

## 1. Horizontal completion of an atom

Retain the [earlier proof's](flow-growth-proof.md) lattice-flow conventions.
Let a,b be the standard generators, with a changing the height and b the
horizontal coordinate. A bridge has strictly positive height after its
initial vertex, and ends at its maximal height H>0. It is an atom when
no internal level h, 1<=h<H, has just one nonzero vertical edge based at
that level. This is a property of its net flow, not of visits in a
particular path. The earlier proof shows that any set of distinct atoms,
of arbitrary positive heights, freely generates a monoid by concatenation.

If w is a bridge representative of an atom, then w b^k is still a
bridge representative of an atom for every integer k. All added steps
are horizontal at its terminal height H; the vertical edges and their
coefficients are unchanged. Its endpoint (H,y+k) distinguishes different
k. Thus even a single certified atom supplies an infinite family.

For an atom flow, retain H and delete only the horizontal edges at height
H. Call the resulting pair its core. **Two atom elements have the same
core if and only if they differ by right multiplication by a power of b.**
One implication follows from the preceding paragraph. Conversely, flows
with the same core differ by a finitely supported flow on the single
horizontal integer line at height H. If their endpoints are (H,y) and
(H,y'), the boundary of this difference is

```
delta_(H,y') - delta_(H,y).
```

On an integer line there is exactly one finitely supported integral flow
with this boundary: the directed segment from y to y'. Indeed, the
difference of two such flows would be a finitely supported circulation
on a tree, hence zero. The flow difference is therefore precisely the
suffix b^(y'-y). Faithfulness of the classical metabelian flow model
gives the asserted equality of group elements.

Consequently grouping a finite atom certificate by cores removes every
overlap among these infinite horizontal families. It does not assume that
the original atoms represented different right cosets.

## 2. Exact rational costs for an entire family

For one core, let the retained representatives end at integer coordinates
y_j and have word costs l_j. They need not be globally geodesic. At each
integer y choose a retained representative followed by a horizontal suffix,
with the least available cost

```
f(y) = min_j (l_j + |y-y_j|).
```

This constructs exactly one atom element at each endpoint y, with a
specific valid representative of cost f(y). Different choices achieving
the minimum represent the same element by the core criterion.

Put L=min_j y_j and U=max_j y_j. For k>=1,

```
f(L-k)=f(L)+k,             f(U+k)=f(U)+k.
```

The complete cost generating function for this family is therefore

```
sum_(y=L)^U z^f(y)
  + (z^(f(L)+1) + z^(f(U)+1))/(1-z).                 (1)
```

The two tails are disjoint from the central interval and from one
another, including when L=U. Distinct cores give disjoint families.
Thus summing (1) over the finitely many cores gives an exact rational
generating function F(z) for a specified infinite alphabet of distinct
atoms, with the chosen costs. It is not the group's growth series.
Each original certified atom occurs in this alphabet with cost no greater
than its original cost.

## 3. Why the infinite alphabet gives a growth bound

All coefficients of F are nonnegative, F(0)=0, F is strictly increasing
on (0,1), and its positive geometric tails imply F(z) tends to infinity
as z tends to 1 from below. There is a unique R in (0,1) with F(R)=1.

Every finite subalphabet consists of distinct atoms and hence generates
a free monoid. The earlier weighted-alphabet argument bounds lambda_2
below by the reciprocal of that finite alphabet's positive generating
function root. Exhaust the infinite alphabet by increasing finite subsets.
Their roots decrease to R: for any z>R, F(z)>1, so some finite partial
sum already exceeds 1 at z. Taking limits proves

```
lambda_2 >= 1/R.                                      (2)
```

This argument requires neither global geodesicity nor a count of every
atom of a given length. It uses actual representatives, distinctness
and free concatenation. The infinite-tail assertion follows from (1),
not from a finite sample of suffix powers.

## 4. The retained certificate and new endpoint

Start with exactly the existing 21,483 atoms whose bridge representatives
have length at most 14. They fall into **8,881 distinct cores**. Write

```
P(z) = z + 2z^2 + 2z^3 + 2z^4 + 2z^5 + 6z^6
       + 26z^7 + 71z^8 + 162z^9 + 341z^10
       + 779z^11 + 1961z^12 + 5098z^13 + 13030z^14.
```

The independently checked completed alphabet has

```
F(z) = P(z) + 551z^15 + 89z^16 + 17762z^15/(1-z).       (3)
```

Here 17,762 is twice the number of cores. All tail starting costs happen
to be 15 for this certificate. The central interval choices add 551
atoms of cost 15 and 89 of cost 16; the coefficients through degree 14
agree with the original certificate. The full per-core data, not just
these aggregates, are retained.

Exact rational arithmetic establishes

```
F(1000000000/2668423113) >= 1,
F(1000000000/2668423114) < 1.
```

By monotonicity, 1/R lies in
[2.668423113,2.668423114). Only the lower endpoint is a lower bound for
lambda_2. **2.668423114 is an upper bound for this alphabet's root,
not an upper bound for the group growth constant.** The group upper
bound 2.943737759 retains its separate older proof and certificate.

The polynomial obtained by multiplying F(z)-1 by 1-z has integer
coefficients and degree 17; the retained certificate records the exact
signed integer evaluations after clearing denominators. No floating-point
root or spectral calculation supplies a premise of the bound.

## 5. Computation, audit and limits

The [Python construction](../../scripts/certify_g9_horizontal_completion.py)
recomputes every original atom flow, forms the cores, and records all
input indices, endpoints, costs, chosen representatives and tail starts.
It checks 57,647 actual central/suffix representatives and the exact
polynomial inequalities. Its run passed in 5.787 seconds.

The [separate GAP checker](../../scripts/check_g9_horizontal_completion.g)
reconstructs the integer flows directly from the original signed words.
It checks that the core groups partition all 21,483 inputs, that their
8,881 cores are pairwise distinct, and that all 21,483 claimed right-power
equalities hold as complete flows. It separately verifies 22,123 central
atom representatives, 35,524 suffix controls, all cost envelopes and all
coefficients of (3), and recomputes the rational inequalities. The original
input words also retain their earlier native Laurent-polynomial Magnus
verification; that older check was not rerun or expanded here.

The first GAP invocation failed on a record-construction syntax error
before any mathematical check. It returned zero but emitted an error and
no success marker, so the process wrapper rejected it. Its exact source
and logs are preserved. Correcting the record field assignments, without
changing any mathematical input or expected output, gave a full pass in
5.137 seconds with empty stderr. The two successful jobs and the failed
invocation were sequential, each one CPU and a 6 GB per-process limit.

The [certificate directory](../../research/certificates/G9-horizontal-completion-v1/)
contains the complete finite description of the infinite alphabet,
GAP input, source snapshot and hash manifest. Replay the Python script
with a fresh `--output` directory through `scripts/run_recorded.py`, then
run the GAP checker after its export is complete. If using a new output
directory, adjust the checker's second input path; its first input is
the unchanged original atom fixture. No genuinely infinite file or
unbounded enumeration is needed.

The general flow-unfolding proof and its free-solvable extension were
reread during this work. In particular, the disjoint upper-height edge
bands, recovery from boundaries, left translations in a nonabelian deck
group, and explicit radius-selection estimate were checked again. No new
gap was identified, but this remains a same-agent audit. The new horizontal
completion is asserted here only for the rank-two lattice model; it is
not silently transferred to a nonabelian deck graph.

The full archived GroupWorld growth page, exact G9 fragment and its
background paragraph were reread, and the retained statement rendering
was actually viewed. Prior flow, unfolding and growth work keeps the
credits and limitations in the [original audit](flow-growth-audit.md).
A targeted search for the new decimal and free-metabelian lower bounds
did not find a matching result; this is not evidence of optimality or
an exhaustive novelty determination. No new source theorem, Kourovka
transfer, external reviewer or additional problem count is claimed.
