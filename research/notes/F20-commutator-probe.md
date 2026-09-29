# F20: explicit commutator identities, still inconclusive

29 September 2026, approximately 19:17--19:21 UTC. Follow-up to
`F20-equational-probe.md`; no candidate count changes.

## Changed representation

The earlier product/inverse encodings were replaced by an encoding with
two additional functions:

    cc(x,y)=x^-1 y^-1 x y,       cj(x,y)=y^-1 x y.

The input includes their definitions and 19 further universal group
identities: commutator and conjugation rules for products, inverses and
the identity, a collection rule, and the Hall--Witt identity. All hold
in arbitrary groups. The presentation still kills only the rank-two
Hall commutators of exactly weight five or exactly weight six. No higher
weight, centrality, nilpotency, or unproved earlier consequence is added.

The generator is `scripts/generate_f20_commutator_encoding.py`, importing
the already saved Hall-list construction from `generate_f20_equational.py`.
It makes 29 files: nine weight-six goals for the weight-five presentation,
18 weight-seven goals for the weight-six presentation, and two lower-weight
negative controls. It refuses to overwrite an existing output directory.

## Independent semantic audit

`scripts/check_f20_commutator_inputs.g` adapts the preceding independent
GAP parser and reconstructs its own Hall words with native free-group
operations. It parses the actual new files, interpreting cc as GAP's
commutator and cj as conjugation. The universal identities are checked
by exact reduction in a free group on distinct variable generators;
this proves them as identities, not merely on a finite sample.

The checker also verifies every presentation equation and target against
the intended Hall word, checks the complete list of clause names and
roles, and constructs the class-four and class-five nilpotent negative
models. All 29 files and 1,389 clauses passed. Both the generation run
and this audit have empty stderr. This checks input semantics, not the
subsequent E proof inferences.

## Bounded searches

The unchanged recorded batch driver invoked the pinned E binary with
`--auto-schedule --silent --proof-object=3 --cpu-limit=60` and a 2,048MB
internal memory limit. Each worker reserved one CPU and 3GB through the
recorded runner, with an 80s external timeout. There were at most four
workers (4CPU/12GB total). The schedule selected one strategy per input
at this budget; it was not a multi-strategy portfolio.

| Batch suffix | Goal | Outcome |
| --- | --- | --- |
| 01 | weight-five presentation, goal 1: known control | No proof in 60s; exit 9, GaveUp |
| 02 | weight-six presentation, goal 1: already obtained earlier | Proof found in 17.33s; exit 0 |
| 03--10 | weight-six goals 3,4,5,6,7,8,11,12 | No proof in 60s each; exit 9, GaveUp |

The positive goal in row 02 was already proved by the earlier encoding
and reduced by the earlier rewriting probe. It is not new progress on
the missing goals. The failed known control in row 01 is particularly
useful: the new encoding is not uniformly better and search failure
cannot establish nontriviality. All eight missing goals remain missing.

Raw process records and logs are `results/f20-e-comm-v1-*`. The batch
summary, generated files, one extracted TSTP proof, frozen sources and
hash manifest are in `research/certificates/F20-commutator/`. The E
checkout, binary pin and reproducible build instructions are those of
the preceding equational probe. E's proof inferences have not been
independently replayed.

There were 12 terminal jobs: input generation, GAP input audit and ten
E searches. Three processes met their expected success marker; nine
proof searches did not. No external timeout, crash, or hidden successful
target occurred. Do not expand this same search just for volume.

F20 remains unresolved. No whole-entry candidate, partial candidate,
established novel result or independent specialist review is added.
