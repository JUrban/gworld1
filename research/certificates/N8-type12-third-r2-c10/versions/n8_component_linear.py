#!/usr/bin/env python3
"""Exact integral affine solution with a verified component Hermite form."""
from flint import fmpz_mat
from n8_component_hnf import hermite


def affine_solution(columns,rhs):
    if not columns:return ([],[]) if not any(rhs) else None
    if not rhs:
        n=len(columns)
        return [0]*n,[[int(i==j) for i in range(n)] for j in range(n)]
    h,u=hermite(fmpz_mat(columns))
    remainder=list(map(int,rhs));z=[0]*len(columns);rank=0;last=-1
    for i in range(h.nrows()):
        row=[int(h[i,j]) for j in range(h.ncols())]
        pivot=next((j for j,n in enumerate(row) if n),None)
        if pivot is None:
            assert all(not h[k,j] for k in range(i,h.nrows()) for j in range(h.ncols()))
            break
        assert pivot>last and row[pivot]>0
        last=pivot;rank+=1
        if remainder[pivot]%row[pivot]:return None
        z[i]=remainder[pivot]//row[pivot]
        if z[i]:remainder=[a-z[i]*b for a,b in zip(remainder,row)]
    if any(remainder):return None
    answer=[sum(z[i]*int(u[i,j]) for i in range(len(z)) if z[i]) for j in range(u.ncols())]
    kernel=[[int(u[i,j]) for j in range(u.ncols())] for i in range(rank,u.nrows())]
    assert [sum(a*c[j] for a,c in zip(answer,columns) if a) for j in range(len(rhs))]==rhs
    return answer,kernel
