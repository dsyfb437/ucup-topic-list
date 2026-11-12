"""Resolve overseas contest/problem links and attachment fallbacks from the judge."""
import concurrent.futures, json, re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from crawl import ROOT, get, fetch_file

def stage_id(title):
    m=re.search(r'The (\d+)(?:st|nd|rd|th) Universal Cup\. (Extra )?Stage (\d+):',title)
    if not m:return None
    return f's{m[1]}-'+('Extra-' if m[2] else '')+m[3]

def inspect(s):
    if not s.get('contest_url'):return s,[]
    url=s['contest_url'].replace('https://qoj.ac/','https://contest.ucup.ac/')
    try:
        r=get(url);soup=BeautifulSoup(r.text,'html.parser')
        (ROOT/'sources'/f"{s['id']}-contest.html").write_text(r.text)
        problems=[]
        for tr in soup.select('table tr'):
            cells=tr.find_all('td')
            if len(cells)<2:continue
            letter=cells[0].get_text(' ',strip=True)
            links=[a for a in tr.select('a[href]') if re.search(r'/problem/\d+',a['href'])]
            if re.fullmatch('[A-Z]',letter) and links:
                a=links[0];problems.append(dict(letter=letter,title=a.get_text(' ',strip=True),url=urljoin(url,a['href'])))
        s['problems']=problems
        attachments=[]
        for a in soup.select('a[href]'):
            label=a.get_text(' ',strip=True)
            if re.search(r'Tutorial|Editorial|Solution',label,re.I):
                href=urljoin(url,a['href'])
                if 'download' in href or 'files/' in href or '.pdf' in href or '.zip' in href:attachments.append(href)
        s['attachment_editorials']=list(dict.fromkeys(attachments))
        return s,[]
    except Exception as e:return s,[str(e)]

def main():
    stages=json.loads((ROOT/'data/stages.json').read_text())
    html=get('https://contest.ucup.ac/contests').text
    (ROOT/'sources'/'judge-contests-index.html').write_text(html)
    for tr in BeautifulSoup(html,'html.parser').select('table tr'):
        sid=stage_id(tr.get_text(' ',strip=True))
        if not sid:continue
        existing=next((s for s in stages if s['id']==sid),None)
        link=next((a for a in tr.select('a[href]') if re.fullmatch(r'/contest/\d+',a['href'])),None)
        if not link:continue
        if existing is None:
            season=int(sid.split('-')[0][1:]);name=link.get_text(' ',strip=True).split(':',1)[-1].strip()
            allowed=sid=='s5-Extra-1'
            existing=dict(id=sid,season=season,stage=sid.split('-',1)[1],name=name,date='',policy='overseas' if allowed else 'excluded',
                reason='' if allowed else ('地域未确认，保守排除' if name=='Ranoa' else '中国赛站或非专题范围，保留 VP'),
                index_url='https://contest.ucup.ac/contests',statements=[],editorials=[],contest_url='')
            stages.append(existing)
        if existing['policy']=='overseas':existing['contest_url']=urljoin('https://qoj.ac/',link['href'])
    over=[s for s in stages if s['policy']=='overseas']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:updated=list(ex.map(inspect,over))
    for s,errors in updated:
        if errors:s['inspect_errors']=errors
        stages[stages.index(next(x for x in stages if x['id']==s['id']))]=s
    log=json.loads((ROOT/'data/fetch-log.json').read_text())
    tasks=[]
    for s in over:
        sid=s['id']
        for r in log:
            if r['stage_id']!=sid:continue
            if r['status']=='error' or (r['url'].startswith('https://qoj.ac/') and r.get('characters',0)<1000):
                url=r['url'].replace('https://qoj.ac/','https://contest.ucup.ac/')
                if s['season']==1:
                    url=f"https://contest.ucup.ac/files/ucup/{'statements' if r['kind']=='statement' else 'tutorials'}/{ 'statements' if r['kind']=='statement' else 'tutorials'}-1-{s['stage']}.pdf"
                if url!=r['url']:tasks.append((sid,r['kind'],1,url))
        if not s['editorials']:
            for i,u in enumerate(s.get('attachment_editorials',[])[:1]):tasks.append((sid,'editorial',2+i,u))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:log.extend(ex.map(fetch_file,tasks))
    (ROOT/'data/stages.json').write_text(json.dumps(stages,ensure_ascii=False,indent=2))
    (ROOT/'data/fetch-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
    print(json.dumps({'overseas':len(over),'problem_links':sum(len(s.get('problems',[])) for s in over),'fallback_files':len(tasks),'remaining_errors':[r['url'] for r in log if r['status']=='error']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
