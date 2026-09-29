# G9: effective approximation of the free metabelian growth constant

29 September 2026, first argument approximately 09:19–09:23 UTC.
**Candidate partial result:** a uniform algorithm to approximate the
standard growth constant in every finite rank, with a proved error bound.
For rank two, finite certificates also give
`2.658596558 <= lambda_2 <= 2.943737759`.
This is not a closed expression for the constant, a rational growth
series, or a practical high-precision calculation. Novelty and independent
specialist review remain outstanding.

The full original growth page, G9 background and actual rendered G9
statement were inspected. The background specifies the ordinary word
growth rate with respect to the standard free generators. We retain
that generating set, rather than the minimum over generating sets or
the much coarser equivalence class of exponential growth functions.

## The quantitative statement

Let M_r=F_r/F_r'' with its standard symmetric generating set, r>=1.
Write V_r(n) for the number of elements of word length at most n, and

    lambda_r = lim_(n -> infinity) V_r(n)^(1/n).

The limit exists by submultiplicativity of balls. Let P(t) be the number
of strictly decreasing finite lists of positive integers having sum at
most t, including the empty list. Put

    K_n = (n+1)^3 P(n+1)^2.

For every n>=1 the proposed bounds are

    max(1, (V_r(n)/K_n)^(1/(n+2))) <= lambda_r <= V_r(n)^(1/n).     (1)

In particular, if L_n,U_n denote the left and right sides, then

    log(U_n/L_n) <=
       [2 log(2r+1) + 3 log(n+1) + 4 sqrt(n+1)]/(n+2).             (2)

Every V_r(n) is exactly computable by a finite lattice-flow enumeration.
The error in (2) tends effectively to zero, uniformly in r. Thus given
r and a positive rational epsilon, there is an algorithm returning
rational L,U with L<=lambda_r<=U and U-L<epsilon.
The rank-one value is 1 directly. No efficiency bound is claimed for
enumerating the very large balls demanded by small epsilon.

## Faithful lattice flows

Regard a word as a lattice path from 0 in Z^r, with generator a_j giving
the step e_j. For the positively oriented edge (z,j): z -> z+e_j, let
f_w(z,j) be its net traversal count. Only finitely many counts are
nonzero. Two words represent the same element of M_r exactly when their
flows agree.

