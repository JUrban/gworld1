#!/usr/bin/env python3
"""Check exact prior analytic sources and their new cyclic-coordinate assembly."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

args_parser = argparse.ArgumentParser()
args_parser.add_argument('--snapshot', required=True, type=Path)
args = args_parser.parse_args()
root = Path(__file__).resolve().parents[1]
project = root / 'scratch/S5-Achxy-k-5-38'
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
    cwd=project / '.lake/packages/mathlib', text=True).strip()
assert revision == 'f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
components = [
    root / 'research/certificates/N8-polynomial-bridge-lean/Bridge.lean',
    root / 'research/certificates/N8-energy-lean/Energy.lean',
    root / 'research/certificates/N8-analytic-assembly/Assembly.lean',
]
imports, bodies, records = [], [], []
for path in components:
    raw = path.read_bytes()
    records.append({'path': str(path.relative_to(root)),
                    'sha256': hashlib.sha256(raw).hexdigest()})
    body = []
    for line in raw.decode().splitlines():
        if line.startswith('import '):
            if line not in imports:
                imports.append(line)
        else:
            body.append(line)
    bodies.append('\n'.join(body))
combined = ('\n'.join(imports) + '\n\n' + '\n\n'.join(bodies) + '\n').encode()
snapshot = args.snapshot if args.snapshot.is_absolute() else root / args.snapshot
snapshot.parent.mkdir(parents=True, exist_ok=True)
with snapshot.open('xb') as f:
    f.write(combined)
subprocess.run(['lean', '--version'], check=True)
command = ['lake', 'env', 'lean', '--trust=0', '--stdin']
print(json.dumps({'components': records, 'snapshot': str(snapshot),
    'snapshot_sha256': hashlib.sha256(combined).hexdigest(), 'command': command,
    'mathlib_revision': revision,
    'scope': 'Full continuous-function implication from positional delta/diagonal identities to constancy. Free-associative/Lie encoding and full N8 algorithm remain outside.'}), flush=True)
subprocess.run(command, cwd=project, input=combined, check=True)
