# B9: the remaining four-strand underlying permutation case

30 September 2026, within the original window. This continues the
[three-strand](three-strand-underlying-exclusion.md) and
[positive-underlying](positive-underlying-exclusion.md) exclusions.
It is a necessary-condition reduction, not an exhaustion of B4.

Let u,v be special, let I_p(w)=w tau_p S(w)^-1, and suppose

    A=I1(u) S(I1(v)) belongs to B3,       m(v)=4.

Then m(u)=5 by the earlier support argument. We prove the following
necessary conditions, using image-list notation for permutations:

    epsilon(v)=2,       pi(v)=(3,1,2,4),
    epsilon(u)=3,       pi(u)=(4,1,2,3,5),
    pi(A)=id.                                             (1)

In particular v is none of the ten already known special braids in B4.
No existence of a special v with the required extra strand is asserted.

## 1. Complete finite permutation bounds

For a special braid b of positive exponent p in B_n, the credited
right-branch expansion gives b=I_p(H), and the support lemma gives
H in B_(n-1). For p=1, H is itself special. These statements apply
to every special braid, with no expression-height assumption.

Let P_3 be the four permutations of the completely classified special
braids 1,s_1,s_1^2 s_2^-1,tau2. For each p, denote by J_p the
permutation map induced by I_p. A complete upper bound for special
B4 permutations, partitioned by exponent, is

    P_(4,0)={id},       P_(4,1)=J_1(P_3),
    P_(4,2)=J_2(S_3),   P_(4,3)=J_3(S_3).                 (2)

Their cardinalities are 1,4,3,1. These nine permutations are all
realized by the ten known special B4 examples, so their union P_4
is exactly the permutation image of the special B4 set. This does
**not** classify the braids in a fibre of that permutation map.

A complete upper bound for the special B5 permutations is

    P_(5,0)={id},       P_(5,1)=J_1(P_4),
    P_(5,p)=J_p(S_4) for p=2,3,4.                         (3)

The respective sizes are 1,9,12,4,1. Only containment is needed;
we do not assert that every element of (3) has a special B5 lift.
All lists are explicit in the
[inventory](../../research/certificates/B9-four-strand-permutations/inventory-v1.json).
The nu statistic equals the named exponent on each list, so the
partition does not silently identify different exponent sectors.

## 2. The complete table

The positive special v=tau3 is excluded by the preceding universal
positive-underlying proposition. At exponent one, exactly two v
have minimum strand number four: I1(s_1^2 s_2^-1) and I1(tau2).
At exponent two, all three permutations in (2) must be retained;
a permutation fixing the fourth position does not imply a braid
on three strands. Thus there are five v-cases.

For every f in (3) and each of these five g=pi(v), compute

    pi(A)=J_1(f) S(J_1(g)).

It must fix positions 4,5,6. The following table gives the number
of permutations satisfying that condition in each exponent sector
of u:

| v-sector and permutation | epsilon(u)=1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: |
| exponent 1: (3,1,4,2) | 0 | 0 | 0 | 0 |
| exponent 1: (1,2,4,3) | 0 | 0 | 0 | 0 |
| exponent 2: (1,4,2,3) | 0 | 0 | 0 | 0 |
| exponent 2: (2,1,4,3) | 0 | 0 | 0 | 0 |
| exponent 2: (3,1,2,4) | 0 | 0 | 1 | 0 |

These are all 5*(9+12+4+1)=130 cases. The single survivor is
exactly (1). It already satisfies the small-class condition; imposing
that additional condition does not remove it.

The six known special braids of exactly four strands have permutations

    (4,1,2,3), (2,1,4,3), (1,4,2,3),
    (1,2,4,3), (3,1,4,2), (2,1,4,3),

in the order of the existing word fixture. None has the required
permutation of v. Together with the previous smaller-strand and
positive-v exclusions, this proves:

**Corollary.** For arbitrary special u and v among the ten known
special braids in B4, A=I1(u) S(I1(v)) belongs to B3 only in the three
already classified cases (u,v)=(1,1),(s_1,1),(s_1^2 s_2^-1,s_1).

The quantifier over u is unrestricted. This is stronger than the older
return obstruction that tested only u from one specified infinite B5
family. It still leaves unknown v and higher underlying strands.

## 3. A conditional descent observation

Suppose an additional special B4 braid is represented by a special
term with the least number of leaves among all such counterexamples
to the known ten-element list. If its right-branch decomposition has
parameter A of total exponent two and both colors are nontrivial,
it has the form

    I1(u) triangle (I1(v) triangle 1).

The underlying v is a proper subterm. If m(v)=4, condition (1) makes
v itself an additional special B4 braid, contradicting that minimal
choice. The earlier reductions exclude m(v)<=3. Consequently such
a minimal counterexample, **if its parameter has total exponent two**,
must have m(v)>=5. Alternatively its parameter can have total exponent
at least three, which this observation does not treat.

This is a descent condition on a hypothetical minimal counterexample,
not a proof that every m(v)=4 parameter is impossible. An existing
unknown B4 braid could occur as the smaller v in another example.

## 4. Verification and limits

The [Python inventory](../../scripts/probe_b9_four_strand_permutations.py)
constructs the finite sets in (2)--(3) from all permutations in S3,S4,
checks their nu statistics and every one of the 130 pairs. The
[GAP verifier](../../scripts/check_b9_four_strand_permutations.g) independently
reconstructs the sets from native symmetric groups and obtains exactly
the same survivor. It also compares the nine-element P4 bound with
the actual permutations of all ten previously witnessed words and
checks the six exact-four-strand inputs. Their specialness and exact
strand numbers retain their existing certificates; this checker
recomputes the permutation interface, not their earlier full proofs.

The jobs are sequential, each one CPU/2 GB with a 60-second limit.
Python passed in 0.071 seconds, GAP in 1.825 seconds, with empty stderr.
Exact data, sources, dependencies and process records are bound by the
[manifest](../../research/certificates/B9-four-strand-permutations/manifest-v1.json).
There was no term-height or word-length cutoff and no increased braid
enumeration. Finiteness of the displayed permutation spaces is exact;
their sufficiency for an actual braid solution is not claimed.

The original problem/source/visual audits and prior theorem attributions
are unchanged from the two preceding supplements. No new bibliography
or primary-page inspection is asserted here. This is a same-agent
deduction with separate computational reconstruction, not an external
mathematical review. B9 remains partial, with no tally or novelty change.
