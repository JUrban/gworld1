#!/usr/bin/env python3
"""Check corpus integrity and readiness; does not run any mathematical search."""
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_catalog import CATEGORIES


def main():
    manifest=json.loads((ROOT/'sources/manifest.json').read_text())
    records={r['url']:r for r in manifest['records']}
    for r in records.values():
        if r['status']=='error': continue
        data=(ROOT/r['path']).read_bytes()
        assert len(data)==r['bytes'],r['path']
        assert hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
    for name,_,_ in CATEGORIES:
        assert records[manifest['base_url']+name]['status']==200,name
    failures=[r['url'] for r in records.values() if r['status']=='error']
    assert failures==[manifest['base_url']+'Back.htm'],failures
    assert records[manifest['base_url']+'Back.html']['status']==200
    for r in json.loads((ROOT/'sources/status-evidence.json').read_text()):
        assert r['status']==200,r['url']
        data=(ROOT/r['path']).read_bytes()
        assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
    problems=json.loads((ROOT/'data/problems.json').read_text())
    ids={p['id']:p for p in problems}
    assert len(ids)==len(problems)==195
    assert len({p['category'] for p in problems})==16
    for p in problems:
        raw=(ROOT/p['source_path']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==p['source_sha256'],p['id']
        fragment=raw[p['start_byte']:p['end_byte']]
        assert hashlib.sha256(fragment).hexdigest()==p['fragment_sha256'],p['id']
        assert fragment==(ROOT/'problems'/p['id']/'source-fragment.html').read_bytes(),p['id']
        assert p['research_status']=='not_started',p['id']
    assert all(p in ids for p in ['F27','F28','F30','M0'])
    assert ids['F1']['site_starred_parts']==['a'] and not ids['F1']['site_heading_star']
    assert ids['F24']['site_starred_parts']==['a'] and not ids['F24']['hall_of_fame']
    assert ids['F39']['site_starred_parts']==['b']
    assert ids['N8']['site_starred_parts']==['a'] and ids['N9']['site_starred_parts']==['b']
    assert ids['FP7']['hall_of_fame'][0]['anchor_id_disagrees_with_label']
    assert ids['FP8']['hall_of_fame'][0]['anchor_id_disagrees_with_label']
    assert ids['O12']['status_updates'][0]['parts']==['b']
    assert all(ids[p]['background_sections'] for p in ['O5','O6','O7','B2','B6','H7','H10'])
    state=json.loads((ROOT/'state/session.json').read_text())
    assert state['phase']=='preparation' and state['started_utc'] is None and state['deadline_utc'] is None
    claims=(ROOT/'research/claims.jsonl').read_text()
    assert not claims.strip(),'Preparation must not contain research claims.'
    print('PASS: 195 entries, 16 categories, source hashes, subpart markers, known link discrepancies, empty claims, unstarted clock.')
    print('One publisher typo returns 404: Back.htm; the adjacent correct Back.html link and its full page are archived.')


if __name__=='__main__': main()
