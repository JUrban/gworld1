# Evidence checkpoint after the shear-tail refinement

30 September 2026, 09:23--09:27 UTC. The experiment remains active until
10:04:49.670358 UTC. This is an interim integrity and process checkpoint,
not the deadline snapshot or a mathematical correctness certificate.

Since the 08:30 checkpoint, the run added G9's finite Steiner connections
and disjoint Nielsen-shear tails, explicit prior credit for the support
connection construction, and N8's higher-weight positive and full-negative
integration controls. The current G9 enclosure is
2.676891785 <= lambda_2 <= 2.943737759. Counts remain ten whole-entry
coverage candidates, two partial-entry candidates and zero established
novel results.

## Retained artifacts

| Observation | Count |
| --- | ---: |
| Selected manifests, scope ledgers and process-closure records | 202 |
| Hash bindings examined | 26,533 |
| Current-path matches | 26,370 |
| Exact historical matches | 163 |
| Missing or mismatched unresolved bindings | 0 |
| Distinct indexed historical file versions checked | 152 |
| Distinct files hashed | 5,787 |
| Bytes hashed across those files | 558,678,803 |
| Parse, recovery or unrecognized-manifest errors | 0 |
| Frozen launch-input hashes matching | 4 of 4 |

The same 91 intentionally untracked bound paths retain matching bytes:
88 A5 dependency sources and three B9 compiled binaries, with the archive
and build records described in the [reproduction guide](REPRODUCTION_GUIDE.md).
The auditor checks selected declared bindings; it does not assert that
every repository file is individually bound. Multiple records can bind
the same file. All 152 indexed historical versions have distinct original
path/hash pairs and distinct hashes at this observation.

## Recorded processes and reservations

After both audits finish, all **782** receipts are terminal: **586** process
successes and **196** nonsuccesses. The latter include 46 timeout flags
and 24 interruption flags. These totals include administrative jobs and
intentional or exploratory failures, not just mathematical checks.

No recorded interval exceeds the agreed reservation budget, overlaps a
CPU slot, lies outside the original window, or has inconsistent status.
Historical peaks are eight reserved CPUs, 52 decimal GB in the sum of
requested per-process address-space limits, and seven simultaneous jobs.
These are not continuously measured peak RAM or consumed CPU time.
Unrecorded administrative commands, network tools and model inference are
outside this receipt accounting.

Each audit observes its own unfinished receipt. Both final receipts,
stdout/stderr hashes, empty stderr and exited PIDs were checked afterward.
The subsequent read-only `/proc` observation finds all 782 receipts
terminal, an empty registry and no remaining matching worker. The
observer's documented non-atomic and detached-process attribution limits
remain. This observation does not prohibit later launches before the
deadline.

The artifact audit takes 4.434 seconds at one CPU/4 GB and the resource
audit 0.168 seconds at one CPU/2 GB. No mathematical suite was repeated
for this checkpoint. A whitespace check on the preceding report commit
identified one extra terminal blank line in the draft; the closing edit
removes it after retaining the exact bound version.

## Records

- [Artifact inventory](../research/audits/artifact-integrity-v8.json).
- [Reservation/process inventory](../research/audits/resource-process-v5.json).
- [Actual terminal-process observation](../research/audits/checkpoint-0925-process-closure-v1.json).
- [Checkpoint bindings](../research/audits/checkpoint-0925-manifest-v1.json).
- [Earlier Git blob-size and environment inventory](../research/audits/review-portability-v1.json).

The deadline freeze, final report and final deliverable audit remain to be
completed. The original clock and mathematical scopes have not changed.
