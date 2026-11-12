"""Fetch only allowlisted overseas UCup stages; never crawl an archive recursively.

Run with Python 3 + requests + beautifulsoup4; PDF extraction needs pdftotext.
"""
import concurrent.futures, hashlib, io, json, re, subprocess, zipfile
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
ALLOW = {
 1: {3,4,5,7,8,12,13,16,19,20},
 2: {2,5,6,7,14,16,18,19,20,21,26,27},
 3: {0,1,2,3,4,5,6,7,11,13,18,21,24,27,30,31,32,33,34,35,39,40},
 4: {0,1,2,3,8,'Extra-3',10,11,13,16,17,18,19,20,21,22,25},
 5: {1,2,3,6},
}
S1 = [(3,'Poland'),(4,'Ukraine'),(5,'Osijek'),(7,'Zaporizhzhia'),(8,'Slovenia'),(12,'Ōokayama'),(13,'Iberia'),(16,'Gomel'),(19,'America'),(20,'India')]
HEADERS = {'User-Agent':'UCup-topic-study/1.0 (personal training archive; overseas allowlist)'}

def get(url):
    r=requests.get(url,headers=HEADERS,timeout=50);r.raise_for_status();return r

def metadata():
    stages=[]
    for season in [2,3,4,5]:
        url=f'https://ucup.ac/archive/season{season}/' if season<5 else 'https://ucup.ac/'
        html=get(url).text
        (ROOT/'sources'/f'season{season}-index.html').write_text(html)
        for row in BeautifulSoup(html,'html.parser').select('tbody tr'):
            cells=row.find_all('td')
            if len(cells)<5:continue
            date,num,name=[x.get_text(' ',strip=True) for x in cells[:3]]
            number=int(num) if num.isdigit() else num
            allowed=number in ALLOW[season]
            links=lambda i:[urljoin(url,a['href']) for a in cells[i].select('a[href]')]
            stages.append(dict(id=f's{season}-{num}',season=season,stage=num,name=name,date=date,
                policy='overseas' if allowed else 'excluded',
                reason='' if allowed else ('地域未确认，保守排除' if name in ['Metropolis','UCup Online','2026 Finals'] else '中国赛站，保留 VP'),
                index_url=url,statements=links(3) if allowed else [],editorials=links(4) if allowed else [],
                contest_url=(links(5) or [''])[0] if allowed and len(cells)>5 else ''))
    for num,name in S1:
        base='https://assets.ucup.ac/'
        stages.append(dict(id=f's1-{num}',season=1,stage=str(num),name=name,date='',policy='overseas',reason='',
            index_url='https://universal-cup-website.qoj.ac/?season=1',
            statements=[base+f'statements/statements-1-{num}.pdf'],
            editorials=[base+f'tutorials/tutorials-1-{num}.pdf'] if num not in [3,19] else [],contest_url=''))
    stages.sort(key=lambda s:(s['season'],int(s['stage']) if s['stage'].isdigit() else 100))
    (ROOT/'data/stages.json').write_text(json.dumps(stages,ensure_ascii=False,indent=2))
    return stages

def fetch_file(task):
    sid,kind,idx,url=task
    stem=f'{sid}-{kind}-{idx}'
    out=ROOT/'sources'/stem
    result=dict(stage_id=sid,kind=kind,url=url,status='error')
    try:
        r=get(url)
        data=r.content
        suffix='.pdf' if data.startswith(b'%PDF') else '.zip' if data.startswith(b'PK') else '.html'
        path=out.with_suffix(suffix);path.write_bytes(data)
        result.update(status='ok',path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),resolved_url=r.url)
        if suffix=='.pdf':
            subprocess.run(['pdftotext','-layout',str(path),str(out.with_suffix('.txt'))],check=True,capture_output=True)
        elif suffix=='.html':
            soup=BeautifulSoup(r.text,'html.parser')
            main=soup.select_one('#main-container') or soup.select_one('main') or soup
            out.with_suffix('.txt').write_text(main.get_text('\n',strip=True))
        else:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for i,n in enumerate(z.namelist()):
                    if n.lower().endswith('.pdf'):
                        p=out.with_name(stem+f'-part{i}').with_suffix('.pdf');p.write_bytes(z.read(n))
                        subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
        result['characters']=sum(len(p.read_text()) for p in (ROOT/'sources').glob(stem+'*.txt'))
    except Exception as e:result['error']=str(e)
    return result

def main():
    (ROOT/'sources').mkdir(parents=True,exist_ok=True)
    (ROOT/'data').mkdir(parents=True,exist_ok=True)
    stages=metadata()
    tasks=[]
    for s in stages:
        if s['policy']!='overseas':continue
        for kind,key in [('statement','statements'),('editorial','editorials')]:
            # Prefer an official PDF over a duplicate supplemental blog.
            for i,url in enumerate(s[key][:1]):tasks.append((s['id'],kind,i,url))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(fetch_file,tasks))
    (ROOT/'data/fetch-log.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps({'stages':sum(s['policy']=='overseas' for s in stages),'files':len(results),'errors':[r for r in results if r['status']!='ok']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
