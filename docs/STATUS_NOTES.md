# Status notes for the source snapshot

The snapshot of 28 September 2026 has 195 numbered entries across 16 categories. The landing page's general description says “over 200”; this catalogue counts the visible numbered headings, not subparts, historical entries, or implied questions. The original numbering is retained, including `M0` and all of `F1`–`F42`.

No comprehensive current literature survey has been performed. A problem's presence here is not evidence that it remains open. **Do not use “195 minus the marked entries” as an open-problem count.**

## Preserved evidence

- 49 entries have a star at the numbered heading.
- 11 other entries have stars immediately before named subparts: F1(a), F24(a), F25(b), F32(b), F34(b), F38(b), F39(b), OR7(b), B5(b), N8(a), N9(b).
- 69 Hall of Fame links refer to 58 distinct numbered entries. Visible labels and attribution text are retained in `data/hall_of_fame.json`, including multiple contributors to one problem.
- In total, 60 entries have a heading/subpart star or Hall of Fame indication. This reports site metadata; it does not establish that all parts or all parameter ranges are solved.
- One external status update, O12(b), adds known prior-resolution evidence for a 61st entry. The publisher's abstract for [Giles Gardam, Annals of Mathematics 194 (2021), 967–979](https://annals.math.princeton.edu/2021/194-3/p09) supplies a negative answer to the general unit question using a torsion-free group over the field of order two. This says nothing about O12(a). We checked the bibliographic status, not the proof, during preparation.

The background pages are archived and indexed as source evidence, not newly endorsed arguments. For example, B5(b)'s background describes a result for **n > 6**, whereas its problem page begins **n > 4**. FP4's background distinguishes rank 2, rank 3, and larger ranks. S3 has no site star or Hall entry, but its background records earlier affirmative results with restrictions. These cases must not be collapsed into a binary solved/open flag.

## Source discrepancies

- F27, F28 and F30 start after `<BR>` rather than `<P>`; they are included.
- Some problem headings have no named HTML anchor. Catalogue references use the visible label and byte range, not anchors alone.
- Hall of Fame labels FP7 and FP8 link to anchors FP8 and FP9 respectively. The visible labels govern indexing; the mismatches are preserved in the metadata. The background pages have the same shifted anchors.
- Background entries O5, O6 and O7 print `(05)`, `(06)`, `(07)` with a zero, while their anchors use O. The index associates those sections with O5–O7; the raw source is unchanged.
- Some background sections cover several problems, such as B1–B2, B5–B7, and H6–H10. The catalogue records shared coverage.
- A malformed empty link `Back.htm#(O3)l` gives HTTP 404. The immediately following correct `Back.html#(O3)` link works, and its page is archived.
- Commented-out Hall of Fame claims are not visible endorsements and are excluded from the active metadata. The comments remain in the raw archive.

## At the start of research

For each candidate record the precise original scope, reported prior progress, relevant primary references and unresolved scope after a current literature check. Split named subparts and parameter ranges explicitly. Add dated evidence to `data/status_updates.json` and record decisions in `research/triage.csv`; do not silently relabel all unmarked entries as open. Check logically related and duplicate questions when counting outcomes.

`data/problems.json` is the preparation snapshot. Its `research_status` fields describe preparation, and should not be confused with the later working triage/claims ledgers. Statement transcriptions and rendering checks are pending for every entry.
