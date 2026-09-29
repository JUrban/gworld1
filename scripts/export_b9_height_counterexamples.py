#!/usr/bin/env python3
"""Extract small, self-contained term DAGs for the eleven B5 witnesses."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path('research/certificates/B9-strand-drop')
    paths = [Path('research/certificates/B9/height5-burau.json'),
             root / 'filter-v1.json', root / 'cbraid-v1.json']
    parents, source, checked = [json.loads(p.read_text()) for p in paths]
    parents = parents['records']
    selected = [(i, h, r) for i, (h, r) in enumerate(zip(source['hits'], checked['results']))
                if r['minimum_strands'] == 5]
    needed = set()
    todo = [j for _, h, _ in selected for j in h['parents']]
    while todo:
        j = todo.pop()
        if j in needed:
            continue
        needed.add(j)
        todo.extend(parents[j]['parents'] or [])
    indices = sorted(needed)
    remap = {j: i for i, j in enumerate(indices)}
    records = [{'word': parents[j]['word'], 'height': parents[j]['height'],
                'parents': [remap[k] for k in parents[j]['parents']] if parents[j]['parents'] else []}
               for j in indices]
    candidates = []
    for i, h, r in selected:
        records.append({'word': h['word'], 'height': h['term_height'],
                        'parents': [remap[j] for j in h['parents']]})
        candidates.append({'term_index': len(records)-1, 'filter_index': i,
                           'small_word': r['word']})
    out = {'sources': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'records': records, 'candidates': candidates,
           'convention': 'zero-based JSON parents; one-based GAP parents; leaf height zero'}
    dest = root / 'height-counterexamples-v1.json'
    assert not dest.exists()
    dest.write_text(json.dumps(out, indent=2) + '\n')
    gap = ['# Self-contained special-braid term DAG; one-based indices.', 'B9Terms := [']
    gap.extend('  ' + json.dumps([r['word'], r['height'], [j+1 for j in r['parents']]]) + ','
               for r in records)
    gap[-1] = gap[-1][:-1]
    gap.extend(['];;', 'B9Witnesses := ['])
    gap.extend('  ' + json.dumps([c['term_index']+1, c['small_word']]) + ',' for c in candidates)
    gap[-1] = gap[-1][:-1]
    gap.append('];;')
    (root / 'height-counterexamples-v1.g').write_text('\n'.join(gap) + '\n')
    print('terms', len(records), 'witnesses', len(candidates))
    print('PASS B9 counterexample export')


if __name__ == '__main__':
    main()
