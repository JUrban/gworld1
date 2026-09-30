# Interim result scope ledger

Assessment: **2026-09-30T03:17:33.067847+00:00**. Research remains active until
**2026-09-30T10:04:49.670358+00:00**. This is not the frozen deadline result.

**10 whole-entry coverage candidates, 2 partial-entry candidates, 0 established novel results.**
Whole-entry coverage combines the proposed arguments with explicitly credited
prior answers. All candidate proofs and novelty assessments await independent
specialist review. Separate implementations and formal fragments have the
limited scopes described in the individual audits.

## Entry and named-part accounting

| Bookkeeping unit | Count |
| --- | ---: |
| Unpartitioned whole-entry candidates | 6 |
| Whole-entry candidates having named parts | 4 |
| Complete proposed answers to named parts | 5 |
| Credited prior named parts within those entries | 4 |
| Other partial-entry candidates | 2 |
| Other catalogue entries, not counted here | 183 |

The 6 unpartitioned answers and 5 proposed named-part answers make
11 proposed components across 10 whole-entry candidates. Neither count
is a count of established new theorems. Rank-restricted prior results inside
a component are credited below and are not additional named parts.

The other 183 catalogue entries are **not** asserted to be open. They include
prior answers, partial results, failed approaches and unverified status.

| Entry | Component basis | Current proposed result |
| --- | --- | --- |
| [F28](../problems/F28/README.md) | entry: candidate | Explicit index-two subgroup isomorphism in F2 with no nontrivial forward-invariant subgroup, even without finite generation or normality. |
| [N5](../problems/N5/README.md) | entry: candidate | Uniform direct-decomposition decision and factor construction for finite presentations promised to define finitely generated nilpotent groups, including torsion. |
| [M0](../problems/M0/README.md) | entry: candidate | A primitive-preserving endomorphism of a free metabelian group of any finite rank is an automorphism. |
| [H4](../problems/H4/README.md) | entry: candidate | No uniform polynomial-time conversion from arbitrary finite hyperbolic-group presentations to explicit finite Dehn presentations, even with new generators and infinite non-elementary virtually free inputs. |
| [F41](../problems/F41/README.md) | entry: candidate | Every nontrivial nonprimitive word in rank r at least two has automorphic-orbit ball growth rate sqrt(2r-1), and the same spherical limsup. |
| [GA3](../problems/GA3/README.md) | entry: candidate | Free-square discrimination for every nonabelian group acting freely without inversions on an arbitrary ordered-abelian-group tree; arbitrary generation is allowed. |
| [F34](../problems/F34/README.md) | a: candidate; b: prior | Uniform decision of potential positivity in all finite ranks, together with the credited prior negative answer to the stability question in (b). |
| [F38](../problems/F38/README.md) | a: candidate; b: prior; c: candidate | Uniform decisions of translation equivalence (a) and bounded translation equivalence (c) in every finite rank; (b) is credited prior. |
| [N8](../problems/N8/README.md) | a: prior; b: candidate | Single commutator equations are decidable, with solution construction, in every finite-rank free nilpotent group of every finite class; general class-two undecidability in (a) is prior. |
| [N9](../problems/N9/README.md) | a: candidate; b: prior | Undecidable retract problem in one fixed finitely generated torsion-free class-two group, on two-generator isolated Heisenberg subgroups with primitive images in both graded layers. |
| [G9](../problems/G9/README.md) | entry: partial candidate | Computable standard growth constant with an explicit approximation modulus for every finite-rank free metabelian group; certified rank-two interval 2.658596558 to 2.943737759. Extension to free solvable groups. |
| [B9](../problems/B9/README.md) | entry: partial candidate | Countably infinitely many special braids in each B_N for N at least five; deductions from prior structure give counts 1, 2 and 4 for N=1,2,3. |

## Prior coverage, limits and controlling files

### F28

Nearby virtual-endomorphism and invariant-subgroup results are credited in the audit; novelty is unverified.

Lean verifies the matrix argument, not the full free-group theorem.

Proofs: [proof.md](../problems/F28/proof.md).

Audits: [audit.md](../problems/F28/audit.md), [matrix-lean-audit.md](../problems/F28/matrix-lean-audit.md).

### N5

Torsion-free decision and rational decomposition machinery are prior. Potentially new scope is the general torsion case.

The promise is essential. The finite-presentation pipeline is implemented only through class two; higher-class integration remains unimplemented.

Proofs: [proof.md](../problems/N5/proof.md).

