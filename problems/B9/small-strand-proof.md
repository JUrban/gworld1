# B9: the small-strand cases and the one remaining sector

29 September 2026. This supplements the [infinite-family candidate](infinite-family-proof.md).
The counts in B1, B2 and B3 are respectively **1, 2 and 4**. These are
direct consequences of Dehornoy's existing structural results; no novelty
is asserted for them. In B4, only exponent sum two remains unclassified.
Thus the combined candidate still covers a proper part of GroupWorld B9.

Use the standard Artin generators s_i, shift S, and shelf operation

    a ▷ b = a S(b) s1 S(a)^-1.

Let C be the closure of 1 under ▷ in B_infinity. Write epsilon for exponent
sum and tau_p=s_p ... s1, with tau_0=1. All strand groups below use the
standard inclusions. Intermediate special terms may have more strands than
their final value.

## 1. Structural facts and their provenance

For a permutation f of the positive integers with finite support, put

    D(f)={j>=1 : f(j+1)=j},       nu(f)=|D(f)|.

Permutations act as functions, with the rightmost factor applied first.
Direct calculation gives

    D(f ▷ g) = f({1} union {j+1 : j in D(g)}).

The two sets inside the union are disjoint, so nu(f▷g)=nu(g)+1.
Also epsilon(a▷b)=epsilon(b)+1. Since both quantities start at zero,

    epsilon(b)=nu(pi(b))       for b in C.

Consequently, for b in C intersect B_N,

    0 <= epsilon(b) <= N-1.                                  (1)

Moreover epsilon(b)=0 implies b=1: every nonleaf special term has positive
exponent sum. These facts appear in Dehornoy, *Strange Questions About
Braids*, Lemma 4.3 and Proposition 5.8. The set formula above includes the
explicit shift of D(g); it is derived directly from the operation.

Define

    I_p(A)=A tau_p S(A)^-1.

The strand-support observation in the proof of Dehornoy's Proposition 5.9
is the following, for N>=2:

    If 0<=p<=N-1 and I_p(A) belongs to B_N, then A belongs to B_(N-1). (2)

Here is also the usual subgroup-intersection argument for (2). Suppose
the smallest m with A in B_m satisfies m>=N. Then tau_p belongs to B_m,
so the equation S(A)=I_p(A)^-1 A tau_p implies S(A) in B_m. But the
standard parabolic subgroups have intersection

    S(B_m) intersect B_m = S(B_(m-1)).

This is the standard consecutive-strand intersection property: the common
braids are supported on strands 2,...,m. Hence A belongs to B_(m-1), a
contradiction. The source gives the alternative proof using a word definite
in its highest generator. We use this established braid-group support
fact, not a conclusion from finite action tests. The converse of (2) is
immediate when p<=N-1.

Following the right branch of a special term of exponent sum p>0 gives

    b=a1 ▷ (a2 ▷ (... (ap ▷ 1)...)),       all ai special.

Expansion of the operation yields

    b=I_p(A),       A=a1 S(a2) ... S^(p-1)(ap).                (3)

In particular, when epsilon(b)=1, b=I_1(a)=a▷1 for a special a.
Equation (2) then gives

    b in C intersect B_N, epsilon(b)=1
        iff b=a▷1 for a in C intersect B_(N-1).               (4)

