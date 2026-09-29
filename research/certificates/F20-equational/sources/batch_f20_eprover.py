#!/usr/bin/env python3
"""Bounded E attempts, each with its own recorded runner/resource reservation."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument("--prefix", required=True)
p.add_argument("--workers", type=int, default=4)
p.add_argument("--seconds", type=int, default=60)
p.add_argument("--schedule", action="store_true")
p.add_argument("--output", type=Path, required=True)
p.add_argument("files", nargs="+")
args = p.parse_args()
assert 1 <= args.workers <= 8 and 0 < args.seconds <= 600
assert not args.output.exists()


def attempt(item):
    index, filename = item
    name = f"{args.prefix}-{index:02d}"
    cmd = ["python3", "scripts/run_recorded.py", "--name", name,
           "--cores", "1", "--memory-gb", "3", "--timeout", str(args.seconds + 20),
           "--expect", "Proof found!", "--", "large-artifacts/tools/eprover/PROVER/eprover",
           "--auto-schedule" if args.schedule else "--auto", "--silent", "--proof-object=3",
           f"--cpu-limit={args.seconds}", "--memory-limit=2048", filename]
    done = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    process = ROOT / "results" / name / "process.json"
    result = {"name": name, "input": filename, "runner_returncode": done.returncode}
    if process.exists():
        data = json.loads(process.read_text())
        result.update({key: data[key] for key in ("actual_returncode", "process_ok", "elapsed_seconds", "timed_out")})
    else:
        result["launch_failure"] = {"stdout": done.stdout, "stderr": done.stderr}
    print(json.dumps(result), flush=True)
    return result


with ThreadPoolExecutor(max_workers=args.workers) as pool:
    results = list(pool.map(attempt, enumerate(args.files, 1)))
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(results, indent=2) + "\n")
print("DONE F20 bounded ATP batch; failed searches do not establish nontriviality", flush=True)
