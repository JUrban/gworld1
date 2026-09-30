#!/usr/bin/env python3
"""Make and compile a self-contained source archive using Tectonic."""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

PAPER = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tectonic", default=os.environ.get("PAPER_TECTONIC", "tectonic"))
    parser.add_argument("--only-cached", action="store_true")
    args = parser.parse_args()
    executable = shutil.which(args.tectonic)
    if not executable:
        parser.error("Tectonic not found; pass --tectonic /path/to/tectonic")
    paths = [PAPER / p for p in ("main.tex", "preamble.tex", "references.bib", "main.bbl")]
    paths += sorted((PAPER / "sections").glob("*.tex"))
    paths += sorted((PAPER / "appendices").glob("*.tex"))
    members = {p.relative_to(PAPER).as_posix(): p.read_bytes() for p in paths}
    members["README.txt"] = b"""Forty-eight hours with GroupWorld
Version 1, 30 September 2026
Codex gpt-6-astra, Michael Kinyon, Josef Urban and Vladimir Shpilrain

Compile here with: tectonic main.tex
Or use pdflatex main.tex; bibtex main; pdflatex main.tex; pdflatex main.tex.
All TeX inputs and a generated bibliography are included. Standard LaTeX
packages and fonts are required; no research software or data is needed.
The full repository, PDF, build receipts and editorial checks are at
https://github.com/JUrban/gworld1/tree/main/paper

This is a candidate account awaiting independent mathematical and novelty
review. Its research evidence links are pinned to the unchanged handoff
commit 0d6b855fd6d9d9e5ddb5dbd186a2a590164c1341.
"""
    archive = PAPER / "gworld-experiment-source.tar.gz"
    with archive.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as tar:
                for name, data in sorted(members.items()):
                    info = tarfile.TarInfo("gworld-experiment/" + name)
                    info.size, info.mode, info.mtime = len(data), 0o644, 0
                    tar.addfile(info, io.BytesIO(data))
    started = datetime.now(timezone.utc)
    attempt = PAPER / "build" / ("package-" + started.strftime("%Y%m%dT%H%M%S.%fZ"))
    attempt.mkdir(parents=True)
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(attempt, filter="data")
    source = attempt / "gworld-experiment"
    extracted_match = all((source / name).read_bytes() == data for name, data in members.items())
    command = [executable, "--keep-logs", "main.tex"]
    if args.only_cached:
        command.insert(1, "--only-cached")
    result = subprocess.run(command, cwd=source, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    (attempt / "console.txt").write_text(result.stdout)
    text_equal = False
    if result.returncode == 0:
        def pdf_text(path):
            return subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
        text_equal = pdf_text(source / "main.pdf") == pdf_text(PAPER / "gworld-experiment.pdf")
    receipt = {"started_utc": started.isoformat(),
               "finished_utc": datetime.now(timezone.utc).isoformat(),
               "scope": "Standalone source compilation; not mathematical reproduction.",
               "archive": {"path": archive.name, "bytes": archive.stat().st_size,
                           "sha256": sha(archive.read_bytes())},
               "members": [{"path": n, "bytes": len(b), "sha256": sha(b)}
                           for n, b in sorted(members.items())],
               "extracted_bytes_match": extracted_match, "command": command,
               "tool": subprocess.check_output([executable, "--version"], text=True).strip(),
               "returncode": result.returncode, "pdf_text_identical": text_equal,
               "published_pdf_sha256": sha((PAPER / "gworld-experiment.pdf").read_bytes()),
               "attempt": attempt.relative_to(PAPER).as_posix(),
               "passed": extracted_match and result.returncode == 0 and text_equal}
    if result.returncode == 0:
        receipt["extracted_pdf_sha256"] = sha((source / "main.pdf").read_bytes())
    (PAPER / "data/source-archive-manifest.json").write_text(json.dumps(receipt, indent=2) + "\n")
    shutil.copy2(attempt / "console.txt", PAPER / "data/source-archive-console.txt")
    print(json.dumps({key: receipt[key] for key in
                      ("passed", "returncode", "pdf_text_identical", "archive")}, indent=2))
    if result.returncode:
        print(result.stdout[-8000:], file=sys.stderr)
    return not receipt["passed"]


if __name__ == "__main__":
    sys.exit(main())
