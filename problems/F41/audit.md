# F41 rank-two candidate: audit and reproduction

Historical audit. The [29 September multipattern audit](multipattern-audit.md)
records the later full intended-scope candidate; the findings and counts
below describe the earlier checkpoint.

28 September 2026, approximately 18:22--18:45 UTC. Read together with
`rank-two-proof.md`. This is one partial candidate; the full problem
and novelty assessment remain open here.

## Statement fidelity

Read the full frozen `sources/raw/probfree.html`, the F41 paragraph,
and the F41 background in `sources/raw/Back.html`. Rendered and actually
viewed `research/statement-audits/F41/statement.png`. Source hash:

    2163a9d6e3c70b36c7df6943042f8b12896430b9e54d24dc23fba5160be4f04d

The question concerns the entire automorphism group, not iterates of a
single automorphism. We count elements, not orbits. Its literal identity
exception is acknowledged but not counted as a solution. We use balls
and spherical limsup, since proper powers give a parity obstruction to
some spherical limits.

## Source checks and limits

All archived PDFs have retrieval metadata and SHA256 hashes in
`literature/raw/` with the indicated prefix.

- `F41-Puder-Wu-1304.7979`: read Question 5.4 and its context; physically
  viewed PDF page 18. The parameter mu minimizes positive occurrences
  **over the whole automorphic orbit**. It is not merely the minimum
  occurrence count in the original spelling. The stronger cyclic-rate
  conjecture is not claimed in this candidate.
- `F41-Puder-1212.5216`: read Lemma 4.1 and proof, Claim 4.2,
  Proposition 4.3 and proof, and Theorem 8.2 with its scope. Physically
  viewed pages 14 and 37. The twice-traversal observation and the
  primitivity-rank threshold bound are credited to Puder. In particular
  the pi=2, r>=5 orbit consequence is excluded from possible new scope.
- `F41-Erlandsson-Souto-1508.02265`: read the introduction and precise
  Theorem 1.1; viewed page 1. Imported the theorem, not an independent
  audit of its 44-page proof. Its nonperipheral/not-a-proper-power
  restriction is handled explicitly, with powers and the peripheral
  commutator treated separately. Only the easy upper comparison of
  geodesic length by word length is needed in the cusped metric.
- `F41-Shpilrain-White3`: read the relevant conjectures, Proposition 2
  proof and references in extracted text. Its rank-two assertion cites
  Khan, but readily accessible descriptions of Khan concern words of
  **minimum length** in their orbit. The original Khan paper/thesis
  was not obtained. We therefore do not use that citation to justify
  counting words of all lengths. The curve-counting theorem supplies
  the required bound independently. No error in Khan's work is alleged.
- `F41-Culler-1981`: read the text of Theorem 3.1 and surrounding
  remarks. Fixed-genus and fixed-square-length counting was considered
  as a different route, then set aside. The current proof does not
  depend on this paper; no complete proof/visual audit is claimed.
- `F41-Orbit-blocking-2505.00477`: read the introduction and relevant
  scope. The paper resolves F40, already credited elsewhere; it does
  not supply the sharp F41 growth bound used here.
- `F41-Shpilrain-survey-2510.00889`: read the author-posted full survey
  through web extraction, including its distinction between minimal
  words and a fixed orbit, then archived the arXiv PDF and text. This
  is a current scope check, not evidence that every special case of
  F41 remains new. No full proof audit of its referenced results.

Searches included combinations of "automorphic orbit", "primitivity
rank", "rank two", "growth", "Stallings", "monomorphic", and
"Mirzakhani", as well as the exact Khan and curve-counting titles.
No matching theorem for the claimed remaining range was located in
this bounded search. This is **not** novelty certification. The
transfer estimate is a short combination of substantial prior results
and may already be known to specialists.

## Adversarial proof checks

- The containing rank-two subgroup is fixed before applying ambient
  automorphisms. Its images have the same rank; changing their markings
  changes the abstract word only within one Aut(F_2) orbit.
