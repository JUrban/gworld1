#!/usr/bin/env python3
"""Read-only process closure observation; launches or kills no research job.

Usable after the immutable research deadline. The observer and its ancestors
are identified explicitly, rather than mistaken for still-running solvers.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_stat(pid):
    raw = Path(f'/proc/{pid}/stat').read_text()
    end = raw.rfind(')')
    fields = raw[end+2:].split()
    return {'pid': pid, 'comm': raw[raw.find('(')+1:end], 'state': fields[0],
            'ppid': int(fields[1]), 'process_group': int(fields[2]),
            'session': int(fields[3]), 'start_ticks_since_boot': int(fields[19])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Use a new output path; preserve previous observations.')
    started = datetime.now(timezone.utc).isoformat()
    ancestors, pid = [], os.getpid()
    while pid and pid not in ancestors:
        ancestors.append(pid)
        pid = read_stat(pid)['ppid']
    receipts, recorded, unfinished, parse_errors = [], {}, [], []
    for path in sorted((ROOT/'results').glob('*/process.json')):
        raw = path.read_bytes()
        try:
            item = json.loads(raw)
        except Exception as error:
            parse_errors.append({'path': str(path.relative_to(ROOT)), 'error': str(error)})
            continue
        receipts.append({'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(raw).hexdigest()})
        if item.get('pid'):
            recorded.setdefault(item['pid'], []).append(path.parent.name)
        if item.get('actual_returncode') is None or not item.get('ended_utc'):
            unfinished.append(path.parent.name)
    found, inaccessible = [], []
    for path in sorted(Path('/proc').iterdir()):
        if not path.name.isdigit():
            continue
        try:
            item = read_stat(int(path.name))
        except FileNotFoundError:
            continue
        except PermissionError:
            inaccessible.append(int(path.name))
            continue
        try:
            cwd = Path(os.readlink(path/'cwd'))
        except (FileNotFoundError, PermissionError):
            cwd = None
        here = cwd is not None and (cwd == ROOT or ROOT in cwd.parents)
        associated = recorded.get(item['pid'], []) + recorded.get(item['process_group'], [])
        if here or associated:
            item.update(cwd=str(cwd) if cwd else None, cwd_in_checkout=here,
                        recorded_job_names=sorted(set(associated)),
                        observer_or_ancestor=item['pid'] in ancestors)
            found.append(item)
    registry = json.loads((ROOT/'state/jobs.json').read_text())
    others = [p for p in found if not p['observer_or_ancestor']]
    closed = not (unfinished or parse_errors or registry or others or inaccessible)
    report = {'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Read-only observation of recorded job PIDs/groups and checkout CWDs; no process stopped by this script.',
              'observer_pid_and_ancestors': ancestors, 'receipt_bindings': receipts,
              'unfinished_receipts': unfinished, 'receipt_parse_errors': parse_errors,
              'jobs_registry': registry, 'matching_processes': found,
              'other_matching_processes': others, 'inaccessible_stat_pids': inaccessible,
              'all_recorded_jobs_closed_in_observed_scope': closed,
              'limitations': ['Sequential /proc reads are not atomic.',
                  'PID/group reuse can conservatively flag an unrelated process.',
                  'Detached descendants changing both process group and CWD can evade attribution.',
                  'This observation does not prohibit later launches before the deadline.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps({'receipts': len(receipts), 'unfinished': unfinished,
        'registry': registry, 'other_matching_processes': others,
        'closed_in_observed_scope': closed}, indent=2))
    return 0 if closed else 1


if __name__ == '__main__':
    raise SystemExit(main())
