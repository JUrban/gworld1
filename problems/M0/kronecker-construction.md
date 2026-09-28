# M0: a terminating finite-field witness construction

28 September 2026, approximately 17:59–18:03 UTC.
This strengthens the existing M0 candidate and adds no result count.
The universal primitive-column argument and Bachmuth criterion remain
those of `proof.md`. The new ingredient here is an explicit finite-field
choice, replacing the earlier prototype's prescribed search cutoff.
No novelty claim is made for Kronecker substitution or polynomial factoring.

## A finite bound from the determinant

Normalize the input endomorphism by a free automorphism so its
abelianization is the identity. Its integer Laurent Fox determinant
f(X_1,...,X_n) has f(1,...,1)=1. A unit is detected directly. Otherwise
f has at least two nonzero monomials. Write its finite support as E.

Put

    B = max(2, 1 + max_i(max_{e in E} e_i - min_{e in E} e_i)),
    w_i = B^(i-1),
    m = min_{e in E} sum_i w_i e_i,
    g(T) = T^(-m) f(T,T^B,...,T^(B^(n-1))).

The exponents sum_i w_i e_i are distinct: subtract the coordinatewise
minima and apply uniqueness of base-B expansion, since each coordinate
then lies between 0 and B-1. Thus g is a nonconstant integer polynomial
with nonzero constant coefficient a_0, nonzero leading coefficient a_D,
degree D >= 1, and g(1)=1.

Choose the least prime p not dividing a_0*a_D. This search terminates.
More explicitly, some prime divisor of |a_0*a_D|+1 does not divide
a_0*a_D, so p <= |a_0*a_D|+1. Reduction modulo p preserves degree D
and the nonzero constant term. Factor it over F_p and choose any monic
irreducible factor h. Set

    K = F_p[T]/(h),  t = T mod h,  chi(X_i)=t^(w_i).

Then t is neither 0 nor 1: these cannot be roots of g. Moreover
K=F_p(t), f(chi)=0 and

    |K| = p^(deg h) <= p^D <= (|a_0*a_D|+1)^D.

This is a concrete, computable bound, with no claim that it is small.
The group character need not have image equal to K^*: generating K as
a field is sufficient for the primitive-column argument.

## An explicit character basis

Because w_1=1, discrete logarithms are unnecessary. A free basis is

    alpha(x_i) = x_(i+1) x_1^(-w_(i+1))  (1 <= i < n),
    alpha(x_n) = x_1.

The inverse sends x_1 to x_n and x_j to x_(j-1) x_n^(w_j) for j>=2.
Direct free reduction verifies both compositions. Its character is
(1,...,1,t). Conjugate the normalized endomorphism by this basis change;
its singular Fox matrix has a nonzero kernel vector with last coordinate
zero, by the Fox identity and t!=1.

The existing proof lifts elementary matrices on the first n-1
coordinates to actual free automorphisms. Here their field coefficients
are already represented by polynomials in t of degree below deg h, so
their Nielsen lifts use those coefficients directly. The result is an
explicit free basis, an inverse free basis, and a primitive first basis
word whose image has a zero Fox column. Transfer the character back
through the initial abelianization normalization as in
`constructor-audit.md`.

For nonunimodular abelianization, trial division finds a prime divisor
of the determinant, or p=2 when it is zero. The earlier integral
primitive-vector lift then supplies the witness. Rank one is included;
rank zero is the trivial theorem case and is omitted from the interface.

Every stage is a finite algorithm on the given input. Word expansion,
polynomial degree and field size can nevertheless be very large. A
resource-limited execution can time out without deciding an input.

## Implementation and evidence

`scripts/m0_kronecker_witness.py` implements this route. It uses exact
trial division for prime choices, deterministic Berlekamp factorization,
and verifies the chosen factor's irreducibility and divisibility.
The earlier bounded constructor remains available unchanged.

`scripts/check_m0_kronecker.py` has twelve deterministic inputs in ranks
one through four. Nine give nonautomorphism witnesses and three give
exact unit determinants. Cases include a prime-eleven abelianization,
cubic extension fields, a negative Laurent exponent, endpoint
coefficients excluding primes two and three, and independent domain
and range basis changes. Fields of orders 2,4,5,8,11 occur; the longest
basis word has length 28. Four additional polynomial cases exercise
the substitution lemma; these are supporting arithmetic checks only.

The final Python run `m0-kronecker-v2` passed in 0.42 seconds.
The first run also passed, but used SymPy's default factorizer.
Its exact constructor and output were retained when the implementation
was changed to explicitly deterministic Berlekamp factorization.
No random seed was set for that initial factorization; its potentially
randomized backend is not the terminating implementation claimed here.
The final JSON and GAP certificate files are byte-identical to that
first output.

`scripts/check_m0_kronecker_gap.g` reuses the earlier independent GAP
certificate arithmetic. It verifies all nine witnesses using affine
matrices over GAP fields and both free-basis inverse compositions; it
checks all three positive determinants symbolically. The run
`m0-kronecker-gap-v1` passed in 1.88 seconds with empty stderr. Because
the final certificate bytes are unchanged, this check also verifies
the final output. It is independent of Python arithmetic, not an
additional independent human review.

All runs requested one core and 8 GB, with 180-second timeouts.
Certificates and a hash manifest are in
`research/certificates/M0-Kronecker/`. To run on another input, wrap
the following command in the recorded runner:

    .venv/bin/python scripts/m0_kronecker_witness.py input.json

No external specialist review or completed novelty audit is claimed.
