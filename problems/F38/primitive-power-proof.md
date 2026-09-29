# F38(c): primitive powers in ambient rank at least three

29 September 2026, approximately 09:00–09:14 UTC. **Complete candidate
classification of a restricted case**, with an elementary growth witness.
Independent specialist review and novelty assessment remain outstanding.
This supplements the existing partial F38 entry; it does not solve
general part (c) or add another entry to the experiment's tally.

The original F38 statement, background and rendered paragraph were read
again. Its quantifier is over automorphisms of the specified ambient free
group. The rank restriction below is essential.

## Theorem

Let F_r have rank r>=3. Suppose u is conjugate to p-th power of a primitive
element a, with p nonzero. For a nonidentity v, the following are equivalent:

1. u and v are boundedly translation equivalent: for some C>=1,

       C^-1 ||phi(u)|| <= ||phi(v)|| <= C ||phi(u)||

   for every phi in Aut(F_r).
2. There is any finite-valued function f on the positive integers with
   ||phi(v)||<=f(||phi(u)||) for all phi.
3. v is conjugate to a nonzero power of the same element a.

If (3) fails, an explicitly constructible automorphism theta fixes [u]
and has ||theta^n(v)|| growing at least linearly as n tends to infinity.
If v is conjugate to a^q, the ratio is exactly |q/p| for every phi.
We use oriented conjugacy classes; v may be a power of either sign.

## An exact Nielsen growth formula

Take distinct positive basis letters d,e and let sigma=sigma_(d,e) be
the automorphism d -> d e fixing all other basis elements. Let w be a
nonempty cyclically reduced word. If w is a power of e, sigma fixes it.
Otherwise list its non-e letters cyclically as t_1,...,t_s and write
e^(k_i) for the possibly empty run between t_i and t_(i+1). Put

    epsilon_i = 1_(t_i=d) - 1_(t_(i+1)=d^-1).

For every integer n,

    ||sigma^n(w)|| = s + sum_i |k_i+n epsilon_i|.          (1)

Indeed, substitution inserts e^n after each positive d and e^-n before
each negative d. No two non-e letters cancel. If successive such letters
are inverse, their original e-run is nonempty and epsilon_i=0: when the
letters are d,d^-1 both contributions cancel, and for any other inverse
pair both are zero. Their separating run therefore never disappears.
If the letters are not inverse, an empty resulting run causes no
cancellation. This also applies across the cyclic seam and proves (1).

Consequently the orbit length is bounded precisely when every epsilon_i
vanishes. Put

    delta = sum_i |epsilon_i|,
    T = max_i |k_i|,
    beta = s + sum_(epsilon_i!=0) epsilon_i k_i
             + sum_(epsilon_i=0) |k_i|.

Then ||sigma^n(w)||=delta n+beta for every n>=T. This supplies an exact
eventual growth rate and threshold whenever delta>0.

## The zero-growth graph

Form the following folded two-vertex inverse labeled graph Gamma_(d,e).
At vertex 0 place a loop for every positive basis letter except d;
add a d-edge from 0 to 1 and an e-loop at 1. Include all inverse edges.
This is the based core graph of

    < basis letters other than d, d e d^-1 >.

A cyclic word has zero growth in (1) precisely when it labels a closed
path somewhere in this graph. Such a path may start at either vertex,
which is necessary for a conjugacy statement. To see the equivalence,
the conditions epsilon_i=0 say that each positive d is followed, after
an e-run, by a negative d, and each negative d is preceded in this way
by a positive d. Each such excursion uses the d-edge, some e-loops at
vertex 1, and the inverse d-edge. All remaining letters stay at vertex
0. Pure e powers lift as well. Reading a closed path conversely gives
exactly these pairing conditions.

## A finite family detecting every non-power

Use a basis (a,b,c,x_4,...,x_r). First take the three Nielsen automorphisms

    sigma_(b,c), sigma_(c,b), sigma_(b,a).                 (2)

All fix a. A conjugacy class of bounded length under the iterates of
each of them has a closed lift in each of their two-vertex graphs,
hence a closed lift in the product graph. Conversely a closed product
lift gives all three zero-growth conditions.

