# Claim template — fill during the active run

- ID and named subpart / parameter range:
- UTC first candidate / final verified artifact / deadline inclusion:
- Original source URL, hash, lines/byte range:
- Exact statement, hypotheses, quantifiers and conventions:
- Source and rendering audit: who/what inspected it, when, and evidence:
- Literature check: queries, date, primary references, prior solved scope:
- Proposed conclusion and scope (whole entry / named subpart / other partial result):
- Proof and precise imported theorems:
- Imported Kourovka material and transfer-ledger record, if any:
- Computation: command, bounds, seed, exact arithmetic, versions, certificate and hashes:
- Independent verifier, negative controls and boundary cases:
- Statement fidelity / proof status / novelty status (separate judgments):
- Related entries; how double counting is avoided:
- Remaining gaps, qualifications, corrections or withdrawal:

Store one JSON object per line in `research/claims.jsonl`, with at least `id`, `scope`, `created_utc`, `claim`, `artifact`, `statement_status`, `proof_status`, `novelty_status`, and `deadline_status`. No preparation example is a claim. Keep dated changes rather than erasing failed claims.

For a transfer, record `date_utc`, `source_repo`, `source_revision`, `source_path`, `source_sha256`, `target_problem`, `kind`, `what_was_reused`, and `corrections_checked` in `research/transfers.jsonl`.
