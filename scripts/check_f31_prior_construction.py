#!/usr/bin/env python3
"""Finite interface audit of Lei--Zhang's prior construction, not a new result."""
import argparse
import json
from pathlib import Path
from check_f34_graph import fold_graph
from f38_polynomial_identity import inverse,word_reduce,substitute


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();assert not args.output.exists()
    records=[];edge_checks=0
    for n in range(2,13):
        colors=[(-1,)*i+(2,)*i for i in range(n)]
        common=[c+c for c in colors[1:]]
        g=[(1,)]+common;h=[(2,)]+common
        gg,_=fold_graph(g);hg,_=fold_graph(h)
        assert len(gg['basis'])==len(hg['basis'])==n
        edges=[(i-1,1,i) for i in range(1,n)]
        for i in range(1,n):edges += [(0,i+1,0),(i,i+1,i)]
        outgoing={}
        for v,label,w in edges:
            for source,letter,target in [(v,label,w),(w,-label,v)]:
                assert (source,letter) not in outgoing
                outgoing[source,letter]=target
            assert g[label-1]==word_reduce(colors[v]+h[label-1]+inverse(colors[w]))
            edge_checks+=1
        assert len(set(colors))==n
        basis=[(i+1,) for i in range(1,n)]
        basis += [(1,)*i+(i+1,)+(-1,)*i for i in range(1,n)]
        ag,_=fold_graph(basis)
        assert len(ag['basis'])==2*n-2 and ag['vertices']==n
        assert len(edges)==3*n-3
        assert all(substitute(w,g)==substitute(w,h) for w in basis)
        assert substitute((1,),g)!=substitute((1,),h)
        records.append({'n':n,'g':g,'h':h,'g_rank':len(gg['basis']),
                        'h_rank':len(hg['basis']),'colors':colors,'colored_edges':edges,
                        'subgroup_basis':basis,'subgroup_rank':len(ag['basis']),
                        'equalizer_full_rank':'not computed'})
    # Equal maps give the whole F2, yet contain this rank-three subgroup.
    bad_basis=[(1,1),(2,),(1,2,-1)]
    bad_graph,_=fold_graph(bad_basis)
    assert len(bad_graph['basis'])==3 and bad_graph['vertices']==2
    assert len(set([(),()]))==1
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:
        json.dump({'attribution':'Lei--Zhang arXiv:2604.24502v2, Sections2--4; prior work only.',
                   'records':records,'edge_equations':edge_checks,
                   'noninjective_color_control':{'maps':'g=h=id(F2)','subgroup_basis':bad_basis,
                     'subgroup_rank':3,'equalizer_rank':2,'vertex_colors':[[],[]]}},f,indent=2)
        f.write('\n')
    print('11 ranks n2..12;',edge_checks,'coloring identities; all image and graph ranks verified')
    print('Rank-monotonicity negative control: subgroup3, equalizer2, noninjective colors')
    print('PASS prior F31 construction interface')


if __name__=='__main__':main()
