#!/usr/bin/env python3
"""Candidate all-rank class-seven commutator algorithm; see class7-proof.md."""
from math import isqrt,lcm
from sympy import Matrix,Rational,floor
from flint import fmpz_mat
from n8_class3 import smith
from n8_class6 import (Magnus,ONE,correction,apply,finished,mixed_candidates,
                       equal_candidates,decide_penultimate,
                       decide_nonzero_degree_two)
from n8_ia_orbits import add,affine_solve
from n8_central import bracket
from n8_flint_linear import linear_solution


def short_particular(result):
    """Reduce a particular solution modulo its full integral kernel.

    Smith transformations can return huge but valid coefficients. Exact
    nearest-plane reduction changes neither the equations nor completeness.
    """
    vector,kernel=result
    if not kernel:return vector
    raw=fmpz_mat(kernel)
    reduced,transform=raw.lll(transform=True,delta=0.75)
    assert reduced==transform*raw and abs(transform.det())==1
    basis=Matrix([[int(reduced[i,j]) for j in range(reduced.ncols())]
                  for i in range(reduced.nrows())])
    orthogonal=[]
    for i in range(basis.rows):
        v=basis.row(i)
        for u in orthogonal:v=v-v.dot(u)/u.dot(u)*u
        orthogonal.append(v)
    answer=Matrix([vector])
    for i in reversed(range(basis.rows)):
        u=orthogonal[i]
        n=floor(answer.dot(u)/u.dot(u)+Rational(1,2))
        answer=answer-n*basis.row(i)
    return list(map(int,answer))


