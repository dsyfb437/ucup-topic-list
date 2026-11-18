"""Build topic lists from editorial-reviewed annotations, with provenance and gaps."""
import collections,csv,hashlib,html,json,re,sys
from pathlib import Path

# Same as crawl.ROOT; computed here so building needs no network libraries.
ROOT=Path(__file__).resolve().parents[1]

DATE='2026-11-13'
PUBLIC='--local' not in sys.argv
TOPICS={
 'dp':'动态规划','ds':'数据结构','graph':'图论','tree':'树上算法',
 'nt':'数论','comb':'组合计数','poly':'多项式与线性代数','string':'字符串',
 'geo':'计算几何','greedy':'贪心','search':'搜索与二分','game':'博弈论',
 'prob':'概率期望与随机化','construct':'构造','interactive':'交互与信息编码',
 'bit':'位运算与状态压缩','numerical':'数值计算','impl':'模拟与基础实现',
}
# These tags are derived from reviewed method summaries, not raw keyword scraping.
FINE={
 '树形DP':r'树形 DP|子树.*DP|树上.*DP', '区间DP':r'区间 DP',
 '背包':r'背包','数位DP':r'数位 DP','子集DP':r'子集.*DP|子集状态|子集划分',
 'DP优化':r'优化.*DP|优化.*转移|DP.*优化|slope trick|凸代价|min-plus',
 '线段树':r'线段树|segtree','树状数组':r'树状数组|Fenwick|BIT',
 '持久化':r'持久|可持久','平衡树':r'Treap|Splay|AVL|平衡树|LCT',
 '单调栈与队列':r'单调栈|单调队列|双调栈', '分块':r'分块|轻重',
 '离线算法':r'离线|扫描线|整体二分|并行二分','分治':r'分治',
 '可撤销结构':r'撤销|rollback','点分治':r'点分治','换根DP':r'换根',
 'LCA与倍增':r'LCA|倍增|重链剖分','并查集':r'DSU|并查集|Union Find',
 '重构树':r'重构树|DSU-tree', '最短路':r'最短路|Dijkstra|BFS|Floyd|Bellman',
 '差分约束':r'差分约束|负环', '网络流与最小割':r'最大流|最小割|网络流|费用流|上下界流|运输费用流',
 '费用流':r'费用流', '匹配与Hall定理':r'匹配|Hall|独立集',
 '强连通与拓扑':r'SCC|强连通|拓扑|DAG|蕴含图',
 '双连通与割点':r'点双|割点|无桥|基本环', '最小生成树':r'MST|Kruskal|Boru|生成树',
 '欧拉图':r'Euler 迹|Euler 回|Euler 路', '2-SAT':r'2-SAT',
 '拟阵':r'拟阵|matroid', '线性基':r'线性基|异或基|带时间戳基',
 '高斯消元':r'高斯|Gauss|消元|线性方程', '矩阵':r'矩阵|Laplacian',
 'FFT与NTT卷积':r'FFT|NTT|卷积|convolution','生成函数':r'生成函数|EGF',
 '多项式插值与求值':r'插值|多点求值|Power Projection|Chirp|Taylor shift',
 '线性递推':r'BM |Bostan|求远项|线性递推',
 '容斥与反演':r'容斥|反演|Mobius', 'Catalan与反射原理':r'Catalan|反射原理|循环引理',
 'Stirling数':r'Stirling', '数论筛':r'Min25|筛法|totient 前缀',
 'gcd与欧几里得':r'gcd|欧几里得|Euclid|互素', 'CRT':r'CRT|中国剩余',
 '素数与分解':r'素因|素数|素因子|质因子|素数幂|原根',
 '连分数':r'连分数', '整除分块':r'整除分段|按整除商|数论分块',
 '数位与进位':r'数位|进位|十进制|三进制',
 'SOS与子集变换':r'SOS|Zeta', 'SG与Nim':r'Grundy|SG |Nim|nimber',
 '哈希':r'哈希|MinHash', 'Trie':r'Trie', '后缀数组':r'后缀数组|Suffix Array',
 '后缀自动机':r'SAM|后缀自动机|endpos', 'KMP与Z算法':r'KMP|Z 算法|Z算法',
 '回文与周期':r'回文|周期|border|循环移位',
 '凸包':r'凸包|Minkowski|上包络|下包络', '半平面交':r'半平面|半空间',
 '扫描线':r'扫描|极角|双指针', '三维几何':r'三维|空间垂直|立方体',
 '平面图':r'平面图|Euler 公式', '斜率优化':r'凸包优化|slope trick|李超|CHT',
 '势能与摊还':r'势能|摊还', '折半搜索':r'折半|meet-in-the-middle',
 '二分答案':r'二分|参数搜索|参数二分', '随机搜索':r'爬山|随机重启|随机交换|束搜索',
 '线性期望':r'线性期望|期望叠加|期望叠|期望.*贡献',
 'RunTwice与编码':r'RunTwice|两次运行|有限自动机|秘密共享|编码|校验',
 '数值积分':r'积分|Taylor 级数', '排列与逆序对':r'排列|逆序对',
 '括号与路径计数':r'括号|路径计数','仙人掌与函数图':r'仙人掌|函数图',
}

