#!/usr/bin/env python3
"""Audit recorded reservations and live processes, not measured resource use."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def stamp(s):
    return datetime.fromisoformat(s)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--self-job', required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Use a fresh output path; earlier observations are immutable.')
    observed = datetime.now(timezone.utc)
    session = json.loads((ROOT / 'state/session.json').read_text())
    start, deadline = map(stamp, [session['started_utc'], session['deadline_utc']])
    cpu_limit = session['run_config']['cpu_cores']
    memory_limit = session['run_config']['memory_gb_decimal']
    jobs, issues, events = {}, [], []
    for path in sorted((ROOT / 'results').glob('*/process.json')):
        name = path.parent.name
        raw = path.read_bytes()
        try:
            record = json.loads(raw)
            begun = stamp(record['started_utc'])
            terminal = record.get('actual_returncode') is not None and bool(record.get('ended_utc'))
            ended = stamp(record['ended_utc']) if terminal else observed
            cpus = record['cpus']
            memory = record['memory_gb_per_process']
            if not isinstance(cpus, list) or not cpus or any(type(c) is not int for c in cpus):
                raise ValueError('CPU set malformed')
            if len(set(cpus)) != len(cpus) or len(cpus) > cpu_limit or memory <= 0 or memory > memory_limit:
                raise ValueError('Individual reservation outside budget')
        except Exception as error:
            issues.append({'job': name, 'kind': 'parse_or_resource_error', 'error': str(error)})
            continue
        item = {'path': str(path.relative_to(ROOT)), 'receipt_sha256_at_observation': hashlib.sha256(raw).hexdigest(),
                'started_utc': record['started_utc'], 'ended_utc': record.get('ended_utc'),
                'terminal': terminal, 'is_this_audit': name == args.self_job,
                'cpus': cpus, 'memory_gb_per_process': memory, 'recorded_pid': record.get('pid'),
                'elapsed_seconds': record.get('elapsed_seconds'), 'returncode': record.get('actual_returncode'),
                'process_ok': record.get('process_ok'), 'timed_out': record.get('timed_out'),
                'interrupted': record.get('interrupted'), 'launch_error': record.get('launch_error')}
        jobs[name] = item
        if begun < start or begun >= deadline or ended < begun or (terminal and ended > deadline):
            issues.append({'job': name, 'kind': 'outside_original_window_or_reversed_interval'})
        if not terminal and name != args.self_job:
            issues.append({'job': name, 'kind': 'nonterminal_other_job'})
        if terminal and abs((ended-begun).total_seconds() - record['elapsed_seconds']) > 2:
            issues.append({'job': name, 'kind': 'elapsed_utc_disagreement_over_two_seconds'})
        if record.get('process_ok') and (not terminal or record['actual_returncode'] != 0 or
                record.get('timed_out') or record.get('interrupted') or
                (record.get('expected_marker') and not record.get('marker_seen'))):
            issues.append({'job': name, 'kind': 'inconsistent_success_flag'})
        events.extend([(begun, 1, name), (ended, 0, name)])

    active, peak_cores, peak_memory, peak_jobs = set(), None, None, None
    budget_excesses, cpu_overlaps = [], []
    for when, kind, name in sorted(events):
        if kind == 0:
            active.discard(name)
            continue
        active.add(name)
        counts = Counter(c for j in active for c in jobs[j]['cpus'])
        cores = sum(counts.values())
        memory = sum(jobs[j]['memory_gb_per_process'] for j in active)
        sample = {'utc': when.isoformat(), 'jobs': sorted(active), 'reserved_cores_sum': cores,
                  'distinct_cpu_ids': sorted(counts), 'requested_memory_gb_sum': memory}
        if peak_cores is None or cores > peak_cores['reserved_cores_sum']:
            peak_cores = sample
        if peak_memory is None or memory > peak_memory['requested_memory_gb_sum']:
            peak_memory = sample
        if peak_jobs is None or len(active) > len(peak_jobs['jobs']):
            peak_jobs = sample
        if cores > cpu_limit or memory > memory_limit:
            budget_excesses.append(sample)
        if any(n > 1 for n in counts.values()):
            cpu_overlaps.append(sample)

    # Read actual kernel process state. CWD identifies checkout processes;
    # a retained process-group ID also catches descendants that changed CWD.
    recorded_groups = {j['recorded_pid']: name for name, j in jobs.items() if j['recorded_pid']}
    census, races = [], 0
    for proc in sorted(Path('/proc').iterdir()):
        if not proc.name.isdigit():
            continue
        try:
            raw_stat = (proc / 'stat').read_text()
            cut = raw_stat.rfind(')')
            tail = raw_stat[cut+2:].split()
            ppid, group, sid = map(int, tail[1:4])
            cwd = Path(os.readlink(proc / 'cwd'))
            here = cwd == ROOT or ROOT in cwd.parents
            if not here and group not in recorded_groups:
                continue
            census.append({'pid': int(proc.name), 'comm': raw_stat[raw_stat.find('(')+1:cut],
                           'state': tail[0], 'ppid': ppid, 'process_group': group, 'session': sid,
                           'start_ticks_since_boot': int(tail[19]), 'cwd': str(cwd),
                           'cwd_in_checkout': here, 'recorded_group_job': recorded_groups.get(group),
                           'is_audit_python': int(proc.name) == os.getpid()})
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            races += 1
    registry = json.loads((ROOT / 'state/jobs.json').read_text())
    counts = Counter(records=len(jobs))
    for job in jobs.values():
        counts['terminal' if job['terminal'] else 'nonterminal'] += 1
        if job['terminal']:
            counts['recorded_success' if job['process_ok'] else 'recorded_nonsuccess'] += 1
        if job['timed_out']:
            counts['timed_out'] += 1
        if job['interrupted']:
            counts['interrupted'] += 1
        if job['launch_error']:
            counts['launch_error'] += 1
    report = {'observed_utc': observed.isoformat(),
              'head': subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip(),
              'scope': 'Interim recorded-reservation accounting and actual process census; not deadline closure or measured resource consumption.',
              'limits': {'cpus': cpu_limit, 'memory_gb_decimal': memory_limit},
              'started_utc': session['started_utc'], 'deadline_utc': session['deadline_utc'],
              'counts': dict(counts), 'jobs': jobs, 'receipt_issues': issues,
              'peak_reserved_cores': peak_cores, 'peak_requested_memory': peak_memory,
              'peak_simultaneous_jobs': peak_jobs, 'budget_excess_observations': budget_excesses,
              'cpu_overlap_observations': cpu_overlaps, 'live_process_census': census,
              'proc_entries_inaccessible_or_gone': races, 'jobs_registry': registry,
              'limitations': [
                  'Intervals use receipt timestamps; reservation release happens after receipt completion.',
                  'Memory is the sum of requested per-process virtual-address limits, not measured tree RSS.',
                  'CPU counts are requested affinity slots, not consumed CPU time.',
                  'Unrecorded commands, agent inference and external tools are outside this accounting.',
                  'The running audit has a mutable nonterminal receipt; inspect its final receipt separately.',
                  'Process-group/PID reuse and a process escaping both group and checkout limit attribution.',
                  'The /proc census is sequential, not an atomic process snapshot.'
              ]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps({'counts': dict(counts), 'receipt_issues': len(issues),
        'peak_reserved_cores': peak_cores, 'peak_requested_memory': peak_memory,
        'peak_simultaneous_jobs': peak_jobs, 'budget_excesses': len(budget_excesses),
        'cpu_overlaps': len(cpu_overlaps), 'live_processes': len(census)}, indent=2))
    print('COMPLETE resource/process inventory; inspect findings')


if __name__ == '__main__':
    main()
