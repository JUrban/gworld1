#!/usr/bin/env python3
"""A finite forbidden-subword certificate for an upper growth bound."""
import json
from pathlib import Path
from g9_flow_unfolding import flow

OUT=Path('research/certificates/G9-forbidden-upper')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'certificate.json').exists(),'Preserve old evidence'
rank=2;bound=10;alphabet=(-2,-1,1,2)
representatives={};words=[]


def visit(w):
    f=flow(rank,w);words.append((w,f))
    old=representatives.get(f)
    if old is None or (len(w),w)<(len(old),old):representatives[f]=w
    if len(w)==bound:return
    for a in alphabet:
        if not w or w[-1]!=-a:visit(w+(a,))


visit(())
bad={};minimal=[]
for w,f in sorted(words,key=lambda pair:(len(pair[0]),pair[0])):
    normal=representatives[f]
    if normal==w:continue
    assert (len(normal),normal)<(len(w),w)
    bad[w]=normal
    if not any(w[i:j] in bad for i in range(len(w)) for j in range(i+1,len(w)+1) if j-i<len(w)):
        minimal.append((w,normal))
for a in alphabet:minimal.append(((a,-a),()))
minimal.sort(key=lambda pair:(len(pair[0]),pair[0]))
patterns={w for w,normal in minimal}
prefixes={()}
for w in patterns:
    for i in range(1,len(w)):prefixes.add(w[:i])
states=sorted(prefixes,key=lambda w:(len(w),w));index={w:i for i,w in enumerate(states)}
transitions=[]
for state in states:
    row=[]
    for a in alphabet:
        w=state+(a,)
        if any(w[i:] in patterns for i in range(len(w))):row.append(-1);continue
        for i in range(len(w)+1):
            if w[i:] in index:row.append(index[w[i:]]);break
        else:raise AssertionError('Missing empty suffix')
    transitions.append(row)

# A positive rational/integer comparison vector, with exact verification.
v=[1]*len(states)
for _ in range(200):v=[1+sum(v[j] for j in row if j>=0) for row in transitions]
Av=[sum(v[j] for j in row if j>=0) for row in transitions]
denominator=1000000000
numerator=max((a*denominator+b-1)//b for a,b in zip(Av,v))
assert 1<numerator/denominator<3
assert all(denominator*a<=numerator*b for a,b in zip(Av,v))
data=dict(rank=rank,max_relation_side_length=bound,alphabet=alphabet,
          words_enumerated=len(words),distinct_ball_elements=len(representatives),
          noncanonical_words=len(bad),minimal_forbidden_relations=minimal,
          states=states,transitions=transitions,positive_vector=v,
          upper_numerator=numerator,upper_denominator=denominator,
          vector_iterations=200)
(OUT/'certificate.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'fixtures.g').write_text('G9UpperRelations := '+json.dumps(minimal)+';\n'+
    'G9UpperAlphabet := '+json.dumps(alphabet)+';\n'+
    'G9UpperStates := '+json.dumps(states)+';\n'+
    'G9UpperTransitions := '+json.dumps(transitions)+';\n'+
    'G9UpperVector := '+json.dumps(v)+';\n'+
    'G9UpperBound := '+json.dumps([numerator,denominator])+';\n')
print('enumerated',len(words),'ball',len(representatives),'noncanonical',len(bad),'minimal_forbidden',len(minimal),'states',len(states))
print('certified upper',numerator,'/',denominator)
print('PASS G9 FORBIDDEN UPPER CERTIFICATE')
