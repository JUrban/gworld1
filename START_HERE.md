# Starting the experiment

**The experiment has now started.** The clock is in `state/session.json`; do not restart it. The procedure below is retained as the launch protocol. When resuming, read the current state, research log, and progress report, then continue within the existing deadline.

On that instruction:

1. Work in this repository, not the enclosing Kourovka repository. Read `AGENTS.md`, `docs/PROTOCOL.md`, `docs/STATUS_NOTES.md`, and `docs/KOUROVKA_LESSONS.md`.
2. Record any user overrides in `config/run.json`. The defaults are 48 hours, 20 CPU cores and 100 decimal GB RAM. Check the local tool paths and run the readiness check. Commit any final preparation changes locally.
3. Start the clock once, quoting the actual launch instruction and recording the model configuration. Do not fabricate authorization from this template:

   ```sh
   python3 scripts/session.py start --confirm-start \
     --authorization 'ACTUAL USER INSTRUCTION TO START' \
     --model 'MODEL AND REASONING CONFIGURATION AT LAUNCH'
   ```

4. Commit the initialized `state/session.json`. The deadline is exactly 48 hours after launch, and includes status research, solving, checking and reporting. Never reset the clock after an interruption.
5. Begin the run with source/scope checks and targeted literature checks, using `data/CATALOG.md` and `research/triage.csv`. The site is historical, not a current open-problem oracle. Select a portfolio only now.
6. Keep the research log and claims ledger current, retain failed checks, and commit useful progress locally. Read `session.py status` when resuming. Reserve the last hours for verification and reporting; stop discovery at the deadline.

A bounded computation during the active run can be recorded as follows (the script must already exist):

```sh
python3 scripts/run_recorded.py --name F-example-001 \
  --cores 1 --memory-gb 8 --timeout 600 --expect PASS \
  -- bin/gap scripts/YOUR_SCRIPT.g
```

This creates a new result directory with command arguments, timestamps, actual exit status, stdout/stderr, hashes, timeout status and optional output-marker check. It never overwrites an old job. A successful process is not a verified mathematical result.

CPU allocations and requested memory reservations are shared among concurrent invocations of this wrapper. CPU affinity and per-process address-space limits are enforced on Linux. **The memory reservation is not an aggregate operating-system limit on a process tree**, and commands run outside the wrapper are not included in its accounting. Monitor total use; use a cgroup if a hard aggregate memory cap is needed. A launcher killed with SIGKILL may leave children requiring manual cleanup before slots are reused.

No subagents are authorized by this setup. Independent computational jobs within the resource budget are allowed. Do not push or send messages to authors without user authorization.
