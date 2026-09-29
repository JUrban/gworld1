# B9: infinitely many special braids on five strands

Candidate result,29 September2026. The proof below gives countably infinitely
many special braids in every B_N with N>=5. It does not determine the
complete counts for N=3,4. Novelty and external specialist review remain
outstanding. See the [audit](infinite-family-audit.md).

Write s_i for the Artin generator sigma_i and S for the shift s_i->s_(i+1).
The operation is exactly the one in GroupWorld B9:

    a ▷ b = a S(b) s1 S(a)^-1.

A braid is special if it lies in the closure of1 under this operation.
Being special is considered in B_infinity; intermediate terms need not
remain on the same number of strands as the final braid.

**Theorem.** For every integer n>=3, the braid

    beta_n = s1^n s3^(n-2) s2^(1-n) s3^2 s4^-1
                         s2 s1 s3^(n-1) s4^(2-n) s2^-n       (1)

is special and lies in B5. The beta_n are pairwise distinct, and none lies
in the standard subgroup B4. Consequently

    |{special braids in B_N}| = aleph_0       for every N>=5.

## 1. Special terms with a useful cancellation

Define special braids by

    u0=1,    u1=1▷1=s1,
    u_(n+1)=u_n▷u_(n-1)       for n>=1.                       (2)

Induction gives

    u_n S(u_(n-1))=s1^n,
    u_n=s1^n S(u_(n-1))^-1       for n>=1.                    (3)

The base case is immediate. If the first identity holds at n, then(2)
gives u_(n+1)=s1^(n+1)S(u_n)^-1, establishing the next identity.

For n>=3 set

    q_n=u_(n-3),       A_n=s1^n s3^(n-2) s2^(1-n).

Expanding(3) three times gives

    u_n=s1^n s3^(n-2) S^3(q_n)^-1 s2^(1-n).

Every generator in S^3(q_n) has index at least4, so it commutes with s2.
Therefore

    u_n S^3(q_n)=A_n.                                       (4)

Only distant-generator commutations are used here. When n=3, q_n=1,
so the same formula includes the boundary case.

## 2. A special term whose high strands all cancel

Set

    v_n = 1 ▷ ((1 ▷ q_n) ▷ 1),
    beta_n = u_n ▷ v_n.                                     (5)

Every factor in these expressions is special by(2), so beta_n is special.
Expand the three operations in v_n directly:

    v_n = S^2(q_n) s2^2 s3^-1 S^3(q_n)^-1 s1.

Substituting this into the final operation gives

    beta_n = u_n S^3(q_n) s3^2 s4^-1 S^4(q_n)^-1
                                       s2 s1 S(u_n)^-1.

Every generator in S^4(q_n) has index at least5, so it commutes with
both s1 and s2. Move that factor past s2 s1 and apply(4):

    beta_n = A_n s3^2 s4^-1 s2 s1
                           (S(u_n) S^4(q_n))^-1
           = A_n s3^2 s4^-1 s2 s1 S(A_n)^-1.                 (6)

Since

    S(A_n)^-1=s3^(n-1) s4^(2-n) s2^-n,

equation(6) is exactly(1). It uses only s1,s2,s3,s4, and thus lies in
B5, independently of n. This is an identity of braids for every n, not
an inference from a bounded list of computed examples.

For n=5 it recovers the earlier29-letter height-six example. In general
the displayed representative has6n-1 letters and exponent sum3.

## 3. An integral matrix entry separates every parameter

Use the unreduced Burau representation at t=-1. It sends s_i to the
identity matrix except for the block on coordinates i,i+1

    T = [ 2 -1 ] = I+N,       N^2=0.
        [ 1  0 ]

These matrices satisfy the Artin relations. For every integer k, including
negative k,

    T^k=I+kN.                                               (7)

Faithfulness is not required: different matrix entries imply different
braids. Products of braid generators correspond to products of these
matrices in the displayed order.

The fifth row of the matrix of beta_n can be computed without expanding
the full product. It stays e5 through the first four blocks of(1).
After s4^-1 it is(0,0,0,-1,2). Multiplication by s2 s1 leaves it
unchanged. The last three blocks successively give

    after s3^(n-1): (0,0,1-n,n-2,2),
    after s4^(2-n): (0,0,1-n,-n^2+3n-2,n^2-2n+2),
    after s2^-n:   (0,n(n-1),1-n^2,-n^2+3n-2,n^2-2n+2).     (8)

Thus the(5,2) entry is n(n-1), strictly increasing for n>=3, proving
pairwise distinctness. Every standard B4 braid has fifth row e5 in this
representation, whereas n(n-1)!=0 here. Thus the minimum standard
strand support of every beta_n is exactly5.

The same matrices embed as an identity extension in dimension N for
N>=5, so the braids remain distinct there. Since a finitely generated
group is countable, an infinite subset of B_N is countably infinite.
This proves the theorem. □

## 4. Consequences and remaining scope

Only finitely many terms have height at most any fixed h. The infinite
family in B5 therefore has unbounded minimum expression height. This
strengthens the earlier counterexample to Dehornoy's survey Question3.19:
there is no bound on minimum term height depending only on the number
of strands, already at five strands.

The result concerns the standard inclusions of braid groups, not minimal
strand number of a knot closure or Markov equivalence. It concerns the
monogenic braid shelf in the source, not the different family also called
special in some work on positive braids and ordinal descents.

The construction gives no exhaustion argument for B3 or B4. Earlier finite
height enumerations remain only bounded counts. We therefore record one
partial candidate for GroupWorld B9, in the parameter range N>=5, rather
than asserting a full all-N counting formula.