Audits: [audit.md](../problems/N5/audit.md), [integrality-audit.md](../problems/N5/integrality-audit.md), [class2-input-audit.md](../problems/N5/class2-input-audit.md), [N5-closing-proof-reread.md](../research/audits/N5-closing-proof-reread.md).

### M0

Ranks at most two are prior; Bachmuth's inverse-function criterion and the Fox/Magnus machinery are credited.

The effective finite-field witness bound is not a practical complexity bound. The integral-flow supplement reproves a credited classical ingredient.

Proofs: [proof.md](../problems/M0/proof.md), [kronecker-construction.md](../problems/M0/kronecker-construction.md).

Audits: [audit.md](../problems/M0/audit.md), [flow-inverse-audit.md](../problems/M0/flow-inverse-audit.md).

### H4

Classical Dehn-language bounds and related earlier output-size obstructions are credited.

Ordinary explicit word output and torsion-allowing input are essential; no compressed-output or torsion-free lower bound is claimed.

Proofs: [proof.md](../problems/H4/proof.md), [infinite-input-proof.md](../problems/H4/infinite-input-proof.md).

Audits: [audit.md](../problems/H4/audit.md), [infinite-input-audit.md](../problems/H4/infinite-input-audit.md).

### F41

Prior special cases and the full Kharlampovich-Myasnikov multipattern theorem and Pillay genericity theorem are credited.

Identity and rank one require separate conventions. No spherical limit or stronger word-dependent cyclic-orbit rate is asserted. Constants depend on the fixed word.

Proofs: [multipattern-proof.md](../problems/F41/multipattern-proof.md).

Audits: [multipattern-audit.md](../problems/F41/multipattern-audit.md), [dependency-boundary-audit.md](../problems/F41/dependency-boundary-audit.md), [F41-closing-proof-reread.md](../research/audits/F41-closing-proof-reread.md).

### GA3

The literal nontrivial abelian case is negative and is not counted separately. Related discrimination results and the imported general tree-collapse theorem are credited.

The positive theorem requires nonabelianness. Free-group computations do not validate the general collapse; the elementary separator remains a written argument.

Proofs: [proof.md](../problems/GA3/proof.md), [elementary-separator-supplement.md](../problems/GA3/elementary-separator-supplement.md).

Audits: [audit.md](../problems/GA3/audit.md), [GA3-closing-proof-reread.md](../research/audits/GA3-closing-proof-reread.md).

### F34

Rank-two decision in (a) and the answer to (b) are prior; potentially new scope is higher-rank (a).

Full EDT0L solution-relation construction is imported and unimplemented. Shared linear-span formalization does not formalize the entire algorithm. Identity convention is explicit.

Proofs: [part-a-proof.md](../problems/F34/part-a-proof.md).

Audits: [part-a-audit.md](../problems/F34/part-a-audit.md), [F34-coverage-reconciliation.md](../research/notes/F34-coverage-reconciliation.md), [F34-F38-closing-proof-reread.md](../research/audits/F34-F38-closing-proof-reread.md).

### F38

Part (b) and the rank-two decisions are prior. The proposed new scope is higher-rank (a) and (c).

Part (a) imports an unimplemented full EDT0L construction. Part (c)'s sufficiency imports graded shortening. The quantifier is over ambient automorphisms, with separate identity cases.

Proofs: [part-a-proof.md](../problems/F38/part-a-proof.md), [bounded-proof.md](../problems/F38/bounded-proof.md).

Audits: [part-a-audit.md](../problems/F38/part-a-audit.md), [bounded-audit.md](../problems/F38/bounded-audit.md), [F34-F38-closing-proof-reread.md](../research/audits/F34-F38-closing-proof-reread.md).

### N8

Part (a) and the free class-two instance of (b) are prior. The current candidate has no class cutoff.

The complete all-rank/class solver is unimplemented. Universal Lean ingredients now include the ordered-word/free-associative dictionary and scalar-power exclusion in the generated Lie subalgebra. Abstract free-Lie identification, homogeneous projections, group application and the full algorithm remain written.

Proofs: [general-proof.md](../problems/N8/general-proof.md).

Audits: [general-audit.md](../problems/N8/general-audit.md), [positional-polynomial-audit.md](../problems/N8/positional-polynomial-audit.md), [N8-closing-proof-reread.md](../research/audits/N8-closing-proof-reread.md), [word-dictionary-audit.md](../problems/N8/word-dictionary-audit.md), [lie-exception-audit.md](../problems/N8/lie-exception-audit.md).

### N9

The uniform class-wide version of (a) and the affirmative free-nilpotent answer to (b) are prior. Potentially new scope is the one fixed ambient group.

