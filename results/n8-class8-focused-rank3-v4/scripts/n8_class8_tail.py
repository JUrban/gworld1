#!/usr/bin/env python3
"""Exact joint-tail solve using injective Hall pivot rows of the Magnus series.

For 2*low>class, gamma_low is additive in the truncated augmentation ideal.
It has basis h-1 for Hall group generators h of weights >=low. The selected
leading Hall pivot rows in each degree form an injective block-triangular
projection of this rational span. Projecting both sides therefore preserves
the full integer solution set, without assuming a saturated image lattice.
"""
from n8_class7 import ONE,tail_axes,tail_columns,apply_tail,short_particular
from n8_ia_orbits import add
from n8_flint_linear import affine_solution


def tail(m,g,x,y,p,q,start,audit=None):
    axes=tail_axes(m,p,q,start)
    columns=tail_columns(m,x,y,axes)
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
    # Verify the positive solution in every original tensor coordinate too.
    check={}
    for n,column in zip(vector,columns):check=add(check,column,n)
    assert check==rhs
    pair=apply_tail(m,x,y,axes,vector)
    assert m.comm(*pair)==g
    return pair
