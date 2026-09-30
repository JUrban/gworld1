# GroupWorld 48-hour experiment — final report

The research window was **28 September 2026, 10:04:49.670358 UTC through
30 September 2026, 10:04:49.670358 UTC**. Discovery has ended. The last
pre-deadline research commit is `401213c09222ebebaf99589553258cf74a918187`,
committed at 09:47:18 UTC on 30 September. The unchanged committed record
was observed and frozen at **10:05:47.903924 UTC**, after the cutoff; this
is the observation time, not an extension of the research window.

The [deadline snapshot](../research/audits/deadline-snapshot-manifest-v1.json)
retains the pre-deadline ledger and exact file bindings. Final rendering,
this report and the closing integrity inventories are **post-deadline
administration**, recorded [separately](../research/audits/postdeadline-administration-v1.json).
They add no mathematical results or solver runs. All 195 entries, counts
and 96 input/artifact bindings in the final scope ledger agree exactly
with the frozen assessment. The original [closing draft](FINAL_REPORT_DRAFT.md)
is retained unchanged as a historical document.

## Deadline outcome

The deadline record contains **ten whole-entry coverage candidates and
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
| [N5](../problems/N5/proof.md) | A uniform direct-decomposition decision and constructor for finitely generated nilpotent groups, including torsion. | Input is a finite presentation promised nilpotent. Torsion-free scope is prior. The complete general presentation command is implemented and checked, with no supplied class bound and factor words returned. The nilpotency promise and written completeness argument remain essential. |
| [M0](../problems/M0/proof.md) | Every primitive-preserving endomorphism of a finite-rank free metabelian group is an automorphism. | Ranks at most two and the classical Jacobian criterion are prior. Effective witness bounds may be enormous. |
| [H4](../problems/H4/infinite-input-proof.md) | No uniform polynomial-time conversion to an explicit Dehn presentation, even for infinite non-elementary virtually free inputs and changed output generators. | An output-size obstruction with torsion; compressed output and torsion-free input restrictions are not covered. |
| [F41](../problems/F41/multipattern-proof.md) | Nontrivial nonprimitive words in rank r at least two have automorphic-orbit ball growth sqrt(2r-1). | The spherical assertion is a limsup. Identity/rank-one cases are separate; substantial definable-set and genericity theorems are imported. |
| [GA3](../problems/GA3/proof.md) | A nonabelian group free on any ordered-abelian-group tree discriminates its free square by conjugating one factor. | Arbitrary generation is allowed. The literal nontrivial abelian case is negative; the general tree-collapse dependency remains substantial. |
| [F34(a)](../problems/F34/part-a-proof.md) | Potential positivity is uniformly decidable in every finite rank. | Rank two and part (b) are prior; the imported full EDT0L solution construction is unimplemented. |
| [F38(a,c)](../problems/F38/bounded-proof.md) | Translation equivalence and bounded translation equivalence are uniformly decidable in every finite rank. | Part (b) and rank-two decisions are prior. The two arguments respectively import full equation languages and graded shortening. |
| [N8(b)](../problems/N8/general-proof.md) | Single commutator equations are decidable, with solutions constructed, in every finite-rank free nilpotent group of every finite class. | Part (a) and the free class-two case are prior. The complete arbitrary-rank/class [word-input solver](../problems/N8/general-word-audit.md) is implemented; finite controls do not establish its structural proof. |
| [N9(a)](../problems/N9/proof.md) | The retract problem is undecidable in one fixed torsion-free class-two group, even on isolated two-generator Heisenberg subgroups with primitive graded images. | The class-wide result and part (b) are prior. DPRM is imported and the universal numerical presentation is not expanded. |
| [G9, partial](../problems/G9/flow-growth-proof.md) | Effective approximation of the standard free-metabelian growth constant in every finite rank, with rank-two bounds 2.676891785 to 2.943737759. | The exact constant remains undetermined. The extension to free solvable groups adds no problem count. |
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
The frozen scope ledger controls this report's accounting; old artifacts
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