For clarity the entire relevant product graph can be listed. Its eight
vertices are binary triples; its positive edges are

    b: (0,s,0) -> (1,s,1), s=0,1;
    c: (s,0,0) -> (s,1,0), s=0,1;
    a: loops at 000 and 001;
    x_j (j>=4): a loop at 000 only.

There are no other positive edges. The b,c edges form a forest: the
component of 000 has edges 000--101, 000--010, 010--111; another edge
joins 100 to 110. Vertex 001 is a separate loop component, and 011 is
isolated. Deleting tree leaves leaves only the loops at 000 and 001.
A cyclically reduced closed path cannot use the deleted edges.

It follows that a cyclically reduced word with zero growth under all
three automorphisms in (2) uses only a and x_4,...,x_r. For each j>=4
also use sigma_(x_j,b). In a word with no b letters, formula (1) has
all k_i=0. Its growth rate equals the number of occurrences of x_j
or x_j^-1: a positive and following negative x_j cannot cancel the
two contributions in epsilon_i, because those would be adjacent
inverse letters in the original cyclic word. Thus zero growth forces
the absence of x_j.

The resulting family of r automorphisms,

    (b -> bc), (c -> cb), (b -> ba),
    (x_j -> x_j b), j=4,...,r,

has common bounded conjugacy classes exactly the powers of a. For any
other nonidentity cyclic word, at least one member has delta>0 in (1).
This is a finite explicit test and not an inference from a bounded
enumeration of words.

## Normalization and proof of the theorem

After replacing the primitive element by its inverse if necessary, take
p>0. Whitehead reduction of the maximal cyclic root of u recognizes
primitivity and constructs an automorphism mu with mu[u]=[a^p]. Apply
mu simultaneously to v and cyclically reduce. If the resulting word is
a power a^q, then v is conjugate to the q-th power of mu^-1(a), while
u is conjugate to its p-th power. Unique roots in a free group identify
this cyclic subgroup with the one in the statement. The exact length
ratio proves (3) implies (1), and (1) implies (2) immediately.

Otherwise choose a positive-growth sigma from the finite family and set

    theta = mu^-1 sigma mu.

This fixes [u]. Put L_mu=max_x |mu(x)| in the chosen basis. Cyclic
length satisfies ||mu(z)||<=L_mu ||z||, by substituting a shortest
cyclic representative. Therefore for every n>=T,

    ||theta^n(v)|| >= ||sigma^n mu(v)|| / L_mu
                   = (delta n+beta)/L_mu,

where delta>0. This contradicts (2) at the constant first length ||u||
and proves the remaining implication. This argument does not require
the general IA_r(Z/3) aperiodicity theorem or a computation of the full
conjugacy stabilizer. Classical Whitehead reduction is used only for
effective normalization of the primitive input.

## Rank boundary, credits and novelty

The assertion is false in ambient rank two. Lee's example
u=a, v=a^2 b a^-1 b^-1 has bounded translation lengths under all
automorphisms of F(a,b), although v is not conjugate to a power of a.
It ceases to be bounded in F(a,b,c), as the proof above also detects.
Rank one is immediate and is outside the implementation's advertised
scope. Identity inputs are excluded from ratios.

Rank-two bounded translation equivalence and the example are prior work:
Donghi Lee, [arXiv:0802.0584](https://arxiv.org/abs/0802.0584), already
archived and discussed in
`research/notes/F38-bounded-scope-boundary.md`. The exact finite growth
calculation and graph argument above are included to make this restricted
classification reviewable without stronger imported structure theorems.
Searches for bounded translation equivalence with primitive words and
powers did not locate an explicit matching statement; this is not
evidence establishing novelty. General part (c) remains unresolved here.

The previously implemented stabilizer test already detects these negative
cases, and the common-cyclic-carrier positive branch covers the positives.
The contribution here is a uniform elementary classification with a
small explicit witness family, rather than a claimed increase in the
old classifier's decision coverage. Verification details and reproduction
records are in [the audit](primitive-power-audit.md).
