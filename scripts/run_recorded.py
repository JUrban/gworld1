#!/usr/bin/env python3
"""Run a bounded command during an active experiment and retain process evidence.

CPU slots are shared cooperatively among invocations of this wrapper. The memory
budget reserves requested amounts; RLIMIT_AS is per process, not a cgroup/tree cap.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]


def utc(): return datetime.now(timezone.utc)


def require_active():
    state=json.loads((ROOT/'state/session.json').read_text())
    if state['phase']!='active' or not state.get('deadline_utc'):
        raise SystemExit('Research commands are disabled: experiment has not started.')
    remaining=(datetime.fromisoformat(state['deadline_utc'])-utc()).total_seconds()
    if remaining<=0: raise SystemExit('Experiment deadline has passed. Preserve and report existing work.')
    return state,remaining


def reserve(name, cores, memory, config, release=False):
    with (ROOT/'state/jobs.lock').open('w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        path=ROOT/'state/jobs.json'
        jobs=json.loads(path.read_text()) if path.exists() else {}
        for key,job in list(jobs.items()):
            try: os.kill(job['supervisor_pid'],0)
            except ProcessLookupError: del jobs[key]
        if release:
            jobs.pop(name,None); cpus=[]
        else:
            if name in jobs: raise SystemExit('A job with this name is already running.')
            used={c for j in jobs.values() for c in j['cpus']}
            allowed=sorted(os.sched_getaffinity(0))[:config['cpu_cores']]
            cpus=[c for c in allowed if c not in used][:cores]
            if len(cpus)<cores or sum(j['memory_gb'] for j in jobs.values())+memory>config['memory_gb_decimal']:
                raise SystemExit('Insufficient unreserved CPU/memory budget. Wait or request a smaller job.')
            jobs[name]={'supervisor_pid':os.getpid(),'cpus':cpus,'memory_gb':memory}
        path.write_text(json.dumps(jobs,indent=2)+'\n')
        return cpus


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()


def contains(path,needle):
    tail=b''; needle=needle.encode()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            chunk=tail+block
            if needle in chunk: return True
            tail=chunk[-max(1,len(needle)):]
    return False


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--name',required=True)
    p.add_argument('--timeout',type=float,default=600)
    p.add_argument('--cores',type=int,default=1)
    p.add_argument('--memory-gb',type=float,default=8)
    p.add_argument('--expect',help='Optional literal success marker required in stdout; does not prove mathematical correctness.')
    p.add_argument('command',nargs=argparse.REMAINDER)
    args=p.parse_args()
    state,remaining=require_active()  # Before creating files or starting any child.
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',args.name): p.error('Invalid job name.')
    command=args.command[1:] if args.command[:1]==['--'] else args.command
    if not command or args.cores<1 or args.memory_gb<=0 or args.timeout<=0: p.error('Command and positive resource limits required.')
    config=state['run_config']
    cpus=reserve(args.name,args.cores,args.memory_gb,config)
    outdir=ROOT/'results'/args.name
    try: outdir.mkdir(parents=True,exist_ok=False)
    except BaseException:
        reserve(args.name,0,0,config,True);raise
    stdout=outdir/'stdout.log';stderr=outdir/'stderr.log'
    record={'command':command,'cwd':str(ROOT),'started_utc':utc().isoformat(),
        'cpus':cpus,'memory_gb_per_process':args.memory_gb,'timeout_seconds':min(args.timeout,remaining),
        'expected_marker':args.expect,'actual_returncode':None,'timed_out':False,'interrupted':False}
    begun=time.monotonic();child=None
    def limits():
        os.setsid();os.sched_setaffinity(0,cpus)
        cap=int(args.memory_gb*1_000_000_000)
        resource.setrlimit(resource.RLIMIT_AS,(cap,cap))
    env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    try:
        with stdout.open('wb') as out,stderr.open('wb') as err:
            child=subprocess.Popen(command,cwd=ROOT,stdout=out,stderr=err,env=env,preexec_fn=limits)
            record['pid']=child.pid
            (outdir/'process.json').write_text(json.dumps(record,indent=2)+'\n')
            try: child.wait(timeout=record['timeout_seconds'])
            except subprocess.TimeoutExpired: record['timed_out']=True
            except KeyboardInterrupt: record['interrupted']=True
    except Exception as error:
        record['launch_error']=str(error)
    finally:
        if child is not None:
            # Kill the entire job group, including descendants left after a parent exits.
            try: os.killpg(child.pid,signal.SIGKILL)
            except ProcessLookupError: pass
            child.wait();record['actual_returncode']=child.returncode
        record.update(ended_utc=utc().isoformat(),elapsed_seconds=time.monotonic()-begun,
            stdout_sha256=digest(stdout) if stdout.exists() else None,
            stderr_sha256=digest(stderr) if stderr.exists() else None,
            marker_seen=contains(stdout,args.expect) if args.expect and stdout.exists() else None)
        record['process_ok']=(record['actual_returncode']==0 and not record['timed_out'] and not record['interrupted']
                              and (args.expect is None or record['marker_seen']))
        (outdir/'process.json').write_text(json.dumps(record,indent=2)+'\n')
        reserve(args.name,0,0,config,True)
    print(json.dumps(record,indent=2))
    return 0 if record['process_ok'] else 1


if __name__=='__main__': sys.exit(main())
