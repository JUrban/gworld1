#!/usr/bin/env python3
"""Read-only environment and reachable-Git-blob inventory for the handoff."""
import argparse
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Use a fresh output path.')
    root = Path(__file__).resolve().parents[1]

    def git(*parts):
        return subprocess.check_output(['git', *parts], cwd=root)

    objects = git('rev-list', '--objects', '--all')
    checked = subprocess.run(
        ['git', 'cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize) %(rest)'],
        cwd=root, input=objects, stdout=subprocess.PIPE, check=True).stdout
    blobs = []
    for line in checked.decode().splitlines():
        oid, kind, size, *rest = line.split(' ', 3)
        if kind == 'blob':
            blobs.append(dict(oid=oid, bytes=int(size), example_path=rest[0] if rest else None))
    assert len({r['oid'] for r in blobs}) == len(blobs)
    limit = json.loads((root/'config/run.json').read_text())['large_blob_threshold_bytes']
    tools = {}
    for name in ['python3', 'gap', 'uv', 'pdftotext', 'git']:
        found = shutil.which(name)
        tools[name] = dict(path=found, resolved=str(Path(found).resolve()) if found else None)
        if found:
            raw = Path(found).read_bytes()
            tools[name].update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    report = dict(
        created_utc=datetime.now(timezone.utc).isoformat(),
        scope='Environment metadata and reachable Git object sizes; no mathematical computation or software installation.',
        head=git('rev-parse', 'HEAD').decode().strip(),
        python=dict(version=sys.version, executable=sys.executable, platform=platform.platform()),
        python_packages=sorted([dict(name=d.metadata['Name'], version=d.version)
                                for d in metadata.distributions()], key=lambda x:x['name'].lower()),
        tools=tools,
        git=dict(version=git('--version').decode().strip(),
                 refs=git('show-ref').decode().splitlines(),
                 remotes=git('remote', '-v').decode().splitlines(),
                 object_inventory_sha256=hashlib.sha256(checked).hexdigest(),
                 reachable_objects=len(checked.splitlines()), reachable_blobs=len(blobs),
                 total_uncompressed_blob_bytes=sum(r['bytes'] for r in blobs),
                 blob_limit_bytes=limit,
                 blobs_at_or_above_limit=[r for r in blobs if r['bytes'] >= limit],
                 largest_blobs=sorted(blobs, key=lambda r:r['bytes'], reverse=True)[:20]),
        limits=['Git inventory covers objects reachable from current refs, not ignored outputs or dangling objects.',
                'Tool paths describe this machine; binaries and installed packages are not included by this inventory.',
                'Installed version metadata is not an independent software supply-chain verification.'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(dict(reachable_blobs=len(blobs), largest_blob_bytes=max(r['bytes'] for r in blobs),
                          oversize=len(report['git']['blobs_at_or_above_limit']))))
    assert not report['git']['blobs_at_or_above_limit'], 'Reachable blob violates the repository limit'
    print('PASS review portability inventory')


if __name__ == '__main__':
    main()
