#!/usr/bin/env python3
"""Complete two-exception linear blocks and their first quadratic, in groups.

Weighted fixtures only; this is not ambient leading-pair enumeration or a
general all-class N8 decision implementation. All arithmetic is exact.
"""
from pathlib import Path
import argparse,json,time
from fractions import Fraction as Q
import sympy as S
from flint import fmpz_mat
from check_n8_parametric_tail import Group,terms,rat
from n8_weighted_automorphisms import add,scale
from n8_component_hnf import hermite
from n8_polynomial_families import families,point_at
from parametric_integer_linear import T,integer_solve,encode_matrix,gap_value

def main(args):
    begin=time.monotonic();p=1;q=args.e_weight+4;t=args.e_weight-1;later=t+2
    d=p+q;c=d+2*t
    assert later<2*t
    out=args.output;out.mkdir(parents=True,exist_ok=False)
    m=Group(1,args.e_weight,c);a,e=m.letters;D=e
    for _ in range(4):D=m.bracket(a,D)
    di=next(i for i,h in enumerate(m.hall) if h['lie']==D)
    base=(m.power(m.group_hall(0),2),m.power(m.group_hall(di),3))
    def axes(s):
        return [(side,i) for side,w in enumerate((p,q)) for i in m.layers[w+s][0]]
    blockaxes=[h for s in range(t,2*t) for h in axes(s)]
    endaxes=axes(2*t)
    def correct(pair,ax,vec):
        pair=list(pair)
        for (side,i),z in zip(ax,vec):
            assert S.sympify(z).is_Integer
            if z:pair[side]=m.mul(pair[side],m.power(m.group_hall(i),int(z)))
        return pair
    def relative(x,y):return m.mul(m.inv(x),y)
    def fullcoords(x,start):
        data=dict(m.collect(x,start));assert all(v.denominator==1 for v in data.values())
        return data
    comm0=m.comm(*base)
    lowrows=[i for i,h in enumerate(m.hall) if d+t<=h['weight']<c]
    endrows=m.layers[c][0]
    def vector(data,rows):return S.Matrix([rat(data.get(i,Q(0))) for i in rows])
    columns=[]
    for j in range(len(blockaxes)):
        z=[int(j==k) for k in range(len(blockaxes))]
        pair=correct(base,blockaxes,z)
        columns.append(vector(fullcoords(relative(comm0,m.comm(*pair)),d+t),lowrows))
    A=S.Matrix.hstack(*columns)
    planted=[(j%4)-1 for j in range(len(blockaxes))]
    known=correct(base,blockaxes,planted);target=m.comm(*known)
    rhs=vector(fullcoords(relative(comm0,target),d+t),lowrows)
    sol=integer_solve(A,rhs);assert sol is not None
    point,K=sol
    assert K.cols==2,('Expected both surviving exceptions',args.e_weight,A.shape,K.shape)
    first=next(j for j,(side,i) in enumerate(blockaxes) if side==0 and m.hall[i]['weight']==p+t)
    ka,kb=K[first,0],K[first,1];u,v,g=S.gcdex(ka,kb)
    assert g>0 and u*ka+v*kb==g
    change=S.Matrix([[u,-kb/g],[v,ka/g]])
    assert change.det()==1
    J=K*change;assert J[first,0]==g and J[first,1]==0
    assert all(not J[j,1] for j,(side,i) in enumerate(blockaxes) if m.hall[i]['weight']<[p,q][side]+later)
    H,U=hermite(fmpz_mat([[int(x) for x in row] for row in A.T.tolist()]))
    H,U=S.Matrix(H.tolist()),S.Matrix(U.tolist())
    assert K==U[A.rank():,:].T
    print('block',args.e_weight,'class',c,'shape',A.shape,'rank',A.rank(),'parameter step',g,flush=True)
    def pair_at(z,s):return correct(base,blockaxes,point+z*J[:,0]+s*J[:,1])
    def residual(z,s):
        pair=pair_at(z,s);r=relative(m.comm(*pair),target)
        data=fullcoords(r,d+t)
        assert all(not data.get(i,0) for i in lowrows)
        return vector(data,endrows)
    v00,v10,v20,v01=[residual(*zs) for zs in [(0,0),(1,0),(2,0),(0,1)]]
    q2=(v20-2*v10+v00)/2;q1=v10-v00-q2;B=v01-v00
    polynomial=(v00+q1*T+q2*T*T).applyfunc(S.expand)
    samples=[[0,0],[1,0],[2,0],[0,1],[1,1],[-2,3]]
    for z,s in samples:assert residual(z,s)==polynomial.subs(T,z)+s*B
    C=scale(a,2);DD=scale(D,3)
    LieBasis=m.layers[c][1]
    def lie_vector(x):
        data=LieBasis.coordinates(x)
        return S.Matrix(len(endrows),1,lambda i,j:rat(data.get(i,Q(0))))
    Aend=S.Matrix.hstack(*(lie_vector(m.bracket(m.hall[i]['lie'],DD) if side==0 else m.bracket(C,m.hall[i]['lie'])) for side,i in endaxes))
    assert Aend.row_join(q2).rank()==Aend.rank()+1
    # The residual is target/[current commutator]; end corrections must
    # equal polynomial(T)+S*B, so unknowns (end corrections,S) solve this.
    P=Aend.row_join(-B);fam=families(P,polynomial)
    assert fam['families'],'Planted target lost'
    tv=(fam['families'][0]['t'] if fam['mode']=='finite' else fam['families'][0]['residue'])
    chosen=point_at(fam,tv);sv=int(chosen[-1]);found=correct(pair_at(tv,sv),endaxes,chosen[:-1,0])
    assert m.comm(*found)==target
    finalnullity=Aend.cols-Aend.rank()
    assert finalnullity==int(2*t==q-p)
    nielsen=None
    if finalnullity:
        idx=next(j for j,h in enumerate(endaxes) if h==[0,di] or h==(0,di))
        ker=integer_solve(Aend,S.zeros(Aend.rows,1))[1]
        assert ker.cols==1 and abs(ker[idx,0])==1
        for k in [-2,-1,1,2]:
            changed=[m.mul(m.power(base[1],k),base[0]),base[1]]
            assert m.comm(*changed)==comm0
        nielsen=dict(axis=idx,hall_index=di,period=3,residues=[0,1,2],powers=[-2,-1,1,2])
    allhall=Group(1,args.e_weight,c+args.e_weight).hall;kept=len(m.hall)
    assert allhall[:kept]==m.hall
    boundaries=[i for i,h in enumerate(allhall) if h['weight']>c and h['pair'] is not None and all(j<kept for j in h['pair'])]
    record=dict(weights=[1,args.e_weight],p=p,q=q,t=t,later=later,class_bound=c,
       retained=kept,hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in allhall],boundaries=boundaries,
       base=[terms(m.collect(x)) for x in base],target=terms(m.collect(target)),known_pair=[terms(m.collect(x)) for x in known],
       found_pair=[terms(m.collect(x)) for x in found],block_axes=blockaxes,end_axes=endaxes,
       low_rows=lowrows,end_rows=endrows,A=encode_matrix(A),rhs=encode_matrix(rhs),H=encode_matrix(H),U=encode_matrix(U),
       point=[int(x) for x in point],kernel=encode_matrix(K),change=encode_matrix(change),J=encode_matrix(J),first_axis=first,
       parameter_step=int(g),polynomial=encode_matrix(polynomial),B=encode_matrix(B),Aend=encode_matrix(Aend),
       samples=samples,families=fam,witness=dict(t=int(tv),s=sv,corrections=[int(x) for x in chosen[:-1,0]]),nielsen=nielsen,
       obstruction_B_nonzero_mod_image=Aend.row_join(B).rank()>Aend.rank(),seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8TwoExceptionBlock := '+gap_value(record)+';\n')
    (out/'families.g').write_text('N8PolynomialFamilies := '+gap_value([fam])+';\n')
    arith=dict(fam['certificate'],name='complete_block_end',sample_parameters=list(range(-20,21)))
    (out/'arithmetic.g').write_text('ParametricIntegerFixtures := '+gap_value([arith])+';\n')
    print('PASS N8 two-exception block: class',c,'full block',A.shape,'six polynomial samples;',len(fam['families']),'complete parameter families; Nielsen',nielsen is not None,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--e-weight',type=int,choices=[4,5],required=True)
    ap.add_argument('--output',type=Path,required=True);main(ap.parse_args())
