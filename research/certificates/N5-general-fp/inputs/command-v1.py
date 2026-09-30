#!/usr/bin/env python3
"""N5 general decision/constructor for a finite presentation PROMISED nilpotent.

JSON input: {"generators": n, "relators": [[i,e,...], ...]}.
Indices start at one; each row is a product of indexed integer powers.
No class bound is required. Use scripts/run_recorded.py for resource/deadline
limits. A timeout or failed stage is not an indecomposability decision.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from n5_rational_lie_decomposition import decompose
from n5_general_central_solve import solve
from check_n5_rational_lie import serial, gap

ROOT = Path(__file__).resolve().parents[1]


def run_gap(path, output, stage):
    command = [str(ROOT/'bin/gap'), '--quitonbreak', str(path)]
    marker = 'PASS N5 general-fp '+stage
    stdout, stderr = output/(stage+'-stdout.log'), output/(stage+'-stderr.log')
    record = dict(command=command, started_utc=datetime.now(timezone.utc).isoformat())
    record_path = output/(stage+'-process.json')
    with stdout.open('w') as out, stderr.open('w') as err:
        process = subprocess.Popen(command, cwd=ROOT, stdout=out, stderr=err)
        record['pid'] = process.pid
        record_path.write_text(json.dumps(record, indent=2)+'\n')
        code = process.wait()
    record.update(actual_returncode=code, ended_utc=datetime.now(timezone.utc).isoformat(),
        marker_seen=marker in stdout.read_text(),
        stdout_sha256=hashlib.sha256(stdout.read_bytes()).hexdigest(),
        stderr_sha256=hashlib.sha256(stderr.read_bytes()).hexdigest())
    record_path.write_text(json.dumps(record, indent=2)+'\n')
    if code or stderr.read_text().strip() or not record['marker_seen']:
        raise RuntimeError('GAP '+stage+' failed; inspect retained logs')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--assume-nilpotent', action='store_true', required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    n, relators = source['generators'], source['relators']
    if type(n) is not int or n < 0 or not isinstance(relators, list):
        raise ValueError('nonnegative integer generator count and relator list required')
    for row in relators:
        if (not isinstance(row, list) or len(row)%2 or any(type(x) is not int for x in row)
            or any(not 1 <= row[i] <= n for i in range(0, len(row), 2))):
            raise ValueError('invalid indexed relator')
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output/'input.json').write_text(json.dumps(dict(generators=n, relators=relators), indent=2)+'\n')
    setup = '''Read("scripts/n5_general_fp_input.g");
Read("scripts/n5_general_pipeline.g");
Read("scripts/n5_class2_json.g");
N5Free := FreeGroup(%d);;
N5Gens := GeneratorsOfGroup(N5Free);;
N5ExtWord := function(v)
    local w,i;
    w:=One(N5Free);
    for i in [1,3..Length(v)-1] do w:=w*N5Gens[v[i]]^v[i+1];od;
    return w;
end;
N5Presentation := N5Free/List(%s,N5ExtWord);;
N5Model := N5FpNilpotent(N5Presentation,true);;
''' % (n, gap(relators))

    def write_stage(stage, body):
        path = output/(stage+'.g')
        path.write_text(setup+body+'\nPrint("PASS N5 general-fp '+stage+'\\n");\nQUIT;\n')
        run_gap(path, output, stage)

    write_stage('malcev', 'N5WriteCoordinateJson('+gap(str(output/'malcev.json'))+',N5Model.data);')
    data = json.loads((output/'malcev.json').read_text())
    lie = serial(decompose(data['structure_constants']))
    (output/'lie.json').write_text(json.dumps(lie, indent=2)+'\n')
    (output/'lie.g').write_text('N5ExpectedMalcev := '+gap(data)+';\nN5Rational := '+gap(lie)+';\n')
    binding = 'Read('+gap(str(output/'lie.g'))+');\nif N5Model.data<>N5ExpectedMalcev then Error("marked Malcev input changed");fi;\n'
    write_stage('branches', binding+'N5Central := N5GeneralCentralData(N5Model,N5ExpectedMalcev.structure_constants,N5Rational.projections);;\nN5WriteCoordinateJson('+gap(str(output/'branches.json'))+',N5Central);')
    central = json.loads((output/'branches.json').read_text())
    result = solve(central)
    (output/'decision.json').write_text(json.dumps(result, indent=2)+'\n')
    gap_result = dict(result, witness_branch=result['witness_branch'] or 0)
    (output/'decision.g').write_text('N5Central := '+gap(central)+';\nN5Decision := '+gap(gap_result)+';\n')
    replay = binding+'Read('+gap(str(output/'decision.g'))+');\n'+'''
Read("scripts/n5_general_fp_factors.g");
N5Words := [];;
if N5Decision.answer then
    N5Factors := N5GeneralFpFactors(N5Model,N5Central,N5Decision);;
    N5Words := List(N5Factors.words,ws->List(ws,w->ExtRepOfObj(UnderlyingElement(w))));;
fi;
'''
    replay += 'N5WriteCoordinateJson('+gap(str(output/'answer.json'))+',rec(answer:=N5Decision.answer,factor_words:=N5Words));'
    write_stage('factors', replay)
    print(json.dumps(dict(answer=result['answer'], factor_words_file=str(output/'answer.json'),
        scope='finite presentation promised nilpotent; no supplied class bound')))
    print('PASS N5 general fp command')


if __name__ == '__main__':
    main()