For fixed p, Dehornoy's Lemma 5.6 gives

    I_p(A)=I_p(A') iff A^-1 A' belongs to B_p.                 (5)

Thus I_1 is injective, since B1 is trivial.

For completeness, the right-power identity is also a prior result, not
a new claim here. Define b^[1]=b and b^[k+1]=b▷b^[k]. Direct expansion
of I_p shows

    I_p(A)^[k] = I_(p+k-1)(A)       for k>=1.                 (6)

In the induction, shifted A factors commute with s1 once shifted twice;
the remaining identity is h tau_r=tau_r S(h) for h in B_r.
Combining (2), (3) and (6) gives Dehornoy's Proposition 5.9:

    b^[N-epsilon(b)] = tau_(N-1)       for b in C intersect B_N. (7)

The case b=1 follows directly from 1^[k]=tau_(k-1). In particular the
only special braid in B_N of exponent sum N-1 is tau_(N-1).

## 2. Complete counts through three strands

B1 is trivial. For B2, (1) permits only exponent sums zero and one;
these give 1 and s1 respectively. For B3:

- Exponent sum zero gives 1.
- Exponent sum one, by (4), gives 1▷1=s1 and s1▷1=s1^2 s2^-1.
- Exponent sum two, by (7), gives tau_2=s2 s1.

These four braids are distinct. Exponent sum separates all except the
two exponent-one braids, which are distinct by the injectivity of I_1.
Thus

    C intersect B3 = {1, s1, s1^2 s2^-1, s2 s1}.              (8)

This is an exhaustion argument using prior structural theorems. It does
not infer exhaustion from the earlier finite-height enumeration.

## 3. Exactly what remains in four strands

In B4, exponent sum zero contributes 1 and exponent sum three contributes
tau_3=s3 s2 s1. By (4) and (8), exponent sum one contributes exactly
the four braids

    a▷1,       a in {1, s1, s1^2 s2^-1, s2 s1}.              (9)

They are distinct by (5). The sole remaining sector is epsilon=2.
Its special braids are exactly

    I_2(A), where A=a S(c) belongs to B3 and a,c are special. (10)

Indeed, any exponent-two special braid has the form a▷(c▷1), and
expands as I_2(a S(c)); conversely each such expression is special and
has four-strand support. By (5), distinct braids in (10) correspond to
distinct right cosets A B2 in B3 with a representative of this form.

There are at least four such cosets, represented by

    A = 1, s2, s1 s2, s1^2 s2^-1,

with special pairs (a,c) respectively

    (1,1), (1,s1), (s1,s1), (s1^2 s2^-1,1).

Their images are

    s2 s1,
    s2^2 s3^-1 s1,
    s1 s2^2 s3^-1 s1 s2^-1,
    s1^3 s3 s2^-2.                                          (11)

Exact faithful actions distinguish these four. They are the same four
examples already displayed in Dehornoy's discussion at the end of
Section 5.3. The source explicitly does not prove their exhaustion.
We likewise **do not claim that (11) exhausts (10)**. The known lower
bound is ten special braids in B4; an exact count is still outstanding.

All braids in (10) satisfy b▷b=tau_3, but the root equation alone is
insufficient as a specialness criterion. Already in B3, every integer k
gives a root

    b_k=s1^k s2^(1-k),       b_k▷b_k=tau_2.

For example b_0=s2 is not special, by the prior classification of positive
special braids. One can verify the displayed identity for all k by
cancelling the s3 factors in S(b_k) and using the Artin relation.
Our exploratory matrix calculation is only a necessary-condition check;
it is not used to certify specialness.

## 4. Combined status

Together with the independently documented infinite-family candidate,
the current count is

| N | Number of special braids in B_N |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 4 |
| 4 | At least 10; only exponent sum two remains unclassified |
| Every N>=5 | Countably infinite, by the candidate family |

The small cases above are credited deductions from prior braid-shelf
results. They add no separate novelty count. B9 remains one partial
candidate, awaiting specialist review and a novelty assessment.

Source: Patrick Dehornoy, [*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf),
Sections 1.3, 2.1, 4.1 and 5.2--5.3. The primary PDF and text are
archived under `literature/raw/B9-Strange-Questions-Dgb.*`; the actual
printed page 26 was viewed and retained as `literature/figures/B9-Dgb-page26.png`.
The page contains minor indexing issues in intermediate displayed formulas;
equations (2) and (6) above retain the explicit standard strand and power
conventions. No full-paper audit or new publication-date determination is
claimed. See the [separate audit](small-strand-audit.md).