- B9's [fixed-color procedure](../problems/B9/fixed-color-decision.md)
  reduces all partners of any supplied first braid to a finite candidate
  list, using exact strand deletion and prior specialness algorithms.
  Separate GAP replay covers all 52 retained first colors, with 40 empty
  fibres and 16 partners among the other 12. The
  [universal family obstruction](../problems/B9/infinite-family-partner-exclusion.md)
  also excludes every braid partner of I1(beta_n), n>=3. Global B4
  exhaustion remains open.

- G9's [completed and shortened families](../problems/G9/steiner-shortening-supplement.md)
  and [disjoint shear tails](../problems/G9/shear-tail-supplement.md) give
  the lower bound 2.676891785, retaining the independent earlier upper bound.
  The 3,239 old two-boundary families and height-one family are augmented by
  2,906 tails in 1,453 shear orbits. Separate GAP code checks seed flows,
  orbit coverage, costs and rational inequalities. Infinite disjointness
  and free concatenation remain written proof obligations.
- F28 has a universal Lean theorem for its integral matrix recurrence.
  The Schreier, free-group and projective-matrix connections remain written.
- The shared F34/F38 linear-span argument has universal Lean reachability
  and termination results. The concrete polynomial encoding and full
  equation-language construction remain outside that formal check.
  The [implemented language interfaces](../problems/F38/language-interface-audit.md)
  now connect group equations to constrained monoid equations and supplied
  tuple grammars to the polynomial checker. GAP separately checks 1,433
  equation tuples and the grammar certificates. Generating a complete
  grammar from arbitrary equations remains unimplemented.
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
  The [four-strand reduction](../problems/B9/four-strand-underlying-reduction.md)
  excludes all ten known second inputs for arbitrary first input, apart
  from three already classified pairs; one unknown permutation case survives.
  A [higher-strand obstruction note](../research/notes/B9-general-permutation-obstruction.md)
  retains a failed permutation-only extension, with explicit special lifts
  whose parameters have three-position permutations but need seven strands.
  The [fixed-first-color reduction](../problems/B9/fixed-first-color-reduction.md)
  excludes all four known first-color families for arbitrary special second
  colors, without restricting the total parameter exponent. The remaining
  first colors are not exhausted.
- N9 has a Lean integer-normalization lemma and actual retractions in
  fixed toy groups. These do not formalize DPRM or its complete reduction.
- N5's [higher-class native input](../problems/N5/general-malcev-input-audit.md)
  was checked on nine groups,108 native words and222 bracket entries. Its
  [rational-support kernels](../problems/N5/general-support-audit.md) pass twelve
  groups and forty partitions, retaining an index-two integral gluing obstruction.
  The [complete native pipeline](../problems/N5/general-pipeline-audit.md) checks
  34 central branches and15 actual products. The [general presentation command](../problems/N5/general-fp-audit.md)
  passes fifteen conversion controls and five standalone commands, returning
  nineteen original-generator factor words. A serialization failure is retained.
- N5's class-two presentation interface was checked on 27 presentations,
  with 810 arithmetic identities, 251 relators and 12 native direct
  decompositions, plus three standalone invocations. That earlier interface
  covered class two only; the later general command above covers the full
  promised-nilpotent input class.
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

N8's [complete projective leading-pair implementation](../problems/N8/projective-leading-pairs-audit.md)
also checks a noncentral example where primitive normalization alone
loses all successful branches. All signed scales are retained, with
separate GAP checks of the eight lift decisions. The subsequent
[complete recursion](../problems/N8/general-implementation-audit.md) connects
all integral period residues, exceptional quadratics and linear tails.
The [word-input command](../problems/N8/general-word-audit.md) also covers
elementary rank/class boundaries. Native GAP reconstructs its finite group
certificates; the general structural proof remains a review obligation. The
[higher-leading positive controls](../problems/N8/higher-leading-group-audit.md)
and [complete negative control](../problems/N8/higher-negative-audit.md)
exercise leading weights above one. In the latter, native GAP verifies both
complete integer kernels, 64 group columns and two rootless quadratics;
it does not independently recompute the projective leading lists.

## Prior results, exclusions and unsuccessful work

