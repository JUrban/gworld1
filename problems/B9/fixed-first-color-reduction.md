# B9: a fixed first color and the four known parameter rays

30 September 2026, within the original experiment. This gives a further
restriction on the unclassified B4 sector. It covers arbitrary parameter
exponent, unlike the previous deductions restricted to total parameter
exponent two. It does not classify all special B4 braids.

Write s=sigma1, t=sigma2, S for the shift, and C for the special braids.
The remaining parameters have the form A=a S(c) in B3, with a,c in C;
the corresponding braid is I2(A), and its value depends precisely on
the right coset A B2. The four known parameter cosets have representatives

```
1,  t,  s t,  z=s^2 t^-1.
```

The [previous parameter reduction](positive-parameter-reduction.md)
proves that every represented coset has one terminal special pair and
all its pairs are forward iterates of T(a,c)=(a triangle c,a).

## 1. Uniqueness of a nontrivial second color

We reuse the earlier rigidity lemma: if b,d are nontrivial special
braids and b^-1 d belongs to B2, then b=d. To recall the proof, write
d=b s^k. For k>0, the unique special decomposition of b s^k is obtained
by applying T^k to (b,1). After the first step both colors are
nontrivial, and remain so; this cannot be the decomposition (d,1).
For k<0 interchange b and d. Thus k=0. The nontriviality assumption
is necessary, since 1 and s are both special.

For an arbitrary braid a, not necessarily special, define

```
R(a) = { c in C : a S(c) belongs to B3 }.
```

**Proposition.** If a belongs to B3 then R(a)={1,s}. If a does not
belong to B3, R(a) is empty or consists of exactly one braid, and
that braid lies outside B2.

**Proof.** If c,d belong to R(a), cancellation of the same first factor
gives

```
S(c^-1 d) = (a S(c))^-1 (a S(d)) in B3.
```

The standard consecutive-parabolic intersection implies c^-1 d in B2.
If c,d are nontrivial, the rigidity lemma makes them equal. If c=1,
then a belongs to B3. More generally, for a in B3 the defining condition
is S(c) in B3, equivalently c in B2, whose special elements are exactly
1 and s. Conversely, if a is outside B3 and a solution c were in B2,
then a=(a S(c)) S(c)^-1 would belong to B3. This proves every case. QED.

The subgroup statement used here is S(B_infinity) intersect B3=S(B2).
It concerns actual braid support, not permutations or matrix support.
It is the same established parabolic-intersection fact used in the
existing small-strand proof.

## 2. All four known families are exhausted

Take the four initial pairs

```
(a_0,c_0) = (1,1), (1,s), (s,s), (z,1).
```

For each such pair define (a_k,c_k)=T^k(a_0,c_0), k>=0, and let
A_0=a_0 S(c_0). The literal identity

```
(a triangle c) S(a) = a S(c) s
```

implies a_k S(c_k)=A_0 s^k for every k. Hence all these pairs remain
in their original one of the four parameter cosets.

**Corollary.** Fix any k in any one of these four families. For every
special braid d, if a_k S(d) belongs to B3, its right B2 coset is one
of the four already known cosets.

If a_k is outside B3, the proposition forces d=c_k. If a_k is in B3,
the complete special B3 list is {1,s,z,t s} and d is 1 or s. The eight
possibilities are explicitly

| a | c | parameter a S(c) | known coset representative |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 1 | s | t | t |
| s | 1 | s | 1 |
| s | s | s t | s t |
| z | 1 | z | z |
| z | s | s^2 | 1 |
| t s | 1 | t s | t |
| t s | s | t s t=s t s | s t |

Thus **every additional parameter coset must have its first special
color outside all four infinite families**. This statement quantifies
over every special second color, of arbitrary strand number and exponent.
It does not rely on trying a selected cancelling partner or on comparing
against a finite-height list.

