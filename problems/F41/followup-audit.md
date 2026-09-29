# F41: parameter and uniformity audit

29 September 2026, approximately 07:14--07:24 UTC, during the original run.
Read with `multipattern-proof.md` and `multipattern-audit.md`. This is a
second internal audit, not outside mathematical review. No new problem or
scope is counted, and no existing finite suite was rerun.

## Dependency check

Reread KM Definitions 5--6, Theorems 7, 12--13, the proof of Theorem 13
and Lemma 14, and the subsequent negligible-set discussion. Reread
Pillay's generic-element definition, Fact 1.10 and Theorem 2.1 with its
proof. Viewed again the four retained images of KM printed pages 3/9
and Pillay printed pages 6/7. The source files and hashes are those in
the original audit. No new source edition is substituted.

The counting argument uses every nonconstant position in the first
noncancelling parametrization, even when a variable's second occurrence
is not another formal occurrence in that expression. The definition
that its value is a piece supplies a second occurrence in the actual
output word. The number of blocks and the total coefficient length
are fixed. These points survive the rereading.

The signed identification graph bounds the number of components by
(n+C)/2. The quotient of the position path is connected, including when
repeated pieces overlap or cross coefficient boundaries. A spanning
tree excludes one alphabet letter for each nonroot component; signed
edges change which letter is excluded, not the number. Inconsistent
signs give no word. This gives the required base 2r-1 rather than 2r.

## Parameter-free formulas are essential twice

The proof chooses phi in the complete generic type over the empty set.
Consequently (i) all automorphic images of w fail phi, and (ii) a basis
element satisfying phi makes its solution set finite-translate generic.
Both statements use the same absence of parameters.

A simple negative control is the formula x=a, with a named basis
element a. Its singleton solution set contains an element generic over
the empty set, but no finite collection of its translates covers the
infinite group. There is no contradiction: the formula has parameter a,
and a is not generic over that parameter set. Also its solution set is
not invariant under all automorphisms. Thus neither of the two proof
steps may be applied to an arbitrary formula with coefficients.

KM allows coefficients; this causes no difficulty. It is Pillay's
separating formula that must be parameter-free. The resulting finite
multipattern description may have fixed coefficients depending on w.
No effective construction of that formula or description is inferred.

## The bound is for each fixed orbit

There is no uniform degree or constant over all nonprimitive words.
For a concrete control, the kernel K of the abelianization map
F_r -> (Z/2Z)^r has finite index. Every element of K has an abelianization
vector with all coordinates even, and hence is nonprimitive. Thus the
union of nonprimitive orbits has full ball exponential rate 2r-1:
it contains K, whose finite-index coset cover implies that rate.

This is consistent with each fixed nontrivial orbit having rate
sqrt(2r-1). An infinite union need not inherit the individual estimates.
In particular the argument provides no polynomial bound uniform in the
input word for F25, and no sharper cyclic-orbit formula.

## Outcome and remaining limits

No gap was found in this pass. It still imports the full KM theorem and
Pillay's model-theoretic dependencies; their deep proofs have not been
independently established by this experiment. The counting checks do not
validate those dependencies. Additional targeted searches did not locate
a matching full orbit-growth theorem or a correction that settles its
status. That failure to locate a source is not evidence of novelty.

F41 remains one whole intended-scope candidate awaiting specialist and
bibliographic review. The experiment tally remains six whole candidates,
three partial candidates and zero established novel results.
