# Reproducing the GroupWorld evidence

This guide covers the retained experiment artifacts. Start with
[the result scopes](RESULT_SCOPE.md) and each problem's controlling proof
and audit in [CURRENT_RESULTS.md](CURRENT_RESULTS.md). Computation checks
particular claims; no command establishes all twelve candidate arguments
or their novelty. Original commands, limits, timestamps, exit status and
log hashes are in `results/JOB/process.json`.

## Keep the original experiment record intact

Use a separate clone or worktree for review. Preserve `state/session.json`
and its original 28--30 September clock. The original recorder refuses new
research after its deadline. Later replays are review evidence with their
own dates and logs, not additional work inside the 48-hour run.

For a replay, read the recorded argument vector and its audit before
running it. Choose fresh output paths wherever an argument creates files.
Some checkers have fixed fixture paths, and some older wrappers have fixed
scratch paths. Do not run all historical commands blindly: many are
deliberate negative controls, superseded sources or exploratory failures.
Dependencies must finish before their consumers start.

A source path may have changed since a historical run. Manifests retain
the expected hash. Exact indexed older versions are under
`research/audits/historical-artifacts/`, with `historical*recovery*.json`
mapping them to their original paths and commits. Several mathematical
certificates also retain their own `sources/` or `versions/` directories.
Use that version when reproducing the old run. The current source can
instead be reviewed as a separate, explicitly dated revision.

## Environment

