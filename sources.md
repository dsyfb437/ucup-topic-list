# 来源与整理规则

优先使用 UCup 官方归档、官方评测站附件、AtCoder 官方题解；其次使用官网指向的委员会补充题解。拉美站补取原赛官方 Solution Sketches。

目录：[第 1 季](https://universal-cup-website.qoj.ac/?season=1)、[第 2 季](https://ucup.ac/archive/season2/)、[第 3 季](https://ucup.ac/archive/season3/)、[第 4 季](https://ucup.ac/archive/season4/)、[第 5 季](https://ucup.ac/)、[评测站目录](https://contest.ucup.ac/contests)。

- 先建立海外站白名单，再下载；中国站在链接提取阶段即排除。
- 题号采用 QOJ 镜像题号。日本原比赛可能重排或删题，按题名、原题解标题和已记录别名对应。
- 主专题和方法摘要逐题归纳；细分标签只对这些摘要做确定性匹配。
- 仅出现题目标题、TBD、外链提示或模型代码的条目进入缺失清单，不伪装成已完成分类。
- 随机算法、数值近似、RunTwice 等按原题解的适用前提收录，不能直接当作通用模板。
- 页码为 PDF 文件页序（包括标题页），不是页脚印刷页码。动画叠页仅为阅读去重，原 PDF 缓存只保留在本地。HTML 题解没有 PDF 页码。
- `data/sections.json` 保存提取正文；`data/annotations.txt` 保存分类；`data/problems.json` 为发布到本地题单的数据。
- `data/fetch-log.json` 保存状态、最终 URL 和 SHA-256。早期死链接失败仍保留，成功的替代链接另有记录，不能把历史失败直接当成最终缺失。

## 已使用的题解来源

| 赛站 | 原文 | 已分类题数 |
|---|---|---:|
| s1-4 Ukraine | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf) | 14 |
| s1-7 Zaporizhzhia | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf) | 13 |
| s1-8 Slovenia | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf) | 12 |
| s1-12 Ōokayama | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf) | 15 |
| s1-13 Iberia | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf) | 8 |
| s1-16 Gomel | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf) | 10 |
| s1-20 India | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf) | 14 |
| s2-2 SPb | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip) | 13 |
| s2-5 Northern | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1) | 6 |
| s2-5 Northern | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2) | 4 |
| s2-5 Northern | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3) | 2 |
| s2-6 Warsaw | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf) | 13 |
| s2-7 Two Capitals | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf) | 14 |
| s2-14 Southeastern Europe | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf) | 13 |
| s2-16 Run Twice | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf) | 11 |
| s2-18 Dolgoprudny | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf) | 10 |
| s2-19 Estonia | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf) | 10 |
| s2-20 Ōokayama | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf) | 16 |
| s2-21 Delft | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf) | 11 |
| s2-26 Latin America | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf) | 12 |
| s3-0 America | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf) | 13 |
| s3-1 St. Petersburg | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf) | 15 |
| s3-2 Zielona Gora | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf) | 13 |
| s3-4 Hongo | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf) | 17 |
| s3-5 Moscow | [原文](https://qoj.ac/blog/jiangly/blogs/941) | 13 |
| s3-6 Osijek | [原文](https://qoj.ac/blog/jiangly/blogs/948) | 6 |
| s3-7 Warsaw | [原文](https://qoj.ac/blog/jiangly/blogs/958) | 13 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10175) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10201) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10024) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10023) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10270) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10026) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10268) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10176) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10019) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10223) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/9999) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10177) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10025) | 1 |
| s3-11 Sumiyosi | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) | 1 |
| s3-13 Sendai | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf) | 15 |
| s3-18 Southeastern Europe | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf) | 12 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11085) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11403) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11291) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11464) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11086) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11224) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11092) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11084) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11470) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11083) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11225) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11222) | 1 |
| s3-21 Ōokayama | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) | 1 |
| s3-24 Poland | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf) | 12 |
| s3-27 London | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf) | 12 |
| s3-30 Northern | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf) | 11 |
| s3-31 Wroclaw | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf) | 12 |
| s3-32 Dhaka | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf) | 11 |
| s3-33 India | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf) | 14 |
| s3-34 Aobayama | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf) | 15 |
| s3-35 Kraków | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf) | 12 |
| s3-39 Tokyo | [原文](https://qoj.ac/blog/jiangly/blogs/1261) | 17 |
| s3-40 Potyczki | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf) | 14 |
| s4-0 America | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf) | 13 |
| s4-1 Korolyov | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf) | 11 |
| s4-2 Paris | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf) | 13 |
| s4-3 Polar | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf) | 11 |
| s4-8 Poland | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf) | 13 |
| s4-10 Wrocław | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf) | 12 |
| s4-11 Southeastern Europe | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf) | 12 |
| s4-13 Ōokayama | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf) | 12 |
| s4-16 Warsaw | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf) | 11 |
| s4-17 St. Petersburg | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf) | 13 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15605) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15693) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/16125) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/16122) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/16127) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15692) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/16136) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15852) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15607) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/16128) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15851) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15885) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15903) | 1 |
| s4-18 Hongō | [原文](https://atcoder.jp/contests/utpc2025/editorial/15904) | 1 |
| s4-19 Belarus | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf) | 13 |
| s4-20 India | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf) | 13 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18120) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17017) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17020) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17026) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17002) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18127) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18125) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18121) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17343) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18124) | 1 |
| s4-21 Kamigō | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17005) | 1 |
| s4-22 Kyoto | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf) | 15 |
| s4-25 Zagreb | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf) | 13 |
| s4-Extra-3 Osijek | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf) | 12 |
| s5-1 Nizhny Novgorod | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1) | 14 |
| s5-3 Gorkovskaya | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1) | 13 |
| s5-6 Hyakumanben | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1) | 14 |
