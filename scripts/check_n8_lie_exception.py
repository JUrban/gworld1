#!/usr/bin/env python3
"""Check the generated Lie exception and unchanged N8 word prerequisites."""
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
version = subprocess.check_output(['lean', '--version'], text=True).strip()
assert 'version 4.24.0' in version and '797c613eb9b6d4ec95db23e3e00af9ac6657f24b' in version
components = [
    'research/certificates/N8-polynomial-bridge-lean/Bridge.lean',
    'research/certificates/N8-energy-lean/Energy.lean',
    'research/certificates/N8-analytic-assembly/Assembly.lean',
    'research/certificates/N8-positional-polynomials/Polynomial.lean',
    'research/certificates/N8-word-dictionary/Words.lean',
    'research/certificates/N8-lie-exception/Lie.lean',
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
component_snapshot = snapshot.with_name(snapshot.stem + '-Lie.lean')
with component_snapshot.open('xb') as stream:
    stream.write((root / components[-1]).read_bytes())
command = ['lake', 'env', 'lean', '--trust=0', '--stdin']
print(json.dumps({'lean_version': version, 'components': records, 'snapshot': str(snapshot),
    'snapshot_sha256': hashlib.sha256(combined).hexdigest(), 'command': command,
    'mathlib_revision': revision,
    'scope': 'Generated Lie-subalgebra scalar-power exclusion and positional separation; abstract free-Lie embedding, projections and full N8 algorithm outside.'}), flush=True)
subprocess.run(command, cwd=project, input=combined, check=True)
