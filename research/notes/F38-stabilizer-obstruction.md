# F38(c): a decidable stabilizer obstruction

29 September 2026, approximately 02:03–02:22 UTC.
**Research tool and necessary condition; not a solution of F38(c).**

For nontrivial words u,v in a finite-rank free group, bounded translation
equivalence implies that their conjugacy stabilizers in Out(F) are
commensurable. This necessary condition is decidable. When it fails, the
procedure produces an explicit automorphism theta such that one word's
conjugacy class is fixed and the other's iterates have cyclic lengths
tending to infinity. The procedure has been implemented and its finite
orbit certificates and failure witnesses replayed independently in GAP.

The converse is **not proved**. A passed test is reported as
`necessary_condition_passed_only`, never as bounded equivalence. No new
whole-entry or named-subpart candidate is added. The existing F38(a)
candidate is unchanged; rank-two F38(c) is already prior work of Lee.

Subsequent supplement: [filling recognition](F38-filling-recognition.md)
adds the already published positive case of two filling words. The
original necessary-condition module retains its conservative return
value; the separate wrapper invokes the prior filling theorems only
after certifying finite stabilizers.

## Original quantifier

The complete frozen F38 paragraph, background and actual rendered
statement were re-read/viewed. Part (c) concerns cyclic lengths under
**automorphisms of the specified ambient free group**. It is not the
stronger quantifier over embeddings or arbitrary free tree actions; the
distinction and a prior counterexample remain in
`F38-bounded-scope-boundary.md`.

We restrict the discussion to nonidentity words, so the ratios are
defined. Rank one is immediate: automorphisms preserve the absolute
exponent, so any two nonidentity words are boundedly equivalent. The
implementation below is intended for ranks at least two.

## Necessary condition

Write H_u=Stab_Out(F)([u]) and H_v=Stab_Out(F)([v]), where [u] is the
oriented conjugacy class. Suppose a common C satisfies

    C^-1 ||phi(u)|| <= ||phi(v)|| <= C ||phi(u)||

for every automorphism phi. For phi in H_u, the right side is the fixed
number C||u||. There are only finitely many conjugacy classes of bounded
cyclic length in a finitely generated free group. Thus H_u has a finite
orbit on [v]. By orbit–stabilizer,

    [H_u : H_u intersect H_v] < infinity.

Interchanging u and v gives finite index in H_v too. This proves the
claimed commensurability. Only conjugacy classes, rather than elements
or unoriented cyclic subgroups, are used.

## Exact finite-orbit decision for a finitely generated outer subgroup

Let H be any subgroup of Out(F_r) supplied by finitely many automorphisms
of F_r, with their inverses. Let

    rho: Out(F_r) -> GL(r,F_3),
    I = ker(rho),  H_0 = H intersect I.

The imported aperiodicity theorem of Handel–Mosher says that, for
theta in I, a theta-periodic conjugacy class is fixed by theta. Therefore

    H.[w] is finite  iff  H_0 fixes [w].                 (1)

For the forward implication, every theta in H_0 permutes the finite
H-orbit, so some positive power fixes [w]; apply aperiodicity. For the
reverse implication, H_0 has finite index in H, bounded by |GL(r,F_3)|.

One algorithm computes Schreier generators of H_0 through the finite
matrix image and checks their action on [w]. The implementation uses an
equivalent search which also gives a compact failure witness:

1. Explore rho(H), keeping one representative h_A and one conjugacy class
   [h_A(w)] for each matrix A. Start with the identity.
2. For every representative and input generator s, compute B=rho(s)A
   and the class [s h_A(w)].
3. If B is new, retain s h_A as its representative. If B is already
   stored, compare the two classes.
4. If they differ, theta=h_B^-1 s h_A lies in H_0 and does not fix [w].
   The aperiodicity theorem proves that [theta^n(w)] are pairwise distinct.
   Consequently their cyclic lengths tend to infinity.
5. If the finite matrix graph closes with every comparison consistent,
   the stored classes form a finite H-invariant set containing [w].

