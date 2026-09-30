#!/usr/bin/env python3
"""Check local Markdown destinations in current reviewer entry points."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Choose a fresh output path.')
    tracked = set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0'))
    scopes = json.loads((ROOT/'research/result-scopes.json').read_text())
    paths = {'README.md', 'reports/README.md', 'reports/CURRENT_RESULTS.md',
             'reports/FINAL_REPORT_DRAFT.md', 'reports/RESULT_SCOPE.md',
             'reports/REPRODUCTION_GUIDE.md', 'reports/CLOSING_AUDIT_PLAN.md'}
    if (ROOT/'reports/FINAL_REPORT.md').exists():
        paths.add('reports/FINAL_REPORT.md')
    for row in scopes['entries']:
        paths.add('problems/'+row['id']+'/README.md')
        paths.update(p for p in row['proofs']+row['audits'] if p.endswith('.md'))
    observations, sources = [], []
    for name in sorted(paths):
        source = ROOT/name
        raw = source.read_bytes()
        sources.append(dict(path=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()))
        text = raw.decode()
        for match in re.finditer(r'\]\(([^)\n]+)\)', text):
            target = match.group(1).strip()
            if target.startswith('<') and target.endswith('>'):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target_path = (source.parent/unquote(parsed.path)).resolve()
            try:
                relative = str(target_path.relative_to(ROOT))
            except ValueError:
                relative = None
            exists = target_path.exists()
            in_git = bool(relative is not None and
                          (relative in tracked or target_path.is_dir() and
                           any(p.startswith(relative+'/') for p in tracked)))
            status = 'tracked_destination' if exists and in_git else 'missing' if not exists else 'local_only'
            observations.append(dict(source=name, line=text.count('\n', 0, match.start())+1,
                                     target=target, resolved_path=relative or str(target_path),
                                     status=status))
    report = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                  scope='Inline local Markdown links in current counted proofs/audits and reviewer entry points, not historical documents or all code paths.',
                  sources=sources, destination_counts=dict(Counter(r['status'] for r in observations)),
                  links=observations, findings=[r for r in observations if r['status'] != 'tracked_destination'],
                  limitations=['URL targets and Markdown fragments are not fetched or checked.',
                               'Plain code-span paths, reference-style links and dynamically generated dependencies are outside this scan.',
                               'A tracked directory destination does not imply every file in that directory is tracked.'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(dict(sources=len(sources), destinations=report['destination_counts'], findings=report['findings']), indent=2))
    print('COMPLETE current review-link inventory; inspect findings')


if __name__ == '__main__':
    main()
