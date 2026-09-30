# GroupWorld 48-hour experiment — report draft

**Interim closing draft. The experiment is still active.** The authorized
window is 28 September 2026, 10:04:49.670358 UTC through 30 September 2026,
10:04:49.670358 UTC. This document does not freeze the deadline result or
certify completion. The final report must replace this status with the
observed closeout, exact snapshot and final evidence inventory.

## Current outcome

The current record contains **ten whole-entry coverage candidates and
two partial-entry candidates, with zero established novel results**.
Whole-entry coverage combines proposed arguments with explicitly credited
prior answers. Every candidate still requires independent specialist
review of correctness and novelty. Same-agent rereads, separate programs
and formal verification of fragments have different evidential scopes;
none is described here as an outside mathematical referee.

The ten whole-entry candidates comprise six unpartitioned proposed
answers and five proposed answers to named parts, together with four
credited prior named parts. These eleven proposed components are not
eleven established new theorems. Known rank-restricted cases inside a
component are also credited. The [scope report](RESULT_SCOPE.md) gives
the complete breakdown, qualifications and source links; its
[JSON ledger](result-scope-ledger.json) retains all 195 catalogue IDs.
The 183 other entries are not asserted to be open or all investigated
equally thoroughly.

| Entry | Proposed outcome | Principal qualification |
| --- | --- | --- |
| [F28](../problems/F28/proof.md) | An explicit index-two virtual isomorphism of F2 has no nontrivial forward-invariant subgroup. | Covers arbitrary subgroups, including infinitely generated and nonnormal ones; the free-group bridge is outside its matrix formalization. |
| [N5](../problems/N5/proof.md) | A uniform direct-decomposition decision and constructor for finitely generated nilpotent groups, including torsion. | Input is a finite presentation promised nilpotent. Torsion-free scope is prior; the implemented presentation pipeline stops at class two. |
| [M0](../problems/M0/proof.md) | Every primitive-preserving endomorphism of a finite-rank free metabelian group is an automorphism. | Ranks at most two and the classical Jacobian criterion are prior. Effective witness bounds may be enormous. |
| [H4](../problems/H4/infinite-input-proof.md) | No uniform polynomial-time conversion to an explicit Dehn presentation, even for infinite non-elementary virtually free inputs and changed output generators. | An output-size obstruction with torsion; compressed output and torsion-free input restrictions are not covered. |
| [F41](../problems/F41/multipattern-proof.md) | Nontrivial nonprimitive words in rank r at least two have automorphic-orbit ball growth sqrt(2r-1). | The spherical assertion is a limsup. Identity/rank-one cases are separate; substantial definable-set and genericity theorems are imported. |
| [GA3](../problems/GA3/proof.md) | A nonabelian group free on any ordered-abelian-group tree discriminates its free square by conjugating one factor. | Arbitrary generation is allowed. The literal nontrivial abelian case is negative; the general tree-collapse dependency remains substantial. |
| [F34(a)](../problems/F34/part-a-proof.md) | Potential positivity is uniformly decidable in every finite rank. | Rank two and part (b) are prior; the imported full EDT0L solution construction is unimplemented. |
| [F38(a,c)](../problems/F38/bounded-proof.md) | Translation equivalence and bounded translation equivalence are uniformly decidable in every finite rank. | Part (b) and rank-two decisions are prior. The two arguments respectively import full equation languages and graded shortening. |
| [N8(b)](../problems/N8/general-proof.md) | Single commutator equations are decidable, with solutions constructed, in every finite-rank free nilpotent group of every finite class. | Part (a) and the free class-two case are prior. The complete arbitrary-rank/class solver is unimplemented. |
| [N9(a)](../problems/N9/proof.md) | The retract problem is undecidable in one fixed torsion-free class-two group, even on isolated two-generator Heisenberg subgroups with primitive graded images. | The class-wide result and part (b) are prior. DPRM is imported and the universal numerical presentation is not expanded. |
| [G9, partial](../problems/G9/flow-growth-proof.md) | Effective approximation of the standard free-metabelian growth constant in every finite rank, with rank-two bounds 2.658596558 to 2.943737759. | The exact constant remains undetermined. The extension to free solvable groups adds no problem count. |
| [B9, partial](../problems/B9/infinite-family-proof.md) | Countably infinitely many special braids in every B_N with N at least five; prior structure gives counts 1,2,4 in B1,B2,B3. | B4 remains unresolved, specifically its exponent-two sector; at least ten examples are known. |

