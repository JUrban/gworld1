#!/usr/bin/env python3
"""Recover Hall commutator trees, checking every supplied expanded word."""
import json
from pathlib import Path

out=Path('research/certificates/N8-odd-adjoint-lead')
text=(out/'fixtures.g').read_text()
words=json.loads(text.split('N8OddHalls := ',1)[1].split(';',1)[0])
def reduced(word):
    stack=[]
    for letter in word:
        if stack and stack[-1]==-letter:stack.pop()
        else:stack.append(letter)
    return stack
def inverse(word):return [-letter for letter in reversed(word)]
halls=[dict(weight=1,pair=None,word=[i+1]) for i in range(2)]
for weight in range(2,12):
    new=[]
    for i,a in enumerate(halls):
        for j in range(i):
            b=halls[j]
            if a['weight']+b['weight']!=weight:continue
            if a['pair'] is not None and a['pair'][1]>j:continue
            new.append(dict(weight=weight,pair=(i,j),word=reduced(inverse(a['word'])+inverse(b['word'])+a['word']+b['word'])))
    halls.extend(new)
for d in range(1,12):assert [h['word'] for h in halls if h['weight']==d]==words[d-1]
records=[[h['weight'],*[i+1 for i in h['pair']]] if h['pair'] is not None else [1,0,i+1]
         for i,h in enumerate(halls)]
target=out/'hall-trees.g';assert not target.exists()
target.write_text('N8OddHallTrees := '+json.dumps(records)+';\n')
print('Exported and word-checked',len(records),'Hall trees')
