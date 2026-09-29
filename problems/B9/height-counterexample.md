# A special braid in B5 with minimum expression height six

29 September 2026. Related-result candidate, **not a solution of the full
GroupWorld B9 counting problem**. Novelty and specialist review remain open.

Write

\[
 a\triangleright b=a\,\operatorname{sh}(b)\,\sigma_1\,
                    \operatorname{sh}(a)^{-1}.
\]

The special braids are the closure of the identity under this operation.
The height of a term is zero at the identity and one plus the maximum
of the two child heights otherwise. Write c(beta) for the minimum height
of a term evaluating to beta.

In [Patrick Dehornoy, *The Braid Shelf*, Section 3.2, Question 3.19](https://dehornoy.lmno.cnrs.fr/Surveys/Dja.pdf),
the question is whether every special beta in Bn satisfies c(beta)<=n.
The example below has c(beta)=6 and belongs to B5. This answers that
printed question negatively. It does not determine whether there are
finitely many special braids in each fixed Bn, or their total number.

## A short special term

Define these special braids, in the indicated order:

| Name | Definition | Displayed term height |
|---|---|---:|
| e | identity | 0 |
| u1 | e ▷ e | 1 |
| u2 | u1 ▷ e | 2 |
| u3 | u2 ▷ u1 | 3 |
| u4 | u3 ▷ u2 | 4 |
| u5 | u4 ▷ u3 | 5 |
| v1 | e ▷ u2 | 3 |
| v2 | v1 ▷ e | 4 |
| v3 | e ▷ v2 | 5 |
| beta | u5 ▷ v3 | 6 |

Straight expansion, cancellation and commutation of distant generators give

\[
\begin{aligned}
u_2&=\sigma_1^2\sigma_2^{-1},\\
u_3&=\sigma_1^3\sigma_3\sigma_2^{-2},\\
u_4&=\sigma_1^4\sigma_3^2\sigma_4^{-1}\sigma_2^{-3},\\
u_5&=\sigma_1^5\sigma_3^3\sigma_5\sigma_4^{-2}\sigma_2^{-4},\\
v_3&=\sigma_3^2\sigma_4^{-1}\sigma_2^2\sigma_3^{-1}
       \sigma_5\sigma_4^{-2}\sigma_1.
\end{aligned}
\]

Consequently beta has the following 29-letter representative:

\[
\boxed{\beta=\sigma_1^5\sigma_3^3\sigma_2^{-4}\sigma_3^2
 \sigma_4^{-1}\sigma_2\sigma_1\sigma_3^4\sigma_4^{-3}\sigma_2^{-5}.}
\tag{1}
\]

Here is the strand reduction explicitly. Before simplifying the shelf product,
its word is

\[
\sigma_1^5\sigma_3^3\sigma_5\sigma_4^{-2}\sigma_2^{-4}
\sigma_4^2\sigma_5^{-1}\sigma_3^2\sigma_4^{-1}
\sigma_6\sigma_5^{-2}\sigma_2\sigma_1\sigma_3^4
\sigma_5^2\sigma_6^{-1}\sigma_4^{-3}\sigma_2^{-5}.
\]

Commute sigma4^2 past sigma2^-4 and cancel it with sigma4^-2;
then commute sigma5 past sigma2^-4 and cancel sigma5^-1.
The remaining sigma5^-2 and sigma5^2 commute past the intervening
sigma2 sigma1 sigma3^4 and cancel. The sigma6 pair then cancels in
the same way. The resulting word is exactly (1), so beta lies in B5.
This reduction uses no normal-form software.

## Excluding every term of height at most five

Use the unreduced Burau representation in dimension seven over
GF(1000003), at t=2. The matrix of sigma_i is the identity except for
the block on coordinates i,i+1:

\[
\begin{pmatrix}1-t&t\\1&0\end{pmatrix}.
\]

Invert these matrices for inverse generators. They satisfy the Artin
relations, so unequal matrices imply unequal braids; faithfulness is
unnecessary.

Let S_h be the set of matrices of all terms of height at most h.
Starting at S_0={I}, compute the exact recurrence

\[
 S_{h+1}=\{I\}\cup
 \{A\,\operatorname{sh}(B)\,\rho(\sigma_1)\,
           \operatorname{sh}(A)^{-1}:A,B\in S_h\}.
\tag{2}
\]

Every height-h term lies in B_(h+1). Thus, throughout the computation
up to height five, matrix shift is unambiguous: remove the last trivial
row and column and add a trivial first coordinate. In particular, equal
parent matrices have equal shifted matrices. Deduplication loses no
possible image, even when the representation identifies different braids.

The cardinalities at heights zero through five are

\[
1,\quad2,\quad4,\quad10,\quad52,\quad1930.
\]

The top-left five-by-five block of rho(beta) is

```text
     54  578176  921968  187449  312360
 999977  828106  671838  187524  312565
 249986  355458  769511  703142  921913
 250008  386727  738297  578119   46856
      0  953127  546875  687503  812505
```

The remaining block is the two-dimensional identity, with zero off-diagonal
blocks. This matrix is absent from S_5. Thus c(beta)>5. The displayed
term gives c(beta)<=6, proving c(beta)=6. The matrix also is not
supported on the first four coordinates, so beta does not belong to
the standard B4 subgroup.

This is a finite computational proof of the exclusion step. The small
standalone GAP verifier
[`scripts/check_b9_height_counterexamples.g`](../../scripts/check_b9_height_counterexamples.g)
recomputes (2) from the identity, rather than trusting a supplied list of
1930 matrices. It also checks the special-term witnesses and strand reductions
independently using free groups. Its fixture is
[`height-counterexamples-v1.g`](../../research/certificates/B9-strand-drop/height-counterexamples-v1.g).
The example (1) is witness 4, term 34 in the one-based GAP fixture,
or filter index 5180 in the discovery data.

## Source scope and limitations

The full frozen GroupWorld braid page, exact B9 fragment and its original
rendering were inspected. The actual printed survey page 13 was also
inspected; its complexity definition agrees with the term-height
convention used here. The survey's preceding forward implication has
an indexing issue: height h immediately gives B_(h+1), not B_h.
The example above refutes the **literal weaker** bound c(beta)<=n as
well as the more restrictive c(beta)<=n-1; it does not rely on choosing
one correction of that indexing issue.

The earlier bounded-enumeration note remains a historical record: at
that stage no counterexample to the height question had been found.
Neither the 1930 images nor the new examples exhaust all special braids
in a fixed braid group. Limited primary-source searches did not locate
a previous answer to this height question; that is not proof of novelty.
No additional GroupWorld whole-entry or named-subpart solution is counted.
