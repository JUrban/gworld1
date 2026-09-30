#!/usr/bin/env python3
"""Run the coordinate solver on data extracted from actual fp inputs by GAP."""
import argparse
import json
from pathlib import Path
from n5_class2_mixed import ClassTwo, decide
from check_n5_class2_pipeline import serial, gap_record


def word(g, generators, ext):
    value = g.identity()
    assert len(ext) % 2 == 0
    for i in range(0, len(ext), 2):
        value = g.multiply(value, g.power(generators[ext[i]-1], ext[i+1]))
    return value


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    a = p.parse_args()
    a.output.mkdir(parents=True, exist_ok=False)
    source = json.loads(a.input.read_text())
    records = []
    arithmetic = relators = 0
    for item in source['records']:
        g = ClassTwo(**item['data'])
        for row in item['arithmetic']:
            assert g.multiply(row['a'],row['b']) == row['product'], item['name']
            assert g.inverse(row['a']) == row['inverse'], item['name']
            assert g.power(row['a'],row['exponent']) == row['power'], item['name']
            arithmetic += 3
        for ext in item['fp_relators']:
            assert word(g,item['source_generator_coordinates'],ext) == g.identity(), item['name']
            relators += 1
        result = decide(**item['data'])
        assert result['answer'] == item['expected'], item['name']
        records.append(serial(dict(name=item['name'],result=result)))
        print(item['name'],result['answer'],flush=True)
    (a.output/'solutions.json').write_text(json.dumps(dict(records=records),indent=2)+'\n')
    (a.output/'solutions.g').write_text('N5InputSolutions := '+gap_record(records)+';\n')
    print('PASS N5 fp pipeline:',len(records),'models;',arithmetic,'arithmetic identities;',relators,'relators')


if __name__ == '__main__':
    main()
