# F38(c): exact finite length envelopes

29 September 2026, approximately 08:52–09:12 UTC. Supplementary reduction
and implementation; **not a decision of bounded translation equivalence**.
The full original F38 paragraph and background were read again and its
actual rendered statement was viewed. We retain the quantifier over
automorphisms of the specified ambient free group.

## Statement and scope

Let u,v be nonidentity elements of F_r, r>=2, and write ||w|| for cyclic
length in a fixed free basis. Define

    E_(u,v)(N) = sup { ||phi(v)|| : phi in Aut(F_r), ||phi(u)|| <= N }.

Below the minimum length of the automorphic orbit of u the set is empty;
the implementation records those entries as `None`, not as positive
bounds. Put H_u=Stab_Out(F_r)([u]), for the oriented conjugacy class.
The following properties are equivalent:

1. E_(u,v)(N) is finite for every nonempty level N.
2. H_u has a finite orbit on [v].
3. There are effectively computable integers m>=1 and B>=1 such that

       ||phi(v)|| <= B * 2^(||phi(u)||-m)                 (1)

   for every automorphism phi; here m is the minimum cyclic length of u.

These properties are decidable by the existing stabilizer procedure.
When they hold, every finite prefix of E is exactly computable. The
original one-sided *linear* comparison is the stronger condition
E_(u,v)(N)=O(N). F38(c) requires linear comparison in both directions.
No argument below decides that additional condition.

## Finite fibers and the decision

Suppose E is finite. Restrict the defining automorphisms to H_u. Their
images of v have bounded length at the fixed level ||u||, hence belong
to a finite set of conjugacy classes. Conversely, suppose H_u[v] has
finite size M. For any class [w] in the automorphic orbit of [u], choose
psi with psi[u]=[w]. All automorphisms taking [u] to [w] are psi H_u,
so the possible second classes are exactly psi(H_u[v]). They number M.
Only finitely many classes [w] have length at most N. This proves the
equivalence of the first two assertions and finiteness of the pair graph
used below. The converse from (1) to finiteness is immediate.

Finite generation of H_u by the Whitehead minimum graph, and the exact
finite-orbit test using Handel–Mosher aperiodicity in IA_r(Z/3), are
imported as in [the stabilizer note](F38-stabilizer-obstruction.md).
If the test fails it returns theta in H_u intersect IA_r(Z/3) moving
[v]. The same aperiodicity theorem implies that all [theta^n(v)] are
distinct. Their lengths tend to infinity, so there is no finite-valued
global envelope at all. The finite tests in this note do not reprove
that imported theorem or Whitehead peak reduction.

## Exact finite algorithm

Use length-reducing Whitehead moves on u, applying each simultaneously
to v. This gives an automorphism mu and a pair (u_0,v_0) with
||u_0||=m minimal. For N>=m explore the graph whose vertices are ordered
pairs of oriented conjugacy classes and whose edges apply one Whitehead
automorphism simultaneously to both coordinates. Keep precisely those
edges whose resulting first coordinate has length at most N. Start at
([u_0],[v_0]). Include all signed permutations and all Whitehead moves
of the second kind, with inverses.

The graph is finite by the fiber argument. It contains exactly the
simultaneous orbit pairs whose first length is at most N. For the
nontrivial containment, apply the full single-word peak-reduction
factorization to the actual automorphism taking the initial pair to the
desired pair, modulo inner automorphisms. Its first-word endpoints have
lengths m and at most N, so the factorization can have every intermediate
first length at most N. Inner automorphisms have no effect on either
conjugacy coordinate. It is important here to factor the *given*
automorphism, rather than merely find some automorphism between the
first-word endpoints: the latter would not establish the second
coordinate assertion.

Breadth-first search therefore terminates and the maximum second length
over vertices of first length at most k is exactly E_(u,v)(k), k<=N.
The algorithm retains all vertices, edge labels, and a predecessor tree
as a finite certificate. An optional resource guard reports
`incomplete_resource_guard`; it never turns a truncated graph into an
exact value. There is no default mathematical cutoff.

## The exponential bound

First compute B=E_(u,v)(m) using the minimum pair graph. A Whitehead
automorphism changes cyclic length by a factor of at most two in either
direction. For signed permutations this is immediate. For a move of
the second kind, the usual cyclic Whitehead-graph formula is

    ||alpha(w)|| - ||w|| = cut(S,S^c) - frequency(multiplier).

There are ||w|| cyclic turns, so the cut is at most ||w||; this gives
||alpha(w)||<=2||w||. The inverse is also a Whitehead move, giving the
reverse inequality. This assertion concerns cyclic length: individual
basis images of a conjugating Whitehead move can have ordinary length
three. The formula and conventions are also in the archived Lee
[math/0311410v3](https://arxiv.org/pdf/math/0311410v3), Section 2.

Now take any phi. A sequence of strictly reducing Whitehead moves takes
phi(u), of length L, to a minimum word in at most L-m steps. Apply the
same sequence to phi(v). Its final length is at most B. Undoing the
sequence multiplies cyclic length by at most two at each step, proving
(1). This is an effective exponential estimate, not a linear estimate.

Two finite-valued envelopes, one in each direction, are therefore
equivalent to commensurability of H_u and H_v, precisely the existing
necessary condition. This reformulation leaves open whether or when
both exact envelopes have linear growth.

## Implementation and bounded audit

`scripts/f38_length_envelope.py` exposes
`length_envelope(rank,u,v,bound,max_states=None)`. Words use signed
integer basis letters, reduced cyclically and canonicalized by rotation;
inversion is not identified. The eight controls comprise five finite
graphs, two failures of the stabilizer condition, and one empty level:

| Ambient rank and pair | Bound | Envelope, beginning at N=0 | Pair vertices |
| --- | ---: | --- | ---: |
| 2: a, a^2 b a^-1 b^-1 | 5 | empty, 5, 6, 7, 8, 9 | 80 |
| 2: a, [a,b] | 5 | empty, 4, 4, 4, 4, 4 | 80 |
| 2: a^2, a^3 | 6 | empty, empty, 3, 3, 6, 6, 9 | 16 |
| 3: a, a^2 | 3 | empty, 2, 4, 6 | 58 |
| 2: (ab)^2, (ab)^3 | 6 | empty, empty, 3, 3, 6, 6, 9 | 16 |

The rank-two Lee pair is known to be boundedly equivalent. Its rank-three
version fails. The reversed commutator/a pair fails, although the table
shows a finite envelope in the other direction. The below-minimum test
uses a^2,a^3 with bound 1. These distinctions are intentional controls.

The independent GAP script reconstructs the complete Whitehead map set
from all signed permutations and all admissible multiplier/subset choices.
It checks map inverses, simultaneous input normalization, all finite-graph
edges and their closure, reachability, maxima, and the exponential bounds
using native free-group operations. It also checks both negative witnesses,
including their level-three homology matrices and fixed/moved classes.
Totals are five graphs, 9,226 directed edges, 23,188 exact substitutions,
and two negative witnesses. This proves correctness of these finite
certificates; completeness of the general method still imports the
theorems identified above.

Recorded runs:

- `results/f38-length-envelope-v1`: 0.370344 seconds.
- `results/f38-length-envelope-gap-v1`: 2.026667 seconds.

Both have actual exit status zero, empty stderr and the required success
marker. Each reserved one core and 6 GB; neither reached a resource guard.
The certificate directory contains generated data, source snapshots and
a hash manifest. Exact commands are in the process records.

No new problem or named-subpart candidate is counted. Novelty of this
auxiliary reduction has not been established; the prior theorems retain
their credits. General F38(c) remains unresolved here.