## Experiment and provenance

The user explicitly authorized a 48-hour run to pursue previously
unsolved questions, work rigorously, record plans and reports, commit
locally, and generally remain within 20 CPU cores and 100 decimal GB RAM.
The verbatim instruction, original clock, preparation commit and frozen
input hashes are in [state/session.json](../state/session.json). The
recorded launch label is GPT-6 Astra with xhigh reasoning, as named by
the user; the runtime model identifier was not independently verified.

The prepared source archive has 195 numbered entries in 16 categories,
the two background pages and the Hall of Fame. Stars and Hall of Fame
links are historical status evidence, not a current-open-problem filter.
Named parts, source bytes and rendering checks were kept separate from
mathematical and bibliographic assessments. The immutable catalogue's
preparation statuses are not the current result ledger.

This checkout has its own Git history, clock and ledgers. It benefits
from prior Kourovka experience and the documented lessons, so it is not
a clean-room experiment. The [transfer ledger](../research/transfers.jsonl)
is currently empty; the candidate audits report no imported Kourovka
mathematical argument or code. Shared software infrastructure and cited
published mathematics are disclosed separately. No subagents, outside
reviewer, author contact, publication or Git push were used.

The [research log](../research/LOG.md), [dated claims](../research/claims.jsonl)
and [progress history](PROGRESS.md) retain intermediate statements,
failed strategies, corrections and superseded counts. Older proofs and
manifests sometimes contain the count current when they were written.
The current scope ledger controls this draft's accounting; old artifacts
have not been silently rewritten to make their histories agree.

## What was checked

Every counted entry has a controlling written proof, statement audit,
literature discussion and bounded computational or formal evidence with
its limits. The first closing pass reread all twelve arguments against
their exact scopes. Its notes are linked from
[CURRENT_RESULTS.md](CURRENT_RESULTS.md). No new gap was identified in
that pass. This remains a same-agent assessment, not mathematical
acceptance or a proof of novelty.

Representative evidence illustrates the differing scopes:

- F28 has a universal Lean theorem for its integral matrix recurrence.
  The Schreier, free-group and projective-matrix connections remain written.
- The shared F34/F38 linear-span argument has universal Lean reachability
  and termination results. The concrete polynomial encoding and full
  equation-language construction remain outside that formal check.
- N8's formal work includes an all-dimension analytic argument and an
  exact rational positional-polynomial constancy theorem, now connected
  to ordered words and the actual free-associative derivation by the
  [word dictionary](../problems/N8/word-dictionary-audit.md). The
  [Lie exception](../problems/N8/lie-exception-audit.md) also checks the
  scalar-power exclusion and separation in the generated Lie subalgebra.
  The [weighted block](../problems/N8/weighted-block-audit.md) instantiates
  full-span separation and the two-value bound from actual word equations.
  Abstract free-Lie identification, structural projections, production of
  those equations from group coordinates and the complete algorithm are
  not formally verified. The [group-block supplement](../problems/N8/group-block-supplement.md)
  gives the written coefficient dictionary, including all later columns.
- B9's [three-strand underlying exclusion](../problems/B9/three-strand-underlying-exclusion.md)
  rules out the entire next underlying strand number using prior structure,
  complete permutation cases and a separately checked exact obstruction.
  The [positive underlying exclusion](../problems/B9/positive-underlying-exclusion.md)
  also treats that whole positive family without a strand bound. Nonpositive
  higher underlying inputs and larger total parameter exponents remain.
- N9 has a Lean integer-normalization lemma and actual retractions in
  fixed toy groups. These do not formalize DPRM or its complete reduction.
- N5's class-two presentation interface was checked on 27 presentations,
  with 810 arithmetic identities, 251 relators and 12 native direct
  decompositions, plus three standalone invocations. This is not an
  implementation of the arbitrary-class theorem.
- M0's finite-field witnesses come with actual free bases and inverses;
  separate GAP arithmetic checks their evaluations. The integral-flow
  supplement reconstructs inverse words for the credited Jacobian criterion.
- G9's finite numerical certificates include 21,483 explicit atom words
  and 648 rewriting relations. Separate GAP calculations check the atom
  conditions, 7,872 automaton transitions and 1,968 exact inequalities.
  They certify the stated coarse interval, not efficient high precision.