DPRM is imported; the universal numerical circuit and presentation are not expanded. Toy groups and Lean normalization are limited checks, not a full reduction verification.

Proofs: [proof.md](../problems/N9/proof.md), [isolated-inputs-and-prior-scope.md](../problems/N9/isolated-inputs-and-prior-scope.md).

Audits: [audit.md](../problems/N9/audit.md), [N9-closing-proof-reread.md](../research/audits/N9-closing-proof-reread.md).

### G9

Flow models, bridge/unfolding arguments and earlier estimates are credited. The solvable extension is not another problem count.

The exact growth constant remains undetermined. Fine-precision computation is not demonstrated.

Proofs: [flow-growth-proof.md](../problems/G9/flow-growth-proof.md), [solvable-extension-proof.md](../problems/G9/solvable-extension-proof.md).

Audits: [flow-growth-audit.md](../problems/G9/flow-growth-audit.md), [solvable-extension-audit.md](../problems/G9/solvable-extension-audit.md).

### B9

Dehornoy's structure and right-power theorem are credited. Small-strand deductions and the known ten B4 braids are not separately counted.

B4 remains unresolved, specifically its exponent-two sector. At least ten special B4 braids are known; excluded families and parameter restrictions are not exhaustion.

Proofs: [infinite-family-proof.md](../problems/B9/infinite-family-proof.md), [small-strand-proof.md](../problems/B9/small-strand-proof.md).

Audits: [infinite-family-audit.md](../problems/B9/infinite-family-audit.md), [small-strand-audit.md](../problems/B9/small-strand-audit.md), [exponent-two-parameter-reduction.md](../problems/B9/exponent-two-parameter-reduction.md).

## Selected uncounted work

This selection explains significant exclusions; it is not a complete list
of prior answers or unsuccessful work.

| Entry | Why it is not counted | Evidence |
| --- | --- | --- |
| F11 | The derived negative example is covered by prior work; no new candidate. | [F11-index3-lead.md](../research/notes/F11-index3-lead.md) |
| F42 | The derived growth formula matches a September 2026 prior answer; no new candidate. | [F42-first-argument.md](../research/notes/F42-first-argument.md) |
| A5 | The prior author's Lean development was reproduced and audited, not newly solved here. | [A5-prior-Lean-proof-audit.md](../research/notes/A5-prior-Lean-proof-audit.md) |
| S5 | The prior author's Lean development was reproduced and audited, not newly solved here. | [S5-prior-Lean-proof-audit.md](../research/notes/S5-prior-Lean-proof-audit.md) |
| N3 | A published construction and one repair fail; a nested-exhaustion cover is proved, with the countable case prior. This neither answers the general question negatively nor establishes its full positive answer. | [N3-published-cover-audit.md](../research/notes/N3-published-cover-audit.md), [N3-profile-repair-obstruction.md](../research/notes/N3-profile-repair-obstruction.md), [N3-nested-cover.md](../research/notes/N3-nested-cover.md) |
| F39 | Primitive-free unimodular embeddings defeat an injection/nilpotent-quotient shortcut. The requested general decision remains unresolved here. | [F39-unimodular-obstruction.md](../research/notes/F39-unimodular-obstruction.md) |
| F37 | Finite quotients cannot supply all the needed primitive-length lower bounds. This does not decide primitive length in general. | [F37-finite-quotient-obstruction.md](../research/notes/F37-finite-quotient-obstruction.md) |
| F20 | Finite-quotient, homology, rewriting and equational probes did not yield a proof or counterexample. | [F20-finite-images.md](../research/notes/F20-finite-images.md), [F20-finite-cover-homology.md](../research/notes/F20-finite-cover-homology.md), [F20-equational-probe.md](../research/notes/F20-equational-probe.md) |

## Reproduction and complete inventory

The [JSON ledger](result-scope-ledger.json) records all catalogue IDs, their
current triage rows, original source locations and hashes, and the precise
candidate components. Its artifact bindings identify this assessment's files.

Regenerate after an explicit scope update with:

```sh
python3 scripts/run_recorded.py --name scope-ledger-NEW --cores 1 --memory-gb 2 \
  --timeout 60 --expect 'PASS result scope ledger' -- python3 scripts/build_scope_ledger.py
```

The script validates ID/part/count consistency, frozen launch-input hashes,
and linked-file availability. It does not establish the correctness of a
proof, a literature assessment, or a novelty claim. Historical claims remain
in the append-only ledger and dated notes. The final report must distinguish
the actual deadline snapshot from any later corrections.
