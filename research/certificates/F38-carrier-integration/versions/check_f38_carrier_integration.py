#!/usr/bin/env python3
"""Check both prior positive branches, the negative branch and unresolved case."""
import json,sys,time
from pathlib import Path
from f38_filling_recognition import bounded_comparison

out=Path('research/certificates/F38-carrier-integration');out.mkdir(exist_ok=False)
versions=out/'versions';versions.mkdir();records=[];fixtures=[]
prior=json.loads(Path('research/certificates/F38-common-filling/checks.json').read_text())
labels=['two_filling_ambient_rank2','proper_free_factor_rank3','cyclic_HNN_vertex_rank3','Lee_positive_beyond_this_test']
cases=[next(row for row in prior if row.get('label')==label) for label in labels]
cases.append(dict(label='Lee_ambient_rank3_negative',rank=3,input_u=[1],input_v=[1,1,2,-1,-2]))
expected=['boundedly_equivalent_prior_filling_case',
          'boundedly_equivalent_prior_common_filling_case',
          'boundedly_equivalent_prior_common_filling_case',
          'unresolved_nonfilling_stabilizers_commensurable','not_boundedly_equivalent']
def export(rank,fixed,generators,checks):
 for row in checks:
  result=row['result']
  if result['finite']:fixtures.append([rank,fixed,row['word'],'finite_orbit',generators,result['orbit']])
  else:fixtures.append([rank,fixed,row['word'],'infinite_orbit_witness',result['witness'],[]])
for case,wanted in zip(cases,expected):
 print('BEGIN',case['label'],flush=True);start=time.monotonic()
 answer=bounded_comparison(case['rank'],case['input_u'],case['input_v'])
 assert answer['status']==wanted,(case['label'],answer['status'])
 obstruction=answer.get('obstruction',answer)
 for row in obstruction['reports']:
  export(case['rank'],row['fixed'],row['generators'],[dict(word=row['moved'],result=row['orbit_check'])])
 if 'first_outer_group' in answer:
  export(case['rank'],case['input_u'],obstruction['reports'][0]['generators'],answer['first_outer_group']['checks'])
 if 'common_carrier' in answer:
  # Exact match to the complete standalone carrier record already replayed in GAP.
  assert json.loads(json.dumps(answer['common_carrier']))==case['result']
 records.append(dict(label=case['label'],rank=case['rank'],result=answer,seconds=time.monotonic()-start))
 (out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
 (out/'fixtures.g').write_text('F38StabilizerFixtures := '+json.dumps(fixtures)+';\n')
 print('RESULT',case['label'],wanted,round(records[-1]['seconds'],3),flush=True)
for module in list(sys.modules.values()):
 path=getattr(module,'__file__',None)
 if path and Path(path).resolve().parent==Path('scripts').resolve():
  src=Path(path);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print('PASS F38 carrier integration:',len(cases),'pairs;',len(fixtures),'additional orbit fixtures',flush=True)
