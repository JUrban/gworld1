#!/usr/bin/env python3
"""Exact nearest-plane reduction using rational Gram data in FLINT.

Same LLL basis and rounding as n8_class7.short_particular. The returned
vector differs from the original by an explicitly verified integer
combination of its full kernel; no approximate arithmetic is used.
"""
from flint import fmpz_mat,fmpq


def short_particular(result):
    vector,kernel=result
    if not kernel:return list(vector)
    raw=fmpz_mat(kernel)
    basis,transform=raw.lll(transform=True,delta=0.75)
    assert basis==transform*raw and abs(transform.det())==1
    gram=basis*basis.transpose();count=basis.nrows()
    mu=[[fmpq(int(i==j)) for j in range(count)] for i in range(count)]
    norms=[]
    for i in range(count):
        for j in range(i):
            mu[i][j]=(fmpq(gram[i,j])-sum(mu[i][k]*mu[j][k]*norms[k]
                        for k in range(j)))/norms[j]
        norms.append(fmpq(gram[i,i])-sum(mu[i][k]**2*norms[k] for k in range(i)))
        assert norms[i]>0
    products=fmpz_mat([list(vector)])*basis.transpose();orth=[]
    for i in range(count):
        orth.append(fmpq(products[0,i])-sum(mu[i][j]*orth[j] for j in range(i)))
    subtract=[0]*count
    for i in reversed(range(count)):
        n=int((orth[i]/norms[i]+fmpq(1,2)).floor());subtract[i]=n
        if n:
            for j in range(i):orth[j]-=n*mu[i][j]*norms[j]
    change=fmpz_mat([subtract])*basis
    answer=[int(vector[j])-int(change[0,j]) for j in range(len(vector))]
    assert fmpz_mat([subtract])*transform*raw==change
    return answer
