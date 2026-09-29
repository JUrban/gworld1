# H4 strengthening: infinite non-elementary inputs

29 September 2026. Extension of the same H4 candidate, not another
problem count. The argument also strengthens its finite-input size bound.
Independent specialist review and novelty checking remain outstanding.

**Claim.** Uniform polynomial-time conversion to an explicit Dehn
presentation is impossible even on finite presentations of infinite,
non-elementary virtually free groups, allowing arbitrary output generators.

The explicit-word and strict-shortening conventions are those of
`proof.md`. This argument allows torsion; it says nothing new about a
torsion-free restriction or compressed output.

## 1. The classical torsion-conjugacy bound

Let a Dehn presentation have r generators and longest relator length L.
Assume L>=1. Every conjugacy class of finite-order elements has a
representative of length less than L.

Choose a word w of shortest length in the conjugacy class of a nonidentity
torsion element. It is freely and cyclically reduced. If its length d
were at least L, a positive power w^e representing the identity would
contain a Dehn-shortenable segment u of length at most L<=d. This segment
is contained in a cyclic rotation of w, including when it crosses the
boundary between consecutive copies. Replacing u by the shorter complement
would give a shorter word in the same conjugacy class, a contradiction.
The identity has the empty representative. Therefore, writing T(G) for
the number of torsion conjugacy classes, including the identity,

    T(G) <= sum_(j=0)^(L-1) (2r)^j < (2r)^L.                 (1)

This is a **classical lemma**, not a discovery here: Michael Batty,
after Panagiotis Papasoglu, [*Notes on Hyperbolic and Automatic Groups*](https://www.math.ucdavis.edu/~kapovich/280-2020/hyplectures_papasoglu.pdf)
(21 October 2003), Theorem 3.27 and proof, p.29,
give precisely the conjugacy-minimal-word argument. It is stronger than
the previous automaton argument for the present family because only
torsion classes, rather than all elements, need short representatives.

For an explicit list of strict shortening rules, replace L by the largest
left-hand-side length. The same cyclic-word argument applies. For the
total explicit size m, both r and L are at most m, hence

    T(G) < (2m)^m.                                         (2)

No relationship to the input generators is assumed. If there are no
nonempty rules/relators, the group is free and has no nonidentity torsion;
that case cannot present the groups used below.

## 2. Many distinct classes in the short finite family

Use the already proved group

    K_n = C_M semidirect C_Q,  Q=2^n, M=2^Q-1,
    t x t^-1=x^2,

with its explicit presentation of size 4n+8 from `proof.md`, Section 2.
Conjugation on the normal cyclic subgroup <x> is exactly multiplication
by powers of two on Z/M. Its orbits are precisely the K_n-conjugacy
classes contained in <x>. They have size at most Q, so their number c_n
satisfies

    c_n >= M/Q > 2^(2^n-n-1).                              (3)

This counts orbits, not elements: x and x^2 are conjugate, and cannot be
used as separate class representatives. The action really has order Q:
for 0<j<Q, 0<2^j-1<M, so 2^j is not one modulo M.

For the bounded exact checks, Burnside's orbit formula gives

    c_n = (1/Q) sum_(j=0)^(Q-1) gcd(2^j-1,2^Q-1)
        = (1/Q) sum_(j=0)^(Q-1) (2^gcd(j,Q)-1)
        = [M + sum_(i=0)^(n-1) 2^(n-i-1)(2^(2^i)-1)]/Q.  (4)

The j=0 term is M. Only the elementary lower bound (3) is needed for
the theorem; formula (4) is not an additional hypothesis.

## 3. Infinite non-elementary hyperbolic inputs

Let

    H_n = K_n * <z>.

Add z as one free generator to the input presentation, with no new
relator. The explicit generator-letter size is 4n+9; the bit length
with binary generator indices is O(n log n).

The retraction H_n -> K_n killing z has free kernel with basis

    { k z k^-1 : k in K_n }.

One can see this directly by writing every word with trivial K_n-image
as a product of these conjugates, using cumulative K_n-prefixes.
A freely reduced product in the displayed symbols stays nontrivial
in free-product normal form: combine consecutive occurrences having
the same k; between distinct k values a nonidentity K_n syllable remains.
This proves freeness and the basis claim. The kernel has index |K_n|
and rank |K_n|>=6. Thus H_n is virtually free and hyperbolic, infinite,
and not virtually cyclic, hence non-elementary.

Two elements of a free factor K_n that are conjugate in K_n * <z>
are already conjugate in K_n. For completeness, strip the terminal
K_n syllable from a reduced conjugator. Unless the remaining conjugator
is empty, it ends in a nontrivial <z> syllable; its conjugation of a
nonidentity K_n element is reduced with syllables outside K_n and
therefore cannot lie in K_n. Identity is handled separately.
Consequently all c_n torsion conjugacy classes above remain distinct
in H_n. This is where the free product, rather than an arbitrary
overgroup, is essential.

## 4. Stronger output bound

For any Dehn presentation of H_n of size m_n, (2) and (3) imply

    m_n log_2(2m_n) > 2^n-n-1.                             (5)

For n>=2, if m_n<=2^n then log_2(2m_n)<=n+1. If m_n>2^n the
following weaker conclusion is immediate as well. In either case,

    m_n > (2^n-n-1)/(n+1).                                (6)

This is superpolynomial in the O(n log n) input bit length. Merely
writing any allowed output takes superpolynomial time. The same bound
holds for K_n itself, strengthening the earlier square-root exponential
bound without invalidating that original argument.

The two proofs use different counting objects. The old finite-group
automaton is necessarily acyclic. For infinite H_n that is false and
is not used: only the finite set of torsion conjugacy classes is bounded.

## Credit and limitations

The short family K_n and the original output-size candidate were derived
earlier in this run. The torsion-conjugacy lemma and free-product facts
are standard. The new development here is their combination to obtain
the stated strengthened bound and infinite-input restriction. No
established novelty is asserted. The prior finite-group suggestion
credited in `audit.md` remains credited.

No outside specialist review has occurred. Computations check selected
finite class counts and free kernels, not the universal theorem. Exact
artifacts, run results and any failures are documented in
`infinite-input-audit.md`.
