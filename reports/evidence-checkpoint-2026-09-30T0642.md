# Interim evidence checkpoint after the general N5/N8 implementations

30 September 2026, approximately 06:41--06:43 UTC. The experiment remains
active until **10:04:49.670358 UTC**. This checkpoint covers retained bytes,
recorded resource reservations and actual process state. It is neither the
deadline freeze nor a mathematical correctness certificate.

The most recent mathematical checks are the N8
[fixed/nonunit exceptional branches](../problems/N8/general-lattice-branches-audit.md).
The complete [N8 word command](../problems/N8/general-word-audit.md) and
[N5 finite-presentation command](../problems/N5/general-fp-audit.md) now connect
their respective candidate algorithms. Their structural and bibliographic
qualifications remain. Counts are still ten whole-entry coverage candidates,
two partial-entry candidates and zero established novel results.

## Retained evidence

| Item | Observation |
| --- | ---: |
| Selected manifests, ledgers and closure records | 172 |
| Hash bindings examined | 15,274 |
| Current-path matches | 15,216 |
| Exact historical matches | 58 |
| Missing or mismatched bound content without a retained exact version | 0 |
| Historical file versions validated by recovery indexes | 57 |
| Distinct files hashed, including logs and receipts | 5,377 |
| Bytes hashed across those files | 416,783,264 |
| Parse, recovery or unrecognized-manifest errors | 0 |
| Frozen launch-input hashes matching | 4 of 4 |

The higher binding count includes each process-closure record's receipt
bindings; it is not a count of distinct proofs or files. Old manifests remain
unchanged. Historical matches point to exact preserved bytes with their
recovery provenance, rather than substituting a newer working file's hash.

The 91 intentionally untracked paths are exactly the same as at the earlier
checkpoint: 88 A5 dependency-source files in ignored scratch space and three
B9 compiled binaries. All bound bytes match. The A5 publisher archive and
the B9 source/build evidence were retained and checked previously; this pass
did not repeat extraction or rebuild binaries. These dependencies are not
misrepresented as committed working files. The inventory concerns selected
hash-bearing records, not an assertion that every repository file is covered.

## Resource reservations and process outcomes

| Item | Observation |
| --- | ---: |
| Terminal recorded jobs after this checkpoint | 730 |
| Recorded successes | 540 |
| Recorded nonsuccesses | 190 |
| Timeout flags | 46 |
| Interruption flags | 24 |
| Peak simultaneous reserved CPU slots | 8 |
| Peak sum of requested per-process memory limits, decimal GB | 52 |
| Peak simultaneous recorded jobs | 7 |
| Recorded CPU-slot overlaps or budget excesses | 0 |
| Receipt/timestamp/success-flag inconsistencies | 0 |

Success is the runner's process/marker condition, not proof correctness.
Administrative and failed exploratory jobs are included. Timeout and
interruption flags need not be disjoint additional outcomes.

These are reconstructed reservations, not measured CPU consumption or
continuous aggregate peak RAM. Affinity and per-process address limits are
enforced; no cgroup or continuous tree-RSS measurement is claimed. Unrecorded
commands, network tools and model inference lie outside this accounting.

The artifact audit necessarily observed its own unfinished receipt, its sole
process issue. The resource audit likewise identified its own running process
and supervisor. Both terminal receipts and log hashes were checked afterward.
A subsequent read-only /proc observation found 730 terminal receipts, an empty
registry, and no other matching recorded PID/group or checkout worker.
Sequential census, PID reuse and detached-process attribution limitations
remain as documented in the observer. No worker was stopped by these audits.

The artifact job used one CPU/four GB and took 2.978 seconds. The resource job
used one CPU/two GB and took 0.170 seconds. Both stderr files are empty. An
initial resource-launch attempt reused an existing job name and was refused
before starting a child. The reservation was released and the original
receipt/output bytes were verified unchanged; a fresh v3 name was then used.
That pre-launch refusal is not another completed computational job.

## Records and cutoff

- [Artifact inventory](../research/audits/artifact-inventory-v5.json).
- [Resource inventory](../research/audits/resource-process-inventory-v3.json).
- [Actual process closure observation](../research/audits/checkpoint-0642-process-closure-v1.json).
- [Checkpoint bindings](../research/audits/checkpoint-0642-manifest-v1.json).

The observations precede this report and its administrative report/README
updates. Their exact prior versions were archived before editing; the new
files are bound by this checkpoint's manifest. The underlying scan identifies
its observed Git revision. The actual deadline still requires its own frozen
scope, final report, resource/process observations and deliverable audit.
