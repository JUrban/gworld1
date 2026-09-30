#!/usr/bin/env python3
"""Bounded check of shortening all central two-ended atom representatives."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from certify_g9_two_ended_completion import act, atom, coordinates
from g9_flow_shortening import shorten


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    source = Path('research/certificates/G9-two-ended-completion-v1/certificate.json')
    old = json.loads(source.read_text())
    words = json.loads(Path('research/certificates/G9-bridge-atoms/certificate.json').read_text())['word_certificates']
    words = [tuple(w) for w in words]
    summary = Counter()
    records = []
    for orbit_index, orbit in enumerate(old['orbit_records']):
        xmin, xmax, zmin, zmax = orbit['rectangle']
        for x in range(xmin, xmax+1):
            for z in range(zmin, zmax+1):
                index = orbit['chosen_indices'][x-xmin][z-zmin]
                _, (old_x, old_z) = coordinates(words[index])
                w = act(words[index], x-old_x, z-old_z)
                assert len(w) == orbit['costs'][x-xmin][z-zmin]
                shortened, connectors = shorten(w)
                assert atom(shortened) and coordinates(shortened) == coordinates(w)
                summary['central_words_checked'] += 1
                summary['words_with_connectors'] += bool(connectors)
                summary['total_letters_saved'] += len(w)-len(shortened)
                summary['shortened_words'] += len(shortened) < len(w)
                summary['saving_'+str(len(w)-len(shortened))] += 1
                if len(shortened) < len(w):
                    records.append(dict(orbit_index=orbit_index, x=x, z=z,
                                        original_input=index, original_cost=len(w),
                                        shortened_cost=len(shortened), word=shortened,
                                        connectors=connectors))
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  source=str(source), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  scope='Same central orbit elements only; no new bound claimed by this probe',
                  summary=dict(summary), improved_representatives=records)
    (out/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['summary'], indent=2))
    print('PASS G9 central flow shortening probe')


if __name__ == '__main__':
    main()