F11 and F42 led to independently derived arguments subsequently identified
with prior answers and excluded from the candidate count. Prior Lean
developments for A5 and S5 were reproduced and audited; those are
reproductions of another author's work, not new solutions here.
F31's prior Lei--Zhang counterexample also received a
[construction audit](../research/notes/F31-prior-construction-audit.md),
including the graph-embedding rank argument and separate Python/GAP
checks. It remains excluded from this experiment's candidates.

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
example, the initial B9 family-return comparison overlooked an entry
of 34; its historical correction treats n=3 separately. The later
first-column argument gives a different, uniform exclusion for all n>=3.
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
The [final reservation inventory](../research/audits/resource-process-v6.json)
and [deadline process observation](../research/audits/deadline-process-closure-v1.json)
account for all recorded research-window jobs. The later
[closure observation](../research/audits/final-process-closure-v1.json)
checks terminal receipts, the registry and actual attributable processes.
The resource auditor retains its generic “interim” scope label; its actual
post-deadline timestamp and the separate closure records govern this use.
Its generic running-self-receipt limitation does not apply to this direct
administrative invocation, which created no research receipt.

All **786 receipts are terminal**: 589 recorded process successes and
197 nonsuccesses, including 46 timeout flags and 24 interruption flags.
Nonsuccesses include an intentional pre-deadline rejection by the final
reporting guard. These figures are process conditions, not proof counts.
Every recorded interval lies within the original research window. Peak
reservations were eight CPU slots, 52 decimal GB in requested per-process
limits and seven simultaneous jobs, with no recorded CPU overlap or budget
excess. Unrecorded commands, external tools and model inference are outside
this accounting. Both closure observations found an empty job registry
and no attributable worker beyond their own observer processes.

The [final artifact inventory](../research/audits/artifact-integrity-v9.json)
reconciles current and exact historical bytes without rewriting old
manifests. Hash reconciliation establishes retained content, not the
mathematical claims in that content.

The inventory reconciles **31,406 bindings across 212 selected records**:
31,192 current matches and 214 historical matches, with no unresolved
content, parse errors or process-integrity issues. All 173 distinct indexed
historical file versions retain their exact bytes. The four frozen launch
inputs match. The 91 intentionally untracked bound paths remain 88 A5
dependency sources and three B9 compiled binaries, with archive/build
records. The inventory predates the final handoff manifest and last report
edits; those files receive separate exact bindings and link checks.

The [reproduction guide](REPRODUCTION_GUIDE.md) gives pinned dependencies,
selected native replay commands, source-version recovery and omitted-data
limits. The [portability inventory](../research/audits/review-portability-v2.json)
covers Git objects reachable at its explicitly recorded pre-closeout HEAD;
new staged files are separately covered by the 90 MB pre-commit hook.
A final all-refs size check follows the closeout commit.

At the recorded HEAD, all 6,369 reachable Git blobs are below 90,000,000
bytes; the largest is 75,046,692 bytes. No remote is configured. The
current-link inventory (`research/audits/review-links-v2.json`) checks local
inline destinations in the counted proofs, audits and reviewer entry points;
it does not fetch URLs or validate Markdown fragments or dynamic code paths.

The omitted 127,724,170-byte formatted F34/F38 language JSON has the same
parsed data as the retained 19,478,346-byte compact file; its original bytes
are reproducible from the recorded formatting and hash.

## Specialist review priorities

The central outstanding task is independent review of correctness and
novelty. In particular:

- F34(a)/F38(a): the complete equation-language construction and its
  connection to the proposed decisions; the general grammar generator
  is not implemented.
- F38(c): the graded-shortening implication and normalization comparison.
- N8: completeness of all-rank leading-pair enumeration, exceptional
  parameter separation and the passage to the full group recursion.
- N5: rational-support uniqueness, integral gluing and central splitting
  in the promised-nilpotent presentation algorithm.
- GA3 and F41: the precise hypotheses and applications of the imported
  tree-collapse and arbitrary-definable-set theorems.
- N9: the passage from a fixed Diophantine encoding to one fixed ambient
  group; the universal numerical presentation is not expanded.

The remaining candidates also require full review. No candidate has
novelty clearance, and the G9 exact constant and B9 four-strand case remain
unresolved here. Any later corrections or research should preserve this
deadline assessment and receive a separate dated record.
