#!/usr/bin/env python3
"""Recognition controls distinct from solving supported inputs."""
import json
from pathlib import Path
from n8_iterated_adjoint import Magnus,leading_family,decide_iterated_adjoint
from n8_penultimate import mixed_candidates
from n8_ia_orbits import wcomm,wpow

records=[]
for rank,c in [(2,10),(3,7)]:
    m=Magnus(rank,c);z=[1,rank];t=list(m.bydegree[2][0]['word'])
    if rank==3:t+=m.bydegree[2][-1]['word']
    d=list(t)
    for _ in range(c-5):d=wcomm(z,d)
    word=wcomm(wpow(z,2),wpow(d,3));w=m.layer(m.expansion(word),c-2)
    pairs,evidence=leading_family(m,w)
    old=mixed_candidates(m,w,1,c-3)
    assert sorted((cc,dd) for cc,dd,_ in pairs)==sorted(old)
    assert len(pairs)==8
    assert any(any(v[1]>1 for v in t0) for _,_,t0 in pairs)
    # A nonzero bracket in L'' has the same leading degree but cannot have
    # the nonzero metabelian image required by the iterated-adjoint family.
    outside=wcomm(m.bydegree[2][0]['word'],m.bydegree[c-4][-1]['word'])
    expansion=m.expansion(outside)
    assert min(len(w) for w in expansion if w)==c-2
    answer=decide_iterated_adjoint(m,outside)
    assert answer['answer'] is None and answer['case']=='outside_iterated_adjoint_scope'
    records.append(dict(rank=rank,degree=c,word=word,leading_family=evidence,
                        pairs=pairs,outside_word=outside,outside_result=answer,
                        outside_reason='Nonzero original-degree c-2 commutator in L-double-prime.'))
out=Path('research/certificates/N8-iterated-adjoint-lead/scope-checks.json')
assert not out.exists();out.write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 iterated-adjoint scope: 16 complete signed leading scales; two same-degree outside-scope positive commutators')
