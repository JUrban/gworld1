# F28 candidate audit

- Scope: the complete F28 question, with an explicit counterexample. The proof excludes f(H)<=H, and therefore also f(H)=H, for every nontrivial subgroup H<=S. No finite-generation or normality restriction is imposed.
- Original source: `sources/raw/probfree.html`, SHA-256 `2163a9d6e3c70b36c7df6943042f8b12896430b9e54d24dc23fba5160be4f04d`; statement starts at line 190 and occupies bytes [9936,10232). The frozen fragment hash is `abc5ba259f75d42f22815f55ab7f87e2911c77149ef71ecbec45a5ac999fc348`.
- Fidelity: the original HTML and linked background were read. The Chromium screenshot in `research/statement-audits/F28/statement.png` was actually viewed. It includes the full statement and adjacent entries; no transcription-only rendering was substituted for the publisher page.
- Derivation: approximately 11:02 UTC, 28 September 2026, before the focused novelty queries. First note: `research/notes/F28-matrix-lead.md`. The earlier portfolio's cover-swapping attempt retained invariant elements; the successful construction instead uses irrational elliptic conjugation.
- Proof: `proof.md`; all requirements have explicit arguments. Injectivity comes from a faithful matrix realization, rather than a numerical absence of relations. Infinite subgroups are covered element by element. The original positive-definite-form proof has been simplified to an integral sum-of-squares energy bound and parity recurrence; the entire matrix-orbit obstruction is now verified in Lean. The free-group bridge is not formalized.
- Computation: `results/f28-matrix-v1`, `results/f28-gap-v1`, and `results/f28-controls-v1` retain exact commands, versions via the environment provenance, return codes and output hashes. The exhaustive word bound is eight (13,120 words), with no random seed. GAP independently checks the matrix identities and subgroup data. Controls retain invariant subgroups when either key matrix hypothesis fails.
- Bibliography: see `literature/LEDGER.md`. Archived nearby primary work establishes simple virtual endomorphisms (normal-subgroup condition), discusses strong simplicity in nilpotent groups, or uses a distinct arithmetic construction. None of the inspected statements supplies this full example. The novelty check is preliminary and may need revision.
- Prior experiment: no mathematical argument or code imported from Kourovka. The arithmetic representation was derived during this run; related Kapovich methodology was found afterwards and credited.
- Counting: one whole-entry candidate, F28. The induced faithful binary-tree action also relates to GA5(c), whose existence question has older positive examples; it is not counted again.
- Review: no independent mathematical review has been performed. Exact computations support implementation details, not the completeness of the proof or its novelty.

## 29 September: integral proof and Lean verification

The energy bound and parity recurrence replace the real norm and
algebraic-integer steps without changing the example or its scope.
`matrix-lean-audit.md` records the exact formal statement, trust boundary,
versioned failures and successful compilation. The same original HTML,
F28/GA5 background and actual statement rendering were checked again.
All-subgroup scope is unchanged. This is stronger internal verification,
not specialist review or a new novelty assessment.
