# F41 closing proof and dependency audit

30 September 2026, approximately 02:08--02:10 UTC. Same-agent review,
not an independent referee report or novelty determination.

Read the full current multipattern proof and its original, follow-up,
and dependency-boundary audits. Reread the full original free-group
HTML page and F41 background; actually viewed the retained F41 rendering.
Reread KM Definitions 5--6 and Theorem 13 with its local proof and
Lemma 14; reread Pillay's generic-element definition, Fact 1.10,
Theorem 2.1 and its proof. Actually viewed the four retained primary
source images of KM pages 3/9 and Pillay pages 6/7.

The argument remains a consequence of the **full arbitrary-definable-set**
multipattern theorem, not merely a theorem about definable subgroups or
density zero. These are the published dependencies being used:

- Kharlampovich--Myasnikov, *Definable sets in a hyperbolic group*,
  [arXiv:1111.0577](https://arxiv.org/abs/1111.0577), archived v5,
  Definitions 5--6 and Theorem 13, specialized to one free variable.
- Pillay, *On genericity and weight in the free group*,
  [arXiv:0812.1692](https://arxiv.org/abs/0812.1692), genericity over the
  empty parameter set, Fact 1.10 and Theorem 2.1(i).

The closing check separates three implications.

1. **Repeated pieces cover the word outside fixed coefficients.** The
   first noncancelling pattern has finitely many variable occurrences.
   Each of their values is a piece of the output word, even if the second
   occurrence is not another formal variable occurrence in that pattern.
   For each displayed block a distinct second occurrence can therefore
   be chosen. There are polynomially many choices of lengths, positions
   and orientations. A signed identification graph has no nonconstant
   singleton component in a realizable scheme, giving at most (n+C)/2
   components. The quotient of the position path is connected; a spanning
   tree leaves at most 2r-1 choices at each nonroot component. This is the
   square-root exponent. One repeated piece without full coverage would
   not imply it.
2. **The correct side of the dichotomy is selected.** A nonprimitive w
   fails a parameter-free formula phi in the generic type. Thus every
   automorphic image of w lies in P=not phi. The complement contains a
   basis element realizing the generic type over the empty set, so finitely
   many translates cover the group. The bound in the first implication
   rules out a sub-multipattern complement; KM then puts P itself in that
   class. Neither the orbit nor the primitive set is assumed definable.
   Fixed coefficients in the resulting pattern do not change the absence
   of parameters in phi.
3. **The claimed growth convention follows.** Nontrivial reduced
   conjugates with prescribed prefix lengths give the matching lower
   bound in every sufficiently large ball and on a subsequence of
   spheres. Thus the conclusion is a ball limit and a spherical limsup.
   Empty spheres can prevent a spherical limit. The identity exception,
   rank-one case, dependence of constants on w, and absence of a sharper
   cyclic-orbit formula remain explicit.

The finite scheme checks and the separate GAP enumeration remain their
previous finite evidence; no rerun was needed. They do not establish KM's
quantifier-elimination/NTQ dependencies or Pillay's stability/free-factor
dependencies. The later source proving the definable-subgroup theorem
cannot replace KM's arbitrary-set theorem here.

Three fresh exact-phrase searches concerning multipattern orbit growth,
square-root orbit growth and corrections to the definable-set theorem
returned mostly irrelevant material or the already archived problem
background. They changed no bibliographic conclusion and are not evidence
of novelty. No new proof gap was identified in this pass. F41 remains one
whole intended-scope candidate with specialist review outstanding.
