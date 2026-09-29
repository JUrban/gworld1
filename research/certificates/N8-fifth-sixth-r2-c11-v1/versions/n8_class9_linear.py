#!/usr/bin/env python3
"""The same homogeneous correction, in verified integral Hall coordinates."""
from n8_central import bracket
from n8_component_linear import affine_solution


def first(m,g,x,y,p,q,j,audit):
    degree=p+q+j
    residual=m.mul(m.inv(m.comm(x,y)),g)
    assert all(not (0<len(w)<degree) for w in residual)
    c,d=m.layer(x,p),m.layer(y,q)
    columns=([bracket(m,m.layer(h['value'],p+j),d) for h in m.bydegree[p+j]]
             +[bracket(m,c,m.layer(h['value'],q+j)) for h in m.bydegree[q+j]])
    result=affine_solution([m.coordinates(col,degree) for col in columns],
                           m.coordinates(m.layer(residual,degree),degree))
    if audit is not None:
        audit.append(dict(kind='layer',degree=degree,x=m.collect(x)[0],y=m.collect(y)[0],
                          axes=([(0,h['word']) for h in m.bydegree[p+j]]
                                +[(1,h['word']) for h in m.bydegree[q+j]]),
                          soluble=result is not None))
    return result