def integer_roots(coefficients):
    """All integer roots of nonzero a+b*k+c*binomial(k,2)."""
    a,b,c=coefficients
    aa,bb,cc=c,2*b-c,2*a
    if not aa:
        if not bb:return []
        return [-cc//bb] if cc%bb==0 else []
    disc=bb*bb-4*aa*cc
    if disc<0:return []
    root=isqrt(disc)
    if root*root!=disc:return []
    return sorted({n//(2*aa) for n in (-bb-root,-bb+root) if n%(2*aa)==0})


def polynomial_lattice(columns,coefficients):
    """Find k with a+b*k+c*binomial(k,2) in the integral column lattice.

    Returns k (or None) and an exact normal-form/candidate certificate.
    coefficients is a list of three coordinate vectors in Newton order.
    """
    a=Matrix.hstack(*(Matrix(v) for v in columns))
    d,s,t=smith(a)
    transformed=s*Matrix.hstack(*(Matrix(v) for v in coefficients))
    rank=sum(bool(d[i,i]) for i in range(min(d.shape)))
    free=[list(map(int,transformed.row(i))) for i in range(rank,a.rows)]
    equation=next((v for v in free if any(v)),None)
    period=None
    if equation is not None:
        candidates=integer_roots(equation)
        mode='integer_roots'
    else:
        period=2*lcm(*(abs(int(d[i,i])) for i in range(rank)))
        candidates=range(period)
        mode='finite_residues'
    chosen=None
    for k in candidates:
        rhs=transformed*Matrix([1,k,k*(k-1)//2])
        if all(rhs[i]%d[i,i]==0 for i in range(rank)) and not any(rhs[rank:]):
            chosen=k;break
    data=dict(matrix=[list(map(int,a.row(i))) for i in range(a.rows)],
              D=[list(map(int,d.row(i))) for i in range(d.rows)],
              S=[list(map(int,s.row(i))) for i in range(s.rows)],
              T=[list(map(int,t.row(i))) for i in range(t.rows)],
              coefficients=coefficients,rank=rank,mode=mode,
              equation=equation,period=period,
              candidates=list(candidates) if equation is not None else None,
              chosen=chosen)
    return chosen,data


def tail_axes(m,p,q,start):
    return [(side,h) for side,low,high in ((0,p+start,m.degree-q),(1,q+start,m.degree-p))
            for degree in range(low,high+1) for h in m.bydegree[degree]]


def apply_tail(m,x,y,axes,vector):
    pair=[x,y]
    for (side,h),n in zip(axes,vector):
        pair[side]=m.mul(pair[side],m.power(h['value'],n))
    return pair


def tail_columns(m,x,y,axes):
    base=m.comm(x,y);columns=[]
    for side,h in axes:
        pair=[x,y];pair[side]=m.mul(pair[side],h['value'])
        columns.append(add(m.mul(m.inv(base),m.comm(*pair)),ONE,-1))
    return columns


def tail(m,g,x,y,p,q,start,audit=None):
    """Joint linear tail: only called under the weight bounds in the proof."""
    axes=tail_axes(m,p,q,start)
    columns=tail_columns(m,x,y,axes)
    rhs=add(m.mul(m.inv(m.comm(x,y)),g),ONE,-1)
    result=linear_solution(columns,rhs)
    if audit is not None:
        audit.append(dict(kind='tail',degree=m.degree,x=m.collect(x)[0],y=m.collect(y)[0],
                          axes=[[side,h['word']] for side,h in axes],soluble=result is not None))
    if result is None:return None
    pair=apply_tail(m,x,y,axes,short_particular(result))
    assert m.comm(*pair)==g
    return pair


def first(m,g,x,y,p,q,j,audit):
    degree=p+q+j
    residual=m.mul(m.inv(m.comm(x,y)),g)
    assert all(not (0<len(w)<degree) for w in residual)
    c,d=m.layer(x,p),m.layer(y,q)
    columns=([bracket(m,m.layer(h['value'],p+j),d) for h in m.bydegree[p+j]]
             +[bracket(m,c,m.layer(h['value'],q+j)) for h in m.bydegree[q+j]])
    result=linear_solution(columns,m.layer(residual,degree))
    old=[[degree,m.collect(x)[0],m.collect(y)[0],
          [h['word'] for h in m.bydegree[p+j]],
          [h['word'] for h in m.bydegree[q+j]],result is not None]]
    if audit is not None:
        for degree,xw,yw,u,v,soluble in old:
            audit.append(dict(kind='layer',degree=degree,x=xw,y=yw,
                              axes=[[0,w] for w in u]+[[1,w] for w in v],soluble=soluble))
    return result


def nielsen_choices(vector,kernel,dd,second_dimension):
    assert len(kernel)==1
    primitive=kernel[0];gauge=dd+[0]*second_dimension
    pivot=next(i for i,n in enumerate(primitive) if n)
    assert gauge[pivot]%primitive[pivot]==0
    period=gauge[pivot]//primitive[pivot]
    assert period and all(a==period*b for a,b in zip(gauge,primitive))
    return [[a+k*b for a,b in zip(vector,primitive)] for k in range(abs(period))]


def quadratic_finish(m,g,x0,y0,vector,kernel,record,audit):
    assert len(kernel)<=1
    if not kernel:
        x,y=apply(m,x0,y0,1,4,1,vector)
        return tail(m,g,x,y,1,4,2,audit)
    direction=kernel[0]
    def pair(k):return apply(m,x0,y0,1,4,1,[a+k*b for a,b in zip(vector,direction)])
    def residual(k):
        x,y=pair(k)
        delta=m.mul(m.inv(m.comm(x,y)),g)
        assert all(len(w) in (0,7) for w in delta)
        return m.coordinates(m.layer(delta,7),7)
    samples=[residual(k) for k in (0,1,2)]
    coefficients=[samples[0],
                  [b-a for a,b in zip(samples[0],samples[1])],
                  [c-2*b+a for a,b,c in zip(*samples)]]
    for k in (-2,-1,3):
        assert residual(k)==[a+k*b+k*(k-1)//2*c for a,b,c in zip(*coefficients)]
    x,y=pair(0);axes=tail_axes(m,1,4,2)
    columns=tail_columns(m,x,y,axes)
    assert all(all(len(w)==7 for w in column) for column in columns)
    for k in (-1,2):assert tail_columns(m,*pair(k),axes)==columns
    coordinates=[m.coordinates(column,7) for column in columns]
    k,certificate=polynomial_lattice(coordinates,coefficients)
    record['quadratic']=certificate
    if audit is not None:
        audit.append(dict(kind='quadratic',degree=7,x0=m.collect(x0)[0],y0=m.collect(y0)[0],
                          vector=vector,kernel=direction,
                          u=[h['word'] for h in m.bydegree[2]],
                          v=[h['word'] for h in m.bydegree[5]],
                          axes=[[side,h['word']] for side,h in axes],
                          samples=[[j,*[m.collect(z)[0] for z in pair(j)]] for j in (-2,-1,0,1,2,3)],
                          certificate=certificate))
    if k is None:return None
    return tail(m,g,*pair(k),1,4,2,audit)


def decide_class7(m,word,audit=None):
    assert m.rank>=2 and m.degree==7
    g=m.expansion(word)
    if g==ONE:return dict(answer=True,x=[],y=[],trace=[],case='identity')
    leading=min(len(w) for w in g if w)
    if leading==1:return dict(answer=False,trace=[],case='abelian_obstruction')
    if leading==2:return decide_nonzero_degree_two(m,word)
    if leading>=6:return decide_penultimate(m,word)
    trace=[];w=m.layer(g,leading)
    for p in range(1,leading//2+1):
        q=leading-p
        pairs=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
        for branch,(cc,dd) in enumerate(pairs):
            x0,y0=m.lift(cc,p),m.lift(dd,q)
            step=first(m,g,x0,y0,p,q,1,audit)
            record=dict(p=p,q=q,branch=branch,C=cc,D=dd,first_soluble=step is not None)
            trace.append(record)
            if step is None:continue
            vector,kernel=step;record['kernel_dimension']=len(kernel)
            pair=None
            if leading==5 and p==1:
                pair=quadratic_finish(m,g,x0,y0,vector,kernel,record,audit)
            elif leading==4:
                assert not kernel
                pair=tail(m,g,*apply(m,x0,y0,p,q,1,vector),p,q,2,audit)
            else:
                assert (p,q) in ((1,2),(2,3))
                choices=nielsen_choices(vector,kernel,dd,len(m.bydegree[q+1]))
                record['period']=len(choices)
                for residue,choice in enumerate(choices):
                    x,y=apply(m,x0,y0,p,q,1,choice)
                    if leading==3:
                        second=first(m,g,x,y,p,q,2,audit)
                        if second is None:continue
                        assert not second[1]
                        x,y=apply(m,x,y,p,q,2,second[0])
                    pair=tail(m,g,x,y,p,q,3 if leading==3 else 2,audit)
                    if pair is not None:
                        record['selected_residue']=residue;break
            if pair is not None:return finished(m,g,*pair,trace,'class7_middle')
    return dict(answer=False,trace=trace,case='all_middle_branches_failed')
