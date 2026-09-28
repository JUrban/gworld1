# Protocol for the future 48-hour run

The objective is rigorous progress on the supplied GroupWorld collection, with explicit separation of complete answers, answers to named subparts, other partial results, independently rediscovered known results, and unsuccessful investigations. Preparation has downloaded and indexed the source, checked one known bibliographic update, and tested infrastructure. It has not selected targets or attempted proofs.

## Inputs and reuse

Freeze the preparation commit, source hashes, configuration and launch instruction in the run record. The initial catalogue is a snapshot, not a claim that all entries remain open. Preserve both the problem pages and their background, which may qualify a question or already contain an answer. Any later source refresh or status correction is a separate dated record, not a silent replacement.

The experiment may use web literature, GAP and the existing Kourovka archive. This is disclosed prior experience. Record actual mathematical/code transfers and citations. Do not import previous claims as established facts: the Kourovka record contains corrections and provisional assessments.

## Budget and work allocation

The proposed computational ceiling is 20 CPU cores and 100 GB RAM for a 48-hour wall-clock run. These are inherited defaults, not a claim that the current machine already has aggregate cgroup enforcement. The recorded runner allocates CPU slots and cooperative memory reservations and sets affinity/per-process address-space limits. Monitor processes, total memory, disk use and deadline. Stop discovery jobs by the deadline; clearly label any later editing or review as post-deadline.

Suggested allocation, adjustable during the active run:

- First 1–3 hours: check exact statements, named subparts and literature status; establish a diverse portfolio. Read site background before treating a question as unsolved.
- Hours 2–18: alternate bounded exact computations and mathematical reasoning. Log assumptions, search bounds, seeds, failures and useful reductions. Avoid unproductive exhaustive searches.
- Hours 12–40: develop the strongest leads into self-contained arguments and minimal verification artifacts. Recheck original hypotheses and novelty against primary sources.
- Final 8 hours, overlapping other work: audit statements and proofs separately, reproduce key computations, check boundary cases and negative controls, reconcile counts, freeze deadline artifacts and write the final report.

## Evidence and counting

For every candidate, retain the exact source location and hash, faithful mathematical statement, answered scope, proof, imported results with precise citations, any computation and an independent check. A counterexample must satisfy every original hypothesis. A bounded non-hit does not establish a general theorem. A known theorem applied to an already solved problem is a rediscovery or exposition, not a new resolution.

Use a parent ID such as `F1` and explicit scope such as `F1(a)`. Do not infer all parts from a whole-entry marker. Link overlapping questions and keep both the number of entries and the number of named subparts. Keep correctness and novelty judgments separate; uncertainty remains visible. The statement audit must use the original rendering as well as the source and must not be inferred from proof review.

No outside mathematical review has been commissioned for this new run. If one is later authorized, preserve the prompt, model/tool configuration, reviews, replies and resulting changes. Do not represent an LLM review as expert human approval.

## Deliverables

During the run maintain `research/LOG.md`, `research/triage.csv`, `research/claims.jsonl`, and the transfer ledger. Produce proofs and compact verifiers alongside their problem IDs, plus `reports/FINAL_REPORT.md`. At the deadline preserve a dated ledger and commit identifying what was actually available then. Report post-deadline corrections distinctly and retain withdrawn claims in the historical accounting.
