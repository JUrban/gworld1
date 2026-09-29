# A5: prior affirmative answer, with reproduced Lean verification

29 September 2026, approximately 07:39–07:50 UTC.
**External prior result; excluded from the experiment's solution count.**

Achyuth Jayadevan, [*Finite presentations of metabelian groups: effective
enumeration via Laurent relations*, arXiv:2609.10281v1](https://arxiv.org/abs/2609.10281v1),
was submitted on 9 September 2026, before this experiment. Its Lean
development builds here, its complete project axiom audit passes, and
independent restatements of the relevant enumeration and certificate
claims compile. Retire A5 as a discovery target on this evidence.
No specialist or journal review is asserted.

## Exact statement and source

Read the complete original `sources/raw/probalg.html`, the A5 background
in `Back2.html`, and the captured A5 paragraph. The actual screenshot was
viewed. The original question asks for recursive enumerability of finitely
presented metabelian groups; its background discusses recognition from
ordinary presentations. There is no restriction to presentations within
the metabelian variety, to torsion-free groups, or to a cyclic quotient.

The preprint's argument was read, including the radius propagation,
central pullback, cofinal epimorphic covers, and finite relator certificates.
PDF pages 1 and 5 were rendered and actually viewed. These are retained
beside the independent Lean check. The full PDF had already been archived
in this experiment; this turn added the version-pinned arXiv source archive:

    URL: https://arxiv.org/src/2609.10281v1
    bytes: 127537
    SHA256: 891b22e3b3461029d2d56719afaa36a2b405878a85bf78003d7a4a5663b6896b

Its `anc/lean` subtree contains 88 files, totaling 467927 bytes, including
CC0 licensing and the author's checksums. The source archive is retained
under `literature/raw`; `research/certificates/A5-prior-lean/source-manifest.json`
records every extracted file's hash. No author source bytes were modified.

## Formal scope

Directly inspected the definitions and proofs in the presentation,
computability, final enumeration, cover soundness, cofinality, and
Bieri–Strebel necessity modules, plus the author's completion and audit
files. The important definitions are:

- `PresentationCode = Nat × List (List (Nat × Bool))`: an ordinary finite
  alphabet and a finite list of relator words.
- `GroupOf`: Mathlib's ordinary `PresentedGroup`, not a quotient that
  silently imposes the metabelian law.
- `WellFormed`: all relator letter indices lie in the declared alphabet.
- `Metabelian`: every two commutators commute, with four universally
  quantified group elements.
- `REPred`, `Primrec₂`: the imported Mathlib computability notions.

Failed natural-number decoding returns the trivial empty presentation.
This coding convention causes no missing group or presentation: the
development proves decode-after-encode equals the original presentation.
The separate certificate restatement quantifies over every structured
presentation, not merely over successfully selected examples.

`StatementCheck.lean` expands the alphabet checks, ordinary presented
group, and commutators explicitly. It proves recursive enumerability and
the existence of a primitive-recursive certificate test, using only the
author's final theorems. It assumes neither tameness nor a hypothetical
enumerator. The author's Bieri–Strebel necessity module also contains
an actual proof, rather than an added axiom.

## Recorded verification and failures

The existing pinned Lean 4.24.0 toolchain was reused: executable revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. Its download and release digest
were checked in the earlier S5 audit. All nine dependency revisions match
this source's manifest; Mathlib is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The dependency package/cache
directory is shared with that earlier external proof, while this project's
source and build outputs are separate.

| Recorded job | Outcome |
| --- | --- |
| `a5-prior-lean-audit-v1` | Stopped before Lean proof compilation: arXiv archive omitted executable permission on `scripts/with-lean.sh`. Exit 1, 0.320 s. |
| `a5-prior-lean-audit-v2` | Author build and full axiom audit passed; subsequently failed in our first independent certificate restatement. Exit 1, 280.621 s. |
| `a5-independent-statement-v2` | Both corrected independent statements and their transitive axiom checks passed. Exit 0. |

The local permission on `with-lean.sh` was restored for the second job;
its contents and hash were unchanged. The author's `lake --wfail build`
reported 3181 jobs, including cached dependencies. This is not 3181
newly compiled author modules. `Audit.lean` then successfully checked
all **1624 project declarations**, including private declarations.
Only `propext`, `Classical.choice`, and `Quot.sound` were permitted.

The later failure was in our proof of the structured-presentation
restatement: simplification did not transport the dependent group
instance across decode-after-encode. Lean reported a type mismatch and
the axiom audit caught its generated `sorryAx`. The unsuccessful source
is preserved as `StatementCheck-v1-failed.lean`. The corrected proof uses
congruence of the whole group-property predicate; the mathematical
statement is unchanged. Both independent statements now have exactly
the three permitted axioms. The successful author's audit was not rerun
merely to obtain an overall green wrapper record.

The source scan found no added axiom, `sorry`, `unsafe`, `native_decide`,
or external proof implementation in the author's Lean modules. The
reported options concern recursion/heartbeat budgets or `autoImplicit`.
Not every line of every module was manually audited.

This is standard Lean verification using trusted pinned dependency
caches. The retained `--trust=0` setting **does not** establish that all
imported Mathlib proofs were independently rechecked. It is not a
full foundational rebuild or independent-kernel validation.

## Reproduction

Restore the retained archive to `scratch/A5-arxiv-source`, restore the
executable permission on `anc/lean/scripts/with-lean.sh`, and install the
pinned toolchain and dependencies. The local package symlink can instead
be replaced by a normal pinned `lake exe cache get` setup. Then:

```sh
python3 scripts/run_recorded.py --name a5-prior-replay \
  --cores 8 --memory-gb 16 --timeout 900 \
  --expect 'PASS: pinned A5 prior proof build, author audit, and independent scope check' \
  -- env PATH="$PWD/scratch/lean-4.24-setup/lean-4.24.0-linux/bin:$PATH" \
  LEAN_NUM_THREADS=8 python3 scripts/check_a5_prior_lean.py
```

Actual logs, return codes, source snapshots, and hashes are retained.
The all-source audit used eight cores and a 16GB per-process cap; the
standalone corrected statement check used four cores and 8GB.

The consequence for the separate M3 question is in
`M3-effective-metabelian-quotient.md`. It does not settle M3. Counts stay
**six whole candidates, three partial candidates, zero established novel
results**. No mathematical material was imported from our Kourovka run;
the external development's `Kourovka` namespace names the author's problem.
