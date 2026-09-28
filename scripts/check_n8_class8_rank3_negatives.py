#!/usr/bin/env python3
"""Additional rank-three class-eight polynomial and last-layer controls."""
import argparse,json,time,faulthandler
from pathlib import Path
from n8_class8 import Magnus,decide_class8
from n8_ia_orbits import wcomm
faulthandler.dump_traceback_later(60,repeat=True)
parser=argparse.ArgumentParser();parser.add_argument('--only-final',action='store_true')
parser.add_argument('--directory',type=Path,default=Path('research/certificates/N8-class8-rank3-negatives'))
args=parser.parse_args();out=args.directory
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
m=Magnus(3,8);records=[];witnesses=[];steps=[];polynomials=[]
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,9)})+'\n')
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=3,seed=None,records=records),indent=2)+'\n')
    (out/'polynomials.json').write_text(json.dumps(polynomials,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C8Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C8Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected=None,**extra):
    print('BEGIN',label,extra,flush=True);start=time.monotonic();audit=[]
    result=decide_class8(m,word,audit)
    if expected is not None:assert result['answer']==expected
    if result['answer']:witnesses.append([3,8,word,result['x'],result['y']])
    for row in audit:
        if row['kind']=='polynomial7':polynomials.append(row)
        else:steps.append([3,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    records.append(dict(test=label,answer=result['answer'],word=word,result=result,
                        seconds=round(time.monotonic()-start,3),**extra))
    save();print(label,result['answer'],records[-1]['seconds'],flush=True)
z=[1,3];t=m.bydegree[2][0]['word']+m.bydegree[2][-1]['word']
d=wcomm(z,wcomm(z,t));base=wcomm(z,d)
for layer in [7,8]:
    for k in range(3):
        if args.only_final and (layer,k)!=(8,2):continue
        check(base+m.bydegree[layer][k]['word'],'exceptional_perturbation',
              False if layer==7 else None,layer=layer,case=k)
check([],'identity',True)
check([1],'nonzero_abelianization',False)
if not args.only_final:assert any(not p['certificate']['values'] for p in polynomials)
faulthandler.cancel_dump_traceback_later()
print('PASS N8 class8 rank3 controls:',len(records),'targets;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomial branches')
