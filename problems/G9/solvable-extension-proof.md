# G9 supplement: effective growth approximation in every free solvable group

29 September 2026, argument approximately 09:53–09:58 UTC.
Candidate extension of `flow-growth-proof.md`; no additional GroupWorld
entry is counted. The exact growth constants and novelty remain unresolved.

## General theorem

Let F=F_r with specified basis a_1,...,a_r, let h:F->Z send a_1 to 1
and the other generators to 0, and let sigma invert a_1 while fixing
the other basis elements. Suppose R is a normal subgroup of F with

    R <= ker(h),             sigma(R)=R.

Set Q=F/R and G=F/R'. Use the images of the specified free basis as
generators. Let V(n) count the ball in G and let lambda be its
exponential growth constant. Let P(t) count strictly decreasing positive
integer lists with sum at most t, including the empty list. For every
n>=1, the following inequalities hold:

    max(1,(V(n)/[(n+1)^3 P(n+1)^2])^(1/(n+2)))
       <= lambda <= V(n)^(1/n),                              (1)

and the logarithm of the ratio of these endpoints is at most

    [2 log(2r+1)+3 log(n+1)+4 sqrt(n+1)]/(n+2).              (2)

If a word-problem algorithm for Q is given, (1)–(2) give an algorithm
computing rational enclosing intervals of any requested positive rational
width. The algorithm is uniform in r, that word-problem algorithm and
the width, **under the stated promises on R**. No algorithm to verify
those promises from arbitrary presentation data is asserted.

## Flows on a noncommutative quotient

Use the labelled Cayley graph of Q: the positive edge (q,j) goes from q
to q a_j. Keep labels and orientation, including loops and parallel
edges if some generator images coincide or have finite order. The
classical Droms–Lewin–Servatius flow criterion, recalled as Guba
math/0508422 Lemma 3, says that two words give the same element of G
if and only if their integral net edge flows agree on this graph.
This cited theorem is stated for arbitrary normal R, not just F'.

The flow boundary is delta_endpoint-delta_start. Left translation L_q
maps positive edges (p,j) to (qp,j), preserves labels and orientations,
and adds h(q) to vertex heights. Concatenation has flow

    f_(uv) = f_u + L_(bar u) f_v,

where bar u is the endpoint in Q. Commutativity of Q is not needed.

The hypothesis on R makes sigma an automorphism of Q, reversing h.
It fixes the labels j>1. On a positive first-generator edge (q,1),
it reverses orientation and gives the negative of the positive edge

    (sigma(q) a_1^-1, 1).

In particular the right multiplication by a_1^-1 in this formula must
not be replaced by left multiplication. Moreover
sigma L_q = L_(sigma(q)) sigma on flows.

Define upper edge height as h(q)+1 for j=1 and h(q) otherwise. A strict
bridge of endpoint height H has all its flow in the upper-height band
(0,H]. Translating consecutive bridges puts their flows in disjoint
bands. Boundary recovery then retrieves the successive Q-endpoints and
each normalized factor flow. Thus the fixed-height bridge product map
is injective exactly as in the lattice case.

## Noncommutative recovery of the unfolded pieces

The sequence of heights along any word is still an integer walk with
increments 0,+1,-1. For a strict half-space representative take the
last remaining maximum, then last remaining minimum, and alternate.
The spans s_1>...>s_k>0 have total at most its length. Apply sigma to
the downward pieces and concatenate: the result is a bridge of the
same word length. This uses a basis permutation with inversions, so
the reflection itself changes neither the length nor the allowed labels.

Suppose the total unfolded flow and the span list are given. Let z_i
be the current start of the i-th piece in Q, and p_i its original start.
Initially z_1=p_1=1. Restrict the unfolded flow to its i-th height band,
giving C_i; its boundary determines the next endpoint z_(i+1).
Normalize and undo the reflection by setting

    D_i = sigma^(i-1)(L_(z_i^-1) C_i).

Here powers of sigma are read modulo two. The original contribution is
L_(p_i) D_i, and its next starting point is

    p_(i+1) = p_i sigma^(i-1)(z_i^-1 z_(i+1)).          (3)

All products in (3) occur in the displayed order. Summing the restored
contributions recovers the original flow and therefore the original
element of G. No representative path or cut times are needed. This is
the only substantive change from the lattice implementation: subtraction
of coordinates becomes multiplication by an inverse on the **left**.

Consequently if b(n,H) counts bridge elements of height H admitting a
representative of length at most n, then b(n,H)^k<=V(kn), and hence
b(n,H)<=lambda^n. If c(n) counts strict half-space elements, the recovery
map just proved gives c(n)<=P(n) sum_H b(n,H)<=P(n)n lambda^n.

Finally split any representative w=P Q at a global minimum height.
The words x=a_1 P^-1 and y=a_1 Q are strict half-space words and
x^-1 y=w, also in this noncommutative group. Their total length is at
most n+2. Thus V(n)<=(n+1)^3 P(n+1)^2 lambda^(n+2).
Submultiplicativity gives the upper bound. The same elementary bound
P(t)<=exp(2 sqrt(t)) and V(n)<=(2r+1)^n prove (1)–(2).

## Effective enumeration and the free-solvable corollary

With a word-problem algorithm in Q, a finite set of path prefixes can
be partitioned into equal Q-elements. For any finite list of words,
their flows can therefore be computed and compared exactly. Enumerating
all words of length at most n and deduplicating their flows computes
V(n). This requires no oracle for geodesic length and no pre-existing
canonical normal forms in Q.

The rational radius-selection and radical-bisection algorithm in the
original G9 proof now applies unchanged. In particular, for n=m^2-1,
m>=2, the difference between the two algebraic endpoints in (1) is
at most

    (2r+1)(4r+2+7m)/(m^2+1).

Take R=F_r^(d-1) for d>=2. It is characteristic and contained in F_r',
so both promises hold. The word problem in Q=F_r/F_r^(d-1) is decidable
uniformly by induction: the base d-1=1 is exponent-sum equality, and
the next derived quotient is handled by the same finite flow criterion.
This recovers the classical recursive Magnus word-problem procedure.
It proves the candidate corollary:

**The standard-basis exponential growth constant of F_r/F_r^(d) is
computable uniformly in r>=1 and d>=1. The modulus above is independent
of d.** For d=1 the constant is 1; the rank-one cases also have value 1.

Uniformity of the modulus does not assert uniform efficient ball
enumeration: the underlying word-problem work depends on d. Nor does
this give the growth series or an exact algebraic expression. Prior
lower bounds and convergence to the free-group rate in increasing
derived length, such as Arzhantseva–Guba–Guyot, remain explicitly credited.

## Scope of checking

`solvable-extension-audit.md` records independent computations in which
the deck group is a genuinely nonabelian free metabelian group. These
checks test the ordering in (3), graph reflection and faithful flows;
they do not constitute specialist review of the theorem for arbitrary R.
No result on G11, general solvable groups, or arbitrary generating sets
is inferred. The GroupWorld tally remains six whole and four partial
candidates, zero established novel results.