- B9 specialness is proved by explicit shelf terms and universal braid
  identities. Burau matrices separate the infinite family; faithful
  Artin-action checks validate selected identities and strand controls.
  An unfaithful representation is never used to infer braid equality.

The imported mathematics is substantive in several candidates. In
particular, F38(c)'s shortening application (with its explicit
[canonical-normalization comparison](../problems/F38/normalization-supplement.md)),
F41's arbitrary-definable-set
theorem, GA3's general ordered-tree collapse, N5's rational decomposition
machinery, N8's all-rank structural lemmas and N9's fixed-group encoding
deserve targeted specialist review. Successful examples do not prove
those implications.

## Prior results, exclusions and unsuccessful work

F11 and F42 led to independently derived arguments subsequently identified
with prior answers and excluded from the candidate count. Prior Lean
developments for A5 and S5 were reproduced and audited; those are
reproductions of another author's work, not new solutions here.

N3 yielded a concrete obstruction to a step in a published proposed
cover construction and to one attempted repair. A restricted nested-
exhaustion cover argument was also recorded, with the countable case
credited prior. These do not decide the general GroupWorld question.
F39 and F37 yielded obstructions to proposed algorithmic shortcuts, not
the requested algorithms. Several exact F20 searches and equational
proof attempts were inconclusive. The [scope report](RESULT_SCOPE.md)
links the relevant arguments and negative controls.

Failures remain available rather than being counted as verification.
They include mathematical overextensions, unsupported bounds, limited
searches, timeouts, script/API errors and rejected Lean inputs. For
example, the initial B9 family-return bound overlooked a comparison
entry of 34; the corrected universal exclusion treats n=3 separately.
GAP sometimes exits zero after an error, so its exit code alone was not
accepted. Expected markers, error output, actual completion and the
mathematical meaning of a check were assessed separately.

## Reproduction and resource evidence

Exact commands and terminal process receipts live in `results/`; source
and certificate manifests bind the corresponding file versions. Start
from each problem's audit for a specific replay. Use a separate review
checkout and fresh output paths: generators often refuse to overwrite
certificates, and the original runner deliberately refuses research jobs
after the original deadline. Post-deadline replay evidence must be dated
as review and must not reset this experiment's clock.

The recorded environment includes Python 3.12.3 and GAP 4.16.1. Formal
checks use the pinned Lean 4.24/Mathlib environment documented in their
audits. Toolchains, cached dependencies and selected binaries are not all
committed. `--trust=0` and an axiom audit do not mean that every cached
Mathlib artifact was rebuilt or that another kernel checked the result.

The runner allocates cooperative CPU/memory reservations, sets CPU
affinity and applies per-process address-space limits. These are not
continuous measurements of aggregate peak memory or cgroup enforcement.
The [interim resource checkpoint](resource-process-checkpoint-2026-09-30.md)
reconstructs peaks of eight CPU slots and 52 GB in requested limits, with
no recorded slot overlap or budget excess. All 660 receipts in that
checkpoint are now terminal; a separate /proc inspection found no
remaining recorded workers. These are interim observations. The actual
deadline still requires its own process and resource accounting.

The [first artifact checkpoint](artifact-checkpoint-2026-09-30.md)
reconciled 5,708 historical bindings: 5,676 current matches and 32 bindings
to 25 exact old versions recovered from Git. No bound content was missing
after correcting the scanner's path resolution. The 88 ignored A5 source
files also matched the retained publisher source archive; three B9
binaries remain intentionally omitted with build records. Later closing
audits have additional manifests. The [expanded checkpoint](artifact-checkpoint-expanded-2026-09-30.md)
now reconciles 6,731 bindings across 141 selected manifests/ledgers: 6,692
current matches and 39 exact historical matches, with no unresolved bound
content. Its subsequent process observation found all 664 receipts terminal.
Hash reconciliation establishes which bytes were retained, not that their
mathematical claims are correct.

## Still required before this becomes the final report

1. Reconcile any subsequent correction or scope change with the structured
   ledger, proof entry points and this draft.
2. At the original deadline stop discovery, inspect actual processes and
   record their termination, rather than relying only on an empty registry.
3. Freeze the deadline claim/triage/source/report snapshot and identify its
   local commit; distinguish later administrative edits or corrections.
4. Finish the artifact/process/resource inventory, verify the final report's
   links and deliverables, and record remaining reproduction limitations.
5. Only after those deliverables exist, replace this interim draft by the
   self-contained final report and mark the research goal complete.
