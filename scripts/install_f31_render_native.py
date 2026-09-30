#!/usr/bin/env python3
"""Fetch and unpack a few Ubuntu runtime libraries into ignored local scratch."""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.request import urlopen

root=Path(__file__).resolve().parents[1]
out=root/'scratch/f31-render-native';out.mkdir(parents=True,exist_ok=True)
specs=[('p/pango1.0','libpango-1.0-0','1.52.1'),
       ('p/pango1.0','libpangoft2-1.0-0','1.52.1'),
       ('h/harfbuzz','libharfbuzz-subset0','8.3.0'),
       ('libt/libthai','libthai0','0.1.29'),
       ('libd/libdatrie','libdatrie1','0.2.13')]
records=[]
for folder,name,version in specs:
    base='https://archive.ubuntu.com/ubuntu/pool/main/'+folder+'/'
    listing=urlopen(base,timeout=15).read().decode()
    candidates=sorted(set(re.findall('href="('+re.escape(name+'_'+version)+'[^"/]*_amd64.deb)"',listing)))
    assert candidates,(name,version)
    filename=candidates[-1]
    data=urlopen(base+filename,timeout=15).read()
    path=out/filename;assert not path.exists();path.write_bytes(data)
    subprocess.run(['dpkg-deb','-x',str(path),str(out/'root')],check=True)
    records.append({'url':base+filename,'filename':filename,'bytes':len(data),
                    'sha256':hashlib.sha256(data).hexdigest()})
    print('Unpacked',filename,flush=True)
record={'retrieved_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Ignored local rendering dependencies, not mathematical artifacts or system installation.',
        'packages':records}
(root/'research/certificates/F31-prior-construction/native-render-deps.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS local F31 native rendering dependencies')