# Difficulty tiers from in-contest solve rate (solved teams / teams with >=1 solve).
# Measured data from contest.ucup.ac standings, not an estimated CF rating.
TIERS=[('签到',0.7),('简单',0.3),('中等',0.1),('困难',0.02),('极难',0.0)]

def tier(rate):
    return next(name for name,low in TIERS if rate>=low)

def difficulty():
    path=ROOT/'data/difficulty.json'
    if not path.exists():return {}
    d=json.loads(path.read_text());out={}
    for sid,st in d['stages'].items():
        for letter,n in st['solved'].items():
            rate=n/st['active_teams'] if st['active_teams'] else None
            out[f'{sid}-{letter}']=dict(solved_teams=n,active_teams=st['active_teams'],
                solve_rate=round(rate,4) if rate is not None else None,
                difficulty=tier(rate) if rate is not None else '')
    return out

def annotations():
    result={};sid=''
    for line in (ROOT/'data/annotations.txt').read_text().splitlines():
        line=line.strip()
        if not line or line.startswith('#'):continue
        if line.startswith('['):sid=line[1:-1];continue
        letter,tags,method=line.split('|',2);pid=sid+'-'+letter
        assert pid not in result,pid
        ts=[t.strip() for t in tags.split(',')]
        assert all(t in TOPICS for t in ts),(pid,ts)
        result[pid]=(ts,method)
    return result

def gap_reason(p):
    text=p['editorial_text']
    if 'TBD' in text:return '原题解标为 TBD'
    if p['stage_id']=='s1-5':return '官方题解为手写图像 PDF，未据题名猜分类'
    if p['stage_id']=='s1-3':return '官方只提供波兰语视频题解，尚无可核验文字稿'
    if p['stage_id']=='s1-19':return '旧目录只给视频题解，未取得对应文字题解'
    if p['id']=='s1-16-G':return '原题解只引用论文第 3 节，未展开解法'
    if p['id']=='s3-27-A':return '原题解只给论文阅读提示，未展开实现方法'
    if p['id']=='s3-32-K':return '原题解明确缺失，仅给模型代码链接'
    if p['stage_id']=='s3-6':return '委员会补充题解仅有标题或未收录此题'
    if p['stage_id']=='s3-3':return '已找到 CF Gym 官方题解附件，下载返回 403'
    if p['editorial_sources']:return '已取得材料，但未找到可对应的解法正文'
    return '官方目录与附件未提供可取得的文字题解'

def link(p):return f"[{p['id']} · {p['title'].replace('|','&#124;')}]({p['url']})"

def md_table(items,methods=False):
    out=['| 题目 | 赛站 | 专题 | 题解依据 |','|---|---|---|---|']
    for p in items:
        src=p['editorial_url'];loc=p['editorial_local']
        label=f'本地 p.{p["editorial_page"]}' if '.pdf#' in loc else '本地材料'
        source=f'[原文]({src})' if not loc else f'[原文]({src}) · [{label}]({loc})'
        if not loc and p.get('editorial_format')=='pdf':source+=f'（文件 p.{p["editorial_page"]}）'
        tags='、'.join(p['topics'])
        if methods:source=p['method']+'；'+source
        out.append(f'| {link(p)} | S{p["season"]} {p["station"]} | {tags} | {source} |')
    return '\n'.join(out)

