# H4: an output-size obstruction to polynomial-time Dehn conversion

Candidate negative answer, 28 September 2026. The first argument was
recorded at approximately 20:59--21:01 UTC in
`research/notes/H4-output-size-lead.md`. This is a uniform complexity
statement for explicit finite presentations. Independent specialist
review and novelty assessment remain outstanding; see `audit.md`.

**Theorem.** There is no algorithm which, on every explicit finite
presentation of a hyperbolic group, outputs an explicit finite Dehn
presentation of an isomorphic group in time polynomial in the input
length. This holds even when the inputs present finite groups and the
algorithm may choose a different output generating set.

Words are written as strings of generator letters and their inverses.
Generator indices may be binary encoded; the input family below has
bit length O(n log n). A compressed grammar, program for enumerating
relators, or unevaluated formula for a presentation is a different output
specification and is not covered by the theorem.

The Dehn convention is the usual strictly length-decreasing one: every
nonempty freely reduced identity word contains more than half of a cyclic
conjugate of a defining relator or its inverse. It can therefore be
shortened using the complementary part. The equivalent formulation by
finite lists of shortening rules is given in Bridson, Definition 1.4,
printed p.128, and Ciobanu--Elder, Lemma 13, p.110:7; exact sources are
listed in the audit. The proof below uses only this defining property.

## 1. A size bound for a Dehn presentation of a finite group

Let P=<a_1,...,a_r | R> be a Dehn presentation of a finite nontrivial
group G. Delete empty relators and set

    m = r + sum_(rho in R) |rho|.

Define a finite forbidden set B of words over the 2r signed generator
letters as follows:

- Include every free-cancellation pair a_i a_i^-1 and a_i^-1 a_i.
- For each relator of length L, each of its L cyclic rotations, and
  each rotation of its inverse, include the initial segment of length
  floor(L/2)+1.

Any word containing a forbidden factor can be shortened without changing
its group value. Conversely the Dehn property implies that a nonempty
identity word cannot avoid B. Every geodesic representative avoids B.
The language K of words avoiding B is closed under taking factors.

There is a deterministic finite automaton for K whose nonfailure states
are the empty word and all proper prefixes of words in B. When a letter
is appended, reject if a forbidden word has just ended; otherwise keep
the longest suffix which is a proper prefix of a forbidden word. This
is sufficient because any future first forbidden occurrence must extend
such a suffix. All reachable nonfailure states are accepting.

The number s of nonfailure states is at most

    s <= 1 + sum_(b in B)(|b|-1)
      <= 1 + 2r + sum_(rho in R) 2|rho| floor(|rho|/2)
      <= 1 + 2r + sum_(rho in R) |rho|^2
      <= (m+1)^2.                                      (1)

There is no reachable directed cycle among these states. Otherwise,
letting u be a path to the cycle and v its nonempty label, all words
u v^k would belong to K. Because G is finite, the group element
represented by v has a positive finite order e. Factor-closure would
then put the nonempty identity word v^e in K, contrary to the Dehn
property. Thus every accepted path has length at most s-1.

Every element of G has a geodesic word, which belongs to K. Consequently

    |G| <= sum_(j=0)^(s-1) (2r)^j
        <= (2r)^s <= (2m)^((m+1)^2).                    (2)

The bound depends only on the explicit output size. No relationship
between input and output generators was assumed. An output given instead
as an explicit list of shortening rules satisfies the same conclusion:
use its left-hand sides as forbidden words, giving an even smaller
prefix-state bound in terms of their total length.

## 2. Short presentations of very large finite groups

For each n>=1 use generators x,t_0,...,t_n and relations

    t_i = t_(i-1)^2       (1<=i<=n),
    t_n = 1,
    t_0 x t_0^-1 = x^2.                                 (3)

There are n+2 generators, n length-three relators, one length-one relator
and one length-five relator. Hence the explicit generator-letter size
is exactly 4n+8. Writing generator indices in binary gives O(n log n)
bits. The powers in (3) are only squares, so this input estimate does
not use compressed words.

Eliminating t_1,...,t_n gives

    G_n = <x,t | t^Q=1, t x t^-1=x^2>,  Q=2^n.

Put M=2^Q-1. Iterated conjugation gives
t^Q x t^-Q=x^(2^Q), and therefore x^M=1. Since M is odd, multiplication
by 2 is invertible modulo the order of x. Both t and t^-1 therefore
normalize <x>. The group <x> has order at most M and the quotient by
it has order at most Q, proving |G_n|<=MQ.

For the reverse inequality take the semidirect product

    H_n = C_M semidirect C_Q,

where the generator of C_Q acts on C_M by x -> x^2. This action is
well-defined: 2 is a unit modulo M and 2^Q=1 modulo M. This group has
order MQ and satisfies (3), with t_i=t^(2^i). The corresponding map
G_n onto H_n is surjective. Thus

    G_n is isomorphic to H_n,
    |G_n|=2^n(2^(2^n)-1).                               (4)

In particular every input group is finite. Its Cayley graph has finite
diameter, hence is delta-hyperbolic for some finite delta. So every
presentation in the family satisfies H4's promise.

## 3. The output cannot have polynomial size

Let m_n be the generator-letter size of any Dehn presentation of G_n.
Combining (2) and (4) gives

    (m_n+1)^2 log_2(2m_n) >= log_2 |G_n| > 2^n-1.        (5)

If m_n<=2^n, then log_2(2m_n)<=n+1, and (5) implies

    m_n > sqrt((2^n-1)/(n+1)) - 1.                      (6)

If m_n>2^n, the same lower bound is immediate. Thus every possible
explicit output has exponential size in n up to a polynomial factor.
It cannot be polynomial in the O(n log n) input bit length. An algorithm
must spend at least the time required to write its explicit output,
proving the theorem.

The later [infinite-input extension](infinite-input-proof.md) strengthens
the size bound to m_n>(2^n-n-1)/(n+1) for n>=2 and also covers infinite,
non-elementary virtually free inputs. It uses the classical bound on
short representatives of torsion conjugacy classes. The original proof
above remains valid and is retained.

This is an unconditional size obstruction. It uses no unproved separation
such as P != NP, no assumption on how the algorithm searches, and no
requirement that it preserve generators or append relators to the input.
It does not preclude algorithms with larger running time or short
compressed descriptions of a Dehn presentation.

## 4. Credit and evidence

Finite groups as a possible source of Dehn-presentation lower bounds
were suggested in a 2012 MathOverflow discussion by user6976, with a
question by Jeff Burdges and related comments by Misha. That prior
observation is credited; the finite-group strategy is not claimed as
new. The explicit automaton bound and the family (3) are the argument
developed here. A matching previous result has not been found in the
bounded searches so far, which is not a novelty guarantee.

The written argument is valid for arbitrary n independently of the
bounded checks. The accompanying code checks the automaton construction,
positive and negative controls, and explicit finite models; GAP also
checks small presentations independently. Details and all qualifications
are in `audit.md`.
