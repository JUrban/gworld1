# Expanded interim artifact checkpoint

30 September 2026, approximately 03:36--03:39 UTC. The experiment remains
active until **10:04:49.670358 UTC**. This expands the
[first checkpoint](artifact-checkpoint-2026-09-30.md); it is not the final
deadline snapshot or a mathematical correctness certificate.

The scanner now includes the certificate manifests, closing-audit
manifests, source manifests, current scope ledger and retained process-
closure receipt bindings. It explicitly validates the separate historical
recovery indexes. It never rewrites an old manifest or substitutes a
current file's hash for the expected older hash.

## Findings

| Item | Observed value |
| --- | --- |
| Selected manifest/ledger/closure files | 141 |
| Hash bindings examined | 6,731 |
| Current-path matches | 6,692 |
| Exact historical matches | 39 |
| Unresolved mismatches or missing bound content | 0 |
| Retained historical file versions validated | 33 |
| Distinct files hashed, including receipts/logs/recoveries | 4,824 |
| Bytes hashed across those distinct files | 394,840,860 |
| Parse errors, unrecognized empty manifests or recovery errors | 0 |
| Frozen launch-input hashes still matching | 4 of 4 |

The 39 historical matches point to separate exact copies rather than the
newer file currently at the original path. The report retains both the
current path's observed hash and the historical archive location, so a
reader can distinguish availability from an unchanged working file.

The first expanded pass found one additional historical mismatch: the
original 4,290-byte closing plan bound by the first checkpoint manifest.
It was recovered from local commit
`bdffbfa40007d49888140bdfd398ba19186a1e1a` and matched its expected SHA-256.
The expanded scanner also retains its own exact earlier source before
the coverage change. The current plan and old manifest remain intact.

The 91 intentionally untracked binding paths are unchanged: 88 A5
dependency-source files in ignored scratch space and three B9 compiled
binaries. The source files' bytes still match their declared hashes;
their retained publisher archive was checked at the first checkpoint.
The binaries have source/build evidence but are deliberately not described
as committed. This pass did not repeat the archive extraction or rebuild
the binaries. The newly recovered scanner and closing-plan copies are
included in this checkpoint's local commit.

## Process reconciliation

The two inventory jobs ran sequentially with one CPU, 8 decimal GB
per-process memory and a 120-second limit. They completed in 2.075 and
2.025 seconds with empty stderr. Their completion marker means that the
inventory finished; the findings above were inspected separately.

Each inventory necessarily observed its own receipt before termination.
This was its sole process issue. Both terminal receipts and their log
hashes were checked afterward. A separate actual /proc observation in
[artifact-inventory-process-closure-v1.json](../research/audits/artifact-inventory-process-closure-v1.json)
then found all 664 receipts terminal, an empty registry and no remaining
recorded job PID/group or other checkout worker. The observer and its
ancestors were explicitly identified. The process-attribution limits in
the [resource checkpoint](resource-process-checkpoint-2026-09-30.md) still
apply; this is an interim observation, not final deadline closure.

## Evidence and next use

- [Expanded pass before recovery](../research/audits/artifact-inventory-v3.json).
- [Reconciled pass](../research/audits/artifact-inventory-v4.json).
- [Scanner](../scripts/audit_artifact_integrity.py).
- [Closing-plan recovery](../research/audits/historical-closing-plan-recovery-v1.json).
- [Earlier scanner recovery](../research/audits/historical-inventory-scanner-recovery-v1.json).
- [Checkpoint manifest](../research/audits/expanded-checkpoint-manifest-v1.json).

The scope is the selected hash-bearing artifacts and their retained exact
versions. It does not claim that every repository file has a manifest,
that omitted software dependencies are committed, or that hash integrity
validates any mathematical statement. Failed proof attempts are retained
as failures. The structural and bibliographic limits in the individual
problem audits remain unchanged.

At final closeout, use a fresh output path for the expanded scanner and
inspect its findings, then inspect its terminal receipt and actual process
state. Identify that observation's cutoff and commit, and distinguish
any subsequent administrative files. The original research clock must
not be reset to run a final inventory.
