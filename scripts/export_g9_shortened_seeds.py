#!/usr/bin/env python3
"""Bind shortened representatives to the original atom certificate."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from certify_g9_two_ended_completion import act, atom, coordinates, gap
from g9_flow_unfolding import flow


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    paths = [Path('research/certificates/G9-bridge-atoms/certificate.json'),
             Path('research/certificates/G9-two-ended-completion-v1/certificate.json'),
             Path('research/certificates/G9-flow-shortening-probe-v1/certificate.json')]
    original, old, improvements = [json.loads(p.read_text()) for p in paths]
    words = [tuple(w) for w in original['word_certificates']]
    count = len(words)
    records = improvements['improved_representatives']
    for r in records:
        i = r['original_input']
        key, (x, z) = coordinates(words[i])
        prior = old['orbit_records'][r['orbit_index']]
        xmin, xmax, zmin, zmax = prior['rectangle']
        assert i == prior['chosen_indices'][r['x']-xmin][r['z']-zmin]
        old_word = act(words[i], r['x']-x, r['z']-z)
        new_word = tuple(r['word'])
        assert len(new_word) == r['shortened_cost'] < r['original_cost'] == len(old_word)
        assert r['shortened_cost'] > 14
        assert flow(2, old_word) == flow(2, new_word)
        assert atom(new_word) and coordinates(new_word) == (key, (r['x'], r['z']))
        r['new_input_index'] = len(words)
        words.append(new_word)
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Original 21483 atom words plus finitely many shorter representatives in the same two-ended orbits',
                  sources=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths],
                  original_count=count, additional_count=len(records),
                  word_certificates=words,
                  counts_by_minimum_bridge_length=original['counts_by_minimum_bridge_length'],
                  lower_bound=original['lower_bound'], replacement_records=records)
    (out/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    (out/'fixtures.g').write_text('G9AtomWords:='+gap(words)+';\nG9AtomCounts:='
        +gap(original['counts_by_minimum_bridge_length'])+';\nG9ShortenedSeedRecords:='+gap(records)+';\n')
    print('ORIGINAL_INPUTS',count,'ADDITIONAL_SEEDS',len(records),'ALL_NEW_COSTS_ABOVE_14')
    print('PASS G9 shortened seed export')


if __name__ == '__main__':
    main()
