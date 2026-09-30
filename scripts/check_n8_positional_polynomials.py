#!/usr/bin/env python3
"""Check the rational polynomial interface and its exact analytic prerequisites."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--snapshot', type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
project = root / 'scratch/S5-Achxy-k-5-38'
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
    cwd=project / '.lake/packages/mathlib', text=True).strip()
assert revision == 'f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
components = [
    'research/certificates/N8-polynomial-bridge-lean/Bridge.lean',
    'research/certificates/N8-energy-lean/Energy.lean',
    'research/certificates/N8-analytic-assembly/Assembly.lean',
    'research/certificates/N8-positional-polynomials/Polynomial.lean',
]
imports, bodies, records = [], [], []
for path in components:
    raw = (root / path).read_bytes()
    records.append({'path': path, 'sha256': hashlib.sha256(raw).hexdigest()})
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
with snapshot.open('xb') as stream:
    stream.write(combined)
subprocess.run(['lean', '--version'], check=True)
command = ['lake', 'env', 'lean', '--trust=0', '--stdin']
print(json.dumps({'components': records, 'snapshot': str(snapshot),
    'snapshot_sha256': hashlib.sha256(combined).hexdigest(), 'command': command,
    'mathlib_revision': revision,
    'scope': 'All finite dimensions: rational positional polynomial identities imply coefficient constancy. Free-Lie projection and the full N8 decision algorithm remain outside.'}), flush=True)
subprocess.run(command, cwd=project, input=combined, check=True)
