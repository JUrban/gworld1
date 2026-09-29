#!/usr/bin/env python3
"""Actual last-exception quadratic and later universal kernel through class26.

Forked from check_n8_three_exception_block.py in this work period. Earlier
exceptional coordinates are fixed in this fixture; it is not a surviving
unbounded absorbed-parameter example. The full integral block is retained.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import argparse,json,time,faulthandler
import sympy as S
from flint import fmpz_mat
from check_n8_polynomial_group_tail import Group
from check_n8_delayed_gauges import description
from check_n8_parametric_tail import terms,rat
from n8_weighted_automorphisms import add,scale
from n8_component_hnf import hermite
from n8_polynomial_families import families,point_at
from parametric_integer_linear import T,integer_solve,encode_matrix,gap_value

def rank(A):
    den=lcm(1,*(int(x.q) for x in A))
    return fmpz_mat([[int(x*den) for x in row] for row in A.tolist()]).rank()

def main(args):
    begin=time.monotonic();ew=4;p,q,t=1,10,7;d=p+q;c=args.class_bound
    assert c in [25,26] and c-d<16
    exceptions=[7];blockexceptions=[7,9,11,13]
    out=args.output;out.mkdir(parents=True,exist_ok=False)
    diagnostic=(out/'diagnostic-stacks.log').open('w');faulthandler.dump_traceback_later(90,repeat=True,file=diagnostic)
    m=Group(1,ew,c);a,e=m.letters;D=e
    for _ in range(6):D=m.bracket(a,D)
    di=next(i for i,h in enumerate(m.hall) if h['lie']==D)
    base=(m.power(m.group_hall(0),2),m.power(m.group_hall(di),3));comm0=m.comm(*base)
    def axes(s):return [(side,i) for side,w in enumerate((p,q)) for i in m.layers[w+s][0]]
    blockaxes=[a for s in range(t,2*t) for a in axes(s)];endaxes=axes(2*t)
    lowrows=[i for i,h in enumerate(m.hall) if d+t<=h['weight']<d+2*t]
    endrows=[i for i,h in enumerate(m.hall) if d+2*t<=h['weight']<=c]
    endaxes=[ax for ss in range(2*t,c-d+1) for ax in axes(ss)]
    def correct(pair,ax,vec):
        pair=list(pair)
        for (side,i),z in zip(ax,vec):
            assert S.sympify(z).is_Integer
            if z:pair[side]=m.mul(pair[side],m.power(m.group_hall(i),int(z)))
        return pair
    def coordinates(x,rows):
        # All compared errors start at weight18, so their multiplication
        # is addition through26. Collect only through the requested bound;
        # approximate block columns are used only through weight24.
        residual=add(x,m.one,-1);data={};stop=max(m.hall[i]['weight'] for i in rows)
        assert all(m.weight(w)>=d+t for w in residual)
        for degree in range(d+t,stop+1):
            inds,basis=m.layers[degree]
            for j,z in basis.coordinates(m.layer(residual,degree)).items():
                assert z.denominator==1
                i=inds[j];data[i]=z
                residual=add(residual,add(m.group_hall(i),m.one,-1),-z)
        assert not any(v for w,v in residual.items() if m.weight(w)<=stop)
        return S.Matrix([rat(data.get(i,Q(0))) for i in rows])
    def relative(x,y):return m.mul(m.inv(x),y)
    base_x_tail,base_y_tail=add(base[0],m.one,-1),add(base[1],m.one,-1)
    delta0=add(comm0,m.one,-1);inv_x,inv_y=m.inv(base[0]),m.inv(base[1])
    def columns_for(ax,rows,limit):
        columns=[]
        for side,i in ax:
            w=m.hall[i]['weight'];v=add(m.group_hall(i),m.one,-1)
            assert 2*d+w>limit and d+2*w>limit
            conjugation=m.bracket(delta0,v)
            if side==0:
                assert 2*w+q>limit
                change=m.mul(inv_y,m.bracket(v,base_y_tail));low=w+q
            else:
                assert p+2*w>limit
                change=m.mul(inv_x,m.bracket(base_x_tail,v));low=p+w
                assert low+2*d>limit
                change=add(change,m.bracket(change,delta0))
            assert 2*low>limit
            columns.append(coordinates(add(m.one,add(change,conjugation)),rows))
        return S.Matrix.hstack(*columns)
    A=columns_for(blockaxes,lowrows,d+2*t-1)
    planted=[j%4-1 for j in range(len(blockaxes))]
    known=correct(base,blockaxes,planted);target=m.comm(*known)
    rhs=coordinates(relative(comm0,target),lowrows)
    assert rhs==A*S.Matrix(planted)
    control=[2-j%5 for j in range(len(blockaxes))]
    assert coordinates(relative(comm0,m.comm(*correct(base,blockaxes,control))),lowrows)==A*S.Matrix(control)
    point,K=integer_solve(A,rhs);r=K.cols
    assert r==len(blockexceptions),('Unexpected surviving block rank',r,blockexceptions)
    # Adapt an integral basis to successive first nonzero exceptional
    # coordinates. Every elementary change is unimodular; steps stay.
    change=S.eye(r);J=K;firstrows=[];steps=[]
    for col,s in enumerate(blockexceptions):
        row=next(j for j,(side,i) in enumerate(blockaxes) if side==0 and m.hall[i]['weight']==p+s and any(J[j,k] for k in range(col,r)))
        for k in range(col+1,r):
            aa,bb=J[row,col],J[row,k]
            if not aa and not bb:continue
            u,v,g=S.gcdex(aa,bb);assert g>0
            H=S.eye(r);H[col,col]=u;H[k,col]=v;H[col,k]=-bb/g;H[k,k]=aa/g
            change=change*H;J=J*H
        if J[row,col]<0:
            H=S.eye(r);H[col,col]=-1;change=change*H;J=J*H
        assert J[row,col]>0 and all(not J[row,k] for k in range(col+1,r))
        assert all(not J[j,col] for j,(side,i) in enumerate(blockaxes) if m.hall[i]['weight']<[p,q][side]+s)
        firstrows.append(row);steps.append(int(J[row,col]))
    assert abs(change.det())==1 and J==K*change
    HH,UU=hermite(fmpz_mat([[int(x) for x in row] for row in A.T.tolist()]))
    H,U=S.Matrix(HH.tolist()),S.Matrix(UU.tolist());arank=rank(A)
    assert K==U[arank:,:].T
    print('delayed block',ew,'class',c,'Hall rank',len(m.hall),'shape',A.shape,'free rank',r,'steps',steps,flush=True)
    def pair_at(values):return correct(base,blockaxes,point+J*S.Matrix(values))
    def residual(values):
        full=relative(m.comm(*pair_at(values)),target)
        assert not any(coordinates(full,lowrows))
        return coordinates(full,endrows)
    origin=[0]*r;v00=residual(origin)
    v10=residual([1]+[0]*(r-1));v20=residual([2]+[0]*(r-1))
    q2=(v20-2*v10+v00)/2;q1=v10-v00-q2;polynomial=(v00+q1*T+q2*T*T).applyfunc(S.expand)
    later=[]
    for k in range(1,r):
        values=[0]*r;values[k]=1;later.append(residual(values)-v00)
    samples=[origin,[1]+[0]*(r-1),[2]+[0]*(r-1)]+[[int(j==k) for j in range(r)] for k in range(1,r)]
    samples += [[1]*r,[-2,3,-1,2][:r],[1,-2,2,-1][:r]]
    for values in samples:
        expected=polynomial.subs(T,values[0])
        for k,B in enumerate(later):expected+=values[k+1]*B
        assert residual(values)==expected
    Aend=columns_for(endaxes,endrows,c)
    assert rank(Aend.row_join(q2))==rank(Aend)+1
    # The first quadratic coefficient is independently identified in
    # the full weight25 Lie component; weight26 may contain other terms.
    lead=[]
    for side,weight in enumerate((p,q)):
        poly={}
        for j,(sidej,i) in enumerate(blockaxes):
            if sidej==side and m.hall[i]['weight']==weight+t:
                poly=add(poly,m.hall[i]['lie'],Q(J[j,0]))
        lead.append(poly)
    expected=m.bracket(*lead);inds,basis=m.layers[d+2*t]
    ec=basis.coordinates(expected)
    assert all(q2[endrows.index(i)]==-rat(ec.get(j,Q(0))) for j,i in enumerate(inds))
    finalnullity=Aend.cols-rank(Aend);assert finalnullity==int(c==26)
    P=Aend.row_join(-S.Matrix.hstack(*later))
    (out/'arithmetic-input.json').write_text(json.dumps(dict(P=encode_matrix(P),b=encode_matrix(polynomial)),indent=2)+'\n')
    print('Delayed quadratic samples passed; solving terminal integer families',P.shape,flush=True)
    fam=families(P,polynomial)
    assert fam['families'];tv=fam['families'][0].get('t',fam['families'][0].get('residue'))
    chosen=point_at(fam,tv);values=[int(tv)]+[int(x) for x in chosen[Aend.cols:,0]]
    found=correct(pair_at(values),endaxes,chosen[:Aend.cols,0]);assert m.comm(*found)==target
    hall=description((1,ew),c+ew);kept=len(m.hall)
    assert [(h['weight'],h['pair']) for h in hall[:kept]]==[(h['weight'],h['pair']) for h in m.hall]
    boundaries=[i for i,h in enumerate(hall) if h['weight']>c and h['pair'] and all(j<kept for j in h['pair'])]
    data=dict(weights=[1,ew],p=p,q=q,t=t,class_bound=c,exceptions=exceptions,block_kernel_offsets=blockexceptions,universal_offsets=[9,11,13],
        retained=kept,hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in hall],boundaries=boundaries,
        base=[terms(m.collect(x)) for x in base],target=terms(m.collect(target)),known_pair=[terms(m.collect(x)) for x in known],
        found_pair=[terms(m.collect(x)) for x in found],block_axes=blockaxes,end_axes=endaxes,low_rows=lowrows,end_rows=endrows,
        A=encode_matrix(A),rhs=encode_matrix(rhs),H=encode_matrix(H),U=encode_matrix(U),point=[int(x) for x in point],
        kernel=encode_matrix(K),change=encode_matrix(change),J=encode_matrix(J),first_rows=firstrows,steps=steps,
        polynomial=encode_matrix(polynomial),later_columns=encode_matrix(S.Matrix.hstack(*later)),Aend=encode_matrix(Aend),
        final_kernel_dimension=finalnullity,samples=samples,joint_vectors=[planted,control],families=fam,
        witness=dict(parameters=values,corrections=[int(x) for x in chosen[:Aend.cols,0]]),
        later_column_cokernel_rank=rank(Aend.row_join(S.Matrix.hstack(*later)))-rank(Aend),seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8DelayedQuadratic := '+gap_value(data)+';\n')
    (out/'families.g').write_text('N8PolynomialFamilies := '+gap_value([fam])+';\n')
    (out/'arithmetic.g').write_text('ParametricIntegerFixtures := '+gap_value([dict(fam['certificate'],name='delayed_quadratic_block',sample_parameters=list(range(-20,21)))])+';\n')
    print('PASS N8 delayed quadratic: class',c,'block rank',r,'terminal kernel',finalnullity,'families',len(fam['families']),flush=True)
    faulthandler.cancel_dump_traceback_later();diagnostic.close()

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--class-bound',type=int,choices=[25,26],required=True)
    ap.add_argument('--output',type=Path,required=True);main(ap.parse_args())
