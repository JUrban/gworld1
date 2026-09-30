# Forty-eight hours with GroupWorld

**[Paper — PDF, version 1](paper/gworld-experiment.pdf)** ·
[Paper source and build instructions](paper/README.md) ·
[Final report](reports/FINAL_REPORT.md) ·
[Results and review guide](reports/CURRENT_RESULTS.md) ·
[Scope ledger](reports/RESULT_SCOPE.md)

This repository records a 48-hour mathematical research experiment by
Codex `gpt-6-astra` (OpenAI), organized by Michael Kinyon and Josef Urban,
with Vladimir Shpilrain, who hosts the problems and suggested the experiment.
The input was the collection of
[open problems in combinatorial group theory](https://shpilrain.ccny.cuny.edu/gworld/problems/oproblems.html)
selected by Gilbert Baumslag, Alexei Myasnikov and Vladimir Shpilrain,
including its background notes and
[Hall of Fame](https://shpilrain.ccny.cuny.edu/gworld/problems/Halloffame.html).

The run took place from **28 September 2026, 10:04:49 UTC, to
30 September 2026, 10:04:49 UTC**, with requested local limits of generally
20 CPU cores and 100 GB RAM. The agent used mathematical literature, GAP,
exact programs and selected Lean formalizations. The archived input has
**195 numbered entries in 16 categories**; it includes prior solutions and
partially answered questions, so this is not a set of 195 verified open problems.

## Results

The deadline record contains **ten whole-entry coverage candidates and two
partial entries**. Complete coverage combines eleven proposed components
with four credited prior subparts. **Independent specialist review of
correctness and novelty is pending; no result has established novelty.**
The paper presents all twelve arguments, their dependencies and the limits
of the supporting checks. Its early results table precedes the proofs.

| Entry | Proposed result and scope |
|---|---|
| [F28](problems/F28/proof.md) | An explicit index-two virtual isomorphism of a free group has no nontrivial forward-invariant subgroup, without assuming finite generation or normality. |
| [H4](problems/H4/proof.md) | Explicit Dehn-presentation output cannot be uniformly polynomial in an arbitrary hyperbolic input presentation, even for infinite virtually free groups with torsion. |
| [M0](problems/M0/proof.md) | Primitive-preserving endomorphisms of finite-rank free metabelian groups are automorphisms; lower-rank results and the Jacobian criterion are prior. |
| [F41](problems/F41/multipattern-proof.md) | Automorphic-orbit ball growth of a nontrivial nonprimitive word in rank r ≥ 2 is √(2r−1), using substantial prior definable-set results. |
| [GA3](problems/GA3/proof.md) | Nonabelian Λ-free groups discriminate their free square, with no finite-generation assumption; the nontrivial abelian case is negative. |
| [F34](problems/F34/part-a-proof.md) | Potential positivity is decidable in every finite rank; stability part (b) and rank two are prior. |
| [F38](problems/F38/README.md) | Translation equivalence and bounded translation equivalence are decidable in every finite rank; part (b) and rank-two decisions are prior. |
| [N5](problems/N5/proof.md) | Direct decomposition is decidable for finitely generated nilpotent groups, including torsion; factors are constructed. |
| [N8](problems/N8/general-proof.md) | Single commutator equations are decidable and constructively solvable in every finite-rank free nilpotent group, without a class cutoff; part (a) is prior. |
| [N9](problems/N9/proof.md) | The retract problem is undecidable in one fixed torsion-free class-two group, even for isolated Heisenberg input subgroups; class-wide undecidability and part (b) are prior. |
| [G9 — partial](problems/G9/flow-growth-proof.md) | Effective approximation of free-metabelian growth; certified rank-two bounds **2.676891785 ≤ λ₂ ≤ 2.943737759**. The exact value is not determined. |
| [B9 — partial](problems/B9/infinite-family-proof.md) | Infinitely many special braids on five strands, hence in every Bₙ for n ≥ 5. Counts 1, 2, 4 on one, two, three strands follow from prior work; the four-strand exponent-two sector remains unclassified. |

The [review guide](reports/CURRENT_RESULTS.md) links every controlling proof,
source comparison and supplement. The [scope ledger](reports/RESULT_SCOPE.md)
classifies all 195 entries and distinguishes whole entries from named parts.
F11 and F42 were rediscovered and credited to prior work; Achyuth Jayadevan's
prior Lean developments for A5 and S5 were reproduced and excluded from the
candidate count. Failed approaches and corrections remain in the record.

N5 and N8 have full candidate commands. F34 and F38(a) have implemented
interfaces and finite checks, but their imported full equation-to-language
construction is unimplemented. Lean checks selected lemmas; no complete
candidate is claimed to be fully formalized. The checks were organized by
the same research agent, not an external referee.

## Paper and frozen record

The [paper](paper/gworld-experiment.pdf), version 1 of 30 September 2026,
was prepared after the experiment. Research results and their deadline
assessment remain unchanged.

- [Last research commit: `401213c`](https://github.com/JUrban/gworld1/tree/401213c09222ebebaf99589553258cf74a918187)
- [Administrative handoff: `0d6b855`](https://github.com/JUrban/gworld1/tree/0d6b855fd6d9d9e5ddb5dbd186a2a590164c1341)
- [Deadline snapshot](research/audits/deadline-snapshot-manifest-v1.json)
- [Final report](reports/FINAL_REPORT.md), [reproduction guide](reports/REPRODUCTION_GUIDE.md), [research log](research/LOG.md) and [progress history](reports/PROGRESS.md)
- [Standalone paper source archive](paper/gworld-experiment-source.tar.gz)

Paper artifact links use the handoff commit. Later paper builds and editorial
checks have separate records under `paper/data/`; they do not extend the
research clock. The [original handoff README](paper/data/README-at-handoff.md)
is preserved as well.

## Sources and relationship to Kourovka

The [offline catalogue](data/CATALOG.md), [source manifest](sources/manifest.json)
and per-entry folders preserve the publisher bytes downloaded on
28 September 2026. The archive includes the problem pages, background pages,
Hall of Fame and locally linked PDF. It retains 49 heading stars, 11 entries
with subpart stars and 69 Hall of Fame links to 58 distinct entries. Those
historical annotations are not an exhaustive present-day status survey.
See the [status notes](docs/STATUS_NOTES.md), [source limitations](sources/README.md)
and [dated literature ledger](literature/LEDGER.md).

This follows the [Kourovka experiment and research archive](https://github.com/JUrban/kour1)
and its [version 4 paper](https://github.com/JUrban/kour1/blob/dce7931e980c7db83100a07fbe084fc1dd655fdb/paper/kourovka-experiment.pdf).
The two experiments have separate histories, corpora, clocks and assessments.
This was not a clean-room experiment: shared software and methodological
lessons are disclosed in the [provenance](provenance/kourovka.json),
[lessons](docs/KOUROVKA_LESSONS.md) and [transfer ledger](research/transfers.jsonl).
Kourovka's external review does not constitute a review of the GroupWorld
arguments. Different inputs and review histories preclude interpreting raw
candidate counts as a controlled comparison.

## Reproduction

Start with the [reproduction guide](reports/REPRODUCTION_GUIDE.md) for pinned
software, exact certificates, review commands and intentional omissions.
The GAP installation and all generated data are not bundled. The original
research runner refuses jobs after the deadline; replay belongs in a separate
checkout with new outputs and separately dated review records.

The preparation utilities need Python 3 and Git. Configure GAP using
[the local-tools example](config/local-tools.example.json) or `GWORLD_GAP_ROOT`.
The authoritative clock is [state/session.json](state/session.json); the
[protocol](docs/PROTOCOL.md) and [environment record](provenance/environment.json)
describe the setup. For the paper alone, use its [build instructions](paper/README.md).

All retained blobs are below 90,000,000 bytes; no history filtering was needed
for this publication. The reproduction guide identifies omitted data and
its compact replacements. Enable the local size check after cloning with
`git config core.hooksPath .githooks`.

Michael Kinyon's work was carried out during a research visit to the
AI4REASON institute. This work was supported by the ERC grant NextReason
(Grant Agreement No. 101200949) and the
[sponsors of the AI4REASON institute](https://ai4reason.eu/sponsors.html).