There are at most

    |GL(r,F_3)| = product_(i=0)^(r-1) (3^r-3^i)

matrix states. This is a terminating mathematical algorithm; it is not
a claim of practical complexity in large rank. Even if the given
generators are not symmetric, the finite matrix semigroup generates the
whole matrix group. In the consistent case, each generator permutes the
finite invariant set, so inverses preserve it as well.

A common fixed conjugacy class is detected directly before exploring
matrices. The script compares cyclic rotations of the freely reduced
word and does not identify a word with its inverse. The inversion control
below matters: replacing the level-three kernel by the mod-two kernel
would make the invoked aperiodicity assertion false.

## Computing the full stabilizers

The other imported ingredient is ordinary Whitehead peak reduction.
First minimize [u] by strictly length-decreasing Whitehead moves, recording
the automorphism mu. Starting from the resulting minimal class [u_0],
construct the finite component of the graph whose vertices are cyclic
classes of length ||u_0|| and whose labelled edges are all length-preserving
Whitehead moves. Loops and distinct labels between the same vertices must
be retained.

Choose a rooted spanning tree, with path label p_x at each vertex x. For
each edge s:x->y, the loop label p_y^-1 s p_x fixes [u_0]. Peak reduction
implies that these labels generate the full outer stabilizer: every outer
automorphism fixing [u_0] has a factorization staying at the minimal
length throughout. Conjugating the labels by mu transports them to H_u.
All operations are effective on finite reduced words. Inner representatives
and redundant loop labels may be retained harmlessly.

This constructs generators for H_u and H_v. Apply (1) in both directions
to decide their commensurability. Equivalently, the necessary condition
is the equality

    H_u intersect I = H_v intersect I.                 (2)

Indeed, commensurability makes every member of H_u intersect I periodic
on [v], hence fixed; this gives one inclusion in (2), and the reverse
inclusion is symmetric. Conversely, equality in (2) gives a common
finite-index subgroup.

If either finite-orbit test fails, its theta is in the stabilizer of the
other input word and supplies a certified negative F38(c) answer for
that pair. The two-sided test is essential: for u=a and v=[a,b] in F_2,
H_u has finite orbit on [v], but H_v has infinite orbit on [u].

## Implementation and checks

The standalone module is `scripts/f38_stabilizer_obstruction.py`.
It enumerates signed basis permutations and all second-kind Whitehead
moves, checks their explicit inverses, constructs the minimal-word graph,
and runs the finite matrix-image test. It has no search cutoff that is
interpreted as a mathematical answer. Resource limits remain external
through the recorded runner.

The main suite contains eight pair cases: distinct primitives; a
commutator versus a primitive; Lee's prior bounded pair and an automorphic
image of it; the same Lee pair included in rank three; two different
rank-three commutators; two powers of the same commutator; and nonminimal
primitive powers. Four isolated orbit controls cover a swap, inversion,
a level-three Nielsen twist and an inner automorphism. A supplement adds
the reversed commutator/primitive pair, where the first direction passes
and the second fails, and a negative example requiring transport through
the initial minimization.

For example, for u=a and v=a^2 b a^-1 b^-1 in F(a,b,c), the computed
witness fixes a,c and sends b to c b c^-1. It is identity on homology;
the cyclic lengths of its images of v are 5+4n for n>=0, while u has
length one. This agrees with the existing free-factor scope warning.
The positive rank-two answer for the original pair is credited to Lee;
a passed stabilizer test is not used to reprove its bounded ratio.

GAP independently evaluates the free-group words and checks every
two-sided inverse, each finite orbit's invariance under its supplied
generators, and every negative witness's level-three matrix, fixed class
and moved class. The main GAP replay verifies five infinite-orbit
witnesses, eleven finite invariant orbits, 310 inverse pairs and 325 orbit
transitions. The supplement checks the reverse-direction and witness-
transport branches separately. GAP does not independently reconstruct
the complete Whitehead graphs; completeness of their generators rests on
the written algorithm, peak reduction and the Python implementation.
The imported aperiodicity theorem is not established by bounded samples.

