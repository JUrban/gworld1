#!/usr/bin/env python3
"""Complete polynomial particular families for a CONSTANT integer matrix.

Uses the previously audited one-parameter solver, then retains a complete
integer kernel. This is an arithmetic component, not the full N8 algorithm.
"""
import sympy as S
from parametric_integer_linear import (T, solve, decode_matrix, encode_matrix,
                                      integer_solve, denominator, specialize)
from n8_component_hnf import hermite
from flint import fmpz_mat

def families(A,b):
    A,b=S.Matrix(A),S.Matrix(b)
    assert all(not x.free_symbols for x in A)
    rec=solve(A,b)
    scale=denominator(list(A))
    integer=(scale*A).applyfunc(S.expand)
    H,U=hermite(fmpz_mat([[int(x) for x in row] for row in integer.T.tolist()]))
    H=S.Matrix(H.tolist());U=S.Matrix(U.tolist())
    rank=A.rank();K=U[rank:,:].T
    assert H==U*integer.T and abs(U.det())==1 and A*K==S.zeros(A.rows,K.cols)
    result=dict(A=encode_matrix(A),b=encode_matrix(b),certificate=rec,
                integer_scale=scale,H=encode_matrix(H),U=encode_matrix(U),
                kernel=encode_matrix(K),rank=rank,families=[])
    if rec['mode']!='periodic':
        for row in rec['finite_checks']:
            if row['witness'] is not None:
                result['families'].append(dict(t=row['t'],point=row['witness']))
        result['mode']='finite'
    else:
        assert rec['rank_drop']==[]
        Z,L=decode_matrix(rec['Z']),decode_matrix(rec['L'])
        assert all(not x.free_symbols for x in L)
        period=rec['K'];result.update(mode='periodic',period=period)
        for row in rec['residue_checks']:
            if row['ell'] is None:continue
            r=row['residue'];ell=S.Matrix(L.cols,1,row['ell'])
            point=((Z.applyfunc(lambda x:S.expand(x.subs(T,period*T+r)))+L*ell)/period).applyfunc(S.expand)
            assert all(c.is_Integer for x in point for c in S.Poly(x,T).all_coeffs())
            assert (A*point-b.applyfunc(lambda x:S.expand(x.subs(T,period*T+r)))).applyfunc(S.expand)==S.zeros(A.rows,1)
            result['families'].append(dict(residue=r,point=encode_matrix(point)))
    return result

def member(result,t):
    if result['mode']=='finite':return any(row['t']==t for row in result['families'])
    return any(row['residue']==t%result['period'] for row in result['families'])

def point_at(result,t):
    if result['mode']=='finite':
        return S.Matrix(next(row['point'] for row in result['families'] if row['t']==t))
    row=next(row for row in result['families'] if row['residue']==t%result['period'])
    return specialize(decode_matrix(row['point']),(t-row['residue'])//result['period'])