The run used Python 3.12.3, GAP 4.16.1, SymPy 1.14.0, python-flint 0.9.0
and mpmath 1.3.0. The Python mathematics pins are retained in
[research-math-requirements.txt](../config/research-math-requirements.txt).
For example, in a fresh review checkout with `uv` already installed:

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r config/research-math-requirements.txt
```

These installation commands are instructions for a new machine, not a
claim that its installation has been tested here. Installed versions and
local executable hashes were captured in the
[portability inventory](../research/audits/review-portability-v1.json).
That record identifies this environment; it does not bundle the binaries.

Install a compatible GAP distribution and packages. The preparation
[environment record](../provenance/environment.json) gives the versions
loaded here: `nq` 2.5.11, `polycyclic` 2.18, `fga` 1.5.0, `smallgrp` 1.7.0,
`kbmag` 1.6.0 and `ace` 5.7.0. Set `GWORLD_GAP_ROOT` to its installation
directory, containing the `gap` launcher, or copy
[the local configuration example](../config/local-tools.example.json) to
the ignored `config/local-tools.json`. The repository's `bin/gap` then
uses that installation. Putting the repository's `bin` first on `PATH`
also resolves recorded commands that invoke plain `gap`.

```sh
export GWORLD_GAP_ROOT=/absolute/path/to/gap-4.16.1
export PATH="$PWD/bin:$PATH"
```

The runner's memory reservation is a requested per-process address-space
limit, not a measured aggregate RAM bound. For manual review runs apply
your own CPU, memory and wall-clock limits, including child processes.
Large rank/class inputs can be prohibitively expensive.

## Small, distinct replay entry points

The following GAP checkers read retained fixtures from the repository
root and do not regenerate the expensive searches. Run only those relevant
to the claim being reviewed, capturing stdout and stderr in fresh logs.
Use `bin/gap --quitonbreak scripts/NAME.g` with the filenames below.

| Claim checked | Checker under `scripts/` | Successful original receipt |
| --- | --- | --- |
| N8 higher-weight complete negative fixture: group blocks and integer lattices | `check_n8_higher_negative_gap.g` | [N8-higher-negative-gap-v1](../results/N8-higher-negative-gap-v1/process.json) |
| G9 shortened atom flows and rational lower bound | `check_g9_steiner_completion.g` | [G9-steiner-completion-gap-v1](../results/G9-steiner-completion-gap-v1/process.json) |
| B9 fixed-first-color decisions on the retained 52 inputs | `check_b9_fixed_color.g` | [B9-fixed-color-decisions-gap-v2](../results/B9-fixed-color-decisions-gap-v2/process.json) |
| B9 universal polynomial obstruction for the infinite family | `check_b9_family_first_column.g` | [B9-family-first-column-gap-v2](../results/B9-family-first-column-gap-v2/process.json) |
| F34/F38 equation reductions and supplied grammar certificates | `check_f34_f38_language_gap.g` | [F34-F38-language-gap-v3](../results/F34-F38-language-gap-v3/process.json) |
| M0 integral-flow inverse controls | `check_m0_flow_inverse.g` | [m0-flow-inverse-gap-v2](../results/m0-flow-inverse-gap-v2/process.json) |
| N9 fixed-circuit finite retraction examples | `check_n9_fixed_circuit.g` | [n9-fixed-circuit-gap-v1](../results/n9-fixed-circuit-gap-v1/process.json) |

For example, in the separate review checkout:

```sh
bin/gap --quitonbreak scripts/check_n8_higher_negative_gap.g
```

This adapted launcher command reads the same mathematical fixture as the
linked original receipt. It is not a newly recorded run. Compare the
actual output with the original logs and read every diagnostic. GAP can
exit zero after an error; a zero exit code or a success-looking filename
is insufficient. Some successful historical runs contain documented
parse-time warnings. A marker also does not establish that a check covers
the theorem rather than its finite controls.

The complete command interfaces are documented separately:

- [N5 general finite-presentation command](../problems/N5/general-fp-audit.md)
  requires the explicit promise that the presented group is nilpotent.
  It returns factor words for a positive answer. The input relator format
  uses alternating generator indices and exponents.
- [N8 general word command](../problems/N8/general-word-audit.md) takes
  rank, class and a word of signed generator indices. Its positive output
  is a Hall-word DAG and two integer coordinate vectors. A partial trace
  or timeout is not a negative answer.
- [F34/F38 language interfaces](../problems/F38/language-interface-audit.md)
  compile equations and check a supplied controlled tuple grammar.
  The complete equation-to-EDT0L construction is unimplemented. All such
  interface outputs retain `complete_problem_decision: false`.

These formats differ; do not exchange N5 relators and N8 signed words.

## Lean fragments and prior formal developments

The new Lean fragments use Lean 4.24.0, reported commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, and Mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The retained S5 source archive
includes its dependency manifest and toolchain file. The
[S5 environment audit](../research/notes/S5-prior-Lean-proof-audit.md)
records setup, release digest, dependencies and trust limits.

Use each fragment's audit for its source files and import order. For
example, [F28's audit](../problems/F28/matrix-lean-audit.md) points to
`research/certificates/F28-matrix-lean/MatrixLemma.lean`; its source can be
passed to `lake env lean --trust=0 --stdin` in the pinned Mathlib workspace.
Some wrappers expect the original ignored scratch layout. Restoring that
layout or adapting the path is a review setup step, not a new theorem.

The transitive axiom audits and accepted declarations establish the
formalized fragments in that environment. They do not formalize the
entire group-theoretic conclusions. `--trust=0` does not mean every cached
Mathlib object was rebuilt or checked by an independent kernel. A5 and S5
are credited reproductions of prior work and are excluded from this
experiment's candidate count.

## Included and omitted data

Publisher bytes, statement fragments, retained renderings, proof sources,
compact certificates, failed attempts and original process logs are in Git.
Toolchains, package caches, browser libraries and the local virtual
environment are omitted. The 88 ignored A5 dependency source files have
an archived source bundle; three compiled B9 binaries have source/build
records. The artifact inventories identify those intentional omissions.

The F34/F38 language certificate retains the full parsed data in a
19,478,346-byte compact JSON file. Its omitted 127,724,170-byte pretty copy
contains the same data. The retained packaging record gives both hashes;
`json.dumps(data, indent=2)+'\n'` recreates the original formatted bytes.
This does not remove mathematical entries from the certificate.

The portability audit checks all Git blobs reachable from its recorded
refs, including historical versions, against the 90,000,000-byte limit.
It found none at or above that limit. Artifact integrity audits reconcile
selected manifest bindings with current or retained historical bytes;
they do not certify mathematical correctness or claim that every file has
a manifest binding.
