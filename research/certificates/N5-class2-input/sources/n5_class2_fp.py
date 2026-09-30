#!/usr/bin/env python3
"""N5 decision and factor words for an fp group PROMISED of class <=2.

Input JSON: {"generators": n, "relators": [[i,e,...], ...]}.
Each relator is a product of generator i to integer power e; indices start
at one. Use run_recorded.py to bound and record this complete command.
The promise is a hypothesis, not a recognition result or a checked fact.
"""
import argparse
import json
from pathlib import Path
import subprocess
from n5_class2_mixed import decide
from check_n5_class2_pipeline import serial, gap_record

ROOT = Path(__file__).resolve().parents[1]


def run_gap(path, output, stage):
    command = [str(ROOT/'bin/gap'), '-q', '--quitonbreak', str(path)]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    (output/(stage+'-stdout.log')).write_text(proc.stdout)
    (output/(stage+'-stderr.log')).write_text(proc.stderr)
    (output/(stage+'-process.json')).write_text(json.dumps(dict(
        command=command, actual_returncode=proc.returncode,
        marker_seen='PASS N5 fp '+stage in proc.stdout), indent=2)+'\n')
    if proc.returncode or proc.stderr.strip() or 'PASS N5 fp '+stage not in proc.stdout:
        raise RuntimeError('GAP '+stage+' failed; inspect retained logs')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--assume-class-at-most-two', action='store_true', required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    n, relators = source['generators'], source['relators']
    if type(n) is not int or n < 0 or not isinstance(relators,list):
        raise ValueError('nonnegative integer generator count and relator list required')
    for row in relators:
        if (not isinstance(row,list) or len(row)%2 or
            any(type(x) is not int for x in row) or
            any(not 1 <= row[i] <= n for i in range(0,len(row),2))):
            raise ValueError('invalid indexed relator')
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output/'input.json').write_text(json.dumps(dict(generators=n,relators=relators),indent=2)+'\n')
    setup = '''Read("scripts/n5_class2_input.g");
Read("scripts/n5_class2_json.g");
N5Free := FreeGroup(%d);
N5Gens := GeneratorsOfGroup(N5Free);
N5ExtWord := function(v)
    local w,i;
    w:=One(N5Free);
    for i in [1,3..Length(v)-1] do w:=w*N5Gens[v[i]]^v[i+1];od;
    return w;
end;
N5Presentation := N5Free/List(%s,N5ExtWord);
N5Model := N5FpClassTwo(N5Presentation,true);
''' % (n,gap_record(relators))
    export = setup + 'N5WriteCoordinateJson('+gap_record(str(output/'coordinates.json'))+',N5Model.data);\nPrint("PASS N5 fp export\\n");\nQUIT;\n'
    (output/'export.g').write_text(export)
    run_gap(output/'export.g',output,'export')
    coordinates = json.loads((output/'coordinates.json').read_text())
    result = decide(**coordinates)
    (output/'decision.json').write_text(json.dumps(serial(result),indent=2)+'\n')
    (output/'decision.g').write_text('N5Decision := '+gap_record(serial(result))+';\n')
    replay = setup + 'Read('+gap_record(str(output/'decision.g'))+');\n'+'''
if not ForAll(RecNames(N5Model.data),k->N5Model.data.(k)=N5Decision.(k)) then
    Error("reconstructed input differs from decision input");fi;
N5Words := [];
if N5Decision.answer then
    N5Factors := N5InputFactors(N5Model,N5Decision);
    N5Words := List(N5Factors.words,ws->List(ws,w->ExtRepOfObj(UnderlyingElement(w))));
fi;
''' + 'N5WriteCoordinateJson('+gap_record(str(output/'answer.json'))+',rec(answer:=N5Decision.answer,factor_words:=N5Words));\nPrint("PASS N5 fp replay\\n");\nQUIT;\n'
    (output/'replay.g').write_text(replay)
    run_gap(output/'replay.g',output,'replay')
    print(json.dumps(dict(answer=result['answer'],factor_words_file=str(output/'answer.json'),
        scope='finite presentation promised nilpotent of class at most two')))
    print('PASS N5 fp command')


if __name__ == '__main__':
    main()
