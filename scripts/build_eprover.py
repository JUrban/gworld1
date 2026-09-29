#!/usr/bin/env python3
"""Build the pinned upstream E checkout locally; do not install system-wide."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "large-artifacts/tools/eprover"
PIN = "3b7afc70fe77d3118bb95144c4735ca45f5f31cf"
actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=SOURCE, text=True).strip()
assert actual == PIN, (actual, PIN)
subprocess.run(["./configure"], cwd=SOURCE, check=True)
subprocess.run(["make", "-j4"], cwd=SOURCE, check=True)
binary = SOURCE / "PROVER/eprover"
version = subprocess.check_output([str(binary), "--version"], text=True).strip()
record = {
    "source_url": "https://github.com/eprover/eprover.git",
    "commit": actual,
    "build": ["./configure", "make -j4"],
    "version": version,
    "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
    "source_and_binary_in_git": False,
    "reproduce": "Clone the source URL, checkout the exact commit, run this script under the recorded runner with four CPU slots.",
}
out = ROOT / "research/certificates/F20-equational/eprover-build.json"
out.parent.mkdir(parents=True, exist_ok=True)
assert not out.exists(), out
out.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
print("PASS pinned E build")
