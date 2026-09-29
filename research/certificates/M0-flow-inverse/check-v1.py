#!/usr/bin/env python3
from pathlib import Path
import json
from m0_flow_inverse import *

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/certificates/M0-flow-inverse'

def comm(a,b):return reduce_word(a+b+inverse(a)+inverse(b))

def correction(n,target,j,k,terms):
    # xi times a Laurent module combination of [xj,xk]. The chosen
    # commutator has derivative zero in the target coordinate.
    c=comm([j+1],[k+1]);w=[target+1]
    for exponent,coefficient in terms:
        p=exponent_word(exponent)
        cpower=(c if coefficient>0 else inverse(c))*abs(coefficient)
        w=reduce_word(w+p+cpower+inverse(p))
    imgs=identity(n);imgs[target]=w
    return imgs

def main():
    output=OUT/'checks-v1.json';fixture=OUT/'fixtures-v1.g'
    assert not output.exists() and not fixture.exists()
    cases=[('rank0',[]),('rank1_negative',[[-1]]),('rank2_identity',identity(2))]
    for m in [-3,-2,-1,0,1,2,3]:
        cases.append((f'rank3_shift_{m}',correction(3,0,1,2,[([m,0,0],1)])))
    f=correction(3,0,1,2,[([-2,1,0],2),([1,-1,2],-1)])
    g=correction(3,1,0,2,[([0,-1,0],-1),([1,0,-1],1)])
    cases.extend([('rank3_two_components',f),('rank3_other_column',g),('rank3_composite',compose(f,g))])
    beta=identity(3);beta[0]=[1,2]; beta[2]=[-3]
    gamma=identity(3);gamma[1]=[2,3];gamma[0],gamma[2]=gamma[2],gamma[0]
    cases.append(('rank3_nonIA_domain_range',compose(beta,compose(f,gamma))))
    h=correction(4,0,2,3,[([0,-1,1,0],1),([-1,0,0,-1],-1)])
    cases.append(('rank4_signed_laurent',h))
    # Rank two inner automorphism is a positive control in a smaller rank.
    c=comm([1],[2]);cases.append(('rank2_inner',[reduce_word(c+[i]+inverse(c)) for i in [1,2]]))
    records=[]
    for name,images in cases:
        row=construct_inverse(images);row['name']=name;records.append(row)
        print(name,'rank',len(images),'inverse lengths',[len(w) for w in row['inverse']],
              'free inverse',row['free_compositions_identity'],flush=True)
    assert any(not row['free_compositions_identity'] for row in records)
    # Disconnected integral cycle controls with nonzero endpoints and signed
    # multiplicities. The realization must add based connecting paths.
    flow_records=[]
    for n in [2,3,4]:
        endpoint=tuple([1,-1]+[0]*(n-2));base=exponent_word(endpoint)
        v=fox_integer(base,n)[1];cycle=fox_integer(comm([1],[2]),n)[1]
        for e,c in [(tuple([2]*n),2),(tuple([-3]*n),-1)]:
            v=[poly_add(a,poly_mul(unit(n,c,e),b)) for a,b in zip(v,cycle)]
        word,cs=realize_flow(endpoint,v)
        flow_records.append({'rank':n,'endpoint':endpoint,'flow':[[[list(e),c] for e,c in sorted(p.items())] for p in v],'word':word,'cycles':cs})
        assert len(cs)>=2
    negative=identity(3);negative[0]=[1]+comm([2],[3]);negative[1]=[2]+comm([1],[3])
    try:construct_inverse(negative)
    except ValueError as ex:assert str(ex)=='nonunit Jacobian determinant'
    else:raise AssertionError('nonunit negative control was accepted')
    try:realize_flow((1,0),[unit(2),unit(2)])
    except ValueError as ex:assert str(ex)=='flow boundary does not match endpoint'
    else:raise AssertionError('wrong boundary was accepted')
    data={'convention':'Left Fox derivatives, column Jacobians, integral Laurent flows; signed-letter words are one based',
          'records':records,'flow_records':flow_records,'nonunit_images':negative,
          'wrong_boundary':{'endpoint':[1,0],'flow':[[[[0,0],1]],[[[0,0],1]]]},
          'finite_separator':{'images':[[1,1,2,3,-2,-3,-1],[2],[3]],
                              'generators':[[2,3,1,4],[1,2,4,3],[1,3,2,4]],
                              'source_order':24,'image_order':6,'fixed_point':1}}
    output.write_text(json.dumps(data,indent=2)+'\n')
    rows=[[r['name'],r['images'],r['inverse'],r['normalization'],r['normalization_inverse'],r['normalized'],r['normalized_inverse'],r['free_compositions_identity']] for r in records]
    fixture.write_text('M0FlowInverse := '+json.dumps(rows).replace('true','true').replace('false','false')+';\n'
                      +'M0FlowControls := '+json.dumps([[r['rank'],r['endpoint'],r['flow'],r['word']] for r in flow_records])+';\n'
                      +'M0FlowNonunit := '+json.dumps(negative)+';\n'
                      +'M0FlowSeparator := '+json.dumps([data['finite_separator'][k] for k in ['images','generators','source_order','image_order','fixed_point']])+';\n')
    print('PASS M0 integral-flow inverse construction',flush=True)

if __name__=='__main__':main()
