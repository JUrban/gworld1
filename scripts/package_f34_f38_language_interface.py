#!/usr/bin/env python3
"""Verify current interface compatibility and compact whitespace-heavy output."""
import hashlib
import json
from pathlib import Path
from f34_f38_language_interface import grammar_case


def main():
    root = Path(__file__).resolve().parents[1]
    directory = root/'research/certificates/F34-F38-language-interface-v1'
    source = directory/'cases.json'
    raw = source.read_bytes()
    records = json.loads(raw)
    for record in records:
        current = grammar_case(record['grammar'], record['system']['problem'], record['system']['rank'])
        assert all(value == record['certificate'][key] for key, value in current.items())
        missing = dict(record['grammar'])
        missing['seeds'] = dict(missing['seeds'])
        del missing['seeds']['V']
        try:
            grammar_case(missing, record['system']['problem'], record['system']['rank'])
        except ValueError:
            pass
        else:
            raise AssertionError('Missing projected variable must be rejected')
    compact = (json.dumps(records, separators=(',', ':'))+'\n').encode()
    assert len(compact) < 90000000
    assert (json.dumps(json.loads(compact), indent=2)+'\n').encode() == raw
    target = root/'large-artifacts/F34-F38-language-interface-v1/cases-pretty.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise ValueError('Preserve previous large artifact')
    source.rename(target)
    source.write_bytes(compact)
    report = dict(current_cases_unchanged=len(records), missing_component_rejections=len(records),
                  representation='Only JSON whitespace changed; original bytes reproducible by indent=2 plus newline',
                  omitted_path=str(target.relative_to(root)), omitted_bytes=len(raw),
                  omitted_sha256=hashlib.sha256(raw).hexdigest(),
                  retained_path=str(source.relative_to(root)), retained_bytes=len(compact),
                  retained_sha256=hashlib.sha256(compact).hexdigest())
    (directory/'packaging.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    print('PASS F34 F38 interface packaging')


if __name__ == '__main__':
    main()
