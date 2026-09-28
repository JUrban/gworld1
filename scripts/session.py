#!/usr/bin/env python3
"""Read the clock, or start it only after the user's explicit launch instruction."""
import argparse
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def start(authorization, confirm, model):
    if not confirm or not authorization.strip():
        raise SystemExit('Explicit user launch authorization and --confirm-start are required.')
    with (ROOT/'state/launch.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path = ROOT/'state/session.json'
        state = json.loads(path.read_text())
        if state['phase'] != 'preparation' or state.get('started_utc'):
            raise SystemExit('This experiment already started; its clock cannot be reset.')
        subprocess.run([sys.executable, str(ROOT/'scripts/verify_preparation.py')], check=True, cwd=ROOT)
        dirty = subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True)
        if dirty.strip():
            raise SystemExit('Commit the reviewed preparation before starting the clock. Working tree is not clean.')
        config = json.loads((ROOT/'config/run.json').read_text())
        if config['duration_hours'] != 48:
            raise SystemExit('Expected the agreed 48-hour duration; inspect configuration.')
        now = datetime.now(timezone.utc)
        state.update(phase='active', started_utc=now.isoformat(),
            deadline_utc=(now+timedelta(hours=48)).isoformat(),
            launch_authorization=authorization, model_recorded_at_launch=model,
            preparation_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            run_config=config,
            input_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in
                ['sources/manifest.json','data/problems.json','data/status_updates.json','config/run.json']},
            note='48-hour run explicitly launched by the user. Wall-clock time includes review and reporting.')
        temporary=path.with_suffix('.tmp')
        temporary.write_text(json.dumps(state,indent=2)+'\n');temporary.replace(path)
        return state


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('status')
    launch=sub.add_parser('start')
    launch.add_argument('--confirm-start',action='store_true')
    launch.add_argument('--authorization',required=True,help='Quote the actual user launch instruction; never invent it.')
    launch.add_argument('--model',required=True,help='Record the model/configuration supplied at launch, including uncertainty.')
    args=parser.parse_args()
    if args.action=='start':
        state=start(args.authorization,args.confirm_start,args.model)
    else:
        state=json.loads((ROOT/'state/session.json').read_text())
        if state.get('deadline_utc'):
            state['seconds_remaining']=max(0,(datetime.fromisoformat(state['deadline_utc'])-datetime.now(timezone.utc)).total_seconds())
    print(json.dumps(state,indent=2))


if __name__=='__main__': main()
