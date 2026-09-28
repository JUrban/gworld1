# Reusing the Kourovka experiment

Use the existing repository as a read-only library, with its revision recorded in `provenance/kourovka.json`. Local paths are configured in ignored `config/local-tools.json`; the public reference is https://github.com/JUrban/kour1. This local source revision is from the unfiltered repository: GitHub history was filtered with `--strip-blobs-bigger-than 90M`, so public commit IDs may differ. A public equivalent has not been asserted here; retained file hashes provide content provenance.

Useful entry points in that repository:

- `research/PLAN.md`: workflow for the 48-hour run. Its dates and live state belong to the old experiment.
- `paper/appendices/protocol.tex`: methods and limits to the original experiment.
- `paper/appendices/statement-correction.tex` and `paper/reviews/v3-2026-09-19/`: the correction to 10.35 and the subsequent statement audit.
- `paper/sections/candidate-proofs.tex`, `paper/main.tex`, `scripts/`, and `results/`: potential arguments, implementation patterns and verification records. Check current qualifications before reusing a result.
- `reports/FINAL_REPORT.md`: historical deadline report, not the final corrected correctness/novelty assessment.
- `scripts/run_21_100_recorded.py`: the process-evidence pattern adapted in the new generic runner.

## Lessons applied here

1. **Read the actual statement.** Kourovka 10.35 was misread with Q in place of the algebraic closure of Q. Proof checking and a second model's review did not catch that mismatch. The claim was withdrawn. Retain raw source and inspect rendering; check fields, quantifiers, notation, conventions and named subparts separately from the proof.
2. **Keep historical counts distinct from current assessments.** The Kourovka deadline count was 46 candidates; one was withdrawn, leaving 45 remaining candidates. Neither figure is a count of established novel theorems. The new repository starts with zero claims.
3. **Treat solutions and scope as bibliographic questions.** Stars can indicate only a subpart or parameter range. An unstarred historical question may now be solved. Check primary sources and preserve rediscovery credit. Do not call a limited literature search proof of novelty.
4. **Verify computations independently of the search predicate.** Retain exact arithmetic, independently checkable certificates, alternative representations, negative controls and boundary cases. A successful program run is distinct from a verified mathematical claim.
5. **Record what actually ran.** Preserve the real subprocess return code, timeout/interruption, stdout, stderr and hashes. Never turn a crash, truncated output, or a missing success marker into a successful computation.
6. **Make the public artifact small and reproducible.** The old public repository omits large blobs. Prefer compact certificates and verifiers; list hashes and regeneration commands for any omitted outputs. Do not make large GAP installations or huge certificates part of this repository's Git history.
7. **Disclose reuse.** Preserve separate experiment clocks and histories while using established tools and prior experience. Record each later imported argument or program in `research/transfers.jsonl`, including corrections and the exact claim reused.

No old research results, private contacts, outreach drafts, active session state, certificates, or repository history have been bulk-copied into this repository. Infrastructure choices and these lessons are the preparation transfers.
