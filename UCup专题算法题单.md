# UCup 海外站专题算法题单

**由 GPT-6.1 Sol 整理的 UCup 海外赛站专题算法题单。**

截至 2026-11-13，登记 66 个海外站、853 题；已依据题解分类 **750 题**，其余 **103 题**见[缺失清单](coverage.md)。分类由题解归纳，不是官方标签。

大陆、港澳台站均保留 VP；Ranoa 等无法确认地域的站点也保守排除。没有使用题目名字猜算法，没有编造难度或 CF 分数。

[在线筛选题单](https://dsyfb437.github.io/ucup-topic-list/) · [完整 CSV](ucup-topics.csv) · [JSON](data/problems.json) · [来源说明](sources.md) · [排除清单](excluded-stages.md)

## 专题索引

| 专题 | 题数（允许交叉） |
|---|---:|
| [动态规划](topics/dp.md) | 163 |
| [数据结构](topics/ds.md) | 146 |
| [图论](topics/graph.md) | 138 |
| [树上算法](topics/tree.md) | 55 |
| [数论](topics/nt.md) | 71 |
| [组合计数](topics/comb.md) | 136 |
| [多项式与线性代数](topics/poly.md) | 80 |
| [字符串](topics/string.md) | 67 |
| [计算几何](topics/geo.md) | 69 |
| [贪心](topics/greedy.md) | 121 |
| [搜索与二分](topics/search.md) | 79 |
| [博弈论](topics/game.md) | 22 |
| [概率期望与随机化](topics/prob.md) | 75 |
| [构造](topics/construct.md) | 118 |
| [交互与信息编码](topics/interactive.md) | 24 |
| [位运算与状态压缩](topics/bit.md) | 80 |
| [数值计算](topics/numerical.md) | 11 |
| [模拟与基础实现](topics/impl.md) | 27 |

## 细分算法索引

细分标签从已核对的核心方法提取；不是从原题解全文批量打词频标签。没有出现细分标签不代表题目不涉及该方法。

- 二分答案：55 题（在浏览版筛选或搜索）
- 线段树：32 题（在浏览版筛选或搜索）
- 扫描线：30 题（在浏览版筛选或搜索）
- 匹配与Hall定理：26 题（在浏览版筛选或搜索）
- 排列与逆序对：25 题（在浏览版筛选或搜索）
- FFT与NTT卷积：21 题（在浏览版筛选或搜索）
- 最短路：21 题（在浏览版筛选或搜索）
- 素数与分解：20 题（在浏览版筛选或搜索）
- 凸包：20 题（在浏览版筛选或搜索）
- 矩阵：19 题（在浏览版筛选或搜索）
- gcd与欧几里得：19 题（在浏览版筛选或搜索）
- 回文与周期：18 题（在浏览版筛选或搜索）
- 离线算法：18 题（在浏览版筛选或搜索）
- 数位与进位：17 题（在浏览版筛选或搜索）
- 容斥与反演：16 题（在浏览版筛选或搜索）
- LCA与倍增：16 题（在浏览版筛选或搜索）
- 强连通与拓扑：15 题（在浏览版筛选或搜索）
- 分治：15 题（在浏览版筛选或搜索）
- 并查集：14 题（在浏览版筛选或搜索）
- 树状数组：14 题（在浏览版筛选或搜索）
- RunTwice与编码：14 题（在浏览版筛选或搜索）
- 生成函数：13 题（在浏览版筛选或搜索）
- 哈希：13 题（在浏览版筛选或搜索）
- DP优化：13 题（在浏览版筛选或搜索）
- 括号与路径计数：12 题（在浏览版筛选或搜索）
- 多项式插值与求值：12 题（在浏览版筛选或搜索）
- 高斯消元：12 题（在浏览版筛选或搜索）
- 背包：12 题（在浏览版筛选或搜索）
- 最小生成树：12 题（在浏览版筛选或搜索）
- 树形DP：10 题（在浏览版筛选或搜索）
- 网络流与最小割：10 题（在浏览版筛选或搜索）
- 分块：9 题（在浏览版筛选或搜索）
- 势能与摊还：9 题（在浏览版筛选或搜索）
- 三维几何：8 题（在浏览版筛选或搜索）
- 子集DP：6 题（在浏览版筛选或搜索）
- Catalan与反射原理：6 题（在浏览版筛选或搜索）
- 双连通与割点：6 题（在浏览版筛选或搜索）
- 区间DP：6 题（在浏览版筛选或搜索）
- 单调栈与队列：6 题（在浏览版筛选或搜索）
- 可撤销结构：5 题（在浏览版筛选或搜索）
- SG与Nim：5 题（在浏览版筛选或搜索）
- 费用流：5 题（在浏览版筛选或搜索）
- 随机搜索：5 题（在浏览版筛选或搜索）
- 线性基：5 题（在浏览版筛选或搜索）
- 仙人掌与函数图：4 题（在浏览版筛选或搜索）
- 换根DP：4 题（在浏览版筛选或搜索）
- 斜率优化：4 题（在浏览版筛选或搜索）
- 半平面交：4 题（在浏览版筛选或搜索）
- CRT：3 题（在浏览版筛选或搜索）
- KMP与Z算法：3 题（在浏览版筛选或搜索）
- 平衡树：3 题（在浏览版筛选或搜索）
- 线性期望：3 题（在浏览版筛选或搜索）
- 线性递推：3 题（在浏览版筛选或搜索）
- 持久化：3 题（在浏览版筛选或搜索）
- 折半搜索：3 题（在浏览版筛选或搜索）
- 后缀数组：3 题（在浏览版筛选或搜索）
- SOS与子集变换：3 题（在浏览版筛选或搜索）
- 差分约束：3 题（在浏览版筛选或搜索）
- 整除分块：3 题（在浏览版筛选或搜索）
- 欧拉图：3 题（在浏览版筛选或搜索）
- 拟阵：3 题（在浏览版筛选或搜索）
- 点分治：2 题（在浏览版筛选或搜索）
- 数值积分：2 题（在浏览版筛选或搜索）
- 连分数：2 题（在浏览版筛选或搜索）
- 数位DP：1 题（在浏览版筛选或搜索）
- Stirling数：1 题（在浏览版筛选或搜索）
- Trie：1 题（在浏览版筛选或搜索）
- 平面图：1 题（在浏览版筛选或搜索）
- 2-SAT：1 题（在浏览版筛选或搜索）
- 重构树：1 题（在浏览版筛选或搜索）
- 数论筛：1 题（在浏览版筛选或搜索）
- 后缀自动机：1 题（在浏览版筛选或搜索）

## 用法

先按当前训练专题筛选，再选题；默认按赛季和站次排列，**不是难度排序**。交互、RunTwice、随机输入专用题与普通算法题混合收录，方法摘要会说明其特殊性。先看题目，卡住再展开方法或打开题解。

## 完整专题列表

### 动态规划

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-G · Graph Problem With Small $n$](https://contest.ucup.ac/contest/1106/problem/5523) | S1 Ukraine | 动态规划、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.4） |
| [s1-4-H · Help Me to Get This Published](https://contest.ucup.ac/contest/1106/problem/5524) | S1 Ukraine | 动态规划、组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.5） |
| [s1-4-I · Increasing Grid](https://contest.ucup.ac/contest/1106/problem/5525) | S1 Ukraine | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-8-K · Skills in Pills](https://contest.ucup.ac/contest/1070/problem/5259) | S1 Slovenia | 动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.7） |
| [s1-12-A · XOR Tree Path](https://contest.ucup.ac/contest/1207/problem/6317) | S1 Ōokayama | 树上算法、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-B · Magical Wallet](https://contest.ucup.ac/contest/1207/problem/6318) | S1 Ōokayama | 动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-F · Forestry](https://contest.ucup.ac/contest/1207/problem/6322) | S1 Ōokayama | 树上算法、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-12-O · Jewel Game](https://contest.ucup.ac/contest/1207/problem/6331) | S1 Ōokayama | 博弈论、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-16-B · Classical Counting Problem](https://contest.ucup.ac/contest/1223/problem/6408) | S1 Gomel | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.1） |
| [s1-16-D · Classical DP Problem](https://contest.ucup.ac/contest/1223/problem/6410) | S1 Gomel | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.2） |
| [s1-20-E · Strange Keyboard](https://contest.ucup.ac/contest/1259/problem/6635) | S1 India | 动态规划、字符串 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.18） |
| [s1-20-F · Longest Strictly Increasing Sequence](https://contest.ucup.ac/contest/1259/problem/6636) | S1 India | 构造、动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.22） |
| [s1-20-H · Treelection](https://contest.ucup.ac/contest/1259/problem/6638) | S1 India | 树上算法、动态规划、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.28） |
| [s1-20-J · Talk That Talk](https://contest.ucup.ac/contest/1259/problem/6640) | S1 India | 组合计数、动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.35） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-5-C · Courses](https://contest.ucup.ac/contest/1388/problem/6548) | S2 Northern | 动态规划、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.2） |
| [s2-5-F · Forever Young](https://contest.ucup.ac/contest/1388/problem/6551) | S2 Northern | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.11） |
| [s2-5-L · LCSLCSLCS](https://contest.ucup.ac/contest/1388/problem/6557) | S2 Northern | 字符串、动态规划、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.54） |
| [s2-6-A · Digital Nim](https://contest.ucup.ac/contest/1398/problem/7606) | S2 Warsaw | 博弈论、动态规划、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-B · The Doubling Game 2](https://contest.ucup.ac/contest/1398/problem/7607) | S2 Warsaw | 树上算法、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-D · Colonization](https://contest.ucup.ac/contest/1398/problem/7609) | S2 Warsaw | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-E · Bus Lines](https://contest.ucup.ac/contest/1398/problem/7610) | S2 Warsaw | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-7-C · Cards](https://contest.ucup.ac/contest/1399/problem/7634) | S2 Two Capitals | 多项式与线性代数、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-E · Fair Elections](https://contest.ucup.ac/contest/1399/problem/7636) | S2 Two Capitals | 博弈论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.3） |
| [s2-7-M · Good Splits](https://contest.ucup.ac/contest/1399/problem/7644) | S2 Two Capitals | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.8） |
| [s2-7-N · Shoes](https://contest.ucup.ac/contest/1399/problem/7645) | S2 Two Capitals | 动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.9） |
| [s2-14-A · AND-OR closure](https://contest.ucup.ac/contest/1452/problem/7932) | S2 Southeastern Europe | 位运算与状态压缩、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.1） |
| [s2-14-G · Graph Race](https://contest.ucup.ac/contest/1452/problem/7938) | S2 Southeastern Europe | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.8） |
| [s2-18-A · Anti-Plagiarism](https://contest.ucup.ac/contest/1475/problem/8003) | S2 Dolgoprudny | 树上算法、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-18-C · Crossing the Border](https://contest.ucup.ac/contest/1475/problem/8005) | S2 Dolgoprudny | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.2） |
| [s2-18-E · Egg Drop Challenge](https://contest.ucup.ac/contest/1475/problem/8007) | S2 Dolgoprudny | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.3） |
| [s2-18-G · Growing Sequences](https://contest.ucup.ac/contest/1475/problem/8009) | S2 Dolgoprudny | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.4） |
| [s2-19-G · LCA Counting](https://contest.ucup.ac/contest/1487/problem/8134) | S2 Estonia | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.11） |
| [s2-20-A · Numerous Elimination](https://contest.ucup.ac/contest/1499/problem/8165) | S2 Ōokayama | 动态规划、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.1） |
| [s2-20-I · T Tile Placement Counting](https://contest.ucup.ac/contest/1499/problem/8173) | S2 Ōokayama | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.10） |
| [s2-20-P · Bridge Elimination](https://contest.ucup.ac/contest/1499/problem/8180) | S2 Ōokayama | 组合计数、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.19） |
| [s2-21-A · Anton's ABCD](https://contest.ucup.ac/contest/1511/problem/8207) | S2 Delft | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-E · Enumerating Substrings](https://contest.ucup.ac/contest/1511/problem/8211) | S2 Delft | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-G · Graffiti](https://contest.ucup.ac/contest/1511/problem/8213) | S2 Delft | 树上算法、动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.5） |
| [s2-26-F · Fair Distribution](https://contest.ucup.ac/contest/1576/problem/8510) | S2 Latin America | 数论、动态规划 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.7） |
| [s2-26-G · Greek Casino](https://contest.ucup.ac/contest/1576/problem/8511) | S2 Latin America | 概率期望与随机化、动态规划、数论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.8） |
| [s2-26-K · KMOP](https://contest.ucup.ac/contest/1576/problem/8515) | S2 Latin America | 图论、动态规划 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.14） |
| [s3-0-A · Arrested Development](https://contest.ucup.ac/contest/1695/problem/8768) | S3 America | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.2） |
| [s3-0-G · Manhattan Walk](https://contest.ucup.ac/contest/1695/problem/8774) | S3 America | 概率期望与随机化、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.14） |
| [s3-0-I · Not Another Constructive!](https://contest.ucup.ac/contest/1695/problem/8776) | S3 America | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.18） |
| [s3-0-M · Training, Round 2](https://contest.ucup.ac/contest/1695/problem/8780) | S3 America | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.26） |
| [s3-1-L · Candies](https://contest.ucup.ac/contest/1696/problem/8792) | S3 St. Petersburg | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.192） |
| [s3-2-C · Radars](https://contest.ucup.ac/contest/1699/problem/8519) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.31） |
| [s3-2-D · Xor Partitions](https://contest.ucup.ac/contest/1699/problem/8520) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.41） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-2-F · Waterfall Matrix](https://contest.ucup.ac/contest/1699/problem/8522) | S3 Zielona Gora | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.76） |
| [s3-2-J · Polygon II](https://contest.ucup.ac/contest/1699/problem/8526) | S3 Zielona Gora | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.160） |
| [s3-2-K · Power Divisions](https://contest.ucup.ac/contest/1699/problem/8527) | S3 Zielona Gora | 动态规划、位运算与状态压缩、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.175） |
| [s3-2-L · Chords](https://contest.ucup.ac/contest/1699/problem/8528) | S3 Zielona Gora | 动态规划、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.212） |
| [s3-2-M · Balance of Permutation](https://contest.ucup.ac/contest/1699/problem/8529) | S3 Zielona Gora | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.232） |
| [s3-4-C · Contour Multiplication](https://contest.ucup.ac/contest/1738/problem/9115) | S3 Hongo | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.16） |
| [s3-4-D · DRD String](https://contest.ucup.ac/contest/1738/problem/9116) | S3 Hongo | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.20） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-J · Japanese Gift Money](https://contest.ucup.ac/contest/1738/problem/9122) | S3 Hongo | 数论、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.64） |
| [s3-4-O · Optimal Train Operation](https://contest.ucup.ac/contest/1738/problem/9127) | S3 Hongo | 动态规划、数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.97） |
| [s3-4-P · Priority Queue 3](https://contest.ucup.ac/contest/1738/problem/9128) | S3 Hongo | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.104） |
| [s3-4-Q · Quotient Sum](https://contest.ucup.ac/contest/1738/problem/9129) | S3 Hongo | 动态规划、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.109） |
| [s3-5-F · Teleports](https://contest.ucup.ac/contest/1741/problem/9135) | S3 Moscow | 动态规划、图论 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-H · Ancient Country](https://contest.ucup.ac/contest/1741/problem/9137) | S3 Moscow | 动态规划、计算几何 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-K · Train Depot](https://contest.ucup.ac/contest/1741/problem/9140) | S3 Moscow | 树上算法、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-C · -is-this-bitset-](https://contest.ucup.ac/contest/1762/problem/9169) | S3 Osijek | 树上算法、动态规划、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-6-H · Game Design](https://contest.ucup.ac/contest/1762/problem/9174) | S3 Osijek | 动态规划、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-A · Bus Analysis](https://contest.ucup.ac/contest/1774/problem/9220) | S3 Warsaw | 动态规划、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-C · Price Combo](https://contest.ucup.ac/contest/1774/problem/9222) | S3 Warsaw | 动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-J · Juliet Unifies Ones](https://contest.ucup.ac/contest/1774/problem/9229) | S3 Warsaw | 动态规划、字符串 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-K · Routing K-Codes](https://contest.ucup.ac/contest/1774/problem/9230) | S3 Warsaw | 树上算法、动态规划 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-A · Welcome to NPCAPC](https://contest.ucup.ac/contest/1804/problem/9435) | S3 Sumiyosi | 动态规划、多项式与线性代数、字符串 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) |
| [s3-11-B · Some Sum of Subset](https://contest.ucup.ac/contest/1804/problem/9436) | S3 Sumiyosi | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10175) |
| [s3-11-D · Two Box](https://contest.ucup.ac/contest/1804/problem/9438) | S3 Sumiyosi | 动态规划、多项式与线性代数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10024) |
| [s3-11-F · Train Seats](https://contest.ucup.ac/contest/1804/problem/9440) | S3 Sumiyosi | 动态规划、数据结构 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10270) |
| [s3-11-I · Left Equals Right](https://contest.ucup.ac/contest/1804/problem/9443) | S3 Sumiyosi | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10176) |
| [s3-11-J · Again Permutation Problem](https://contest.ucup.ac/contest/1804/problem/9444) | S3 Sumiyosi | 动态规划、图论、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10019) |
| [s3-11-K · Peace with Magic](https://contest.ucup.ac/contest/1804/problem/9445) | S3 Sumiyosi | 动态规划 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10223) |
| [s3-11-M · Admired Person](https://contest.ucup.ac/contest/1804/problem/9447) | S3 Sumiyosi | 动态规划、贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10177) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-N · 0100 Insertion](https://contest.ucup.ac/contest/1812/problem/9489) | S3 Sendai | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.68） |
| [s3-18-G · Shrek's Song of the Swamp](https://contest.ucup.ac/contest/1849/problem/9787) | S3 Southeastern Europe | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.9） |
| [s3-21-D · A xor B plus C](https://contest.ucup.ac/contest/1872/problem/9878) | S3 Ōokayama | 位运算与状态压缩、动态规划 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11464) |
| [s3-21-E · ReTravel](https://contest.ucup.ac/contest/1872/problem/9879) | S3 Ōokayama | 动态规划、计算几何 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11086) |
| [s3-21-H · Two Convex Sets](https://contest.ucup.ac/contest/1872/problem/9882) | S3 Ōokayama | 计算几何、动态规划 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11084) |
| [s3-24-E · Express Rotations](https://contest.ucup.ac/contest/1890/problem/9963) | S3 Poland | 动态规划、数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.217） |
| [s3-24-H · High Jump](https://contest.ucup.ac/contest/1890/problem/9966) | S3 Poland | 动态规划、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.107） |
| [s3-30-B · Glass Stepping Stones](https://contest.ucup.ac/contest/1917/problem/10088) | S3 Northern | 博弈论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-30-E · Fractal Maze](https://contest.ucup.ac/contest/1917/problem/10091) | S3 Northern | 动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-30-G · Jump the Frog](https://contest.ucup.ac/contest/1917/problem/10093) | S3 Northern | 多项式与线性代数、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-H · Slot Machine](https://contest.ucup.ac/contest/1917/problem/10094) | S3 Northern | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-I · Product](https://contest.ucup.ac/contest/1917/problem/10095) | S3 Northern | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-32-B · Gona Guni](https://contest.ucup.ac/contest/1939/problem/10215) | S3 Dhaka | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-F · Yet Another Crossover Episode](https://contest.ucup.ac/contest/1939/problem/10219) | S3 Dhaka | 位运算与状态压缩、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-I · Unhappy Team](https://contest.ucup.ac/contest/1939/problem/10222) | S3 Dhaka | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.5） |
| [s3-33-B · Bin Packing](https://contest.ucup.ac/contest/1954/problem/10266) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.2） |
| [s3-33-E · Easy Counting Problem](https://contest.ucup.ac/contest/1954/problem/10269) | S3 India | 概率期望与随机化、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.5） |
| [s3-33-F · Greedy Prices](https://contest.ucup.ac/contest/1954/problem/10270) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.7） |
| [s3-33-M · Ticket Revenue Maximization](https://contest.ucup.ac/contest/1954/problem/10277) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.14） |
| [s3-34-C · 2-Power Rush](https://contest.ucup.ac/contest/1965/problem/10323) | S3 Aobayama | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.40） |
| [s3-34-I · Small Steps](https://contest.ucup.ac/contest/1965/problem/10329) | S3 Aobayama | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.63） |
| [s3-35-B · ICFC World Finals](https://contest.ucup.ac/contest/1993/problem/10702) | S3 Kraków | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-C · Diamonds and the Genie](https://contest.ucup.ac/contest/1993/problem/10703) | S3 Kraków | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.2） |
| [s3-35-H · Decent Path Around Bajtów](https://contest.ucup.ac/contest/1993/problem/10708) | S3 Kraków | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-39-G · Guarding Plan](https://contest.ucup.ac/contest/2071/problem/10976) | S3 Tokyo | 计算几何、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-B · Collatz Sum](https://contest.ucup.ac/contest/2135/problem/12151) | S3 Potyczki | 数论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.251） |
| [s3-40-C · DNA Subsequences](https://contest.ucup.ac/contest/2135/problem/12152) | S3 Potyczki | 动态规划、搜索与二分、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.2） |
| [s3-40-D · Fern Market](https://contest.ucup.ac/contest/2135/problem/12153) | S3 Potyczki | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.55） |
| [s3-40-E · One Bit](https://contest.ucup.ac/contest/2135/problem/12154) | S3 Potyczki | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.88） |
| [s3-40-G · Furniture](https://contest.ucup.ac/contest/2135/problem/12156) | S3 Potyczki | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.266） |
| [s3-40-K · Projects](https://contest.ucup.ac/contest/2135/problem/12160) | S3 Potyczki | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.171） |
| [s3-40-L · Directed Hanoi](https://contest.ucup.ac/contest/2135/problem/12161) | S3 Potyczki | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.329） |
| [s4-0-B · Circle of Leaf](https://contest.ucup.ac/contest/2041/problem/11357) | S4 America | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.12） |
| [s4-0-H · Ornaments on a Tree](https://contest.ucup.ac/contest/2041/problem/11363) | S4 America | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.32） |
| [s4-1-I · troS XEM](https://contest.ucup.ac/contest/2539/problem/14434) | S4 Korolyov | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-2-A · Apple Tree](https://contest.ucup.ac/contest/2551/problem/14130) | S4 Paris | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-B · Balatro](https://contest.ucup.ac/contest/2551/problem/14131) | S4 Paris | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-D · Digit Division](https://contest.ucup.ac/contest/2551/problem/14133) | S4 Paris | 数论、构造、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-E · Euclid in Manhattan](https://contest.ucup.ac/contest/2551/problem/14134) | S4 Paris | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.2） |
| [s4-3-B · Christmas Tree](https://contest.ucup.ac/contest/2559/problem/14416) | S4 Polar | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-3-E · Maximum Segment Sum](https://contest.ucup.ac/contest/2559/problem/14419) | S4 Polar | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-3-F · This Time I Will Be Lucky](https://contest.ucup.ac/contest/2559/problem/14420) | S4 Polar | 概率期望与随机化、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-H · Absolutely Flat](https://contest.ucup.ac/contest/2559/problem/14422) | S4 Polar | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-J · One Permutation](https://contest.ucup.ac/contest/2559/problem/14424) | S4 Polar | 动态规划、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-C · Count Triangular Sequences](https://contest.ucup.ac/contest/2668/problem/15446) | S4 Poland | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.102） |
| [s4-8-D · Division with Polylines](https://contest.ucup.ac/contest/2668/problem/15447) | S4 Poland | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.123） |
| [s4-10-C · Connecting Railway Stations](https://contest.ucup.ac/contest/2814/problem/16002) | S4 Wrocław | 树上算法、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.67） |
| [s4-10-F · Foxes](https://contest.ucup.ac/contest/2814/problem/16005) | S4 Wrocław | 数据结构、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.97） |
| [s4-10-G · Game of Darts](https://contest.ucup.ac/contest/2814/problem/16006) | S4 Wrocław | 动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.15） |
| [s4-11-F · Language Barrier](https://contest.ucup.ac/contest/2828/problem/16120) | S4 Southeastern Europe | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.6） |
| [s4-11-G · Intervals from Triplets](https://contest.ucup.ac/contest/2828/problem/16121) | S4 Southeastern Europe | 动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.7） |
| [s4-13-C · Sum of Three Inversions](https://contest.ucup.ac/contest/2921/problem/16228) | S4 Ōokayama | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.4） |
| [s4-16-C · Copy-paste](https://contest.ucup.ac/contest/3347/problem/17152) | S4 Warsaw | 数论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.5） |
| [s4-16-E · Evaluation](https://contest.ucup.ac/contest/3347/problem/17154) | S4 Warsaw | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.7） |
| [s4-16-H · House](https://contest.ucup.ac/contest/3347/problem/17157) | S4 Warsaw | 搜索与二分、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.11） |
| [s4-18-B · Binary Tree Counting](https://contest.ucup.ac/contest/3420/problem/17247) | S4 Hongō | 树上算法、动态规划、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15693) |
| [s4-18-E · Exchange or Not](https://contest.ucup.ac/contest/3420/problem/17250) | S4 Hongō | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16127) |
| [s4-19-B · Building a Reactor](https://contest.ucup.ac/contest/3426/problem/17261) | S4 Belarus | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.1） |
| [s4-19-I · Ivan Tsarevich in the Magical Grove](https://contest.ucup.ac/contest/3426/problem/17268) | S4 Belarus | 图论、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-20-B · Palindrome and Permutation](https://contest.ucup.ac/contest/3516/problem/17407) | S4 India | 图论、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.3） |
| [s4-20-D · Merging Maximum](https://contest.ucup.ac/contest/3516/problem/17409) | S4 India | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.7） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-20-F · Restricted Removals](https://contest.ucup.ac/contest/3516/problem/17411) | S4 India | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.9） |
| [s4-20-G · Sequence Domination](https://contest.ucup.ac/contest/3516/problem/17412) | S4 India | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.10） |
| [s4-20-J · Counting Is Fun](https://contest.ucup.ac/contest/3516/problem/17415) | S4 India | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.16） |
| [s4-21-F · Increase Decrease](https://contest.ucup.ac/contest/3542/problem/17424) | S4 Kamigō | 构造、动态规划 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18127) |
| [s4-21-H · OR Preference](https://contest.ucup.ac/contest/3542/problem/17426) | S4 Kamigō | 位运算与状态压缩、动态规划、贪心 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) |
| [s4-21-I · Penguin Flicker](https://contest.ucup.ac/contest/3542/problem/17427) | S4 Kamigō | 动态规划、多项式与线性代数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18125) |
| [s4-22-B · Cat Cut](https://contest.ucup.ac/contest/3575/problem/17714) | S4 Kyoto | 字符串、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.1） |
| [s4-22-G · The Symbolic Tree](https://contest.ucup.ac/contest/3575/problem/17719) | S4 Kyoto | 树上算法、动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-25-G · Grid Gradient](https://contest.ucup.ac/contest/3773/problem/18407) | S4 Zagreb | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.27） |
| [s4-Extra-3-D · Electi Lamps](https://contest.ucup.ac/contest/2757/problem/15520) | S4 Osijek | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-E · XOR Again?](https://contest.ucup.ac/contest/2757/problem/15521) | S4 Osijek | 位运算与状态压缩、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s5-1-A · Astana Hard Metro](https://contest.ucup.ac/contest/4126/problem/20248) | S5 Nizhny Novgorod | 动态规划、概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.1） |
| [s5-1-G · Game Show: XOR Edition](https://contest.ucup.ac/contest/4126/problem/20254) | S5 Nizhny Novgorod | 位运算与状态压缩、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.13） |
| [s5-1-M · Minecraft Spiderweb](https://contest.ucup.ac/contest/4126/problem/20260) | S5 Nizhny Novgorod | 计算几何、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.24） |
| [s5-6-A · Fugaku NK-kei](https://contest.ucup.ac/contest/4617/problem/23669) | S5 Hyakumanben | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.1） |
| [s5-6-C · Moving Silver](https://contest.ucup.ac/contest/4617/problem/23671) | S5 Hyakumanben | 博弈论、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.6） |
| [s5-6-D · Go Robots](https://contest.ucup.ac/contest/4617/problem/23672) | S5 Hyakumanben | 图论、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.8） |
| [s5-6-H · Please Insert Coin](https://contest.ucup.ac/contest/4617/problem/23676) | S5 Hyakumanben | 动态规划、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.12） |
| [s5-6-K · Dyads of Hanoi](https://contest.ucup.ac/contest/4617/problem/23679) | S5 Hyakumanben | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.19） |

### 数据结构

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-J · Jewel of Data Structure Problems](https://contest.ucup.ac/contest/1106/problem/5526) | S1 Ukraine | 位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-8-A · Bandits](https://contest.ucup.ac/contest/1070/problem/5249) | S1 Slovenia | 树上算法、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.14） |
| [s1-8-C · Constellations](https://contest.ucup.ac/contest/1070/problem/5251) | S1 Slovenia | 数据结构、计算几何 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.5） |
| [s1-8-J · Mortgage](https://contest.ucup.ac/contest/1070/problem/5258) | S1 Slovenia | 数据结构、计算几何、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.12） |
| [s1-12-N · XOR Reachable](https://contest.ucup.ac/contest/1207/problem/6330) | S1 Ōokayama | 数据结构、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-16-C · Classical Data Structure Problem](https://contest.ucup.ac/contest/1223/problem/6409) | S1 Gomel | 数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.2） |
| [s1-16-I · Classical Minimization Problem](https://contest.ucup.ac/contest/1223/problem/6415) | S1 Gomel | 贪心、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.4） |
| [s1-16-J · Classical Scheduling Problem](https://contest.ucup.ac/contest/1223/problem/6416) | S1 Gomel | 贪心、搜索与二分、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-A · Maximum Bitwise OR](https://contest.ucup.ac/contest/1259/problem/6631) | S1 India | 位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.2） |
| [s1-20-C · Exam Requirements](https://contest.ucup.ac/contest/1259/problem/6633) | S1 India | 图论、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.10） |
| [s1-20-I · Disk Tree](https://contest.ucup.ac/contest/1259/problem/6639) | S1 India | 计算几何、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.32） |
| [s2-2-G · Graph Cuts](https://contest.ucup.ac/contest/1356/problem/7181) | S2 SPb | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.20） |
| [s2-2-H · Very Sparse Table](https://contest.ucup.ac/contest/1356/problem/7182) | S2 SPb | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.32） |
| [s2-2-K · Poor Students](https://contest.ucup.ac/contest/1356/problem/7185) | S2 SPb | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.7） |
| [s2-5-H · Shared Memory Switch](https://contest.ucup.ac/contest/1388/problem/6553) | S2 Northern | 贪心、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.45） |
| [s2-5-K · Text Editor](https://contest.ucup.ac/contest/1388/problem/6556) | S2 Northern | 数据结构、字符串 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.49） |
| [s2-6-C · Cliques](https://contest.ucup.ac/contest/1398/problem/7608) | S2 Warsaw | 树上算法、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-F · Max-Min](https://contest.ucup.ac/contest/1398/problem/7611) | S2 Warsaw | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.3） |
| [s2-6-K · Jump Graph](https://contest.ucup.ac/contest/1398/problem/7616) | S2 Warsaw | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-6-L · Spectacle](https://contest.ucup.ac/contest/1398/problem/7617) | S2 Warsaw | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-7-J · Range Sets](https://contest.ucup.ac/contest/1399/problem/7641) | S2 Two Capitals | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-14-F · Fast XORting](https://contest.ucup.ac/contest/1452/problem/7937) | S2 Southeastern Europe | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.7） |
| [s2-14-H · High Towers](https://contest.ucup.ac/contest/1452/problem/7939) | S2 Southeastern Europe | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.9） |
| [s2-14-K · $K$ Subsequences](https://contest.ucup.ac/contest/1452/problem/7942) | S2 Southeastern Europe | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.12） |
| [s2-14-M · Max Minus Min](https://contest.ucup.ac/contest/1452/problem/7944) | S2 Southeastern Europe | 搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.14） |
| [s2-18-D · Dinosaur Bones Digging](https://contest.ucup.ac/contest/1475/problem/8006) | S2 Dolgoprudny | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.2） |
| [s2-18-E · Egg Drop Challenge](https://contest.ucup.ac/contest/1475/problem/8007) | S2 Dolgoprudny | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.3） |
| [s2-18-J · Jumping Lights](https://contest.ucup.ac/contest/1475/problem/8012) | S2 Dolgoprudny | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.6） |
| [s2-19-F · When Anton Saw This Task He Reacted With 😩](https://contest.ucup.ac/contest/1487/problem/8133) | S2 Estonia | 多项式与线性代数、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.9） |
| [s2-20-D · Spacecraft](https://contest.ucup.ac/contest/1499/problem/8168) | S2 Ōokayama | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.3） |
| [s2-20-H · 404 Chotto Found](https://contest.ucup.ac/contest/1499/problem/8172) | S2 Ōokayama | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.9） |
| [s2-26-H · Harmonic Operations](https://contest.ucup.ac/contest/1576/problem/8512) | S2 Latin America | 字符串、数据结构 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.9） |
| [s3-0-H · MountainCraft](https://contest.ucup.ac/contest/1695/problem/8775) | S3 America | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.16） |
| [s3-0-K · Shadow Line](https://contest.ucup.ac/contest/1695/problem/8778) | S3 America | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.22） |
| [s3-1-A · Element-Wise Comparison](https://contest.ucup.ac/contest/1696/problem/8781) | S3 St. Petersburg | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.2） |
| [s3-1-C · Cherry Picking](https://contest.ucup.ac/contest/1696/problem/8783) | S3 St. Petersburg | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.44） |
| [s3-1-K · Tasks and Bugs](https://contest.ucup.ac/contest/1696/problem/8791) | S3 St. Petersburg | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.187） |
| [s3-1-M · Toilets](https://contest.ucup.ac/contest/1696/problem/8793) | S3 St. Petersburg | 数据结构、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.210） |
| [s3-2-B · Roars III](https://contest.ucup.ac/contest/1699/problem/8518) | S3 Zielona Gora | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.13） |
| [s3-2-F · Waterfall Matrix](https://contest.ucup.ac/contest/1699/problem/8522) | S3 Zielona Gora | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.76） |
| [s3-2-G · Puzzle II](https://contest.ucup.ac/contest/1699/problem/8523) | S3 Zielona Gora | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.102） |
| [s3-2-I · Mercenaries](https://contest.ucup.ac/contest/1699/problem/8525) | S3 Zielona Gora | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.134） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-K · Kth Sum](https://contest.ucup.ac/contest/1738/problem/9123) | S3 Hongo | 搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.76） |
| [s3-4-O · Optimal Train Operation](https://contest.ucup.ac/contest/1738/problem/9127) | S3 Hongo | 动态规划、数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.97） |
| [s3-5-C · Painting Fences](https://contest.ucup.ac/contest/1741/problem/9132) | S3 Moscow | 数据结构、贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-K · Train Depot](https://contest.ucup.ac/contest/1741/problem/9140) | S3 Moscow | 树上算法、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-D · Cycle Game](https://contest.ucup.ac/contest/1762/problem/9170) | S3 Osijek | 数据结构、图论 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-6-G · Touching Grass](https://contest.ucup.ac/contest/1762/problem/9173) | S3 Osijek | 计算几何、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-C · Price Combo](https://contest.ucup.ac/contest/1774/problem/9222) | S3 Warsaw | 动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-F · Train Seats](https://contest.ucup.ac/contest/1804/problem/9440) | S3 Sumiyosi | 动态规划、数据结构 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10270) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-H · Maximize Array](https://contest.ucup.ac/contest/1812/problem/9483) | S3 Sendai | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.41） |
| [s3-18-K · Intrusive Donkey](https://contest.ucup.ac/contest/1849/problem/9791) | S3 Southeastern Europe | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.14） |
| [s3-18-L · Ogre Sort](https://contest.ucup.ac/contest/1849/problem/9792) | S3 Southeastern Europe | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.15） |
| [s3-18-M · Enchanted Lawns Quest](https://contest.ucup.ac/contest/1849/problem/9793) | S3 Southeastern Europe | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.16） |
| [s3-21-C · Segment Tree](https://contest.ucup.ac/contest/1872/problem/9877) | S3 Ōokayama | 数据结构、图论 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11291) |
| [s3-21-K · Sum is One](https://contest.ucup.ac/contest/1872/problem/9885) | S3 Ōokayama | 图论、数据结构 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11225) |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-24-E · Express Rotations](https://contest.ucup.ac/contest/1890/problem/9963) | S3 Poland | 动态规划、数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.217） |
| [s3-24-J · Just Zeros](https://contest.ucup.ac/contest/1890/problem/9968) | S3 Poland | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.94） |
| [s3-27-B · The Best Wife](https://contest.ucup.ac/contest/1901/problem/8612) | S3 London | 数据结构、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-C · Cardinality](https://contest.ucup.ac/contest/1901/problem/8613) | S3 London | 概率期望与随机化、位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-H · Have You Seen This Subarray?](https://contest.ucup.ac/contest/1901/problem/8618) | S3 London | 数据结构、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-27-K · Knapsack](https://contest.ucup.ac/contest/1901/problem/8621) | S3 London | 搜索与二分、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-31-F · Flats](https://contest.ucup.ac/contest/1924/problem/10119) | S3 Wroclaw | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.44） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-M · Tree Flip](https://contest.ucup.ac/contest/1939/problem/10226) | S3 Dhaka | 树上算法、数据结构、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.7） |
| [s3-33-G · Lexicographic Raffle](https://contest.ucup.ac/contest/1954/problem/10271) | S3 India | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.8） |
| [s3-33-H · Majority Graph](https://contest.ucup.ac/contest/1954/problem/10272) | S3 India | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.9） |
| [s3-33-I · Majority Voters](https://contest.ucup.ac/contest/1954/problem/10273) | S3 India | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.10） |
| [s3-33-K · P to Q](https://contest.ucup.ac/contest/1954/problem/10275) | S3 India | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.12） |
| [s3-33-L · Score Sum](https://contest.ucup.ac/contest/1954/problem/10276) | S3 India | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.13） |
| [s3-34-B · Matching Query](https://contest.ucup.ac/contest/1965/problem/10322) | S3 Aobayama | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.52） |
| [s3-34-J · Median Operations](https://contest.ucup.ac/contest/1965/problem/10330) | S3 Aobayama | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.68） |
| [s3-35-A · Suspicious Submissions](https://contest.ucup.ac/contest/1993/problem/10701) | S3 Kraków | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-G · Road Trip](https://contest.ucup.ac/contest/1993/problem/10707) | S3 Kraków | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-35-I · Random Remainders](https://contest.ucup.ac/contest/1993/problem/10709) | S3 Kraków | 数论、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-35-J · Sumotonic Sequences](https://contest.ucup.ac/contest/1993/problem/10710) | S3 Kraków | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-39-A · Array Similarity](https://contest.ucup.ac/contest/2071/problem/10970) | S3 Tokyo | 数据结构、概率期望与随机化 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-G · Guarding Plan](https://contest.ucup.ac/contest/2071/problem/10976) | S3 Tokyo | 计算几何、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-P · Perfect Suika Game on a Tree](https://contest.ucup.ac/contest/2071/problem/10985) | S3 Tokyo | 树上算法、数据结构、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-N · Frequency Function](https://contest.ucup.ac/contest/2135/problem/12163) | S3 Potyczki | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.224） |
| [s4-0-E · Humans vs AI](https://contest.ucup.ac/contest/2041/problem/11360) | S4 America | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.19） |
| [s4-0-G · Most Scenic Cycle](https://contest.ucup.ac/contest/2041/problem/11362) | S4 America | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.25） |
| [s4-1-F · Yet Another MST Problem](https://contest.ucup.ac/contest/2539/problem/14431) | S4 Korolyov | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-H · Misread Problem](https://contest.ucup.ac/contest/2539/problem/14433) | S4 Korolyov | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-1-K · Robot Construction](https://contest.ucup.ac/contest/2539/problem/14436) | S4 Korolyov | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.4） |
| [s4-2-J · JamBrains](https://contest.ucup.ac/contest/2551/problem/14139) | S4 Paris | 数据结构、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.5） |
| [s4-2-K · $k$ Operations](https://contest.ucup.ac/contest/2551/problem/14140) | S4 Paris | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-3-C · Roman Numerals](https://contest.ucup.ac/contest/2559/problem/14417) | S4 Polar | 数据结构、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-3-D · Disjoint Set Splitting](https://contest.ucup.ac/contest/2559/problem/14418) | S4 Polar | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-3-H · Absolutely Flat](https://contest.ucup.ac/contest/2559/problem/14422) | S4 Polar | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-J · One Permutation](https://contest.ucup.ac/contest/2559/problem/14424) | S4 Polar | 动态规划、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-B · Beats](https://contest.ucup.ac/contest/2668/problem/15445) | S4 Poland | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.51） |
| [s4-8-E · Enigma](https://contest.ucup.ac/contest/2668/problem/15448) | S4 Poland | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.93） |
| [s4-8-L · Linear Averaging](https://contest.ucup.ac/contest/2668/problem/15455) | S4 Poland | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.113） |
| [s4-10-A · Automatized Mineral Classification](https://contest.ucup.ac/contest/2814/problem/16000) | S4 Wrocław | 交互与信息编码、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.45） |
| [s4-10-F · Foxes](https://contest.ucup.ac/contest/2814/problem/16005) | S4 Wrocław | 数据结构、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.97） |
| [s4-11-F · Language Barrier](https://contest.ucup.ac/contest/2828/problem/16120) | S4 Southeastern Europe | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.6） |
| [s4-13-A · Depth of Interval](https://contest.ucup.ac/contest/2921/problem/16226) | S4 Ōokayama | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.1） |
| [s4-13-E · Max Twice Subsequences](https://contest.ucup.ac/contest/2921/problem/16230) | S4 Ōokayama | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.6） |
| [s4-13-I · Subgrid Connected Components](https://contest.ucup.ac/contest/2921/problem/16234) | S4 Ōokayama | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.15） |
| [s4-13-M · Many Approaches](https://contest.ucup.ac/contest/2921/problem/16238) | S4 Ōokayama | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.22） |
| [s4-16-D · Deque Sort](https://contest.ucup.ac/contest/3347/problem/17153) | S4 Warsaw | 数据结构、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.6） |
| [s4-16-G · Good Permutations](https://contest.ucup.ac/contest/3347/problem/17156) | S4 Warsaw | 数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.9） |
| [s4-17-C · String Workshop](https://contest.ucup.ac/contest/3384/problem/17163) | S4 St. Petersburg | 数据结构、字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.2） |
| [s4-17-G · Traffic Lights](https://contest.ucup.ac/contest/3384/problem/17167) | S4 St. Petersburg | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.5） |
| [s4-17-I · Wooden Checker](https://contest.ucup.ac/contest/3384/problem/17169) | S4 St. Petersburg | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.8） |
| [s4-18-F · Finite Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17251) | S4 Hongō | 字符串、数据结构 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15692) |
| [s4-18-G · Greatest Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17252) | S4 Hongō | 字符串、数据结构、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16136) |
| [s4-19-G · Guaranteed Medal](https://contest.ucup.ac/contest/3426/problem/17266) | S4 Belarus | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.4） |
| [s4-19-J · Jolly Wheel](https://contest.ucup.ac/contest/3426/problem/17269) | S4 Belarus | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-19-K · Kitchen](https://contest.ucup.ac/contest/3426/problem/17270) | S4 Belarus | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-19-M · May We Answer Your Questions Right?](https://contest.ucup.ac/contest/3426/problem/17272) | S4 Belarus | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-20-C · Score Queries](https://contest.ucup.ac/contest/3516/problem/17408) | S4 India | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.5） |
| [s4-20-D · Merging Maximum](https://contest.ucup.ac/contest/3516/problem/17409) | S4 India | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.7） |
| [s4-20-F · Restricted Removals](https://contest.ucup.ac/contest/3516/problem/17411) | S4 India | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.9） |
| [s4-20-H · Maximum Difference](https://contest.ucup.ac/contest/3516/problem/17413) | S4 India | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.12） |
| [s4-20-K · Prefix MEX Equation](https://contest.ucup.ac/contest/3516/problem/17416) | S4 India | 数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.18） |
| [s4-21-E · Find "rururutata"](https://contest.ucup.ac/contest/3542/problem/17423) | S4 Kamigō | 字符串、数据结构 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17002) |
| [s4-22-D · Campaign Speech](https://contest.ucup.ac/contest/3575/problem/17716) | S4 Kyoto | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.4） |
| [s4-22-M · Linked VERSE](https://contest.ucup.ac/contest/3575/problem/17725) | S4 Kyoto | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.10） |
| [s4-25-A · Arrow Array](https://contest.ucup.ac/contest/3773/problem/18401) | S4 Zagreb | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.2） |
| [s4-25-B · Big Balls](https://contest.ucup.ac/contest/3773/problem/18402) | S4 Zagreb | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.7） |
| [s4-25-E · Exchange Error](https://contest.ucup.ac/contest/3773/problem/18405) | S4 Zagreb | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.18） |
| [s4-25-K · Kempt Kale](https://contest.ucup.ac/contest/3773/problem/18411) | S4 Zagreb | 贪心、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.42） |
| [s4-25-M · Maximum Mex](https://contest.ucup.ac/contest/3773/problem/18413) | S4 Zagreb | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.49） |
| [s4-Extra-3-D · Electi Lamps](https://contest.ucup.ac/contest/2757/problem/15520) | S4 Osijek | 动态规划、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-I · Bobs Rating](https://contest.ucup.ac/contest/2757/problem/15525) | S4 Osijek | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s4-Extra-3-J · AND Components](https://contest.ucup.ac/contest/2757/problem/15526) | S4 Osijek | 数据结构、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-1-C · Cost of Conflicts](https://contest.ucup.ac/contest/4126/problem/20250) | S5 Nizhny Novgorod | 图论、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.5） |
| [s5-1-F · Fresh Cartridges](https://contest.ucup.ac/contest/4126/problem/20253) | S5 Nizhny Novgorod | 多项式与线性代数、概率期望与随机化、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.11） |
| [s5-1-H · Hockey Hog](https://contest.ucup.ac/contest/4126/problem/20255) | S5 Nizhny Novgorod | 计算几何、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.15） |
| [s5-3-B · Binary Rotations](https://contest.ucup.ac/contest/4565/problem/20730) | S5 Gorkovskaya | 树上算法、数据结构、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.2） |
| [s5-3-D · Dynamic Adjustment](https://contest.ucup.ac/contest/4565/problem/20732) | S5 Gorkovskaya | 数据结构、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |
| [s5-3-I · Interval MST](https://contest.ucup.ac/contest/4565/problem/20737) | S5 Gorkovskaya | 图论、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.8） |
| [s5-3-K · Keep Colors Apart](https://contest.ucup.ac/contest/4565/problem/20739) | S5 Gorkovskaya | 贪心、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.11） |
| [s5-3-M · Matching Substrings](https://contest.ucup.ac/contest/4565/problem/20741) | S5 Gorkovskaya | 字符串、树上算法、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.13） |
| [s5-6-B · PerMutation](https://contest.ucup.ac/contest/4617/problem/23670) | S5 Hyakumanben | 数据结构、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.4） |
| [s5-6-F · Path XOR on MST](https://contest.ucup.ac/contest/4617/problem/23674) | S5 Hyakumanben | 图论、位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |
| [s5-6-H · Please Insert Coin](https://contest.ucup.ac/contest/4617/problem/23676) | S5 Hyakumanben | 动态规划、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.12） |
| [s5-6-I · tatesoto decomposition](https://contest.ucup.ac/contest/4617/problem/23677) | S5 Hyakumanben | 字符串、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.14） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |

### 图论

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-B · Binary Arrays and Sliding Sums](https://contest.ucup.ac/contest/1106/problem/5518) | S1 Ukraine | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.1） |
| [s1-4-C · Count Hamiltonian Cycles](https://contest.ucup.ac/contest/1106/problem/5519) | S1 Ukraine | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.2） |
| [s1-4-D · Distance Parities](https://contest.ucup.ac/contest/1106/problem/5520) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-F · F*** 3-Colorable Graphs](https://contest.ucup.ac/contest/1106/problem/5522) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-G · Graph Problem With Small $n$](https://contest.ucup.ac/contest/1106/problem/5523) | S1 Ukraine | 动态规划、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.4） |
| [s1-4-H · Help Me to Get This Published](https://contest.ucup.ac/contest/1106/problem/5524) | S1 Ukraine | 动态规划、组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.5） |
| [s1-4-K · King of Swapping](https://contest.ucup.ac/contest/1106/problem/5527) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.8） |
| [s1-4-L · Least Annoying Constructive Problem](https://contest.ucup.ac/contest/1106/problem/5528) | S1 Ukraine | 构造、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.9） |
| [s1-7-D · Triterminant](https://contest.ucup.ac/contest/1129/problem/5741) | S1 Zaporizhzhia | 图论、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.6） |
| [s1-7-H · Graph Isomorphism](https://contest.ucup.ac/contest/1129/problem/5745) | S1 Zaporizhzhia | 图论、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.14） |
| [s1-7-I · DAG Generation](https://contest.ucup.ac/contest/1129/problem/5746) | S1 Zaporizhzhia | 概率期望与随机化、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.14） |
| [s1-7-L · Directed Vertex Cacti](https://contest.ucup.ac/contest/1129/problem/5749) | S1 Zaporizhzhia | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.16） |
| [s1-7-M · Siteswap](https://contest.ucup.ac/contest/1129/problem/5750) | S1 Zaporizhzhia | 图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.16） |
| [s1-8-B · Combination Locks](https://contest.ucup.ac/contest/1070/problem/5250) | S1 Slovenia | 博弈论、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.8） |
| [s1-8-I · Money Laundering](https://contest.ucup.ac/contest/1070/problem/5257) | S1 Slovenia | 多项式与线性代数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.10） |
| [s1-12-M · Colorful Graph](https://contest.ucup.ac/contest/1207/problem/6329) | S1 Ōokayama | 图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.8） |
| [s1-12-N · XOR Reachable](https://contest.ucup.ac/contest/1207/problem/6330) | S1 Ōokayama | 数据结构、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-13-K · 4](https://contest.ucup.ac/contest/1212/problem/6354) | S1 Iberia | 图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-H · Classical Maximization Problem](https://contest.ucup.ac/contest/1223/problem/6414) | S1 Gomel | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-20-C · Exam Requirements](https://contest.ucup.ac/contest/1259/problem/6633) | S1 India | 图论、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.10） |
| [s1-20-D · Central Subset](https://contest.ucup.ac/contest/1259/problem/6634) | S1 India | 图论、树上算法 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.14） |
| [s1-20-M · Graphs and Colors](https://contest.ucup.ac/contest/1259/problem/6643) | S1 India | 构造、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.43） |
| [s2-2-C · Many Many Cycles](https://contest.ucup.ac/contest/1356/problem/7177) | S2 SPb | 图论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.6） |
| [s2-2-D · Bishops](https://contest.ucup.ac/contest/1356/problem/7178) | S2 SPb | 贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.13） |
| [s2-2-G · Graph Cuts](https://contest.ucup.ac/contest/1356/problem/7181) | S2 SPb | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.20） |
| [s2-2-K · Poor Students](https://contest.ucup.ac/contest/1356/problem/7185) | S2 SPb | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.7） |
| [s2-5-A · Greedy Bipartite Matching](https://contest.ucup.ac/contest/1388/problem/6546) | S2 Northern | 图论、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.2） |
| [s2-5-E · Elimination Race](https://contest.ucup.ac/contest/1388/problem/6550) | S2 Northern | 图论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.33） |
| [s2-6-K · Jump Graph](https://contest.ucup.ac/contest/1398/problem/7616) | S2 Warsaw | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-7-I · Colorful Cycles](https://contest.ucup.ac/contest/1399/problem/7640) | S2 Two Capitals | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-14-A · AND-OR closure](https://contest.ucup.ac/contest/1452/problem/7932) | S2 Southeastern Europe | 位运算与状态压缩、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.1） |
| [s2-14-E · Eliminate Tree](https://contest.ucup.ac/contest/1452/problem/7936) | S2 Southeastern Europe | 树上算法、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.6） |
| [s2-14-G · Graph Race](https://contest.ucup.ac/contest/1452/problem/7938) | S2 Southeastern Europe | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.8） |
| [s2-14-I · Impossible Numbers](https://contest.ucup.ac/contest/1452/problem/7940) | S2 Southeastern Europe | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.10） |
| [s2-14-L · LIS on Grid](https://contest.ucup.ac/contest/1452/problem/7943) | S2 Southeastern Europe | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.13） |
| [s2-16-F · Mark on a Graph](https://contest.ucup.ac/contest/1465/problem/4829) | S2 Run Twice | 图论、构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.65） |
| [s2-18-A · Anti-Plagiarism](https://contest.ucup.ac/contest/1475/problem/8003) | S2 Dolgoprudny | 树上算法、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-18-F · Fortune Wheel](https://contest.ucup.ac/contest/1475/problem/8008) | S2 Dolgoprudny | 概率期望与随机化、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.4） |
| [s2-18-I · Institute](https://contest.ucup.ac/contest/1475/problem/8011) | S2 Dolgoprudny | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.6） |
| [s2-19-A · Alternating Paths](https://contest.ucup.ac/contest/1487/problem/8128) | S2 Estonia | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.1） |
| [s2-19-C · Yet Another Balanced Coloring Problem](https://contest.ucup.ac/contest/1487/problem/8130) | S2 Estonia | 树上算法、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.6） |
| [s2-19-D · Filesystem](https://contest.ucup.ac/contest/1487/problem/8131) | S2 Estonia | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.8） |
| [s2-19-H · Minimum Cost Flow²](https://contest.ucup.ac/contest/1487/problem/8135) | S2 Estonia | 多项式与线性代数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.12） |
| [s2-19-I · Rebellious Edge](https://contest.ucup.ac/contest/1487/problem/8136) | S2 Estonia | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.15） |
| [s2-20-B · Almost Large](https://contest.ucup.ac/contest/1499/problem/8166) | S2 Ōokayama | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.1） |
| [s2-20-K · Dense Planting](https://contest.ucup.ac/contest/1499/problem/8175) | S2 Ōokayama | 图论、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.14） |
| [s2-20-O · 2D Parentheses](https://contest.ucup.ac/contest/1499/problem/8179) | S2 Ōokayama | 计算几何、贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.18） |
| [s2-20-P · Bridge Elimination](https://contest.ucup.ac/contest/1499/problem/8180) | S2 Ōokayama | 组合计数、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.19） |
| [s2-21-B · Beer Circuits](https://contest.ucup.ac/contest/1511/problem/8208) | S2 Delft | 搜索与二分、计算几何、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-F · Football in Osijek](https://contest.ucup.ac/contest/1511/problem/8212) | S2 Delft | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.4） |
| [s2-26-C · Clever Cell Choices](https://contest.ucup.ac/contest/1576/problem/8507) | S2 Latin America | 图论、博弈论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.4） |
| [s2-26-E · Expanding STACKS!](https://contest.ucup.ac/contest/1576/problem/8509) | S2 Latin America | 图论、构造 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.6） |
| [s2-26-K · KMOP](https://contest.ucup.ac/contest/1576/problem/8515) | S2 Latin America | 图论、动态规划 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.14） |
| [s3-1-G · Unusual Case](https://contest.ucup.ac/contest/1696/problem/8787) | S3 St. Petersburg | 概率期望与随机化、图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.102） |
| [s3-1-N · (Un)labeled graphs](https://contest.ucup.ac/contest/1696/problem/8794) | S3 St. Petersburg | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.217） |
| [s3-2-A · Interesting Paths](https://contest.ucup.ac/contest/1699/problem/8517) | S3 Zielona Gora | 图论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.2） |
| [s3-5-F · Teleports](https://contest.ucup.ac/contest/1741/problem/9135) | S3 Moscow | 动态规划、图论 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-L · Array Spread](https://contest.ucup.ac/contest/1741/problem/9141) | S3 Moscow | 图论、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-D · Cycle Game](https://contest.ucup.ac/contest/1762/problem/9170) | S3 Osijek | 数据结构、图论 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-E · Express Eviction](https://contest.ucup.ac/contest/1774/problem/9224) | S3 Warsaw | 图论 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-J · Again Permutation Problem](https://contest.ucup.ac/contest/1804/problem/9444) | S3 Sumiyosi | 动态规划、图论、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10019) |
| [s3-11-L · Construction of Town](https://contest.ucup.ac/contest/1804/problem/9446) | S3 Sumiyosi | 构造、图论 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/9999) |
| [s3-13-B · Topological Sort](https://contest.ucup.ac/contest/1812/problem/9477) | S3 Sendai | 组合计数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.13） |
| [s3-13-I · Colored Complete Graph](https://contest.ucup.ac/contest/1812/problem/9484) | S3 Sendai | 交互与信息编码、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.44） |
| [s3-13-M · Do Not Turn Back](https://contest.ucup.ac/contest/1812/problem/9488) | S3 Sendai | 图论、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.63） |
| [s3-13-O · Sub Brackets](https://contest.ucup.ac/contest/1812/problem/9490) | S3 Sendai | 图论、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.72） |
| [s3-18-A · All-Star](https://contest.ucup.ac/contest/1849/problem/9781) | S3 Southeastern Europe | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.1） |
| [s3-18-H · Shreckless](https://contest.ucup.ac/contest/1849/problem/9788) | S3 Southeastern Europe | 贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.10） |
| [s3-21-A · Don't Detect Cycle](https://contest.ucup.ac/contest/1872/problem/9875) | S3 Ōokayama | 图论、贪心 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11085) |
| [s3-21-C · Segment Tree](https://contest.ucup.ac/contest/1872/problem/9877) | S3 Ōokayama | 数据结构、图论 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11291) |
| [s3-21-K · Sum is One](https://contest.ucup.ac/contest/1872/problem/9885) | S3 Ōokayama | 图论、数据结构 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11225) |
| [s3-24-B · Baggage](https://contest.ucup.ac/contest/1890/problem/9960) | S3 Poland | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.61） |
| [s3-24-E · Express Rotations](https://contest.ucup.ac/contest/1890/problem/9963) | S3 Poland | 动态规划、数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.217） |
| [s3-24-G · Game MPO](https://contest.ucup.ac/contest/1890/problem/9965) | S3 Poland | 图论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.13） |
| [s3-30-E · Fractal Maze](https://contest.ucup.ac/contest/1917/problem/10091) | S3 Northern | 动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-31-I · Illuminati](https://contest.ucup.ac/contest/1924/problem/10122) | S3 Wroclaw | 图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.29） |
| [s3-31-J · Just Mining](https://contest.ucup.ac/contest/1924/problem/10123) | S3 Wroclaw | 图论、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.81） |
| [s3-31-L · Labyrinth](https://contest.ucup.ac/contest/1924/problem/10125) | S3 Wroclaw | 图论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.25） |
| [s3-32-E · Travel on the Grid](https://contest.ucup.ac/contest/1939/problem/10218) | S3 Dhaka | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.2） |
| [s3-32-H · Are the nodes reachable?](https://contest.ucup.ac/contest/1939/problem/10221) | S3 Dhaka | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.4） |
| [s3-33-H · Majority Graph](https://contest.ucup.ac/contest/1954/problem/10272) | S3 India | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.9） |
| [s3-33-N · Yet Another MST Problem](https://contest.ucup.ac/contest/1954/problem/10278) | S3 India | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.15） |
| [s3-34-A · Inversions of PQ and QP](https://contest.ucup.ac/contest/1965/problem/10321) | S3 Aobayama | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.48） |
| [s3-34-B · Matching Query](https://contest.ucup.ac/contest/1965/problem/10322) | S3 Aobayama | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.52） |
| [s3-34-H · 12 Grid](https://contest.ucup.ac/contest/1965/problem/10328) | S3 Aobayama | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.25） |
| [s3-34-N · Palindromic Path](https://contest.ucup.ac/contest/1965/problem/10334) | S3 Aobayama | 图论、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.34） |
| [s3-35-F · Red-Blue MST](https://contest.ucup.ac/contest/1993/problem/10706) | S3 Kraków | 图论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.4） |
| [s3-35-H · Decent Path Around Bajtów](https://contest.ucup.ac/contest/1993/problem/10708) | S3 Kraków | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-39-E · Edge Coloring Problem](https://contest.ucup.ac/contest/2071/problem/10974) | S3 Tokyo | 图论、构造 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-M · Minimum Distance Tree](https://contest.ucup.ac/contest/2071/problem/10982) | S3 Tokyo | 图论、树上算法 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-J · Housing Estate](https://contest.ucup.ac/contest/2135/problem/12159) | S3 Potyczki | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.145） |
| [s3-40-L · Directed Hanoi](https://contest.ucup.ac/contest/2135/problem/12161) | S3 Potyczki | 图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.329） |
| [s4-0-F · Mob Grinder](https://contest.ucup.ac/contest/2041/problem/11361) | S4 America | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.23） |
| [s4-0-G · Most Scenic Cycle](https://contest.ucup.ac/contest/2041/problem/11362) | S4 America | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.25） |
| [s4-1-B · Domain Compression](https://contest.ucup.ac/contest/2539/problem/14427) | S4 Korolyov | 多项式与线性代数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-F · Yet Another MST Problem](https://contest.ucup.ac/contest/2539/problem/14431) | S4 Korolyov | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-G · Cyclic Topsort](https://contest.ucup.ac/contest/2539/problem/14432) | S4 Korolyov | 概率期望与随机化、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-2-F · Framboise 2](https://contest.ucup.ac/contest/2551/problem/14135) | S4 Paris | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.3） |
| [s4-2-M · Manhattan Graph](https://contest.ucup.ac/contest/2551/problem/14142) | S4 Paris | 图论、计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.13） |
| [s4-3-A · Two Spanning Trees](https://contest.ucup.ac/contest/2559/problem/14415) | S4 Polar | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.1） |
| [s4-3-D · Disjoint Set Splitting](https://contest.ucup.ac/contest/2559/problem/14418) | S4 Polar | 数据结构、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-3-G · Far Away](https://contest.ucup.ac/contest/2559/problem/14421) | S4 Polar | 图论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-8-E · Enigma](https://contest.ucup.ac/contest/2668/problem/15448) | S4 Poland | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.93） |
| [s4-8-F · Finances](https://contest.ucup.ac/contest/2668/problem/15449) | S4 Poland | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.23） |
| [s4-8-G · Game of Pipes](https://contest.ucup.ac/contest/2668/problem/15450) | S4 Poland | 交互与信息编码、图论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.136） |
| [s4-10-C · Connecting Railway Stations](https://contest.ucup.ac/contest/2814/problem/16002) | S4 Wrocław | 树上算法、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.67） |
| [s4-10-J · Joyful Guided Tour](https://contest.ucup.ac/contest/2814/problem/16009) | S4 Wrocław | 图论、贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.93） |
| [s4-10-K · Key Properties](https://contest.ucup.ac/contest/2814/problem/16010) | S4 Wrocław | 构造、图论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.24） |
| [s4-11-D · Two Options](https://contest.ucup.ac/contest/2828/problem/16118) | S4 Southeastern Europe | 图论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.4） |
| [s4-11-H · Sorted Pairs](https://contest.ucup.ac/contest/2828/problem/16122) | S4 Southeastern Europe | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.8） |
| [s4-11-I · Colorful Components](https://contest.ucup.ac/contest/2828/problem/16123) | S4 Southeastern Europe | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.10） |
| [s4-13-I · Subgrid Connected Components](https://contest.ucup.ac/contest/2921/problem/16234) | S4 Ōokayama | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.15） |
| [s4-16-F · Fix the Coloring](https://contest.ucup.ac/contest/3347/problem/17155) | S4 Warsaw | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.8） |
| [s4-17-I · Wooden Checker](https://contest.ucup.ac/contest/3384/problem/17169) | S4 St. Petersburg | 图论、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.8） |
| [s4-17-K · Traversal of a Triangular Grid](https://contest.ucup.ac/contest/3384/problem/17171) | S4 St. Petersburg | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.11） |
| [s4-17-M · Construction Company](https://contest.ucup.ac/contest/3384/problem/17173) | S4 St. Petersburg | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.13） |
| [s4-18-I · Inversion Graph](https://contest.ucup.ac/contest/3420/problem/17254) | S4 Hongō | 组合计数、多项式与线性代数、图论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15607) |
| [s4-19-H · Helpful Bits](https://contest.ucup.ac/contest/3426/problem/17267) | S4 Belarus | 图论、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.5） |
| [s4-19-I · Ivan Tsarevich in the Magical Grove](https://contest.ucup.ac/contest/3426/problem/17268) | S4 Belarus | 图论、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-20-B · Palindrome and Permutation](https://contest.ucup.ac/contest/3516/problem/17407) | S4 India | 图论、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.3） |
| [s4-20-M · Vertex Separation](https://contest.ucup.ac/contest/3516/problem/17418) | S4 India | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.20） |
| [s4-21-A · 01 Matrix](https://contest.ucup.ac/contest/3542/problem/17419) | S4 Kamigō | 位运算与状态压缩、图论、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18120) |
| [s4-22-E · Ball Dumping Golf](https://contest.ucup.ac/contest/3575/problem/17717) | S4 Kyoto | 图论、组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.5） |
| [s4-22-F · 1e16 Cities](https://contest.ucup.ac/contest/3575/problem/17718) | S4 Kyoto | 数论、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-22-N · Cellular Component Constellation](https://contest.ucup.ac/contest/3575/problem/17726) | S4 Kyoto | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.11） |
| [s4-25-C · Crooked Cycles](https://contest.ucup.ac/contest/3773/problem/18403) | S4 Zagreb | 图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.11） |
| [s4-25-F · Flipping Frenzy](https://contest.ucup.ac/contest/3773/problem/18406) | S4 Zagreb | 多项式与线性代数、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.22） |
| [s4-25-L · Loop Land](https://contest.ucup.ac/contest/3773/problem/18412) | S4 Zagreb | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.45） |
| [s4-Extra-3-B · Word Generator](https://contest.ucup.ac/contest/2757/problem/15518) | S4 Osijek | 图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-H · Magical Puzzles](https://contest.ucup.ac/contest/2757/problem/15524) | S4 Osijek | 概率期望与随机化、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s5-1-C · Cost of Conflicts](https://contest.ucup.ac/contest/4126/problem/20250) | S5 Nizhny Novgorod | 图论、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.5） |
| [s5-1-L · Leave Triple & Link Tree](https://contest.ucup.ac/contest/4126/problem/20259) | S5 Nizhny Novgorod | 图论、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.22） |
| [s5-3-H · Hamiltonian LCM](https://contest.ucup.ac/contest/4565/problem/20736) | S5 Gorkovskaya | 图论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.6） |
| [s5-3-I · Interval MST](https://contest.ucup.ac/contest/4565/problem/20737) | S5 Gorkovskaya | 图论、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.8） |
| [s5-6-D · Go Robots](https://contest.ucup.ac/contest/4617/problem/23672) | S5 Hyakumanben | 图论、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.8） |
| [s5-6-F · Path XOR on MST](https://contest.ucup.ac/contest/4617/problem/23674) | S5 Hyakumanben | 图论、位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |
| [s5-6-G · Source to Sink](https://contest.ucup.ac/contest/4617/problem/23675) | S5 Hyakumanben | 图论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.11） |
| [s5-6-L · Consecutive Pairs](https://contest.ucup.ac/contest/4617/problem/23680) | S5 Hyakumanben | 交互与信息编码、搜索与二分、图论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.23） |

### 树上算法

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-A · Bandits](https://contest.ucup.ac/contest/1070/problem/5249) | S1 Slovenia | 树上算法、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.14） |
| [s1-8-D · Deforestation](https://contest.ucup.ac/contest/1070/problem/5252) | S1 Slovenia | 贪心、树上算法 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.3） |
| [s1-12-A · XOR Tree Path](https://contest.ucup.ac/contest/1207/problem/6317) | S1 Ōokayama | 树上算法、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-F · Forestry](https://contest.ucup.ac/contest/1207/problem/6322) | S1 Ōokayama | 树上算法、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-20-D · Central Subset](https://contest.ucup.ac/contest/1259/problem/6634) | S1 India | 图论、树上算法 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.14） |
| [s1-20-H · Treelection](https://contest.ucup.ac/contest/1259/problem/6638) | S1 India | 树上算法、动态规划、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.28） |
| [s2-6-B · The Doubling Game 2](https://contest.ucup.ac/contest/1398/problem/7607) | S2 Warsaw | 树上算法、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-C · Cliques](https://contest.ucup.ac/contest/1398/problem/7608) | S2 Warsaw | 树上算法、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-D · Colonization](https://contest.ucup.ac/contest/1398/problem/7609) | S2 Warsaw | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-E · Bus Lines](https://contest.ucup.ac/contest/1398/problem/7610) | S2 Warsaw | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-14-E · Eliminate Tree](https://contest.ucup.ac/contest/1452/problem/7936) | S2 Southeastern Europe | 树上算法、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.6） |
| [s2-18-A · Anti-Plagiarism](https://contest.ucup.ac/contest/1475/problem/8003) | S2 Dolgoprudny | 树上算法、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-18-J · Jumping Lights](https://contest.ucup.ac/contest/1475/problem/8012) | S2 Dolgoprudny | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.6） |
| [s2-19-C · Yet Another Balanced Coloring Problem](https://contest.ucup.ac/contest/1487/problem/8130) | S2 Estonia | 树上算法、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.6） |
| [s2-19-G · LCA Counting](https://contest.ucup.ac/contest/1487/problem/8134) | S2 Estonia | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.11） |
| [s2-21-G · Graffiti](https://contest.ucup.ac/contest/1511/problem/8213) | S2 Delft | 树上算法、动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.5） |
| [s2-21-I · Isomorphic Delight](https://contest.ucup.ac/contest/1511/problem/8215) | S2 Delft | 树上算法、搜索与二分、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.7） |
| [s3-2-B · Roars III](https://contest.ucup.ac/contest/1699/problem/8518) | S3 Zielona Gora | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.13） |
| [s3-5-K · Train Depot](https://contest.ucup.ac/contest/1741/problem/9140) | S3 Moscow | 树上算法、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-C · -is-this-bitset-](https://contest.ucup.ac/contest/1762/problem/9169) | S3 Osijek | 树上算法、动态规划、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-K · Routing K-Codes](https://contest.ucup.ac/contest/1774/problem/9230) | S3 Warsaw | 树上算法、动态规划 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-18-M · Enchanted Lawns Quest](https://contest.ucup.ac/contest/1849/problem/9793) | S3 Southeastern Europe | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.16） |
| [s3-21-G · Diverge and Converge](https://contest.ucup.ac/contest/1872/problem/9881) | S3 Ōokayama | 树上算法、构造 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11092) |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-27-F · Fast Tree Queries](https://contest.ucup.ac/contest/1901/problem/8616) | S3 London | 树上算法、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-30-K · Vortex](https://contest.ucup.ac/contest/1917/problem/10097) | S3 Northern | 树上算法、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.5） |
| [s3-32-B · Gona Guni](https://contest.ucup.ac/contest/1939/problem/10215) | S3 Dhaka | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-C · Packet Transmission](https://contest.ucup.ac/contest/1939/problem/10216) | S3 Dhaka | 树上算法 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-M · Tree Flip](https://contest.ucup.ac/contest/1939/problem/10226) | S3 Dhaka | 树上算法、数据结构、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.7） |
| [s3-33-D · Counting Distance Arrays](https://contest.ucup.ac/contest/1954/problem/10268) | S3 India | 树上算法、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.4） |
| [s3-35-B · ICFC World Finals](https://contest.ucup.ac/contest/1993/problem/10702) | S3 Kraków | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-G · Road Trip](https://contest.ucup.ac/contest/1993/problem/10707) | S3 Kraków | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-35-K · Bitter](https://contest.ucup.ac/contest/1993/problem/10711) | S3 Kraków | 字符串、树上算法、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.8） |
| [s3-39-M · Minimum Distance Tree](https://contest.ucup.ac/contest/2071/problem/10982) | S3 Tokyo | 图论、树上算法 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-P · Perfect Suika Game on a Tree](https://contest.ucup.ac/contest/2071/problem/10985) | S3 Tokyo | 树上算法、数据结构、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s4-0-B · Circle of Leaf](https://contest.ucup.ac/contest/2041/problem/11357) | S4 America | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.12） |
| [s4-0-H · Ornaments on a Tree](https://contest.ucup.ac/contest/2041/problem/11363) | S4 America | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.32） |
| [s4-2-A · Apple Tree](https://contest.ucup.ac/contest/2551/problem/14130) | S4 Paris | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-L · Lice Hopping](https://contest.ucup.ac/contest/2551/problem/14141) | S4 Paris | 树上算法、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-3-B · Christmas Tree](https://contest.ucup.ac/contest/2559/problem/14416) | S4 Polar | 树上算法、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-10-C · Connecting Railway Stations](https://contest.ucup.ac/contest/2814/problem/16002) | S4 Wrocław | 树上算法、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.67） |
| [s4-17-G · Traffic Lights](https://contest.ucup.ac/contest/3384/problem/17167) | S4 St. Petersburg | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.5） |
| [s4-17-H · Sweet Remainders!](https://contest.ucup.ac/contest/3384/problem/17168) | S4 St. Petersburg | 树上算法、构造、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.7） |
| [s4-18-B · Binary Tree Counting](https://contest.ucup.ac/contest/3420/problem/17247) | S4 Hongō | 树上算法、动态规划、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15693) |
| [s4-20-L · Alice and Bob](https://contest.ucup.ac/contest/3516/problem/17417) | S4 India | 树上算法、博弈论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.19） |
| [s4-22-G · The Symbolic Tree](https://contest.ucup.ac/contest/3575/problem/17719) | S4 Kyoto | 树上算法、动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-22-H · How to Validate Such a Program](https://contest.ucup.ac/contest/3575/problem/17720) | S4 Kyoto | 多项式与线性代数、交互与信息编码、树上算法 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-25-B · Big Balls](https://contest.ucup.ac/contest/3773/problem/18402) | S4 Zagreb | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.7） |
| [s4-25-M · Maximum Mex](https://contest.ucup.ac/contest/3773/problem/18413) | S4 Zagreb | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.49） |
| [s4-Extra-3-G · Amoeba Tree](https://contest.ucup.ac/contest/2757/problem/15523) | S4 Osijek | 树上算法、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s4-Extra-3-I · Bobs Rating](https://contest.ucup.ac/contest/2757/problem/15525) | S4 Osijek | 树上算法、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s4-Extra-3-L · Robots](https://contest.ucup.ac/contest/2757/problem/15528) | S4 Osijek | 树上算法、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-3-B · Binary Rotations](https://contest.ucup.ac/contest/4565/problem/20730) | S5 Gorkovskaya | 树上算法、数据结构、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.2） |
| [s5-3-L · Leaf Meeting](https://contest.ucup.ac/contest/4565/problem/20740) | S5 Gorkovskaya | 树上算法、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.12） |
| [s5-3-M · Matching Substrings](https://contest.ucup.ac/contest/4565/problem/20741) | S5 Gorkovskaya | 字符串、树上算法、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.13） |

### 数论

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-7-A · Square Sum](https://contest.ucup.ac/contest/1129/problem/5738) | S1 Zaporizhzhia | 数论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.1） |
| [s1-12-L · Many Products](https://contest.ucup.ac/contest/1207/problem/6328) | S1 Ōokayama | 数论、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.7） |
| [s1-13-H · Exact Subsequences](https://contest.ucup.ac/contest/1212/problem/6351) | S1 Iberia | 数论、搜索与二分、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-16-A · Classical A+B Problem](https://contest.ucup.ac/contest/1223/problem/6407) | S1 Gomel | 搜索与二分、数论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.1） |
| [s2-2-C · Many Many Cycles](https://contest.ucup.ac/contest/1356/problem/7177) | S2 SPb | 图论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.6） |
| [s2-5-D · Two Missing Numbers](https://contest.ucup.ac/contest/1388/problem/6549) | S2 Northern | 数论、位运算与状态压缩、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3)（文件 p.7） |
| [s2-6-A · Digital Nim](https://contest.ucup.ac/contest/1398/problem/7606) | S2 Warsaw | 博弈论、动态规划、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-H · Inverse Problem](https://contest.ucup.ac/contest/1398/problem/7613) | S2 Warsaw | 搜索与二分、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-7-H · Forbidden Set](https://contest.ucup.ac/contest/1399/problem/7639) | S2 Two Capitals | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-19-E · Freshman's Dream](https://contest.ucup.ac/contest/1487/problem/8132) | S2 Estonia | 构造、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.8） |
| [s2-20-A · Numerous Elimination](https://contest.ucup.ac/contest/1499/problem/8165) | S2 Ōokayama | 动态规划、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.1） |
| [s2-20-C · Yet Another Simple Math Problem](https://contest.ucup.ac/contest/1499/problem/8167) | S2 Ōokayama | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.2） |
| [s2-20-E · R-Connected Components](https://contest.ucup.ac/contest/1499/problem/8169) | S2 Ōokayama | 数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.5） |
| [s2-20-M · Sum is Integer](https://contest.ucup.ac/contest/1499/problem/8177) | S2 Ōokayama | 数论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.16） |
| [s2-21-J · Jumbled Primes](https://contest.ucup.ac/contest/1511/problem/8216) | S2 Delft | 交互与信息编码、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.8） |
| [s2-26-D · DiviDuelo](https://contest.ucup.ac/contest/1576/problem/8508) | S2 Latin America | 博弈论、数论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.5） |
| [s2-26-F · Fair Distribution](https://contest.ucup.ac/contest/1576/problem/8510) | S2 Latin America | 数论、动态规划 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.7） |
| [s2-26-G · Greek Casino](https://contest.ucup.ac/contest/1576/problem/8511) | S2 Latin America | 概率期望与随机化、动态规划、数论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.8） |
| [s3-1-B · Schoolgirls](https://contest.ucup.ac/contest/1696/problem/8782) | S3 St. Petersburg | 计算几何、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.7） |
| [s3-1-F · The Whole World](https://contest.ucup.ac/contest/1696/problem/8786) | S3 St. Petersburg | 多项式与线性代数、数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.85） |
| [s3-4-F · Flip or Not](https://contest.ucup.ac/contest/1738/problem/9118) | S3 Hongo | 多项式与线性代数、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.32） |
| [s3-4-J · Japanese Gift Money](https://contest.ucup.ac/contest/1738/problem/9122) | S3 Hongo | 数论、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.64） |
| [s3-5-J · Prefix Divisible by Suffix](https://contest.ucup.ac/contest/1741/problem/9139) | S3 Moscow | 数论、组合计数、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-A · Coprime Array](https://contest.ucup.ac/contest/1762/problem/9167) | S3 Osijek | 数论、构造、概率期望与随机化 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-F · Fibonacci Fusion](https://contest.ucup.ac/contest/1774/problem/9225) | S3 Warsaw | 数论、概率期望与随机化、数值计算 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-I · ICPC Inference](https://contest.ucup.ac/contest/1774/problem/9228) | S3 Warsaw | 数论、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-13-D · And DNA](https://contest.ucup.ac/contest/1812/problem/9479) | S3 Sendai | 数论、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.25） |
| [s3-13-J · (mod N² + 1)](https://contest.ucup.ac/contest/1812/problem/9485) | S3 Sendai | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.47） |
| [s3-18-B · NonZero PrefSuf Sums](https://contest.ucup.ac/contest/1849/problem/9782) | S3 Southeastern Europe | 贪心、数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.2） |
| [s3-21-F · Origami Warp](https://contest.ucup.ac/contest/1872/problem/9880) | S3 Ōokayama | 计算几何、数论 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11224) |
| [s3-24-D · Diminishing Fractions](https://contest.ucup.ac/contest/1890/problem/9962) | S3 Poland | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.111） |
| [s3-24-F · Frogs](https://contest.ucup.ac/contest/1890/problem/9964) | S3 Poland | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.162） |
| [s3-30-F · Interactive Primality](https://contest.ucup.ac/contest/1917/problem/10092) | S3 Northern | 交互与信息编码、数论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.3） |
| [s3-31-B · Bad Digits](https://contest.ucup.ac/contest/1924/problem/10115) | S3 Wroclaw | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.19） |
| [s3-31-D · Divisors](https://contest.ucup.ac/contest/1924/problem/10117) | S3 Wroclaw | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.15） |
| [s3-33-J · Max Mod](https://contest.ucup.ac/contest/1954/problem/10274) | S3 India | 数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.11） |
| [s3-34-L · Square Connection](https://contest.ucup.ac/contest/1965/problem/10332) | S3 Aobayama | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.18） |
| [s3-35-E · Gambling](https://contest.ucup.ac/contest/1993/problem/10705) | S3 Kraków | 概率期望与随机化、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.3） |
| [s3-35-I · Random Remainders](https://contest.ucup.ac/contest/1993/problem/10709) | S3 Kraków | 数论、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-39-D · Digits of Prefix Product](https://contest.ucup.ac/contest/2071/problem/10973) | S3 Tokyo | 构造、数论 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-B · Collatz Sum](https://contest.ucup.ac/contest/2135/problem/12151) | S3 Potyczki | 数论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.251） |
| [s4-0-A · A Totient Quotient](https://contest.ucup.ac/contest/2041/problem/11356) | S4 America | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.2） |
| [s4-0-M · This Is Sparta!](https://contest.ucup.ac/contest/2041/problem/11368) | S4 America | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.53） |
| [s4-1-A · Grid Problem](https://contest.ucup.ac/contest/2539/problem/14426) | S4 Korolyov | 组合计数、多项式与线性代数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.1） |
| [s4-2-D · Digit Division](https://contest.ucup.ac/contest/2551/problem/14133) | S4 Paris | 数论、构造、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-3-K · Game on Board](https://contest.ucup.ac/contest/2559/problem/14425) | S4 Polar | 博弈论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.6） |
| [s4-8-A · AIMPPZ](https://contest.ucup.ac/contest/2668/problem/15444) | S4 Poland | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.4） |
| [s4-10-K · Key Properties](https://contest.ucup.ac/contest/2814/problem/16010) | S4 Wrocław | 构造、图论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.24） |
| [s4-13-D · Grid Path Tree](https://contest.ucup.ac/contest/2921/problem/16229) | S4 Ōokayama | 组合计数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.5） |
| [s4-16-C · Copy-paste](https://contest.ucup.ac/contest/3347/problem/17152) | S4 Warsaw | 数论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.5） |
| [s4-17-H · Sweet Remainders!](https://contest.ucup.ac/contest/3384/problem/17168) | S4 St. Petersburg | 树上算法、构造、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.7） |
| [s4-17-J · Euler Line](https://contest.ucup.ac/contest/3384/problem/17170) | S4 St. Petersburg | 计算几何、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.8） |
| [s4-18-D · Divisible by 11](https://contest.ucup.ac/contest/3420/problem/17249) | S4 Hongō | 多项式与线性代数、组合计数、数论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16122) |
| [s4-18-L · Linear Floor](https://contest.ucup.ac/contest/3420/problem/17257) | S4 Hongō | 数论、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15885) |
| [s4-19-A · Art of Multiplication](https://contest.ucup.ac/contest/3426/problem/17260) | S4 Belarus | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.1） |
| [s4-19-E · Encountering a Friend](https://contest.ucup.ac/contest/3426/problem/17264) | S4 Belarus | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-20-I · Point Mirror](https://contest.ucup.ac/contest/3516/problem/17414) | S4 India | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.14） |
| [s4-21-K · Talk Event](https://contest.ucup.ac/contest/3542/problem/17429) | S4 Kamigō | 组合计数、数论 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17343) |
| [s4-22-F · 1e16 Cities](https://contest.ucup.ac/contest/3575/problem/17718) | S4 Kyoto | 数论、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-22-J · Sum of max of iai](https://contest.ucup.ac/contest/3575/problem/17722) | S4 Kyoto | 组合计数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.8） |
| [s4-22-K · Square Resistance Value](https://contest.ucup.ac/contest/3575/problem/17723) | S4 Kyoto | 数论、构造、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-25-I · Intricate Instrument](https://contest.ucup.ac/contest/3773/problem/18409) | S4 Zagreb | 数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.34） |
| [s5-1-B · Beggar Robin](https://contest.ucup.ac/contest/4126/problem/20249) | S5 Nizhny Novgorod | 数论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.3） |
| [s5-1-D · Digesting](https://contest.ucup.ac/contest/4126/problem/20251) | S5 Nizhny Novgorod | 数论、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.8） |
| [s5-1-J · Jaded Juice](https://contest.ucup.ac/contest/4126/problem/20257) | S5 Nizhny Novgorod | 贪心、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.19） |
| [s5-1-K · Kitchen Knives](https://contest.ucup.ac/contest/4126/problem/20258) | S5 Nizhny Novgorod | 组合计数、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.21） |
| [s5-1-N · Native Niuean](https://contest.ucup.ac/contest/4126/problem/20261) | S5 Nizhny Novgorod | 数论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.27） |
| [s5-3-E · Equal Totients](https://contest.ucup.ac/contest/4565/problem/20733) | S5 Gorkovskaya | 数论、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.4） |
| [s5-3-L · Leaf Meeting](https://contest.ucup.ac/contest/4565/problem/20740) | S5 Gorkovskaya | 树上算法、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.12） |
| [s5-6-E · K-Independent Matrix](https://contest.ucup.ac/contest/4617/problem/23673) | S5 Hyakumanben | 数论、构造、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |
| [s5-6-J · Hugest Number](https://contest.ucup.ac/contest/4617/problem/23678) | S5 Hyakumanben | 数论、字符串、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.15） |

### 组合计数

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-B · Binary Arrays and Sliding Sums](https://contest.ucup.ac/contest/1106/problem/5518) | S1 Ukraine | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.1） |
| [s1-4-C · Count Hamiltonian Cycles](https://contest.ucup.ac/contest/1106/problem/5519) | S1 Ukraine | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.2） |
| [s1-4-H · Help Me to Get This Published](https://contest.ucup.ac/contest/1106/problem/5524) | S1 Ukraine | 动态规划、组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.5） |
| [s1-4-I · Increasing Grid](https://contest.ucup.ac/contest/1106/problem/5525) | S1 Ukraine | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-4-M · Most Annoying Constructive Problem](https://contest.ucup.ac/contest/1106/problem/5529) | S1 Ukraine | 构造、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.9） |
| [s1-4-N · No Zero-Sum Subsegment](https://contest.ucup.ac/contest/1106/problem/5530) | S1 Ukraine | 组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.10） |
| [s1-7-B · Super Meat Bros](https://contest.ucup.ac/contest/1129/problem/5739) | S1 Zaporizhzhia | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.2） |
| [s1-7-G · Palindromic Differences](https://contest.ucup.ac/contest/1129/problem/5744) | S1 Zaporizhzhia | 组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.13） |
| [s1-7-H · Graph Isomorphism](https://contest.ucup.ac/contest/1129/problem/5745) | S1 Zaporizhzhia | 图论、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.14） |
| [s1-7-J · Persian Casino](https://contest.ucup.ac/contest/1129/problem/5747) | S1 Zaporizhzhia | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.15） |
| [s1-7-L · Directed Vertex Cacti](https://contest.ucup.ac/contest/1129/problem/5749) | S1 Zaporizhzhia | 组合计数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.16） |
| [s1-12-E · Five Med Sum](https://contest.ucup.ac/contest/1207/problem/6321) | S1 Ōokayama | 组合计数、贪心 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-12-G · Range NEQ](https://contest.ucup.ac/contest/1207/problem/6323) | S1 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.4） |
| [s1-12-I · Peaceful Results](https://contest.ucup.ac/contest/1207/problem/6325) | S1 Ōokayama | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.6） |
| [s1-12-K · Count Arithmetic Progression](https://contest.ucup.ac/contest/1207/problem/6327) | S1 Ōokayama | 计算几何、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.7） |
| [s1-13-C · Record Parity](https://contest.ucup.ac/contest/1212/problem/6346) | S1 Iberia | 组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.1） |
| [s1-13-H · Exact Subsequences](https://contest.ucup.ac/contest/1212/problem/6351) | S1 Iberia | 数论、搜索与二分、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-13-J · Kth Lex Min Min Min Subpalindromes](https://contest.ucup.ac/contest/1212/problem/6353) | S1 Iberia | 字符串、构造、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-B · Classical Counting Problem](https://contest.ucup.ac/contest/1223/problem/6408) | S1 Gomel | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.1） |
| [s1-16-D · Classical DP Problem](https://contest.ucup.ac/contest/1223/problem/6410) | S1 Gomel | 动态规划、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.2） |
| [s1-16-E · Classical FFT Problem](https://contest.ucup.ac/contest/1223/problem/6411) | S1 Gomel | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-16-K · Classical Summation Problem](https://contest.ucup.ac/contest/1223/problem/6417) | S1 Gomel | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-G · Perfect Strings](https://contest.ucup.ac/contest/1259/problem/6637) | S1 India | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.24） |
| [s1-20-J · Talk That Talk](https://contest.ucup.ac/contest/1259/problem/6640) | S1 India | 组合计数、动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.35） |
| [s2-5-F · Forever Young](https://contest.ucup.ac/contest/1388/problem/6551) | S2 Northern | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.11） |
| [s2-5-I · Endless Road](https://contest.ucup.ac/contest/1388/problem/6554) | S2 Northern | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.21） |
| [s2-5-J · Sets May Be Good](https://contest.ucup.ac/contest/1388/problem/6555) | S2 Northern | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.30） |
| [s2-6-C · Cliques](https://contest.ucup.ac/contest/1398/problem/7608) | S2 Warsaw | 树上算法、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-M · Pattern Search](https://contest.ucup.ac/contest/1398/problem/7618) | S2 Warsaw | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-7-A · Balanced Arrays](https://contest.ucup.ac/contest/1399/problem/7632) | S2 Two Capitals | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-M · Good Splits](https://contest.ucup.ac/contest/1399/problem/7644) | S2 Two Capitals | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.8） |
| [s2-16-A · Bracket-and-bar Sequences](https://contest.ucup.ac/contest/1465/problem/4824) | S2 Run Twice | 组合计数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.5） |
| [s2-16-K · Trijection](https://contest.ucup.ac/contest/1465/problem/4834) | S2 Run Twice | 组合计数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.158） |
| [s2-18-H · Hierarchies of Judges](https://contest.ucup.ac/contest/1475/problem/8010) | S2 Dolgoprudny | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.5） |
| [s2-20-K · Dense Planting](https://contest.ucup.ac/contest/1499/problem/8175) | S2 Ōokayama | 图论、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.14） |
| [s2-20-L · Next TTPC 3](https://contest.ucup.ac/contest/1499/problem/8176) | S2 Ōokayama | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.15） |
| [s2-20-N · Bracket Sequestion](https://contest.ucup.ac/contest/1499/problem/8178) | S2 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.16） |
| [s2-20-P · Bridge Elimination](https://contest.ucup.ac/contest/1499/problem/8180) | S2 Ōokayama | 组合计数、动态规划、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.19） |
| [s2-21-A · Anton's ABCD](https://contest.ucup.ac/contest/1511/problem/8207) | S2 Delft | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-E · Enumerating Substrings](https://contest.ucup.ac/contest/1511/problem/8211) | S2 Delft | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-I · Isomorphic Delight](https://contest.ucup.ac/contest/1511/problem/8215) | S2 Delft | 树上算法、搜索与二分、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.7） |
| [s2-21-K · King's Dinner](https://contest.ucup.ac/contest/1511/problem/8217) | S2 Delft | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.9） |
| [s3-0-E · House Deconstruction](https://contest.ucup.ac/contest/1695/problem/8772) | S3 America | 贪心、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.10） |
| [s3-1-E · Fake Coin and Lying Scales](https://contest.ucup.ac/contest/1696/problem/8785) | S3 St. Petersburg | 组合计数、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.65） |
| [s3-1-L · Candies](https://contest.ucup.ac/contest/1696/problem/8792) | S3 St. Petersburg | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.192） |
| [s3-2-A · Interesting Paths](https://contest.ucup.ac/contest/1699/problem/8517) | S3 Zielona Gora | 图论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.2） |
| [s3-2-M · Balance of Permutation](https://contest.ucup.ac/contest/1699/problem/8529) | S3 Zielona Gora | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.232） |
| [s3-4-D · DRD String](https://contest.ucup.ac/contest/1738/problem/9116) | S3 Hongo | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.20） |
| [s3-4-H · Huge Segment Tree](https://contest.ucup.ac/contest/1738/problem/9120) | S3 Hongo | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.50） |
| [s3-4-I · I Love Marathon Contest](https://contest.ucup.ac/contest/1738/problem/9121) | S3 Hongo | 组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.56） |
| [s3-4-M · Majority and Permutation](https://contest.ucup.ac/contest/1738/problem/9125) | S3 Hongo | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.87） |
| [s3-4-N · Number of Abbreviations](https://contest.ucup.ac/contest/1738/problem/9126) | S3 Hongo | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.92） |
| [s3-5-A · Counting Permutations](https://contest.ucup.ac/contest/1741/problem/9130) | S3 Moscow | 组合计数、贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-J · Prefix Divisible by Suffix](https://contest.ucup.ac/contest/1741/problem/9139) | S3 Moscow | 数论、组合计数、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-H · Game Design](https://contest.ucup.ac/contest/1762/problem/9174) | S3 Osijek | 动态规划、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-A · Bus Analysis](https://contest.ucup.ac/contest/1774/problem/9220) | S3 Warsaw | 动态规划、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-I · ICPC Inference](https://contest.ucup.ac/contest/1774/problem/9228) | S3 Warsaw | 数论、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-B · Some Sum of Subset](https://contest.ucup.ac/contest/1804/problem/9436) | S3 Sumiyosi | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10175) |
| [s3-11-G · Many Common Segment Problems](https://contest.ucup.ac/contest/1804/problem/9441) | S3 Sumiyosi | 多项式与线性代数、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10026) |
| [s3-11-I · Left Equals Right](https://contest.ucup.ac/contest/1804/problem/9443) | S3 Sumiyosi | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10176) |
| [s3-11-J · Again Permutation Problem](https://contest.ucup.ac/contest/1804/problem/9444) | S3 Sumiyosi | 动态规划、图论、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10019) |
| [s3-13-A · 012 Grid](https://contest.ucup.ac/contest/1812/problem/9476) | S3 Sendai | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.8） |
| [s3-13-B · Topological Sort](https://contest.ucup.ac/contest/1812/problem/9477) | S3 Sendai | 组合计数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.13） |
| [s3-13-K · Random Mex](https://contest.ucup.ac/contest/1812/problem/9486) | S3 Sendai | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.53） |
| [s3-18-E · Shrooks](https://contest.ucup.ac/contest/1849/problem/9785) | S3 Southeastern Europe | 组合计数、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.6） |
| [s3-18-I · Donkey, Keep Watch](https://contest.ucup.ac/contest/1849/problem/9789) | S3 Southeastern Europe | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.11） |
| [s3-21-B · Self Checkout](https://contest.ucup.ac/contest/1872/problem/9876) | S3 Ōokayama | 组合计数、字符串 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11403) |
| [s3-21-L · Long Sequence Inversion 2](https://contest.ucup.ac/contest/1872/problem/9886) | S3 Ōokayama | 组合计数、位运算与状态压缩 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11222) |
| [s3-32-B · Gona Guni](https://contest.ucup.ac/contest/1939/problem/10215) | S3 Dhaka | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-L · Uncle Bob and XOR Sum](https://contest.ucup.ac/contest/1939/problem/10225) | S3 Dhaka | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.6） |
| [s3-33-D · Counting Distance Arrays](https://contest.ucup.ac/contest/1954/problem/10268) | S3 India | 树上算法、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.4） |
| [s3-33-E · Easy Counting Problem](https://contest.ucup.ac/contest/1954/problem/10269) | S3 India | 概率期望与随机化、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.5） |
| [s3-34-F · Another Long Sequence Inversion](https://contest.ucup.ac/contest/1965/problem/10326) | S3 Aobayama | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.56） |
| [s3-34-K · Shuffle and Max Bracket Score](https://contest.ucup.ac/contest/1965/problem/10331) | S3 Aobayama | 概率期望与随机化、贪心、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.72） |
| [s3-34-O · Twin Contests](https://contest.ucup.ac/contest/1965/problem/10335) | S3 Aobayama | 组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.30） |
| [s3-35-D · Money in the Hat](https://contest.ucup.ac/contest/1993/problem/10704) | S3 Kraków | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.3） |
| [s3-39-B · Bracket Character Frequency](https://contest.ucup.ac/contest/2071/problem/10971) | S3 Tokyo | 组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-C · Card Deck](https://contest.ucup.ac/contest/2071/problem/10972) | S3 Tokyo | 贪心、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-J · Journey through the Fractal](https://contest.ucup.ac/contest/2071/problem/10979) | S3 Tokyo | 贪心、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-O · One Different Inequality](https://contest.ucup.ac/contest/2071/problem/10984) | S3 Tokyo | 组合计数、多项式与线性代数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-D · Fern Market](https://contest.ucup.ac/contest/2135/problem/12153) | S3 Potyczki | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.55） |
| [s3-40-H · Merge Sort](https://contest.ucup.ac/contest/2135/problem/12157) | S3 Potyczki | 组合计数、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.138） |
| [s4-0-B · Circle of Leaf](https://contest.ucup.ac/contest/2041/problem/11357) | S4 America | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.12） |
| [s4-0-I · Polygon Partition](https://contest.ucup.ac/contest/2041/problem/11364) | S4 America | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.36） |
| [s4-1-A · Grid Problem](https://contest.ucup.ac/contest/2539/problem/14426) | S4 Korolyov | 组合计数、多项式与线性代数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.1） |
| [s4-1-E · Coffee Shops](https://contest.ucup.ac/contest/2539/problem/14430) | S4 Korolyov | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-2-A · Apple Tree](https://contest.ucup.ac/contest/2551/problem/14130) | S4 Paris | 树上算法、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-3-E · Maximum Segment Sum](https://contest.ucup.ac/contest/2559/problem/14419) | S4 Polar | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-8-C · Count Triangular Sequences](https://contest.ucup.ac/contest/2668/problem/15446) | S4 Poland | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.102） |
| [s4-11-A · Sum Game](https://contest.ucup.ac/contest/2828/problem/16115) | S4 Southeastern Europe | 博弈论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.1） |
| [s4-11-C · XOR-Excluding Sets](https://contest.ucup.ac/contest/2828/problem/16117) | S4 Southeastern Europe | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.3） |
| [s4-11-D · Two Options](https://contest.ucup.ac/contest/2828/problem/16118) | S4 Southeastern Europe | 图论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.4） |
| [s4-11-E · Phone Company](https://contest.ucup.ac/contest/2828/problem/16119) | S4 Southeastern Europe | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.5） |
| [s4-11-J · Triangle Hull](https://contest.ucup.ac/contest/2828/problem/16124) | S4 Southeastern Europe | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.12） |
| [s4-13-C · Sum of Three Inversions](https://contest.ucup.ac/contest/2921/problem/16228) | S4 Ōokayama | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.4） |
| [s4-13-D · Grid Path Tree](https://contest.ucup.ac/contest/2921/problem/16229) | S4 Ōokayama | 组合计数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.5） |
| [s4-13-H · Akari Counting](https://contest.ucup.ac/contest/2921/problem/16233) | S4 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.12） |
| [s4-13-J · Divide Polygon](https://contest.ucup.ac/contest/2921/problem/16235) | S4 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.17） |
| [s4-16-A · Three Castles](https://contest.ucup.ac/contest/3347/problem/17150) | S4 Warsaw | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.2） |
| [s4-16-G · Good Permutations](https://contest.ucup.ac/contest/3347/problem/17156) | S4 Warsaw | 数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.9） |
| [s4-16-I · Palindromes](https://contest.ucup.ac/contest/3347/problem/17158) | S4 Warsaw | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.13） |
| [s4-16-J · Jewel Guards](https://contest.ucup.ac/contest/3347/problem/17159) | S4 Warsaw | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.16） |
| [s4-17-C · String Workshop](https://contest.ucup.ac/contest/3384/problem/17163) | S4 St. Petersburg | 数据结构、字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.2） |
| [s4-17-E · Four Sages Around an Oak Tree](https://contest.ucup.ac/contest/3384/problem/17165) | S4 St. Petersburg | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.4） |
| [s4-18-B · Binary Tree Counting](https://contest.ucup.ac/contest/3420/problem/17247) | S4 Hongō | 树上算法、动态规划、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15693) |
| [s4-18-D · Divisible by 11](https://contest.ucup.ac/contest/3420/problem/17249) | S4 Hongō | 多项式与线性代数、组合计数、数论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16122) |
| [s4-18-E · Exchange or Not](https://contest.ucup.ac/contest/3420/problem/17250) | S4 Hongō | 动态规划、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16127) |
| [s4-18-I · Inversion Graph](https://contest.ucup.ac/contest/3420/problem/17254) | S4 Hongō | 组合计数、多项式与线性代数、图论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15607) |
| [s4-18-M · Max Conference](https://contest.ucup.ac/contest/3420/problem/17258) | S4 Hongō | 贪心、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15903) |
| [s4-18-N · Numerical Error](https://contest.ucup.ac/contest/3420/problem/17259) | S4 Hongō | 组合计数、搜索与二分、数值计算 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15904) |
| [s4-19-F · Forgot to Refuel](https://contest.ucup.ac/contest/3426/problem/17265) | S4 Belarus | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.4） |
| [s4-20-B · Palindrome and Permutation](https://contest.ucup.ac/contest/3516/problem/17407) | S4 India | 图论、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.3） |
| [s4-20-G · Sequence Domination](https://contest.ucup.ac/contest/3516/problem/17412) | S4 India | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.10） |
| [s4-20-J · Counting Is Fun](https://contest.ucup.ac/contest/3516/problem/17415) | S4 India | 动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.16） |
| [s4-20-L · Alice and Bob](https://contest.ucup.ac/contest/3516/problem/17417) | S4 India | 树上算法、博弈论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.19） |
| [s4-21-A · 01 Matrix](https://contest.ucup.ac/contest/3542/problem/17419) | S4 Kamigō | 位运算与状态压缩、图论、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18120) |
| [s4-21-B · Birds-of-Paradise' Card Game](https://contest.ucup.ac/contest/3542/problem/17420) | S4 Kamigō | 贪心、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17017) |
| [s4-21-J · Set Sequence](https://contest.ucup.ac/contest/3542/problem/17428) | S4 Kamigō | 组合计数、多项式与线性代数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18121) |
| [s4-21-K · Talk Event](https://contest.ucup.ac/contest/3542/problem/17429) | S4 Kamigō | 组合计数、数论 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17343) |
| [s4-21-M · Up-Down Sequence](https://contest.ucup.ac/contest/3542/problem/17431) | S4 Kamigō | 构造、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17005) |
| [s4-22-E · Ball Dumping Golf](https://contest.ucup.ac/contest/3575/problem/17717) | S4 Kyoto | 图论、组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.5） |
| [s4-22-J · Sum of max of iai](https://contest.ucup.ac/contest/3575/problem/17722) | S4 Kyoto | 组合计数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.8） |
| [s4-22-O · Xor Triangle](https://contest.ucup.ac/contest/3575/problem/17727) | S4 Kyoto | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.12） |
| [s4-25-K · Kempt Kale](https://contest.ucup.ac/contest/3773/problem/18411) | S4 Zagreb | 贪心、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.42） |
| [s4-Extra-3-F · Binary Permutation](https://contest.ucup.ac/contest/2757/problem/15522) | S4 Osijek | 组合计数、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s5-1-A · Astana Hard Metro](https://contest.ucup.ac/contest/4126/problem/20248) | S5 Nizhny Novgorod | 动态规划、概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.1） |
| [s5-1-B · Beggar Robin](https://contest.ucup.ac/contest/4126/problem/20249) | S5 Nizhny Novgorod | 数论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.3） |
| [s5-1-K · Kitchen Knives](https://contest.ucup.ac/contest/4126/problem/20258) | S5 Nizhny Novgorod | 组合计数、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.21） |
| [s5-1-N · Native Niuean](https://contest.ucup.ac/contest/4126/problem/20261) | S5 Nizhny Novgorod | 数论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.27） |
| [s5-3-A · Adjacent Decrements](https://contest.ucup.ac/contest/4565/problem/20729) | S5 Gorkovskaya | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.1） |
| [s5-3-B · Binary Rotations](https://contest.ucup.ac/contest/4565/problem/20730) | S5 Gorkovskaya | 树上算法、数据结构、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.2） |
| [s5-3-F · Flipping Lamps](https://contest.ucup.ac/contest/4565/problem/20734) | S5 Gorkovskaya | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.5） |
| [s5-3-H · Hamiltonian LCM](https://contest.ucup.ac/contest/4565/problem/20736) | S5 Gorkovskaya | 图论、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.6） |
| [s5-6-A · Fugaku NK-kei](https://contest.ucup.ac/contest/4617/problem/23669) | S5 Hyakumanben | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.1） |
| [s5-6-K · Dyads of Hanoi](https://contest.ucup.ac/contest/4617/problem/23679) | S5 Hyakumanben | 动态规划、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.19） |
| [s5-6-M · I hate prime numbers](https://contest.ucup.ac/contest/4617/problem/23681) | S5 Hyakumanben | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.24） |

### 多项式与线性代数

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-7-B · Super Meat Bros](https://contest.ucup.ac/contest/1129/problem/5739) | S1 Zaporizhzhia | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.2） |
| [s1-7-D · Triterminant](https://contest.ucup.ac/contest/1129/problem/5741) | S1 Zaporizhzhia | 图论、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.6） |
| [s1-7-F · Palindromic Polynomial](https://contest.ucup.ac/contest/1129/problem/5743) | S1 Zaporizhzhia | 多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.9） |
| [s1-7-K · Determinant, or...?](https://contest.ucup.ac/contest/1129/problem/5748) | S1 Zaporizhzhia | 多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.16） |
| [s1-8-I · Money Laundering](https://contest.ucup.ac/contest/1070/problem/5257) | S1 Slovenia | 多项式与线性代数、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.10） |
| [s1-12-G · Range NEQ](https://contest.ucup.ac/contest/1207/problem/6323) | S1 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.4） |
| [s1-12-H · Expanded Hull](https://contest.ucup.ac/contest/1207/problem/6324) | S1 Ōokayama | 计算几何、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.5） |
| [s1-12-I · Peaceful Results](https://contest.ucup.ac/contest/1207/problem/6325) | S1 Ōokayama | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.6） |
| [s1-12-L · Many Products](https://contest.ucup.ac/contest/1207/problem/6328) | S1 Ōokayama | 数论、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.7） |
| [s1-13-D · XOR Determinant](https://contest.ucup.ac/contest/1212/problem/6347) | S1 Iberia | 多项式与线性代数、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-16-E · Classical FFT Problem](https://contest.ucup.ac/contest/1223/problem/6411) | S1 Gomel | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-20-G · Perfect Strings](https://contest.ucup.ac/contest/1259/problem/6637) | S1 India | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.24） |
| [s2-2-M · Hardcore String Counting](https://contest.ucup.ac/contest/1356/problem/7187) | S2 SPb | 字符串、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.9） |
| [s2-5-C · Courses](https://contest.ucup.ac/contest/1388/problem/6548) | S2 Northern | 动态规划、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.2） |
| [s2-5-D · Two Missing Numbers](https://contest.ucup.ac/contest/1388/problem/6549) | S2 Northern | 数论、位运算与状态压缩、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3)（文件 p.7） |
| [s2-5-G · Good and Lucky Matrices](https://contest.ucup.ac/contest/1388/problem/6552) | S2 Northern | 多项式与线性代数、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3)（文件 p.2） |
| [s2-5-J · Sets May Be Good](https://contest.ucup.ac/contest/1388/problem/6555) | S2 Northern | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.30） |
| [s2-5-L · LCSLCSLCS](https://contest.ucup.ac/contest/1388/problem/6557) | S2 Northern | 字符串、动态规划、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.54） |
| [s2-6-G · Matrix Inverse](https://contest.ucup.ac/contest/1398/problem/7612) | S2 Warsaw | 多项式与线性代数、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.3） |
| [s2-7-A · Balanced Arrays](https://contest.ucup.ac/contest/1399/problem/7632) | S2 Two Capitals | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-C · Cards](https://contest.ucup.ac/contest/1399/problem/7634) | S2 Two Capitals | 多项式与线性代数、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-18-G · Growing Sequences](https://contest.ucup.ac/contest/1475/problem/8009) | S2 Dolgoprudny | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.4） |
| [s2-18-H · Hierarchies of Judges](https://contest.ucup.ac/contest/1475/problem/8010) | S2 Dolgoprudny | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.5） |
| [s2-19-F · When Anton Saw This Task He Reacted With 😩](https://contest.ucup.ac/contest/1487/problem/8133) | S2 Estonia | 多项式与线性代数、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.9） |
| [s2-19-H · Minimum Cost Flow²](https://contest.ucup.ac/contest/1487/problem/8135) | S2 Estonia | 多项式与线性代数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.12） |
| [s2-20-G · Cola](https://contest.ucup.ac/contest/1499/problem/8171) | S2 Ōokayama | 概率期望与随机化、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.8） |
| [s2-20-I · T Tile Placement Counting](https://contest.ucup.ac/contest/1499/problem/8173) | S2 Ōokayama | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.10） |
| [s2-20-K · Dense Planting](https://contest.ucup.ac/contest/1499/problem/8175) | S2 Ōokayama | 图论、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.14） |
| [s2-20-L · Next TTPC 3](https://contest.ucup.ac/contest/1499/problem/8176) | S2 Ōokayama | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.15） |
| [s2-20-N · Bracket Sequestion](https://contest.ucup.ac/contest/1499/problem/8178) | S2 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.16） |
| [s3-1-F · The Whole World](https://contest.ucup.ac/contest/1696/problem/8786) | S3 St. Petersburg | 多项式与线性代数、数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.85） |
| [s3-1-O · Mysterious Sequence](https://contest.ucup.ac/contest/1696/problem/8795) | S3 St. Petersburg | 搜索与二分、多项式与线性代数、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.231） |
| [s3-4-F · Flip or Not](https://contest.ucup.ac/contest/1738/problem/9118) | S3 Hongo | 多项式与线性代数、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.32） |
| [s3-4-H · Huge Segment Tree](https://contest.ucup.ac/contest/1738/problem/9120) | S3 Hongo | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.50） |
| [s3-4-M · Majority and Permutation](https://contest.ucup.ac/contest/1738/problem/9125) | S3 Hongo | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.87） |
| [s3-11-A · Welcome to NPCAPC](https://contest.ucup.ac/contest/1804/problem/9435) | S3 Sumiyosi | 动态规划、多项式与线性代数、字符串 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) |
| [s3-11-D · Two Box](https://contest.ucup.ac/contest/1804/problem/9438) | S3 Sumiyosi | 动态规划、多项式与线性代数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10024) |
| [s3-11-G · Many Common Segment Problems](https://contest.ucup.ac/contest/1804/problem/9441) | S3 Sumiyosi | 多项式与线性代数、组合计数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10026) |
| [s3-11-N · Product Matrix](https://contest.ucup.ac/contest/1804/problem/9448) | S3 Sumiyosi | 多项式与线性代数 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10025) |
| [s3-13-A · 012 Grid](https://contest.ucup.ac/contest/1812/problem/9476) | S3 Sendai | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.8） |
| [s3-13-D · And DNA](https://contest.ucup.ac/contest/1812/problem/9479) | S3 Sendai | 数论、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.25） |
| [s3-13-M · Do Not Turn Back](https://contest.ucup.ac/contest/1812/problem/9488) | S3 Sendai | 图论、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.63） |
| [s3-30-C · Elegia❄️ 's Mind](https://contest.ucup.ac/contest/1917/problem/10089) | S3 Northern | 多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-30-G · Jump the Frog](https://contest.ucup.ac/contest/1917/problem/10093) | S3 Northern | 多项式与线性代数、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-I · Product](https://contest.ucup.ac/contest/1917/problem/10095) | S3 Northern | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-L · Random Sum](https://contest.ucup.ac/contest/1917/problem/10098) | S3 Northern | 多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.5） |
| [s3-32-L · Uncle Bob and XOR Sum](https://contest.ucup.ac/contest/1939/problem/10225) | S3 Dhaka | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.6） |
| [s3-34-C · 2-Power Rush](https://contest.ucup.ac/contest/1965/problem/10323) | S3 Aobayama | 动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.40） |
| [s3-34-F · Another Long Sequence Inversion](https://contest.ucup.ac/contest/1965/problem/10326) | S3 Aobayama | 多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.56） |
| [s3-39-F · Fourier Coefficients](https://contest.ucup.ac/contest/2071/problem/10975) | S3 Tokyo | 多项式与线性代数、交互与信息编码 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-K · K-rep Array](https://contest.ucup.ac/contest/2071/problem/10980) | S3 Tokyo | 多项式与线性代数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-N · Nice Bouquets](https://contest.ucup.ac/contest/2071/problem/10983) | S3 Tokyo | 多项式与线性代数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-O · One Different Inequality](https://contest.ucup.ac/contest/2071/problem/10984) | S3 Tokyo | 组合计数、多项式与线性代数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s4-0-J · Popping Balloons](https://contest.ucup.ac/contest/2041/problem/11365) | S4 America | 概率期望与随机化、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.40） |
| [s4-1-A · Grid Problem](https://contest.ucup.ac/contest/2539/problem/14426) | S4 Korolyov | 组合计数、多项式与线性代数、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.1） |
| [s4-1-B · Domain Compression](https://contest.ucup.ac/contest/2539/problem/14427) | S4 Korolyov | 多项式与线性代数、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-10-B · Bit Recovery](https://contest.ucup.ac/contest/2814/problem/16001) | S4 Wrocław | 多项式与线性代数、位运算与状态压缩、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.104） |
| [s4-11-C · XOR-Excluding Sets](https://contest.ucup.ac/contest/2828/problem/16117) | S4 Southeastern Europe | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.3） |
| [s4-13-F · Decimal Pyramid](https://contest.ucup.ac/contest/2921/problem/16231) | S4 Ōokayama | 多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.9） |
| [s4-13-H · Akari Counting](https://contest.ucup.ac/contest/2921/problem/16233) | S4 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.12） |
| [s4-13-J · Divide Polygon](https://contest.ucup.ac/contest/2921/problem/16235) | S4 Ōokayama | 组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.17） |
| [s4-17-F · Pluses and Minuses](https://contest.ucup.ac/contest/3384/problem/17166) | S4 St. Petersburg | 多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.5） |
| [s4-18-D · Divisible by 11](https://contest.ucup.ac/contest/3420/problem/17249) | S4 Hongō | 多项式与线性代数、组合计数、数论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16122) |
| [s4-18-I · Inversion Graph](https://contest.ucup.ac/contest/3420/problem/17254) | S4 Hongō | 组合计数、多项式与线性代数、图论 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15607) |
| [s4-19-C · Cell Flip Game](https://contest.ucup.ac/contest/3426/problem/17262) | S4 Belarus | 位运算与状态压缩、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.2） |
| [s4-21-I · Penguin Flicker](https://contest.ucup.ac/contest/3542/problem/17427) | S4 Kamigō | 动态规划、多项式与线性代数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18125) |
| [s4-21-J · Set Sequence](https://contest.ucup.ac/contest/3542/problem/17428) | S4 Kamigō | 组合计数、多项式与线性代数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18121) |
| [s4-22-E · Ball Dumping Golf](https://contest.ucup.ac/contest/3575/problem/17717) | S4 Kyoto | 图论、组合计数、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.5） |
| [s4-22-G · The Symbolic Tree](https://contest.ucup.ac/contest/3575/problem/17719) | S4 Kyoto | 树上算法、动态规划、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-22-H · How to Validate Such a Program](https://contest.ucup.ac/contest/3575/problem/17720) | S4 Kyoto | 多项式与线性代数、交互与信息编码、树上算法 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-25-D · Dangerous Data](https://contest.ucup.ac/contest/3773/problem/18404) | S4 Zagreb | 多项式与线性代数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.14） |
| [s4-25-F · Flipping Frenzy](https://contest.ucup.ac/contest/3773/problem/18406) | S4 Zagreb | 多项式与线性代数、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.22） |
| [s5-1-F · Fresh Cartridges](https://contest.ucup.ac/contest/4126/problem/20253) | S5 Nizhny Novgorod | 多项式与线性代数、概率期望与随机化、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.11） |
| [s5-1-I · Incident in the Bakery](https://contest.ucup.ac/contest/4126/problem/20256) | S5 Nizhny Novgorod | 计算几何、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.16） |
| [s5-3-A · Adjacent Decrements](https://contest.ucup.ac/contest/4565/problem/20729) | S5 Gorkovskaya | 多项式与线性代数、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.1） |
| [s5-3-F · Flipping Lamps](https://contest.ucup.ac/contest/4565/problem/20734) | S5 Gorkovskaya | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.5） |
| [s5-6-B · PerMutation](https://contest.ucup.ac/contest/4617/problem/23670) | S5 Hyakumanben | 数据结构、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.4） |
| [s5-6-E · K-Independent Matrix](https://contest.ucup.ac/contest/4617/problem/23673) | S5 Hyakumanben | 数论、构造、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |
| [s5-6-J · Hugest Number](https://contest.ucup.ac/contest/4617/problem/23678) | S5 Hyakumanben | 数论、字符串、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.15） |
| [s5-6-M · I hate prime numbers](https://contest.ucup.ac/contest/4617/problem/23681) | S5 Hyakumanben | 组合计数、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.24） |

### 字符串

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-F · Differences](https://contest.ucup.ac/contest/1070/problem/5254) | S1 Slovenia | 字符串 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.9） |
| [s1-8-H · Insertions](https://contest.ucup.ac/contest/1070/problem/5256) | S1 Slovenia | 字符串 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.16） |
| [s1-13-J · Kth Lex Min Min Min Subpalindromes](https://contest.ucup.ac/contest/1212/problem/6353) | S1 Iberia | 字符串、构造、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-20-E · Strange Keyboard](https://contest.ucup.ac/contest/1259/problem/6635) | S1 India | 动态规划、字符串 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.18） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-2-M · Hardcore String Counting](https://contest.ucup.ac/contest/1356/problem/7187) | S2 SPb | 字符串、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.9） |
| [s2-5-K · Text Editor](https://contest.ucup.ac/contest/1388/problem/6556) | S2 Northern | 数据结构、字符串 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.49） |
| [s2-5-L · LCSLCSLCS](https://contest.ucup.ac/contest/1388/problem/6557) | S2 Northern | 字符串、动态规划、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.54） |
| [s2-6-M · Pattern Search](https://contest.ucup.ac/contest/1398/problem/7618) | S2 Warsaw | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-19-B · Binary Sequence](https://contest.ucup.ac/contest/1487/problem/8129) | S2 Estonia | 字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.6） |
| [s2-20-H · 404 Chotto Found](https://contest.ucup.ac/contest/1499/problem/8172) | S2 Ōokayama | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.9） |
| [s2-21-E · Enumerating Substrings](https://contest.ucup.ac/contest/1511/problem/8211) | S2 Delft | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-G · Graffiti](https://contest.ucup.ac/contest/1511/problem/8213) | S2 Delft | 树上算法、动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.5） |
| [s2-26-H · Harmonic Operations](https://contest.ucup.ac/contest/1576/problem/8512) | S2 Latin America | 字符串、数据结构 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.9） |
| [s3-0-B · Champernowne Substring](https://contest.ucup.ac/contest/1695/problem/8769) | S3 America | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.4） |
| [s3-0-I · Not Another Constructive!](https://contest.ucup.ac/contest/1695/problem/8776) | S3 America | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.18） |
| [s3-1-I · Spin & Rotate!](https://contest.ucup.ac/contest/1696/problem/8789) | S3 St. Petersburg | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.117） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-4-A · Again Make UTPC](https://contest.ucup.ac/contest/1738/problem/9113) | S3 Hongo | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.6） |
| [s3-4-D · DRD String](https://contest.ucup.ac/contest/1738/problem/9116) | S3 Hongo | 字符串、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.20） |
| [s3-4-N · Number of Abbreviations](https://contest.ucup.ac/contest/1738/problem/9126) | S3 Hongo | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.92） |
| [s3-7-J · Juliet Unifies Ones](https://contest.ucup.ac/contest/1774/problem/9229) | S3 Warsaw | 动态规划、字符串 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-A · Welcome to NPCAPC](https://contest.ucup.ac/contest/1804/problem/9435) | S3 Sumiyosi | 动态规划、多项式与线性代数、字符串 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) |
| [s3-13-G · Count Pseudo-Palindromes](https://contest.ucup.ac/contest/1812/problem/9482) | S3 Sendai | 字符串、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.36） |
| [s3-13-N · 0100 Insertion](https://contest.ucup.ac/contest/1812/problem/9489) | S3 Sendai | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.68） |
| [s3-13-O · Sub Brackets](https://contest.ucup.ac/contest/1812/problem/9490) | S3 Sendai | 图论、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.72） |
| [s3-18-G · Shrek's Song of the Swamp](https://contest.ucup.ac/contest/1849/problem/9787) | S3 Southeastern Europe | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.9） |
| [s3-21-B · Self Checkout](https://contest.ucup.ac/contest/1872/problem/9876) | S3 Ōokayama | 组合计数、字符串 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11403) |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-24-A · Acronym](https://contest.ucup.ac/contest/1890/problem/9959) | S3 Poland | 字符串、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.2） |
| [s3-24-L · Looping RPS](https://contest.ucup.ac/contest/1890/problem/9970) | S3 Poland | 字符串、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.126） |
| [s3-27-E · Equal Strings](https://contest.ucup.ac/contest/1901/problem/8615) | S3 London | 交互与信息编码、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-30-K · Vortex](https://contest.ucup.ac/contest/1917/problem/10097) | S3 Northern | 树上算法、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.5） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-33-A · AB to C](https://contest.ucup.ac/contest/1954/problem/10265) | S3 India | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.1） |
| [s3-33-G · Lexicographic Raffle](https://contest.ucup.ac/contest/1954/problem/10271) | S3 India | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.8） |
| [s3-34-E · 010-11 Shorten](https://contest.ucup.ac/contest/1965/problem/10325) | S3 Aobayama | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.15） |
| [s3-34-M · Divide Digit String](https://contest.ucup.ac/contest/1965/problem/10333) | S3 Aobayama | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.22） |
| [s3-34-N · Palindromic Path](https://contest.ucup.ac/contest/1965/problem/10334) | S3 Aobayama | 图论、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.34） |
| [s3-35-A · Suspicious Submissions](https://contest.ucup.ac/contest/1993/problem/10701) | S3 Kraków | 字符串、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-K · Bitter](https://contest.ucup.ac/contest/1993/problem/10711) | S3 Kraków | 字符串、树上算法、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.8） |
| [s3-39-H · Hidden Sequence Rotation](https://contest.ucup.ac/contest/2071/problem/10977) | S3 Tokyo | 字符串、交互与信息编码 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-C · DNA Subsequences](https://contest.ucup.ac/contest/2135/problem/12152) | S3 Potyczki | 动态规划、搜索与二分、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.2） |
| [s4-1-D · Sequence Is Not Subsequence](https://contest.ucup.ac/contest/2539/problem/14429) | S4 Korolyov | 字符串、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-2-G · Goofy Songs](https://contest.ucup.ac/contest/2551/problem/14136) | S4 Paris | 字符串、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-3-C · Roman Numerals](https://contest.ucup.ac/contest/2559/problem/14417) | S4 Polar | 数据结构、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-10-D · DNA](https://contest.ucup.ac/contest/2814/problem/16003) | S4 Wrocław | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.20） |
| [s4-10-I · Identical Fences](https://contest.ucup.ac/contest/2814/problem/16008) | S4 Wrocław | 概率期望与随机化、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.33） |
| [s4-10-L · Letters on T-shirts](https://contest.ucup.ac/contest/2814/problem/16011) | S4 Wrocław | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.11） |
| [s4-11-B · AND Reconstruction](https://contest.ucup.ac/contest/2828/problem/16116) | S4 Southeastern Europe | 位运算与状态压缩、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.2） |
| [s4-16-E · Evaluation](https://contest.ucup.ac/contest/3347/problem/17154) | S4 Warsaw | 动态规划、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.7） |
| [s4-16-I · Palindromes](https://contest.ucup.ac/contest/3347/problem/17158) | S4 Warsaw | 字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.13） |
| [s4-17-C · String Workshop](https://contest.ucup.ac/contest/3384/problem/17163) | S4 St. Petersburg | 数据结构、字符串、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.2） |
| [s4-18-A · Apparently Make UTPC](https://contest.ucup.ac/contest/3420/problem/17246) | S4 Hongō | 字符串、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15605) |
| [s4-18-F · Finite Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17251) | S4 Hongō | 字符串、数据结构 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15692) |
| [s4-18-G · Greatest Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17252) | S4 Hongō | 字符串、数据结构、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16136) |
| [s4-19-L · Layered Caesar Salad](https://contest.ucup.ac/contest/3426/problem/17271) | S4 Belarus | 构造、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-21-E · Find "rururutata"](https://contest.ucup.ac/contest/3542/problem/17423) | S4 Kamigō | 字符串、数据结构 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17002) |
| [s4-22-B · Cat Cut](https://contest.ucup.ac/contest/3575/problem/17714) | S4 Kyoto | 字符串、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.1） |
| [s4-22-L · Make Many KUPC](https://contest.ucup.ac/contest/3575/problem/17724) | S4 Kyoto | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-25-H · Halfway Hawser](https://contest.ucup.ac/contest/3773/problem/18408) | S4 Zagreb | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.31） |
| [s5-3-M · Matching Substrings](https://contest.ucup.ac/contest/4565/problem/20741) | S5 Gorkovskaya | 字符串、树上算法、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.13） |
| [s5-6-I · tatesoto decomposition](https://contest.ucup.ac/contest/4617/problem/23677) | S5 Hyakumanben | 字符串、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.14） |
| [s5-6-J · Hugest Number](https://contest.ucup.ac/contest/4617/problem/23678) | S5 Hyakumanben | 数论、字符串、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.15） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |

### 计算几何

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-C · Constellations](https://contest.ucup.ac/contest/1070/problem/5251) | S1 Slovenia | 数据结构、计算几何 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.5） |
| [s1-8-J · Mortgage](https://contest.ucup.ac/contest/1070/problem/5258) | S1 Slovenia | 数据结构、计算几何、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.12） |
| [s1-12-H · Expanded Hull](https://contest.ucup.ac/contest/1207/problem/6324) | S1 Ōokayama | 计算几何、多项式与线性代数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.5） |
| [s1-12-J · Make Convex Sequence](https://contest.ucup.ac/contest/1207/problem/6326) | S1 Ōokayama | 计算几何 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.7） |
| [s1-12-K · Count Arithmetic Progression](https://contest.ucup.ac/contest/1207/problem/6327) | S1 Ōokayama | 计算几何、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.7） |
| [s1-13-B · Random Interactive Convex Hull Bot](https://contest.ucup.ac/contest/1212/problem/6345) | S1 Iberia | 计算几何、交互与信息编码、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.1） |
| [s1-16-F · Classical Geometry Problem](https://contest.ucup.ac/contest/1223/problem/6412) | S1 Gomel | 计算几何、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-20-I · Disk Tree](https://contest.ucup.ac/contest/1259/problem/6639) | S1 India | 计算几何、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.32） |
| [s2-2-J · Transport Pluses](https://contest.ucup.ac/contest/1356/problem/7184) | S2 SPb | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.1） |
| [s2-14-C · Christmas Sky](https://contest.ucup.ac/contest/1452/problem/7934) | S2 Southeastern Europe | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.3） |
| [s2-20-D · Spacecraft](https://contest.ucup.ac/contest/1499/problem/8168) | S2 Ōokayama | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.3） |
| [s2-20-O · 2D Parentheses](https://contest.ucup.ac/contest/1499/problem/8179) | S2 Ōokayama | 计算几何、贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.18） |
| [s2-21-B · Beer Circuits](https://contest.ucup.ac/contest/1511/problem/8208) | S2 Delft | 搜索与二分、计算几何、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-C · Curly Palindromes](https://contest.ucup.ac/contest/1511/problem/8209) | S2 Delft | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.2） |
| [s2-21-H · Huge Oil Platform](https://contest.ucup.ac/contest/1511/problem/8214) | S2 Delft | 计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.6） |
| [s2-26-A · Almost Aligned](https://contest.ucup.ac/contest/1576/problem/8505) | S2 Latin America | 计算几何 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.1） |
| [s2-26-I · Insects, Mathematics, Accuracy, and Efficiency](https://contest.ucup.ac/contest/1576/problem/8513) | S2 Latin America | 计算几何 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.11） |
| [s3-0-H · MountainCraft](https://contest.ucup.ac/contest/1695/problem/8775) | S3 America | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.16） |
| [s3-0-K · Shadow Line](https://contest.ucup.ac/contest/1695/problem/8778) | S3 America | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.22） |
| [s3-0-L · Square of Triangles](https://contest.ucup.ac/contest/1695/problem/8779) | S3 America | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.25） |
| [s3-1-B · Schoolgirls](https://contest.ucup.ac/contest/1696/problem/8782) | S3 St. Petersburg | 计算几何、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.7） |
| [s3-2-I · Mercenaries](https://contest.ucup.ac/contest/1699/problem/8525) | S3 Zielona Gora | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.134） |
| [s3-4-L · Largest Triangle](https://contest.ucup.ac/contest/1738/problem/9124) | S3 Hongo | 贪心、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.82） |
| [s3-4-O · Optimal Train Operation](https://contest.ucup.ac/contest/1738/problem/9127) | S3 Hongo | 动态规划、数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.97） |
| [s3-5-H · Ancient Country](https://contest.ucup.ac/contest/1741/problem/9137) | S3 Moscow | 动态规划、计算几何 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-B · Square Locator](https://contest.ucup.ac/contest/1762/problem/9168) | S3 Osijek | 计算几何 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-6-G · Touching Grass](https://contest.ucup.ac/contest/1762/problem/9173) | S3 Osijek | 计算几何、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-H · Henry the Plumber](https://contest.ucup.ac/contest/1774/problem/9227) | S3 Warsaw | 计算几何 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-13-L · Vivid Colors](https://contest.ucup.ac/contest/1812/problem/9487) | S3 Sendai | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.58） |
| [s3-18-E · Shrooks](https://contest.ucup.ac/contest/1849/problem/9785) | S3 Southeastern Europe | 组合计数、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.6） |
| [s3-21-E · ReTravel](https://contest.ucup.ac/contest/1872/problem/9879) | S3 Ōokayama | 动态规划、计算几何 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11086) |
| [s3-21-F · Origami Warp](https://contest.ucup.ac/contest/1872/problem/9880) | S3 Ōokayama | 计算几何、数论 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11224) |
| [s3-21-H · Two Convex Sets](https://contest.ucup.ac/contest/1872/problem/9882) | S3 Ōokayama | 计算几何、动态规划 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11084) |
| [s3-24-H · High Jump](https://contest.ucup.ac/contest/1890/problem/9966) | S3 Poland | 动态规划、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.107） |
| [s3-27-D · 3D](https://contest.ucup.ac/contest/1901/problem/8614) | S3 London | 搜索与二分、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-G · Geo Sharding](https://contest.ucup.ac/contest/1901/problem/8617) | S3 London | 构造、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-27-J · Jigsaw Puzzle](https://contest.ucup.ac/contest/1901/problem/8620) | S3 London | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-30-A · Archaeology](https://contest.ucup.ac/contest/1917/problem/10087) | S3 Northern | 交互与信息编码、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-31-F · Flats](https://contest.ucup.ac/contest/1924/problem/10119) | S3 Wroclaw | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.44） |
| [s3-31-H · Hues](https://contest.ucup.ac/contest/1924/problem/10121) | S3 Wroclaw | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.61） |
| [s3-31-J · Just Mining](https://contest.ucup.ac/contest/1924/problem/10123) | S3 Wroclaw | 图论、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.81） |
| [s3-34-G · Convex Hull of Intersections](https://contest.ucup.ac/contest/1965/problem/10327) | S3 Aobayama | 计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.59） |
| [s3-35-L · Empty Triangles](https://contest.ucup.ac/contest/1993/problem/10712) | S3 Kraków | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.9） |
| [s3-39-G · Guarding Plan](https://contest.ucup.ac/contest/2071/problem/10976) | S3 Tokyo | 计算几何、动态规划、数据结构 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-G · Furniture](https://contest.ucup.ac/contest/2135/problem/12156) | S3 Potyczki | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.266） |
| [s4-0-D · Geometry Rush](https://contest.ucup.ac/contest/2041/problem/11359) | S4 America | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.17） |
| [s4-0-I · Polygon Partition](https://contest.ucup.ac/contest/2041/problem/11364) | S4 America | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.36） |
| [s4-0-L · Solar Farm](https://contest.ucup.ac/contest/2041/problem/11367) | S4 America | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.50） |
| [s4-2-E · Euclid in Manhattan](https://contest.ucup.ac/contest/2551/problem/14134) | S4 Paris | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.2） |
| [s4-2-I · Infrared](https://contest.ucup.ac/contest/2551/problem/14138) | S4 Paris | 计算几何、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-2-M · Manhattan Graph](https://contest.ucup.ac/contest/2551/problem/14142) | S4 Paris | 图论、计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.13） |
| [s4-8-D · Division with Polylines](https://contest.ucup.ac/contest/2668/problem/15447) | S4 Poland | 动态规划、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.123） |
| [s4-11-J · Triangle Hull](https://contest.ucup.ac/contest/2828/problem/16124) | S4 Southeastern Europe | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.12） |
| [s4-11-K · Connect the Points](https://contest.ucup.ac/contest/2828/problem/16125) | S4 Southeastern Europe | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.14） |
| [s4-13-L · Colorful Quadrilateral](https://contest.ucup.ac/contest/2921/problem/16237) | S4 Ōokayama | 计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.19） |
| [s4-16-A · Three Castles](https://contest.ucup.ac/contest/3347/problem/17150) | S4 Warsaw | 计算几何、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.2） |
| [s4-16-K · Multiset Variance](https://contest.ucup.ac/contest/3347/problem/17160) | S4 Warsaw | 概率期望与随机化、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.17） |
| [s4-17-J · Euler Line](https://contest.ucup.ac/contest/3384/problem/17170) | S4 St. Petersburg | 计算几何、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.8） |
| [s4-17-L · Triangles](https://contest.ucup.ac/contest/3384/problem/17172) | S4 St. Petersburg | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.12） |
| [s4-18-C · Convex Crusher](https://contest.ucup.ac/contest/3420/problem/17248) | S4 Hongō | 计算几何、位运算与状态压缩 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16125) |
| [s4-20-A · Ant and Sticks](https://contest.ucup.ac/contest/3516/problem/17406) | S4 India | 计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.1） |
| [s4-21-C · Don't be Clockwise](https://contest.ucup.ac/contest/3542/problem/17421) | S4 Kamigō | 计算几何、贪心、构造 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17020) |
| [s4-22-D · Campaign Speech](https://contest.ucup.ac/contest/3575/problem/17716) | S4 Kyoto | 计算几何、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.4） |
| [s4-22-M · Linked VERSE](https://contest.ucup.ac/contest/3575/problem/17725) | S4 Kyoto | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.10） |
| [s4-25-E · Exchange Error](https://contest.ucup.ac/contest/3773/problem/18405) | S4 Zagreb | 数据结构、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.18） |
| [s5-1-H · Hockey Hog](https://contest.ucup.ac/contest/4126/problem/20255) | S5 Nizhny Novgorod | 计算几何、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.15） |
| [s5-1-I · Incident in the Bakery](https://contest.ucup.ac/contest/4126/problem/20256) | S5 Nizhny Novgorod | 计算几何、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.16） |
| [s5-1-M · Minecraft Spiderweb](https://contest.ucup.ac/contest/4126/problem/20260) | S5 Nizhny Novgorod | 计算几何、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.24） |
| [s5-3-C · Circle Construction](https://contest.ucup.ac/contest/4565/problem/20731) | S5 Gorkovskaya | 计算几何、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |

### 贪心

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-A · Adjacent Product Sum](https://contest.ucup.ac/contest/1106/problem/5517) | S1 Ukraine | 贪心、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.1） |
| [s1-8-D · Deforestation](https://contest.ucup.ac/contest/1070/problem/5252) | S1 Slovenia | 贪心、树上算法 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.3） |
| [s1-12-E · Five Med Sum](https://contest.ucup.ac/contest/1207/problem/6321) | S1 Ōokayama | 组合计数、贪心 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-13-I · SPPPSPSS.](https://contest.ucup.ac/contest/1212/problem/6352) | S1 Iberia | 贪心、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-I · Classical Minimization Problem](https://contest.ucup.ac/contest/1223/problem/6415) | S1 Gomel | 贪心、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.4） |
| [s1-16-J · Classical Scheduling Problem](https://contest.ucup.ac/contest/1223/problem/6416) | S1 Gomel | 贪心、搜索与二分、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-B · Minimize Median](https://contest.ucup.ac/contest/1259/problem/6632) | S1 India | 搜索与二分、贪心 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.6） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-2-D · Bishops](https://contest.ucup.ac/contest/1356/problem/7178) | S2 SPb | 贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.13） |
| [s2-2-E · Fischer's Chess Guessing Game](https://contest.ucup.ac/contest/1356/problem/7179) | S2 SPb | 交互与信息编码、贪心、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.3） |
| [s2-5-A · Greedy Bipartite Matching](https://contest.ucup.ac/contest/1388/problem/6546) | S2 Northern | 图论、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.2） |
| [s2-5-B · Banshee](https://contest.ucup.ac/contest/1388/problem/6547) | S2 Northern | 搜索与二分、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.19） |
| [s2-5-H · Shared Memory Switch](https://contest.ucup.ac/contest/1388/problem/6553) | S2 Northern | 贪心、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.45） |
| [s2-6-I · Boxes](https://contest.ucup.ac/contest/1398/problem/7614) | S2 Warsaw | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-6-L · Spectacle](https://contest.ucup.ac/contest/1398/problem/7617) | S2 Warsaw | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-7-B · Bins and Balls](https://contest.ucup.ac/contest/1399/problem/7633) | S2 Two Capitals | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-G · Lake](https://contest.ucup.ac/contest/1399/problem/7638) | S2 Two Capitals | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.6） |
| [s2-7-N · Shoes](https://contest.ucup.ac/contest/1399/problem/7645) | S2 Two Capitals | 动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.9） |
| [s2-14-B · Build Permutation](https://contest.ucup.ac/contest/1452/problem/7933) | S2 Southeastern Europe | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.2） |
| [s2-14-J · Jackpot](https://contest.ucup.ac/contest/1452/problem/7941) | S2 Southeastern Europe | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.11） |
| [s2-14-K · $K$ Subsequences](https://contest.ucup.ac/contest/1452/problem/7942) | S2 Southeastern Europe | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.12） |
| [s2-16-E · Four Plus Four](https://contest.ucup.ac/contest/1465/problem/4828) | S2 Run Twice | 贪心、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.47） |
| [s2-16-H · Eager Sorting](https://contest.ucup.ac/contest/1465/problem/4831) | S2 Run Twice | 交互与信息编码、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.92） |
| [s2-19-G · LCA Counting](https://contest.ucup.ac/contest/1487/problem/8134) | S2 Estonia | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.11） |
| [s2-19-J · 'Ello, and What Are You After, Then?](https://contest.ucup.ac/contest/1487/problem/8137) | S2 Estonia | 概率期望与随机化、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.16） |
| [s2-20-O · 2D Parentheses](https://contest.ucup.ac/contest/1499/problem/8179) | S2 Ōokayama | 计算几何、贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.18） |
| [s2-26-J · Joys of Trading](https://contest.ucup.ac/contest/1576/problem/8514) | S2 Latin America | 贪心 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.13） |
| [s3-0-E · House Deconstruction](https://contest.ucup.ac/contest/1695/problem/8772) | S3 America | 贪心、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.10） |
| [s3-1-G · Unusual Case](https://contest.ucup.ac/contest/1696/problem/8787) | S3 St. Petersburg | 概率期望与随机化、图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.102） |
| [s3-1-I · Spin & Rotate!](https://contest.ucup.ac/contest/1696/problem/8789) | S3 St. Petersburg | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.117） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-2-H · Weather Forecast](https://contest.ucup.ac/contest/1699/problem/8524) | S3 Zielona Gora | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.123） |
| [s3-4-A · Again Make UTPC](https://contest.ucup.ac/contest/1738/problem/9113) | S3 Hongo | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.6） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-J · Japanese Gift Money](https://contest.ucup.ac/contest/1738/problem/9122) | S3 Hongo | 数论、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.64） |
| [s3-4-L · Largest Triangle](https://contest.ucup.ac/contest/1738/problem/9124) | S3 Hongo | 贪心、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.82） |
| [s3-5-A · Counting Permutations](https://contest.ucup.ac/contest/1741/problem/9130) | S3 Moscow | 组合计数、贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-C · Painting Fences](https://contest.ucup.ac/contest/1741/problem/9132) | S3 Moscow | 数据结构、贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-E · Building a Fence](https://contest.ucup.ac/contest/1741/problem/9134) | S3 Moscow | 贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-M · Uniting Amoebas](https://contest.ucup.ac/contest/1741/problem/9142) | S3 Moscow | 贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-7-B · Missing Boundaries](https://contest.ucup.ac/contest/1774/problem/9221) | S3 Warsaw | 贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-D · Data Determination](https://contest.ucup.ac/contest/1774/problem/9223) | S3 Warsaw | 贪心、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-M · Mathematics Championships](https://contest.ucup.ac/contest/1774/problem/9232) | S3 Warsaw | 贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-C · Solve with Friends](https://contest.ucup.ac/contest/1804/problem/9437) | S3 Sumiyosi | 贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10201) |
| [s3-11-M · Admired Person](https://contest.ucup.ac/contest/1804/problem/9447) | S3 Sumiyosi | 动态规划、贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10177) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-H · Maximize Array](https://contest.ucup.ac/contest/1812/problem/9483) | S3 Sendai | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.41） |
| [s3-13-L · Vivid Colors](https://contest.ucup.ac/contest/1812/problem/9487) | S3 Sendai | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.58） |
| [s3-18-B · NonZero PrefSuf Sums](https://contest.ucup.ac/contest/1849/problem/9782) | S3 Southeastern Europe | 贪心、数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.2） |
| [s3-18-D · Donkey and Puss in Boots](https://contest.ucup.ac/contest/1849/problem/9784) | S3 Southeastern Europe | 博弈论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.5） |
| [s3-18-F · Magical Bags](https://contest.ucup.ac/contest/1849/problem/9786) | S3 Southeastern Europe | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.8） |
| [s3-18-H · Shreckless](https://contest.ucup.ac/contest/1849/problem/9788) | S3 Southeastern Europe | 贪心、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.10） |
| [s3-18-J · Make Swamp Great Again](https://contest.ucup.ac/contest/1849/problem/9790) | S3 Southeastern Europe | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.13） |
| [s3-18-L · Ogre Sort](https://contest.ucup.ac/contest/1849/problem/9792) | S3 Southeastern Europe | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.15） |
| [s3-21-A · Don't Detect Cycle](https://contest.ucup.ac/contest/1872/problem/9875) | S3 Ōokayama | 图论、贪心 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11085) |
| [s3-24-C · Cows](https://contest.ucup.ac/contest/1890/problem/9961) | S3 Poland | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.135） |
| [s3-24-I · Imbalanced Teams](https://contest.ucup.ac/contest/1890/problem/9967) | S3 Poland | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.19） |
| [s3-27-B · The Best Wife](https://contest.ucup.ac/contest/1901/problem/8612) | S3 London | 数据结构、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-J · Jigsaw Puzzle](https://contest.ucup.ac/contest/1901/problem/8620) | S3 London | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-27-M · Meta](https://contest.ucup.ac/contest/1901/problem/8623) | S3 London | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.4） |
| [s3-30-D · Preparation for the Exam](https://contest.ucup.ac/contest/1917/problem/10090) | S3 Northern | 贪心、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-31-C · CERC Plaques](https://contest.ucup.ac/contest/1924/problem/10116) | S3 Wroclaw | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.11） |
| [s3-31-G · Groceries](https://contest.ucup.ac/contest/1924/problem/10120) | S3 Wroclaw | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.69） |
| [s3-31-I · Illuminati](https://contest.ucup.ac/contest/1924/problem/10122) | S3 Wroclaw | 图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.29） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-33-A · AB to C](https://contest.ucup.ac/contest/1954/problem/10265) | S3 India | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.1） |
| [s3-33-B · Bin Packing](https://contest.ucup.ac/contest/1954/problem/10266) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.2） |
| [s3-33-F · Greedy Prices](https://contest.ucup.ac/contest/1954/problem/10270) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.7） |
| [s3-33-M · Ticket Revenue Maximization](https://contest.ucup.ac/contest/1954/problem/10277) | S3 India | 贪心、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.14） |
| [s3-34-D · Swap Counter](https://contest.ucup.ac/contest/1965/problem/10324) | S3 Aobayama | 构造、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.43） |
| [s3-34-E · 010-11 Shorten](https://contest.ucup.ac/contest/1965/problem/10325) | S3 Aobayama | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.15） |
| [s3-34-J · Median Operations](https://contest.ucup.ac/contest/1965/problem/10330) | S3 Aobayama | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.68） |
| [s3-34-K · Shuffle and Max Bracket Score](https://contest.ucup.ac/contest/1965/problem/10331) | S3 Aobayama | 概率期望与随机化、贪心、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.72） |
| [s3-39-C · Card Deck](https://contest.ucup.ac/contest/2071/problem/10972) | S3 Tokyo | 贪心、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-J · Journey through the Fractal](https://contest.ucup.ac/contest/2071/problem/10979) | S3 Tokyo | 贪心、组合计数 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-Q · Quadratic Pieces](https://contest.ucup.ac/contest/2071/problem/10986) | S3 Tokyo | 贪心 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-A · AGI](https://contest.ucup.ac/contest/2135/problem/12150) | S3 Potyczki | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.244） |
| [s3-40-I · Santa Claus](https://contest.ucup.ac/contest/2135/problem/12158) | S3 Potyczki | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.281） |
| [s4-0-D · Geometry Rush](https://contest.ucup.ac/contest/2041/problem/11359) | S4 America | 计算几何、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.17） |
| [s4-0-H · Ornaments on a Tree](https://contest.ucup.ac/contest/2041/problem/11363) | S4 America | 树上算法、动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.32） |
| [s4-0-K · SLA Tomography](https://contest.ucup.ac/contest/2041/problem/11366) | S4 America | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.48） |
| [s4-1-H · Misread Problem](https://contest.ucup.ac/contest/2539/problem/14433) | S4 Korolyov | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-2-H · Heure de Rush](https://contest.ucup.ac/contest/2551/problem/14137) | S4 Paris | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-2-K · $k$ Operations](https://contest.ucup.ac/contest/2551/problem/14140) | S4 Paris | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-3-I · Two Permutations](https://contest.ucup.ac/contest/2559/problem/14423) | S4 Polar | 构造、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-B · Beats](https://contest.ucup.ac/contest/2668/problem/15445) | S4 Poland | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.51） |
| [s4-8-J · Jury of AMPPZ](https://contest.ucup.ac/contest/2668/problem/15453) | S4 Poland | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.18） |
| [s4-8-K · Kids' Blocks](https://contest.ucup.ac/contest/2668/problem/15454) | S4 Poland | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.12） |
| [s4-8-M · Market](https://contest.ucup.ac/contest/2668/problem/15456) | S4 Poland | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.145） |
| [s4-10-D · DNA](https://contest.ucup.ac/contest/2814/problem/16003) | S4 Wrocław | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.20） |
| [s4-10-E · Easy Tetris](https://contest.ucup.ac/contest/2814/problem/16004) | S4 Wrocław | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.126） |
| [s4-10-H · Hiking](https://contest.ucup.ac/contest/2814/problem/16007) | S4 Wrocław | 贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.38） |
| [s4-10-I · Identical Fences](https://contest.ucup.ac/contest/2814/problem/16008) | S4 Wrocław | 概率期望与随机化、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.33） |
| [s4-10-J · Joyful Guided Tour](https://contest.ucup.ac/contest/2814/problem/16009) | S4 Wrocław | 图论、贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.93） |
| [s4-11-G · Intervals from Triplets](https://contest.ucup.ac/contest/2828/problem/16121) | S4 Southeastern Europe | 动态规划、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.7） |
| [s4-13-B · Increasing Swaps](https://contest.ucup.ac/contest/2921/problem/16227) | S4 Ōokayama | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.1） |
| [s4-16-D · Deque Sort](https://contest.ucup.ac/contest/3347/problem/17153) | S4 Warsaw | 数据结构、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.6） |
| [s4-18-J · Jelly](https://contest.ucup.ac/contest/3420/problem/17255) | S4 Hongō | 贪心 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16128) |
| [s4-18-K · Keep or Gamble](https://contest.ucup.ac/contest/3420/problem/17256) | S4 Hongō | 概率期望与随机化、贪心 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15851) |
| [s4-18-M · Max Conference](https://contest.ucup.ac/contest/3420/problem/17258) | S4 Hongō | 贪心、组合计数 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15903) |
| [s4-19-D · Detecting the Missing Ship](https://contest.ucup.ac/contest/3426/problem/17263) | S4 Belarus | 交互与信息编码、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-21-B · Birds-of-Paradise' Card Game](https://contest.ucup.ac/contest/3542/problem/17420) | S4 Kamigō | 贪心、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17017) |
| [s4-21-C · Don't be Clockwise](https://contest.ucup.ac/contest/3542/problem/17421) | S4 Kamigō | 计算几何、贪心、构造 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17020) |
| [s4-21-D · Except Ai](https://contest.ucup.ac/contest/3542/problem/17422) | S4 Kamigō | 贪心 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17026) |
| [s4-21-H · OR Preference](https://contest.ucup.ac/contest/3542/problem/17426) | S4 Kamigō | 位运算与状态压缩、动态规划、贪心 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) |
| [s4-22-C · Partition AND/OR Aggregation](https://contest.ucup.ac/contest/3575/problem/17715) | S4 Kyoto | 位运算与状态压缩、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.2） |
| [s4-22-L · Make Many KUPC](https://contest.ucup.ac/contest/3575/problem/17724) | S4 Kyoto | 贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-25-A · Arrow Array](https://contest.ucup.ac/contest/3773/problem/18401) | S4 Zagreb | 贪心、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.2） |
| [s4-25-H · Halfway Hawser](https://contest.ucup.ac/contest/3773/problem/18408) | S4 Zagreb | 字符串、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.31） |
| [s4-25-K · Kempt Kale](https://contest.ucup.ac/contest/3773/problem/18411) | S4 Zagreb | 贪心、数据结构、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.42） |
| [s4-Extra-3-B · Word Generator](https://contest.ucup.ac/contest/2757/problem/15518) | S4 Osijek | 图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-F · Binary Permutation](https://contest.ucup.ac/contest/2757/problem/15522) | S4 Osijek | 组合计数、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-G · Amoeba Tree](https://contest.ucup.ac/contest/2757/problem/15523) | S4 Osijek | 树上算法、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s5-1-D · Digesting](https://contest.ucup.ac/contest/4126/problem/20251) | S5 Nizhny Novgorod | 数论、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.8） |
| [s5-1-E · Easter Eggs](https://contest.ucup.ac/contest/4126/problem/20252) | S5 Nizhny Novgorod | 概率期望与随机化、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.10） |
| [s5-1-J · Jaded Juice](https://contest.ucup.ac/contest/4126/problem/20257) | S5 Nizhny Novgorod | 贪心、数论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.19） |
| [s5-3-D · Dynamic Adjustment](https://contest.ucup.ac/contest/4565/problem/20732) | S5 Gorkovskaya | 数据结构、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |
| [s5-3-K · Keep Colors Apart](https://contest.ucup.ac/contest/4565/problem/20739) | S5 Gorkovskaya | 贪心、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.11） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |

### 搜索与二分

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-E · Denormalization](https://contest.ucup.ac/contest/1070/problem/5253) | S1 Slovenia | 数值计算、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.4） |
| [s1-8-J · Mortgage](https://contest.ucup.ac/contest/1070/problem/5258) | S1 Slovenia | 数据结构、计算几何、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.12） |
| [s1-12-C · Parallel Processing (Easy)](https://contest.ucup.ac/contest/1207/problem/6319) | S1 Ōokayama | 搜索与二分、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-13-E · Egor Has a Problem](https://contest.ucup.ac/contest/1212/problem/6348) | S1 Iberia | 搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-13-H · Exact Subsequences](https://contest.ucup.ac/contest/1212/problem/6351) | S1 Iberia | 数论、搜索与二分、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-13-I · SPPPSPSS.](https://contest.ucup.ac/contest/1212/problem/6352) | S1 Iberia | 贪心、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-A · Classical A+B Problem](https://contest.ucup.ac/contest/1223/problem/6407) | S1 Gomel | 搜索与二分、数论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.1） |
| [s1-16-J · Classical Scheduling Problem](https://contest.ucup.ac/contest/1223/problem/6416) | S1 Gomel | 贪心、搜索与二分、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-B · Minimize Median](https://contest.ucup.ac/contest/1259/problem/6632) | S1 India | 搜索与二分、贪心 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.6） |
| [s1-20-H · Treelection](https://contest.ucup.ac/contest/1259/problem/6638) | S1 India | 树上算法、动态规划、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.28） |
| [s2-2-E · Fischer's Chess Guessing Game](https://contest.ucup.ac/contest/1356/problem/7179) | S2 SPb | 交互与信息编码、贪心、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.3） |
| [s2-2-F · Forward-Capturing Pawns](https://contest.ucup.ac/contest/1356/problem/7180) | S2 SPb | 博弈论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.4） |
| [s2-2-J · Transport Pluses](https://contest.ucup.ac/contest/1356/problem/7184) | S2 SPb | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.1） |
| [s2-5-B · Banshee](https://contest.ucup.ac/contest/1388/problem/6547) | S2 Northern | 搜索与二分、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.19） |
| [s2-6-H · Inverse Problem](https://contest.ucup.ac/contest/1398/problem/7613) | S2 Warsaw | 搜索与二分、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-7-D · Fairy Chess](https://contest.ucup.ac/contest/1399/problem/7635) | S2 Two Capitals | 博弈论、位运算与状态压缩、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.2） |
| [s2-7-F · Exactly Three Neighbors](https://contest.ucup.ac/contest/1399/problem/7637) | S2 Two Capitals | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.3） |
| [s2-7-H · Forbidden Set](https://contest.ucup.ac/contest/1399/problem/7639) | S2 Two Capitals | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-14-C · Christmas Sky](https://contest.ucup.ac/contest/1452/problem/7934) | S2 Southeastern Europe | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.3） |
| [s2-14-M · Max Minus Min](https://contest.ucup.ac/contest/1452/problem/7944) | S2 Southeastern Europe | 搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.14） |
| [s2-16-I · Telepathy](https://contest.ucup.ac/contest/1465/problem/4832) | S2 Run Twice | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.113） |
| [s2-16-J · Tetra-puzzle](https://contest.ucup.ac/contest/1465/problem/4833) | S2 Run Twice | 搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.136） |
| [s2-19-J · 'Ello, and What Are You After, Then?](https://contest.ucup.ac/contest/1487/problem/8137) | S2 Estonia | 概率期望与随机化、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.16） |
| [s2-20-C · Yet Another Simple Math Problem](https://contest.ucup.ac/contest/1499/problem/8167) | S2 Ōokayama | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.2） |
| [s2-21-B · Beer Circuits](https://contest.ucup.ac/contest/1511/problem/8208) | S2 Delft | 搜索与二分、计算几何、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-I · Isomorphic Delight](https://contest.ucup.ac/contest/1511/problem/8215) | S2 Delft | 树上算法、搜索与二分、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.7） |
| [s2-26-B · Beating the Record](https://contest.ucup.ac/contest/1576/problem/8506) | S2 Latin America | 搜索与二分、概率期望与随机化 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.1） |
| [s3-0-B · Champernowne Substring](https://contest.ucup.ac/contest/1695/problem/8769) | S3 America | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.4） |
| [s3-0-J · Passport Stamps](https://contest.ucup.ac/contest/1695/problem/8777) | S3 America | 搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.20） |
| [s3-0-L · Square of Triangles](https://contest.ucup.ac/contest/1695/problem/8779) | S3 America | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.25） |
| [s3-1-D · Dwarfs' Bedtime](https://contest.ucup.ac/contest/1696/problem/8784) | S3 St. Petersburg | 交互与信息编码、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.57） |
| [s3-1-F · The Whole World](https://contest.ucup.ac/contest/1696/problem/8786) | S3 St. Petersburg | 多项式与线性代数、数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.85） |
| [s3-1-J · First Billion](https://contest.ucup.ac/contest/1696/problem/8790) | S3 St. Petersburg | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.177） |
| [s3-1-O · Mysterious Sequence](https://contest.ucup.ac/contest/1696/problem/8795) | S3 St. Petersburg | 搜索与二分、多项式与线性代数、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.231） |
| [s3-2-H · Weather Forecast](https://contest.ucup.ac/contest/1699/problem/8524) | S3 Zielona Gora | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.123） |
| [s3-4-K · Kth Sum](https://contest.ucup.ac/contest/1738/problem/9123) | S3 Hongo | 搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.76） |
| [s3-4-Q · Quotient Sum](https://contest.ucup.ac/contest/1738/problem/9129) | S3 Hongo | 动态规划、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.109） |
| [s3-5-J · Prefix Divisible by Suffix](https://contest.ucup.ac/contest/1741/problem/9139) | S3 Moscow | 数论、组合计数、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-L · Array Spread](https://contest.ucup.ac/contest/1741/problem/9141) | S3 Moscow | 图论、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-7-D · Data Determination](https://contest.ucup.ac/contest/1774/problem/9223) | S3 Warsaw | 贪心、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-L · Random Numbers](https://contest.ucup.ac/contest/1774/problem/9231) | S3 Warsaw | 概率期望与随机化、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-13-C · Shift Puzzle](https://contest.ucup.ac/contest/1812/problem/9478) | S3 Sendai | 搜索与二分、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.18） |
| [s3-18-M · Enchanted Lawns Quest](https://contest.ucup.ac/contest/1849/problem/9793) | S3 Southeastern Europe | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.16） |
| [s3-21-I · Near Pair](https://contest.ucup.ac/contest/1872/problem/9883) | S3 Ōokayama | 交互与信息编码、搜索与二分 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11470) |
| [s3-24-C · Cows](https://contest.ucup.ac/contest/1890/problem/9961) | S3 Poland | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.135） |
| [s3-27-D · 3D](https://contest.ucup.ac/contest/1901/problem/8614) | S3 London | 搜索与二分、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-K · Knapsack](https://contest.ucup.ac/contest/1901/problem/8621) | S3 London | 搜索与二分、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-27-L · London Underground](https://contest.ucup.ac/contest/1901/problem/8622) | S3 London | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-31-D · Divisors](https://contest.ucup.ac/contest/1924/problem/10117) | S3 Wroclaw | 数论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.15） |
| [s3-31-G · Groceries](https://contest.ucup.ac/contest/1924/problem/10120) | S3 Wroclaw | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.69） |
| [s3-31-K · King's Festival](https://contest.ucup.ac/contest/1924/problem/10124) | S3 Wroclaw | 搜索与二分、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.35） |
| [s3-33-C · Construct uwu](https://contest.ucup.ac/contest/1954/problem/10267) | S3 India | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.3） |
| [s3-34-M · Divide Digit String](https://contest.ucup.ac/contest/1965/problem/10333) | S3 Aobayama | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.22） |
| [s3-35-F · Red-Blue MST](https://contest.ucup.ac/contest/1993/problem/10706) | S3 Kraków | 图论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.4） |
| [s3-35-L · Empty Triangles](https://contest.ucup.ac/contest/1993/problem/10712) | S3 Kraków | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.9） |
| [s3-40-C · DNA Subsequences](https://contest.ucup.ac/contest/2135/problem/12152) | S3 Potyczki | 动态规划、搜索与二分、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.2） |
| [s3-40-M · Clubs](https://contest.ucup.ac/contest/2135/problem/12162) | S3 Potyczki | 博弈论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.368） |
| [s4-0-C · Entrapment](https://contest.ucup.ac/contest/2041/problem/11358) | S4 America | 博弈论、搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.16） |
| [s4-0-L · Solar Farm](https://contest.ucup.ac/contest/2041/problem/11367) | S4 America | 计算几何、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.50） |
| [s4-1-C · Staple Stable](https://contest.ucup.ac/contest/2539/problem/14428) | S4 Korolyov | 搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-J · Yet Another Constructive Problem](https://contest.ucup.ac/contest/2539/problem/14435) | S4 Korolyov | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.4） |
| [s4-2-J · JamBrains](https://contest.ucup.ac/contest/2551/problem/14139) | S4 Paris | 数据结构、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.5） |
| [s4-3-J · One Permutation](https://contest.ucup.ac/contest/2559/problem/14424) | S4 Polar | 动态规划、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-I · ICPC Isolation](https://contest.ucup.ac/contest/2668/problem/15452) | S4 Poland | 构造、搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.7） |
| [s4-8-J · Jury of AMPPZ](https://contest.ucup.ac/contest/2668/problem/15453) | S4 Poland | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.18） |
| [s4-10-E · Easy Tetris](https://contest.ucup.ac/contest/2814/problem/16004) | S4 Wrocław | 搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.126） |
| [s4-10-L · Letters on T-shirts](https://contest.ucup.ac/contest/2814/problem/16011) | S4 Wrocław | 字符串、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.11） |
| [s4-16-B · Bitwise Beach](https://contest.ucup.ac/contest/3347/problem/17151) | S4 Warsaw | 位运算与状态压缩、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.4） |
| [s4-16-H · House](https://contest.ucup.ac/contest/3347/problem/17157) | S4 Warsaw | 搜索与二分、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.11） |
| [s4-17-B · Missing Number](https://contest.ucup.ac/contest/3384/problem/17162) | S4 St. Petersburg | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.1） |
| [s4-18-A · Apparently Make UTPC](https://contest.ucup.ac/contest/3420/problem/17246) | S4 Hongō | 字符串、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15605) |
| [s4-18-G · Greatest Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17252) | S4 Hongō | 字符串、数据结构、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16136) |
| [s4-18-L · Linear Floor](https://contest.ucup.ac/contest/3420/problem/17257) | S4 Hongō | 数论、搜索与二分 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15885) |
| [s4-18-N · Numerical Error](https://contest.ucup.ac/contest/3420/problem/17259) | S4 Hongō | 组合计数、搜索与二分、数值计算 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15904) |
| [s4-21-L · Unique Sheet](https://contest.ucup.ac/contest/3542/problem/17430) | S4 Kamigō | 搜索与二分 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18124) |
| [s4-22-C · Partition AND/OR Aggregation](https://contest.ucup.ac/contest/3575/problem/17715) | S4 Kyoto | 位运算与状态压缩、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.2） |
| [s4-25-M · Maximum Mex](https://contest.ucup.ac/contest/3773/problem/18413) | S4 Zagreb | 树上算法、搜索与二分、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.49） |
| [s4-Extra-3-C · Glitch](https://contest.ucup.ac/contest/2757/problem/15519) | S4 Osijek | 搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s5-6-L · Consecutive Pairs](https://contest.ucup.ac/contest/4617/problem/23680) | S5 Hyakumanben | 交互与信息编码、搜索与二分、图论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.23） |

### 博弈论

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-B · Combination Locks](https://contest.ucup.ac/contest/1070/problem/5250) | S1 Slovenia | 博弈论、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.8） |
| [s1-12-O · Jewel Game](https://contest.ucup.ac/contest/1207/problem/6331) | S1 Ōokayama | 博弈论、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-20-L · (1, 2) Nim](https://contest.ucup.ac/contest/1259/problem/6642) | S1 India | 博弈论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.41） |
| [s2-2-F · Forward-Capturing Pawns](https://contest.ucup.ac/contest/1356/problem/7180) | S2 SPb | 博弈论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.4） |
| [s2-6-A · Digital Nim](https://contest.ucup.ac/contest/1398/problem/7606) | S2 Warsaw | 博弈论、动态规划、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-7-D · Fairy Chess](https://contest.ucup.ac/contest/1399/problem/7635) | S2 Two Capitals | 博弈论、位运算与状态压缩、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.2） |
| [s2-7-E · Fair Elections](https://contest.ucup.ac/contest/1399/problem/7636) | S2 Two Capitals | 博弈论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.3） |
| [s2-14-D · Distinct Game](https://contest.ucup.ac/contest/1452/problem/7935) | S2 Southeastern Europe | 博弈论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.4） |
| [s2-26-C · Clever Cell Choices](https://contest.ucup.ac/contest/1576/problem/8507) | S2 Latin America | 图论、博弈论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.4） |
| [s2-26-D · DiviDuelo](https://contest.ucup.ac/contest/1576/problem/8508) | S2 Latin America | 博弈论、数论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.5） |
| [s3-7-G · Game of Geniuses](https://contest.ucup.ac/contest/1774/problem/9226) | S3 Warsaw | 博弈论 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-13-F · Min Nim](https://contest.ucup.ac/contest/1812/problem/9481) | S3 Sendai | 博弈论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.33） |
| [s3-18-D · Donkey and Puss in Boots](https://contest.ucup.ac/contest/1849/problem/9784) | S3 Southeastern Europe | 博弈论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.5） |
| [s3-30-B · Glass Stepping Stones](https://contest.ucup.ac/contest/1917/problem/10088) | S3 Northern | 博弈论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-40-M · Clubs](https://contest.ucup.ac/contest/2135/problem/12162) | S3 Potyczki | 博弈论、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.368） |
| [s4-0-C · Entrapment](https://contest.ucup.ac/contest/2041/problem/11358) | S4 America | 博弈论、搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.16） |
| [s4-3-K · Game on Board](https://contest.ucup.ac/contest/2559/problem/14425) | S4 Polar | 博弈论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.6） |
| [s4-11-A · Sum Game](https://contest.ucup.ac/contest/2828/problem/16115) | S4 Southeastern Europe | 博弈论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.1） |
| [s4-11-L · Neo-Nim](https://contest.ucup.ac/contest/2828/problem/16126) | S4 Southeastern Europe | 博弈论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.15） |
| [s4-20-L · Alice and Bob](https://contest.ucup.ac/contest/3516/problem/17417) | S4 India | 树上算法、博弈论、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.19） |
| [s5-3-G · Game](https://contest.ucup.ac/contest/4565/problem/20735) | S5 Gorkovskaya | 博弈论、位运算与状态压缩 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.6） |
| [s5-6-C · Moving Silver](https://contest.ucup.ac/contest/4617/problem/23671) | S5 Hyakumanben | 博弈论、动态规划 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.6） |

### 概率期望与随机化

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-7-C · Testing Subjects Usually Die](https://contest.ucup.ac/contest/1129/problem/5740) | S1 Zaporizhzhia | 概率期望与随机化、数值计算 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.4） |
| [s1-7-I · DAG Generation](https://contest.ucup.ac/contest/1129/problem/5746) | S1 Zaporizhzhia | 概率期望与随机化、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.14） |
| [s1-7-J · Persian Casino](https://contest.ucup.ac/contest/1129/problem/5747) | S1 Zaporizhzhia | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.15） |
| [s1-8-G · Greedy Drawers](https://contest.ucup.ac/contest/1070/problem/5255) | S1 Slovenia | 构造、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.6） |
| [s1-12-F · Forestry](https://contest.ucup.ac/contest/1207/problem/6322) | S1 Ōokayama | 树上算法、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-13-B · Random Interactive Convex Hull Bot](https://contest.ucup.ac/contest/1212/problem/6345) | S1 Iberia | 计算几何、交互与信息编码、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.1） |
| [s1-16-K · Classical Summation Problem](https://contest.ucup.ac/contest/1223/problem/6417) | S1 Gomel | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s2-5-I · Endless Road](https://contest.ucup.ac/contest/1388/problem/6554) | S2 Northern | 概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.21） |
| [s2-6-G · Matrix Inverse](https://contest.ucup.ac/contest/1398/problem/7612) | S2 Warsaw | 多项式与线性代数、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.3） |
| [s2-16-C · Find the Parts](https://contest.ucup.ac/contest/1465/problem/4826) | S2 Run Twice | 构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.27） |
| [s2-16-D · Message Made of Noise](https://contest.ucup.ac/contest/1465/problem/4827) | S2 Run Twice | 构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.35） |
| [s2-16-F · Mark on a Graph](https://contest.ucup.ac/contest/1465/problem/4829) | S2 Run Twice | 图论、构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.65） |
| [s2-16-G · Transfer of Duty](https://contest.ucup.ac/contest/1465/problem/4830) | S2 Run Twice | 位运算与状态压缩、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.80） |
| [s2-16-I · Telepathy](https://contest.ucup.ac/contest/1465/problem/4832) | S2 Run Twice | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.113） |
| [s2-18-F · Fortune Wheel](https://contest.ucup.ac/contest/1475/problem/8008) | S2 Dolgoprudny | 概率期望与随机化、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.4） |
| [s2-19-J · 'Ello, and What Are You After, Then?](https://contest.ucup.ac/contest/1487/problem/8137) | S2 Estonia | 概率期望与随机化、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.16） |
| [s2-20-G · Cola](https://contest.ucup.ac/contest/1499/problem/8171) | S2 Ōokayama | 概率期望与随机化、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.8） |
| [s2-20-M · Sum is Integer](https://contest.ucup.ac/contest/1499/problem/8177) | S2 Ōokayama | 数论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.16） |
| [s2-26-B · Beating the Record](https://contest.ucup.ac/contest/1576/problem/8506) | S2 Latin America | 搜索与二分、概率期望与随机化 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.1） |
| [s2-26-G · Greek Casino](https://contest.ucup.ac/contest/1576/problem/8511) | S2 Latin America | 概率期望与随机化、动态规划、数论 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.8） |
| [s3-0-G · Manhattan Walk](https://contest.ucup.ac/contest/1695/problem/8774) | S3 America | 概率期望与随机化、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.14） |
| [s3-1-G · Unusual Case](https://contest.ucup.ac/contest/1696/problem/8787) | S3 St. Petersburg | 概率期望与随机化、图论、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.102） |
| [s3-1-J · First Billion](https://contest.ucup.ac/contest/1696/problem/8790) | S3 St. Petersburg | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.177） |
| [s3-2-J · Polygon II](https://contest.ucup.ac/contest/1699/problem/8526) | S3 Zielona Gora | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.160） |
| [s3-2-K · Power Divisions](https://contest.ucup.ac/contest/1699/problem/8527) | S3 Zielona Gora | 动态规划、位运算与状态压缩、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.175） |
| [s3-2-L · Chords](https://contest.ucup.ac/contest/1699/problem/8528) | S3 Zielona Gora | 动态规划、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.212） |
| [s3-6-A · Coprime Array](https://contest.ucup.ac/contest/1762/problem/9167) | S3 Osijek | 数论、构造、概率期望与随机化 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-F · Fibonacci Fusion](https://contest.ucup.ac/contest/1774/problem/9225) | S3 Warsaw | 数论、概率期望与随机化、数值计算 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-L · Random Numbers](https://contest.ucup.ac/contest/1774/problem/9231) | S3 Warsaw | 概率期望与随机化、搜索与二分 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-H · Music Game](https://contest.ucup.ac/contest/1804/problem/9442) | S3 Sumiyosi | 概率期望与随机化 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10268) |
| [s3-13-G · Count Pseudo-Palindromes](https://contest.ucup.ac/contest/1812/problem/9482) | S3 Sendai | 字符串、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.36） |
| [s3-13-K · Random Mex](https://contest.ucup.ac/contest/1812/problem/9486) | S3 Sendai | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.53） |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-24-H · High Jump](https://contest.ucup.ac/contest/1890/problem/9966) | S3 Poland | 动态规划、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.107） |
| [s3-24-L · Looping RPS](https://contest.ucup.ac/contest/1890/problem/9970) | S3 Poland | 字符串、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.126） |
| [s3-27-C · Cardinality](https://contest.ucup.ac/contest/1901/problem/8613) | S3 London | 概率期望与随机化、位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-D · 3D](https://contest.ucup.ac/contest/1901/problem/8614) | S3 London | 搜索与二分、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-E · Equal Strings](https://contest.ucup.ac/contest/1901/problem/8615) | S3 London | 交互与信息编码、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-H · Have You Seen This Subarray?](https://contest.ucup.ac/contest/1901/problem/8618) | S3 London | 数据结构、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-27-I · Interactive Casino](https://contest.ucup.ac/contest/1901/problem/8619) | S3 London | 概率期望与随机化、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-27-K · Knapsack](https://contest.ucup.ac/contest/1901/problem/8621) | S3 London | 搜索与二分、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-27-L · London Underground](https://contest.ucup.ac/contest/1901/problem/8622) | S3 London | 搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-30-A · Archaeology](https://contest.ucup.ac/contest/1917/problem/10087) | S3 Northern | 交互与信息编码、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-30-D · Preparation for the Exam](https://contest.ucup.ac/contest/1917/problem/10090) | S3 Northern | 贪心、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-30-F · Interactive Primality](https://contest.ucup.ac/contest/1917/problem/10092) | S3 Northern | 交互与信息编码、数论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.3） |
| [s3-30-K · Vortex](https://contest.ucup.ac/contest/1917/problem/10097) | S3 Northern | 树上算法、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.5） |
| [s3-32-I · Unhappy Team](https://contest.ucup.ac/contest/1939/problem/10222) | S3 Dhaka | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.5） |
| [s3-33-E · Easy Counting Problem](https://contest.ucup.ac/contest/1954/problem/10269) | S3 India | 概率期望与随机化、动态规划、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.5） |
| [s3-34-K · Shuffle and Max Bracket Score](https://contest.ucup.ac/contest/1965/problem/10331) | S3 Aobayama | 概率期望与随机化、贪心、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.72） |
| [s3-35-D · Money in the Hat](https://contest.ucup.ac/contest/1993/problem/10704) | S3 Kraków | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.3） |
| [s3-35-E · Gambling](https://contest.ucup.ac/contest/1993/problem/10705) | S3 Kraków | 概率期望与随机化、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.3） |
| [s3-35-I · Random Remainders](https://contest.ucup.ac/contest/1993/problem/10709) | S3 Kraków | 数论、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-35-K · Bitter](https://contest.ucup.ac/contest/1993/problem/10711) | S3 Kraków | 字符串、树上算法、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.8） |
| [s3-39-A · Array Similarity](https://contest.ucup.ac/contest/2071/problem/10970) | S3 Tokyo | 数据结构、概率期望与随机化 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-H · Merge Sort](https://contest.ucup.ac/contest/2135/problem/12157) | S3 Potyczki | 组合计数、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.138） |
| [s4-0-J · Popping Balloons](https://contest.ucup.ac/contest/2041/problem/11365) | S4 America | 概率期望与随机化、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.40） |
| [s4-1-G · Cyclic Topsort](https://contest.ucup.ac/contest/2539/problem/14432) | S4 Korolyov | 概率期望与随机化、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-3-F · This Time I Will Be Lucky](https://contest.ucup.ac/contest/2559/problem/14420) | S4 Polar | 概率期望与随机化、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-G · Far Away](https://contest.ucup.ac/contest/2559/problem/14421) | S4 Polar | 图论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-8-G · Game of Pipes](https://contest.ucup.ac/contest/2668/problem/15450) | S4 Poland | 交互与信息编码、图论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.136） |
| [s4-8-I · ICPC Isolation](https://contest.ucup.ac/contest/2668/problem/15452) | S4 Poland | 构造、搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.7） |
| [s4-10-A · Automatized Mineral Classification](https://contest.ucup.ac/contest/2814/problem/16000) | S4 Wrocław | 交互与信息编码、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.45） |
| [s4-10-I · Identical Fences](https://contest.ucup.ac/contest/2814/problem/16008) | S4 Wrocław | 概率期望与随机化、贪心、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.33） |
| [s4-16-K · Multiset Variance](https://contest.ucup.ac/contest/3347/problem/17160) | S4 Warsaw | 概率期望与随机化、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.17） |
| [s4-17-A · Anthill/Honeypot Simulator](https://contest.ucup.ac/contest/3384/problem/17161) | S4 St. Petersburg | 数值计算、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.1） |
| [s4-17-D · Distinguishable Distributions](https://contest.ucup.ac/contest/3384/problem/17164) | S4 St. Petersburg | 构造、概率期望与随机化、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.4） |
| [s4-18-K · Keep or Gamble](https://contest.ucup.ac/contest/3420/problem/17256) | S4 Hongō | 概率期望与随机化、贪心 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15851) |
| [s4-19-F · Forgot to Refuel](https://contest.ucup.ac/contest/3426/problem/17265) | S4 Belarus | 概率期望与随机化、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.4） |
| [s4-22-A · Kendama Challenge](https://contest.ucup.ac/contest/3575/problem/17713) | S4 Kyoto | 概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.1） |
| [s4-25-J · Jolly Janes](https://contest.ucup.ac/contest/3773/problem/18410) | S4 Zagreb | 概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.39） |
| [s4-Extra-3-H · Magical Puzzles](https://contest.ucup.ac/contest/2757/problem/15524) | S4 Osijek | 概率期望与随机化、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s5-1-A · Astana Hard Metro](https://contest.ucup.ac/contest/4126/problem/20248) | S5 Nizhny Novgorod | 动态规划、概率期望与随机化、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.1） |
| [s5-1-E · Easter Eggs](https://contest.ucup.ac/contest/4126/problem/20252) | S5 Nizhny Novgorod | 概率期望与随机化、贪心 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.10） |
| [s5-1-F · Fresh Cartridges](https://contest.ucup.ac/contest/4126/problem/20253) | S5 Nizhny Novgorod | 多项式与线性代数、概率期望与随机化、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.11） |
| [s5-1-G · Game Show: XOR Edition](https://contest.ucup.ac/contest/4126/problem/20254) | S5 Nizhny Novgorod | 位运算与状态压缩、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.13） |

### 构造

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-A · Adjacent Product Sum](https://contest.ucup.ac/contest/1106/problem/5517) | S1 Ukraine | 贪心、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.1） |
| [s1-4-D · Distance Parities](https://contest.ucup.ac/contest/1106/problem/5520) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-E · Excellent XOR Problem](https://contest.ucup.ac/contest/1106/problem/5521) | S1 Ukraine | 构造、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-F · F*** 3-Colorable Graphs](https://contest.ucup.ac/contest/1106/problem/5522) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-K · King of Swapping](https://contest.ucup.ac/contest/1106/problem/5527) | S1 Ukraine | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.8） |
| [s1-4-L · Least Annoying Constructive Problem](https://contest.ucup.ac/contest/1106/problem/5528) | S1 Ukraine | 构造、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.9） |
| [s1-4-M · Most Annoying Constructive Problem](https://contest.ucup.ac/contest/1106/problem/5529) | S1 Ukraine | 构造、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.9） |
| [s1-7-E · Garbage Disposal](https://contest.ucup.ac/contest/1129/problem/5742) | S1 Zaporizhzhia | 构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.9） |
| [s1-8-G · Greedy Drawers](https://contest.ucup.ac/contest/1070/problem/5255) | S1 Slovenia | 构造、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.6） |
| [s1-12-C · Parallel Processing (Easy)](https://contest.ucup.ac/contest/1207/problem/6319) | S1 Ōokayama | 搜索与二分、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-D · Parallel Processing (Hard)](https://contest.ucup.ac/contest/1207/problem/6320) | S1 Ōokayama | 构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.2） |
| [s1-13-J · Kth Lex Min Min Min Subpalindromes](https://contest.ucup.ac/contest/1212/problem/6353) | S1 Iberia | 字符串、构造、组合计数 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-F · Classical Geometry Problem](https://contest.ucup.ac/contest/1223/problem/6412) | S1 Gomel | 计算几何、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-16-H · Classical Maximization Problem](https://contest.ucup.ac/contest/1223/problem/6414) | S1 Gomel | 图论、构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.3） |
| [s1-20-F · Longest Strictly Increasing Sequence](https://contest.ucup.ac/contest/1259/problem/6636) | S1 India | 构造、动态规划 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.22） |
| [s1-20-K · XOR Dice](https://contest.ucup.ac/contest/1259/problem/6641) | S1 India | 构造、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.39） |
| [s1-20-M · Graphs and Colors](https://contest.ucup.ac/contest/1259/problem/6643) | S1 India | 构造、图论 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.43） |
| [s1-20-N · Red Black Grid](https://contest.ucup.ac/contest/1259/problem/6644) | S1 India | 构造 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.46） |
| [s2-2-I · Password](https://contest.ucup.ac/contest/1356/problem/7183) | S2 SPb | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.6） |
| [s2-2-L · "Memo" Game With a Hint](https://contest.ucup.ac/contest/1356/problem/7186) | S2 SPb | 交互与信息编码、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.8） |
| [s2-5-G · Good and Lucky Matrices](https://contest.ucup.ac/contest/1388/problem/6552) | S2 Northern | 多项式与线性代数、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3)（文件 p.2） |
| [s2-7-F · Exactly Three Neighbors](https://contest.ucup.ac/contest/1399/problem/7637) | S2 Two Capitals | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.3） |
| [s2-7-K · Integer Half-Sum](https://contest.ucup.ac/contest/1399/problem/7642) | S2 Two Capitals | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-7-L · esreveR Order](https://contest.ucup.ac/contest/1399/problem/7643) | S2 Two Capitals | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.8） |
| [s2-14-B · Build Permutation](https://contest.ucup.ac/contest/1452/problem/7933) | S2 Southeastern Europe | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.2） |
| [s2-14-H · High Towers](https://contest.ucup.ac/contest/1452/problem/7939) | S2 Southeastern Europe | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.9） |
| [s2-14-L · LIS on Grid](https://contest.ucup.ac/contest/1452/problem/7943) | S2 Southeastern Europe | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.13） |
| [s2-16-A · Bracket-and-bar Sequences](https://contest.ucup.ac/contest/1465/problem/4824) | S2 Run Twice | 组合计数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.5） |
| [s2-16-B · Even and Odd Combinations](https://contest.ucup.ac/contest/1465/problem/4825) | S2 Run Twice | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.15） |
| [s2-16-C · Find the Parts](https://contest.ucup.ac/contest/1465/problem/4826) | S2 Run Twice | 构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.27） |
| [s2-16-D · Message Made of Noise](https://contest.ucup.ac/contest/1465/problem/4827) | S2 Run Twice | 构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.35） |
| [s2-16-F · Mark on a Graph](https://contest.ucup.ac/contest/1465/problem/4829) | S2 Run Twice | 图论、构造、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.65） |
| [s2-16-K · Trijection](https://contest.ucup.ac/contest/1465/problem/4834) | S2 Run Twice | 组合计数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.158） |
| [s2-18-B · Bit Component](https://contest.ucup.ac/contest/1475/problem/8004) | S2 Dolgoprudny | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-19-C · Yet Another Balanced Coloring Problem](https://contest.ucup.ac/contest/1487/problem/8130) | S2 Estonia | 树上算法、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.6） |
| [s2-19-E · Freshman's Dream](https://contest.ucup.ac/contest/1487/problem/8132) | S2 Estonia | 构造、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.8） |
| [s2-20-J · Set Construction](https://contest.ucup.ac/contest/1499/problem/8174) | S2 Ōokayama | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.13） |
| [s2-21-C · Curly Palindromes](https://contest.ucup.ac/contest/1511/problem/8209) | S2 Delft | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.2） |
| [s2-21-D · Division 3 Polyglot](https://contest.ucup.ac/contest/1511/problem/8210) | S2 Delft | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-K · King's Dinner](https://contest.ucup.ac/contest/1511/problem/8217) | S2 Delft | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.9） |
| [s2-26-E · Expanding STACKS!](https://contest.ucup.ac/contest/1576/problem/8509) | S2 Latin America | 图论、构造 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.6） |
| [s3-0-F · Magic Bean](https://contest.ucup.ac/contest/1695/problem/8773) | S3 America | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.12） |
| [s3-1-N · (Un)labeled graphs](https://contest.ucup.ac/contest/1696/problem/8794) | S3 St. Petersburg | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.217） |
| [s3-2-G · Puzzle II](https://contest.ucup.ac/contest/1699/problem/8523) | S3 Zielona Gora | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.102） |
| [s3-4-B · Black or White 2](https://contest.ucup.ac/contest/1738/problem/9114) | S3 Hongo | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.11） |
| [s3-4-E · Equally Dividing](https://contest.ucup.ac/contest/1738/problem/9117) | S3 Hongo | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.27） |
| [s3-5-D · Function with Many Maximums](https://contest.ucup.ac/contest/1741/problem/9133) | S3 Moscow | 构造 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-I · Marks Sum](https://contest.ucup.ac/contest/1741/problem/9138) | S3 Moscow | 构造 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-A · Coprime Array](https://contest.ucup.ac/contest/1762/problem/9167) | S3 Osijek | 数论、构造、概率期望与随机化 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-11-E · Aim High](https://contest.ucup.ac/contest/1804/problem/9439) | S3 Sumiyosi | 构造 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/10023) |
| [s3-11-L · Construction of Town](https://contest.ucup.ac/contest/1804/problem/9446) | S3 Sumiyosi | 构造、图论 | [原文](https://atcoder.jp/contests/npcapc_2024/editorial/9999) |
| [s3-13-I · Colored Complete Graph](https://contest.ucup.ac/contest/1812/problem/9484) | S3 Sendai | 交互与信息编码、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.44） |
| [s3-13-J · (mod N² + 1)](https://contest.ucup.ac/contest/1812/problem/9485) | S3 Sendai | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.47） |
| [s3-18-A · All-Star](https://contest.ucup.ac/contest/1849/problem/9781) | S3 Southeastern Europe | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.1） |
| [s3-18-B · NonZero PrefSuf Sums](https://contest.ucup.ac/contest/1849/problem/9782) | S3 Southeastern Europe | 贪心、数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.2） |
| [s3-21-G · Diverge and Converge](https://contest.ucup.ac/contest/1872/problem/9881) | S3 Ōokayama | 树上算法、构造 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11092) |
| [s3-21-J · Grid Construction](https://contest.ucup.ac/contest/1872/problem/9884) | S3 Ōokayama | 构造 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11083) |
| [s3-24-D · Diminishing Fractions](https://contest.ucup.ac/contest/1890/problem/9962) | S3 Poland | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.111） |
| [s3-27-G · Geo Sharding](https://contest.ucup.ac/contest/1901/problem/8617) | S3 London | 构造、计算几何 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-31-B · Bad Digits](https://contest.ucup.ac/contest/1924/problem/10115) | S3 Wroclaw | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.19） |
| [s3-31-H · Hues](https://contest.ucup.ac/contest/1924/problem/10121) | S3 Wroclaw | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.61） |
| [s3-31-K · King's Festival](https://contest.ucup.ac/contest/1924/problem/10124) | S3 Wroclaw | 搜索与二分、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.35） |
| [s3-32-A · Sort and &](https://contest.ucup.ac/contest/1939/problem/10214) | S3 Dhaka | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-D · Qwiksort](https://contest.ucup.ac/contest/1939/problem/10217) | S3 Dhaka | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.2） |
| [s3-33-C · Construct uwu](https://contest.ucup.ac/contest/1954/problem/10267) | S3 India | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.3） |
| [s3-33-K · P to Q](https://contest.ucup.ac/contest/1954/problem/10275) | S3 India | 构造、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.12） |
| [s3-34-A · Inversions of PQ and QP](https://contest.ucup.ac/contest/1965/problem/10321) | S3 Aobayama | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.48） |
| [s3-34-D · Swap Counter](https://contest.ucup.ac/contest/1965/problem/10324) | S3 Aobayama | 构造、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.43） |
| [s3-34-H · 12 Grid](https://contest.ucup.ac/contest/1965/problem/10328) | S3 Aobayama | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.25） |
| [s3-34-L · Square Connection](https://contest.ucup.ac/contest/1965/problem/10332) | S3 Aobayama | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.18） |
| [s3-39-D · Digits of Prefix Product](https://contest.ucup.ac/contest/2071/problem/10973) | S3 Tokyo | 构造、数论 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-E · Edge Coloring Problem](https://contest.ucup.ac/contest/2071/problem/10974) | S3 Tokyo | 图论、构造 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-L · LIS Triangle](https://contest.ucup.ac/contest/2071/problem/10981) | S3 Tokyo | 构造 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-A · AGI](https://contest.ucup.ac/contest/2135/problem/12150) | S3 Potyczki | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.244） |
| [s3-40-F · Puzzle IV](https://contest.ucup.ac/contest/2135/problem/12155) | S3 Potyczki | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.96） |
| [s4-0-A · A Totient Quotient](https://contest.ucup.ac/contest/2041/problem/11356) | S4 America | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.2） |
| [s4-0-F · Mob Grinder](https://contest.ucup.ac/contest/2041/problem/11361) | S4 America | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.23） |
| [s4-1-D · Sequence Is Not Subsequence](https://contest.ucup.ac/contest/2539/problem/14429) | S4 Korolyov | 字符串、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-E · Coffee Shops](https://contest.ucup.ac/contest/2539/problem/14430) | S4 Korolyov | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-J · Yet Another Constructive Problem](https://contest.ucup.ac/contest/2539/problem/14435) | S4 Korolyov | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.4） |
| [s4-2-D · Digit Division](https://contest.ucup.ac/contest/2551/problem/14133) | S4 Paris | 数论、构造、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-L · Lice Hopping](https://contest.ucup.ac/contest/2551/problem/14141) | S4 Paris | 树上算法、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-2-M · Manhattan Graph](https://contest.ucup.ac/contest/2551/problem/14142) | S4 Paris | 图论、计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.13） |
| [s4-3-I · Two Permutations](https://contest.ucup.ac/contest/2559/problem/14423) | S4 Polar | 构造、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-A · AIMPPZ](https://contest.ucup.ac/contest/2668/problem/15444) | S4 Poland | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.4） |
| [s4-8-I · ICPC Isolation](https://contest.ucup.ac/contest/2668/problem/15452) | S4 Poland | 构造、搜索与二分、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.7） |
| [s4-10-J · Joyful Guided Tour](https://contest.ucup.ac/contest/2814/problem/16009) | S4 Wrocław | 图论、贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.93） |
| [s4-10-K · Key Properties](https://contest.ucup.ac/contest/2814/problem/16010) | S4 Wrocław | 构造、图论、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.24） |
| [s4-11-E · Phone Company](https://contest.ucup.ac/contest/2828/problem/16119) | S4 Southeastern Europe | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.5） |
| [s4-11-H · Sorted Pairs](https://contest.ucup.ac/contest/2828/problem/16122) | S4 Southeastern Europe | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.8） |
| [s4-11-K · Connect the Points](https://contest.ucup.ac/contest/2828/problem/16125) | S4 Southeastern Europe | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.14） |
| [s4-13-B · Increasing Swaps](https://contest.ucup.ac/contest/2921/problem/16227) | S4 Ōokayama | 贪心、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.1） |
| [s4-13-G · Don't Make Zero](https://contest.ucup.ac/contest/2921/problem/16232) | S4 Ōokayama | 构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.11） |
| [s4-17-B · Missing Number](https://contest.ucup.ac/contest/3384/problem/17162) | S4 St. Petersburg | 构造、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.1） |
| [s4-17-D · Distinguishable Distributions](https://contest.ucup.ac/contest/3384/problem/17164) | S4 St. Petersburg | 构造、概率期望与随机化、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.4） |
| [s4-17-E · Four Sages Around an Oak Tree](https://contest.ucup.ac/contest/3384/problem/17165) | S4 St. Petersburg | 构造、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.4） |
| [s4-17-H · Sweet Remainders!](https://contest.ucup.ac/contest/3384/problem/17168) | S4 St. Petersburg | 树上算法、构造、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.7） |
| [s4-17-K · Traversal of a Triangular Grid](https://contest.ucup.ac/contest/3384/problem/17171) | S4 St. Petersburg | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.11） |
| [s4-17-L · Triangles](https://contest.ucup.ac/contest/3384/problem/17172) | S4 St. Petersburg | 计算几何、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.12） |
| [s4-18-H · Heyawake-like Problem](https://contest.ucup.ac/contest/3420/problem/17253) | S4 Hongō | 构造 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15852) |
| [s4-19-L · Layered Caesar Salad](https://contest.ucup.ac/contest/3426/problem/17271) | S4 Belarus | 构造、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-20-I · Point Mirror](https://contest.ucup.ac/contest/3516/problem/17414) | S4 India | 数论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.14） |
| [s4-20-M · Vertex Separation](https://contest.ucup.ac/contest/3516/problem/17418) | S4 India | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.20） |
| [s4-21-C · Don't be Clockwise](https://contest.ucup.ac/contest/3542/problem/17421) | S4 Kamigō | 计算几何、贪心、构造 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17020) |
| [s4-21-F · Increase Decrease](https://contest.ucup.ac/contest/3542/problem/17424) | S4 Kamigō | 构造、动态规划 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18127) |
| [s4-21-M · Up-Down Sequence](https://contest.ucup.ac/contest/3542/problem/17431) | S4 Kamigō | 构造、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17005) |
| [s4-22-I · Xor Magic Square](https://contest.ucup.ac/contest/3575/problem/17721) | S4 Kyoto | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-22-K · Square Resistance Value](https://contest.ucup.ac/contest/3575/problem/17723) | S4 Kyoto | 数论、构造、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-22-N · Cellular Component Constellation](https://contest.ucup.ac/contest/3575/problem/17726) | S4 Kyoto | 构造、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.11） |
| [s4-25-D · Dangerous Data](https://contest.ucup.ac/contest/3773/problem/18404) | S4 Zagreb | 多项式与线性代数、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.14） |
| [s4-25-L · Loop Land](https://contest.ucup.ac/contest/3773/problem/18412) | S4 Zagreb | 图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.45） |
| [s4-Extra-3-A · Magician](https://contest.ucup.ac/contest/2757/problem/15517) | S4 Osijek | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-L · Robots](https://contest.ucup.ac/contest/2757/problem/15528) | S4 Osijek | 树上算法、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-1-L · Leave Triple & Link Tree](https://contest.ucup.ac/contest/4126/problem/20259) | S5 Nizhny Novgorod | 图论、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.22） |
| [s5-3-C · Circle Construction](https://contest.ucup.ac/contest/4565/problem/20731) | S5 Gorkovskaya | 计算几何、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |
| [s5-3-E · Equal Totients](https://contest.ucup.ac/contest/4565/problem/20733) | S5 Gorkovskaya | 数论、构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.4） |
| [s5-3-J · Jump Cycle](https://contest.ucup.ac/contest/4565/problem/20738) | S5 Gorkovskaya | 构造 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.9） |
| [s5-6-E · K-Independent Matrix](https://contest.ucup.ac/contest/4617/problem/23673) | S5 Hyakumanben | 数论、构造、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |

### 交互与信息编码

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-13-B · Random Interactive Convex Hull Bot](https://contest.ucup.ac/contest/1212/problem/6345) | S1 Iberia | 计算几何、交互与信息编码、概率期望与随机化 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.1） |
| [s2-2-E · Fischer's Chess Guessing Game](https://contest.ucup.ac/contest/1356/problem/7179) | S2 SPb | 交互与信息编码、贪心、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.3） |
| [s2-2-L · "Memo" Game With a Hint](https://contest.ucup.ac/contest/1356/problem/7186) | S2 SPb | 交互与信息编码、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.8） |
| [s2-16-H · Eager Sorting](https://contest.ucup.ac/contest/1465/problem/4831) | S2 Run Twice | 交互与信息编码、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.92） |
| [s2-16-J · Tetra-puzzle](https://contest.ucup.ac/contest/1465/problem/4833) | S2 Run Twice | 搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.136） |
| [s2-21-J · Jumbled Primes](https://contest.ucup.ac/contest/1511/problem/8216) | S2 Delft | 交互与信息编码、数论 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.8） |
| [s3-1-D · Dwarfs' Bedtime](https://contest.ucup.ac/contest/1696/problem/8784) | S3 St. Petersburg | 交互与信息编码、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.57） |
| [s3-13-I · Colored Complete Graph](https://contest.ucup.ac/contest/1812/problem/9484) | S3 Sendai | 交互与信息编码、图论、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.44） |
| [s3-21-I · Near Pair](https://contest.ucup.ac/contest/1872/problem/9883) | S3 Ōokayama | 交互与信息编码、搜索与二分 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11470) |
| [s3-27-E · Equal Strings](https://contest.ucup.ac/contest/1901/problem/8615) | S3 London | 交互与信息编码、概率期望与随机化、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-I · Interactive Casino](https://contest.ucup.ac/contest/1901/problem/8619) | S3 London | 概率期望与随机化、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-30-A · Archaeology](https://contest.ucup.ac/contest/1917/problem/10087) | S3 Northern | 交互与信息编码、计算几何、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-30-F · Interactive Primality](https://contest.ucup.ac/contest/1917/problem/10092) | S3 Northern | 交互与信息编码、数论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.3） |
| [s3-39-F · Fourier Coefficients](https://contest.ucup.ac/contest/2071/problem/10975) | S3 Tokyo | 多项式与线性代数、交互与信息编码 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-H · Hidden Sequence Rotation](https://contest.ucup.ac/contest/2071/problem/10977) | S3 Tokyo | 字符串、交互与信息编码 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s4-0-C · Entrapment](https://contest.ucup.ac/contest/2041/problem/11358) | S4 America | 博弈论、搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.16） |
| [s4-8-G · Game of Pipes](https://contest.ucup.ac/contest/2668/problem/15450) | S4 Poland | 交互与信息编码、图论、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.136） |
| [s4-10-A · Automatized Mineral Classification](https://contest.ucup.ac/contest/2814/problem/16000) | S4 Wrocław | 交互与信息编码、概率期望与随机化、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.45） |
| [s4-10-B · Bit Recovery](https://contest.ucup.ac/contest/2814/problem/16001) | S4 Wrocław | 多项式与线性代数、位运算与状态压缩、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.104） |
| [s4-19-D · Detecting the Missing Ship](https://contest.ucup.ac/contest/3426/problem/17263) | S4 Belarus | 交互与信息编码、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-22-H · How to Validate Such a Program](https://contest.ucup.ac/contest/3575/problem/17720) | S4 Kyoto | 多项式与线性代数、交互与信息编码、树上算法 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-Extra-3-C · Glitch](https://contest.ucup.ac/contest/2757/problem/15519) | S4 Osijek | 搜索与二分、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-K · Hidden Digits](https://contest.ucup.ac/contest/2757/problem/15527) | S4 Osijek | 交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-6-L · Consecutive Pairs](https://contest.ucup.ac/contest/4617/problem/23680) | S5 Hyakumanben | 交互与信息编码、搜索与二分、图论 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.23） |

### 位运算与状态压缩

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-E · Excellent XOR Problem](https://contest.ucup.ac/contest/1106/problem/5521) | S1 Ukraine | 构造、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.3） |
| [s1-4-G · Graph Problem With Small $n$](https://contest.ucup.ac/contest/1106/problem/5523) | S1 Ukraine | 动态规划、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.4） |
| [s1-4-J · Jewel of Data Structure Problems](https://contest.ucup.ac/contest/1106/problem/5526) | S1 Ukraine | 位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-12-A · XOR Tree Path](https://contest.ucup.ac/contest/1207/problem/6317) | S1 Ōokayama | 树上算法、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-N · XOR Reachable](https://contest.ucup.ac/contest/1207/problem/6330) | S1 Ōokayama | 数据结构、图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-12-O · Jewel Game](https://contest.ucup.ac/contest/1207/problem/6331) | S1 Ōokayama | 博弈论、动态规划、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-13-D · XOR Determinant](https://contest.ucup.ac/contest/1212/problem/6347) | S1 Iberia | 多项式与线性代数、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.2） |
| [s1-13-K · 4](https://contest.ucup.ac/contest/1212/problem/6354) | S1 Iberia | 图论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-20-A · Maximum Bitwise OR](https://contest.ucup.ac/contest/1259/problem/6631) | S1 India | 位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.2） |
| [s1-20-K · XOR Dice](https://contest.ucup.ac/contest/1259/problem/6641) | S1 India | 构造、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.39） |
| [s1-20-L · (1, 2) Nim](https://contest.ucup.ac/contest/1259/problem/6642) | S1 India | 博弈论、位运算与状态压缩 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.41） |
| [s2-5-D · Two Missing Numbers](https://contest.ucup.ac/contest/1388/problem/6549) | S2 Northern | 数论、位运算与状态压缩、多项式与线性代数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=3)（文件 p.7） |
| [s2-5-J · Sets May Be Good](https://contest.ucup.ac/contest/1388/problem/6555) | S2 Northern | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.30） |
| [s2-6-B · The Doubling Game 2](https://contest.ucup.ac/contest/1398/problem/7607) | S2 Warsaw | 树上算法、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-7-D · Fairy Chess](https://contest.ucup.ac/contest/1399/problem/7635) | S2 Two Capitals | 博弈论、位运算与状态压缩、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.2） |
| [s2-7-L · esreveR Order](https://contest.ucup.ac/contest/1399/problem/7643) | S2 Two Capitals | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.8） |
| [s2-14-A · AND-OR closure](https://contest.ucup.ac/contest/1452/problem/7932) | S2 Southeastern Europe | 位运算与状态压缩、图论、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.1） |
| [s2-14-F · Fast XORting](https://contest.ucup.ac/contest/1452/problem/7937) | S2 Southeastern Europe | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.7） |
| [s2-14-I · Impossible Numbers](https://contest.ucup.ac/contest/1452/problem/7940) | S2 Southeastern Europe | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.10） |
| [s2-16-B · Even and Odd Combinations](https://contest.ucup.ac/contest/1465/problem/4825) | S2 Run Twice | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.15） |
| [s2-16-E · Four Plus Four](https://contest.ucup.ac/contest/1465/problem/4828) | S2 Run Twice | 贪心、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.47） |
| [s2-16-G · Transfer of Duty](https://contest.ucup.ac/contest/1465/problem/4830) | S2 Run Twice | 位运算与状态压缩、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.80） |
| [s2-18-B · Bit Component](https://contest.ucup.ac/contest/1475/problem/8004) | S2 Dolgoprudny | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-18-C · Crossing the Border](https://contest.ucup.ac/contest/1475/problem/8005) | S2 Dolgoprudny | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.2） |
| [s2-19-E · Freshman's Dream](https://contest.ucup.ac/contest/1487/problem/8132) | S2 Estonia | 构造、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.8） |
| [s2-20-B · Almost Large](https://contest.ucup.ac/contest/1499/problem/8166) | S2 Ōokayama | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.1） |
| [s2-20-J · Set Construction](https://contest.ucup.ac/contest/1499/problem/8174) | S2 Ōokayama | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.13） |
| [s2-26-L · LED Matrix](https://contest.ucup.ac/contest/1576/problem/8516) | S2 Latin America | 模拟与基础实现、位运算与状态压缩 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.16） |
| [s3-0-C · Comparator](https://contest.ucup.ac/contest/1695/problem/8770) | S3 America | 位运算与状态压缩、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.7） |
| [s3-0-M · Training, Round 2](https://contest.ucup.ac/contest/1695/problem/8780) | S3 America | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.26） |
| [s3-1-A · Element-Wise Comparison](https://contest.ucup.ac/contest/1696/problem/8781) | S3 St. Petersburg | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.2） |
| [s3-2-C · Radars](https://contest.ucup.ac/contest/1699/problem/8519) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.31） |
| [s3-2-D · Xor Partitions](https://contest.ucup.ac/contest/1699/problem/8520) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.41） |
| [s3-2-J · Polygon II](https://contest.ucup.ac/contest/1699/problem/8526) | S3 Zielona Gora | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.160） |
| [s3-2-K · Power Divisions](https://contest.ucup.ac/contest/1699/problem/8527) | S3 Zielona Gora | 动态规划、位运算与状态压缩、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.175） |
| [s3-4-C · Contour Multiplication](https://contest.ucup.ac/contest/1738/problem/9115) | S3 Hongo | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.16） |
| [s3-4-F · Flip or Not](https://contest.ucup.ac/contest/1738/problem/9118) | S3 Hongo | 多项式与线性代数、数论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.32） |
| [s3-6-C · -is-this-bitset-](https://contest.ucup.ac/contest/1762/problem/9169) | S3 Osijek | 树上算法、动态规划、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-13-C · Shift Puzzle](https://contest.ucup.ac/contest/1812/problem/9478) | S3 Sendai | 搜索与二分、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.18） |
| [s3-18-I · Donkey, Keep Watch](https://contest.ucup.ac/contest/1849/problem/9789) | S3 Southeastern Europe | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.11） |
| [s3-21-D · A xor B plus C](https://contest.ucup.ac/contest/1872/problem/9878) | S3 Ōokayama | 位运算与状态压缩、动态规划 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11464) |
| [s3-21-L · Long Sequence Inversion 2](https://contest.ucup.ac/contest/1872/problem/9886) | S3 Ōokayama | 组合计数、位运算与状态压缩 | [原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11222) |
| [s3-24-J · Just Zeros](https://contest.ucup.ac/contest/1890/problem/9968) | S3 Poland | 位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.94） |
| [s3-27-C · Cardinality](https://contest.ucup.ac/contest/1901/problem/8613) | S3 London | 概率期望与随机化、位运算与状态压缩、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-31-E · Expression](https://contest.ucup.ac/contest/1924/problem/10118) | S3 Wroclaw | 模拟与基础实现、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.51） |
| [s3-32-A · Sort and &](https://contest.ucup.ac/contest/1939/problem/10214) | S3 Dhaka | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-F · Yet Another Crossover Episode](https://contest.ucup.ac/contest/1939/problem/10219) | S3 Dhaka | 位运算与状态压缩、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-H · Are the nodes reachable?](https://contest.ucup.ac/contest/1939/problem/10221) | S3 Dhaka | 图论、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.4） |
| [s3-32-I · Unhappy Team](https://contest.ucup.ac/contest/1939/problem/10222) | S3 Dhaka | 概率期望与随机化、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.5） |
| [s3-32-L · Uncle Bob and XOR Sum](https://contest.ucup.ac/contest/1939/problem/10225) | S3 Dhaka | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.6） |
| [s3-32-M · Tree Flip](https://contest.ucup.ac/contest/1939/problem/10226) | S3 Dhaka | 树上算法、数据结构、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.7） |
| [s3-39-P · Perfect Suika Game on a Tree](https://contest.ucup.ac/contest/2071/problem/10985) | S3 Tokyo | 树上算法、数据结构、位运算与状态压缩 | [原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-E · One Bit](https://contest.ucup.ac/contest/2135/problem/12154) | S3 Potyczki | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.88） |
| [s3-40-K · Projects](https://contest.ucup.ac/contest/2135/problem/12160) | S3 Potyczki | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.171） |
| [s4-2-C · Classement Nationale](https://contest.ucup.ac/contest/2551/problem/14132) | S4 Paris | 位运算与状态压缩、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-10-B · Bit Recovery](https://contest.ucup.ac/contest/2814/problem/16001) | S4 Wrocław | 多项式与线性代数、位运算与状态压缩、交互与信息编码 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.104） |
| [s4-11-B · AND Reconstruction](https://contest.ucup.ac/contest/2828/problem/16116) | S4 Southeastern Europe | 位运算与状态压缩、字符串 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.2） |
| [s4-11-C · XOR-Excluding Sets](https://contest.ucup.ac/contest/2828/problem/16117) | S4 Southeastern Europe | 位运算与状态压缩、多项式与线性代数、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.3） |
| [s4-16-B · Bitwise Beach](https://contest.ucup.ac/contest/3347/problem/17151) | S4 Warsaw | 位运算与状态压缩、搜索与二分 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.4） |
| [s4-16-J · Jewel Guards](https://contest.ucup.ac/contest/3347/problem/17159) | S4 Warsaw | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.16） |
| [s4-17-D · Distinguishable Distributions](https://contest.ucup.ac/contest/3384/problem/17164) | S4 St. Petersburg | 构造、概率期望与随机化、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.4） |
| [s4-18-C · Convex Crusher](https://contest.ucup.ac/contest/3420/problem/17248) | S4 Hongō | 计算几何、位运算与状态压缩 | [原文](https://atcoder.jp/contests/utpc2025/editorial/16125) |
| [s4-19-B · Building a Reactor](https://contest.ucup.ac/contest/3426/problem/17261) | S4 Belarus | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.1） |
| [s4-19-C · Cell Flip Game](https://contest.ucup.ac/contest/3426/problem/17262) | S4 Belarus | 位运算与状态压缩、多项式与线性代数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.2） |
| [s4-19-I · Ivan Tsarevich in the Magical Grove](https://contest.ucup.ac/contest/3426/problem/17268) | S4 Belarus | 图论、动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-21-A · 01 Matrix](https://contest.ucup.ac/contest/3542/problem/17419) | S4 Kamigō | 位运算与状态压缩、图论、组合计数 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18120) |
| [s4-21-H · OR Preference](https://contest.ucup.ac/contest/3542/problem/17426) | S4 Kamigō | 位运算与状态压缩、动态规划、贪心 | [原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) |
| [s4-22-C · Partition AND/OR Aggregation](https://contest.ucup.ac/contest/3575/problem/17715) | S4 Kyoto | 位运算与状态压缩、搜索与二分、贪心 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.2） |
| [s4-22-I · Xor Magic Square](https://contest.ucup.ac/contest/3575/problem/17721) | S4 Kyoto | 构造、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-22-O · Xor Triangle](https://contest.ucup.ac/contest/3575/problem/17727) | S4 Kyoto | 位运算与状态压缩、组合计数 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.12） |
| [s4-25-F · Flipping Frenzy](https://contest.ucup.ac/contest/3773/problem/18406) | S4 Zagreb | 多项式与线性代数、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.22） |
| [s4-25-G · Grid Gradient](https://contest.ucup.ac/contest/3773/problem/18407) | S4 Zagreb | 动态规划、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.27） |
| [s4-Extra-3-A · Magician](https://contest.ucup.ac/contest/2757/problem/15517) | S4 Osijek | 位运算与状态压缩、构造 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-E · XOR Again?](https://contest.ucup.ac/contest/2757/problem/15521) | S4 Osijek | 位运算与状态压缩、动态规划 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-H · Magical Puzzles](https://contest.ucup.ac/contest/2757/problem/15524) | S4 Osijek | 概率期望与随机化、位运算与状态压缩、图论 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s4-Extra-3-J · AND Components](https://contest.ucup.ac/contest/2757/problem/15526) | S4 Osijek | 数据结构、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-1-G · Game Show: XOR Edition](https://contest.ucup.ac/contest/4126/problem/20254) | S5 Nizhny Novgorod | 位运算与状态压缩、动态规划、概率期望与随机化 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.13） |
| [s5-3-F · Flipping Lamps](https://contest.ucup.ac/contest/4565/problem/20734) | S5 Gorkovskaya | 多项式与线性代数、位运算与状态压缩、组合计数 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.5） |
| [s5-3-G · Game](https://contest.ucup.ac/contest/4565/problem/20735) | S5 Gorkovskaya | 博弈论、位运算与状态压缩 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.6） |
| [s5-6-F · Path XOR on MST](https://contest.ucup.ac/contest/4617/problem/23674) | S5 Hyakumanben | 图论、位运算与状态压缩、数据结构 | [原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |

### 数值计算

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-7-C · Testing Subjects Usually Die](https://contest.ucup.ac/contest/1129/problem/5740) | S1 Zaporizhzhia | 概率期望与随机化、数值计算 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-7.pdf)（文件 p.4） |
| [s1-8-E · Denormalization](https://contest.ucup.ac/contest/1070/problem/5253) | S1 Slovenia | 数值计算、搜索与二分 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.4） |
| [s3-1-E · Fake Coin and Lying Scales](https://contest.ucup.ac/contest/1696/problem/8785) | S3 St. Petersburg | 组合计数、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.65） |
| [s3-1-O · Mysterious Sequence](https://contest.ucup.ac/contest/1696/problem/8795) | S3 St. Petersburg | 搜索与二分、多项式与线性代数、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.231） |
| [s3-5-G · Exponent Calculator](https://contest.ucup.ac/contest/1741/problem/9136) | S3 Moscow | 数值计算 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-7-F · Fibonacci Fusion](https://contest.ucup.ac/contest/1774/problem/9225) | S3 Warsaw | 数论、概率期望与随机化、数值计算 | [原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s4-2-I · Infrared](https://contest.ucup.ac/contest/2551/problem/14138) | S4 Paris | 计算几何、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-17-A · Anthill/Honeypot Simulator](https://contest.ucup.ac/contest/3384/problem/17161) | S4 St. Petersburg | 数值计算、概率期望与随机化 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.1） |
| [s4-18-N · Numerical Error](https://contest.ucup.ac/contest/3420/problem/17259) | S4 Hongō | 组合计数、搜索与二分、数值计算 | [原文](https://atcoder.jp/contests/utpc2025/editorial/15904) |
| [s4-19-H · Helpful Bits](https://contest.ucup.ac/contest/3426/problem/17267) | S4 Belarus | 图论、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.5） |
| [s4-22-K · Square Resistance Value](https://contest.ucup.ac/contest/3575/problem/17723) | S4 Kyoto | 数论、构造、数值计算 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |

### 模拟与基础实现

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-L · The Game](https://contest.ucup.ac/contest/1070/problem/5260) | S1 Slovenia | 模拟与基础实现 | [原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.2） |
| [s2-2-B · I Flipped The Calendar...](https://contest.ucup.ac/contest/1356/problem/7176) | S2 SPb | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-6-J · Sequence Folding](https://contest.ucup.ac/contest/1398/problem/7615) | S2 Warsaw | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-20-F · $N^a (\log N)^b$](https://contest.ucup.ac/contest/1499/problem/8170) | S2 Ōokayama | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.7） |
| [s2-26-L · LED Matrix](https://contest.ucup.ac/contest/1576/problem/8516) | S2 Latin America | 模拟与基础实现、位运算与状态压缩 | [原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.16） |
| [s3-0-C · Comparator](https://contest.ucup.ac/contest/1695/problem/8770) | S3 America | 位运算与状态压缩、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.7） |
| [s3-0-D · Dihedral Group](https://contest.ucup.ac/contest/1695/problem/8771) | S3 America | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.9） |
| [s3-1-H · Page on vdome.com](https://contest.ucup.ac/contest/1696/problem/8788) | S3 St. Petersburg | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.111） |
| [s3-1-K · Tasks and Bugs](https://contest.ucup.ac/contest/1696/problem/8791) | S3 St. Petersburg | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.187） |
| [s3-1-M · Toilets](https://contest.ucup.ac/contest/1696/problem/8793) | S3 St. Petersburg | 数据结构、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.210） |
| [s3-5-B · Bookshelf Tracking](https://contest.ucup.ac/contest/1741/problem/9131) | S3 Moscow | 模拟与基础实现 | [原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-13-E · Hotel](https://contest.ucup.ac/contest/1812/problem/9480) | S3 Sendai | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.29） |
| [s3-24-A · Acronym](https://contest.ucup.ac/contest/1890/problem/9959) | S3 Poland | 字符串、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.2） |
| [s3-24-F · Frogs](https://contest.ucup.ac/contest/1890/problem/9964) | S3 Poland | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.162） |
| [s3-24-G · Game MPO](https://contest.ucup.ac/contest/1890/problem/9965) | S3 Poland | 图论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.13） |
| [s3-24-K · Kindergarten Square](https://contest.ucup.ac/contest/1890/problem/9969) | S3 Poland | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.8） |
| [s3-27-F · Fast Tree Queries](https://contest.ucup.ac/contest/1901/problem/8616) | S3 London | 树上算法、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-31-E · Expression](https://contest.ucup.ac/contest/1924/problem/10118) | S3 Wroclaw | 模拟与基础实现、位运算与状态压缩 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.51） |
| [s3-31-L · Labyrinth](https://contest.ucup.ac/contest/1924/problem/10125) | S3 Wroclaw | 图论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.25） |
| [s4-0-M · This Is Sparta!](https://contest.ucup.ac/contest/2041/problem/11368) | S4 America | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.53） |
| [s4-2-C · Classement Nationale](https://contest.ucup.ac/contest/2551/problem/14132) | S4 Paris | 位运算与状态压缩、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-G · Goofy Songs](https://contest.ucup.ac/contest/2551/problem/14136) | S4 Paris | 字符串、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-8-H · Hacking](https://contest.ucup.ac/contest/2668/problem/15451) | S4 Poland | 模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.2） |
| [s4-19-A · Art of Multiplication](https://contest.ucup.ac/contest/3426/problem/17260) | S4 Belarus | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.1） |
| [s4-19-E · Encountering a Friend](https://contest.ucup.ac/contest/3426/problem/17264) | S4 Belarus | 数论、模拟与基础实现 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-19-G · Guaranteed Medal](https://contest.ucup.ac/contest/3426/problem/17266) | S4 Belarus | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.4） |
| [s4-19-K · Kitchen](https://contest.ucup.ac/contest/3426/problem/17270) | S4 Belarus | 模拟与基础实现、数据结构 | [原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |

