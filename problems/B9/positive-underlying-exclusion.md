# B9: exclude every positive underlying second braid beyond B2

30 September 2026, within the original experiment. This extends the
positive-v half of [the three-strand exclusion](three-strand-underlying-exclusion.md)
to all strand numbers. It concerns the parameter A=I1(u) S(I1(v)) of
total exponent two. It does not exhaust the special exponent-two
braids in B4, whose parameters may also have larger total exponents.

Use s_i=sigma_i, tau_j=s_j ... s_1, I1(w)=w s_1 S(w)^-1, and the
standard strand inclusions. Permutations act on positive integers,
with the rightmost factor applied first.

**Proposition.** For every q>=3, put v=tau_(q-1). For every special
braid u,

    I1(u) S(I1(v)) does not belong to B3.

Since the positive special braids are exactly the tau_j, this excludes
every positive special underlying v of at least three strands.

## 1. Two credited permutation restrictions

For a special braid u with permutation f, the earlier source facts give

    epsilon(u) = nu(f) = #{j : f(j+1)=j},
    f^-1(1) is either 1 or 2.                              (1)

The first fact and the strand-power identity were already used in the
[small-strand proof](small-strand-proof.md). The second is Dehornoy's
Proposition 4.9 in *Strange Questions About Braids*. For clarity, the
needed small-class assertion also has the following direct proof in
our conventions. For permutations f,g put h=f S(g) s_1 S(f)^-1.
Then

    h^-1(1) = S(f) s_1 S(g)^-1(f^-1(1)).

If f^-1(1)=1, the result is 2. If f^-1(1)=2, it is 1 or 2 according
as g^-1(1) is 1 or 2. Thus the condition is closed under the shelf
operation and holds at its identity generator. Induction on a special
term proves the required assertion. No description of all special
permutations is assumed.

## 2. A universal permutation calculation

Suppose A=I1(u) S(I1(v)) belongs to B3. The existing support argument
gives m(u)=q+1. Let f=pi(u) be a permutation of {1,...,q+1}, extended
by the identity, and let a=pi(A). Since epsilon(A)=2, a is an even
permutation of {1,2,3}. Also

    pi(I1(v))=(q q+1).

Put l=(q+1 q+2). The exact equation for pi(A) is equivalently

    f s_1 = a l S(f).                                    (2)

Evaluating at 1 and 2 yields

    f(2)=a(1),       f(1)=a(l(f(1)+1)).                    (3)

At i>=3, equation (2) gives the recurrence

    f(i)=a(l(f(i-1)+1)).                                 (4)

By (1), either f(1)=1 or f(2)=1. We examine both cases.

If f(1)=1, then q>=3 and (3) give a(2)=1. The only even permutation
of three positions with that value is a=(3,1,2) in image-list notation.
Thus f(2)=3. Let k be the preimage of 2 under f. Then 3<=k<=q+1.
Applying (4) at k, and using a^-1(2)=3 and l(3)=3, gives

    f(k-1)+1=3,       hence f(k-1)=2=f(k).

This contradicts injectivity. The use of l(3)=3 is precisely where
q>=3 matters; the valid q=2 examples are not discarded.

Therefore f(2)=1. Equation (3) gives a(1)=1, so a is the identity.
The second equation in (3) becomes

    f(1)=l(f(1)+1).

For 1<=f(1)<=q+1 its sole solution is f(1)=q+1. Starting from f(2)=1,
recurrence (4) now gives f(i)=i-1 for every 2<=i<=q+1: throughout
these steps the argument of l is at most q, where l fixes it. Thus

    a=id,       f=(q+1,1,2,...,q)=pi(tau_q).                (5)

This argument applies to every integer q>=3, not only to the finite
range in the check records below.

## 3. The permutation forces an actual braid, then gives an obstruction

Equation (5) has nu(f)=q. By (1), epsilon(u)=q. A special braid in
B_(q+1) with that maximal exponent is tau_q itself, by the credited
strand-power identity. Consequently the only possible actual pair is

    u=tau_q,       v=tau_(q-1).

Put c=I1(v). Expanding the parameter as in the previous reduction,

    A=u s_1 S(u^-1 c),

shows that A in B3 would imply u^-1 c in B_q. Indeed u and A belong
to B_(q+1), and the shifted-parabolic intersection removes one strand.

In the (q+1)-dimensional unreduced Burau representation at -1, every
element of B_q fixes the last coordinate vector e_(q+1). Hence the
last columns of rho(u) and rho(c) would agree. They do not.

The generator block is [[2,-1],[1,0]], with inverse [[0,1],[-1,2]].
Since all generators to the right of s_q in tau_q fix e_(q+1),

    rho(u)e_(q+1)=-e_q,

whose first coordinate is zero. On the other hand,

    c=s_(q-1) ... s_2 s_1^2 s_2^-1 ... s_q^-1.

The rightmost inverse string sends e_(q+1) to

    e_2 + 2e_3 + ... + 2e_(q+1).

Applying s_1^2 gives first coordinate -2. Every remaining generator
s_2,...,s_(q-1) fixes that coordinate, so

    (rho(c)e_(q+1))_1=-2.

The unequal columns contradict u^-1 c in B_q and prove the proposition.
The full last column of rho(c) is (-2,-4,...,-4,-1,2), with q-2 entries
equal to -4; the proof only needs its first entry. Faithfulness of
Burau is neither assumed nor needed.

## 4. Consequence and checks

The only parameters A=I1(u) S(I1(v)) in B3 with **positive special v**
are therefore the already known cases with v=1 or s_1. Combining this
with the separate exclusion of the nonpositive three-strand v, any
additional terminal parameter of total exponent two must have

    v nonpositive,       m(v)>=4,       m(u)=m(v)+1>=5.

This condition leaves infinitely many possible inputs. Parameters of
total exponent at least three are outside this reduction altogether.
B9 remains partial and the whole/partial/established-novel tally is
unchanged.

The [Python checker](../../scripts/check_b9_positive_underlying.py) reconstructs
every possible permutation from a and f(1), using (3)--(4), for
q=3,...,64. It checks the full equation (2), not just the recurrence,
and finds exactly the predicted survivor satisfying the small-class
condition. Dropping that condition leaves a second permutation
(q+1,2,1,3,...,q), with preimage of 1 equal to 3; this checks the
necessity of that proof ingredient. Exact vector actions check both
last-column formulas in that same finite range.

The [GAP checker](../../scripts/check_b9_positive_underlying.g) independently
reconstructs the permutations for q=3,...,24 and uses full native
rational matrix multiplication for q=3,...,12. It reads no Python
certificate. Both implementations verify the actual valid q=2 boundary
(u,v)=(s_1^2 s_2^-1,s_1), and the false permutation-only positive at
q=3 using faithful free-group actions. These finite checks verify
interfaces and examples; the unbounded conclusion is the written
argument in Sections 2--3, not an extrapolation.

Both recorded jobs passed with empty stderr: Python in 0.169 seconds,
GAP in 1.775 seconds. Each reserved one CPU and 2 GB, with maximum
overlap two CPUs/4 GB. Exact data, dependency identities, source and
terminal logs are bound by the
[manifest](../../research/certificates/B9-positive-underlying/manifest-v1.json).
No earlier successful search or mathematical suite was rerun.

The source statement and rendering were checked in the immediately
preceding three-strand supplement. Proposition 4.9 was newly reread
in the retained primary-source text; the related survey statement was
also inspected online. The small-class assertion, exponent statistic,
positive-special classification and maximal-exponent identity are
credited prior facts from Dehornoy's
[*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf).
No new primary-page rendering, full-paper review, specialist acceptance
or novelty determination is asserted here.
