#!/usr/bin/env python3
"""Replace two sufficient large periods by exact elementary substitutions."""
from pathlib import Path
import json,argparse
from check_n8_polynomial_group_tail import Group
from n8_universal_gauges import terms_json
from n8_weighted_automorphisms import add

ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
out=args.output;out.mkdir(parents=True,exist_ok=False)
data=json.loads(Path('research/certificates/N8-three-exception-gauges-c26-v2/checks.json').read_text())
m=Group(1,10,26);x,y=m.group_hall(0),m.group_hall(1);comm=m.comm(x,y)
maps=[(9,'left Nielsen', [m.mul(y,x),y],[m.mul(m.inv(y),x),y]),
      (11,'conjugation by the commutator',
       [m.mul(m.inv(comm),m.mul(z,comm)) for z in [x,y]],
       [m.mul(comm,m.mul(z,m.inv(comm))) for z in [x,y]])]
def images(pair,words):
    hall=[]
    for i,h in enumerate(m.hall):
        hall.append(pair[i] if not h['pair'] else m.comm(hall[h['pair'][0]],hall[h['pair'][1]]))
    answer=[]
    for row in words:
        value=m.one
        for i,n in row:value=m.mul(value,m.power(hall[i],n))
        answer.append(value)
    return answer
for offset,kind,plus,minus in maps:
    pp=[terms_json(m.collect(z)) for z in plus];mm=[terms_json(m.collect(z)) for z in minus]
    assert images(plus,mm)==[x,y] and images(minus,pp)==[x,y]
    assert m.comm(*plus)==comm and m.comm(*minus)==comm
    changes=[add(m.log(z),m.letters[i],-1) for i,z in enumerate(plus)]
    assert all(m.weight(w)>=[1,10][i]+offset for i,row in enumerate(changes) for w in row)
    assert any(m.layer(row,[1,10][i]+offset) for i,row in enumerate(changes))
    index=next(i for i,r in enumerate(data['records']) if r['offset']==offset)
    data['records'][index]=dict(offset=offset,power=1,kind=kind,plus=pp,minus=mm)
data['note']='Elementary periods at9/11 replace sufficient nonminimal periods;13/15 retain prior exact maps'
data.pop('seconds',None);data.pop('direction_divisor',None)
fixture=[1,10,26,data['hall'],data['retained'],data['boundaries'],[[r['offset'],r['power'],r['plus'],r['minus']] for r in data['records']]]
(out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(out/'fixtures.g').write_text('N8UniversalFixture := '+json.dumps(fixture)+';\n')
print('PASS N8 compact universal gauges: exact left Nielsen and commutator conjugation; later two maps retained')
