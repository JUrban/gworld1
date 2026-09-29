#!/usr/bin/env python3
"""Construct inverse words in a free metabelian group via integral lattice flows.

Exact Laurent arithmetic and finite Euler circuits. No assertion that the
returned substitutions are mutually inverse in the absolutely free group.
"""
from collections import defaultdict
from itertools import permutations
from m0_witness import poly_add, poly_mul, normalize_abelianization
from check_m0_finite_fields import reduce_word, inverse, compose, identity


def unit(n, coefficient=1, exponent=None):
    return {tuple(exponent or [0]*n): coefficient} if coefficient else {}


def exponent_word(v):
    return [i+1 if a >= 0 else -i-1 for i,a in enumerate(v) for _ in range(abs(a))]


def fox_integer(word,n):
    position=[0]*n; columns=[{} for _ in range(n)]
    for letter in word:
        i=abs(letter)-1
        assert 0<=i<n
        if letter<0: position[i]-=1
        columns[i]=poly_add(columns[i],{tuple(position):1},1 if letter>0 else -1)
        if letter>0: position[i]+=1
    return tuple(position),columns


def boundary(flow,n):
    out={}
    for i,p in enumerate(flow):
        x=[0]*n;x[i]=1
        out=poly_add(out,poly_mul(poly_add(unit(n,exponent=x),unit(n),-1),p))
    return out


def realize_flow(endpoint,flow):
    n=len(endpoint)
    if boundary(flow,n)!=poly_add(unit(n,exponent=endpoint),unit(n),-1):
        raise ValueError('flow boundary does not match endpoint')
    base=exponent_word(endpoint)
    residual=[poly_add(p,q,-1) for p,q in zip(flow,fox_integer(base,n)[1])]
    # Turn negative coefficients into reversed directed edges, retaining the
    # actual signed free-group letter on every edge.
    edges=defaultdict(lambda:defaultdict(int)); balance=defaultdict(int)
    for i,p in enumerate(residual):
        for exponent,coefficient in sorted(p.items()):
            tip=list(exponent);tip[i]+=1;tip=tuple(tip)
            start,end,letter=(exponent,tip,i+1) if coefficient>0 else (tip,exponent,-i-1)
            amount=abs(coefficient)
            edges[start][(end,letter)]+=amount
            balance[start]-=amount;balance[end]+=amount
    assert all(v==0 for v in balance.values())
    cycles=[];result=[]
    while edges:
        start=min(edges);current=start;letters=[]
        while True:
            assert current in edges and edges[current]
            end,letter=min(edges[current]);letters.append(letter)
            edges[current][(end,letter)]-=1
            if not edges[current][(end,letter)]:del edges[current][(end,letter)]
            if not edges[current]:del edges[current]
            current=end
            if current==start:break
        connector=exponent_word(start)
        result=reduce_word(result+connector+letters+inverse(connector))
        cycles.append({'start':start,'letters':letters,'connector':connector})
    result=reduce_word(result+base)
    assert fox_integer(result,n)==(tuple(endpoint),flow)
    return result,cycles


def determinant(a,n):
    k=len(a);out={}
    for p in permutations(range(k)):
        sign=(-1)**sum(p[i]>p[j] for i in range(k) for j in range(i+1,k))
        term=unit(n,sign)
        for i,j in enumerate(p):term=poly_mul(term,a[i][j])
        out=poly_add(out,term)
    return out


def matrix_product(a,b,n):
    return [[sum_polys(poly_mul(a[i][k],b[k][j]) for k in range(n)) for j in range(n)] for i in range(n)]


def sum_polys(polys):
    out={}
    for p in polys:out=poly_add(out,p)
    return out


def jacobian(images):
    n=len(images);columns=[fox_integer(w,n)[1] for w in images]
    return [[columns[j][i] for j in range(n)] for i in range(n)]


def inverse_matrix(a,n):
    delta=determinant(a,n)
    if len(delta)!=1 or abs(next(iter(delta.values())))!=1:
        raise ValueError('nonunit Jacobian determinant')
    exponent,coefficient=next(iter(delta.items()))
    inverse_unit=unit(n,coefficient,[-i for i in exponent])
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            # Transposed cofactor: delete original row j, column i.
            minor=[[a[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
            row.append(poly_mul(poly_mul(unit(n,(-1)**(i+j)),determinant(minor,n)),inverse_unit))
        out.append(row)
    identity_matrix=[[unit(n,int(i==j)) for j in range(n)] for i in range(n)]
    assert matrix_product(a,out,n)==identity_matrix==matrix_product(out,a,n)
    return out,delta


def construct_inverse(images):
    n=len(images)
    if not n:return {'images':[],'normalization':[],'normalization_inverse':[],
                     'normalized':[],'inverse':[],'normalized_inverse':[],'cycles':[],
                     'determinant':[[[],1]],'free_compositions_identity':True}
    beta,beta_inverse=normalize_abelianization(images)
    normalized=compose(beta,images)
    jac=jacobian(normalized);inv,delta=inverse_matrix(jac,n)
    words=[];cycles=[]
    for i in range(n):
        endpoint=[int(i==j) for j in range(n)]
        w,cs=realize_flow(endpoint,[inv[j][i] for j in range(n)])
        words.append(w);cycles.append(cs)
    # normalized=beta after phi, hence phi^-1=normalized^-1 after beta.
    answer=compose(words,beta)
    compositions=[compose(images,answer),compose(answer,images)]
    for comp in compositions:
        for i,w in enumerate(comp):assert fox_integer(w,n)==fox_integer([i+1],n)
    return {'images':images,'normalization':beta,'normalization_inverse':beta_inverse,
            'normalized':normalized,'normalized_inverse':words,'inverse':answer,
            'cycles':cycles,'determinant':[[list(e),c] for e,c in sorted(delta.items())],
            'free_compositions_identity':all(x==identity(n) for x in compositions)}
