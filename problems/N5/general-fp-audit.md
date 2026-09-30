# General finite-presentation command for N5

30 September 2026. The complete N5 pipeline now accepts an ordinary finite
presentation **promised to define a nilpotent group, with no supplied class
bound**, decides nontrivial direct decomposability, and returns generators
of two factors as words in the original presentation. This connects the
[native pipeline](general-pipeline-audit.md); it does not add a candidate
or certify the novelty or correctness of the general written argument.

## Input promise and conversion

The [nq manual](https://gap-packages.github.io/nq/doc/chap3.html) specifies that
omitting the class bound computes the largest nilpotent quotient when it
exists. Under the input promise, this is the input group itself. The command
does not infer nilpotency from successful quotient computation: for a group
outside the promised class, its largest nilpotent quotient could be proper.
The required `--assume-nilpotent` option makes that hypothesis explicit.

The zero-generator presentation is handled directly. Otherwise the program
first computes the abelianization. If this is cyclic, the promised nilpotent
group is cyclic too: its second and third lower central terms coincide,
and nilpotency forces them to be trivial. This also avoids the installed
nq cyclic/high-class assertion previously encountered in the class-two work.
Every other presentation goes through nq with **no class parameter**.

The resulting native group is passed through torsion removal, central-series
rebasing, exact matrix logarithms, rational Lie decomposition, rational-support
kernels, bounded-index normal subgroup enumeration, and central lifting.
Before passing between separately reconstructed GAP stages, the command
compares canonical serialized data including the native group's presentation
and the images of every original generator. This binds the chosen coordinate
system as well as the abstract group invariants.

For a positive answer, all accepted central branches are checked as actual
native direct products. For the selected branch, preimages under the original
presentation map supply factor words; mapping them forward is checked against
the constructed native generators. The conclusion for the original group is
conditional on the stated nilpotency promise and the correctness of the
credited algorithms and written N5 argument. It is not a formal certificate
of the whole mathematical theorem.

## Command and data

`scripts/n5_general_fp.py` takes JSON of the form

    {"generators": 2, "relators": [[1, -1, 2, -1, 1, 1, 2, 1]]}

Each relator is a list of generator-index/exponent pairs, with one-based
indices; this example presents Z^2. During the experiment, invoke it through
the recorder, using a fresh output directory and job name:

```sh
python3 scripts/run_recorded.py --name n5-custom-input --cores 1 --memory-gb 8 \
  --timeout 180 --expect 'PASS N5 general fp command' -- \
  .venv/bin/python scripts/n5_general_fp.py --input presentation.json \
  --output research/certificates/N5-custom-input --assume-nilpotent
```

The output retains the input, generated GAP scripts, rational decomposition,
complete quotient branch data, central decisions, stage logs and final
`answer.json`. Positive `factor_words` use the same index/exponent convention.
The output directory must be new. A failed or timed-out stage does not return
an indecomposability answer. The experiment recorder enforces the original
deadline; no clock change is part of this interface.

## Verification and retained failure

Fifteen finite presentations were converted: the twelve native controls,
infinite cyclic and cyclic-of-order-six controls, and a class-three presentation
with an explicitly added redundant generator t=x1*x2. For each, a homomorphism
from the known native group to the converted group has trivial kernel and full
image. The redundant-generator case additionally checks the marked generator
diagram. All fifteen conversions pass without a supplied class bound.

Five standalone command tests then pass:

| Input | Answer | Central branches | Accepted branches | Returned factor words |
| --- | --- | ---: | ---: | ---: |
| free rank-two, class four | no | 2 | 0 | 0 |
| class-three group x D8 | yes | 4 | 2 | 8 |
| class-three group x Heisenberg x Z | yes | 4 | 4 | 9 |
| cyclic group of order six | yes | 1 | 1 | 2 |
| trivial presentation | no | 1 | 0 | 0 |

Here “no” means there is no direct product with both factors nontrivial.
The seven accepted branches are all replayed as actual native products;
nineteen factor words are returned across the three positive commands.
A command omitting the promise option exits with argparse status two before
creating the requested output directory. This is an expected negative control,
retained as a nonsuccessful process receipt.

The first standalone class-four run failed at its cross-stage data comparison:
the GAP serializer parsed rational JSON strings as rational numbers, while the
reconstructed export still held strings. The failed command, generated files,
logs and exact original Python source are preserved. The repair compares
canonical JSON bytes while separately supplying numerical structure constants
to the algebraic code. The corrected class-four run and the four other commands
pass. No mathematical change was required.

The failed GAP stage returned process status zero despite printing its error;
its success marker was absent. The command correctly rejected it by checking
both stderr and the marker. A later administrative hash audit initially treated
zero status alone as success, stopped on this retained stderr, and was corrected
before the final manifest was written. No mathematical run was repeated for it.

Eight recorded runs cover this stage: conversion (3.028 seconds), failed first
command (4.584), five successful commands (7.346, 7.294, 8.398, 6.592 and 6.692),
and omitted-promise rejection (0.369). Successful research jobs reserve one
CPU/eight decimal GB; the argument rejection reserves one CPU/two GB. The
largest overlap is three CPU slots and 24 GB of requested per-process limits.
These are reservations, not measured aggregate RSS. Successful outer and GAP
stage stderr files are empty. Actual process closure, hashes and source bindings
are retained with the manifest.

The original full HTML and N5 paragraph were read and the statement rendering
viewed earlier in this work period. All development and proof audits remain
same-agent work; GAP/Python agreement is separate program evidence, not an
external referee. General completeness and practicality still require review.
The current status remains ten whole-entry coverage candidates, two partial
candidates and zero established novel results.
