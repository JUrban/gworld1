#!/usr/bin/env python3
"""Exact weighted-group overlap fixtures, not the full ambient N8 algorithm.

The polynomial degree bound is proved from weight: every occurrence of T
starts in weight p+t, so degree <= floor(c/(p+t)). Tail relative group
elements have weight >= d+t and twice that is above c; Hall collection is
linear there. Complete integer parameter decisions use the separate solver.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import sympy as S
from n8_universal_gauges import WeightedTensor
from n8_weighted_automorphisms import add,scale
from parametric_integer_linear import T,integer_solve,solve,encode_matrix,gap_value

class Group(WeightedTensor):
    def inv(self,g):
        a=add(g,self.one,-1);ans=dict(self.one);term=dict(self.one)
        for k in range(1,self.degree+1):
            term=self.mul(term,a)
            if not term:break
            ans=add(ans,term,(-1)**k)
        return ans

def rat(x):return S.Rational(x.numerator,x.denominator)
def terms(v):return [[int(i),int(x)] for i,x in v if x]

def main(args):
    begin=time.monotonic();c=args.class_bound;p,q,t=1,8,3;d=p+q;s=t+2
    assert d+2*s>c and 2*(d+t)>c
    m=Group(1,4,c);out=args.output;out.mkdir(parents=True,exist_ok=False)
    a,e=m.letters;D=e
    for _ in range(4):D=m.bracket(a,D)
    # Choose an actual integral group lift with pure logarithm a multiple
    # of D. Its Hall coordinate polynomials have degree <= floor(c/q).
    ysamples=[dict(m.collect(m.exp(scale(D,k)))) for k in range(c//q+1)]
    ypolys=[S.interpolate([(k,rat(row.get(i,Q(0)))) for k,row in enumerate(ysamples)],T)
            for i in range(len(m.hall))]
    yscale=lcm(1,*(int(v.q) for poly in ypolys for v in S.Poly(poly,T).all_coeffs()))
    ycoords=[(i,Q(poly.subs(T,yscale))) for i,poly in enumerate(ypolys) if poly]
    assert all(x.denominator==1 for _,x in ycoords)
    x0=m.power(m.group_hall(0),args.x_scale);y0=m.from_hall(ycoords)
    assert m.log(y0)==scale(D,yscale)
    C=scale(a,args.x_scale);D=scale(D,yscale)
    print('weighted group',c,'Hall rank',len(m.hall),'pure-log scale',yscale,flush=True)

    def axes(offset):
        return [(side,i) for side,weight in enumerate((p,q))
                for i in m.layers[weight+offset][0]]
    def correction(pair,ax,vec):
        answer=list(pair)
        for (side,i),n in zip(ax,vec):
            if n:answer[side]=m.mul(answer[side],m.power(m.group_hall(i),int(n)))
        return answer
    def lievec(poly,degree):
        inds,B=m.layers[degree];coords=B.coordinates(m.layer(poly,degree))
        return S.Matrix(len(inds),1,lambda j,k:rat(coords.get(j,Q(0))))
    def linear(offset):
        cols=[m.bracket(m.hall[i]['lie'],D) if side==0 else m.bracket(C,m.hall[i]['lie'])
              for side,i in axes(offset)]
        return S.Matrix.hstack(*(lievec(v,d+offset) for v in cols))
    ax3,ax4=axes(t),axes(t+1);A3,A4=linear(t),linear(t+1)
    ans3=integer_solve(A3,S.zeros(A3.rows,1));K3=ans3[1]
    assert K3.cols==1 and A4.rank()==A4.cols
    v3=S.zeros(K3.rows,1);K3=K3[:,0]
    tailaxes=[(side,i) for side,weight in enumerate((p,q))
              for w in range(weight+s,c-(q if side==0 else p)+1)
              for i in m.layers[w][0]]
    knownk=6;known4=[0]*len(ax4);knownz=[(j%3)-1 for j in range(len(tailaxes))]
    known=correction(correction((x0,y0),ax3,knownk*K3),ax4,known4)
    known=correction(known,tailaxes,knownz);g=m.comm(*known)
    comm0=m.comm(x0,y0)
    assert not m.layer(add(g,comm0,-1),d+t)
    pair1=correction((x0,y0),ax3,K3)
    delta=lievec(add(m.comm(*pair1),comm0,-1),d+t+1)
    rhs=lievec(add(g,comm0,-1),d+t+1)
    joint=delta.row_join(A4);line=integer_solve(joint,rhs)
    assert line is not None and line[1].cols==1,('No affine parameter line',joint.shape)
    point,direction=line[0],line[1][:,0]
    if direction[0]<0:direction=-direction
    assert direction[0]!=0
    print('offset3 kernel',len(K3),'offset4 injective',A4.shape,
          'parameter step',direction[0],'tail unknowns',len(tailaxes),flush=True)

    def baseline(value):
        row=point+value*direction
        return correction(correction((x0,y0),ax3,v3+row[0]*K3),ax4,row[1:,0])
    rows=[i for i,h in enumerate(m.hall) if h['weight']>=d+t]
    def coords(value):
        data=dict(m.collect(value,d+t))
        assert all(x.denominator==1 for x in data.values())
        return [rat(data.get(i,Q(0))) for i in rows]
    def relative(base,other):return m.mul(m.inv(base),other)
    degree=c//(p+t);pmats=[];bvecs=[];samplechecks=0
    for value in range(degree+1):
        pair=baseline(value);base=m.comm(*pair)
        bvecs.append(coords(relative(base,g)))
        cols=[]
        for side,i in tailaxes:
            changed=list(pair);changed[side]=m.mul(changed[side],m.group_hall(i))
            cols.append(coords(relative(base,m.comm(*changed))))
        mat=S.Matrix(len(rows),len(tailaxes),lambda i,j:cols[j][i]);pmats.append(mat)
        # Two complete joint vectors test simultaneous positive/negative
        # powers, not only one-coordinate increments.
        for vec in [knownz,[2-j%5 for j in range(len(tailaxes))]]:
            actual=coords(relative(base,m.comm(*correction(pair,tailaxes,vec))))
            assert S.Matrix(actual)==mat*S.Matrix(vec)
            samplechecks+=1
        print('group samples',value,'columns',len(cols),flush=True)
    P=S.Matrix(len(rows),len(tailaxes),lambda i,j:S.interpolate(
        [(v,pmats[v][i,j]) for v in range(degree+1)],T))
    b=S.Matrix(len(rows),1,lambda i,j:S.interpolate(
        [(v,bvecs[v][i]) for v in range(degree+1)],T))
    rec=solve(P,b);assert rec['witness'] is not None
    win=rec['witness'];found=correction(baseline(win['t']),tailaxes,win['witness'])
    assert m.comm(*found)==g
    # A genuine negative instance at this fixed lower-coordinate branch:
    # shift one target Hall coordinate and use the complete arithmetic
    # solver. This bounded search is only fixture selection, not a proof
    # that a negative instance exists or that other leading branches fail.
    negative=None
    for j in range(len(rows)-1,-1,-1):
        bb=b.copy();bb[j]+=1;attempt=solve(P,bb)
        if attempt['witness'] is None:
            negative=dict(row=j,hall_index=rows[j],certificate=attempt);break
    if negative is None:print('No one-coordinate negative control located',flush=True)
    allhall=Group(1,4,c+4).hall;kept=len(m.hall)
    assert allhall[:kept]==m.hall
    boundary=[i for i,h in enumerate(allhall) if h['weight']>c and h['pair'] is not None
              and all(j<kept for j in h['pair'])]
    data=dict(class_bound=c,weights=[1,4],p=p,q=q,t=t,x_scale=args.x_scale,y_scale=yscale,
              hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in allhall],
              retained=kept,boundaries=boundary,base=[terms(m.collect(x0)),terms(ycoords)],
              axes3=ax3,axes4=ax4,axes_tail=tailaxes,rows=rows,
              kernel3=[int(x) for x in K3],point=[int(x) for x in point],
              direction=[int(x) for x in direction],degree_bound=degree,
              P=encode_matrix(P),b=encode_matrix(b),certificate=rec,negative=negative,
              target=terms(m.collect(g)),known_pair=[terms(m.collect(x)) for x in known],
              found_pair=[terms(m.collect(x)) for x in found],sample_values=list(range(degree+1)),
              joint_vectors=[knownz,[2-j%5 for j in range(len(tailaxes))]],
              joint_checks=samplechecks,seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8ParametricTail := '+gap_value(data)+';\n')
    arithmetic=[dict(rec,name='overlap_positive',sample_parameters=list(range(-10,11)))]
    if negative:arithmetic.append(dict(negative['certificate'],name='overlap_negative',sample_parameters=list(range(-10,11))))
    (out/'arithmetic.g').write_text('ParametricIntegerFixtures := '+gap_value(arithmetic)+';\n')
    print('PASS N8 parametric tail: class',c,'parameter step',int(direction[0]),
          'matrix',P.shape,'mode',rec['mode'],'negative',negative is not None,
          'joint controls',samplechecks,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--class-bound',type=int,default=18)
    ap.add_argument('--x-scale',type=int,default=1);ap.add_argument('--output',type=Path,required=True)
    main(ap.parse_args())
