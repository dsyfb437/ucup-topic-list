# 动态规划

163 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-G · Graph Problem With Small $n$](https://contest.ucup.ac/contest/1106/problem/5523) | S1 Ukraine | 动态规划、图论、位运算与状态压缩 | 子集 Hamilton 路 DP，位集压缩端点；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.4） |
| [s1-4-H · Help Me to Get This Published](https://contest.ucup.ac/contest/1106/problem/5524) | S1 Ukraine | 动态规划、组合计数、图论 | 按彩色度数从大到小计数 DP；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.5） |
| [s1-4-I · Increasing Grid](https://contest.ucup.ac/contest/1106/problem/5525) | S1 Ukraine | 动态规划、组合计数 | 把单调 01 网格转成边界路径计数；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-8-K · Skills in Pills](https://contest.ucup.ac/contest/1070/problem/5259) | S1 Slovenia | 动态规划 | 以相邻两天服药顺序为状态转移到下一冲突；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.7） |
| [s1-12-A · XOR Tree Path](https://contest.ucup.ac/contest/1207/problem/6317) | S1 Ōokayama | 树上算法、动态规划、位运算与状态压缩 | 按子树选中叶子数奇偶做树形 DP；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-B · Magical Wallet](https://contest.ucup.ac/contest/1207/problem/6318) | S1 Ōokayama | 动态规划 | 钱包金额 DP，先把数位重排为最大值；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.1） |
| [s1-12-F · Forestry](https://contest.ucup.ac/contest/1207/problem/6322) | S1 Ōokayama | 树上算法、动态规划、概率期望与随机化 | 断边概率 DP，统计连通块最小值期望；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-12-O · Jewel Game](https://contest.ucup.ac/contest/1207/problem/6331) | S1 Ōokayama | 博弈论、动态规划、位运算与状态压缩 | 剩余宝石子集状态，逆向分析有环博弈；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-16-B · Classical Counting Problem](https://contest.ucup.ac/contest/1223/problem/6408) | S1 Gomel | 动态规划、组合计数 | 枚举边界并用背包统计可行题目集合；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.1） |
| [s1-16-D · Classical DP Problem](https://contest.ucup.ac/contest/1223/problem/6410) | S1 Gomel | 动态规划、组合计数 | 棋盘最大正方形确定最少车数，按已覆盖列数 DP；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.2） |
| [s1-20-E · Strange Keyboard](https://contest.ucup.ac/contest/1259/problem/6635) | S1 India | 动态规划、字符串 | 字符串前缀 DP，计算一次键盘操作的覆盖代价；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.18） |
| [s1-20-F · Longest Strictly Increasing Sequence](https://contest.ucup.ac/contest/1259/problem/6636) | S1 India | 构造、动态规划 | 取 a=b 并验证前缀 LIS 条件；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.22） |
| [s1-20-H · Treelection](https://contest.ucup.ac/contest/1259/problem/6638) | S1 India | 树上算法、动态规划、搜索与二分 | 树形 DP 计算向祖先传票数，二分票数上界；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.28） |
| [s1-20-J · Talk That Talk](https://contest.ucup.ac/contest/1259/problem/6640) | S1 India | 组合计数、动态规划 | 按等差位置聚合，奇偶前后缀和优化计数；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.35） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | 子序列位置 DP，或枚举中间字符贪心选两侧；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-5-C · Courses](https://contest.ucup.ac/contest/1388/problem/6548) | S2 Northern | 动态规划、多项式与线性代数 | 双参数背包生成函数，单位根筛与有理函数递推；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.2） |
| [s2-5-F · Forever Young](https://contest.ucup.ac/contest/1388/problem/6551) | S2 Northern | 动态规划、组合计数 | Young 图增删路径交换恒等式，按子图形计数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=2)（文件 p.11） |
| [s2-5-L · LCSLCSLCS](https://contest.ucup.ac/contest/1388/problem/6557) | S2 Northern | 字符串、动态规划、多项式与线性代数 | 半局部 LCS 与 sticky braids 合成重复串转移；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.54） |
| [s2-6-A · Digital Nim](https://contest.ucup.ac/contest/1398/problem/7606) | S2 Warsaw | 博弈论、动态规划、数论 | 最近必败态递推，按十进制块加速；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-B · The Doubling Game 2](https://contest.ucup.ac/contest/1398/problem/7607) | S2 Warsaw | 树上算法、动态规划、位运算与状态压缩 | 子树按有效位数排序，合并入边权集合；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.1） |
| [s2-6-D · Colonization](https://contest.ucup.ac/contest/1398/problem/7609) | S2 Warsaw | 树上算法、动态规划 | 树形 DP 与换根，按最大子状态是否唯一转移；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-E · Bus Lines](https://contest.ucup.ac/contest/1398/problem/7610) | S2 Warsaw | 树上算法、动态规划 | 有向边状态统计可达层，聚合距离贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-7-C · Cards](https://contest.ucup.ac/contest/1399/problem/7634) | S2 Two Capitals | 多项式与线性代数、动态规划 | 随机游走计数，生成函数或分治加速 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-E · Fair Elections](https://contest.ucup.ac/contest/1399/problem/7636) | S2 Two Capitals | 博弈论、动态规划 | 三候选人逆推最优选择，压缩计票状态；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.3） |
| [s2-7-M · Good Splits](https://contest.ucup.ac/contest/1399/problem/7644) | S2 Two Capitals | 动态规划、组合计数 | 按包含首顶点的连通块分解做计数 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.8） |
| [s2-7-N · Shoes](https://contest.ucup.ac/contest/1399/problem/7645) | S2 Two Capitals | 动态规划、贪心 | 交换论证后做双端区间 DP，优化访问天数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.9） |
| [s2-14-A · AND-OR closure](https://contest.ucup.ac/contest/1452/problem/7932) | S2 Southeastern Europe | 位运算与状态压缩、图论、动态规划 | 相同位压缩成 DAG，统计向上闭合集合；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.1） |
| [s2-14-G · Graph Race](https://contest.ucup.ac/contest/1452/problem/7938) | S2 Southeastern Europe | 图论、动态规划 | 构造有向无环状态图，DP 聚合竞速答案；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.8） |
| [s2-18-A · Anti-Plagiarism](https://contest.ucup.ac/contest/1475/problem/8003) | S2 Dolgoprudny | 树上算法、动态规划、图论 | 树嵌入 DP，每对节点用二分图匹配合并子树；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.1） |
| [s2-18-C · Crossing the Border](https://contest.ucup.ac/contest/1475/problem/8005) | S2 Dolgoprudny | 动态规划、位运算与状态压缩 | 子集划分背包，固定最高位避免重复计数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.2） |
| [s2-18-E · Egg Drop Challenge](https://contest.ucup.ac/contest/1475/problem/8007) | S2 Dolgoprudny | 动态规划、数据结构 | DP 转移函数取下包络，类李超树维护；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.3） |
| [s2-18-G · Growing Sequences](https://contest.ucup.ac/contest/1475/problem/8009) | S2 Dolgoprudny | 动态规划、多项式与线性代数 | 证明计数 DP 为多项式，幂和递推计算系数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.4） |
| [s2-19-G · LCA Counting](https://contest.ucup.ac/contest/1487/problem/8134) | S2 Estonia | 树上算法、动态规划、贪心 | 树上取两个最大免费子状态，再按增益付费扩展；[原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.11） |
| [s2-20-A · Numerous Elimination](https://contest.ucup.ac/contest/1499/problem/8165) | S2 Ōokayama | 动态规划、数论 | 淘汰场次递推，利用整除结构化简到对数复杂度；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.1） |
| [s2-20-I · T Tile Placement Counting](https://contest.ucup.ac/contest/1499/problem/8173) | S2 Ōokayama | 动态规划、多项式与线性代数 | 插头状态记录环连接，BM 递推与 Bostan-Mori 求远项；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.10） |
| [s2-20-P · Bridge Elimination](https://contest.ucup.ac/contest/1499/problem/8180) | S2 Ōokayama | 组合计数、动态规划、图论 | 按无桥连通块分解，结合树计数公式；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.19） |
| [s2-21-A · Anton's ABCD](https://contest.ucup.ac/contest/1511/problem/8207) | S2 Delft | 动态规划、组合计数 | 递归块结构计数，合并各块大小；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.1） |
| [s2-21-E · Enumerating Substrings](https://contest.ucup.ac/contest/1511/problem/8211) | S2 Delft | 字符串、动态规划、组合计数 | 按 border 与周期分解，DP 统计不同字符模式；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-G · Graffiti](https://contest.ucup.ac/contest/1511/problem/8213) | S2 Delft | 树上算法、动态规划、字符串 | 记录父子字母做树形 DP，合并长度三路径贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.5） |
| [s2-26-F · Fair Distribution](https://contest.ucup.ac/contest/1576/problem/8510) | S2 Latin America | 数论、动态规划 | 住宅层高 gcd 给出可调差，模意义子集划分 DP；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.7） |
| [s2-26-G · Greek Casino](https://contest.ucup.ac/contest/1576/problem/8511) | S2 Latin America | 概率期望与随机化、动态规划、数论 | gcd 随机游走的期望递推，约数筛统计转移概率；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.8） |
| [s2-26-K · KMOP](https://contest.ucup.ac/contest/1576/problem/8515) | S2 Latin America | 图论、动态规划 | 打字位置、模式、辅音数量构成 DAG，BFS 求最短方案；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.14） |
| [s3-0-A · Arrested Development](https://contest.ucup.ac/contest/1695/problem/8768) | S3 America | 动态规划 | 以第一名实习生用时为容量，背包求另一人最少用时；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.2） |
| [s3-0-G · Manhattan Walk](https://contest.ucup.ac/contest/1695/problem/8774) | S3 America | 概率期望与随机化、动态规划 | 网格状态期望递推，利用方向对称性；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.14） |
| [s3-0-I · Not Another Constructive!](https://contest.ucup.ac/contest/1695/problem/8776) | S3 America | 动态规划、字符串 | 记忆化搜索记录 N、NA、NAC 子序列数量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.18） |
| [s3-0-M · Training, Round 2](https://contest.ucup.ac/contest/1695/problem/8780) | S3 America | 动态规划、位运算与状态压缩 | 二维能力可达状态，用 bitset 和删除已处理状态加速；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.26） |
| [s3-1-L · Candies](https://contest.ucup.ac/contest/1696/problem/8792) | S3 St. Petersburg | 动态规划、组合计数 | 三维计数递推与组合恒等式化简；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.192） |
| [s3-2-C · Radars](https://contest.ucup.ac/contest/1699/problem/8519) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | 只需覆盖四角，十六状态最小代价 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.31） |
| [s3-2-D · Xor Partitions](https://contest.ucup.ac/contest/1699/problem/8520) | S3 Zielona Gora | 动态规划、位运算与状态压缩 | 区间异或拆位，按前缀奇偶聚合 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.41） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | Fibonacci 单词递归，预处理匹配转移；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-2-F · Waterfall Matrix](https://contest.ucup.ac/contest/1699/problem/8522) | S3 Zielona Gora | 动态规划、数据结构 | 阈值最优边界单调，整体二分配合 multiset；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.76） |
| [s3-2-J · Polygon II](https://contest.ucup.ac/contest/1699/problem/8526) | S3 Zielona Gora | 概率期望与随机化、动态规划、位运算与状态压缩 | 均匀分布拆二进制，按进位状态做概率 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.160） |
| [s3-2-K · Power Divisions](https://contest.ucup.ac/contest/1699/problem/8527) | S3 Zielona Gora | 动态规划、位运算与状态压缩、概率期望与随机化 | 大整数进位摊还维护，哈希找二的幂区间；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.175） |
| [s3-2-L · Chords](https://contest.ucup.ac/contest/1699/problem/8528) | S3 Zielona Gora | 动态规划、概率期望与随机化 | 区间 DP 选非交叉弦，利用随机弦优化规模；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.212） |
| [s3-2-M · Balance of Permutation](https://contest.ucup.ac/contest/1699/problem/8529) | S3 Zielona Gora | 动态规划、组合计数 | 从左至右配对位置与值，按未配对数量计数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.232） |
| [s3-4-C · Contour Multiplication](https://contest.ucup.ac/contest/1738/problem/9115) | S3 Hongo | 动态规划、位运算与状态压缩 | 扩展快速 Zeta 变换，状态记录不同位数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.16） |
| [s3-4-D · DRD String](https://contest.ucup.ac/contest/1738/problem/9116) | S3 Hongo | 字符串、动态规划、组合计数 | 按最短 border 分解，前缀和优化计数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.20） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | 凸代价分组，堆处理增量并优化 min-plus 卷积；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-J · Japanese Gift Money](https://contest.ucup.ac/contest/1738/problem/9122) | S3 Hongo | 数论、动态规划、贪心 | 贪心货币表示，数位 DP 统计全部偶数张的补集；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.64） |
| [s3-4-O · Optimal Train Operation](https://contest.ucup.ac/contest/1738/problem/9127) | S3 Hongo | 动态规划、数据结构、计算几何 | 转移拆成直线，凸包优化最小代价；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.97） |
| [s3-4-P · Priority Queue 3](https://contest.ucup.ac/contest/1738/problem/9128) | S3 Hongo | 动态规划 | 预设最终阈值，记录已入队数量和最大未选元素；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.104） |
| [s3-4-Q · Quotient Sum](https://contest.ucup.ac/contest/1738/problem/9129) | S3 Hongo | 动态规划、搜索与二分 | 排序后每点只保留两个有效转移，用二分定位；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.109） |
| [s3-5-F · Teleports](https://contest.ucup.ac/contest/1741/problem/9135) | S3 Moscow | 动态规划、图论 | 按区间长度分层，层内 Dijkstra 处理等长转移；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-H · Ancient Country](https://contest.ucup.ac/contest/1741/problem/9137) | S3 Moscow | 动态规划、计算几何 | 区间 DP 选凸多边形，极角顺序优化转移；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-K · Train Depot](https://contest.ucup.ac/contest/1741/problem/9140) | S3 Moscow | 树上算法、动态规划、数据结构 | 树上不交路径 DP，DFS 序区间维护贡献；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-C · -is-this-bitset-](https://contest.ucup.ac/contest/1762/problem/9169) | S3 Osijek | 树上算法、动态规划、位运算与状态压缩 | 浅层构造完整倍数，下层做余数 DP 并撤销更新；[原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-6-H · Game Design](https://contest.ucup.ac/contest/1762/problem/9174) | S3 Osijek | 动态规划、组合计数 | 扫描排列，按未闭合入边出边数计数；[原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-A · Bus Analysis](https://contest.ucup.ac/contest/1774/problem/9220) | S3 Warsaw | 动态规划、组合计数 | 只保留最优费用附近三层，压缩状态统计总费用；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-C · Price Combo](https://contest.ucup.ac/contest/1774/problem/9222) | S3 Warsaw | 动态规划、数据结构 | 交换论证转单调折线，线段树维护转移及奇偶标记；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-J · Juliet Unifies Ones](https://contest.ucup.ac/contest/1774/problem/9229) | S3 Warsaw | 动态规划、字符串 | 按 0、1、0 三段状态求最少删除；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-K · Routing K-Codes](https://contest.ucup.ac/contest/1774/problem/9230) | S3 Warsaw | 树上算法、动态规划 | 根值与子节点二进制关系，换根 DP 求最小编码和；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-A · Welcome to NPCAPC](https://contest.ucup.ac/contest/1804/problem/9435) | S3 Sumiyosi | 动态规划、多项式与线性代数、字符串 | 记录目标子序列匹配长度，矩阵或递推求大长度计数；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) |
| [s3-11-B · Some Sum of Subset](https://contest.ucup.ac/contest/1804/problem/9436) | S3 Sumiyosi | 动态规划、组合计数 | 背包统计子集和小于阈值的方案；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10175) |
| [s3-11-D · Two Box](https://contest.ucup.ac/contest/1804/problem/9438) | S3 Sumiyosi | 动态规划、多项式与线性代数 | 按操作极大段做 DP，二项式变换用卷积加速；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10024) |
| [s3-11-F · Train Seats](https://contest.ucup.ac/contest/1804/problem/9440) | S3 Sumiyosi | 动态规划、数据结构 | 区间 DP 利用最优决策单调性优化；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10270) |
| [s3-11-I · Left Equals Right](https://contest.ucup.ac/contest/1804/problem/9443) | S3 Sumiyosi | 动态规划、组合计数 | 按元素数和左右部分和做计数 DP；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10176) |
| [s3-11-J · Again Permutation Problem](https://contest.ucup.ac/contest/1804/problem/9444) | S3 Sumiyosi | 动态规划、图论、组合计数 | 置换操作连通性分析，小规模 BFS 与逆序对计数 DP；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10019) |
| [s3-11-K · Peace with Magic](https://contest.ucup.ac/contest/1804/problem/9445) | S3 Sumiyosi | 动态规划 | 记录当前位置取值，前后缀最小值优化绝对值转移；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10223) |
| [s3-11-M · Admired Person](https://contest.ucup.ac/contest/1804/problem/9447) | S3 Sumiyosi | 动态规划、贪心 | 排序后做保序最小代价匹配 DP；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10177) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | 贪心决定分组，DSU 合并配合可撤销背包；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-N · 0100 Insertion](https://contest.ucup.ac/contest/1812/problem/9489) | S3 Sendai | 动态规划、字符串 | 记录前缀和及其最小值，统计插入可达串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.68） |
| [s3-18-G · Shrek's Song of the Swamp](https://contest.ucup.ac/contest/1849/problem/9787) | S3 Southeastern Europe | 动态规划、字符串 | 等字符块只需长度二或三，前缀 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.9） |
| [s3-21-D · A xor B plus C](https://contest.ucup.ac/contest/1872/problem/9878) | S3 Ōokayama | 位运算与状态压缩、动态规划 | 按位分析递推周期与进位，用稀疏一位位置列表迭代；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11464) |
| [s3-21-E · ReTravel](https://contest.ucup.ac/contest/1872/problem/9879) | S3 Ōokayama | 动态规划、计算几何 | 区间 DP，按两坐标区间最小值拆分回退路径；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11086) |
| [s3-21-H · Two Convex Sets](https://contest.ucup.ac/contest/1872/problem/9882) | S3 Ōokayama | 计算几何、动态规划 | 按横坐标扫描，两组凸链末端与出现阶段压缩计数 DP；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11084) |
| [s3-24-E · Express Rotations](https://contest.ucup.ac/contest/1890/problem/9963) | S3 Poland | 动态规划、数据结构、图论 | 分阶段最短路，用带偏移的有序表处理负边和长度限制；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.217） |
| [s3-24-H · High Jump](https://contest.ucup.ac/contest/1890/problem/9966) | S3 Poland | 动态规划、计算几何、概率期望与随机化 | 期望 DP 转直线最大值，凸包优化；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.107） |
| [s3-30-B · Glass Stepping Stones](https://contest.ucup.ac/contest/1917/problem/10088) | S3 Northern | 博弈论、动态规划 | 区间端点博弈，刻画可获胜的水平线段；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-30-E · Fractal Maze](https://contest.ucup.ac/contest/1917/problem/10091) | S3 Northern | 动态规划、图论 | 按分形层级递归求路，记忆化关键边界点；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-30-G · Jump the Frog](https://contest.ucup.ac/contest/1917/problem/10093) | S3 Northern | 多项式与线性代数、动态规划 | 每段路径形成转移矩阵，按串结构合成；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-H · Slot Machine](https://contest.ucup.ac/contest/1917/problem/10094) | S3 Northern | 动态规划 | 候选数保持连续区间，双端状态优化最坏代价；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-30-I · Product](https://contest.ucup.ac/contest/1917/problem/10095) | S3 Northern | 动态规划、多项式与线性代数 | 把带权子结构 DP 转为多项式乘法；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.4） |
| [s3-32-B · Gona Guni](https://contest.ucup.ac/contest/1939/problem/10215) | S3 Dhaka | 树上算法、动态规划、组合计数 | 交换求和次序，树形 DP 计数指定顶点属于最小点覆盖；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.1） |
| [s3-32-F · Yet Another Crossover Episode](https://contest.ucup.ac/contest/1939/problem/10219) | S3 Dhaka | 位运算与状态压缩、动态规划 | SOS DP 求存在的最大子掩码及其数量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | 从最小值起安排金字塔两端，区间 DP 合并最少交换；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-I · Unhappy Team](https://contest.ucup.ac/contest/1939/problem/10222) | S3 Dhaka | 概率期望与随机化、动态规划、位运算与状态压缩 | 枚举分数贡献，子集 DP 统计前 k 名入选概率；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.5） |
| [s3-33-B · Bin Packing](https://contest.ucup.ac/contest/1954/problem/10266) | S3 India | 贪心、动态规划 | 优先配满容量十二，剩余四类数量做 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.2） |
| [s3-33-E · Easy Counting Problem](https://contest.ucup.ac/contest/1954/problem/10269) | S3 India | 概率期望与随机化、动态规划、组合计数 | 删除事件线性期望，前缀和递推并转回计数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.5） |
| [s3-33-F · Greedy Prices](https://contest.ucup.ac/contest/1954/problem/10270) | S3 India | 贪心、动态规划 | 交换论证确定购买顺序，乘性增长界压缩购买数量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.7） |
| [s3-33-M · Ticket Revenue Maximization](https://contest.ucup.ac/contest/1954/problem/10277) | S3 India | 贪心、动态规划 | 按强弱排序转合法括号选择，优化收入；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.14） |
| [s3-34-C · 2-Power Rush](https://contest.ucup.ac/contest/1965/problem/10323) | S3 Aobayama | 动态规划、多项式与线性代数 | 按二的幂结构压缩 DP，插值处理大参数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.40） |
| [s3-34-I · Small Steps](https://contest.ucup.ac/contest/1965/problem/10329) | S3 Aobayama | 动态规划 | 按小部件串联推导递推，求一般项；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.63） |
| [s3-35-B · ICFC World Finals](https://contest.ucup.ac/contest/1993/problem/10702) | S3 Kraków | 树上算法、动态规划 | 子树边界框宽高 DP，利用面积上界压缩状态；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-C · Diamonds and the Genie](https://contest.ucup.ac/contest/1993/problem/10703) | S3 Kraków | 动态规划 | 两向网格 DP，枚举唯一逆向移动的局部形态；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.2） |
| [s3-35-H · Decent Path Around Bajtów](https://contest.ucup.ac/contest/1993/problem/10708) | S3 Kraków | 图论、动态规划 | 混合有向无向图分解成树与 DAG，线性统计路径；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-39-G · Guarding Plan](https://contest.ucup.ac/contest/2071/problem/10976) | S3 Tokyo | 计算几何、动态规划、数据结构 | 凸包支配分段，单调队列优化覆盖 DP；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | 前缀平衡分类，笛卡尔树或单调栈优化插入 DP；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-B · Collatz Sum](https://contest.ucup.ac/contest/2135/problem/12151) | S3 Potyczki | 数论、动态规划 | Collatz 变换按奇偶拆成等差数列，递归求和；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.251） |
| [s3-40-C · DNA Subsequences](https://contest.ucup.ac/contest/2135/problem/12152) | S3 Potyczki | 动态规划、搜索与二分、字符串 | 分段费用凸性，参数搜索配合线性 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.2） |
| [s3-40-D · Fern Market](https://contest.ucup.ac/contest/2135/problem/12153) | S3 Potyczki | 动态规划、组合计数 | 静态交易堆策略转前缀平衡，两组 DP 计数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.55） |
| [s3-40-E · One Bit](https://contest.ucup.ac/contest/2135/problem/12154) | S3 Potyczki | 动态规划、位运算与状态压缩 | 只枚举对数距离内的上个保留元素，按 Hamming 距离转移；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.88） |
| [s3-40-G · Furniture](https://contest.ucup.ac/contest/2135/problem/12156) | S3 Potyczki | 动态规划、计算几何 | 按家具高度排序，记录两侧伸出长度的可行状态；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.266） |
| [s3-40-K · Projects](https://contest.ucup.ac/contest/2135/problem/12160) | S3 Potyczki | 动态规划、位运算与状态压缩 | 子集状态及最小正变量数，按二进制层递推线性规划目标；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.171） |
| [s3-40-L · Directed Hanoi](https://contest.ucup.ac/contest/2135/problem/12161) | S3 Potyczki | 图论、动态规划 | 有向 Hanoi 的中间柱容量递推，按可达关系做三重 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.329） |
| [s4-0-B · Circle of Leaf](https://contest.ucup.ac/contest/2041/problem/11357) | S4 America | 树上算法、动态规划、组合计数 | 树形 DP 记录零条或一条尚未截断的叶路径；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.12） |
| [s4-0-H · Ornaments on a Tree](https://contest.ucup.ac/contest/2041/problem/11363) | S4 America | 树上算法、动态规划、贪心 | 自底向上分配权值，保存可向父节点转移的余量；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.32） |
| [s4-1-I · troS XEM](https://contest.ucup.ac/contest/2539/problem/14434) | S4 Korolyov | 动态规划 | 利用长度十七的充分可达界，短转移枚举加长转移摘要；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-2-A · Apple Tree](https://contest.ucup.ac/contest/2551/problem/14130) | S4 Paris | 树上算法、动态规划、组合计数 | 换根维护各距离点数，利用平方根深度界压空间；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-B · Balatro](https://contest.ucup.ac/contest/2551/problem/14131) | S4 Paris | 动态规划 | 按小数值维度把牌拆两组背包，再合并乘积收益；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-D · Digit Division](https://contest.ucup.ac/contest/2551/problem/14133) | S4 Paris | 数论、构造、动态规划 | 移去二五因子，选择倍数数位和做背包或搜索；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.1） |
| [s4-2-E · Euclid in Manhattan](https://contest.ucup.ac/contest/2551/problem/14134) | S4 Paris | 动态规划、计算几何 | 街区拐角 DP，按最优路径结构减少候选转移；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.2） |
| [s4-3-B · Christmas Tree](https://contest.ucup.ac/contest/2559/problem/14416) | S4 Polar | 树上算法、动态规划 | 子树高度状态 DP，后缀最小值优化合并；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-3-E · Maximum Segment Sum](https://contest.ucup.ac/contest/2559/problem/14419) | S4 Polar | 动态规划、组合计数 | 最大后缀和转折返随机游走，组合计数；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-3-F · This Time I Will Be Lucky](https://contest.ucup.ac/contest/2559/problem/14420) | S4 Polar | 概率期望与随机化、动态规划 | 只保留均值附近窄带状态，用浓度界控制误差；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-H · Absolutely Flat](https://contest.ucup.ac/contest/2559/problem/14422) | S4 Polar | 动态规划、数据结构 | 按数值阈值分解 01 问题，利用最优解嵌套性；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-J · One Permutation](https://contest.ucup.ac/contest/2559/problem/14424) | S4 Polar | 动态规划、搜索与二分、数据结构 | LCS 路径凹性，参数二分与树状数组 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-C · Count Triangular Sequences](https://contest.ucup.ac/contest/2668/problem/15446) | S4 Poland | 动态规划、组合计数 | Fibonacci 权重完全背包，按同余类前缀优化；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.102） |
| [s4-8-D · Division with Polylines](https://contest.ucup.ac/contest/2668/problem/15447) | S4 Poland | 动态规划、计算几何 | 对所有候选交点 DP，检查四组范围约束；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.123） |
| [s4-10-C · Connecting Railway Stations](https://contest.ucup.ac/contest/2814/problem/16002) | S4 Wrocław | 树上算法、图论、动态规划 | 树边约束的对偶规划，类 Dijkstra 逐条确定最小值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.67） |
| [s4-10-F · Foxes](https://contest.ucup.ac/contest/2814/problem/16005) | S4 Wrocław | 数据结构、动态规划 | 维护分割指针两侧 LIS，线段树聚合跨侧最优值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.97） |
| [s4-10-G · Game of Darts](https://contest.ucup.ac/contest/2814/problem/16006) | S4 Wrocław | 动态规划 | 投掷分数完全背包，记录转移恢复具体命中序列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.15） |
| [s4-11-F · Language Barrier](https://contest.ucup.ac/contest/2828/problem/16120) | S4 Southeastern Europe | 动态规划、数据结构 | 区间交叠上的 DP，扫描端点维护距离项最小值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.6） |
| [s4-11-G · Intervals from Triplets](https://contest.ucup.ac/contest/2828/problem/16121) | S4 Southeastern Europe | 动态规划、贪心 | 按三元组中点排序，记录最早和最晚结尾两状态；[原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.7） |
| [s4-13-C · Sum of Three Inversions](https://contest.ucup.ac/contest/2921/problem/16228) | S4 Ōokayama | 动态规划、组合计数 | 六种三元排列分两组，计数 DP 合并逆序贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.4） |
| [s4-16-C · Copy-paste](https://contest.ucup.ac/contest/3347/problem/17152) | S4 Warsaw | 数论、动态规划 | 逆向删除或除法，只枚举小质因子并记忆化最少操作；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.5） |
| [s4-16-E · Evaluation](https://contest.ucup.ac/contest/3347/problem/17154) | S4 Warsaw | 动态规划、字符串 | 扫描表达式，维护已完成项、未完成乘项和当前因子总和；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.7） |
| [s4-16-H · House](https://contest.ucup.ac/contest/3347/problem/17157) | S4 Warsaw | 搜索与二分、动态规划 | 二分面积，枚举长边后按每根木料分组背包；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.11） |
| [s4-18-B · Binary Tree Counting](https://contest.ucup.ac/contest/3420/problem/17247) | S4 Hongō | 树上算法、动态规划、组合计数 | 二叉树转有序树与路径，在关键点树上 DP；[原文](https://atcoder.jp/contests/utpc2025/editorial/15693) |
| [s4-18-E · Exchange or Not](https://contest.ucup.ac/contest/3420/problem/17250) | S4 Hongō | 动态规划、组合计数 | 按不交换位置分段，差分累加前缀计数；[原文](https://atcoder.jp/contests/utpc2025/editorial/16127) |
| [s4-19-B · Building a Reactor](https://contest.ucup.ac/contest/3426/problem/17261) | S4 Belarus | 动态规划、位运算与状态压缩 | 三进制轮廓 DP 覆盖燃料棒，最小化冷却元件；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.1） |
| [s4-19-I · Ivan Tsarevich in the Magical Grove](https://contest.ucup.ac/contest/3426/problem/17268) | S4 Belarus | 图论、动态规划、位运算与状态压缩 | 连通分量两种染色数，分组 bitset 背包判断可选顶点；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-20-B · Palindrome and Permutation](https://contest.ucup.ac/contest/3516/problem/17407) | S4 India | 图论、动态规划、组合计数 | 对称位置建伪森林，树分量选根计数 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.3） |
| [s4-20-D · Merging Maximum](https://contest.ucup.ac/contest/3516/problem/17409) | S4 India | 动态规划、数据结构 | 按最短末段规范去重，单调结构优化奇长最大值划分；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.7） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | 两子序列可达状态 DP，逐位贪心最小化最大串；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-20-F · Restricted Removals](https://contest.ucup.ac/contest/3516/problem/17411) | S4 India | 动态规划、数据结构 | 分块代价 DP，单调栈合并同最大值转移组；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.9） |
| [s4-20-G · Sequence Domination](https://contest.ucup.ac/contest/3516/problem/17412) | S4 India | 动态规划、组合计数 | 差序列转带饱和上界状态，前缀和优化加权转移；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.10） |
| [s4-20-J · Counting Is Fun](https://contest.ucup.ac/contest/3516/problem/17415) | S4 India | 动态规划、组合计数 | 排序后每个前缀仅线性种得分，逐元素计数；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.16） |
| [s4-21-F · Increase Decrease](https://contest.ucup.ac/contest/3542/problem/17424) | S4 Kamigō | 构造、动态规划 | LIS、LDS 二维网格嵌入，贪心恢复指定前缀长度；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18127) |
| [s4-21-H · OR Preference](https://contest.ucup.ac/contest/3542/problem/17426) | S4 Kamigō | 位运算与状态压缩、动态规划、贪心 | 交换论证把 OR 放在 AND 前，前缀掩码 DP；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) |
| [s4-21-I · Penguin Flicker](https://contest.ucup.ac/contest/3542/problem/17427) | S4 Kamigō | 动态规划、多项式与线性代数 | 有环期望转三对角线性方程，逐层消元；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18125) |
| [s4-22-B · Cat Cut](https://contest.ucup.ac/contest/3575/problem/17714) | S4 Kyoto | 字符串、动态规划 | 按最终后缀形态拆分，DP 求最小字典序前缀拼接；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.1） |
| [s4-22-G · The Symbolic Tree](https://contest.ucup.ac/contest/3575/problem/17719) | S4 Kyoto | 树上算法、动态规划、多项式与线性代数 | 树形前缀和 DP 的多项式性，用插值处理大 K；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.6） |
| [s4-25-G · Grid Gradient](https://contest.ucup.ac/contest/3773/problem/18407) | S4 Zagreb | 动态规划、位运算与状态压缩 | 固定网格奇偶性后，轮廓 DP 统计可修改集合；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.27） |
| [s4-Extra-3-D · Electi Lamps](https://contest.ucup.ac/contest/2757/problem/15520) | S4 Osijek | 动态规划、数据结构 | 单调栈预处理覆盖端点，贪心最早有效 DP 转移；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-E · XOR Again?](https://contest.ucup.ac/contest/2757/problem/15521) | S4 Osijek | 位运算与状态压缩、动态规划 | 按位确定使 OR 出现的切点区间，再统计划分；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s5-1-A · Astana Hard Metro](https://contest.ucup.ac/contest/4126/problem/20248) | S5 Nizhny Novgorod | 动态规划、概率期望与随机化、组合计数 | 随机树父节点选择转球盒模型，记录待配红点与叶数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.1） |
| [s5-1-G · Game Show: XOR Edition](https://contest.ucup.ac/contest/4126/problem/20254) | S5 Nizhny Novgorod | 位运算与状态压缩、动态规划、概率期望与随机化 | 按最高位分组，少量随机代表做异或 DP 构造目标值；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.13） |
| [s5-1-M · Minecraft Spiderweb](https://contest.ucup.ac/contest/4126/problem/20260) | S5 Nizhny Novgorod | 计算几何、动态规划 | 矩形边界终端的直角 Steiner 树，枚举结构拓扑并优化；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.24） |
| [s5-6-A · Fugaku NK-kei](https://contest.ucup.ac/contest/4617/problem/23669) | S5 Hyakumanben | 动态规划、组合计数 | 按首元素确定根，左右独立分解再容斥处理环；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.1） |
| [s5-6-C · Moving Silver](https://contest.ucup.ac/contest/4617/problem/23671) | S5 Hyakumanben | 博弈论、动态规划 | max-min 网格算子迭代，证明半高步后稳定；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.6） |
| [s5-6-D · Go Robots](https://contest.ucup.ac/contest/4617/problem/23672) | S5 Hyakumanben | 图论、动态规划 | 按拓扑序累加机器人经过数，奇偶决定开关流向；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.8） |
| [s5-6-H · Please Insert Coin](https://contest.ucup.ac/contest/4617/problem/23676) | S5 Hyakumanben | 动态规划、数据结构 | 仅更新障碍附近 DP，线段树维护移动代价下包络；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.12） |
| [s5-6-K · Dyads of Hanoi](https://contest.ucup.ac/contest/4617/problem/23679) | S5 Hyakumanben | 动态规划、组合计数 | Hanoi 最短路分两类，差值只保留负一零一的有限状态；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.19） |
