# B9: two infinite-family routes do not give a new four-strand braid

29 September 2026, approximately 22:12--22:15 UTC. These are exclusions
of two proposed constructions, not an exhaustion of the remaining B4
sector. B9 remains partial and the candidate tally does not change.

Use the previously audited special-braid operation
a triangle b=a S(b) s1 S(a)^-1 and write I1(a)=a triangle 1.
The [remaining parameter problem](../../problems/B9/small-strand-proof.md)
asks which right B2 cosets in B3 contain a product a S(c) of two
special colors. Its total-exponent-two sector has a=I1(u), c=I1(v).

## 1. The known infinite B5 family cannot return through a known B4 input

Let beta_n, n>=3, be the infinite family from
[the existing proof](../../problems/B9/infinite-family-proof.md):

    beta_n = s1^n s3^(n-2) s2^(1-n) s3^2 s4^-1 s2 s1
             s3^(n-1) s4^(2-n) s2^-n.

Let V be the following **ten known examples** in C intersect B4. This
notation does not assume that they exhaust that intersection. Put
s=s1, t=s2 and r=s3 in this table.

| v | Burau matrix entry (1,5) of I1(v), at parameter -1 |
|---|---:|
| 1 | 0 |
| s | 0 |
| t s | 0 |
| s^2 t^-1 | 0 |
| r t s | -2 |
| t^2 r^-1 s | 0 |
| s t^2 r^-1 s t^-1 | -2 |
| t s^2 t^-1 r^-1 | 2 |
| s^2 t^-1 s r t^-2 | 34 |
| s^3 r t^-2 | 12 |

**Proposition.** For every n>=3 and every v in V, the parameter

    A = I1(beta_n) S(I1(v))

does not belong to B3. Thus this construction produces no additional
special four-strand braid.

**Proof.** Put u=beta_n and c=I1(v). Both lie in B5. Expanding gives

    A = u s1 S(u^-1 c).

If A belonged to B3, then S(u^-1 c)=s1^-1 u^-1 A would lie in B5.
The standard shifted-parabolic intersection therefore implies

    h=u^-1 c in B4.                                         (1)

In the five-dimensional unreduced Burau representation at -1, every
matrix representing B4 fixes the last coordinate vector e5. Equation
c=u h would consequently give

    rho(c)e5=rho(u)e5.                                      (2)

It is the last **column** that is invariant under right multiplication
by B4. A last-row comparison would not be justified here.

Use the generator block [[2,-1],[1,0]] on coordinates i,i+1. It equals
I+N_i with N_i^2=0, so its k-th power is I+k N_i for every integer k.
Multiplying the ten displayed factors of beta_n gives

    rho(beta_n)[1,5] = n(n-1)((n-1)^2+1).                    (3)

At n=3 this is 30, which is absent from the table. For n=m+4, m>=0,
it is

    m^4+13m^3+64m^2+142m+120 >=120,

whereas every entry in the table is at most 34. Thus (2) fails for
every allowed n and v. This proves the proposition. No faithfulness of
Burau is used: distinct images exclude equality. QED.

The exponent-two condition here concerns epsilon(A), because both
I1(u) and I1(v) have exponent one. It does not require epsilon(u)=1.
The construction is therefore distinct from merely rerunning the old
height-four pair probe. It tests an entire infinite family of u, but
only the specified ten v. Other special B5 families, unknown special
B4 inputs and larger underlying strand numbers remain unexcluded.

## 2. A natural cancellation of the recurrence is just a known ray

Write f0=1, f1=s1 and f_(j+1)=f_j triangle f_(j-1). The existing
infinite-family proof establishes, for j>=1,

    f_j S(f_(j-1))=s1^j.

One might try to cancel the high-strand tail of f_n by defining

    w_n=S^2(f_(n-3)) s1^(n-1) s2^(2-n),       n>=3.

This expression is indeed special, but it is exactly f_(n-1). In fact,
shifting the identity with j=n-2 gives

    S(f_(n-2)) S^2(f_(n-3))=s2^(n-2),

and therefore

    f_(n-1)=s1^(n-1) S(f_(n-2))^-1
            =s1^(n-1) S^2(f_(n-3)) s2^(2-n)=w_n.

The last equality commutes s1 past the twice-shifted factor, whose
generators all have indices at least 3. Consequently

    f_n S(w_n)=s1^n in B2,

and I2(f_n S(w_n)) is always the already known braid s2 s1. This
explains why that cancellation creates no new parameter coset. It
uses the universal recurrence identity, not a finite sample of n.

## 3. Verification, failed bounds and limitations

`scripts/check_b9_family_return.py` independently recomputes the
polynomial (3) from the braid factors and the ten constants from the
previously certified special words. It checks the generator relations,
nilpotent increments and expansion at n=m+4 over the integers.
`scripts/check_b9_family_return_gap.g` independently repeats these matrix
calculations in GAP and checks the input words against the archived
height-four GAP fixture. Neither program enumerates a larger term-height
list. Existing specialness certificates and the full group-theoretic
family proof are reused, not replaced by matrix images.

An explicit control u=s4, c=s4 s3 has u^-1 c in B4. Their last columns
agree but their last rows differ. This checks the side of multiplication
in (2). The universal written argument supplies the subgroup implication.

Four recorded runs, each one CPU and 4 GB:

- `b9-family-return-v1`: failed. The proposed bound that every table
  entry is strictly below beta_3[1,5]=30 is false: one entry is 34.
  Its exact script, table and logs are retained.
- `b9-family-return-v2`: passed in 0.47 seconds, empty stderr. Separating
  n=3 from n>=4 repairs the argument for the same entire family.
- `b9-family-return-gap-v1`: failed because GAP had no matrix inverse
  method for the polynomial-domain generator in that control. Its
  exact script and logs are retained; zero exit code was rejected.
- `b9-family-return-gap-v2`: passed in 1.82 seconds, empty stderr, using
  the directly checked inverse I-N_i. It also binds the original words.

The first Python run's JSON is evidence of the failed bound, not a
successful certificate. The v2 outputs are the final ones. The manifest
binds both versions, all four process records, the previous source
fixtures and this note. No new source theorem, Kourovka material or
novelty claim is introduced. Independent specialist review remains pending.
