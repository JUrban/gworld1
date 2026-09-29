#!/usr/bin/env python3
"""Exact symbolic Burau check for a proposed infinite special B5 family."""
import json
from pathlib import Path
import sympy as sp

n = sp.Symbol('n', integer=True)
d = 5
generators = []
for i in range(d-1):
    s = sp.eye(d)
    s[i, i] = 2
    s[i, i+1] = -1
    s[i+1, i] = 1
    s[i+1, i+1] = 0
    generators.append(s)
    assert (s-sp.eye(d))**2 == sp.zeros(d)
for i in range(d-1):
    for j in range(d-1):
        a, b = generators[i], generators[j]
        if abs(i-j) > 1:
            assert a*b == b*a
        if abs(i-j) == 1:
            assert a*b*a == b*a*b

blocks = [(1,n), (3,n-2), (2,1-n), (3,2), (4,-1),
          (2,1), (1,1), (3,n-1), (4,2-n), (2,-n)]
matrix = sp.eye(d)
for i, k in blocks:
    matrix = matrix*(sp.eye(d)+k*(generators[i-1]-sp.eye(d)))
matrix = matrix.applyfunc(sp.expand)
assert sp.expand(matrix.det()) == 1
print('Exact symbolic Burau matrix at t=-1:')
print(matrix)
print('Bottom row:', list(matrix[-1,:]))
print('Top row:', list(matrix[0,:]))
root = Path('research/certificates/B9-parametric')
root.mkdir(exist_ok=False)
(root/'symbolic-v1.json').write_text(json.dumps({
    'parameter': 'integer n>=3', 'dimension': d, 'burau_t': -1,
    'blocks': [[i,str(k)] for i,k in blocks],
    'matrix': [[str(x) for x in row] for row in matrix.tolist()],
    'scope': 'Symbolic representation only; specialness and strand cancellation require the written group proof.'
},indent=2)+'\n')
print('PASS symbolic B9 family matrix')
