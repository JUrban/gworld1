# B9: deciding every possible partner of a fixed first color

30 September 2026, within the original experiment. This supplements the
[fixed-first-color uniqueness argument](fixed-first-color-reduction.md).
The new reduction is uniform in the first braid and gives a finite list
of possible partners. It does not classify all special four-strand braids.

Write s=sigma1, t=sigma2 and S for the shift. Let C be the special braids.
For any supplied braid a, not necessarily special, put

```
R(a) = { c in C : a S(c) belongs to B3 }.
```

**Proposition.** R(a) is effectively computable. If a is represented in
B_m with m>=3, an explicit strand-deletion test either proves R(a) empty
or reduces its computation to at most m-1 specialness decisions.
No bound on the term height of c is imposed. As proved previously, R(a)
is {1,s} when a lies in B3, and otherwise has at most one element.

## 1. An elementary product-membership test

Let D(a) be the three-braid obtained by retaining only the strands that
start in positions 1,2,3, deleting all others, and relabelling the surviving
endpoints in their order. This is well-defined on braids. It is not a
homomorphism on all B_m: for example, D(sigma3 sigma2)=1, whereas
D(sigma3)D(sigma2)=sigma2. The following restricted product rule is what
we need.

Set H=S(B_(m-1)). If a=A h with A in B3 and h in H, then

```
D(a) = A t^j                    for some integer j.           (1)
```

To prove (1), choose a diagram formed by the A portion followed by the
h portion, in the word-concatenation convention used by the implementation.
The A portion preserves the retained set and survives deletion unchanged.
In the h portion the first strand never crosses another strand. After
deletion, only the two other retained strands can cross one another, so
that portion is a power of the second generator of B3. No statement about
deletion of an arbitrary product is used.

Consequently

```
a belongs to B3 H  if and only if  a^-1 D(a) belongs to H.      (2)
```

For the forward implication, (1) gives a^-1 D(a)=h^-1 t^j in H.
For the converse, writing q=a^-1 D(a) in H gives a=D(a) q^-1.
Thus the actual factorization is constructed when the test succeeds.

Membership in H is itself elementary and exact. For a word q in B_m,
track its first strand. If it does not finish in position one, q is not
in H. Otherwise delete that strand, obtaining a word d in B_(m-1), and
test the full braid equality q=S(d). Equality proves membership and
produces the preimage; inequality disproves it. The converse holds because
deleting the fixed first strand of a shifted braid recovers its preimage.
The program tests equality with the faithful Artin action on a free group,
not merely with permutations or a potentially nonfaithful matrix image.

## 2. All partners lie in one explicit cyclic coset

If (2) fails, R(a) is empty. Suppose it succeeds, and put

```
A0=D(a),       c0=S^-1(a^-1 A0),       a S(c0)=A0.             (3)
```

The braid c0 is not assumed special. Every braid c satisfying a S(c) in
B3 must lie in B_(m-1), since S(c)=a^-1(a S(c)) lies in B_m and the
standard shifted-parabolic intersection removes one strand.

For such c, the two parameters satisfy

```
A0^-1 (a S(c)) = S(c0^-1 c)
              in B3 intersect S(B_(m-1)) = <t>.
```

Hence c=c0 s^k for one integer k. Conversely every such braid satisfies
a S(c)=A0 t^k in B3. This describes **all** possible partners before the
specialness requirement, not a sample of them.

The credited exponent bound for special braids in B_(m-1) is
0<=epsilon(c)<=m-2. Therefore the complete candidate list is

```
c0 s^k,   -epsilon(c0) <= k <= m-2-epsilon(c0).                (4)
```

There are exactly m-1 entries to test. The bound m may come directly
from the input word and need not be the smallest strand number. Testing
specialness in (4) using Dehornoy's existing algorithm proves the
proposition. This does not provide a uniform word-length or runtime bound.

## 3. The specialness procedure actually implemented

The [Python module](../../scripts/b9_fixed_color.py) implements (2)--(4)
and the following existing specialness procedure. First rewrite a braid
word as a positive word followed by a negative word using Artin word
reversing. Then propagate the unit colors through that fraction. At a
positive crossing apply (x,y)->(x triangle y,x). At a negative crossing,
solve y triangle d=x by testing

