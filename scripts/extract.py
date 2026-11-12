"""Split local editorials into problem sections; keep page numbers for auditing."""
import json,re,unicodedata
from pathlib import Path
from difflib import SequenceMatcher
from crawl import ROOT

def norm(t):
    t=unicodedata.normalize('NFKD',t).lower()
    return ''.join(c for c in t if c.isalnum())

# Editorials retain original contest names/order, while UCup sometimes renames tasks.
ALIASES={
 's3-0':{'Magic Bean Cube':'F'}, 's3-1':{'Whole World':'F'}, 's1-20':{'Graph and Colors':'M'},
 's2-5':{'Young':'F','Two Missing Numbers/Nimbers':'D'},
 's3-13':{'012Grid':'A','Shift Grid':'C','(mod HW+1)':'J'},
 's2-16':{'Noise Halving':'D','Graph Mark':'F'},
 's3-31':{'Expressions':'E'},
 's4-2':{'Framboise':'F'},'s4-16':{'Three Circles':'A'},
 's3-34':{'Another Long Sequence':'F','Convex Hull of':'G'},
}

def split_stage(st):
    sid=st['id'];probs=st.get('problems',[]);names={norm(p['title']):p['letter'] for p in probs}
    names.update({norm(k):v for k,v in ALIASES.get(sid,{}).items()})
    sections={p['letter']:[] for p in probs};sources={p['letter']:[] for p in probs}
    logs=json.loads((ROOT/'data/fetch-log.json').read_text())
    for f in sorted((ROOT/'sources').glob(sid+'-editorial-*.txt')):
        txt=f.read_text()
        if sid=='s2-16':
            txt='\f'.join('' if len(re.findall(r'Problem [A-Z]:',page))>4 else page for page in txt.split('\f'))
        if len(txt)<100 or '<html' in txt:continue
        # AtCoder index pages are catalogs, not editorials.
        if 'Editorial\n-' in txt[:200] or 'There is no editorial yet' in txt:continue
        idx=re.search(r'-editorial-(\d+)',f.stem)[1]
        rec=next((r for r in logs if r['stage_id']==sid and r['kind']=='editorial' and r.get('path','').split('/')[-1].startswith(sid+'-editorial-'+idx+'.')),None)
        url=rec.get('resolved_url',rec['url']) if rec else ''
        current=None;page=1
        for raw in txt.splitlines(keepends=True):
            if '\f' in raw:page+=raw.count('\f')
            line=raw.strip().replace('\x15','-');n=norm(line);letter=None
            if sid=='s3-21':
                line=re.sub(r'^Div\.\s*[12]\s+','',line)
                n=norm(line)
            if not n:continue
            # Exact title on a slide, title after a letter, or explicit Problem Tutorial.
            for name,l in names.items():
                if not name:continue
                if n==name or n=='problemtutorial'+name or (re.match(r'^(?:Problem )?[A-Z][. :\-–—]',line) and (n[1:]==name or n.startswith('problem') and n[8:]==name or sid=='s2-16' and n.startswith('problem') and n[8:].startswith(name))) or (sid=='s1-20' and n.endswith(name) and len(n)<len(name)+25):
                    letter=l;break
            m=re.match(r'^(?:Problem\s+)?([A-Z])(?:\s*[.\-–—:．]\s+|$)',line)
            if sid=='s2-2' and re.match(r'^[BEFIKM] \(',line):letter=line[0]
            if letter is None and m and m[1] in sections:
                l=m[1]
                if re.match(r'^Problem [A-Z](?:\.|$)',line):letter=l
                elif sid in ['s3-24','s3-40','s4-8'] and re.match(r'^[A-Z]\s*[.\-–—]\s*',line):letter=l
                elif sid=='s3-35' and line==l:letter=l
            if letter:
                current=letter
                src=dict(path=str(f.relative_to(ROOT)),url=url,page=page)
                if src not in sources[current]:sources[current].append(src)
            elif sid in ['s3-13','s3-21','s3-34'] and re.match(r'^[A-Z]\s*-\s*\S',line):
                # A booklet may also contain tasks omitted from the UCup mirror.
                current=None
            if current:sections[current].append((page,line))
    # The individual AtCoder editorial title matches UCup's task title.
    atpath=ROOT/'data/atcoder-editorials.json'
    if atpath.exists():
        for a in json.loads(atpath.read_text()):
            if a['stage_id']!=sid:continue
            name=norm(re.sub(r'^[A-Z]\s*-\s*','',a['title']))
            l=names.get(name)
            if l:
                sections[l]=[(1,line) for line in (ROOT/a['path']).read_text().splitlines()]
                sources[l]=[dict(path=a['path'],url=a['url'],page=1)]
    out=[]
    for p in probs:
        # Remove repeated animation-slide lines, preserving the first occurrence.
        seen=set();lines=[]
        for page,line in sections[p['letter']]:
            if line not in seen:seen.add(line);lines.append(line)
        text='\n'.join(lines)
        out.append(dict(id=sid+'-'+p['letter'],stage_id=sid,season=st['season'],stage=st['stage'],station=st['name'],**p,
            editorial_text=text,editorial_sources=sources[p['letter']]))
    return out

def main():
    stages=json.loads((ROOT/'data/stages.json').read_text());out=[]
    for st in stages:
        if st['policy']=='overseas':out.extend(split_stage(st))
    (ROOT/'data/sections.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print('problems',len(out),'with sections',sum(len(x['editorial_text'])>120 for x in out))

if __name__=='__main__':main()
