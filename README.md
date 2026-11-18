# UCup 海外站专题算法题单

**由 GPT-6.1 Sol 整理的 UCup 海外赛站专题算法题单。**

截至 2026-11-13，登记 66 个海外站、853 题；已依据题解分类 **750 题**，其余 **103 题**见[缺失清单](coverage.md)。分类由题解归纳，不是官方标签。

大陆、港澳台站均保留 VP；Ranoa 等无法确认地域的站点也保守排除。没有使用题目名字猜算法，没有编造难度或 CF 分数。

难度取自 contest.ucup.ac 赛时榜单：通过队数 ÷ 至少过一题的队数，分为签到（≥70%）、简单（30–70%）、中等（10–30%）、困难（2–10%）、极难（<2%）。这是实测通过率，不是 CF 分数；镜像赛参赛队水平不一，只作选题参考。

[在线筛选题单](https://dsyfb437.github.io/ucup-topic-list/) · [完整 CSV](ucup-topics.csv) · [JSON](data/problems.json) · [来源说明](sources.md) · [排除清单](excluded-stages.md)

题面和原始题解版权归各自作者；本仓库提供分类、方法摘要、原文链接和整理脚本。详见 [整理说明](NOTICE.md)。

## 文件

- `index.html`：GitHub Pages 在线浏览，也支持下载后离线筛选，方法摘要默认折叠，可勾选已练。
- `UCup专题算法题单.md`：全部专题总表。
- `topics/`：十八个主专题独立题单。
- `ucup-topics.csv`、`data/problems.json`：可导入或二次筛选的数据。
- `coverage.md`：每站覆盖率和逐题缺失原因。
- `data/difficulty.json`：各站赛时榜单的每题通过队数。
- `excluded-stages.md`：中国及地域未确认站点清单。
- `sources/`：本地下载缓存，已加入 `.gitignore`，公开仓库不包含。

## 更新

需要 Python 3、requests、beautifulsoup4 和系统命令 `pdftotext`。下载的原始题面、题解及其全文提取缓存不随 Git 提交；运行更新脚本后会重新生成。默认生成适合公开仓库的原站链接，使用 `scripts/build.py --local` 可生成本地材料链接。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/crawl.py
.venv/bin/python scripts/enrich.py
.venv/bin/python scripts/supplement.py
.venv/bin/python scripts/atcoder_editorials.py
.venv/bin/python scripts/extract.py
.venv/bin/python scripts/difficulty.py   # 赛时榜单通过数，--refresh 重新抓取
# 核对新题解，更新 data/annotations.txt 后生成
.venv/bin/python scripts/build.py
```

浏览版可通过 [GitHub Pages](https://dsyfb437.github.io/ucup-topic-list/) 直接访问，也可下载后通过 `file://` 离线打开。Pages 从 `main` 分支根目录自动发布，后续推送会自动更新。勾选记录保存在当前浏览器的 localStorage；换浏览器不会自动同步，可用页面的导出/导入保存。
