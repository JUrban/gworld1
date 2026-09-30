#!/usr/bin/env python3
"""Complete necessary permutation cases for m(v)=4, not braid exhaustion."""
import argparse
from itertools import permutations
import json
from pathlib import Path

from check_b9_three_strand_underlying import compose,extend,invperm,shperm,wordperm,nu
from b9_special_braids import shelf


def ip(p,k):
    return compose(compose(extend(p),wordperm(tuple(range(k,0,-1)),len(p)+1)),invperm(shperm(p)))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();assert not args.output.exists()
    p3=[wordperm(w,3) for w in [(),(1,),(1,1,-2),(2,1)]]
    s3=list(permutations(range(1,4)));s4=list(permutations(range(1,5)))
    p4={0:{(1,2,3,4)},1:{ip(p,1) for p in p3},
        2:{ip(p,2) for p in s3},3:{ip(p,3) for p in s3}}
    p4all=set().union(*p4.values())
    p5={0:{(1,2,3,4,5)},1:{ip(p,1) for p in p4all},
        2:{ip(p,2) for p in s4},3:{ip(p,3) for p in s4},4:{ip(p,4) for p in s4}}
    for groups in [p4,p5]:
        for e,rows in groups.items():
            assert all(nu(p)==e for p in rows)
    vwords=[shelf((1,1,-2),()),shelf((2,1),())]
    vcases=[{'kind':'known epsilon1 word','word':w,'permutation':wordperm(w,4),'epsilon':1}
            for w in vwords]
    vcases += [{'kind':'unknown epsilon2 sector','permutation':p,'epsilon':2}
               for p in sorted(p4[2])]
    rows=[];survivors=[];tested=0
    for v in vcases:
        vc=ip(v['permutation'],1)
        for e,possibilities in p5.items():
            if e==0:continue
            for up in sorted(possibilities):
                tested+=1
                ap=compose(ip(up,1),shperm(vc))
                if ap[3:]==(4,5,6):
                    record={'v':v,'u_epsilon':e,'u_permutation':up,'A_permutation':ap}
                    rows.append(record)
                    if up.index(1)<2:
                        survivors.append(record)
    output={'scope':'Complete necessary permutation bounds for m(v)=4 and m(u)=5, with positive v excluded beforehand. No surviving row certifies a braid or specialness.',
            'P4_by_exponent':{str(e):sorted(ps) for e,ps in p4.items()},
            'P5_upper_by_exponent':{str(e):sorted(ps) for e,ps in p5.items()},
            'v_cases':vcases,'tested':tested,'all_support_survivors':rows,
            'small_class_survivors':survivors}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
    print('P4 counts',{e:len(ps) for e,ps in p4.items()},'P5 upper counts',{e:len(ps) for e,ps in p5.items()})
    print('tested',tested,'permutation survivors',len(rows),'small-class survivors',len(survivors))
    for row in survivors:print(json.dumps(row))
    print('PASS B9 four-strand necessary permutation inventory')


if __name__=='__main__':main()
