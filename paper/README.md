# Forty-eight hours with GroupWorld

**[Read the paper (PDF)](gworld-experiment.pdf)** ·
[LaTeX source](main.tex) · [Standalone source archive](gworld-experiment-source.tar.gz)

Version 1, 30 September 2026. Authors: Codex `gpt-6-astra` (OpenAI),
Michael Kinyon, Josef Urban and Vladimir Shpilrain. Shpilrain hosts the
problem collection and suggested this experiment.

This follows the format of the
[Kourovka paper, version 4](https://github.com/JUrban/kour1/blob/dce7931e980c7db83100a07fbe084fc1dd655fdb/paper/kourovka-experiment.pdf),
which is cited alongside its research repository. The visit and funding
acknowledgments appear as first-page author footnotes; the AI4REASON
sponsors link is clickable.

The paper presents the **ten whole-entry coverage candidates and two
partial entries** recorded at the deadline. Complete coverage includes
four credited prior subparts. These are proposed arguments awaiting
independent specialist review, not twelve established new solutions.
The review history of the earlier Kourovka experiment does not constitute
a review of this one.

## Reading and reviewing

Section 2 gives the complete inventory before the proofs. Sections 4–7
contain the mathematics, and the appendices develop the central-splitting,
shortening and all-class commutator arguments and the certificate details.

| Entry | Paper source | Frozen argument |
|---|---|---|
| F28, H4, M0 | [Explicit constructions](sections/explicit.tex) | [F28](../problems/F28/proof.md), [H4](../problems/H4/proof.md), [M0](../problems/M0/proof.md) |
| F41, GA3, F34, F38 | [Free groups and tree actions](sections/free-groups.tex) | See the [review guide](../reports/CURRENT_RESULTS.md) for controlling arguments and supplements |
| N5, N8, N9 | [Nilpotent groups](sections/nilpotent.tex) | [N5](../problems/N5/proof.md), [N8](../problems/N8/general-proof.md), [N9](../problems/N9/proof.md) |
| G9, B9 | [Partial results](sections/partial.tex) | [G9](../problems/G9/flow-growth-proof.md), [B9](../problems/B9/infinite-family-proof.md) |

The frozen [scope ledger](../reports/RESULT_SCOPE.md) remains authoritative
for the deadline classification. Paper links to the research record use
the public handoff commit `0d6b855fd6d9d9e5ddb5dbd186a2a590164c1341`.
The last research commit was `401213c09222ebebaf99589553258cf74a918187`.
Manuscript preparation is post-experiment work and does not restart the clock.

## Building

From this directory, with Tectonic installed:

```sh
python3 scripts/build_paper.py
# When all TeX resources are already cached:
python3 scripts/build_paper.py --only-cached
```

Set `PAPER_TECTONIC` or pass `--tectonic /path/to/tectonic` if it is not
on `PATH`. This checkout used Tectonic 0.17.0. The build script writes
`gworld-experiment.pdf`, retains `main.bbl`, and records actual invocation,
return status and source/output hashes in `data/build-manifest.json`.
Attempts, including failures, go into ignored `build/` subdirectories.
The latest successful TeX and console logs are also retained under `data/`.
Tectonic can download standard TeX resources unless `--only-cached` is set.

Alternatively, a standard LaTeX installation with the packages in
`preamble.tex` can run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

This produces `main.pdf`. The retained `main.bbl` also permits compilation
without regenerating the bibliography. The source archive contains all
TeX inputs and bibliography files and needs no research software or data.
Font and engine versions can change pagination; byte-identical output
across TeX installations is not claimed.

## Editorial checks

```sh
python3 scripts/audit_paper.py
python3 scripts/package_paper.py
```

The audit uses Python 3, Git and Poppler's `pdftotext`. It checks source
inclusion, labels and citations, all twelve entries, artifact links at the
pinned commit, source/proof bindings, the frozen research files and PDF
content. Run it in the full repository; the standalone archive is for
compilation. Packaging records member hashes and verifies a fresh extracted
build with Tectonic. Both commands write their own reports under `data/`.
These are editorial and artifact checks, not independent mathematical
validation. [Entry map](data/entry-map.json), [provenance](data/provenance.json)
and [review notes](data/editorial-review.md) document the checks and their limits.
