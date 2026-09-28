#!/usr/bin/env python3
"""Index the frozen publisher HTML. Derived text is a finding aid, not an audit."""
from collections import Counter
import csv
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://shpilrain.ccny.cuny.edu/gworld/problems/'
CATEGORIES = [
 ('probout.html', 'O', 'Outstanding problems'),
 ('probaux.html', 'AUX', 'Auxiliary problems'),
 ('probfree.html', 'F', 'Free groups'),
 ('probone-rel.html', 'OR', 'One-relator groups'),
 ('probFP.html', 'FP', 'Finitely presented groups'),
 ('probBr.html', 'B', 'Mapping class groups'),
 ('probgrowth.html', 'G', 'Growth'),
 ('probeq.html', 'E', 'Equations in and over groups'),
 ('probalg.html', 'A', 'Algorithmic problems'),
 ('probcomplex.html', 'C', 'Complexity of algorithms'),
 ('probmat.html', 'MA', 'Groups of matrices'),
 ('probhyp.html', 'H', 'Hyperbolic and automatic groups'),
 ('probnil.html', 'N', 'Nilpotent groups'),
 ('probmet.html', 'M', 'Metabelian groups'),
 ('probsol.html', 'S', 'Solvable groups'),
 ('probact.html', 'GA', 'Group actions'),
]
ID = r'[A-Z]+\d+'

class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bits = []; self.links = []; self.current = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in {'p','br','div','h1','h2','h3','li'}: self.bits.append('\n')
        if tag == 'a' and a.get('href'):
            self.current = {'href':a['href'], 'label':''}
        # Keep superscript/subscript boundaries explicit in the search aid.
        if tag in {'sup','sub'}: self.bits.append('^{' if tag == 'sup' else '_{')
    def handle_endtag(self, tag):
        if tag in {'sup','sub'}: self.bits.append('}')
        if tag == 'a' and self.current is not None:
            self.links.append(self.current); self.current = None
    def handle_data(self, data):
        self.bits.append(data)
        if self.current is not None: self.current['label'] += data
    @property
    def text(self):
        return '\n'.join(' '.join(line.split()) for line in ''.join(self.bits).splitlines() if line.strip())


def parse(fragment):
    p=Plain(); p.feed(fragment); p.close(); return p


def uncomment(s):
    return re.sub(r'<!--.*?-->', lambda m: ''.join('\n' if c=='\n' else ' ' for c in m[0]), s, flags=re.S)


def sections(raw, prefix=None):
    """Return visible ID-led sections, including BR-led F27/F28/F30."""
    s=uncomment(raw)
    boundaries=list(re.finditer(r'<(?:p|br)\b[^>]*>',s,re.I))
    headers=[]
    for i,b in enumerate(boundaries):
        end=boundaries[i+1].start() if i+1<len(boundaries) else len(s)
        peek=parse(s[b.end():end]).text
        m=re.match(r'\s*(\*)?\s*\(('+ID+r')\)',peek)
        # The background page prints (05), (06), (07), but anchors them as O5–O7.
        if m is None and prefix is None and re.match(r'\s*\(0[567]\)',peek):
            peek=re.sub(r'^(\s*\()0([567]\))',r'\1O\2',peek)
            m=re.match(r'\s*(\*)?\s*\(('+ID+r')\)',peek)
        if m and (prefix is None or re.match(r'[A-Z]+',m[2])[0]==prefix):
            headers.append((m[2], b.start()))
    endbody=re.search(r'</body\s*>',s,re.I)
    last=endbody.start() if endbody else len(s)
    for i,(pid,start) in enumerate(headers):
        end=headers[i+1][1] if i+1<len(headers) else last
        yield pid,start,end,raw[start:end]


