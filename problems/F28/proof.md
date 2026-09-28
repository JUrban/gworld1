# F28: a virtual isomorphism with no nontrivial invariant subgroup

Candidate negative answer, 28 September 2026. The proof is self-contained apart from the elementary ping-pong and Schreier basis lemmas, whose applications are described below. Novelty remains provisional pending the literature audit. No external review has yet occurred.

## Statement and example

The [original problem](https://shpilrain.ccny.cuny.edu/gworld/problems/probfree.html), attributed to S. Sidki, asks whether every isomorphism from an index-two subgroup S of F2 onto a subgroup R of F2 preserves some nontrivial subgroup H contained in S. We disprove even the weaker requirement f(H) contained in H; hence the example also excludes f(H)=H. H need not be finitely generated or normal.

Let F=F(a,b). Set

    S = <a, bab^-1, b^2>,
    f(a) = b^-2,
    f(bab^-1) = b^-1 a^2 b,
    f(b^2) = b^-1 a.

Then S has index two, these three displayed generators form a free basis, f is injective, and the only subgroup H<=S with f(H)<=H is H=1. The image R=f(S) also has index two, though the problem does not require this.

The domain assertion follows from the parity homomorphism F -> Z/2 sending a to 0 and b to 1: Schreier rewriting with transversal {1,b} gives precisely the displayed basis. In particular the assignments define a homomorphism on S.

## Faithful matrices and injectivity

Represent a,b in PSL(2,R) by

    A = [[1,2],[0,1]],   B = [[1,0],[2,1]].

This representation is faithful. Indeed, on the real projective line let X_A={|x|>1}, including infinity, and X_B={|x|<1}. For every nonzero integer n, A^n sends X_B into X_A, while B^n sends X_A into X_B. These strict inclusions prove, by the ping-pong lemma, that A and B generate the free product of their infinite cyclic subgroups. For completeness, a nontrivial word conjugate to a power of one generator is visibly nonidentity. Any other word is conjugate to an alternating word whose first and last syllables are powers of A: conjugate a cyclically reduced alternating word by a suitable power of A, avoiding cancellation at either end. This word sends X_B into the disjoint set X_A, and is also nonidentity.

Put

    Q = [[0,-1],[2,1]],   det Q=2.

Direct matrix multiplication gives

    Q A Q^-1 = B^-2,
    Q (BAB^-1) Q^-1 = B^-1 A^2 B,
    Q B^2 Q^-1 = -(B^-1 A).

The minus sign disappears in PSL. Thus f is realized by conjugation by Q on a faithfully represented free group, and is injective. Its image R is therefore an isomorphic copy of S contained in F, as required.

One can also see [F:R]=2 directly. Put c=b^-1 a. The image contains b^2 and c. It contains b^-1 a^2 b = cbc b, and hence bcb=(c^-1)(cbc b); multiplying by b^-2 then gives bcb^-1. Conversely the three original image generators belong to <b^2,c,bcb^-1>. Since {b,c} is a free basis of F, these are the Schreier generators for the kernel of b-parity with c even.

## No nontrivial invariant subgroup

Assume H<=S and f(H)<=H, and choose h in H. Take any integral determinant-one matrix M representing h. Every

    M_n = Q^n M Q^-n,   n=0,1,2,...,

is integral: projectively it represents f^n(h), and a determinant-one lift differs from an integral lift by at most its sign.

These matrices form a bounded set over R. To see this without an approximation, use the positive definite matrix

    P = [[4,1],[1,2]].

It has positive leading principal minors 4 and 7, and Q^t P Q=2P. Therefore Q/sqrt(2) is an isometry of the P-inner product. Conjugation by its powers preserves the associated operator norm of M, so all M_n lie in a fixed bounded subset of the four-dimensional real matrix space. A bounded set contains only finitely many integral matrices. Consequently M_i=M_j for some i<j, and M commutes with Q^(j-i).

No positive power of Q is scalar. Its eigenvalues are

    lambda=(1+i sqrt(7))/2,   conjugate(lambda)=(1-i sqrt(7))/2.

Their ratio z has z+z^-1=-3/2. If a positive power of Q were scalar, z would be a root of unity. Then z+z^-1 would be an algebraic integer, contradicting the fact that the rational number -3/2 is not an integer. Thus Q^k has two distinct eigenvalues for every k>0. Its two complex eigenspaces are those of Q. Any matrix commuting with Q^k preserves both eigenspaces and hence commutes with Q.

Writing M=[[a,b],[c,d]], the equation MQ=QM yields

    c=-2b,   d=a-b.

Since det M=1,

    1 = a^2-ab+2b^2 = (a-b/2)^2 + 7b^2/4.

The entries are integers. If b is nonzero, the right-hand side is at least 7/4, a contradiction. Therefore b=c=0 and a=d=+/-1. Hence M=+/-I and h=1 in PSL. Faithfulness implies h=1 in F. As h was arbitrary, H is trivial. This proves the claimed negative answer.

## Evidence and limits

The proof handles all subgroups and all word lengths; finite checks are supplementary. `scripts/check_f28.py` verifies the three matrix identities, the positive definite form identity, and all 13,120 nonempty freely reduced words through length eight using exact rational arithmetic. Every tested word eventually leaves the iterated domain, with at most 14 successful steps. These bounds are observations, not a substitute for the bounded-orbit proof. `scripts/check_f28_gap.g` independently checks both subgroup indices/ranks and the matrix identities in GAP. Two controls in `scripts/check_f28_controls.py` prevent overgeneralization: conjugation by diag(2,1) preserves <a>, while conjugation by [[0,-1],[2,0]] preserves <a,b^2>. Thus ellipticity and the absence of scalar powers are both relevant to the argument.

The original HTML and its complete F28 rendering have been inspected; the screenshot also includes the adjacent F26/F27 statements because the publisher uses one HTML paragraph. The source background refers to Nekrashevych–Sidki on binary-tree actions. Prior work on simple virtual endomorphisms excludes **normal** invariant subgroups; that conclusion alone is weaker than the one proved here. Literature comparisons are recorded separately in `literature/LEDGER.md` and the claim audit.