```
S(d) = y^-1 x S(y) s^-1.
```

The same exact deletion/equality test computes d if it exists. Division
closure ensures that d remains special. If a division is impossible,
the required coloring does not exist. Otherwise the braid is special
exactly when every final color after the first is trivial. The first
color is then the input braid.

Termination of word reversing into the fraction and completeness of
this coloring test are credited inputs from Dehornoy's
[*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf),
Lemma 2.1 and Propositions 2.2--2.3. They are not inferred from the tests
below. The program also uses the earlier credited exponent/permutation,
positive-special and right-power restrictions as quick decisions where
they apply. None of their necessary conditions is used as a sufficient
specialness test. In particular a nonspecial braid can satisfy the
right-power identity.

The default implementation has explicit limits on word size, faithful
image size and reversal steps. A limit raises `ResourceLimit`; it never
returns a negative mathematical answer. Invalid letters are rejected.
The uncapped algorithm terminates by the cited results, but no claim of
practicality on arbitrary input is made.

For a supplied finite word one can call `fibre(word)` after importing
the module from `scripts`. Its complete result lists each candidate,
its decision evidence, every actual special partner and a B3 word for
the parameter. The accompanying checker catches resource exceptions as
`incomplete` and requires all fixture decisions to complete before passing.

## 4. What this settles for the retained first colors

Applied to the **same 52 height-at-most-four first colors** already stored
in the experiment, the procedure completes every decision:

| Outcome | First colors |
| --- | ---: |
| No factorization in B3 S(B_(m-1)) | 34 |
| Factorization exists, but no candidate partner is special | 6 |
| At least one special partner | 12 |

There are 59 candidate specialness tests and 16 total partners. Four
small first colors have the two partners 1,s; eight others have a single
partner. Every resulting I2(parameter) belongs to the four already known
parameter classes, as separately verified by full faithful actions.

Thus the forty negative cases exclude **every** special second color,
of arbitrary term height. This is stronger than pairing the 52 first
colors only with another bounded list. The twelve positive first colors
are precisely the already identified known-ray cases. It does not extend
the finite list of first colors or establish that no other first color
could give an additional B4 braid.

## 5. Independent reconstruction, failures and scope

The [GAP checker](../../scripts/check_b9_fixed_color.g) independently uses
native free-group words for the faithful action. It redoes strand deletion,
shifted-subgroup decisions, every candidate interval and specialness
certificate, and all resulting parameter equalities. It checks the literal
positive/negative fraction against the original braid; it does not trust
the Python reversing implementation. Coloring steps are checked as full
braid identities against the retained compact representatives.

The final replay covers 52 original first colors, 66 specialness checks
(59 candidates and seven controls), 53 coloring steps, an explicitly
failed division, five fraction controls and sixteen product-deletion
controls. The negative controls include a nontrivial exponent-zero braid,
positive nonspecial braids and a right-power root with a failed coloring.
The original input words retain their earlier special-term certificates.

Four sequential jobs used one CPU and a 6 GB per-process limit. Python
v1 passed in 0.120 seconds; v2 added invalid-input/resource-limit controls
and the failed-division example and passed in 0.119 seconds. GAP v1 failed
because a classifier reused its caller's working variable. The wrapper
rejected its zero exit status because the error was emitted and the
success marker absent. Its exact source and logs are retained. Giving
that working variable local scope and checking all sixteen output classes
produced the final GAP pass in 1.824 seconds, with empty stderr.

The source page and exact B9 fragment were reread and the retained
statement rendering was viewed. The relevant prior coloring and braid
ordering passages were reread in the archived Dehornoy paper. The
procedure imports the established specialness and braid-support results
already credited in the experiment.

The general proof is a same-agent deduction, and the separate GAP replay
is computational verification, not outside mathematical review. No novelty
claim or extra problem count is made. B9 remains partial: the first colors
outside the previously excluded families and this finite fixture set
still leave the B4 count unresolved.
