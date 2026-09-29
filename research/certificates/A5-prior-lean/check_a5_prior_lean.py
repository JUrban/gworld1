#!/usr/bin/env python3
"""Verify the archived external A5 development and independently restate its scope."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / 'research/certificates/A5-prior-lean'


def main():
    meta = json.loads((CERT / 'source-manifest.json').read_text())
    project = ROOT / meta['project_path']
    assert hashlib.sha256((ROOT / meta['archive']).read_bytes()).hexdigest() == meta['archive_sha256']
    for row in meta['files']:
        data = (project / row['path']).read_bytes()
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
    for line in (project / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(None, 1)
        assert hashlib.sha256((project / name.strip()).read_bytes()).hexdigest() == digest, name
    manifest = json.loads((project / 'lake-manifest.json').read_text())
    for package in manifest['packages']:
        path = project / manifest['packagesDir'] / package['name']
        rev = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=path, text=True).strip()
        assert rev == package['rev'], (package['name'], rev)
    print(f"PASS: {len(meta['files'])} archived sources, author checksums, and nine dependency pins", flush=True)

    def run(command, **kw):
        print('COMMAND', json.dumps(command), flush=True)
        subprocess.run(command, cwd=project, check=True, **kw)

    run(['lean', '--version'])
    run(['bash', 'scripts/check.sh'])
    # Uses the previously checked pinned Lean release and trusted Mathlib caches.
    # --trust=0 does not recheck all imported cached proofs; no such claim is made.
    with (CERT / 'StatementCheck.lean').open('rb') as stream:
        run(['lake', 'env', 'lean', '--trust=0', '--stdin'], stdin=stream)
    print('PASS: pinned A5 prior proof build, author audit, and independent scope check', flush=True)


if __name__ == '__main__':
    main()