- Core graphs have finitely many shapes only after suppressing
  degree-two vertices. Moving the starting point to a branch vertex
  costs a factor of at most the ambient word length; it is not omitted.
- Bridges are permitted, notably the barbell graph. The twice-traversal
  argument distinguishes bridges and nonbridges.
- The abstract path is counted through its word in a fixed tree basis.
  Collapsing the tree leaves a cyclically reduced word; for a fixed
  basepoint this word uniquely determines the reduced path.
- The label entropy uses n-L, not n: each extra letter in an edge
  label is charged at least twice. Arbitrarily long paths do not
  multiply the bound by all possible rank-two reduced words; only one
  polynomial-size automorphic orbit is permitted.
- Foldedness ensures the length identity. We may subsequently
  overcount label assignments, but cannot use the identity for an
  arbitrary nonimmersed labelled graph.
- Proper powers, the identity, peripheral curves, arbitrary
  homomorphisms, and primitive words are treated separately. In
  particular a^2 b^3 under **noninjective** substitutions produces
  every word, so extending the estimate to arbitrary maps would be false.
- The conjugacy lower bound uses reduced concatenations with distinct
  prefixes, avoiding an unproved estimate for centralizer cosets.

## Finite computational checks

These checks exercise the combinatorial steps and representation
conventions. They neither prove the infinite bound nor replace review.

`scripts/check_f41_graph_transfer.py` exhausts all based cyclically
reduced paths of topological length at most eight in the three
rank-two leaf-free shapes (rose, theta, barbell), at every vertex.
Whitehead reduction in rank two classifies primitive roots, identifying
the paths carried by a proper free factor. It checks injectivity of
the path-to-tree-basis encoding, cyclic reduction, and twice-traversal
for every filling nonprimitive path. Totals:

| Shape | Paths checked | Filling nonprimitive paths |
| --- | ---: | ---: |
| Rose | 9,856 | 9,256 |
| Theta | 696 | 432 |
| Barbell | 496 | 224 |

There are 11,048 paths overall, including 9,912 filling nonprimitive
ones. Primitive single-traversal controls and proper-factor unused-edge
controls are retained, rather than incorrectly asserting the lemma
for them.

With seed 20260928, the script also creates 18 marked immersed labelled
graphs, covering all three shapes, ambient ranks three and four, and
the abstract words a^2 b^3, [a,b], and a^2 b^2. Each marking is obtained
by six explicitly recorded Nielsen moves. Edge labels have lengths
one through five; the largest resulting word has length 136.

The separate GAP/fga checker replays the Nielsen moves, verifies that
they generate all of F_2, checks the abstract and labelled word
identities, tests immersion independently, verifies no cancellation
in the cyclic path and confirms that each image subgroup has rank two.
The last condition independently certifies injectivity of its
two-generator marking. All 18 records passed.

Reproduce from the repository root, using new run names:

```sh
python3 scripts/run_recorded.py --name f41-graph-transfer-v2 --cores 1 --memory-gb 8 --timeout 180 --expect 'PASS F41 finite graph transfer checks' -- .venv/bin/python scripts/check_f41_graph_transfer.py
python3 scripts/run_recorded.py --name f41-graph-gap-v2 --cores 1 --memory-gb 8 --timeout 180 --expect 'PASS F41 GAP graph fixtures' -- bin/gap -q --quitonbreak scripts/check_f41_graph_gap.g
```

The completed v1 runs took 0.42s and 1.87s respectively, each on one
core with an 8GB per-process limit, and both had empty stderr. The
certificate directory is `research/certificates/F41-graph-transfer/`;
its artifact manifest hashes the exact JSON and GAP fixtures. No
failed computational run occurred in this pass. No asymptotic rate
was estimated by fitting finite data.

## Counting decision

Count one additional **partial candidate**, provisionally: pi(w)=2 in
ambient rank three or four. Do not count a new whole-entry solution,
the already known rank-two/proper-power/large-rank cases, the transfer
lemma as a separate problem, or an established novel theorem.