This is the classical flow criterion for F/R', applied to R=F': loops
in the covering graph for F/R represent R, and their integral edge
cycles identify R/R' with the first homology of that graph. In particular,
zero net flow is precisely the commutator subgroup of R. This criterion
is credited to Droms–Lewin–Servatius, and is explicitly stated and proved
as Lemma 3 in Guba [math/0508422](https://arxiv.org/abs/math/0508422),
page 5, which was read and visually inspected. We use no assertion about
polynomial-time computation of shortest representatives.

The flow determines its endpoint: its boundary is delta_endpoint-delta_0.
The same holds for a path with any specified starting point. Word
concatenation adds the first flow to the translate of the second flow
by the first endpoint. Reflection of the first lattice coordinate sends
a_1 to a_1^-1 and fixes the other letters; it acts on flows as the
corresponding graph reflection, reversing the orientation of first-axis
edges. These observations let us recover group elements from separated
parts of a flow even when paths have repeated edges and cancellations.

## Bridge elements and concatenation

Use the first coordinate as height. A strict half-space word w of length
ell is one whose successive vertex heights satisfy h_0=0 and h_i>0 for
1<=i<=ell. It is a bridge of height H if also h_i<=h_ell=H for all i.
These conditions concern a representative path; we count its represented
group element only once.

Let B(n,H) be the set of elements admitting a bridge representative of
length at most n and height H; write b(n,H)=|B(n,H)|. Heights range from
1 to n. Define the upper height of a positive edge by

    height(z,j) = z_1 + 1_(j=1).

A strict bridge flow of height H is supported on edges with upper height
in {1,...,H}. In particular, it has no horizontal edge at its initial
height. Concatenating k bridges of the same height H places their flows
in the disjoint bands

    ((i-1)H, iH],  i=1,...,k,                            (3)

where a band refers to upper edge height. From the total flow one can
restrict to these bands, recover successive endpoints using boundaries,
and translate each piece back to 0. Thus distinct k-tuples of bridge
elements give distinct products. The argument uses disjoint *edges*;
sharing the boundary vertex or having horizontal edges at a terminal
height causes no ambiguity.

There are b(n,H)^k such products in the ball of radius kn. Taking k-th
roots and the growth limit proves

    b(n,H) <= lambda_r^n,
    b(n):=sum_(H=1)^n b(n,H) <= n lambda_r^n.             (4)

More generally any finite family of distinct bridge elements of one
fixed height generates a free monoid, with any chosen bridge word
lengths as costs. Different numbers of factors have different endpoint
heights. If c_l is the number of chosen elements of cost l, and rho is
the positive solution of sum_l c_l rho^-l=1, then lambda_r>=rho. Indeed,
the generating function for words in this free monoid is
1/(1-sum_l c_l z^l), and every such word has group length at most its
cost. This gives finite, independently reproducible lower bounds.

## Unfolding at the level of flows

We adapt the classical Hammersley–Welsh unfolding argument. That argument
is for self-avoiding paths; here paths need not be self-avoiding and the
objects being counted are group elements. The required extra point is
recovery from the **total flow**, not from the unfolded path. A primary
account of the classical decomposition is Duminil-Copin–Ganguly–Hammond–
Manolescu, *Bounding the number of self-avoiding walks: Hammersley–Welsh
with polygon insertion*, Section 2. Its Lemmas 2.1–2.2 were read and
the page containing the latter proof was visually inspected.

For each element represented by a strict half-space word of length at
most n, choose one such word deterministically, for example a shortest
one followed by a lexical tie break. Starting at time 0, cut at the last
occurrence of the highest height in the remaining path. Then cut at the
last occurrence of its lowest remaining height, then highest, and so on,
stopping when the final vertex is reached. The positive spans s_1,...,s_k
of the successive pieces satisfy

    s_1 > s_2 > ... > s_k > 0,     sum_i s_i <= n.         (5)

For the first strict inequality, every vertex after time 0 has height at
least 1. At each subsequent step the previous extremum was taken at its
*last* occurrence, so the new remaining span is at least one smaller.
Each span requires that many first-axis steps, proving the sum bound.
In particular k(k+1)/2<=n. Every piece, after reflecting the first
coordinate when its direction is downward, is a strict bridge.

Concatenate these reflected pieces, in their original order, to obtain
a bridge of the same word length. Its flow separates into the disjoint
bands (S_(i-1),S_i], where S_i=s_1+...+s_i. Therefore, from its flow and
the list (s_1,...,s_k), one recovers each translated piece flow, its
endpoint, and its original reflection and position. Adding the restored
pieces recovers the original flow. No original path or cut times are
needed by this recovery operation. Vanishing edge counts within a piece
are harmless because its boundary still recovers its endpoints.

Consequently two different original group elements cannot produce the
same pair consisting of unfolded flow and span list. If h(n) counts
the elements admitting a strict half-space representative of length at
most n, then (4) and (5) give

    h(n) <= P(n) b(n) <= P(n) n lambda_r^n.               (6)

For completeness, P(t)<=exp(2 sqrt(t)) for t>=1. For any s>0,

    P(t) <= exp(st) product_(j>=1)(1+exp(-sj))
         <= exp(st + 1/(exp(s)-1)) <= exp(st+1/s).

Take s=1/sqrt(t). Alternatively P(t) is obtained exactly from the
coefficients through degree t of product_(j=1)^t (1+z^j).

## From arbitrary elements to half-space elements

Choose a word w of length at most n for each element in the ball, and
split w=P Q at a vertex of globally minimal height, after i letters.
Viewed from that vertex, both the reverse path P^-1 and the forward path
Q stay at nonnegative relative height. Thus

    x=a_1 P^-1,    y=a_1 Q

are strict half-space words of lengths at most i+1 and n-i+1, and
x^-1 y=w in the group. This also covers an empty piece or the identity
word. The pair of represented elements determines w's group element,
so

    V_r(n) <= sum_(i=0)^n h(i+1) h(n-i+1)
           <= (n+1)^3 P(n+1)^2 lambda_r^(n+2).           (7)

Use (6), monotonicity of P, and (i+1)(n-i+1)<=(n+1)^2 for the last
inequality. Equation (7) proves the lower bound in (1). Fekete's lemma
gives lambda_r=inf_n V_r(n)^(1/n), proving the upper bound.

Finally V_r(n)<=(2r+1)^n by padding words with an identity symbol.
Taking logarithms in (1), and using the partition estimate, gives (2).
Clamping the lower endpoint at 1 can only improve that estimate.

## Explicit terminating approximation algorithm

To compute V_r(n), enumerate all words of length at most n and put their
integer flow vectors in a finite set. Freely reduced words suffice.
This counts group elements by the faithful flow criterion, without an
oracle for geodesic length. Compute P(n+1) by integer dynamic programming
and form the algebraic endpoints in (1). Rational bisection of their
integer powers produces certified rational enclosing endpoints.

The procedure can choose n in advance without knowing lambda_r. For
m>=2 put n=m^2-1. The elementary inequalities log(n+1)<=sqrt(n+1) and
log(2r+1)<=2r+1 imply

    U_n-L_n <= (2r+1) * (4r+2+7m)/(m^2+1).               (8)

Choose an integer m making the rational expression in (8) less than
epsilon/2, then bound each radical outward to within epsilon/4. This is
a uniform terminating algorithm in r and epsilon. It is likely very
expensive: our bounded computations validate the construction and small
growth counts, not a practical execution at fine requested accuracy.

## Limits, verification and status

The proof supplies effective two-sided approximation of the actual
standard-basis constant, not merely another proof of exponential growth.
The experiment records it as a **partial G9 candidate**, because no
closed expression or useful high-precision value has been obtained.
The fixed-height bridge computations stop below the numerical lower
bound quoted in the website's background. The separate atom construction
below gives a larger lower bound, without claiming it is the best bound
in the literature.

The new Python decoder, independent GAP Laurent-polynomial Magnus
calculations, and separate C++ bridge enumeration are described in
[the audit](flow-growth-audit.md). They are implementation checks, not
independent specialist review of the all-rank proof. The flow criterion
and classical unfolding method are prior work and explicitly credited;
novelty of this combination for growth constants is not established.

## Supplement: bridge atoms and a numerical lower bound

A stronger finite alphabet can combine several bridge heights. For a
bridge flow of height H, call an integer h with 1<=h<H a separating cut
if exactly one first-axis edge based at height h has nonzero flow. Its
coefficient must be +1: the algebraic total flow through every level
between the initial and terminal heights is +1. Call a bridge element
an atom if its flow has no separating cut. This property depends only
on the element's flow, not on the particular bridge path chosen.

Any set of distinct such atoms, with arbitrary positive heights, freely
generates a monoid. Indeed, concatenate their bridge paths. At every
factor boundary of height h, the next factor has exactly one first-axis
edge based at h, with coefficient +1; its strict half-space condition
prevents a return to that starting height. Previous factors have no
edges above their terminal height, and subsequent ones lie higher.
Thus this boundary is a separating cut of the total flow. Within each
factor there is no separating cut, and disjoint edge bands prevent
another factor from changing that fact. Consequently the separating
cuts of the product are precisely its factor boundaries. They recover
the number and heights of the factors; restriction to the corresponding
bands and successive endpoint recovery then recover each factor flow.
This proves uniqueness of every product, including between tuples with
different numbers or heights of factors.

For each distinct atom in a finite list choose a bridge representative
of cost l, and let c_l count these chosen representatives. As before,
if rho is the positive root of sum_l c_l rho^-l=1, then lambda_2>=rho.
The certificate constructed here enumerates all rank-two strict bridge
words through length 14 and deduplicates atom flows, choosing a shortest
bridge word within that enumeration. Global geodesicity is not required:
the chosen lengths are valid upper bounds for group length.

The verified count vector, indexed by l=1,...,14, is

    1, 2, 2, 2, 2, 6, 26, 71, 162, 341, 779, 1961, 5098, 13030.

There are 21,483 distinct atom elements. The resulting exact rational
lower bound is

    lambda_2 >= 2658596558/1000000000 = 2.658596558.

The root of this particular certificate polynomial lies below
2.658596559. That last number bounds the polynomial root, **not**
lambda_2. This lower bound exceeds the 2.63815853034 quoted in the
frozen website background. No current best-in-literature claim is made.
We have not validated the website's description of that decimal as a
rigorous lower bound: Section 5.3 of its cited Guttmann–Conway paper
reports numerical estimates. This comparison supplies no premise of
our lower-bound proof.
The full list of representative words is included, so a verifier needs
only check that the listed elements are distinct atoms of the stated
costs, not trust that the enumeration was exhaustive. Completeness of
the enumeration is useful for comparison between implementations, but
is unnecessary for the resulting lower bound.

## Supplement: forbidden subwords and a numerical upper bound

Order the signed alphabet as -2 < -1 < 1 < 2 and order words first by
length, then lexicographically. Every group element has a unique least
word in this order. Suppose two explicit words w,u have equal flows
and u is strictly smaller than w. No least word can contain w as a
contiguous subword: replacing that occurrence by u gives a smaller word
for the same element. This argument does not require a complete rewriting
system, or that u itself be a least word.

Our certificate gives 648 such forbidden words, including the four
inverse-adjacency pairs with replacement the empty word. The longest
word has length 10. A finite automaton for avoiding them has 1968 states:
the empty word and all proper prefixes of forbidden words. Its state
after an accepted prefix records the longest suffix that is one of those
prefixes. Appending a letter is rejected if it completes a forbidden
word; otherwise it moves to the corresponding longest suffix. Every
state is accepting. In particular every least representative is accepted.

Let A be the nonnegative integer matrix counting allowed single-letter
transitions. The certificate supplies a vector v with strictly positive
integer entries, and the independently checked inequalities

    A v <= U v,       U = 2943737759/1000000000.

If m is the minimum entry of v and v_0 its initial-state entry, then
the number of accepted words of length n is at most

    e_0 A^n 1 <= (v_0/m) U^n.

Since U>1, summing through n gives the same exponential upper bound for
balls. Every element in the ball has one accepted least representative
of length at most n, so lambda_2<=U. The GAP verifier checks every relation
using native Laurent-polynomial Magnus entries, reconstructs every state
and transition from the forbidden words, and verifies all 1968 integer
inequalities. Thus the upper bound does not depend on the completeness
of the generator's bounded enumeration or on floating-point eigenvalues.

Together the two explicit certificates prove the candidate enclosure

    2.658596558 <= lambda_2 <= 2.943737759.

This is a coarse enclosure. Neither endpoint is asserted to be optimal
or previously unknown, and the exact constant remains undetermined.
