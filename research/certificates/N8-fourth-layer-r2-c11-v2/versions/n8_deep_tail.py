#!/usr/bin/env python3
"""Exact joint tails with component-wise integer Hermite reduction.

For b=[x,y], [xh,y]=b^h[h,y] and [x,yh]=[x,h]b^h.
Under the asserted weights all products of the correction increments vanish
in the truncated augmentation ideal. The remaining columns are computed
directly from associative brackets and the fixed inverses of x and y.
"""
from n8_class7 import ONE,tail_axes,apply_tail,short_particular
from n8_ia_orbits import add
from n8_central import bracket
from n8_component_linear import affine_solution


def tail_columns(m,x,y,axes,p,q):
    d=p+q
    a=add(x,ONE,-1);b=add(y,ONE,-1)
    comm=add(m.comm(x,y),ONE,-1)
    ix=m.inv(x);iy=m.inv(y)
    columns=[]
    for side,h in axes:
        weight=h['weight'];v=add(h['value'],ONE,-1)
        # [base,h]-1 is just its associative bracket in this range.
        assert 2*d+weight>m.degree and d+2*weight>m.degree
        base_change=bracket(m,comm,v)
        if side==0:
            assert 2*weight+q>m.degree
            change=m.mul(iy,bracket(m,v,b))
            low=weight+q
        else:
            assert p+2*weight>m.degree
            change=m.mul(ix,bracket(m,a,v))
            low=p+weight
            # At leading degree three this conjugation contributes in degree ten.
            # Its second iterated commutator is still beyond the truncation.
            assert low+2*d>m.degree
            change=add(change,bracket(m,change,comm))
        assert 2*low>m.degree
        columns.append(add(change,base_change))
    return columns


def tail(m,g,x,y,p,q,start,audit=None):
    s=p+start;t=q+start
    assert 2*s+q>m.degree and p+2*t>m.degree and s+t>m.degree
    if m.comm(x,y)==g:
        if audit is not None:
            audit.append(dict(kind='tail',degree=m.degree,x=m.collect(x)[0],y=m.collect(y)[0],
                              axes=[],soluble=True))
        return x,y
    axes=tail_axes(m,p,q,start)
    columns=tail_columns(m,x,y,axes,p,q)
    rhs=add(m.mul(m.inv(m.comm(x,y)),g),ONE,-1)
    low=p+q+start
    assert 2*low>m.degree
    assert all(len(w)>=low for row in columns+[rhs] for w in row)
    selected=[]
    for degree in range(low,m.degree+1):
        words,rows,_,_=m.projections[degree]
        selected.extend(words[i] for i in rows)
    result=affine_solution([[row.get(w,0) for w in selected] for row in columns],
                           [rhs.get(w,0) for w in selected])
    if audit is not None:
        audit.append(dict(kind='tail',degree=m.degree,x=m.collect(x)[0],y=m.collect(y)[0],
                          axes=[[side,h['word']] for side,h in axes],soluble=result is not None))
    if result is None:return None
    vector=short_particular(result)
    total={}
    for n,column in zip(vector,columns):
        if n:total=add(total,column,n)
    assert total==rhs
    pair=apply_tail(m,x,y,axes,vector)
    assert m.comm(*pair)==g
    return pair
