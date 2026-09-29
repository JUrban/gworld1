# B9: terminal pairs and complete positive-parameter classification

29 September 2026, during the original run. This is a reduction of the
remaining B4 case, **not its exhaustion**. It uses the conventions and
credited structural facts in `small-strand-proof.md`. No separate novelty
claim is made for these deductions.

Write s=sigma1, t=sigma2 and S for the shift. The remaining special
four-strand braids have the form

    I_2(A)=A t s S(A)^-1,       A=a S(c) in B3, a,c special.

Two parameters give the same braid precisely when they belong to the
same right coset modulo B2=<s>. The special decomposition of A is unique.
These are Dehornoy's Lemma 5.6 and Proposition 2.5.

## 1. Each represented coset has a unique terminal special pair

Define T(a,c)=(a triangle c,a). Expanding the shelf operation gives

    (a triangle c) S(a) = a S(c) s.                            (1)

Thus T is defined on every special pair, preserves its parameter coset,
and increases epsilon(a)+epsilon(c) by one. It is injective: the second
output recovers a, and left cancellativity recovers c.

An inverse step at (a,c) exists exactly when c triangle d=a for some
braid d. Such a d, if it exists, is special, by Dehornoy's Lemma 2.1.
The inverse is then (c,d), and its total exponent sum is one smaller.
Special exponent sums are nonnegative, so repeated inverse steps stop.
Call the final pair terminal.

The terminal pair is unique even among different special decompositions
representing the same coset. Indeed their parameters have the form A and
A s^k. If k>=0, applying T^k to the decomposition of A gives a special
decomposition of A s^k; uniqueness of special decomposition identifies
it with the other pair. If k<0, apply this argument in the opposite
direction. Consequently each coset represented by a special pair consists
of one ray of special pairs

    (a0,c0), T(a0,c0), T^2(a0,c0), ... ,                       (2)

and its admissible parameters are exactly A0 s^k, k>=0, for the unique
terminal parameter A0=a0 S(c0). No finiteness of the set of rays follows.

## 2. Classify every positive parameter

Here positive means that **A**, not necessarily I_2(A), belongs to the
standard Artin positive monoid B3^+.

For a positive word, follow the coloring of (1,1,1). Record just whether
each color equals 1. Every special product x triangle y is nontrivial,
because its exponent sum is epsilon(y)+1. At a positive crossing the
two identity flags therefore change by the exact rule

    (z_x,z_y) -> (false,z_x).                                 (3)

The positive words whose third output color is 1 form exactly the language

    s*  union  t s*  union  t* s t s*.                        (4)

Here is an elementary proof, without a word-length cutoff. Before the
first s, the first color remains 1. Under t^k the third color is 1 only
for k=0 or k=1: the first t makes the second color nontrivial, and any
subsequent t transfers a nontrivial color into the third position.

Once s first occurs, the first color is permanently nontrivial. That
first s makes the second color 1. Each later s transfers the nontrivial
first color to the second position, and each t makes the second color
nontrivial. Thus the second color can never become 1 again after the
first further crossing. If there is a t after the first s and the final
third color is to be 1, this t must be immediately after that first s,
and no further t is allowed. These are precisely the last words in
(4). If there is no such t, the initial exponent k must be zero or one,
giving the first two languages. All displayed words satisfy (3).

The braid relation t s t=s t s gives, by induction,

    t^k s t = s t s^k       for k>=0.                         (5)

Combining (4)--(5), the entire set of positive parameters with a special
decomposition (a,c,1) is

    {s^j, t s^j, s t s^j : j>=0}.                            (6)

Conversely these positive braids have the required third color, so (6)
is an equality, not just a necessary condition. Exactly three parameter
cosets have a positive representative: B2, t B2 and s t B2.

## 3. Known terminal pairs and the remaining restriction

Four terminal pairs are

| Pair | Parameter |
|---|---|
| (1,1) | 1 |
| (1,s) | t |
| (s,s) | s t |
| (u,1), where u=s triangle 1=s^2 t^-1 | u |

The first two are terminal because a=1 cannot equal c triangle d for
special d. For either of the last two, a putative inverse step requires

    S(d)=c^-1 a S(c) s^-1.                                   (7)

The right side is respectively t s^-1 or s^2 t^-1 s^-1. Its permutation
moves the first strand, whereas every shifted braid fixes that strand.
Thus no such inverse exists. This is only a necessary test for shifted
membership in general, but it suffices for these two exclusions.

The four cosets are distinct already in the standard representation

    s -> [[1,1],[0,1]],       t -> [[1,0],[-1,1]].

Right multiplication by any power of s preserves the first column.
The four displayed parameters have columns (1,0), (1,-1), (0,-1),
and (3,1), respectively. No faithfulness of this representation is
needed for their separation. In particular u B2 has **no** positive
representative, by Section 2.

There are no additional terminal pairs having an identity color. If
a=1, A=S(c) in B3 forces c in B2, giving c=1 or s. If c=1, A=a in B3
is one of the four special three-strand braids

    1, s, u, t s.

The middle case s and last case t s are the T-images of (1,1) and
(1,s), respectively; the other cases are already in the table.

Therefore **any additional B4 exponent-two special braid must have a
terminal parameter A0 with no positive representative in its coset,
both terminal colors nontrivial, and epsilon(A0)>=2**. This leaves an
unbounded class of possible parameters. We have not ruled it out.

## 4. Checks, provenance and limits

The source is Dehornoy, [*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf),
Lemma 2.1, Propositions 2.3/2.5 and Lemma 5.6, archived previously in
`literature/raw/B9-Strange-Questions-Dgb.pdf`. The relevant Section 2
and Section 5 text was reread for this deduction. Lemma 2.1 imports the
free-LD division theorem; no independent proof of that deep input is
claimed. The original B9 fragment and its actual retained rendering were
reread and viewed again; the statement and shelf conventions agree.

The new Python check compares (3) with an NFA for (4) by exhausting their
reachable product automaton: ten states and twenty transitions. This is
a finite verification of the regular-language claim for all positive
word lengths. It includes a missing-branch negative control and rejects
t^2. The handwritten argument above supplies its mathematical meaning.

A separate GAP checker independently reconstructs all 46 saved endpoints
from the earlier depth-12 probe as explicit iterates of the four terminal
pairs. Their distribution is 13,12,11,10; there are 244 forward steps in
total, with largest individual count 12. Faithful Artin actions on F18
check both colors and the parameter identity, and check the four cosets
and terminal obstructions. This replaces reliance on CBraid for those
46 endpoint certificates. It does not replay the other 1845 graph states
or establish global exhaustion. No search bound was increased.

Both recorded jobs passed with empty stderr: the Python run took 0.12s
with one CPU/2GB, the GAP run 2.78s with one CPU/6GB. Exact commands,
fixtures, source bindings and logs are listed in
`research/certificates/B9-positive-parameters/manifest-v1.json`.

These deductions sharpen the remaining question without resolving it.
B9 remains one partial candidate; the whole experiment remains at ten
whole-entry candidates, two partial candidates and zero established
novel results. Independent specialist and novelty review are outstanding.
