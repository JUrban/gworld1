# M3: what the A5 enumeration theorem supplies, and what it leaves open

29 September 2026, during the original run. An effective reduction using
prior results; **not a solution of M3 or an additional candidate**.

M3 asks whether metabelianity is decidable from an ordinary finite
presentation promised to define a solvable group. The full frozen
`probmet.html` was reread. The new A5 audit concerns Jayadevan's
arXiv:2609.10281v1, submitted before our experiment.

## Effective construction of the maximal metabelian quotient

Assume the prior A5 theorem: there is a uniform semidecision procedure
accepting exactly ordinary finite presentations of metabelian groups.

**Consequence.** From a finite presentation `P=<X|R>` one can compute an
ordinary finite presentation of `G/G''` and finitely many words normally
generating `G''`, whenever `G/G''` is finitely presented. The procedure
halts exactly for that class of inputs. In particular it terminates if
`G` is solvable, or more generally has no nonabelian free subgroup.

Enumerate all words

    d_i = [[u_i,v_i],[s_i,t_i]]

in the finite alphabet X, by enumerating all quadruples of words. They
normally generate the second derived subgroup of the free group on X.
Let

    P_j = <X | R,d_1,...,d_j>.

Dovetail the A5 semidecision procedures for all j, including j=0.
Return the first accepted `P_j` and the list `d_1,...,d_j`.

To prove soundness, put `K_j=<<d_1,...,d_j>>_G`. Always `K_j <= G''`.
Acceptance says `G/K_j` is metabelian, so also `G'' <= K_j`. Thus
`K_j=G''`; the returned presentation and normal generators are exact.
The order in which successful threads terminate does not matter.

For termination, the kernel of an epimorphism between finitely presented
groups is finitely normally generated. This elementary fact follows by
writing a presentation of the target on the source's finite generating
alphabet. Apply it to `G -> G/G''`. Each of the finitely many necessary
kernel generators is a finite product of conjugates of the enumerated
`d_i` values. Hence some finite prefix normally generates all of `G''`,
and its `P_j` is metabelian. Its A5 thread eventually accepts.
Conversely, if any thread accepts, its finite presentation presents
`G/G''`, which is therefore finitely presented. This proves the exact
halting characterization.

The termination promise for solvable groups uses Bieri–Strebel:
an infinitely presented finitely generated metabelian group cannot be
an epimorphic image of a finitely presented group without nonabelian
free subgroups. The precise form used is Theorem 1.5 of
[Benli–Grigorchuk–de la Harpe, *Amenable groups without finitely presented
amenable covers*](https://doi.org/10.1007/s13373-013-0031-5), together with
Proposition A.5(ii'). The publisher renders the latter as Proposition 6.5.
These exact statements and the relevant proof discussion were read;
the underlying Bieri–Strebel theorem was not reproved here.

There is no bound asserted on j, certificate size, or running time.
This is a theoretical construction, not an implemented general solver.
For a nonabelian free group its metabelianization is infinitely presented,
so this procedure does not halt; omitting the termination promise would
be an error.

## Why M3 remains unresolved

Finding normal generators of `G''` does not determine whether those
generators are trivial in G. The solvability promise does not supply
a word-problem algorithm: finitely presented solvable groups with
unsolvable word problem exist. Metabelianity of the quotient is not
metabelianity of the original group.

An explicit control is S4. With `a=(1,2,3,4)` and `b=(1,2)`, let
`c=[a,b]` and `d=[c,c^a]`, using right commutators and right conjugation.
Then `G''=V4` is nontrivial and is the normal closure of d, while
`G/<<d>>` is S3 and metabelian. Thus an accepted nonzero prefix in the
construction cannot be used as a positive M3 verdict. The retained GAP
check verifies the ordinary presentation `<a,b|a^4,b^2,(ab)^3>`, its
quotient after adding d, and the permutation realization independently.

Another possible route passes to `G''/G'''`: since G is solvable, this
module vanishes exactly when `G''=1`. But normal finite generation alone
gives only finite generation of that module over `Z[G/G'']`. It does
**not** give an effective finite module presentation or a general module
zero test. No such missing procedure is assumed here.

## A separate conditional decision procedure

If an actual word-problem algorithm for G is supplied along with P,
metabelianity is decidable, using the A5 theorem:

1. Run the positive A5 test on P.
2. In parallel enumerate the `d_i` and apply the supplied word-problem
   algorithm. Reject as soon as a nontrivial value is found.

Exactly one branch terminates. This works without a solvability promise.
For residually finite groups the negative branch can instead enumerate
finite quotients and find a nonmetabelian image; residual finiteness
ensures detection of a nontrivial double commutator. These are direct
consequences of credited prior work, not counted new resolutions. Neither
argument supplies the missing negative branch for all M3 inputs.

## Provenance and limits

- A5 source, unchanged Lean build and statement evidence are documented
  separately in `A5-prior-Lean-proof-audit.md`.
- The full 2013 publisher HTML and retrieval/hash metadata are retained
  as `literature/raw/M3-BieriStrebel-cover-2013.{html,json}`.
- The original M3 statement has no extra subpart or linked background.
- This note does not claim a proof of Bieri–Strebel, a general M3 decision,
  novelty of the reductions, or a practical complexity bound.
