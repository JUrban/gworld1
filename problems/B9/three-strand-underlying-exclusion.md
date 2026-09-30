# B9: exclude every three-strand underlying second braid

30 September 2026, within the original experiment. This strengthens the
[exponent-two parameter reduction](exponent-two-parameter-reduction.md).
B9 remains partial: the total-exponent-two parameter sector at higher
underlying strand numbers, and larger total parameter exponents, are
not exhausted. There is no new problem count or established novelty claim.

Write s=sigma1, t=sigma2, r=sigma3, z=s^2 t^-1, and tau2=ts,
tau3=rts. Let I1(w)=w s S(w)^-1, and let m(w) be the least standard
strand number of w, with m(1)=1.

**Proposition.** If u,v are special and m(v)=3, then

    A=I1(u) S(I1(v)) does not belong to B3.

This quantifies over every special u, not only an enumerated term family.

## 1. Complete reduction to permutations and known sectors

Suppose A belongs to B3. The existing support argument gives m(u)=4.
The complete small-strand classification gives v=z or v=tau2. Also
epsilon(u) is 1,2 or3. The endpoint cases are already known:

    epsilon(u)=1:  u=I1(z) or I1(tau2),
    epsilon(u)=3:  u=tau3.

Indeed every exponent-one special braid is I1(w), and its minimal
strand number is m(w)+1. The only special braids of exactly three
strands are z,tau2. The maximal exponent sector in B4 consists only
of tau3. These are deductions from Dehornoy's structural theorems,
as proved and credited in [the small-strand note](small-strand-proof.md).

The unknown exponent-two sector need not be classified. For a special
u, its permutation f satisfies

    nu(f) = #{j : f(j+1)=j} = epsilon(u).

The only permutations in S4 with nu(f)=2, in image-list notation, are

    (1,4,2,3),       (2,1,4,3),       (3,1,2,4).

One can obtain this list by choosing the two required positions among
1,2,3; the other possible completion is (4,1,2,3), which has nu=3.
No hypothesis about which permutations are realizable by special braids
is needed: the displayed list contains every possible image in this sector.

All permutations are functions composed with the rightmost factor first.
For a permutation f, the image of I1 is f (1 2) S(f)^-1. Substituting
in A gives the following images of positions 4 and 5:

| Permutation of u, epsilon(u)=2 | v=z | v=tau2 |
| --- | --- | --- |
| (1,4,2,3) | (2,3) | (2,5) |
| (2,1,4,3) | (3,2) | (3,5) |
| (3,1,2,4) | (5,4) | (5,3) |

Every braid in B3 fixes both positions, so the required pair is (4,5).
None of these cases works. This excludes the **entire unknown
exponent-two sector** of u under the present m(v)=3 assumption.

For the two known exponent-one possibilities and the exponent-three
possibility the same calculation gives:

| Actual special u | v=z | v=tau2 |
| --- | --- | --- |
| I1(z) | (2,5) | (2,3) |
| I1(tau2) | (3,4) | (3,5) |
| tau3 | (4,3) | (4,5) |

Only u=tau3,v=tau2 survives this necessary permutation test. Its A
has the identity permutation; that fact does not establish strand support.

## 2. The single permutation survivor is excluded

Put c=I1(v). Expanding and cancelling shifted factors gives

    A=u s S(u^-1 c).

If A belongs to B3 and u belongs to B4, then S(u^-1 c) belongs to B4.
The standard shifted-parabolic intersection implies u^-1 c in B3.

For u=tau3 and v=tau2 the two actual words are

    u=r t s,             c=t s^2 t^-1 r^-1.

Use the four-dimensional unreduced Burau representation at -1, with
generator block [[2,-1],[1,0]]. Direct integer matrix multiplication gives

    rho(u)e4 = ( 0, 0,-1,0)^T,
    rho(c)e4 = (-2,-4,-1,2)^T.

Every element of B3 fixes e4. If c=u h with h in B3, these columns
would agree. They do not. This excludes the last case and proves the
proposition. Faithfulness of Burau is not used.

For an additional exact check, the faithful Artin actions in the same
word convention send the fourth free generator to

    u(x4) = x3,
    c(x4) = x4^-1 x2^-1 x1 x2 x3 x2^-1 x1^-1 x2 x4.

They are distinct reduced free words. The explicit parameter A also
moves x5 under its Artin action, despite its trivial permutation.

## 3. Consequence for the remaining problem

Combining the proposition with the earlier complete treatment of v in B2,
the parameters A=I1(u) S(I1(v)) in B3 with **v in B3** are exactly

    s t,        s^2,        z s,

coming respectively from (u,v)=(1,1),(s,1),(z,s). All belong to known
parameter cosets. Of these pairs of colors only the first is terminal.

Therefore any additional terminal parameter of total exponent two must
have

    m(v)>=4,       m(u)=m(v)+1>=5.

Its actual colors a=I1(u), c=I1(v) have at least six and five strands,
respectively. Their product a S(c) would have to drop to three strands.
This sharper lower bound does not rule out such cancellation. It also
does not constrain a terminal parameter of total exponent at least three.
The resulting special braid I2(A) has exponent two throughout; its
exponent must not be confused with the variable exponent of A.

## 4. Checks and source boundary

The [Python checker](../../scripts/check_b9_three_strand_underlying.py)
enumerates all 24 permutations in S4, obtains the complete three-element
nu=2 list, computes all six unknown-sector rows and all six known-sector
rows, and verifies the final matrix and faithful-action obstruction.
It retains the full permutations, explicit words and reduced free words
in [the certificate](../../research/certificates/B9-three-strand-underlying/checks-v1.json).

The [GAP checker](../../scripts/check_b9_three_strand_underlying.g) independently
constructs S4, all table entries, the Burau generator matrices and the
native free-group actions. It reads neither the Python certificate nor
the old height-four term list. Both check right-column invariance; the
surviving identity permutation is an explicit control against accepting
permutation support as braid support.

Two recorded jobs passed with empty stderr: Python in 0.069 seconds and
GAP in 1.775 seconds, each with one CPU and a 2 GB per-process cap.
Their small overlap reserved two CPU slots and 4 GB. Both terminal PIDs
were confirmed absent and the registry empty; log hashes were checked.
There was no failed mathematical run or enlarged term search here.
The [manifest](../../research/certificates/B9-three-strand-underlying/manifest-v1.json)
binds the exact sources, data, records and proof dependencies.

The full frozen problem page and original B9 fragment were reread, and
the retained statement rendering was actually viewed. The relevant
nu/exponent and strand-power statements and local proofs in Dehornoy's
[*Strange Questions About Braids*](https://dehornoy.lmno.cnrs.fr/Papers/Dgb.pdf)
were reread in text. No new visual inspection of a primary-source page
or full-paper audit is claimed. The ordinary support and specialness
dependencies remain those in the earlier small-strand audit.

Three fresh searches about special-braid enumeration mainly returned
that paper, the already archived braid-shelf survey, and a different
notion of special positive braid. The survey's fraction-recognition
discussion was inspected; it was not used as an exhaustion theorem.
Search freshness labels are not publication dates, and this limited
check establishes no novelty conclusion. All work here is same-agent;
the separate GAP reconstruction is not external specialist review.