For the first family write f_0=1, f_1=s and
f_(n+1)=f_n triangle f_(n-1). Then f_n S(f_(n-1))=s^n for n>=1.
For n>=3 the first color f_n is outside B3. Indeed epsilon(f_n)=ceil(n/2)
excludes n>=5 by the B3 exponent bound; f_3 and f_4 move respectively
the fourth and fifth strands. Consequently

```
For n>=3 and d special,
f_n S(d) in B3  if and only if  d=f_(n-1).
```

This strengthens the earlier observation that one naturally constructed
partner gives s^n: it proves that no other special partner can work.

## 3. A complete finite test for the excluded first-color families

Let p_0=epsilon(a_0), q_0=epsilon(c_0). Since
epsilon(a triangle c)=epsilon(c)+1, the first-color exponents are

```
epsilon(a_(2m))   = p_0+m,
epsilon(a_(2m+1)) = q_0+1+m.
```

For an input braid a with exponent e, membership in this family's
first colors can therefore occur only at

```
k=2(e-p_0),        when e>=p_0,
k=2(e-q_0-1)+1,    when e>=q_0+1.
```

There are at most two candidate indices for each family, hence at most
eight overall. Construct these finitely many explicit special words and
compare with a using the faithful Artin action. This is a terminating
exact membership test for the specified union of families, with no
term-height cutoff. The number of word comparisons is at most eight;
their word lengths and cost are not claimed to be uniformly bounded.
No match means only that this exclusion does not apply, not that a
produces a new parameter or is special.

The [implementation](../../scripts/b9_known_ray_filter.py) returns every
matching family/index, retaining possible coincidences at the small
initial colors. It makes no decision about the remaining B4 problem.

## 4. Verification and remaining scope

The [Python check](../../scripts/check_b9_known_ray_filter.py) applies the
new test to exactly the existing 52 height-at-most-four words and the
first colors of the existing 46 endpoint records. It does not enumerate
any larger term-height or coloring graph. It also checks the eight small
pairs, the f_3/f_4 permutation boundaries, and the explicit exponent
recurrence. The [GAP checker](../../scripts/check_b9_known_ray_filter.g)
independently reconstructs the rays as signed words, compares faithful
native free-group actions, and recovers the candidate-index sets by
iterating the exponent recurrence rather than using the inverted formula.
Exact counts and terminal process records are retained in the
[certificate directory](../../research/certificates/B9-known-ray-filter-v1/).
These computations check the displayed word interfaces and finite
fixtures; the universal uniqueness statement is the written argument
from the credited special-decomposition theorem.

The Python run matches 12 of the 52 first colors and all 46 endpoint
first colors. The GAP replay checks 60 family pairs through the largest
required candidate index 14, 109 exponent/index records, 734 exact word
comparisons, the eight small pairs and the two boundary permutations.
The two sequential jobs used one CPU and a 6 GB per-process limit each,
and passed in 5.789 and 2.780 seconds with empty stderr. No search bound
was increased, no failed run occurred, and both process groups were
observed absent afterward. The proof is not inferred from these counts.

The full archived GroupWorld braid page and exact B9 fragment were reread,
and the retained rendering was actually viewed during this pass.
Dehornoy's Lemma 2.1 and Propositions 2.2–2.5, and the special square-root
discussion at the end of Section 5.3, were reread in the archived text of
[*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf).
The free-LD division/closure theorem and decomposition uniqueness remain
credited dependencies, not independently reproved imported results.

A limited search also surfaced Cramer, Ho, Miller Edwards and Trang's
[*Free Left Distributive Algebras and a Canonical Extension*](https://arxiv.org/abs/2604.08768).
Only its abstract was consulted; its large-cardinal extension results
are not used here. Search results using “special braid” for different
positive-braid constructions were not treated as results about this
shelf. No exhaustive novelty audit or external review is claimed.

The unresolved case now excludes these entire four first-color families,
but it still allows other first colors and unbounded underlying strand
numbers. B9 remains partial. No extra whole-entry, subproblem or
established-novelty count is added.
