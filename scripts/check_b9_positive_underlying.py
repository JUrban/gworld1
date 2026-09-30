#!/usr/bin/env python3
"""Interface checks for the universal positive-underlying B9 exclusion."""
import argparse
from pathlib import Path
import json

from check_b9_three_strand_underlying import compose, extend, i1perm, shperm, wordperm, nu
from b9_special_braids import artin, shelf, shift, reduce_word


def last_swap(q, i):
    return q+2 if i == q+1 else q+1 if i == q+2 else i


def low(a, i):
    return a[i-1] if i <= 3 else i


def column(word, n):
    v = [0]*(n-1)+[1]
    for letter in reversed(word):
        i = abs(letter)-1
        x,y = v[i:i+2]
        v[i:i+2] = [2*x-y,x] if letter > 0 else [y,-x+2*y]
    return v


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(); assert not args.output.exists()
    rows=[]
    for q in range(3,65):
        all_survivors=[]; special_survivors=[]
        for a in [(1,2,3),(2,3,1),(3,1,2)]:
            for f1 in range(1,q+2):
                f=[f1,a[0]]
                for i in range(3,q+2):
                    f.append(low(a,last_swap(q,f[-1]+1)))
                if sorted(f)!=list(range(1,q+2)):
                    continue
                if f1!=low(a,last_swap(q,f1+1)):
                    continue
                left=compose(extend(tuple(f)),(2,1)+tuple(range(3,q+3)))
                right=tuple(low(a,last_swap(q,j)) for j in shperm(tuple(f)))
                if left!=right:
                    continue
                all_survivors.append((a,tuple(f)))
                if f[0]==1 or f[1]==1:
                    special_survivors.append((a,tuple(f)))
        tau=(q+1,)+tuple(range(1,q+1))
        bad=(q+1,2,1)+tuple(range(3,q+1))
        assert all_survivors==[((1,2,3),tau),((2,3,1),bad)]
        assert special_survivors==[((1,2,3),tau)]
        assert nu(tau)==q and bad.index(1)+1==3
        u=tuple(range(q,0,-1));v=tuple(range(q-1,0,-1));c=shelf(v,())
        assert wordperm(u,q+1)==tau
        assert wordperm(c,q+1)==tuple(range(1,q))+(q+1,q)
        uc=column(u,q+1);cc=column(c,q+1)
        assert uc==[0]*(q-1)+[-1,0]
        assert cc==[-2]+[-4]*(q-2)+[-1,2]
        assert column(u+(1,-2,1),q+1)==uc
        rows.append({'q':q,'all_permutation_survivors':all_survivors,
                     'small_class_survivors':special_survivors,
                     'u_word':u,'v_word':v,'c_word':c,
                     'u_last_column':uc,'c_last_column':cc})
    # q>=3 is necessary: v=s and u=s^2 t^-1 give A=(s^2 t^-1)s in B3.
    u=(1,1,-2);v=(1,)
    a=reduce_word(shelf(u,())+shift(shelf(v,())))
    assert artin(a,5)==artin(u+(1,),5)
    assert artin(a,5)[3:]==((4,),(5,))
    # At the first excluded q, the permutation survivor is not actual support.
    u=(3,2,1);v=(2,1)
    a=reduce_word(shelf(u,())+shift(shelf(v,())))
    assert wordperm(a,5)==(1,2,3,4,5) and artin(a,5)[4]!=(5,)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:
        json.dump({'scope':'Finite interface checks q=3..64 for the separate universal written proof; no B4 exhaustion.',
                   'records':rows,'q2_boundary':{'u':[1,1,-2],'v':[1],'A':[1,1,-2,1]},
                   'small_class_control':'Dropping f^-1(1)<=2 retains the displayed second permutation at every tested q.'},f,indent=2)
        f.write('\n')
    print('62 strand parameters: unique small-class permutation survivor; second survivor retained without that hypothesis')
    print('All exact columns: u=(0,...,0,-1,0), c=(-2,-4,...,-4,-1,2)')
    print('q=2 valid boundary and q=3 permutation-only false positive checked by faithful actions')
    print('PASS B9 positive underlying interface checks')


if __name__=='__main__':main()
