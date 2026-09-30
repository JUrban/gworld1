#!/usr/bin/env python3
"""Real special-braid lifts of a false permutation-only shortcut."""
import argparse
import json
from pathlib import Path
from b9_special_braids import artin, shelf, shift, reduce_word, strand_number
from check_b9_three_strand_underlying import wordperm, burau


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args=parser.parse_args()
    assert not args.output.exists()
    fixtures=json.loads(Path('research/certificates/B9/height4.json').read_text())['records']
    known=[(i,tuple(r['word'])) for i,r in enumerate(fixtures) if r['strands']<=4]
    target_g=(1,4,5,3,2)
    target_f=(1,2,5,6,4,3)
    gs=[(i,shelf(w,())) for i,w in known if wordperm(shelf(w,()),5)==target_g]
    fs=[(i,shelf(shelf(w,()),())) for i,w in known
        if wordperm(shelf(shelf(w,()),()),6)==target_f]
    assert gs and fs
    rows=[]
    for gi,v in gs:
        for fi,u in fs:
            a=reduce_word(shelf(u,())+shift(shelf(v,())))
            ap=wordperm(a,7)
            assert ap==(2,3,1,4,5,6,7)
            ui,vi,ai=artin(u,7),artin(v,7),artin(a,7)
            m=[strand_number(x) for x in [ui,vi,ai]]
            assert m[0]==6 and m[1]==5 and m[2]>3
            bm=burau(a,7)
            assert bm[6]!=[0,0,0,0,0,0,1]
            rows.append({'v_fixture_zero_based':gi,'u_fixture_zero_based':fi,
                         'u_word':u,'v_word':v,'A_word':a,'A_permutation':ap,
                         'minimum_strands_u_v_A':m,'A_x7':ai[6],
                         'A_Burau_last_row':bm[6]})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:
        json.dump({'scope':'Actual special lifts satisfy the high-strand permutation obstruction but A is not in B3. No braid counterexample to the conditional four-strand theorem.',
                   'rows':rows},f,indent=2);f.write('\n')
    for row in rows: print(json.dumps(row))
    print('PASS B9 general permutation special lifts')


if __name__=='__main__':main()
