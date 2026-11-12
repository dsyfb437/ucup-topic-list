"""Download individual official editorials linked by allowed AtCoder indexes."""
import concurrent.futures,json,re,time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from crawl import ROOT,get

def fetch(t):
    sid,title,url,task=t
    path=ROOT/'sources'/f'{sid}-atcoder-{url.rsplit("/",1)[-1]}'
    if path.with_suffix('.html').exists():html=path.with_suffix('.html').read_text()
    else:
        time.sleep(2)
        r=get(url);html=r.text
        path.with_suffix('.html').write_text(html)
    s=BeautifulSoup(html,'html.parser')
    content=s.select_one('#main-container') or s
    txt=content.get_text('\n',strip=True);path.with_suffix('.txt').write_text(txt)
    return dict(stage_id=sid,title=title,url=url,task_url=task,path=str(path.with_suffix('.txt').relative_to(ROOT)),characters=len(txt))

def main():
    stages=json.loads((ROOT/'data/stages.json').read_text());tasks=[]
    for st in stages:
        if st['policy']!='overseas':continue
        extra=['https://atcoder.jp/contests/ttpc2024_1/editorial'] if st['id']=='s3-21' else []
        for url in st['editorials']+extra:
            if 'atcoder.jp' not in url:continue
            s=BeautifulSoup(get(url).text,'html.parser')
            for h in s.select('h3'):
                title=h.get_text(' ',strip=True)
                task=next((urljoin(url,a['href']) for a in h.select('a[href]') if '/tasks/' in a['href']),'')
                section=h.find_next_sibling('div')
                if section is None:continue
                lis=section.select('li')
                official=[li for li in lis if li.find('span',string='Official')]
                for li in official[:1]:
                    a=next((a for a in li.select('a[href]') if re.search(r'/editorial/\d+$',a['href'])),None)
                    if a:tasks.append((st['id'],title,urljoin(url,a['href']),task))
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:results=list(ex.map(fetch,tasks))
    (ROOT/'data/atcoder-editorials.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print('downloaded',len(results))

if __name__=='__main__':main()
