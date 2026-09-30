#!/usr/bin/env python3
"""Inventory retained hash bindings and process receipts, not mathematics.

Historical mismatches are reported, never repaired or silently rebaselined.
The completion marker means the inventory finished, not that all checks pass.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HEX = re.compile(r'^[0-9a-f]{64}$')


def bindings(obj, inherited=None):
    if isinstance(obj, dict):
        path = obj.get('path', inherited)
        if isinstance(path,str) and isinstance(obj.get('sha256'),str) and HEX.fullmatch(obj['sha256']):
            yield path, obj['sha256'], obj.get('bytes')
        if isinstance(obj.get('archive'),str) and HEX.fullmatch(str(obj.get('archive_sha256',''))):
            yield obj['archive'],obj['archive_sha256'],None
        for key,value in obj.items():
            if isinstance(value,str) and HEX.fullmatch(value) and ('/' in key or '.' in key):
                yield key,value,None
            elif isinstance(value,(dict,list)):
                yield from bindings(value,key if '/' in key or '.' in key else None)
    elif isinstance(obj,list):
        for value in obj:
            yield from bindings(value)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise SystemExit('Choose a new output path; preserve prior observations.')
    tracked=set(subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0'))
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    cache={}
    def inspect(path):
        key=str(path)
        if key not in cache:
            if not path.is_file():
                cache[key]=None
            else:
                h=hashlib.sha256();size=0
                with path.open('rb') as stream:
                    for block in iter(lambda:stream.read(1024*1024),b''):
                        size+=len(block);h.update(block)
                cache[key]=(h.hexdigest(),size)
        return cache[key]
    # Validate explicitly indexed historical bytes without changing either
    # their original manifest or the current working version.
    historical={};recovery_observations=[];recovery_errors=[]
    for index in sorted((ROOT/'research/audits').glob('historical*recovery*.json')):
        try:
            recovery=json.loads(index.read_text())
            for row in recovery['records']:
                archive=ROOT/row['archived_path']
                actual=inspect(archive)
                valid=bool(actual and actual[0]==row['expected_sha256'] and
                           actual[1]==row['bytes'])
                entry=dict(row,index=str(index.relative_to(ROOT)),archive_matches=valid,
                           archive_tracked=row['archived_path'] in tracked)
                recovery_observations.append(entry)
                if valid:
                    historical[(row['original_path'],row['expected_sha256'])]=entry
                else:
                    recovery_errors.append(entry)
        except Exception as error:
            recovery_errors.append(dict(index=str(index.relative_to(ROOT)),error=str(error)))
    files=sorted(p for p in (ROOT/'research/certificates').rglob('*.json')
                 if 'manifest' in p.name or 'hash' in p.name)
    files += sorted((ROOT/'research/audits').glob('*manifest*.json'))
    files += [ROOT/'sources/manifest.json',ROOT/'sources/status-evidence.json']
    files += [ROOT/'reports/result-scope-ledger.json']
    files += sorted((ROOT/'research/audits').glob('*process-closure*.json'))
    observations=[];empty=[];parse_errors=[]
    for manifest in files:
        try:obj=json.loads(manifest.read_text())
        except Exception as e:
            parse_errors.append(dict(manifest=str(manifest.relative_to(ROOT)),error=str(e)));continue
        rows=list(bindings(obj))
        if not rows:empty.append(str(manifest.relative_to(ROOT)))
        for name,expected,size in rows:
            path=Path(name)
            if path.is_absolute():
                candidates=[path]
            elif isinstance(obj,dict) and obj.get('project_path') and name!=obj.get('archive'):
                candidates=[ROOT/obj['project_path']/path]
            elif path.parts[0] in {'research','results','scripts','sources','literature','problems','reports','state','scratch','provenance','config','bin','large-artifacts','data','docs'}:
                candidates=[ROOT/path]
            else:
                candidates=[manifest.parent/path]
            path=candidates[0]
            try:resolved=str(path.relative_to(ROOT))
            except ValueError:resolved=str(path)
            actual=inspect(path)
            status='missing' if actual is None else ('match' if actual[0]==expected and
                      (size is None or actual[1]==size) else 'mismatch')
            current_status=status
            old=historical.get((resolved,expected))
            if status!='match' and old and (size is None or old['bytes']==size):
                status='historical_match'
            observations.append(dict(manifest=str(manifest.relative_to(ROOT)),declared_path=name,
                resolved_path=resolved,expected_sha256=expected,expected_bytes=size,
                actual_sha256=actual[0] if actual else None,actual_bytes=actual[1] if actual else None,
                status=status,current_path_status=current_status,tracked=resolved in tracked,
                historical_archive=old['archived_path'] if status=='historical_match' else None,
                recovery_index=old['index'] if status=='historical_match' else None))
    processes=[];process_issues=[]
    for p in sorted((ROOT/'results').glob('*/process.json')):
        try:r=json.loads(p.read_text())
        except Exception as e:
            process_issues.append(dict(path=str(p.relative_to(ROOT)),kind='parse_error',error=str(e)));continue
        issues=[]
        for stream in ['stdout','stderr']:
            expected=r.get(stream+'_sha256')
            if expected:
                actual=inspect(p.parent/(stream+'.log'))
                if actual is None or actual[0]!=expected:issues.append(stream+'_hash')
        terminal=r.get('actual_returncode') is not None and bool(r.get('ended_utc'))
        if not terminal:issues.append('no_terminal_receipt')
        if r.get('process_ok') and (r.get('actual_returncode')!=0 or r.get('timed_out') or
                r.get('interrupted') or (r.get('expected_marker') and not r.get('marker_seen'))):
            issues.append('inconsistent_success_flag')
        item=dict(path=str(p.relative_to(ROOT)),terminal_receipt=terminal,
            recorded_process_ok=r.get('process_ok'),returncode=r.get('actual_returncode'),
            timed_out=r.get('timed_out'),interrupted=r.get('interrupted'),issues=issues)
        processes.append(item)
        if issues:process_issues.append(item)
    session=json.loads((ROOT/'state/session.json').read_text())
    frozen=[]
    for name,expected in session.get('input_sha256',{}).items():
        actual=inspect(ROOT/name)
        frozen.append(dict(path=name,expected_sha256=expected,
            actual_sha256=actual[0] if actual else None,matches=bool(actual and actual[0]==expected)))
    registry=json.loads((ROOT/'state/jobs.json').read_text())
    # This administrative audit's own process receipt is necessarily unfinished.
    # Keep it visible; a subsequent observation must inspect its terminal record.
    report=dict(created_utc=datetime.now(timezone.utc).isoformat(),head=head,
        scope='Artifact/receipt integrity only. No proof checking, solver rerun, or novelty determination.',
        source_manifest_count=len(files),unrecognized_empty_manifests=empty,parse_errors=parse_errors,
        historical_recoveries=recovery_observations,recovery_errors=recovery_errors,
        bindings=observations,binding_counts=dict(Counter(x['status'] for x in observations)),
        distinct_files_hashed=sum(v is not None for v in cache.values()),
        distinct_bytes_hashed=sum(v[1] for v in cache.values() if v is not None),
        untracked_binding_paths=sorted({x['resolved_path'] for x in observations if not x['tracked']}),
        process_records=processes,process_issues=process_issues,frozen_inputs=frozen,
        jobs_registry_at_observation=registry)
    with args.output.open('x') as stream:json.dump(report,stream,indent=2);stream.write('\n')
    print(json.dumps({k:report[k] for k in ['source_manifest_count','binding_counts','distinct_files_hashed','distinct_bytes_hashed']}))
    print('Untracked binding paths:',len(report['untracked_binding_paths']))
    print('Process issues:',len(process_issues),'Unrecognized manifests:',len(empty))
    print('Historical recovery errors:',len(recovery_errors))
    print('COMPLETE artifact inventory; inspect findings before judging integrity')


if __name__=='__main__':
    main()
