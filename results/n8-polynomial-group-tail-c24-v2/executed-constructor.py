#!/usr/bin/env python3
"""A nonlinear one-parameter group family with the full remaining tail.

This tests the tail reduction, not a surviving B!=0 normalized branch.
Early zero rows remain in the polynomial system and fix the parameter.
"""
import argparse,json,time,faulthandler
from pathlib import Path
from fractions import Fraction as Q
import sympy as S
from flint import fmpz_mat
from check_n8_parametric_tail import Group as OriginalGroup,terms,rat
from n8_weighted_automorphisms import add,scale
from n8_component_hnf import hermite
from parametric_integer_linear import (T,integer_solve,integer_roots,encode_matrix,
                                      encode_poly,gap_value)

class Group(OriginalGroup):
    """Same rational tensor product; omit impossible weight pairs early."""
    def mul(self,a,b):
        buckets={}
        for v,y in b.items():buckets.setdefault(self.weight(v),[]).append((v,y))
        ordered=sorted(buckets.items());out={}
        for u,x in a.items():
            remaining=self.degree-self.weight(u)
            for weight,terms_ in ordered:
                if weight>remaining:break
                for v,y in terms_:
                    w=u+v;out[w]=out.get(w,0)+x*y
        return {w:x for w,x in out.items() if x}

    def collect(self,value,start=1):
        if 2*start<=self.degree:return super().collect(value,start)
        # Here every product of two augmentation tails has excessive
        # weight. Hall division is exactly subtraction of h_i-1.
        residual=add(value,self.one,-1);answer=[]
        assert all(self.weight(w)>=start for w in residual)
        for d in range(start,self.degree+1):
            inds,basis=self.layers[d]
            coordinates=basis.coordinates(self.layer(residual,d))
            for j,coefficient in sorted(coordinates.items()):
                i=inds[j];answer.append((i,coefficient))
                residual=add(residual,add(self.group_hall(i),self.one,-1),-coefficient)
        assert not residual,('Linear collection residual',residual)
        return answer

def hall_description(c):
    """Only the combinatorial Hall words are needed beyond the class bound."""
    hall=[dict(weight=w,pair=None) for w in (1,4)]
    for d in range(1,c+1):
        pending=[]
        for i,a in enumerate(hall):
            for j,b in enumerate(hall[:i]):
                if a['weight']+b['weight']!=d:continue
                if a['pair'] is not None and a['pair'][1]>j:continue
                pending.append(dict(weight=d,pair=(i,j)))
        hall.extend(pending)
    return hall

