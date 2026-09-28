# GroupWorld experiment instructions

- Read `state/session.json` at the start of every work period. Until the user explicitly launches the experiment, do preparation only: no solving, mathematical probes, candidate selection, or autonomous research jobs. Never infer launch authorization from these files.
- Keep this repository independent of its enclosing Kourovka checkout. Do not modify the parent repository, its paper, outreach drafts, results or clock.
- At launch follow `START_HERE.md` and `docs/PROTOCOL.md`. Record the user's actual instruction. Do not restart or extend the 48-hour clock after interruptions.
- Do not spawn subagents without explicit user authorization. Local parallel computational processes are distinct from agents and must respect the shared budget.
- Preserve the archived publisher bytes. Derived text is only a search aid. Before claiming anything, compare the full original HTML, its rendered statement, and the exact mathematical transcription. Do not claim visual inspection unless it happened.
- Track each named subpart and all quantifiers. A heading star or Hall of Fame mention can describe only partial progress. An unstarred entry is not verified open. Consult `docs/STATUS_NOTES.md` and primary sources.
- Separate statement fidelity, proof correctness, bibliographic status and novelty. Model agreement is not specialist validation. Count whole entries and subparts separately and avoid double counting related questions.
- Record imported Kourovka arguments or code with origin, revision, exact claim and its current corrected status in `research/transfers.jsonl`. Do not silently inherit obsolete claims or private correspondence. Consult `docs/KOUROVKA_LESSONS.md` first.
- Record claims in `research/claims.jsonl`; use `research/CLAIM_TEMPLATE.md`. Preserve failed attempts and negative controls. Use exact arithmetic and compact independently checkable certificates where possible.
- For computations use `scripts/run_recorded.py`; record seeds, bounds and representation conventions in the accompanying research note. Respect the limitations of its resource controls. Zero exit status or a marker alone is not mathematical validation.
- Commit useful work locally and keep the report current. Do not push, publish, email or contact others without explicit authorization.
- Keep blobs below 90,000,000 bytes. Put genuinely large outputs in ignored `large-artifacts/`, document their hashes and regeneration commands, and retain compact verifiers in Git. Never describe omitted data as included.
