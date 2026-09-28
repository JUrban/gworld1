# F38(a): scope, dependency and computational audit

28 September 2026, approximately 21:47--22:08 UTC. Read with
[the candidate proof](part-a-proof.md). This is one answer to a named
subpart, not a whole-entry F38 solution or an established novel theorem.

## Statement and bibliographic scope

The exact original F38 HTML paragraph and its linked background in
`sources/raw/Back.html` were read. All three subparts were actually viewed
in `research/statement-audits/F38/statement.png`. The archived source
page hash is

    2163a9d6e3c70b36c7df6943042f8b12896430b9e54d24dc23fba5160be4f04d

The input is a pair of words in an arbitrary finite-rank free group;
the equality is required under **every automorphism**, and concerns
cyclic length. Only (b) has the site's red star. Part (c) is a separate
uniform bounded-ratio question and is not answered by this argument.

The candidate is a terminating uniform decision procedure for (a).
Rank zero/one and identity cases are handled separately. Rank two is
explicitly prior: Donghi Lee, *An algorithm that decides translation
equivalence in a free group of rank two*, Theorem 1.2, J. Group Theory
10 (2007), 561--569; [preprint](https://arxiv.org/abs/math/0610833).
The archived paper's introduction and finite Whitehead-chain algorithm
were read, not its whole proof. The site's background credits Lee's
2006 answer to (b). Earlier triage already archives the rank-two answer
to (c), arXiv:0802.0584.

Shpilrain's *Automorphic orbits in free groups: recent progress*, Section 5,
Problem 5.1, still asks the general decision question. The archived file
under `Free-Shpilrain-survey-2510.00889` is the version published on
**17 June 2026**, following a 2025 preprint; it should not be described
as only a 2025 status source. Its Section 5 and publication header were
rechecked. The [GAGTA 2026 program](https://profbsteinberg-math.github.io/BSteinberg-math.github.io/abstracts.html)
contains Siobhan O'Connor's *Translation equivalence in the free group
of rank 2*, announcing a fast algorithm. The abstract is archived as
`F38-GAGTA2026-abstracts`; no full paper or proof was checked.

Searches on 28 September included combinations of “translation
equivalence”, “EDT0L”, “decidable”, “algorithm”, “higher rank”, “2026”,
“injective”, and polynomial/Parikh constraints. No matching all-rank
answer was located. The potential novelty is the application in ranks
at least three. Limited searches cannot establish novelty, and the
elementary polynomial lifting/span method is not claimed as new.

## Precise imported theorems and reading limits

All source prefixes below have retained PDF/HTML bytes, extracted text
where applicable, retrieval metadata and SHA-256 hashes in `literature/raw/`.

- `F38-KapovichLevittSchuppShpilrain0409284`: read Corollary 1.4,
  Theorem A and its Section 2 argument, including Lemmas 2.1--2.2 and
  Proposition 2.3; also Corollary 1.5 and Examples 7.3--7.5. Viewed
  PDF page 4 containing the exact injective-endomorphism equivalence.
  The required implication follows by pulling back a free tree action
  through an injection. General very-small-action results are imported,
  not independently reproved or computationally verified.
- `F38-DiekertElder1701.03297`: read Section 3.4's effective relation
  definition, Section 4's input definition, Theorem 4.3, and the statement
  and normal-form context of Theorem 14.2. Viewed PDF pages 14 and 50.
  Theorem 4.3 explicitly supplies separate letters d_i and the **entire**
  solution relation with regular constraints. Its long recompression
  proof is an imported established result, not fully audited here.
  The candidate uses H=1 and an elementary group-to-monoid reduction,
  avoiding any uncertainty about basis choice in the virtually free
  group formulation or uniformity in the free rank.
- `F38-CiobanuDiekertElder1508.02149`: read the introduction,
  Theorem 4 and Corollary 5. They confirm that components can be
  extracted as h(c_i) and solutions are actual freely reduced words.
  The candidate relies on the later explicit constrained theorem.
- `F38-CiobanuZetzsche2405.07911`: read the introduction, Theorem 5
  and the counting-function formulation in Section 4. This prior work
  handles counting inequations using slice closures of indexed languages.
  It is relevant context, not a substitute for the determinant polynomial
  argument, and its proof was not fully audited here. The present span
  lemma uses the more specific rationally controlled endomorphism
  presentation of an EDT0L relation. No analogous polynomial-identity
  algorithm for arbitrary indexed languages is asserted.

## Adversarial checks of the reduction

1. Nonzero abelianization determinant is **sufficient**, not necessary,
   for injectivity. The proof uses the rank of the image free subgroup
   and Hopficity; it does not equate injectivity with unimodularity.
2. Every automorphism has nonzero determinant. KLSS extends its length
   equality to all injections, making the determinant product exactly
   equivalent to the original universal condition. This is the key
   logical step, rather than an approximation to the automorphism set.
3. Singular endomorphisms cannot simply be included without that factor.
   KLSS Corollary 1.5, M=2, gives translation-equivalent
   u=a b a^-3 b^-1 and v=a^2 b a^-2 b^-1. Sending a to a and b to 1
   gives cyclic lengths 2 and 0 but determinant zero. Both implementations
   checked this control.
4. The group equations retain all endomorphisms. Cyclic reduction is
   imposed on U,V, including the empty word; ordinary reduced length
   cannot silently replace cyclic length.
5. The cancellation-triangle construction preserves the **projected
   full solution relation**. Constraints are imposed in the original
   alphabet with inverse-paired variables. The finite endpoint monoid
   recognizes reduced and cyclically reduced words explicitly.
6. Component counts are separate blocks of a common incidence matrix.
   No assumption that EDT0L is closed under arbitrary transductions
   or an unproved separator-labelling operation is needed.
7. Function-composition order and path-application order are opposite
   under the source convention. Reverse the control automaton before
   applying the matrices. Noncommuting matrix controls detect the error.
8. A support-state product enforces terminal output if necessary;
   simply discarding nonterminal coordinates is not sound. Erasing
   morphisms and the empty output are included in the controls.
9. The algorithm tests universal zero, not existence of a zero. A
   six-initial-zero control still produces a later nonzero witness.
   This is not a solution to existential length-equation constraints.
10. The closed span at each state has a finite-dimensional termination
    argument and consists of spans of actual path vectors. A negative
    certificate supplies an actual accepted path, not a spurious
    linear combination. An injective witness need not be an automorphism;
    the optional Nielsen enumeration is justified separately by KLSS.

## Implemented evidence and exact limits

`scripts/f38_polynomial_identity.py` implements the polynomial span
stage over exact rational arithmetic. It retains actual count vectors
and paths as the basis representatives; applying the base matrix and
then evaluating all monomials has the same effect on these representatives
as the explicit lifted matrix. `scripts/check_f38_polynomial_gap.g`
independently reconstructs the monomial values, replays every path,
checks basis independence and initial-vector inclusion, and checks span
closure under every outgoing transition using GAP's rational linear algebra.
It does not import the Python elimination or a precomputed lifted matrix.

The final suite, `research/certificates/F38-polynomial-tuples`, contains:

- 43 controlled systems, including 24 finite branching systems exhaustively
  compared on all 32 complete paths each (768 paths total).
- Infinite-control examples with true and false polynomial identities,
  delayed failure, parity-restricted acceptance, composition order,
  terminal filtering, erasure, an empty language, a zero polynomial,
  and degree-three determinant-times-length polynomials.
- Three actual tuple-morphism examples testing distinct component
  counts, quadratic relations and repeated output seeds. GAP reconstructs
  their block incidence matrices from the word morphisms themselves.
- 902 total retained basis vectors and 1,151 transition-closure checks
  independently replayed in GAP.
- 2,809 cancellation triangles for all pairs of reduced F_2 words of
  length at most three; 7,225 endpoint-monoid multiplication checks on
  all raw F_2 words of length at most three. These elementary checks
  are Python-only and do not prove the all-word statements.
- 309 free-word records independently replayed in GAP: every pair of
  F_2 image words of length at most two for the KLSS control, and 20
  rank-three scope/boundary examples. Across the records there are 65
  singular maps with differing lengths, 207 nonzero determinants, and
  five nonzero determinant products. These are bounded examples, not
  an exhaustive decision test for arbitrary input pairs.

**The general equation-to-EDT0L construction is not implemented.** These
checks support the new reduction and finite linear algebra; the all-rank
termination claim rests on the written argument and imported theorem.

Recorded processes (one core, 4 GB reservation each, all terminal):

| Run | Result | Scope |
| --- | --- | --- |
| `f38-polynomial-v1` | PASS, 0.37 s | Original 40 systems plus word/reduction checks |
| `f38-polynomial-gap-v1` | Failed success-marker check, 1.83 s | GAP syntax error before checks; actual process exit was zero |
| `f38-polynomial-gap-v2` | PASS, 2.73 s | Independent replay of the original 40 systems and 309 words |
| `f38-polynomial-v2` | PASS, 0.32 s | Final 43 systems, including tuple-specific controls |
| `f38-polynomial-gap-v3` | PASS, 2.68 s | Independent replay of the final suite |

Successful stderr files are empty. The failed GAP source and stderr
are retained. The syntax error required parentheses around `not nonzero`;
the unexecuted three-argument Product call was also replaced by an
explicit word loop. The successful v2 source is reconstructed from that
saved source and those two exact edits. Final sources are copied into
the final certificate directory. Repeated cases across versions are not
counted as additional independent tests.

To reproduce without overwriting original evidence, choose a fresh
output directory and unique recorded-run names:

```sh
python3 scripts/run_recorded.py --name f38-polynomial-replay --cores 1 \
  --memory-gb 4 --timeout 300 --expect 'PASS F38 polynomial stage' -- \
  .venv/bin/python scripts/check_f38_polynomial.py --output scratch/F38-replay
python3 scripts/run_recorded.py --name f38-gap-replay --cores 1 \
  --memory-gb 4 --timeout 300 --expect 'PASS F38 GAP independent' -- \
  bin/gap -q --quitonbreak scripts/check_f38_polynomial_gap.g
```

The second command replays the retained final fixtures. The artifact
manifest hashes the proof, source/dependency evidence, exact checkers,
fixtures and process records. No Kourovka mathematical argument or code
was imported for this candidate. No outside review has yet occurred.
