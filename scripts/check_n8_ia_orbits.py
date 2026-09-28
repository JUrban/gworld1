#!/usr/bin/env python3
"""Deterministic tests of IA orbit lifting, integer kernels and full stratum cases."""
import json,time
from pathlib import Path
from n8_ia_orbits import Magnus,IA,IABasis,orbit,decide_nonzero_degree_two,wcomm,wpow

out=Path(__file__).resolve().parents[1]/'research/certificates/N8-IA'
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
checks=[];fixtures=[]
def record(row):
    checks.append(row)
    (out/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8IAFixtures := '+json.dumps(fixtures)+';\n')
    print(json.dumps(row),flush=True)

for rank,degree in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]:
    started=time.monotonic();m=Magnus(rank,degree);u=m.ia_group();gens=u.generators()
    record(dict(test='build',rank=rank,degree=degree,ia_dimension=len(gens),
                seconds=round(time.monotonic()-started,3)))
    # Inverses/composition and Euclidean subgroup pivots with nonprimitive inputs.
    a=gens[0];b=gens[1]
    assert a.compose(a.inverse()).is_identity() and a.inverse().compose(a).is_identity()
    small=IABasis(m);small.insert(a.power(6));small.insert(a.power(10));small.complete()
    assert small.reduce(a.power(2)).is_identity() and not small.reduce(a).is_identity()
    small.insert(a.power(3));small.complete();assert small.reduce(a).is_identity()
    # The correction words need not have been supplied to the orbit algorithm.
    chosen=a.power(2).compose(b.inverse()).compose(gens[min(len(gens)-1,rank+1)])
    for nonprimitive in (False,True):
        started=time.monotonic()
        x=m.expansion([1,1] if nonprimitive else [1])
        y=m.expansion([2,2] if nonprimitive else [2]);start=m.comm(x,y)
        target=chosen.apply(start);trace=[];found=orbit(m,u,start,target,trace)
        assert found is not None
        xx,yy=found.apply(x),found.apply(y);assert m.comm(xx,yy)==target
        targetword=m.collect(target)[0];xword=m.collect(xx)[0];yword=m.collect(yy)[0]
        fixtures.append([rank,degree,targetword,xword,yword])
        record(dict(test='positive_orbit',rank=rank,degree=degree,nonprimitive=nonprimitive,
                    seconds=round(time.monotonic()-started,3),trace=trace))
    # Every IA displacement of this degree-two coefficient is divisible by 4
    # in degree three. This is a negative ORBIT control, not a claim about all
    # possible factor pairs of the altered target.
    bad=m.mul(m.comm(m.expansion([1,1]),m.expansion([2,2])),m.bydegree[3][0]['value'])
    trace=[];assert orbit(m,u,m.comm(m.expansion([1,1]),m.expansion([2,2])),bad,trace) is None
    record(dict(test='negative_integer_orbit',rank=rank,degree=degree,trace=trace))

# Here the full decision procedure really enumerates all leading pairs and
# residues. Positive examples include a nonprimitive exterior coefficient.
for degree in (3,4):
    m=Magnus(2,degree)
    for word,expected,label in [
        (wcomm([1],[2]),True,'primitive'),
        (wcomm([1,1],[2])+[],True,'nonprimitive'),
        (wpow(wcomm([1],[2]),2),False,'square obstruction'),
    ]:
        started=time.monotonic();result=decide_nonzero_degree_two(m,word)
        assert result['answer']==expected,(degree,label,result)
        if expected:fixtures.append([2,degree,word,result['x'],result['y']])
        record(dict(test='full_decision',rank=2,degree=degree,label=label,expected=expected,
                    tried=result.get('tried'),seconds=round(time.monotonic()-started,3)))

for degree in (3,4):
    m=Magnus(3,degree)
    word=wcomm([1],[2])+wcomm(wcomm([3],[1]),[3])
    result=decide_nonzero_degree_two(m,word)
    assert not result['answer']
    record(dict(test='full_decision',rank=3,degree=degree,label='outside support plane obstruction',
                expected=False,tried=result['tried']))

print('PASS N8 IA orbit checks:',len(checks),'records;',len(fixtures),'positive witnesses')