def main(args):
    begin=time.monotonic();c=args.class_bound;p,q,t,s=1,10,3,7;d=p+q
    assert 2*s>c-d and 2*(d+t)>c
    out=args.output;out.mkdir(parents=True,exist_ok=False)
    diagnostic=(out/'diagnostic-stacks.log').open('w')
    faulthandler.dump_traceback_later(90,repeat=True,file=diagnostic)
    m=Group(1,4,c);a,e=m.letters;D=e
    print('weighted tensor model constructed',len(m.hall),'Hall coordinates',flush=True)
    for _ in range(6):D=m.bracket(a,D)
    di=next(i for i,h in enumerate(m.hall) if h['lie']==D)
    base=(m.power(m.group_hall(0),2),m.power(m.group_hall(di),3))
    C,DD=scale(a,2),scale(D,3)
    def axes(off):return [(side,i) for side,w in enumerate((p,q)) for i in m.layers[w+off][0]]
    def linear(off):
        inds,basis=m.layers[d+off]
        polys=[m.bracket(m.hall[i]['lie'],DD) if side==0 else m.bracket(C,m.hall[i]['lie']) for side,i in axes(off)]
        columns=[basis.coordinates(poly) for poly in polys]
        return S.Matrix(len(inds),len(columns),lambda i,j:rat(columns[j].get(i,Q(0))))
    layers=[]
    for off,exponent in [(3,T),(5,T*T)]:
        A=linear(off);K=integer_solve(A,S.zeros(A.rows,1))[1]
        assert K.cols==1
        layers.append(dict(offset=off,axes=axes(off),kernel=[int(x) for x in K],exponent=encode_poly(exponent)))
    assert linear(7).cols-linear(7).rank()==1
    def correct(pair,ax,vec):
        pair=list(pair)
        for (side,i),v in zip(ax,vec):
            assert S.sympify(v).is_Integer
            if v:pair[side]=m.mul(pair[side],m.power(m.group_hall(i),int(v)))
        return pair
    def family(value):
        pair=base
        for row in layers:
            exponent=value if row['offset']==3 else value*value
            pair=correct(pair,row['axes'],[exponent*v for v in row['kernel']])
        return pair
    tailaxes=[(side,i) for side,w in enumerate((p,q)) for i,h in enumerate(m.hall)
              if w+s<=h['weight']<=c-[q,p][side]]
    rows=[i for i,h in enumerate(m.hall) if h['weight']>=d+t]
    def coords(g):
        data=dict(m.collect(g,d+t));assert all(v.denominator==1 for v in data.values())
        return [rat(data.get(i,Q(0))) for i in rows]
    def relative(g,h):return m.mul(m.inv(g),h)
    planted=[j%3-1 for j in range(len(tailaxes))];known=correct(family(2),tailaxes,planted);target=m.comm(*known)
    rho=max(Q(1 if row['offset']==3 else 2,m.hall[i]['weight'])
            for row in layers for (side,i),v in zip(row['axes'],row['kernel']) if v)
    degree=(c*rho.numerator)//rho.denominator
    mats=[];rhs=[];joint_vectors=[planted,[2-j%5 for j in range(len(tailaxes))]]
    print('group class',c,'Hall rank',len(m.hall),'tail axes',len(tailaxes),'rho',rho,'degree',degree,flush=True)
    for value in range(degree+1):
        pair=family(value);comm=m.comm(*pair)
        if value==0:
            assert m.mul(*pair)==OriginalGroup.mul(m,*pair)
        rhs.append(coords(relative(comm,target)))
        aa,bb=add(pair[0],m.one,-1),add(pair[1],m.one,-1)
        cc=add(comm,m.one,-1);ix,iy=m.inv(pair[0]),m.inv(pair[1]);columns=[]
        for side,i in tailaxes:
            w=m.hall[i]['weight'];v=add(m.group_hall(i),m.one,-1)
            assert 2*d+w>c and d+2*w>c
            conjugation=m.bracket(cc,v)
            if side==0:
                assert 2*w+q>c
                delta=m.mul(iy,m.bracket(v,bb));low=w+q
            else:
                assert p+2*w>c and p+w+2*d>c
                delta=m.mul(ix,m.bracket(aa,v));low=p+w
                delta=add(delta,m.bracket(delta,cc))
            assert 2*low>c
            columns.append(coords(add(m.one,add(delta,conjugation))))
        mat=S.Matrix(len(rows),len(tailaxes),lambda i,j:columns[j][i]);mats.append(mat)
        for vec in joint_vectors:
            actual=coords(relative(comm,m.comm(*correct(pair,tailaxes,vec))))
            assert S.Matrix(actual)==mat*S.Matrix(vec)
        print('sample',value,'checked',len(columns),'columns and 2 joint vectors',flush=True)
    P=S.Matrix(len(rows),len(tailaxes),lambda i,j:S.interpolate([(v,mats[v][i,j]) for v in range(degree+1)],T))
    b=S.Matrix(len(rows),1,lambda i,j:S.interpolate([(v,rhs[v][i]) for v in range(degree+1)],T))
    critical=next(i for i in range(P.rows) if all(x==0 for x in P[i,:]) and b[i]!=0)
    candidates=integer_roots(b[critical]);decisions=[]
    for value in candidates:
        A,bb=P.subs(T,value),b.subs(T,value)
        assert all(x.is_Integer for x in list(A)+list(bb))
        ans=integer_solve(A,bb)
        row=dict(t=value,witness=None if ans is None else [int(x) for x in ans[0]])
        if ans is not None:
            H,U=hermite(fmpz_mat([[int(x) for x in r] for r in A.T.tolist()]))
            H,U=S.Matrix(H.tolist()),S.Matrix(U.tolist());rank=A.rank()
            assert ans[1]==U[rank:,:].T
            row.update(H=encode_matrix(H),U=encode_matrix(U),kernel=encode_matrix(ans[1]),rank=rank)
        decisions.append(row)
    win=next(row for row in decisions if row['witness'] is not None)
    found=correct(family(win['t']),tailaxes,win['witness']);assert m.comm(*found)==target
    allhall=hall_description(c+4);kept=len(m.hall)
    assert allhall[:kept]==[{k:h[k] for k in ('weight','pair')} for h in m.hall]
    boundaries=[i for i,h in enumerate(allhall) if h['weight']>c and h['pair'] is not None and all(j<kept for j in h['pair'])]
    record=dict(class_bound=c,p=p,q=q,t=t,tail_offset=s,weights=[1,4],retained=kept,
      hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in allhall],boundaries=boundaries,
      base=[terms(m.collect(g)) for g in base],family_layers=layers,tail_axes=tailaxes,rows=rows,
      target=terms(m.collect(target)),known_pair=[terms(m.collect(g)) for g in known],found_pair=[terms(m.collect(g)) for g in found],
      rho=[rho.numerator,rho.denominator],degree_bound=degree,sample_values=list(range(degree+1)),joint_vectors=joint_vectors,
      P=encode_matrix(P),b=encode_matrix(b),critical_row=critical,integer_candidates=candidates,decisions=decisions,witness=win,
      family_status='Arbitrary nonlinear polynomial family; early compatibility retained as zero rows, not a surviving absorbed branch',seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8PolynomialGroupTail := '+gap_value(record)+';\n')
    print('PASS N8 polynomial group tail: class',c,'matrix',P.shape,'degree bound',degree,'complete candidates',candidates,flush=True)
    faulthandler.cancel_dump_traceback_later();diagnostic.close()

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--class-bound',type=int,default=21)
    ap.add_argument('--output',type=Path,required=True);main(ap.parse_args())
