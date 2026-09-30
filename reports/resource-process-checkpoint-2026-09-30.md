# Interim resource and process checkpoint

30 September 2026, approximately 03:21--03:24 UTC. The experiment remains
active until **10:04:49.670358 UTC**. This checkpoint neither closes the
research window nor extends it.

The corrected inventory examines 660 immediate `results/*/process.json`
receipts, including its own then-running job. After its completion, the
separate actual-process observation found all 660 receipts terminal, an
empty registry and no remaining recorded job PID/group or other process
with its working directory in this checkout. The observer and its
ancestors were explicitly identified and excluded from research workers.

## Recorded limits and outcomes

| Observation | Value |
| --- | --- |
| Peak simultaneous reserved CPU slots | 8 |
| Peak sum of requested per-process memory limits | 52 decimal GB |
| Peak simultaneous recorded jobs | 7 |
| CPU-slot overlaps in recorded intervals | 0 |
| Recorded reservation sums above 20 CPUs or 100 GB | 0 |
| Basic receipt/timestamp/success-flag inconsistencies | 0 |
| Terminal receipts after this audit completed | 660 |
| Recorded process successes | 481 |
| Recorded process nonsuccesses | 179 |
| Receipts marked timed out | 46 |
| Receipts marked interrupted | 24 |

Success here means the runner's return-code, timeout/interruption and
expected-marker condition. It is not a count of mathematical checks,
correct proofs or solved problems. Administrative jobs are included.
Timeout and interruption flags are reported separately, not added to the
nonsuccess count as if they were disjoint additional jobs.

The eight-slot peak occurred during `s5-lean-cache-setup-v1` on
29 September at 03:27:41 UTC. The 52 GB peak occurred among five N8 jobs
on 28 September at 16:54:01 UTC. The seven-job peak occurred during the
N8 three-exception GAP checks on 29 September at 15:52:22 UTC. The exact
job names, timestamps, CPU sets and limits are in the inventory.

These numbers reconstruct **reservations**, not measured CPU time or
aggregate peak memory. The runner sets affinity and per-process virtual-
address-space limits; it does not continuously measure tree-wide RSS or
enforce a cgroup memory cap. Receipt intervals also end just before the
wrapper releases its cooperative reservation. Unrecorded shell commands,
downloads, external tools and agent inference are outside this accounting.

## Actual process observation

The corrected inventory's /proc census found only its supervisor and
audit process. After both had finished,
[resource-process-closure-v1.json](../research/audits/resource-process-closure-v1.json)
bound all 660 terminal receipts and observed no other matching processes.
The check inspected process IDs and groups, not only `state/jobs.json`.

The census is sequential rather than atomic. PID reuse can conservatively
flag an unrelated process; descendants that detach and change both group
and working directory can evade this attribution. No process was killed
by either audit. The observations do not assert that later research jobs
will not be launched before the deadline.

## Retained attempts and reproduction

Both recorded accounting jobs used one CPU, 2 GB per-process memory and a
60-second timeout. They completed in 0.171 and 0.168 seconds with empty
stderr. The first census skipped a process if its working directory could
not be read; the corrected version still records matching PIDs/groups in
that case. This did not change the reservation peaks or reveal additional
workers. Both exact source versions and outputs are retained.

- [Corrected inventory](../research/audits/resource-process-inventory-v2.json).
- [First inventory](../research/audits/resource-process-inventory-v1.json).
- [Accounting script](../scripts/audit_resource_process_records.py).
- [Read-only closure observer](../scripts/inspect_recorded_process_closure.py).
- [File manifest](../research/audits/resource-process-manifest-v1.json).

Before the deadline, a fresh recorded inventory can be made with:

```sh
python3 scripts/run_recorded.py --name resource-process-NEW \
  --cores 1 --memory-gb 2 --timeout 60 \
  --expect 'COMPLETE resource/process inventory; inspect findings' -- \
  python3 scripts/audit_resource_process_records.py \
  --output research/audits/resource-process-NEW.json \
  --self-job resource-process-NEW
```

Its completion marker means the inventory finished, not that its findings
are clean. The separate closure observer starts no research job and may
also be used after the deadline, without resetting the experiment:

```sh
python3 scripts/inspect_recorded_process_closure.py \
  --output research/audits/process-closure-NEW.json
```

Use fresh output paths and inspect all findings. The actual deadline
snapshot, final report and final process observation remain outstanding.
