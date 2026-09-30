#!/usr/bin/env python3
"""Check the shared finite-dimensional lemma, not either full group algorithm."""
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
project = root / 'scratch/S5-Achxy-k-5-38'
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
    cwd=project / '.lake/packages/mathlib', text=True).strip()
assert revision == 'f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
subprocess.run(['lean', '--version'], check=True)
source = root / 'research/certificates/F34-F38-span-lean/Span.lean'
command = ['lake', 'env', 'lean', '--trust=0', '--stdin']
print(json.dumps({'source': str(source), 'command': command,
    'mathlib_revision': revision,
    'scope': 'Universal span, path and finite-dimension arguments. No concrete monomial lift, equation-to-EDT0L construction or full free-group decision algorithm.'}), flush=True)
with source.open('rb') as stream:
    subprocess.run(command, cwd=project, stdin=stream, check=True)
