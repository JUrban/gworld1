# N8 diagonal separation: two further actual group fixtures

29 September 2026, 18:18--18:24 UTC. These complete the two specific
group tests left in `N8-diagonal-separation-audit.md`. The general
decision argument is still unadopted pending a fresh audit of its
assembly and inherited dependencies. Counts remain 8 whole-entry
candidates, 2 partial candidates and 0 established novel results.

Both fixtures use weighted free nilpotent groups with generator weights
(1,4), exact rational tensors for construction, and actual integral
Hall group coordinates for every final pair, target and correction.
Native GAP/nq independently constructs each weighted group, all block
columns, the complete integer lattice, quadratic residuals and two
witness pairs. Separate GAP arithmetic and family checkers reconstruct
the full integer fibers for each new input. These are bounded examples,
not an implementation of the proposed arbitrary-rank decision algorithm.

## 1. Leading term with two E letters

Write E_i=ad_a^i(e), and put

    D=2[e,E_3]+3[E_1,E_2],
    V=2[e,[e,E_2]]-[E_1,[e,E_1]].

Then [a,V]=[e,D]. Unlike the preceding group fixtures, D has two
E letters. Its weight is q=11. With p=1, first offset t=3 and class18,
take x=exp(a) and y=exp(M h(ad_a)^(-1)D), where
h(z)=(1-exp(-z))/z. Hall-coordinate denominator clearing gives M=30240.
All terms with two Y occurrences are above this class. The constructor
checks the exact logarithmic identity, integrality, every block equation
and full group witnesses.

The group has Hirsch length76. The full block matrix has32 rows and27
columns, kernel rank1 and first integer step12. That step is preserved.
The last correction matrix has15 columns and rank15, while appending
the first quadratic gives rank16. There are no later free block columns.
GAP checks27 block columns, all15 terminal columns at two base parameter
values, and six parameter samples. The samples include0,1,2, which
determine every coefficient under the proved degree-two weight bound.
Thus the nonzero four-E-letter quadratic is tested in an actual group,
not just the free associative algebra.

The native verifier reconstructs the base from its integral Hall
coordinates; the explanatory rational h^(-1) description is checked
by the constructor only. The recorded fixture is
`research/certificates/N8-two-e-leading-block-v1/`.

## 2. A nonzero fixed first-factor prefix

Now D=E_6, p=1,q=10,t=5 and class21. Let A=exp(a), E=exp(e), and
take the actual first factor x=AE. Its logarithm X begins

    X=a+e+(1/2)[a,e]+terms of weight at least6.

Thus offsets3 and4 of the first factor are fixed and nonzero before
the first remaining exception at5. Let phi be the filtered rational
Lie substitution a->X,e->e. It has identity associated graded. Put

    Y=phi(h(ad_a)^(-1)D),
    Z=phi(D),
    y=exp(MY),        M=11404800.

The constructor collects exp(kY) at k=1,2 and clears denominators of
both coefficients of the resulting Hall polynomials. Their constant
terms vanish, and their degrees are at most floor(21/10)=2. It then
verifies integrality directly at M. The full commutator logarithm is

    log[x,y] = M[X,Z] + (M^2/2)[[a,D],D].

The second term has weight21. It is nonzero in this example and must
be kept. The constructor checks this complete identity; it does not
silently discard all two-Y terms. A block parameter first appears
at offset5, so its effect on that two-Y term is above class21, as
required by the proposed general argument.

The actual group has Hirsch length171. Its full earlier block has
95 rows and80 columns, with kernel rank3 and adapted steps2,2,1.
The kernel offsets are5,7,9. The first two are exceptional; offset9
is the Nielsen (universal) offset and is labelled separately in the
certificate. The terminal correction matrix has33 columns and full
rank33. The later-column cokernel rank is zero, and appending the
first quadratic gives rank34.

Native GAP verifies80 block columns, all33 terminal columns at two
parameter values, the whole integral affine lattice, five layer-kernel
ranks and two full group witnesses. Eleven parameter samples have
rank10 on all monomials of total degree at most two in three variables;
GAP independently reconstructs that evaluation matrix and its rank.
Consequently it verifies all10 coefficients, including every mixed
and square term, under the degree bound from the first increment
weights6 and15. In particular 2*6+10=22>21 excludes same-first-factor
quadratic terms in the commutator, and three total parameter increments
are later still. The group fixture is
`research/certificates/N8-normalized-prefix-block-v2/`.

## 3. Records, failure and remaining scope

| Recorded job | Result | Seconds |
|---|---|---:|
| n8-two-e-leading-block-v1 | Pass | 5.035 |
| n8-two-e-leading-block-gap-v1 | Pass | 3.331 |
| n8-two-e-leading-families-gap-v1 | Pass | 2.077 |
| n8-two-e-leading-arithmetic-gap-v1 | Pass | 2.178 |
| n8-normalized-prefix-block-v1 | Failed in parameter-basis selection | 15.370 |
| n8-normalized-prefix-block-v2 | Pass | 44.470 |
| n8-normalized-prefix-block-gap-v1 | Pass | 18.878 |
| n8-normalized-prefix-families-gap-v1 | Pass | 2.126 |
| n8-normalized-prefix-arithmetic-gap-v1 | Pass | 2.479 |

The failed prefix constructor had already checked the logarithmic
identity and complete block kernel. It chose the first Hall row of
an offset when adapting the parameter basis, although that row could
vanish on the relevant kernel direction. The correction selects a
row that is actually nonzero on the remaining kernel. The resulting
change remains integral unimodular; GAP checks it and the full kernel.
The failed run, partial output and exact executed source are retained.
Its temporary offset list also called the Nielsen offset9 exceptional;
the final source and certificate distinguish it from offsets5,7.

All jobs are terminal, and successful runs have empty stderr. Maximum
overlap was3 CPU cores and16 GB reserved memory. No push, contacts,
subagents or original-clock changes occurred. No fresh general novelty
claim or specialist validation follows from these tests. The next work
is the full proof audit, not enlarging these finite fixtures or repeating
their passed arithmetic checks.
