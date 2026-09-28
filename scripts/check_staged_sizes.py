#!/usr/bin/env python3
"""Keep newly staged blobs below the public-repository size threshold."""
import json
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
limit=json.loads((root/'config/run.json').read_text())['large_blob_threshold_bytes']
names=subprocess.check_output(['git','diff','--cached','--name-only','--diff-filter=ACM','-z'],cwd=root)
bad=[]
for name in names.split(b'\0'):
    if not name: continue
    size=int(subprocess.check_output([b'git',b'cat-file',b'-s',b':'+name],cwd=root))
    if size>=limit: bad.append((name.decode(errors='replace'),size))
for name,size in bad: print(f'{name}: {size} bytes reaches the {limit}-byte limit; use a compact artifact or documented external output.',file=sys.stderr)
sys.exit(bool(bad))
