#!/usr/bin/env python3
"""Specialize exact universal maps and retain the entire block period lattice.

Prefixes through offset15 need input weights only through25. The formal maps
are already checked through26; this constructs their prefix translations and
the complete finite quotient, without enumerating its potentially huge size.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,time
from math import gcd
import sympy as S
from flint import fmpz_mat
from check_n8_polynomial_group_tail import Group
from n8_weighted_automorphisms import add
from n8_component_hnf import hermite
from parametric_integer_linear import decode_matrix,encode_matrix,integer_solve,gap_value

def main(args):
    begin=time.monotonic();out=args.output;out.mkdir(parents=True,exist_ok=False)
    fixture=json.loads(args.block.read_text());gauges=json.loads(args.gauges.read_text())
    assert fixture['class_bound']==26 and gauges['class_bound']==26
    m=Group(1,4,25);D=m.letters[1]
    for _ in range(6):D=m.bracket(m.letters[0],D)
    di=next(i for i,h in enumerate(m.hall) if h['lie']==D)
    base=[m.power(m.group_hall(0),2),m.power(m.group_hall(di),3)]
    formal=[]
    for i,(w,pair) in enumerate(gauges['hall']):
        if w>25:formal.append(m.one)
        elif not pair:formal.append(base[i])
        else:formal.append(m.comm(formal[pair[0]],formal[pair[1]]))
    def evaluate(terms):
        result=m.one
        for i,n in terms:
            if gauges['hall'][i][0]<=25:result=m.mul(result,m.power(formal[i],n))
        return result
    def prefix(value,side):
        start=[1,10][side]+9;stop=[1,10][side]+15
        assert 2*start>stop
        residual=add(value,m.one,-1);result={}
        assert all(m.weight(w)>=start for w in residual)
        for degree in range(start,stop+1):
            inds,basis=m.layers[degree]
            for j,z in basis.coordinates(m.layer(residual,degree)).items():
                assert z.denominator==1
                i=inds[j];result[i]=int(z)
                residual=add(residual,add(m.group_hall(i),m.one,-1),-z)
        assert not any(v for w,v in residual.items() if m.weight(w)<=stop)
        return result
    A,J=decode_matrix(fixture['A']),decode_matrix(fixture['J'])
    End=decode_matrix(fixture['Aend']);records=[];periods=[]
    for rec in gauges['records']:
        plus=[evaluate(row) for row in rec['plus']]
        minus=[evaluate(row) for row in rec['minus']]
        pp=[prefix(m.mul(m.inv(base[i]),plus[i]),i) for i in range(2)]
        mm=[prefix(m.mul(m.inv(base[i]),minus[i]),i) for i in range(2)]
        assert all(pp[i]=={j:-n for j,n in mm[i].items()} for i in range(2))
        vector=S.Matrix([pp[side].get(i,0) for side,i in fixture['block_axes']])
        assert A*vector==S.zeros(A.rows,1)
        answer=integer_solve(J,vector);assert answer is not None
        z,kernel=answer;assert kernel.cols==0 and z[0]==0
        if rec['offset']<=13:periods.append(z[1:,0])
        else:
            assert not any(vector)
            endvector=S.Matrix([pp[side].get(i,0) for side,i in fixture['end_axes']])
            assert any(endvector) and End*endvector==S.zeros(End.rows,1)
            assert End.cols-fmpz_mat([[int(x) for x in row] for row in End.tolist()]).rank()==1
            terminal_step=gcd(*(int(x) for x in endvector))
            assert terminal_step>0
            terminal_primitive=[int(x)//terminal_step for x in endvector]
            assert gcd(*terminal_primitive)==1
        records.append(dict(offset=rec['offset'],power=rec['power'],prefix=[sorted(x.items()) for x in pp],
                            block_translation=[int(x) for x in vector],kernel_coordinates=[int(x) for x in z]))
        print('specialized universal period',rec['offset'],'block coordinates',list(z),flush=True)
    L=S.Matrix.hstack(*periods);assert L.shape==(3,3) and L.det()!=0
    HH,UU=hermite(fmpz_mat([[int(x) for x in row] for row in L.T.tolist()]))
    H,U=S.Matrix(HH.tolist()),S.Matrix(UU.tolist())
    assert H==U*L.T and all(H[i,i]>0 for i in range(3))
    assert all(H[i,j]==0 for i in range(3) for j in range(i))
    bounds=[int(H[i,i]) for i in range(3)];index=int(abs(L.det()))
    assert S.prod(bounds)==index
    data=dict(block=str(args.block),gauges=str(args.gauges),prefix_class=25,
        records=records,L=encode_matrix(L),H=encode_matrix(H),U=encode_matrix(U),
        quotient_order=index,residue_bounds=bounds,
        terminal_period_step=terminal_step,terminal_primitive=terminal_primitive,
        residue_rule='Every integer triple 0<=r_i<residue_bounds[i]; none enumerated or discarded',
        free_coordinate='First adapted block parameter; periods have zero first coordinate',
        seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8DelayedPeriods := '+gap_value(data)+';\n')
    print('PASS N8 delayed periods: full three-dimensional period lattice; quotient order',index,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--block',type=Path,required=True)
    ap.add_argument('--gauges',type=Path,default=Path('research/certificates/N8-three-exception-gauges-c26-v2/checks.json'))
    ap.add_argument('--output',type=Path,required=True);main(ap.parse_args())
