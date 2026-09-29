#!/usr/bin/env python3
"""Exact carrier controls and source snapshots; outputs for native GAP replay."""
import json,sys,time
from pathlib import Path
from f38_common_filling import (common_filling_carrier, fringe, cycle_graph,
                               quotient, basis_data)
from f38_stabilizer_obstruction import apply, cyclic, inv

out=Path('research/certificates/F38-common-filling');out.mkdir(exist_ok=False)
versions=out/'versions';versions.mkdir()
for module in list(sys.modules.values()):
    name=getattr(module,'__file__',None)
    if name and Path(name).resolve().parent==Path('scripts').resolve():
        src=Path(name);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
records=[];orbits=[];witnesses=[];quotients=[]

def save():
    (out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
    (out/'fixtures.g').write_text('F38CarrierWitnesses := '+json.dumps(witnesses)+';\n'+
        'F38CarrierQuotients := '+json.dumps(quotients)+';\n'+
        'F38StabilizerFixtures := '+json.dumps(orbits)+';\n')

def partitions(n):
    def visit(word):
        if len(word)==n:
            yield word;return
        for k in range(max(word,default=-1)+2):yield from visit(word+[k])
    yield from visit([])

for word in [(1,), (1,1,1,1), (1,2), (1,2,-1,-2), (1,1,2,2,-1,-2)]:
    graphs=set(fringe(word));start=cycle_graph(word)
    n=1+max(max(a,c) for a,b,c in start);direct=set();total=0
    for labels in partitions(n):
        pairs=[(i,j) for i in range(n) for j in range(i) if labels[i]==labels[j]]
        direct.add(quotient(start,pairs));total+=1
    assert graphs==direct
    for graph in sorted(graphs):
        basis,paths,rewrite=basis_data(graph);coords=rewrite(cyclic(word))
        assert coords is not None
        quotients.append([2,cyclic(word),graph,basis,coords])
    records.append(dict(kind='complete_fringe',word=word,graphs=len(graphs),partitions=total))
    save();print('FRINGE',word,len(graphs),total,flush=True)

u=(1,1,2,2,-1,-2);v=(1,1,-2,-2,-1,2)
cases=[
    ('same_cyclic_powers',2,(1,1),(1,1,1),True),
    ('independently_conjugate_powers',3,(2,1,1,-2),(3,1,1,1,-3),True),
    ('distinct_primitive_carriers',2,(1,),(2,),False),
    ('Lee_positive_beyond_this_test',2,(1,),(1,1,2,-1,-2),False),
    ('two_filling_ambient_rank2',2,u,v,True),
    ('proper_free_factor_rank3',3,u,v,True),
    ('cyclic_HNN_vertex_rank2',2,apply([(1,),(2,1,-2)],u),apply([(1,),(2,1,-2)],v),True),
    ('cyclic_HNN_vertex_rank3',3,apply([(1,),(2,1,-2)],u),apply([(1,),(2,1,-2)],v),True),
    ('independent_conjugates_of_vertex_words',3,
        (3,)+apply([(1,),(2,1,-2)],u)+(-3,),
        (2,3)+apply([(1,),(2,1,-2)],v)+(-3,-2),True),
]
for label,rank,left,right,expected in cases:
    print('BEGIN',label,flush=True);started=time.monotonic()
    answer=common_filling_carrier(rank,left,right)
    positive=answer['status']=='boundedly_equivalent_prior_common_filling_case'
    assert positive is expected,(label,answer)
    if positive:
        witnesses.append([rank,answer['u'],answer['v'],answer['graph'],answer['basis'],
            answer['left'],answer['right'],answer['conjugator']])
    for check in answer['filling_tests']:
        h=len(check['generators'][0][0]) if check['generators'] else len(answer.get('basis',[]))
        # Every nontrivial-rank filling check comes with signed permutation
        # representatives, but obtain rank from a detecting word if necessary.
        if not check['generators']:
            h=max(abs(a) for row in check['outer_group']['checks'] for a in row['word'])
        for row in check['outer_group']['checks']:
            result=row['result']
            if result['finite']:
                orbits.append([h,check['word'],row['word'],'finite_orbit',check['generators'],result['orbit']])
            else:
                orbits.append([h,check['word'],row['word'],'infinite_orbit_witness',result['witness'],[]])
    records.append(dict(kind='carrier',label=label,rank=rank,input_u=left,input_v=right,
                        result=answer,seconds=time.monotonic()-started))
    save();print('RESULT',label,answer['status'],answer['graphs_considered'],round(records[-1]['seconds'],3),flush=True)
print('PASS F38 common filling:',len(cases),'pairs;',len(witnesses),'positive carriers;',
      len(quotients),'quotient graphs;',len(orbits),'orbit fixtures',flush=True)
