#!/usr/bin/env python3
"""Compile the paper and record the actual invocation and input/output hashes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

PAPER = Path(__file__).resolve().parents[1]


def binding(path):
    data = path.read_bytes()
    return {"path": path.relative_to(PAPER).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tectonic", default=os.environ.get("PAPER_TECTONIC", "tectonic"))
    parser.add_argument("--only-cached", action="store_true")
    args = parser.parse_args()
    executable = shutil.which(args.tectonic)
    if not executable:
        parser.error("Tectonic not found; use --tectonic /path/to/tectonic or PAPER_TECTONIC")
    started = now()
    attempt = PAPER / "build" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    attempt.mkdir(parents=True)
    inputs = [PAPER / "main.tex", PAPER / "preamble.tex", PAPER / "references.bib"]
    inputs += sorted((PAPER / "sections").glob("*.tex"))
    inputs += sorted((PAPER / "appendices").glob("*.tex"))
    # Tectonic may read the retained bibliography before regenerating it.
    if (PAPER / "main.bbl").exists():
        inputs.append(PAPER / "main.bbl")
    receipt = {"started_utc": started, "inputs": [binding(p) for p in inputs],
               "tool": subprocess.check_output([executable, "--version"], text=True).strip(),
               "purpose": "Post-deadline manuscript build; no mathematical research job."}
    command = [executable, "--keep-logs", "--keep-intermediates",
               "--outdir", str(attempt.relative_to(PAPER)), "main.tex"]
    if args.only_cached:
        command.insert(1, "--only-cached")
    receipt["command"] = command
    result = subprocess.run(command, cwd=PAPER, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    (attempt / "console.txt").write_text(result.stdout)
    receipt.update({"finished_utc": now(), "returncode": result.returncode,
                    "console": binding(attempt / "console.txt")})
    if result.returncode == 0:
        shutil.copy2(attempt / "main.pdf", PAPER / "gworld-experiment.pdf")
        shutil.copy2(attempt / "main.bbl", PAPER / "main.bbl")
        receipt["outputs"] = [binding(PAPER / name) for name in
                              ("gworld-experiment.pdf", "main.bbl")]
        receipt["tex_log"] = binding(attempt / "main.log")
    (attempt / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if result.returncode == 0:
        (PAPER / "data").mkdir(exist_ok=True)
        (PAPER / "data/build-manifest.json").write_text(json.dumps(receipt, indent=2) + "\n")
        shutil.copy2(attempt / "main.log", PAPER / "data/build-log.txt")
        shutil.copy2(attempt / "console.txt", PAPER / "data/build-console.txt")
    print(json.dumps({"returncode": result.returncode, "attempt": str(attempt),
                      "pdf": str(PAPER / "gworld-experiment.pdf") if result.returncode == 0 else None}))
    if result.returncode:
        print(result.stdout[-8000:], file=sys.stderr)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
