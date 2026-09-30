# Evidence checkpoint after the G9 and B9 refinements

30 September 2026, 08:30--08:32 UTC. The experiment remains active until
10:04:49.670358 UTC. This is a byte, receipt and resource audit, not a
mathematical correctness certificate or the deadline freeze.

Since the previous checkpoint the experiment added the shared F34/F38
language interface, stronger G9 lower bounds, and B9 first-color and
infinite-family exclusions. The current G9 enclosure is
2.676871486 <= lambda_2 <= 2.943737759. The whole/partial/established-novel
counts remain 10/2/0.

## Artifact observations

| Item | Count |
| --- | ---: |
| Selected manifests, ledgers and closure records | 189 |
| Hash bindings examined | 21,612 |
| Current-path matches | 21,502 |
| Exact historical matches | 110 |
| Unresolved missing/mismatched bindings | 0 |
| Historical versions validated | 114 |
| Distinct files hashed | 5,630 |
| Bytes hashed across those files | 508,055,626 |
| Parse, recovery and unrecognized-manifest errors | 0 |
| Frozen launch-input hashes matching | 4 of 4 |

The 91 deliberately untracked paths are unchanged from the earlier
checkpoint: 88 A5 dependency sources and three B9 compiled binaries.
Their recorded bytes match. The audit does not assert that all repository
files have manifest bindings. Multiple bindings can refer to the same file.

The first pass reported five missing README files. Each was actually a
root README reference that the auditor interpreted relative to its manifest.
The auditor now explicitly recognizes root metadata names, after honoring
the existing project-local convention used for Lean manifests. The old
script and first inventory are retained. No manifest was changed to make a
hash match. The corrected pass resolves all five references, including
their exact archived historical versions.

An administrative comparison initially used an incorrect filename for the
previous inventory and stopped. Reading the actual `artifact-inventory-v5`
file then confirmed that the untracked path set is unchanged. No mathematical
job or artifact was affected.

## Process and resource observations

All **763** recorded jobs have terminal receipts: **567** runner successes
and **196** nonsuccesses, including 46 timeout flags and 24 interruption
flags. Success is the process/marker condition, not proof correctness.
Administrative audits and failed exploratory work are included.

The reservation inventory finds no recorded budget excess, overlapping CPU
slot, inconsistent receipt or out-of-window job. Historical peaks remain
eight reserved CPUs, a 52 GB sum of requested per-process address-space
limits, and seven simultaneous jobs. These are reservation records, not
continuous measurements of aggregate RAM or CPU consumption. Unrecorded
commands, network tools and model inference remain outside this accounting.

Each audit necessarily observed its own running receipt. Its final receipt,
log hashes, empty stderr and exited PID were checked afterward. The later
read-only process observation found all 763 receipts terminal, an empty
registry and no other matching checkout/recorded worker. Sequential `/proc`
and detached-process attribution limitations remain those of the observer.

The two artifact passes used one CPU and a 4 GB limit, taking 3.832 and
3.781 seconds. The resource pass used one CPU and a 2 GB limit and took
0.169 seconds. No mathematical suite was rerun for this checkpoint.

## Records

- [Corrected artifact inventory](../research/audits/artifact-integrity-v7.json).
- [Initial inventory with the path-resolution findings](../research/audits/artifact-integrity-v6.json).
- [Resource inventory](../research/audits/resource-process-v4.json).
- [Subsequent actual process observation](../research/audits/checkpoint-0832-process-closure-v1.json).
- [Checkpoint bindings](../research/audits/checkpoint-0832-manifest-v1.json).

The final deadline still requires a frozen scope, final report and separate
closure/deliverable audit. This checkpoint neither ends nor extends the run.
