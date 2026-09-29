#!/usr/bin/env python3
"""Compile the F28 all-exponent lemma using the existing pinned Mathlib workspace."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'scratch/S5-Achxy-k-5-38'
MATHLIB = PROJECT / '.lake/packages/mathlib'
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=MATHLIB, text=True).strip()
assert revision == 'f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
subprocess.run(['lean', '--version'], check=True)
source = ROOT / 'research/certificates/F28-matrix-lean/MatrixLemma.lean'
command = ['lake', 'env', 'lean', '--trust=0', '--stdin']
print(json.dumps({'source': str(source), 'command': command,
                  'mathlib_revision': revision, 'scope': 'No external S5 result imported'}), flush=True)
with source.open('rb') as stream:
    subprocess.run(command, cwd=PROJECT, stdin=stream, check=True)
