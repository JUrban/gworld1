# Active-run tools

Recorded 28 September 2026.

- GAP 4.16.1, external installation selected through ignored `config/local-tools.json` and `bin/gap`. Confirmed available: smallgrp 1.7.0, fga 1.5.0, kbmag 1.6.0, nq 2.5.11, polycyclic 2.18, ace 5.7.0.
- Python 3.12.3. Created ignored `.venv` with `uv venv --clear .venv` after system `venv` lacked ensurepip. Installed playwright 1.63.0 and pypdf 6.19.0. System `pdftotext` is also available.
- Playwright Chromium installed with `.venv/bin/playwright install chromium`. Runtime libraries unavailable on the base image were downloaded from Ubuntu noble repositories using isolated apt state/cache under `scratch/apt/`, then extracted without root using `dpkg-deb -x` into `scratch/browser-libs/root`.
- Downloaded runtime packages: libatk1.0-0t64, libatk-bridge2.0-0t64, libxcomposite1, libxdamage1, libxfixes3, libxrandr2, libgbm1, libatspi2.0-0t64. Rendering command:

```sh
LD_LIBRARY_PATH="$PWD/scratch/browser-libs/root/usr/lib/x86_64-linux-gnu" \
  .venv/bin/python scripts/render_statement.py F42
```

The renderer opens archived original HTML with external HTTP(S) requests blocked. Its PNG captures only the selected paragraph; additional paragraphs/subparts require separate inspection. A generated capture is not evidence that an agent has visually inspected it. Inspection is recorded separately in each audit's metadata.

Runtime installations and package downloads are ignored rather than embedded in Git. These dependencies support source inspection; they are not mathematical evidence or imported Kourovka arguments.

For the N8 exact prototype installed SymPy 1.14.0 and mpmath 1.3.0 in the ignored virtual environment. Smith decompositions use `sympy.polys.matrices.normalforms.smith_normal_decomp`; the implementation checks D=S*A*T on each use.
