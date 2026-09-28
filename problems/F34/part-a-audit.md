# F34(a): candidate audit and reproduction

28 September 2026, approximately 22:10--22:22 UTC. This named-subpart
candidate is derived from the polynomial method recorded for F38(a),
plus an elementary subgroup-graph lemma. It is not a new answer to (b).

## Exact statement and literature scope

Read the original F34 paragraph, its definition of positive words, and
the linked background in `sources/raw/Back.html`. Actually viewed both
subparts in `research/statement-audits/F34/statement.png`. The full source
page is retained with SHA-256

    2163a9d6e3c70b36c7df6943042f8b12896430b9e54d24dc23fba5160be4f04d

The question concerns automorphisms of an arbitrary finite-rank free
group and positivity with respect to a fixed initial basis. The candidate
gives a total decision procedure, not just the immediate semidecision
procedure obtained by enumerating automorphisms. The identity convention
is stated separately; no result is based on that edge case.

The website background credits Clark--Goldstein's 2005 stability theorem
for part (b). Their full paper was not obtained or audited. Rank-two
decision algorithms by Goldstein and Lee are prior work. The archived
`Free-Lee-rank2-0802.0584` already supplies the precise rank-two statement;
the June 2026 Shpilrain survey, Section 4, discusses the later complexity
improvements. None of these rank-two/stability assertions is counted anew.

Two further primary sources were archived and their relevant pages read:

- Dinowitz--Koch-Hyde--O'Connor--Olive, *Growth and Language Complexity of
  Potentially Positive Elements of Free Groups*,
  [arXiv:2512.13967v1](https://arxiv.org/abs/2512.13967), 16 December 2025.
  Read the introduction, Question 1.3, and Section 7's discussion of the
  higher-rank algorithmic gap. Actually viewed PDF page 2. The counting
  and language-separation proofs were not audited or used.
- Koch-Hyde--O'Connor--Olive, *Residually Solvable One-Relator Groups*,
  [arXiv:2606.13933v2](https://arxiv.org/abs/2606.13933), 24 June 2026.
  Read the introduction, Question 1.5 and surrounding prior-algorithm
  discussion; actually viewed PDF page 2. The newer book calls this
  question F33, whereas our frozen website calls it F34. The matching
  wording, not the changed book number, identifies the problem. Its
  residual-solvability theorem is not used or claimed to be proved here.

Queries combined “potentially positive”, “algorithm”, “higher rank”,
“monomorphism”, “EDT0L”, and “stably potentially positive”. The current
primary sources explicitly describe a higher-rank gap, but neither they
nor a bounded search prove novelty. The potentially new candidate scope
is (a) in ranks at least three. No originality is claimed for spanning-tree
bases, the embedding-reflection observation, or the finite polynomial
span construction in isolation.

## Proof audit

- The nonzero determinant criterion is used only to guarantee injectivity.
  A singular endomorphism may still be injective; one control exhibits
  exactly this. Conversely every witnessing automorphism has determinant
  +/-1, so discarding determinant-zero maps loses no affirmative inputs.
- The graph proof takes the **image subgroup** of an injection. Its rank
  is the source rank, and pulling a basis back is justified by an actual
  isomorphism, not merely by equality of abelianization ranks.
- Orient geometric edges by positive ambient labels before choosing a
  tree. A positive closed path only traverses those positive orientations.
  Deleting tree edges cannot create a negative basis letter. Tree-basis
  elements themselves may have negative letters in the ambient spelling;
  positivity here concerns their abstract coordinates, which is precisely
  what the pulled-back basis needs.
- Basepoints, graph loops, stems and infinite-index subgroups are permitted.
  No finite-index assumption or free-factor replacement is made.
- The algorithm outputs an automorphism directly by reading the original
  image generators in the tree basis. This avoids an unnecessary search
  for preimages of the basis elements. The map is a composition of two
  isomorphisms, and its image of w is the positive collapsed spelling.
- The regular constraint on the image word forbids inverse letters; it
  is not a constraint on exponent sums alone. The determinant polynomial
  uses separate variable-component counts from the full EDT0L relation.
- Existence of a **nonzero** determinant is the complement of universal
  determinant zero. The polynomial lemma gives exactly this decision.
  No existential polynomial-zero test or unimodularity equation is assumed.
- The equation-solution theorem and polynomial-span proof are imported
  from the explicitly cited dependencies of `../F38/part-a-proof.md`.
  The general recompression construction has not been implemented here.

## Exact computational evidence

The original finite fixture suite is in
`research/certificates/F34-positivity/checks.json` and `fixtures.g`.
Seed: **34092026**. No floating-point arithmetic is used.

`scripts/check_f34_graph.py` folds a subdivided bouquet of the image words
to a finite inverse-labelled graph using vertex identifications. It chooses
a spanning tree, computes the non-tree basis, reads every image generator
in that basis, and produces an explicit automorphism and positive word.
This is a witness constructor for the reflection lemma. It is not an
end-to-end F34 solver, and it returns scope controls rather than purported
negative decisions when its sufficient conditions fail.

The suite contains **270 positive automorphism witnesses**:

- 180 from 36 explicitly designed injective maps: ranks 2, 3 and 4;
  identity, power and positive cyclic-generator embeddings composed with
  3, 7, 10 or 15 elementary Nielsen moves. Each map is tested on five
  positive source words of lengths 0, 1, 2, 5 and 8, pulled back by the
  recorded construction's exact inverse automorphism.
- 90 from 30 arbitrary short-image maps in rank two, selected after
  inspecting 43 maps. Image words have length at most three; the bounded
  search for positive images uses source words of length at most four.
  The selection is explicitly bounded and its non-hits imply nothing
  about the general decision question.

Totals by rank are 150, 60 and 60. There are 36 identity-word controls,
162 input words containing inverse letters, and 168 records with
|det|>1, hence genuinely nonsurjective input endomorphisms. The largest
input word has length 305 and the largest image-generator word has
length 296. The witness automorphisms may differ from the ones used to
construct these examples.

Three further scope controls are retained:

1. A singular map sends a nontrivial commutator to the empty positive word;
   it must not certify potential positivity.
2. The singular map a->a, b->b a b^-1 has free image of rank two. It is
   injective despite determinant zero; the sufficient determinant test
   declines this individual map without declaring the original word negative.
3. The identity map does not send the commutator to a positive word.

`scripts/check_f34_graph_gap.g` uses GAP/FGA independently to check:
the image words and determinant; folded graph labels; spanning-tree
connectivity; the exact tree basis; equality of the subgroup generated
by that basis and the original images; image rank; surjectivity of each
claimed automorphism by membership of every free generator; exact word
images; and positive-path traversal and collapse. It does not load the
Python fold routine. The singular injective control is independently
checked by its free subgroup rank.

| Recorded run | Result | Requested resources |
| --- | --- | --- |
| `f34-graph-v1` | PASS, 1.42 s; 270 witnesses and 3 controls | 1 core, 4 GB |
| `f34-graph-gap-v1` | PASS, 1.98 s; all 273 records | 1 core, 4 GB |

Both actual return codes are zero and both stderr files are empty.
The F38 polynomial-stage checks are shared evidence, not rerun or counted
as another independent test here. No failed research process occurred in
this suite. The written all-rank argument, not these bounded examples,
supplies the candidate decision result.

Reproduce with unique run names and a fresh output directory:

```sh
python3 scripts/run_recorded.py --name f34-graph-replay --cores 1 \
  --memory-gb 4 --timeout 300 --expect 'PASS F34 graph' -- \
  .venv/bin/python scripts/check_f34_graph.py --output scratch/F34-replay
python3 scripts/run_recorded.py --name f34-gap-replay --cores 1 \
  --memory-gb 4 --timeout 300 --expect 'PASS F34 GAP graph' -- \
  bin/gap -q --quitonbreak scripts/check_f34_graph_gap.g
```

The GAP command replays the retained original fixtures. Source snapshots,
dependencies, proof, rendered statement and process records are covered
by the artifact manifest. No Kourovka mathematical argument or code was
imported. Independent specialist review and the novelty audit remain open.
