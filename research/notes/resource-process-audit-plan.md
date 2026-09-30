# Recorded resource and process audit

30 September 2026, during the closing phase. This is administrative
accounting, not a mathematical check or the final deadline observation.

Read the immediate `results/*/process.json` receipts. Reconstruct interval
overlaps using their recorded UTC start/end times, CPU sets and requested
per-process address-space limits. Distinguish reservations from measured
usage: these receipts do not provide aggregate RSS or consumed CPU time.
Check time-window and basic receipt consistency without rerunning solvers.

Inspect actual /proc state for processes in this checkout and process
groups named by recorded job PIDs. The audit itself is necessarily alive;
retain that observation and inspect its terminal receipt afterward.
No process is killed by this audit. The final deadline still requires
its own observation and closure, even if this interim audit is clean.

Keep all observed issues, source receipt hashes, and the exact script.
Do not infer continuous enforcement for unrecorded commands, detached
processes, external tools, downloads or agent inference from this report.
