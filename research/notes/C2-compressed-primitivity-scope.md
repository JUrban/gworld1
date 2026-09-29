# C2: compressed primitivity is not arbitrary orbit comparison

29 September 2026. Scope audit and unsuccessful extension lead; no new
candidate answer.

The full original complexity page, C2 source fragment, background and
rendered paragraph were inspected. C2 asks whether, for arbitrary words
u,v in a fixed finite-rank free group, testing existence of an
automorphism taking u to v is in NP, with ordinary word length as input
size. Its background points to F25(a), not just primitivity testing.

Ilya Kapovich, *Compressed primitivity problem in free groups*,
[arXiv:2607.21499v1](https://arxiv.org/abs/2607.21499v1), 23 July 2026,
proves NP membership for compressed primitivity in fixed rank, polynomial
time in rank two, and polynomial-time recognition of compressed
automorphic minimality. Theorem 5.3 certifies primitivity by adjoining
s-1 differences of prefixes of a cyclically reduced word of support
size s and checking that the resulting subgroup is the support free
group. Sections 5-6 use Puder's quotient criterion and Linton's
compressed subgroup-membership algorithm. Read the introduction and
these arguments; printed pages 2 and 16 were viewed. The source PDF is
archived with SHA-256
`4a4d719ccad31a38a33097107c5341e0dfcd05af449f530246a5b51be3754c01`.
The deeper imported algorithms were not independently audited.

This supplies no certificate for the general C2 pair. For instance,
u=v=[a,b] is a yes-instance of C2, while adjoining just one element to
<[a,b]> cannot generate F(a,b): its abelianized image has rank at most
one. Thus applying the same primitivity endpoint condition to arbitrary
orbit comparisons would reject a valid instance. This is a failure of
that proposed extension, not evidence against NP membership.

Nor does efficient evaluation of a supplied automorphism sequence give
a polynomial bound on the sequence needed to connect arbitrary input
words. A polynomial-size general certificate, or an alternative complete
certificate construction, remains missing here. The paper's compressed
input has a different size measure, so its descent examples must not be
reported as lower bounds for the ordinary-input C2 problem. Keep C2 in
the unresolved portfolio.
