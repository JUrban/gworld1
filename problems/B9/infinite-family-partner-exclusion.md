# B9: the existing infinite family has no returning partner

30 September 2026, within the original experiment. This strengthens the
earlier [ten-input exclusion](../../research/notes/B9-family-return-obstruction.md).
It does not determine the remaining four-strand special-braid count.

Let beta_n, n>=3, be the special five-strand braid from the
[infinite-family proof](infinite-family-proof.md):

```
beta_n = s1^n s3^(n-2) s2^(1-n) s3^2 s4^-1
                     s2 s1 s3^(n-1) s4^(2-n) s2^-n.
```

Put a_n=I1(beta_n)=beta_n s1 S(beta_n)^-1, a special braid in B6.

**Proposition.** For every n>=3 and every braid c in B_infinity,

```
a_n S(c) does not belong to B3.
```

In particular no special second color of any term height can return
this first-color family to a three-strand parameter. This excludes every
partner, without a specialness assumption on c.

**Proof.** Take the unreduced Burau representation at parameter -1 in
any finite dimension large enough to contain the braids in question.
The generator s_i is the identity except for its block on coordinates
i,i+1:

```
T = [ 2 -1 ] = I+N,     N^2=0.
    [ 1  0 ]
```

Every shifted braid fixes the column vector e1. Consequently

```
rho(a_n S(c))e1 = rho(a_n)e1 = rho(beta_n)(2e1+e2).          (1)
```

Every element of the standard B3 subgroup has zero coordinates after
the third in its first column. However, multiplying the ten factors of
beta_n, using T^k=I+kN for every integer k, gives

```
(rho(beta_n)(2e1+e2))_5 = n(n-1).                          (2)
```

This is positive for every n>=3. Equations (1)--(2) exclude membership
in B3. Embedding in a larger braid group merely adds identity coordinates
and does not change this obstruction. No faithfulness of Burau is used.
QED.

For reproducibility, the first six coordinates in (1) are

```
n^4-2n^3-n^2+2n+3,
n^4-3n^3+n^2+3n+2,
-n^4+2n^3+n^2-2n+4,
-n^4+3n^3-4n+4,
n(n-1),
0.
```

Only the fifth coordinate is needed. At n=m+3 it is m^2+5m+6,
which also supplies a direct certificate of strict positivity on the
specified domain.

## Verification and limitations

The [Python calculation](../../scripts/probe_b9_family_first_column.py)
multiplies the parameterized generators and the shifted inverse exactly,
checks the Artin relations and verifies the entire first column. The
[separate GAP calculation](../../scripts/check_b9_family_first_column.g)
reconstructs the polynomial matrices in its own native polynomial ring,
checks all six coordinates and the positivity identity, and includes a
valid B3 product and a column-versus-row control.

The first recorded Python invocation used the system interpreter, which
does not contain SymPy, and failed before any mathematical computation.
The unchanged script passed with the existing virtual environment. Its
failed launch record is retained. The first GAP replay reached the last
control but compared a polynomial-ring zero with an integer zero. The
corrected replay uses `Zero(ring)` and passed with empty stderr; its
failed predecessor's exact source and logs are preserved. All four jobs
used one CPU and a 4 GB per-process limit; the successful Python and GAP
runs took 0.671 and 1.774 seconds. These are exact all-parameter matrix
identities, not extrapolations from a finite sample of n.

The previous family proof supplies specialness of beta_n and hence a_n;
the obstruction itself applies to arbitrary partner braids. Other first
colors remain unresolved. B9 stays partial, with no extra result count
or novelty claim. The written deduction and computational reconstruction
remain subject to independent specialist review.
