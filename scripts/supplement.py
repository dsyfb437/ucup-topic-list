"""Fetch verified official materials missing from the UCup archive index."""
import json
from crawl import ROOT,fetch_file

TASKS = [
 ('s2-5','editorial',3,'https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2'),
 ('s2-5','editorial',4,'https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3'),
 ('s2-26','editorial',3,'https://scorelatam.naquadah.com.br/pda24/editorial.pdf'),
]

if __name__=='__main__':
    log=json.loads((ROOT/'data/fetch-log.json').read_text())
    for task in TASKS:
        if any(r['url']==task[3] and r['status']=='ok' for r in log):continue
        log.append(fetch_file(task))
    (ROOT/'data/fetch-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
    print('supplemental sources checked:',len(TASKS))
