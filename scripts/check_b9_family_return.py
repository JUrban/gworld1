#!/usr/bin/env python3
"""An all-parameter necessary-condition test, not a B4 exhaustion."""
import json
from pathlib import Path
import sympy as sp
from b9_special_braids import shelf


def main():
    n = sp.Symbol('n', integer=True)
    ident = sp.eye(5)
    generators = []
    for i in range(4):
        g = ident.copy()
        g[i, i], g[i, i+1], g[i+1, i], g[i+1, i+1] = 2, -1, 1, 0
        assert (g-ident)**2 == sp.zeros(5)
        generators.append(g)
    for i, g in enumerate(generators):
        for j, h in enumerate(generators):
            if abs(i-j) == 1:
                assert g*h*g == h*g*h
            if abs(i-j) > 1:
                assert g*h == h*g

    def image(word):
        result = ident
        for a in word:
            result = result*(ident + (1 if a > 0 else -1)*(generators[abs(a)-1]-ident))
        return result

    blocks = [(1,n), (3,n-2), (2,1-n), (3,2), (4,-1),
              (2,1), (1,1), (3,n-1), (4,2-n), (2,-n)]
    matrix = ident
    for i, exponent in blocks:
        matrix = matrix*(ident+exponent*(generators[i-1]-ident))
    matrix = matrix.applyfunc(sp.expand)
    f = sp.factor(matrix[0,4])
    assert sp.expand(f-n*(n-1)*((n-1)**2+1)) == 0
    m = sp.Symbol('m', nonnegative=True, integer=True)
    coeff = list(map(int, sp.Poly(f.subs(n,m+3),m).all_coeffs()))
    assert coeff == [1,9,31,49,30]
    coeff4 = list(map(int, sp.Poly(f.subs(n,m+4),m).all_coeffs()))
    assert coeff4 == [1,13,64,142,120]
    # Existing explicitly witnessed examples; no assertion that these exhaust B4.
    old = json.loads(Path('research/certificates/B9/height4.json').read_text())['records']
    examples = [(i,r) for i,r in enumerate(old) if r['strands'] <= 4]
    assert len(examples) == 10
    rows = []
    for i,r in examples:
        c = shelf(tuple(r['word']), ())
        ci = image(c)
        value = int(ci[0,4])
        rows.append({'source_index':i, 'v':r['word'], 'c':list(c),
                     'c_last_column':list(map(int,ci[:,4])), 'top_entry':value,
                     'difference_at_n3':30-value})
        print('v index',i,'strands',r['strands'],'c(1,5)',value,flush=True)
    out = Path('research/certificates/B9-family-return')
    out.mkdir(exist_ok=True)
    assert not (out/'checks-v2.json').exists() and not (out/'fixtures-v2.g').exists()
    data = {'scope':'Only u=beta_n from the existing infinite B5 family, n>=3, and the ten known v in B4',
            'beta_top_last_entry':str(f), 'coefficients_at_n_equals_m_plus_3':coeff,
            'coefficients_at_n_equals_m_plus_4':coeff4,
            'records':rows, 'maximum_c_entry':max(r['top_entry'] for r in rows)}
    (out/'checks-v2.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'fixtures-v2.g').write_text('B9FamilyReturn := '+json.dumps([
        [r['source_index']+1,r['v'],r['top_entry']] for r in rows])+';\n')
    assert all(r['difference_at_n3'] != 0 for r in rows)
    assert data['maximum_c_entry'] < 120
    # Right B4 multiplication fixes the last column, not the last row.
    assert all(g[:,4] == ident[:,4] for g in generators[:3])
    assert (generators[3]*generators[2])[:,4] == generators[3][:,4]
    assert list((generators[3]*generators[2])[4,:]) != list(generators[3][4,:])
    print('n=3 entry30 is absent; for n>=4 entry>=120; all c entries <=',data['maximum_c_entry'])
    print('PASS B9 all-parameter family-return obstruction')


if __name__ == '__main__':
    main()