def main():
    raw=json.loads((ROOT/'data/sections.json').read_text());stages=json.loads((ROOT/'data/stages.json').read_text())
    ann=annotations();ids={p['id'] for p in raw};assert set(ann)<=ids
    diff=difficulty()
    records=[];gaps=[]
    for p in raw:
        r={k:v for k,v in p.items() if k not in ['editorial_text','editorial_sources']}
        r.update(diff.get(p['id'],dict(solved_teams=None,active_teams=None,solve_rate=None,difficulty='')))
        r['editorial_sources']=[{k:v for k,v in s.items() if k!='path'} for s in p['editorial_sources']] if PUBLIC else p['editorial_sources']
        if p['id'] in ann:
            assert p['editorial_sources'] and len(p['editorial_text'])>60,p['id']
            assert 'TBD' not in p['editorial_text'],p['id']
            codes,method=ann[p['id']];src=p['editorial_sources'][0]
            local=Path(src['path']);pdf=local.with_suffix('.pdf');ht=local.with_suffix('.html')
            target=pdf if (ROOT/pdf).exists() else ht if (ROOT/ht).exists() else local
            assert (ROOT/target).exists(),target
            r.update(status='classified',topic_codes=codes,topics=[TOPICS[t] for t in codes],method=method,
                techniques=[tag for tag,pat in FINE.items() if re.search(pat,method,re.I)],
                editorial_url=src['url'],editorial_page=src['page'],
                editorial_format=target.suffix[1:],
                editorial_local='' if PUBLIC else target.as_posix()+(f'#page={src["page"]}' if target.suffix=='.pdf' else ''),
                classification_basis='题解归纳（非官方标签）')
        else:
            r.update(status='missing_editorial',topics=[],topic_codes=[],techniques=[],method='',
                editorial_url='',editorial_local='',editorial_page=None,gap_reason=gap_reason(p))
            gaps.append(r)
        records.append(r)
    classified=[r for r in records if r['status']=='classified'];over=[s for s in stages if s['policy']=='overseas']
    excluded=[s for s in stages if s['policy']!='overseas']
    for p in records:
        assert next(s for s in stages if s['id']==p['stage_id'])['policy']=='overseas'
    log=json.loads((ROOT/'data/fetch-log.json').read_text())
    allowed={s['id'] for s in over}
    assert all(r['stage_id'] in allowed for r in log)
    at=json.loads((ROOT/'data/atcoder-editorials.json').read_text());assert all(a['stage_id'] in allowed for a in at)
    counts={key:sum(key in p['topic_codes'] for p in classified) for key in TOPICS}
    finecounts=collections.Counter(t for p in classified for t in p['techniques'])
    stats=dict(date=DATE,overseas_stages=len(over),catalogued_problems=len(records),classified_problems=len(classified),
        missing_problems=len(gaps),classified_stages=len({p['stage_id'] for p in classified}),
        excluded_stages=len(excluded),topic_count=len(TOPICS),technique_count=len(finecounts),
        topic_counts=counts,technique_counts=dict(finecounts.most_common()),
        difficulty_tiers=[dict(name=n,min_rate=low) for n,low in TIERS],
        difficulty_counts={n:sum(p['difficulty']==n for p in records) for n,_ in TIERS},
        difficulty_missing=sum(not p['difficulty'] for p in records))
    (ROOT/'data/problems.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    (ROOT/'data/stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))
    cols=['id','season','stage','station','letter','title','status','difficulty','solved_teams','active_teams','solve_rate','topics','techniques','method','url','editorial_url','editorial_local','editorial_page','gap_reason']
    with (ROOT/'ucup-topics.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for p in records:w.writerow({k:';'.join(p[k]) if isinstance(p.get(k),list) else p.get(k,'') for k in cols})
    intro=f'# UCup 海外站专题算法题单\n\n截至 {DATE}，登记 {len(over)} 个海外站、{len(records)} 题；已依据题解分类 **{len(classified)} 题**，其余 **{len(gaps)} 题**见[缺失清单](coverage.md)。分类由题解归纳，不是官方标签。\n\n大陆、港澳台站均保留 VP；Ranoa 等无法确认地域的站点也保守排除。没有使用题目名字猜算法，没有编造难度或 CF 分数。\n\n难度取自 contest.ucup.ac 赛时榜单：通过队数 ÷ 至少过一题的队数，分为签到（≥70%）、简单（30–70%）、中等（10–30%）、困难（2–10%）、极难（<2%）。这是实测通过率，不是 CF 分数；镜像赛参赛队水平不一，只作选题参考。\n\n[可筛选浏览版](index.html) · [完整 CSV](ucup-topics.csv) · [JSON](data/problems.json) · [来源说明](sources.md) · [排除清单](excluded-stages.md)\n\n'
    intro=intro.replace('\n\n截至', '\n\n**由 GPT-6.1 Sol 整理的 UCup 海外赛站专题算法题单。**\n\n截至',1)
    if PUBLIC:
        intro=intro.replace('[可筛选浏览版](index.html)', '[在线筛选题单](https://dsyfb437.github.io/ucup-topic-list/)')
    doc=intro+'## 专题索引\n\n| 专题 | 题数（允许交叉） |\n|---|---:|\n'
    for key,name in TOPICS.items():doc+=f'| [{name}](topics/{key}.md) | {counts[key]} |\n'
    doc+='\n## 细分算法索引\n\n细分标签从已核对的核心方法提取；不是从原题解全文批量打词频标签。没有出现细分标签不代表题目不涉及该方法。\n\n'
    for tag,n in finecounts.most_common():doc+=f'- {tag}：{n} 题（在浏览版筛选或搜索）\n'
    doc+='\n## 用法\n\n先按当前训练专题筛选，再选题；默认按赛季和站次排列，**不是难度排序**。交互、RunTwice、随机输入专用题与普通算法题混合收录，方法摘要会说明其特殊性。先看题目，卡住再展开方法或打开题解。\n\n## 完整专题列表\n\n'
    for key,name in TOPICS.items():
        rows=[p for p in classified if key in p['topic_codes']]
        text=f'# {name}\n\n{len(rows)} 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。\n\n'+md_table(rows,True)+'\n'
        # Topic pages live one level below the source paths.
        text=text.replace('](sources/','](../sources/')
        (ROOT/'topics'/f'{key}.md').write_text(text)
        doc+=f'### {name}\n\n'+md_table(rows)+'\n\n'
    (ROOT/'UCup专题算法题单.md').write_text(doc)
    # Make gaps explicit even when an entire stage has no textual editorial.
    coverage=f'# 覆盖与缺失\n\n核对日期：{DATE}。共有 {len(classified)} 题已分类、{len(gaps)} 题未分类。下表的“无题解”指本次未取得可据以分类的正文，不等于断言全网不存在。\n\n## 分站覆盖\n\n| 赛季站次 | 站名 | 已分类 / 总题数 | 比赛入口 |\n|---|---|---:|---|\n'
    for st in over:
        rows=[p for p in records if p['stage_id']==st['id']];n=sum(p['status']=='classified' for p in rows)
        coverage+=f'| {st["id"]} | {st["name"]} | {n} / {len(rows)} | [比赛]({st["contest_url"]}) |\n'
    coverage+='\n## 尚未分类的题目\n\n| 题目 | 原因 |\n|---|---|\n'
    for p in gaps:coverage+=f'| {link(p)} | {p["gap_reason"]} |\n'
    (ROOT/'coverage.md').write_text(coverage)
    ex='# 保留 VP 的站点\n\n这里只保存目录级站名与排除理由；没有下载这些站的题面、题解或题目列表。Ranoa 地域未确认，继续保留。\n\n| 赛季站次 | 站名 | 排除原因 |\n|---|---|---|\n'
    for st in excluded:ex+=f'| {st["id"]} | {st["name"]} | {st["reason"]} |\n'
    (ROOT/'excluded-stages.md').write_text(ex)
    source='# 来源与整理规则\n\n优先使用 UCup 官方归档、官方评测站附件、AtCoder 官方题解；其次使用官网指向的委员会补充题解。拉美站补取原赛官方 Solution Sketches。\n\n目录：[第 1 季](https://universal-cup-website.qoj.ac/?season=1)、[第 2 季](https://ucup.ac/archive/season2/)、[第 3 季](https://ucup.ac/archive/season3/)、[第 4 季](https://ucup.ac/archive/season4/)、[第 5 季](https://ucup.ac/)、[评测站目录](https://contest.ucup.ac/contests)。\n\n- 先建立海外站白名单，再下载；中国站在链接提取阶段即排除。\n- 题号采用 QOJ 镜像题号。日本原比赛可能重排或删题，按题名、原题解标题和已记录别名对应。\n- 主专题和方法摘要逐题归纳；细分标签只对这些摘要做确定性匹配。\n- 仅出现题目标题、TBD、外链提示或模型代码的条目进入缺失清单，不伪装成已完成分类。\n- 随机算法、数值近似、RunTwice 等按原题解的适用前提收录，不能直接当作通用模板。\n- 页码为 PDF 文件页序（包括标题页），不是页脚印刷页码。动画叠页仅为阅读去重，原 PDF 保留。HTML 题解没有 PDF 页码。\n- `data/sections.json` 保存提取正文；`data/annotations.txt` 保存分类；`data/problems.json` 为发布到本地题单的数据。\n- `data/fetch-log.json` 保存状态、最终 URL 和 SHA-256。早期死链接失败仍保留，成功的替代链接另有记录，不能把历史失败直接当成最终缺失。\n\n## 已使用的题解文件\n\n| 赛站 | 原文 | 本地材料 | 已分类题数 |\n|---|---|---|---:|\n'
    if PUBLIC:
        source=source.replace('动画叠页仅为阅读去重，原 PDF 保留。','动画叠页仅为阅读去重，原 PDF 缓存只保留在本地。')
        source=source.replace('## 已使用的题解文件\n\n| 赛站 | 原文 | 本地材料 | 已分类题数 |\n|---|---|---|---:|', '## 已使用的题解来源\n\n| 赛站 | 原文 | 已分类题数 |\n|---|---|---:|')
    seen=set()
    for p in classified:
        k=(p['stage_id'],p['editorial_url'] if PUBLIC else p['editorial_local'].split('#')[0])
        if k in seen:continue
        seen.add(k);n=sum(x['stage_id']==k[0] and (x['editorial_url'] if PUBLIC else x['editorial_local'].split('#')[0])==k[1] for x in classified)
        source+=f'| {p["stage_id"]} {p["station"]} | [原文]({p["editorial_url"]}) | '+('' if PUBLIC else f'[材料]({k[1]}) | ')+f'{n} |\n'
    (ROOT/'sources.md').write_text(source)
    audit=dict(date=DATE,policy='Explicit overseas-stage allowlist; exclude mainland, Hong Kong, Macau, Taiwan and uncertain locations',
        downloaded_stage_ids=sorted({r['stage_id'] for r in log}),atcoder_stage_ids=sorted({a['stage_id'] for a in at}),
        excluded_stage_ids=sorted(s['id'] for s in excluded),excluded_content_downloads=0,
        unique_problem_ids=len(ids),classified_problem_ids=len(ann),all_annotations_have_local_editorial=True,
        all_records_have_problem_url=all(p['url'].startswith('https://') for p in records))
    (ROOT/'data/audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    template=(ROOT/'scripts/viewer.html').read_text()
    payload=json.dumps(dict(problems=records,stats=stats,topics=TOPICS),ensure_ascii=False).replace('</','<\\/')
    (ROOT/'index.html').write_text(template.replace('/*DATA*/',payload))
    readme=intro+'## 文件\n\n- `index.html`：本地离线筛选，方法摘要默认折叠，可勾选已练。\n- `UCup专题算法题单.md`：全部专题总表。\n- `topics/`：十八个主专题独立题单。\n- `ucup-topics.csv`、`data/problems.json`：可导入或二次筛选的数据。\n- `coverage.md`：每站覆盖率和逐题缺失原因。\n- `data/difficulty.json`：各站赛时榜单的每题通过队数。\n- `excluded-stages.md`：中国及地域未确认站点清单。\n- `sources/`：原始材料与提取文本，仅供本地个人训练。\n\n## 更新\n\n需要 Python 3、requests、beautifulsoup4 和系统命令 `pdftotext`。当前没有把本项目接入训练工作台，也没有修改现有训练计划。\n\n```bash\npython3 -m venv .venv\n.venv/bin/pip install -r requirements.txt\n.venv/bin/python scripts/crawl.py\n.venv/bin/python scripts/enrich.py\n.venv/bin/python scripts/supplement.py\n.venv/bin/python scripts/atcoder_editorials.py\n.venv/bin/python scripts/extract.py\n.venv/bin/python scripts/difficulty.py   # 赛时榜单通过数，--refresh 重新抓取\n# 核对新题解，更新 data/annotations.txt 后生成\n.venv/bin/python scripts/build.py\n```\n\n浏览版通过 `file://` 打开即可使用，无需服务。勾选记录保存在当前浏览器的 localStorage；换浏览器不会自动同步，可用页面的导出/导入保存。\n'
    readme=readme.replace('当前没有把本项目接入训练工作台，也没有修改现有训练计划。','下载的原始题面、题解及其全文提取缓存不随 Git 提交；运行更新脚本后会重新生成。默认生成适合公开仓库的原站链接，使用 `scripts/build.py --local` 可生成本地材料链接。')
    readme=readme.replace('## 文件','题面和原始题解版权归各自作者；本仓库提供分类、方法摘要、原文链接和整理脚本。详见 [整理说明](NOTICE.md)。\n\n## 文件',1)
    readme=readme.replace('`sources/`：原始材料与提取文本，仅供本地个人训练。','`sources/`：本地下载缓存，已加入 `.gitignore`，公开仓库不包含。')
    readme=readme.replace('`index.html`：本地离线筛选', '`index.html`：GitHub Pages 在线浏览，也支持下载后离线筛选')
    readme=readme.replace('浏览版通过 `file://` 打开即可使用，无需服务。', '浏览版可通过 [GitHub Pages](https://dsyfb437.github.io/ucup-topic-list/) 直接访问，也可下载后通过 `file://` 离线打开。Pages 从 `main` 分支根目录自动发布，后续推送会自动更新。')
    (ROOT/'README.md').write_text(readme)
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
