"""Print compact editorial evidence for annotation; no classifications from titles."""
import json,re,sys
from crawl import ROOT
KEY = re.compile(r'dynamic|\bdp\b|greedy|segment tree|fenwick|binary search|convol|polynomial|\bfft\b|\bntt\b|convex|dijkstra|shortest|flow|match|disjoint|\bdsu\b|\blca\b|centroid|heavy.light|suffix|\bkmp\b|z.function|hash|grundy|nim|sprague|gauss|matrix|determin|mobius|möbius|inclusion|exclusion|generat|random|probab|expect|modul|prime|factor|dfs|bfs|topolog|divide.and.conquer|sqrt|bitset|linear basis|meet.in.the.middle|rollback|\bset\b|\bmap\b|interactive|ternary|sweep|sorted|\bsort|manacher|cartesian|numerical|integral|欧拉|背包|线性基|二分|差分|分治|线段树|树状数组|贪心|动态规划|DP|ハッシュ|セグメント|畳み込み|二分|貪欲|行列|多項式|オイラー|最短|双対|フロー|包除|累積|ゲーム|Grund|DFS|BFS|DP|ダイクストラ|動的|確率|期待|乱択|逆元|数え上げ|トポロジ|ガウス|重心|FFT|NTT',re.I)
allp=json.loads((ROOT/'data/sections.json').read_text())
for p in allp:
    if sys.argv[1:] and p['stage_id'] not in sys.argv[1:]:continue
    t=p['editorial_text'];lines=t.splitlines()
    if len(t)<100:print(p['id'],p['title'],'MISSING');continue
    hits=[i for i,l in enumerate(lines) if KEY.search(l)]
    chosen=[]
    for i in hits:
        if not any(abs(i-j)<2 for j in chosen):chosen.append(i)
    limit=1300 if '--long' in sys.argv else 620
    evidence=' / '.join(' '.join(lines[max(0,i-1):i+2]) for i in chosen)
    print('\n'+p['id']+' '+p['title']+' ['+str(len(t))+']\n'+(evidence[:limit] if evidence else t[:limit]))
