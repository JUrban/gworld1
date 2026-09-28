"""Infrastructure checks use disposable fixtures, never the experiment clock."""
import contextlib
from datetime import datetime,timedelta,timezone
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

REPO=Path(__file__).resolve().parents[1]


def module(name):
    spec=importlib.util.spec_from_file_location(name,REPO/'scripts'/f'{name}.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


class Lifecycle(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for d in ['state','config','sources','data','results']: (self.root/d).mkdir()
        self.session=module('session');self.session.ROOT=self.root
        self.runner=module('run_recorded');self.runner.ROOT=self.root
        self.config={'duration_hours':48,'cpu_cores':1,'memory_gb_decimal':1}
        (self.root/'config/run.json').write_text(json.dumps(self.config))
        for f in ['sources/manifest.json','data/problems.json','data/status_updates.json']:
            (self.root/f).write_text('[]\n')
        self.state={'phase':'preparation','started_utc':None,'deadline_utc':None}
        self.write_state()

    def write_state(self):
        (self.root/'state/session.json').write_text(json.dumps(self.state))

    def active(self):
        now=datetime.now(timezone.utc)
        self.state.update(phase='active',started_utc=now.isoformat(),deadline_utc=(now+timedelta(minutes=1)).isoformat(),run_config=self.config)
        self.write_state()

    def run_command(self,name,code,timeout=5,expect='PASS'):
        argv=['run_recorded','--name',name,'--memory-gb','0.5','--timeout',str(timeout),'--expect',expect,'--',sys.executable,'-c',code]
        with mock.patch.object(sys,'argv',argv),contextlib.redirect_stdout(io.StringIO()):
            return self.runner.main()

    def test_preparation_refuses_commands_and_creates_no_result(self):
        with self.assertRaises(SystemExit): self.run_command('forbidden','print("PASS")')
        self.assertEqual(list((self.root/'results').iterdir()),[])
        self.assertIsNone(json.loads((self.root/'state/session.json').read_text())['started_utc'])

    def test_explicit_start_is_required_and_deadline_is_48_hours(self):
        with self.assertRaises(SystemExit): self.session.start('fixture only',False,'test')
        with self.assertRaises(SystemExit): self.session.start('',True,'test')
        def git(args,**kw): return '' if 'status' in args else 'fixture-commit\n'
        with mock.patch.object(self.session.subprocess,'run'),mock.patch.object(self.session.subprocess,'check_output',side_effect=git):
            state=self.session.start('SYNTHETIC FIXTURE AUTHORIZATION',True,'fixture model')
        delta=datetime.fromisoformat(state['deadline_utc'])-datetime.fromisoformat(state['started_utc'])
        self.assertEqual(delta,timedelta(hours=48))
        with self.assertRaises(SystemExit): self.session.start('fixture only',True,'test')

    def test_exit_failure_is_not_masked_by_success_marker(self):
        self.active()
        self.assertEqual(self.run_command('failure','print("PASS");raise SystemExit(3)'),1)
        r=json.loads((self.root/'results/failure/process.json').read_text())
        self.assertEqual(r['actual_returncode'],3);self.assertTrue(r['marker_seen']);self.assertFalse(r['process_ok'])

    def test_success_and_missing_marker(self):
        self.active()
        self.assertEqual(self.run_command('success','print("PASS")'),0)
        self.assertEqual(self.run_command('missing','print("nothing")'),1)
        self.assertEqual(json.loads((self.root/'state/jobs.json').read_text()),{})

    def test_timeout_and_expired_deadline(self):
        self.active()
        self.assertEqual(self.run_command('timeout','import time;time.sleep(2)',timeout=0.05),1)
        r=json.loads((self.root/'results/timeout/process.json').read_text())
        self.assertTrue(r['timed_out']);self.assertNotEqual(r['actual_returncode'],0)
        self.state['deadline_utc']=(datetime.now(timezone.utc)-timedelta(seconds=1)).isoformat();self.write_state()
        with self.assertRaises(SystemExit): self.run_command('expired','print("PASS")')
        self.assertFalse((self.root/'results/expired').exists())

    def test_budget_reservations_block_oversubscription(self):
        self.active()
        self.runner.reserve('first',1,0.75,self.config)
        with self.assertRaises(SystemExit): self.runner.reserve('second',1,0.5,self.config)
        self.runner.reserve('first',0,0,self.config,True)
        with self.assertRaises(SystemExit): self.runner.reserve('oversized',1,2,self.config)


if __name__=='__main__': unittest.main()
