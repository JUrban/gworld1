#!/usr/bin/env python3
"""Row Hermite form by disconnected support components, over the integers.

Rows joined by a common nonzero column form a component. Distinct components
use disjoint constraint columns, so their unimodular transformations combine
by direct sum and row permutation. No lattice is replaced by its saturation.
"""
from collections import defaultdict
from flint import fmpz_mat


def hermite(matrix):
    count=matrix.nrows();width=matrix.ncols()
    sparse=[{j:int(matrix[i,j]) for j in range(width) if matrix[i,j]}
            for i in range(count)]
    parent=list(range(count));owner={}
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i,row in enumerate(sparse):
        for j in row:
            if j in owner:
                a=root(i);b=root(owner[j])
                if a!=b:parent[a]=b
            else:owner[j]=i
    groups=defaultdict(list)
    for i in range(count):groups[root(i)].append(i)
    if len(groups)==1:
        H,U=matrix.hnf(transform=True)
        assert H==U*matrix and abs(U.det())==1
        return H,U
    transformed=[]
    for indexes in groups.values():
        columns=sorted(set().union(*(set(sparse[i]) for i in indexes)))
        if not columns:
            for i in indexes:transformed.append((width,{}, {i:1}))
            continue
        block=fmpz_mat([[sparse[i].get(j,0) for j in columns] for i in indexes])
        h,u=block.hnf(transform=True)
        assert h==u*block and abs(u.det())==1
        for i in range(len(indexes)):
            hrow={j:int(h[i,k]) for k,j in enumerate(columns) if h[i,k]}
            urow={j:int(u[i,k]) for k,j in enumerate(indexes) if u[i,k]}
            transformed.append((min(hrow,default=width),hrow,urow))
    transformed.sort(key=lambda row:row[0])
    H=fmpz_mat(count,width);U=fmpz_mat(count,count)
    for i,(_,hrow,urow) in enumerate(transformed):
        for j,n in hrow.items():H[i,j]=n
        for j,n in urow.items():U[i,j]=n
    assert H==U*matrix and abs(U.det())==1
    return H,U
