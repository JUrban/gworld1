#!/usr/bin/env python3
"""Bounded full-group controls for the fifth/sixth-layer candidate."""
import argparse,gzip,json,sys,time
from pathlib import Path
from n8_fifth_sixth_layer import Magnus,decide_fifth_sixth_layer
from n8_ia_orbits import wcomm,wpow
from n8_class5 import reduced
p=argparse.ArgumentParser();p.add_argument('--rank',type=int,required=True)
p.add_argument('--class-bound',type=int,required=True);p.add_argument('--directory',type=Path,required=True)
a=p.parse_args();rank=a.rank;c=a.class_bound;out=a.directory
assert (rank,c) in [(2,11),(2,12),(3,8)]
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
versions=out/'versions';versions.mkdir(exist_ok=True)
for name,module in list(sys.modules.items()):
 path=getattr(module,'__file__',None)
 if path and Path(path).resolve().parent==Path('scripts').resolve():
  src=Path(path);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print('BEGIN Magnus',rank,c,flush=True);m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];audit_all=[];polynomials=[]
def save():
 (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,records=records),indent=2)+'\n')
 (out/'audit.json.gz').write_bytes(gzip.compress((json.dumps(audit_all,separators=(',',':'))+'\n').encode(),mtime=0))
 (out/'witnesses.json').write_text(json.dumps(witnesses)+'\n')
def trim(value):
 if isinstance(value,list):return [trim(v) for v in value]
 if isinstance(value,dict):
  return {('polynomial_certificate_index' if k=='polynomial' else k):
          (next(i for i,v in enumerate(polynomials) if v is x) if k=='polynomial' else trim(x))
          for k,x in value.items()}
 return value
def check(word,label,expected='unspecified'):
 word=reduced(word);print('BEGIN',label,flush=True);started=time.monotonic();audit=[]
 result=decide_fifth_sixth_layer(m,word,audit)
 if expected!='unspecified':assert result['answer'] is expected,(label,result)
 if result['answer']:witnesses.append([rank,c,word,result['x'],result['y']])
 for row in audit:
  row.setdefault('rank',rank);row.setdefault('word',word)
  if row['kind'].startswith('polynomial'):polynomials.append(row['certificate'])
 audit_all.extend(audit)
 records.append(dict(test=label,word=word,result=trim(result),seconds=time.monotonic()-started));save()
 print('RESULT',label,result['answer'],round(records[-1]['seconds'],3),flush=True)
 return result
def ad(z,t,n):
 for _ in range(n):t=wcomm(z,t)
 return t
def family(left,right,p,q,label):
 base=wcomm(left,right)
 check(base,label+'_base',True)
 x=wpow(left,2)+wpow(m.bydegree[p+1][-1]['word'],-2)+m.bydegree[p+2][0]['word']
 y=wpow(right,-3)+m.bydegree[q+1][0]['word']+m.bydegree[q+4][-1]['word']
 check(wcomm(x,y),label+'_corrected',True)
 check(base+m.bydegree[c][0]['word'],label+'_top_perturbation')
 check(base+m.bydegree[p+q+1][0]['word'],label+'_first_perturbation')
 if rank==3 and p==q==2:
  # A nonzero metabelian top term cannot be a commutator of two
  # gamma_2 elements; its leading degree-four pair list has only (2,2).
  negative=check(base+ad([3],[2],c-1),label+'_metabelian_top_negative',False)
  assert all(t['p']==2 or t['integral_pairs']==0 for t in negative['leading_types'])
 if q-p in (1,2):
  check(wcomm(left,wpow(right,3))+m.bydegree[c][0]['word'],label+'_nonprimitive_nielsen')
for d in ([6,7] if c==11 else [7,8] if c==12 else [4]):
 for p0 in range(2,d//2+1):
  q0=d-p0
  if p0==q0 and len(m.bydegree[p0])<2:continue
  family(m.bydegree[p0][0]['word'],m.bydegree[q0][-1]['word'],p0,q0,f'd{d}_type{p0}_{q0}')
 # Consecutive adjoints give first/second exceptional kernels according
 # to parity, or the second Nielsen direction at q=3.
 q0=d-1;z=[1];t=m.bydegree[2][0]['word'];right=ad(z,t,q0-2)
 base=wcomm(z,right);answer=check(base,f'd{d}_type1_base',True)
 last=answer['trace'][-1]
 assert last['first_kernel_dimension']==int(q0%2==0)
 if q0%2:
  assert last['second_branches'][-1]['kernel_dimension']==1
 x=z+wpow(m.bydegree[3][-1]['word'],2)+m.bydegree[4][0]['word']
 y=wpow(right,3)+wpow(m.bydegree[q0+2][0]['word'],-2)+m.bydegree[q0+4][-1]['word']
 check(wcomm(x,y),f'd{d}_type1_corrected',True)
 for j in (2,3,4,c-d):
  if j==4 and c-d==4:continue
  check(base+m.bydegree[d+j][0]['word'],f'd{d}_type1_offset{j}_perturbation')
check([],'outside_identity',None);check([1],'outside_degree_one',None)
assert any(r['result']['answer'] is False for r in records)
from collections import Counter
counts=Counter(row['kind'] for row in audit_all)
if c>=11:assert counts['coupled'] and counts['polynomial_late']
print('PASS N8 fifth/sixth layer:',len(records),'records;',len(witnesses),'witnesses;',dict(counts),flush=True)