def save_json(path, obj):
    (ROOT/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')


def main():
    session=ROOT/'state/session.json'
    if session.exists() and json.loads(session.read_text())['phase']!='preparation':
        raise SystemExit('The catalogue is frozen after launch; record dated status updates separately.')
    manifest=json.loads((ROOT/'sources/manifest.json').read_text())
    rawdir=ROOT/'sources/raw'
    problems=[]; counts={}; seen=set(); backgrounds=[]
    for filename in ['Back.html','Back2.html']:
        raw=(rawdir/filename).read_bytes().decode('latin-1')
        for pid,start,end,fragment in sections(raw):
            text=parse(fragment).text
            heading=re.match(r'^(?:\([A-Z]+\d+\)(?:\s*[,\-]\s*)?)+',text)
            related=re.findall(ID,heading[0]) if heading else [pid]
            if heading and '-' in heading[0] and len(related)==2:
                left,right=related
                prefix=re.match(r'[A-Z]+',left)[0]
                related=[prefix+str(n) for n in range(int(re.search(r'\d+',left)[0]),int(re.search(r'\d+',right)[0])+1)]
            backgrounds.append({'problem_id':pid,'path':'sources/raw/'+filename,
                'start_byte':start,'end_byte':end,'start_line':raw[:start].count('\n')+1,
                'related_problem_ids':related,'text':text})
    hallraw=(rawdir/'Halloffame.html').read_bytes().decode('latin-1')
    hall=[]
    for part in re.split(r'<p\b[^>]*>',uncomment(hallraw),flags=re.I)[1:]:
        p=parse(part)
        for link in p.links:
            m=re.search(r'\(('+ID+r')',link['label'])
            if not m: continue
            pid=m[1]; suffix=link['label'][m.end():]
            parts=sorted(set(re.findall(r'\(([a-z])\)',suffix)))
            compact=re.match(r'([a-z])\)',suffix)
            if compact: parts=sorted(set(parts+[compact[1]]))
            anchor=unquote(urlsplit(link['href']).fragment)
            aid=re.search(ID,anchor)
            hall.append({'problem_id':pid,'parts':parts,
                'visible_label':' '.join(link['label'].split()),
                'attribution':' '.join(p.text.split()),'href_as_published':link['href'],
                'url':urljoin(BASE+'Halloffame.html',link['href']),
                'source':'sources/raw/Halloffame.html',
                'anchor_id_disagrees_with_label':bool(aid and aid[0]!=pid)})
    updates=json.loads((ROOT/'data/status_updates.json').read_text())
    for filename,prefix,title in CATEGORIES:
        rawbytes=(rawdir/filename).read_bytes(); raw=rawbytes.decode('latin-1')
        entries=list(sections(raw,prefix)); counts[title]=len(entries)
        for pid,start,end,fragment in entries:
            if pid in seen: raise ValueError('Duplicate problem: '+pid)
            seen.add(pid); parsed=parse(fragment); statement=parsed.text
            whole_star=bool(re.match(r'\s*\*\s*\('+pid+r'\)',statement))
            starred_parts=sorted(set(re.findall(r'\*\s*\(([a-z])\)',statement)))
            # Labels at line starts, or the initial inline label after ID/attribution.
            # Occurrences elsewhere may be cross-references; these are hints only.
            explicit_parts=sorted(set(re.findall(r'(?:^|\n)\s*\*?\s*\(([a-z])\)',statement)))
            first=statement.split('\n')[0]
            for m in re.finditer(r'\(([a-z])\)',first):
                if m[1] == 'a' or m[1] in starred_parts: explicit_parts.append(m[1])
            explicit_parts=sorted(set(explicit_parts+starred_parts))
            h=[e for e in hall if e['problem_id']==pid]
            b=[e for e in backgrounds if pid in e['related_problem_ids']]
            up=[e for e in updates if e['problem_id']==pid]
            reported=whole_star or bool(starred_parts or h or up)
            record={'id':pid,'category':title,'category_file':filename,
                'source_url':BASE+filename,'source_path':'sources/raw/'+filename,
                'source_sha256':hashlib.sha256(rawbytes).hexdigest(),
                'start_byte':start,'end_byte':end,'start_line':raw[:start].count('\n')+1,
                'fragment_sha256':hashlib.sha256(rawbytes[start:end]).hexdigest(),
                'statement_text':statement,'parts_detected':explicit_parts,
                'statement_audit':'pending; raw HTML and rendering have not been checked against a formal transcription',
                'site_heading_star':whole_star,'site_starred_parts':starred_parts,
                'hall_of_fame':h,'background_sections':b,
                'links':[dict(l, url=urljoin(BASE+filename,l['href'])) for l in parsed.links],
                'status_updates':up,
                'triage_status':'prior_resolution_evidence_scope_check_needed' if reported else 'status_unverified',
                'research_status':'not_started'}
            problems.append(record)
            out=ROOT/'problems'/pid; out.mkdir(parents=True,exist_ok=True)
            # Verbatim bytes allow direct reconstruction and hash checks.
            (out/'source-fragment.html').write_bytes(rawbytes[start:end])
            page='<!doctype html>\n<html><head><meta charset="utf-8">'+\
                 '<base href="../../sources/raw/"><title>GroupWorld '+pid+'</title></head><body>'+\
                 '<p><b>Archived excerpt '+pid+'.</b> Derived wrapper; compare the '+\
                 '<a href="'+filename+'">complete original page</a>. No statement audit has been completed.</p><hr>\n'+fragment+'\n</body></html>\n'
            (out/'statement.html').write_text(page)
            parts=', '.join(starred_parts) or 'none detected'
            (out/'README.md').write_text(f'# {pid} — {title}\n\n'
                f'[Offline statement](statement.html) · [Complete archived page](../../sources/raw/{filename}) · [Publisher]({BASE+filename})\n\n'
                f'Source begins at line {record["start_line"]}; byte range [{start}, {end}). '
                f'The raw fragment is stored in `source-fragment.html`.\n\n'
                f'Heading star: {whole_star}. Starred subparts: {parts}. '
                f'Hall of Fame entries: {len(h)}. Linked background sections indexed: {len(b)}.\n\n'
                'Current openness and exact scope require review. No solving has started. '
                'The machine-readable source evidence is in `data/problems.json`; '
                'the extracted text below is a search aid, not an authoritative transcription.\n\n'
                '```text\n'+statement+'\n```\n')
    unknown=sorted({h['problem_id'] for h in hall}-seen)
    if unknown: raise ValueError('Unknown Hall of Fame labels: '+str(unknown))
    # Catch omitted visible headings independently of paragraph structure.
    for filename,prefix,_ in CATEGORIES:
        raw=uncomment((rawdir/filename).read_bytes().decode('latin-1'))
        visible=set(re.findall(r'\(('+prefix+r'\d+)\)',parse(raw).text))
        parsed_ids={p['id'] for p in problems if p['category_file']==filename}
        if visible-parsed_ids: raise ValueError(f'Unindexed visible IDs in {filename}: {visible-parsed_ids}')
    save_json('data/problems.json',problems)
    save_json('data/hall_of_fame.json',hall)
    save_json('data/background_sections.json',backgrounds)
    summary={'numbered_entries':len(problems),'categories':counts,
        'heading_star_entries':sum(p['site_heading_star'] for p in problems),
        'entries_with_subpart_stars':sum(bool(p['site_starred_parts']) for p in problems),
        'hall_of_fame_links':len(hall),'hall_of_fame_distinct_entries':len({h['problem_id'] for h in hall}),
        'entries_with_prior_resolution_evidence':sum(p['triage_status'].startswith('prior_') for p in problems),
        'entries_without_heading_star_or_hall_entry_but_with_background':[
            p['id'] for p in problems if not p['site_heading_star'] and not p['hall_of_fame'] and p['background_sections']],
        'scope':'Counts are numbered entries, not open problems, atomic questions, or new results.'}
    save_json('data/catalog_summary.json',summary)
    fields=['id','category','site_heading_star','site_starred_parts','hall_of_fame_labels','triage_status','research_status','source_path','start_line']
    with (ROOT/'data/problems.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for p in problems:
            row={k:p[k] for k in fields if k in p}
            row['site_starred_parts']=','.join(p['site_starred_parts'])
            row['hall_of_fame_labels']='; '.join(e['visible_label'] for e in p['hall_of_fame'])
            w.writerow(row)
    lines=['# Problem catalogue','',f'{len(problems)} numbered entries in {len(CATEGORIES)} categories. These are **not** counts of currently open problems.',
        '', 'Stars and Hall of Fame entries report prior progress; inspect their exact scope and the archived background before selecting a target. '
        'Unmarked entries require a literature check too. [Status notes](../docs/STATUS_NOTES.md).','',
        '| ID | Category | Heading star | Starred parts | Hall of Fame labels |','|---|---|---|---|---|']
    for p in problems:
        lines.append(f'| [{p["id"]}](../problems/{p["id"]}/README.md) | {p["category"]} | '+('yes' if p['site_heading_star'] else '')+' | '+', '.join(p['site_starred_parts'])+' | '+'; '.join(e['visible_label'] for e in p['hall_of_fame'])+' |')
    (ROOT/'data/CATALOG.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
