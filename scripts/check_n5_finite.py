#!/usr/bin/env python3
"""Apply N5 lifting to complete finite-central-quotient branch lists."""
import argparse,json
from pathlib import Path
from n5_central_constraints import split,relation_constraints,lifting_corrections

parser=argparse.ArgumentParser()
parser.add_argument('--directory',default='research/certificates/N5-finite')
parser.add_argument('--label',default='finite')
args=parser.parse_args()
out=Path(__file__).resolve().parents[1]/args.directory
data=json.loads((out/'input.json').read_text());records=[];witnesses=[]
assert not (out/'checks.json').exists()
for index,(order,gid,expected,orders,zgens,branches) in enumerate(data):
    n=orders.count(0);assert all(d==0 for d in orders[:n])
    torsion_orders=orders[n:]
    witness=None
    for branchid,parts in enumerate(branches):
        constraints=[]
        for side,(e,defects,require,lifts,rels) in enumerate(parts,1):
            constraints+=relation_constraints(e,defects,n,torsion_orders,side)
        p=split(n,torsion_orders,constraints,tuple(bool(part[2]) for part in parts))
        if p is None:continue
        corrections=[lifting_corrections(e,defects,len(lifts),n,torsion_orders,side,p)
                     for side,(e,defects,require,lifts,rels) in enumerate(parts,1)]
        witness=[index+1,branchid+1,[[int(x) for x in p.row(i)] for i in range(p.rows)],corrections]
        witnesses.append(witness);break
    assert bool(witness)==bool(expected),(order,gid,expected,witness)
    record=dict(answer=bool(witness),branches=len(branches))
    record.update(dict(order=order,id=gid) if args.label=='finite' else dict(m=order,kind=gid))
    records.append(record)
    (out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
    (out/'witnesses.g').write_text('N5FiniteWitnesses := '+json.dumps(witnesses)+';\n')
    print(json.dumps(records[-1]),flush=True)
(out/'input.g').write_text('N5FiniteInput := '+json.dumps(data)+';\n')
print('PASS N5 '+args.label+' lifting:',len(records),'groups;',len(witnesses),'decompositions')
