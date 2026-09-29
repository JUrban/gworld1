# MA7: an explicit finite noncommutative-ring construction

29 September 2026, during the active experiment. **Not counted as a new
answer to the website entry:** its short formulation already has prior
affirmative answers. The additional finite-ring construction below is an
internally checked argument, with novelty and intended ring conventions
unverified. No commutative-ring conclusion follows from it.

## Statement and scope

For each integer n>=3 there is a finite associative ring R with identity
and a matrix T in E_n(R) such that:

1. T is nonscalar modulo every proper two-sided ideal of R;
2. T is not ABA^-1B^-1 for any A,B in GL_n(R).

The construction uses a **noncommutative** ring. The ambient dimension n
is fixed: no assertion about commutators after stabilization is made.
The original MA7 says only “a ring” and “for some n.” The related
Kourovka 16.23 adds n>2 and the nonscalar condition. We satisfy those
two extra conditions, but make no claim that this resolves a formulation
in which all rings are implicitly required to be commutative.

## 1. The ring

Let k=F_3, m=2n^2+1, and V=k^(2m), with ordered basis e_1,...,e_(2m).
Set

    R = exterior(V) / (all terms of degree at least 3)
      = k + V + exterior^2(V).

Multiplication is inherited from the associative exterior algebra.
Equivalently,

    (a,v,z)(b,w,t) = (ab, aw+bv, at+bz+v wedge w).

This explicitly defines a finite associative unital ring. Its cardinality
is 3^(1+2m+binomial(2m,2)). The ideal J=V+exterior^2(V) satisfies J^3=0,
and R/J=k. An element is a unit precisely when its scalar part is nonzero:
for a nonzero scalar a, invert a+j by the finite geometric series.
The degree-two part is central and has square zero. The ring itself is
noncommutative, since e_1 e_2=-e_2 e_1 and 2 is nonzero in k.

Put

    z = 2 sum_(i=1)^m e_(2i-1) wedge e_(2i),
    D = diag(1+z,1,...,1),
    T = E_12(1) D.

The (1,2) entry of T is exactly 1. It remains nonzero modulo every
proper ideal, whereas a scalar matrix has zero off-diagonal entries.
This proves the required nonscalar condition, without having to classify
the ideals of R.

## 2. An elementary factorization

For each pair let u=1+e_(2i-1) and v=1+e_(2i). Their inverses are
1-e_(2i-1) and 1-e_(2i). Direct multiplication in the truncated ring gives

    u v u^-1 v^-1 = 1+2 e_(2i-1) e_(2i).

For any unit u in any associative unital ring, the embedded 2-by-2 matrix

    h(u) = diag(u,u^-1)
         = E_12(u) E_21(-u^-1) E_12(u)
           E_12(-1) E_21(1) E_12(-1)

is elementary. The order in the next identity matters:

    h(u) h(v) h(vu)^-1 = diag(u v u^-1 v^-1, 1).

The second diagonal entry is u^-1 v^-1 v u=1. The first is the displayed
unit commutator. Embed these identities in the first two coordinates of
n-by-n matrices. Multiplying over the m disjoint pairs gives D, since
products of degree-two terms vanish. Hence D and T belong to E_n(R).
This supplies 18m+1 elementary factors, with no appeal to stable K-theory.

## 3. The exterior-quotient obstruction

We use the following elementary linear-algebra fact. If W is a subspace
of V of dimension s and z belongs to W wedge V, the alternating matrix
of z has rank at most 2s. Indeed, after choosing a basis of W one can
write z=sum_(i=1)^s w_i wedge v_i. Each summand has matrix rank at most
two, so subadditivity of rank gives the bound. Also the kernel of

    exterior^2(V) -> exterior^2(V/W)

is exactly W wedge V, by extending a basis of W to a basis of V.
Our particular z has rank 2m, since its matrix has m nonsingular
2-by-2 alternating blocks. Therefore its image zbar in exterior^2(V/W)
is nonzero whenever dim W<m.

Suppose, for contradiction, that T=ABA^-1B^-1 in GL_n(R). Let W be
the span of the degree-one components of all entries of A and B.
There are 2n^2 entries, so dim W<=2n^2<m. The natural ring homomorphism

    pi: R -> Rbar = k + (V/W) + exterior^2(V/W)

kills those degree-one components. Consequently every entry of pi(A)
and pi(B) belongs to the commutative subring

    S = k + exterior^2(V/W).

These matrices are invertible over S, not just over Rbar. To see this,
write either one as A_0+N, where A_0 is its invertible constant matrix
and N has entries in the square-zero degree-two ideal. Its inverse is

    (I-A_0^-1 N) A_0^-1,

which has entries in S. The constant matrix is invertible because the
original A is invertible after reduction modulo J; likewise for B.

We may now take the **ordinary determinant over S**. A group commutator
in GL_n(S) has determinant 1. But

    pi(T) = E_12(1) diag(1+zbar,1,...,1)

has determinant 1+zbar, which differs from 1 by the rank argument.
This contradiction proves the claim. No determinant over the original
noncommutative ring is used.

For n=3, m=19: R has dimension 742 over F_3, the factorization has
343 transvections, and z has rank 38. Any two proposed 3-by-3 factors
have at most 18 independent degree-one components. Killing them leaves
z nonzero. The ring is described by its small basis/multiplication rule;
enumerating its 3^742 elements is unnecessary.

## 4. Status and prior material

Dennis--Vaserstein, *On a question of M. Newman on the number of
commutators*, Journal of Algebra 118 (1988), 150--161,
[doi:10.1016/0021-8693(88)90055-5](https://doi.org/10.1016/0021-8693(88)90055-5),
Theorem 1, already gives unbounded commutator width in SL_n(C[x]) for
each fixed n>=2. Since C[x] is Euclidean, SL_n(C[x])=E_n(C[x]). A
commutator in GL_n(C[x]) can also be realized in SL_n(C[x]): the two
determinants are nonzero constants, so multiplying each factor by a
suitable scalar nth root makes determinant one without changing the
commutator. Thus the website's unrestricted existential question is
already answered, even for commutative rings and n>=3. This observation
does not supply the nonscalar-modulo-every-ideal condition.

The exterior-algebra unit-group construction is standard prior material.
For an explicit readily accessible source, David Speyer's Math 594
[Problem Set Five, Problem 6 and its footnote](https://sites.lsa.umich.edu/speyer/wp-content/uploads/sites/1332/2024/08/PSet5-594.pdf)
uses exactly the truncated exterior ring and characterizes its unit
commutators. Our argument adds the fixed matrix-size quotient obstruction;
we have not established that this extension is new. The elementary
diagonal identity and bivector rank bound are also standard ingredients.

The finite checks and bibliographic access limits are in
`exterior-ring-audit.md`. They do not convert the construction into an
independently reviewed theorem or settle the commutative-ring version of
the stronger question. **No candidate tally is increased.**