Recorded runs, all at one CPU slot and 4 GB per process:

- `f38-stabilizer-obstruction-v1`: main Python suite passed in 0.269s,
  with empty stderr.
- `f38-stabilizer-obstruction-gap-v1`: failed before its first fixture on
  an unavailable `KroneckerDelta` identifier. Its warning, error, exact
  source and misleading GAP exit code zero are preserved. The runner
  recorded failure because the required marker was absent.
- `f38-stabilizer-obstruction-gap-v2`: explicit diagonal/off-diagonal
  checks replaced that identifier; all sixteen fixtures passed in 1.824s
  with empty stderr.
- `f38-stabilizer-supplement-v1`: two additional branch controls passed
  in 0.119s with empty stderr.
- `f38-stabilizer-supplement-gap-v1`: separate GAP replay of the exported
  supplementary fixtures passed in 1.774s with empty stderr: two
  infinite-orbit witnesses, one finite invariant orbit, eleven inverse
  pairs and eighteen orbit transitions. The two successful GAP replays
  together verify nineteen fixtures, 321 inverse pairs and 343 transitions.

Sources, fixtures, records and hashes are in
`research/certificates/F38-stabilizer-obstruction/`. The general solver
depends only on Python's standard library. Python 3.12 and GAP 4.16.1 were
used. There is no random seed. Verification may be rerun after the
deadline without restarting the experiment, using a disposable copy for
the output-producing Python checkers, which refuse to overwrite evidence.

## Primary sources and reading limits

- Handel–Mosher, *Subgroup decomposition in Out(F_n), Part II: A relative
  Kolchin theorem*, [arXiv:1302.2379](https://arxiv.org/abs/1302.2379),
  Theorem 4.1, printed/PDF page 19: exact aperiodicity statement read and
  viewed, together with the level-three definition. The substantial
  train-track proof is imported, not independently re-proved here.
- Kapovich, *Generic-case complexity of Whitehead's algorithm, revisited*,
  [arXiv:1903.07040v3](https://arxiv.org/abs/1903.07040v3), 2 August 2026:
  Definitions 2.1–2.3, Propositions 2.4–2.5 and 3.14, Remark 3.15 and
  Corollary 3.16 read. Page 14 was viewed. These credit the classical
  Whitehead/McCool stabilizer construction; it is not a new theorem here.
- Guerch, [arXiv:2601.03947v1](https://arxiv.org/abs/2601.03947v1),
  introduction and Theorem 1.1 read as text. It credits the original
  Handel–Mosher free-group theorem and supplies a different proof in a
  broader setting. Its full proof and PDF typography were not audited.
- Solie, [arXiv:1007.4022](https://arxiv.org/abs/1007.4022), Sections 2–3
  read as extracted text; its sufficient filling criterion and generic
  class are prior. Kapovich–Lustig,
  [arXiv:0711.4337](https://arxiv.org/abs/0711.4337), introduction and
  Corollary 1.8 checked as text: pairs of filling elements satisfy even
  the stronger tree-action boundedness. Neither source is being asserted
  to settle arbitrary F38(c) pairs. Their full PDFs are archived, but no
  full proof audit or visual inspection of these two papers is claimed.

No matching full higher-rank F38(c) algorithm was located in the bounded
literature search. This is not a novelty certificate for the present
necessary condition, which is a short consequence of the cited machinery.

## Remaining mathematical step

Determine whether commensurability of H_u and H_v is sufficient for
bounded translation equivalence, or construct a pair disproving that
implication. Neither a proof nor a counterexample is currently available
in this work. Finite stabilizer orbits only control automorphisms fixing
one conjugacy class; they do not by themselves give a uniform linear
comparison along all automorphisms.

Compactness of projective length functions alone is insufficient: limits
may make both words elliptic while their lengths approach zero at
different rates. Nor may the automorphism quantifier be replaced by all
tree actions or embeddings. The existing rank-two Lee example already
blocks that replacement. This missing converse, or an additional
condition addressing it, is the next substantive F38(c) task.
