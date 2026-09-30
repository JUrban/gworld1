# Editorial review of version 1

Completed 2026-09-30T14:31:46.373590+00:00 by the same agent that prepared
the manuscript. This is a source, exposition and production check, not an
independent mathematical referee report.

## Scope and preservation

The manuscript describes all twelve counted entries, gives the inventory
before the proofs, credits four prior named parts and retains the ten-whole /
two-partial deadline classification. It does not claim established novelty,
full formal verification or external review. The N5/N8 implementation claims
are distinguished from the unimplemented full F34/F38(a) grammar generator.
The four-strand B9 gap and the exact-growth G9 gap are explicit.

The introductory summary, result tables and mathematical expositions were
compared with the frozen scope record. The twelve original statement images
and the F3 cross-reference for M0 were viewed during preparation. The entry
map records source/proof/audit hashes. The longer N5, F38(c) and N8 steps
are exposed in appendices rather than replaced by computational success
claims. This presentation does not independently certify those steps.

`audit_paper.py` checks all 96 frozen ledger bindings, the four launch inputs,
the additional statement/proof/image bindings, labels, citations, README
links, PDF text and artifact paths at the public handoff commit. Its report
is `editorial-audit.json`. The tracked research, source archive, experiment
state and pre-existing reports remain unchanged; only the paper directory
and root landing README were edited. The old README is retained verbatim.

## Build and visual inspection

The final PDF has **33 pages** and SHA-256
`f27240bd46e1af516b110992af916799db85ad6de02738693c750468b4741621`.
It was built with Tectonic 0.17.0; the successful invocation, input/output
hashes and logs are retained in the build manifest and text logs.
The final log has no overfull/underfull boxes, missing characters, undefined
citations/references or multiply defined labels.

The first complete layout was inspected on pages 1, 3, 6, 12, 15, 16, 19,
21, 22, 24, 28, 31 and 34. That pass covered the authors and funding,
inventory, representative proofs and equations, bibliography and appendices.
It led to keeping the two partial-result rows together and widening longtable
captions. After the final rebuild, pages **1, 3, 4, 6, 19, 24, 28, 31 and 33**
were rendered and actually viewed again. The final paper is one page shorter;
the initial attempt to render a now-nonexistent page 34 was corrected to 33.
No claim is made to have visually inspected every final page.

All 33 pages also passed the text-bounding-box check (no text outside the
page). PDF annotations confirm both the AI4REASON sponsors hyperlink and
Shpilrain's supplied email on page one. These checks are in `pdf-checks.json`.
The source archive was extracted into a fresh directory and compiled; its
PDF has exactly the same extracted layout text as the published PDF.
The archive manifest records every member hash and the actual return code.
Byte-identical PDFs across engines, fonts or build times are not claimed.

## Attribution and remaining review

Shpilrain is credited for hosting the collection and suggesting the experiment,
and is included as coauthor with the supplied email. Kinyon's visit and Urban's
funding footnotes follow the Kourovka paper, including the linked sponsors.
Both the public Kourovka repository and its version 4 PDF are cited; the latter
was retrieved at its actual public commit and hashed in `provenance.json`.
Bibliographic corrections and reading limits are in `bibliography-notes.md`.

Specialist review is still needed, particularly for the imported shortening,
solution-language, definable-set and ordered-tree interfaces and the all-rank
commutator argument. The numerical examples, certificates and formalized
fragments have the scopes stated in the paper. No new solver run or additional
mathematical result was added during manuscript preparation.

A final rebuild after removing a trailing blank line preserved all extracted
layout text and produced byte-identical PNGs for the nine reviewed pages.
The PDF hash above and all build/package manifests refer to that rebuild.
