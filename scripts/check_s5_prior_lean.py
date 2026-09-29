#!/usr/bin/env python3
"""Build and audit an unchanged, pinned external S5 proof; no new claim."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'scratch/S5-Achxy-k-5-38'
ARCHIVE = ROOT / 'literature/code/S5-Achxy-k-5-38'


def run(args, **kwargs):
    print('COMMAND', json.dumps(args), flush=True)
    return subprocess.run(args, cwd=PROJECT, check=True, **kwargs)


def main():
    metadata = json.loads((ARCHIVE / 'provenance.json').read_text())
    actual = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=PROJECT, text=True).strip()
    assert actual == metadata['revision'] == '4330f0513173258259f0585d1c1b8a624fda59d2'
    for item in metadata['files']:
        raw = (PROJECT / item['path']).read_bytes()
        assert raw == (ARCHIVE / 'source' / item['path']).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item['sha256']
    manifest = json.loads((PROJECT / 'lake-manifest.json').read_text())
    for package in manifest['packages']:
        path = PROJECT / manifest['packagesDir'] / package['name']
        revision = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=path, text=True).strip()
        assert revision == package['rev'], (package['name'], revision)
    print('PASS: all 35 external source files and 9 dependency revisions match pins', flush=True)
    run(['lean', '--version'])
    run(['bash', 'scripts/check.sh'])
    # Retain the explicit --trust=0 setting. Do not infer from that flag
    # that every cached dependency was rebuilt or independently rechecked:
    # the pinned Lean importer directly installs imported constant maps.
    # The project itself was compiled above; dependency caches are trusted
    # parts of this standard Lean/Mathlib verification environment.
    statement = ROOT / 'research/certificates/S5-prior-lean/StatementCheck.lean'
    with statement.open('rb') as stream:
        run(['lake', 'env', 'lean', '--trust=0', '--stdin'], stdin=stream)
    print('PASS: pinned S5 prior proof build, author audit, completion, and trust-zero restatement', flush=True)


if __name__ == '__main__':
    main()
