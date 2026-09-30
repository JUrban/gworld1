#!/usr/bin/env python3
"""Structured mixed class-two fixtures with independently replayable arithmetic."""
import argparse
import json
import random
from pathlib import Path
from n5_class2_mixed import ClassTwo, decide
from check_n5_class2_pipeline import form, serial, gap_record


def model(qo, zo, entries, powers=None):
    return dict(quotient_orders=qo,center_orders=zo,
                beta=form(len(qo),len(zo),entries),
                powers=powers if powers is not None else [[0]*len(zo) for _ in qo])


def direct_sum(*models):
    qlabels=[(j,i,d) for j,m in enumerate(models) for i,d in enumerate(m['quotient_orders'])]
    zlabels=[(j,i,d) for j,m in enumerate(models) for i,d in enumerate(m['center_orders'])]
    qlabels.sort(key=lambda x:bool(x[2]));zlabels.sort(key=lambda x:bool(x[2]))
    qi={(j,i):k for k,(j,i,d) in enumerate(qlabels)}
    zi={(j,i):k for k,(j,i,d) in enumerate(zlabels)}
    out=model([d for j,i,d in qlabels],[d for j,i,d in zlabels],[])
    for j,m in enumerate(models):
        for u in range(len(m['quotient_orders'])):
            for v in range(len(m['center_orders'])):
                out['powers'][qi[j,u]][zi[j,v]]=m['powers'][u][v]
            for v in range(len(m['quotient_orders'])):
                for k,b in enumerate(m['beta'][u][v]):out['beta'][qi[j,u]][qi[j,v]][zi[j,k]]=b
    return out


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=False)
    d8=model([2,2],[2],[(0,1,[1])])
    q8=model([2,2],[2],[(0,1,[1])],[[1],[1]])
    m16=model([2,2],[4],[(0,1,[2])],[[1],[0]])
    h3=model([0,0],[0],[(0,1,[1])])
    cyclic=lambda m:model([],[m],[])
    gm=lambda m:model([m,m],[0,0,m],[(0,1,[0,0,1])],[[1,0,0],[0,1,0]])
    sheared=direct_sum(h3,d8)
    sheared['beta'][0][2]=[0,1];sheared['beta'][2][0]=[0,-1]
    fixtures=[('trivial',model([],[],[]),False),('C4',cyclic(4),False),
        ('C6',cyclic(6),True),('C4_C2',direct_sum(cyclic(4),cyclic(2)),True),
        ('Z_C2',direct_sum(cyclic(0),cyclic(2)),True),
        ('D8',d8,False),('Q8',q8,False),('M16',m16,False),
        ('D8_C2',direct_sum(d8,cyclic(2)),True),
        ('Q8_Z',direct_sum(q8,cyclic(0)),True),
        ('G2',gm(2),False),('G3',gm(3),False),('G4',gm(4),False),
        ('G2_Z',direct_sum(gm(2),cyclic(0)),True),
        ('G2_C2',direct_sum(gm(2),cyclic(2)),True),
        ('H3',h3,False),('H3_D8',direct_sum(h3,d8),True),
        ('H3_D8_sheared',sheared,True),
        ('quotient_glue2',model([0]*4,[0,0],[(0,1,[1,0]),(0,3,[0,1]),(2,3,[0,2])]),False),
        ('center_glue2',model([0]*4,[0,0],[(0,1,[2,1]),(2,3,[0,1])]),False)]
    rng=random.Random(9302606);records=[];lies=[]
    for name,inputs,expected in fixtures:
        result=decide(**inputs)
        assert result['answer']==expected,(name,result)
        group=ClassTwo(**inputs);arithmetic=[]
        for _ in range(8):
            a=group.normalize([rng.randrange(-3,4) for _ in group.qo],[rng.randrange(-3,4) for _ in group.zo])
            b=group.normalize([rng.randrange(-3,4) for _ in group.qo],[rng.randrange(-3,4) for _ in group.zo])
            exponent=rng.randrange(-4,5)
            arithmetic.append(dict(a=a,b=b,product=group.multiply(a,b),inverse=group.inverse(a),
                                   exponent=exponent,power=group.power(a,exponent)))
            assert group.multiply(a,group.inverse(a))==group.identity()
        if name=='H3_D8_sheared':
            p=result['branches'][result['witness_branch']]['projection']
            assert any(p[2:,:2]),'cross commutator requires a nonzero quotient shear'
        records.append(serial(dict(name=name,expected=expected,result=result,arithmetic=arithmetic)))
        lies.append(serial(dict(name=name,structure_constants=result['lie_structure_constants'],
                    expected=result['rational']['factor_dimensions'],result=result['rational'])))
        print(json.dumps({'name':name,'answer':expected,'branches':len(result['branches']),
              'quotient_obstructions':len(result['rational_quotient_obstructions'])}),flush=True)
    invalid=[('inconsistent_power',model([2,2],[4],[(0,1,[1])])),
             ('incomplete_center',model([0],[0],[])),
             ('power_on_infinite',model([0,0],[0],[(0,1,[1])],[[1],[0]]))]
    rejections=[]
    for name,data in invalid:
        try:ClassTwo(**data)
        except ValueError as error:rejections.append(dict(name=name,reason=str(error)))
        else:raise AssertionError(('bad input accepted',name))
    (args.output/'certificate.json').write_text(json.dumps(dict(seed=9302606,records=records,rejections=rejections),indent=2)+'\n')
    (args.output/'certificate.g').write_text('N5MixedFixtures := '+gap_record(records)+';\n'
                                           +'N5LieFixtures := '+gap_record(lies)+';\n')
    print('PASS N5 mixed class2:',len(records),'fixtures;',len(rejections),'rejections')


if __name__=='__main__':main()
