# Artifact checkpoint, 30 September 2026

This is the first closing integrity inventory, completed at approximately
01:55 UTC. It checks stored bytes and process records, not mathematical
correctness or novelty. The experiment remains active until 10:04:49 UTC.

The [corrected inventory](../research/audits/artifact-inventory-v2.json)
reads 124 certificate manifests and the two source manifests. It checks
5,708 historical hash bindings: 5,676 match their current paths and 32
refer to changed versions. There are no missing files, no JSON parse
errors and no unrecognized manifest shapes. It hashes 4,460 distinct
files totaling 384,828,148 bytes, including process output logs.

All 32 changed bindings are accounted for by 25 distinct historical file
versions. Each was recovered from the local Git history, checked against
the original SHA-256, and copied into a separate content-addressed archive.
The [recovery index](../research/audits/historical-artifact-recovery-v1.json)
records original path, historical commit, content hash, size and archived
path. The original manifests and current proofs/scripts were not edited.
Thus the original bound content remains reviewable without pretending
that an old manifest certifies a later version. Mathematical review of
changes to arguments is a separate closing task.

Ninety-one bound paths are intentionally outside the tracked working
files: 88 files from the reproduced A5 prior-result dependency under
`scratch/`, and three B9 tool binaries under `large-artifacts/`. All match
their recorded hashes locally. The 88 A5 files also match individual
members of the retained, tracked publisher source archive, verified
without extracting or executing them; see the
[archive comparison](../research/audits/A5-dependency-archive-check-v1.json).
The three B9 binaries remain omitted from Git, as their original manifests
already state. Their build/source records must accompany reproduction;
this checkpoint does not describe these binaries as published artifacts.

All four frozen launch inputs match their start-of-run hashes. The process
inventory found no historical log-hash mismatch or inconsistent recorded
success flag. Its only nonterminal receipt was its own then-running audit
job. That job subsequently finished normally with empty stderr; its
[terminal receipt](../results/closing-artifact-inventory-v2/process.json)
is retained, and the job registry was empty afterward. Failed and timed-out
research jobs remain recorded as such; a terminal failure is not a missing
receipt or a successful mathematical check.

The [first inventory](../research/audits/artifact-inventory-v1.json)
incorrectly reported five missing paths because its resolver treated two
A5 project-relative script paths as repository-relative and three ignored
binary paths as manifest-relative. The corrected resolver uses the
declared project root and recognizes `large-artifacts/`. Both observations
and the first script version are retained. Each audit job used one CPU and
an 8 GB reservation and completed in about 1.88 seconds. The completion
marker explicitly means that the inventory finished, not that a theorem
was verified.

The next steps are in the [closing audit plan](CLOSING_AUDIT_PLAN.md).
No final report, deadline snapshot, comprehensive proof reread or completed
novelty assessment is claimed by this checkpoint.
