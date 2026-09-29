# F38(c): implementing the prior filling case

29 September 2026, approximately 03:04–03:15 UTC.
**Prior positive scope and a research tool; no new candidate or novelty claim.**

The stabilizer tool now returns a positive answer when both input words
are filling. It still returns an explicit negative witness when their
conjugacy stabilizers are not commensurable. A non-filling pair which
passes the stabilizer test remains unresolved by this implementation.

The original complete F38 paragraph, its linked background, and its
actual rendered statement were re-read/viewed. We keep its automorphism
quantifier and exclude the identity from ratios. Rank one is immediate;
the implementation is for ranks at least two. This update does not change
the separate F38(a) candidate.

## Exact prior result and attribution

Let H_w be the stabilizer of the oriented conjugacy class [w] in Out(F_r).
Gupta–Kapovich, *The primitivity index function for a free group, and
untangling closed curves on hyperbolic surfaces*,
[arXiv:1411.5523v4](https://arxiv.org/abs/1411.5523v4),
Propositions 4.16–4.17, proves that w is filling exactly when H_w is finite,
and gives an algorithm deciding filling. Their Proposition 2.14 identifies
filling with positive length in every nontrivial minimal very small tree
action. These are prior theorems. The paper appeared online in 2017 and
in *Math. Proc. Cambridge Philos. Soc.* 166 (2019), 83–121,
[DOI](https://doi.org/10.1017/S0305004117000755).

Kapovich–Lustig, *Intersection form, laminations and currents on free
groups*, [arXiv:0711.4337](https://arxiv.org/abs/0711.4337), Proposition
13.8, already proves bounded translation equivalence for any two filling
elements. Its quantifier covers all free tree actions, so implies the
automorphism-only property in F38(c). The proof takes the positive minimum
and finite maximum of the length ratio on compactified Outer space.

The converse exploration initially reconstructed the finite-stabilizer
criterion from splitting and compactness arguments. The literature check
then located the explicit Gupta–Kapovich propositions. **This is a
rediscovery of prior machinery, not an additional result of the run.**

## An implementation using the existing orbit routine

The existing Whitehead graph procedure produces generators of H_w.
Rather than implement another outer-group word problem and enumeration,
we reuse `finite_conjugacy_orbit` from the stabilizer obstruction tool.
Here is the exact termination/correctness argument for this implementation.

Fix a basis x_1,...,x_r and put

    Q = {x_i : 1<=i<=r} union {x_i x_j : 1<=i<j<=r}.

**Detection lemma.** If an automorphism fixes every oriented conjugacy
class in Q, then it is inner.

To see this in the unit-edge Cayley tree, its basis images are conjugates
of their respective x_i, so have length-one axes whose edges carry the
respective basis labels. For i!=j the axes cannot share an edge. If they
were disjoint, the product of the two images would have translation
length 2 plus twice the positive distance between their axes. Its length
is 2 by the hypothesis on x_i x_j, so the axes intersect. The finite Helly
property for subtrees gives a common vertex for all axes. Conjugating
that vertex to the identity makes every image equal to x_i: the signs
are positive because the conjugacy classes are oriented. This proves
the lemma. Conversely, inner maps fix all conjugacy classes.

Let H be any finitely generated subgroup of Out(F_r), supplied by actual
automorphisms and their inverses. Set I=ker(Out(F_r)->GL(r,F_3)).
The previously cited Handel–Mosher aperiodicity theorem implies that
every finite H-orbit of a conjugacy class is fixed by H intersect I.
Consequently

    H is finite iff H.[q] is finite for every q in Q.

The forward direction is immediate. For the reverse direction,
H intersect I fixes Q, so is trivial by the detection lemma. Thus H
injects into the finite group GL(r,F_3). Each of the finitely many orbit
tests terminates by the existing finite matrix search. If one fails,
it supplies an infinite-order outer automorphism in H, with an explicitly
moved conjugacy class. No finite samples or bounded search cutoff decide
the general finiteness assertion.

This also explains two implementation traps. Infinite inner
representatives can generate the trivial outer group. Conversely,
fixing only the individual basis conjugacy classes is insufficient:
in rank three, a->a, b->aba^-1, c->c fixes all three such classes but
has infinite outer order. The word bc detects it. These are explicit
controls below.

For a pair u,v, first run the previous necessary commensurability test.
On failure, retain its negative automorphism witness. On success, decide
whether H_u is finite. Commensurability implies H_v is finite exactly
when H_u is. If both are finite, invoke the two prior filling theorems
and return `boundedly_equivalent_prior_filling_case`. Otherwise return
`unresolved_nonfilling_stabilizers_commensurable`.

This last outcome is not a negative answer. Lee's rank-two bounded pair
is one such control. The procedure does not compute a comparison constant
C, and it is not intended to reproduce Lee's separate complete rank-two
algorithm. It is a terminating partial classifier in arbitrary finite
rank. The general linear-envelope question remains open here.

## Checks and independent replay

The module is `scripts/f38_filling_recognition.py`; its driver is
`scripts/check_f38_filling_recognition.py`. The bounded suite has:

- Six outer-group controls: empty generators; a swap; an inversion;
  an infinite group of inner representatives; a level-three Nielsen
  automorphism; and the basis-conjugating rank-three trap above.
- Six word controls: two rank-three balanced cyclic words, a proper
  power of one, a rank-two balanced word, a primitive, and a commutator.
- Four pair controls: the two filling rank-three words; a filling word
  and a primitive; Lee's prior rank-two pair; and that pair included in
  rank three, where boundedness fails.

The balanced words come from deterministically shuffled Euler circuits
on the directed reduced-letter graph. Each allowable ordered bigram
occurs exactly once. Seeds 0 and 1 are stored in the driver; word lengths
are 30 in rank three and 12 in rank two. Full computed words are retained
in JSON. They are test inputs, not a probabilistic proof of filling.
The algorithm itself verifies the stabilizer condition.

The Python suite exported 59 certificate fixtures. The separate GAP
replay uses GAP's free group word arithmetic to check explicit two-sided
inverses, conjugacy-class actions, invariance of finite orbits, and the
level-three matrices and moved classes of negative witnesses. It reuses
the already checked GAP replay module, whose exact source is copied into
this certificate directory. It does not independently reconstruct the
complete Whitehead graphs; their completeness still rests on classical
peak reduction and the Python implementation. Neither computation
verifies the imported tree or aperiodicity theorems.

The Python run `f38-filling-recognition-v1` passed in 1.925 seconds;
`f38-filling-recognition-gap-v1` passed in 1.825 seconds. Both have empty
stderr. GAP verified seven infinite-orbit witnesses, 52 finite invariant
orbits, 287 two-sided inverse pairs and 293 orbit transitions. There were
no failed mathematical runs in this supplement.

Run outcomes and artifact hashes are recorded alongside the fixtures in
`research/certificates/F38-filling-recognition/`. Python 3.12 and GAP
4.16.1 were used, one CPU slot and 4 GB per run. The drivers refuse to
overwrite evidence; use a disposable copy when regenerating outputs.

## Source inspection and limits

- Gupta–Kapovich 1411.5523v4: Definitions 2.11–2.12 and Proposition 2.14
  read as text; Propositions 4.16–4.17 and their local proofs read and
  actually viewed on PDF/printed page 20. Their imported splitting,
  compactness and McCool results are not independently re-proved here.
- Kapovich–Lustig 0711.4337: Section 13 read as text; Definition 13.7,
  Proposition 13.8 and its proof actually viewed on PDF/printed page 38.
  This updates the earlier note's historically accurate statement that
  no page of that source had yet been visually inspected.
- Solie 1007.4022: Sections 2–3 re-read as text. The finite-stabilizer
  criterion is taken from the later explicit Gupta–Kapovich statement.
- Solie 2311.01668: introduction and Section 4 read as text, no visual
  inspection claimed. Its finitely generated subgroup/splitting problems
  have broader scope than recognizing a single filling word. It does
  not contradict the prior single-word algorithm.

The NSF-hosted copy of Gupta–Kapovich timed out; the arXiv v4 PDF was
successfully archived instead. The rendered page 19 was generated before
locating the propositions on page 20; it was not visually inspected.
All downloaded sources retain URL, retrieval time and SHA-256 metadata.
This is a targeted source audit, not an exhaustive survey.

**Count unchanged:** six whole-entry candidates, three partial candidates,
zero established novel results. The new positive scope is explicitly prior.
