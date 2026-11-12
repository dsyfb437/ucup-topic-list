# 数据结构

146 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-J · Jewel of Data Structure Problems](https://contest.ucup.ac/contest/1106/problem/5526) | S1 Ukraine | 位运算与状态压缩、数据结构 | 维护排列奇偶性和位置同奇偶计数；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.7） |
| [s1-8-A · Bandits](https://contest.ucup.ac/contest/1070/problem/5249) | S1 Slovenia | 树上算法、数据结构 | 点分治维护带半径的覆盖贡献；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.14） |
| [s1-8-C · Constellations](https://contest.ucup.ac/contest/1070/problem/5251) | S1 Slovenia | 数据结构、计算几何 | 优先队列维护聚类距离，合并后更新；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.5） |
| [s1-8-J · Mortgage](https://contest.ucup.ac/contest/1070/problem/5258) | S1 Slovenia | 数据结构、计算几何、搜索与二分 | 区间下包络与凸包上二分查询；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.12） |
| [s1-12-N · XOR Reachable](https://contest.ucup.ac/contest/1207/problem/6330) | S1 Ōokayama | 数据结构、图论、位运算与状态压缩 | 异或条件拆成区间，时间分治与可撤销并查集；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.9） |
| [s1-16-C · Classical Data Structure Problem](https://contest.ucup.ac/contest/1223/problem/6409) | S1 Gomel | 数据结构 | 动态区间分裂配合 AVL 或 Splay 旋转保持平衡；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.2） |
| [s1-16-I · Classical Minimization Problem](https://contest.ucup.ac/contest/1223/problem/6415) | S1 Gomel | 贪心、数据结构 | 优先处理点数最多的横纵线并配对；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.4） |
| [s1-16-J · Classical Scheduling Problem](https://contest.ucup.ac/contest/1223/problem/6416) | S1 Gomel | 贪心、搜索与二分、数据结构 | 二分目标数量，堆维护前后缀最小代价；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-A · Maximum Bitwise OR](https://contest.ucup.ac/contest/1259/problem/6631) | S1 India | 位运算与状态压缩、数据结构 | 最高位刻画可达 OR，区间统计最少变换；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.2） |
| [s1-20-C · Exam Requirements](https://contest.ucup.ac/contest/1259/problem/6633) | S1 India | 图论、数据结构 | 区间相交建图，线段树辅助节点压缩边；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.10） |
| [s1-20-I · Disk Tree](https://contest.ucup.ac/contest/1259/problem/6639) | S1 India | 计算几何、数据结构 | 扫描线维护活跃圆，按上下关系连接；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.32） |
| [s2-2-G · Graph Cuts](https://contest.ucup.ac/contest/1356/problem/7181) | S2 SPb | 数据结构、图论 | 按度数分轻重，分块或 bitset 维护跨集合边；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.20） |
| [s2-2-H · Very Sparse Table](https://contest.ucup.ac/contest/1356/problem/7182) | S2 SPb | 数据结构 | 递归分块与前后缀积，压缩幺半群区间查询；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.32） |
| [s2-2-K · Poor Students](https://contest.ucup.ac/contest/1356/problem/7185) | S2 SPb | 图论、数据结构 | 费用流增广路径压成课程图，集合维护转课代价；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.7） |
| [s2-5-H · Shared Memory Switch](https://contest.ucup.ac/contest/1388/problem/6553) | S2 Northern | 贪心、数据结构 | 离线预知发送时间，堆淘汰最晚发送的包；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.45） |
| [s2-5-K · Text Editor](https://contest.ucup.ac/contest/1388/problem/6556) | S2 Northern | 数据结构、字符串 | 可持久化 Treap，节点存原输入字符串切片；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.49） |
| [s2-6-C · Cliques](https://contest.ucup.ac/contest/1398/problem/7608) | S2 Warsaw | 树上算法、数据结构、组合计数 | 树上路径 Helly 性质，维护点及父边覆盖数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.2） |
| [s2-6-F · Max-Min](https://contest.ucup.ac/contest/1398/problem/7611) | S2 Warsaw | 数据结构 | 维护左右更大值及其对子段最大值和的贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.3） |
| [s2-6-K · Jump Graph](https://contest.ucup.ac/contest/1398/problem/7616) | S2 Warsaw | 图论、数据结构 | 区间可达集合压缩，链表或 DSU 跳过已处理位置；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-6-L · Spectacle](https://contest.ucup.ac/contest/1398/problem/7617) | S2 Warsaw | 贪心、数据结构 | 相邻差排序激活，DSU 维护分量可配对数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-7-J · Range Sets](https://contest.ucup.ac/contest/1399/problem/7641) | S2 Two Capitals | 数据结构 | 有序区间集合配合动态开点线段树维护答案；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.7） |
| [s2-14-F · Fast XORting](https://contest.ucup.ac/contest/1452/problem/7937) | S2 Southeastern Europe | 位运算与状态压缩、数据结构 | 异或各位独立，按逆序对变化选择每一位；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.7） |
| [s2-14-H · High Towers](https://contest.ucup.ac/contest/1452/problem/7939) | S2 Southeastern Europe | 构造、数据结构 | 从可见塔数量恢复递增栈并递归分段；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.9） |
| [s2-14-K · $K$ Subsequences](https://contest.ucup.ac/contest/1452/problem/7942) | S2 Southeastern Europe | 贪心、数据结构 | 正一给当前和最小的序列，负一给最大的；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.12） |
| [s2-14-M · Max Minus Min](https://contest.ucup.ac/contest/1452/problem/7944) | S2 Southeastern Europe | 搜索与二分、数据结构 | 二分极差，区间内外最大最小值判可行；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.14） |
| [s2-18-D · Dinosaur Bones Digging](https://contest.ucup.ac/contest/1475/problem/8006) | S2 Dolgoprudny | 数据结构 | 扫描值域，线段树维护候选区间内更大元素个数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.2） |
| [s2-18-E · Egg Drop Challenge](https://contest.ucup.ac/contest/1475/problem/8007) | S2 Dolgoprudny | 动态规划、数据结构 | DP 转移函数取下包络，类李超树维护；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.3） |
| [s2-18-J · Jumping Lights](https://contest.ucup.ac/contest/1475/problem/8012) | S2 Dolgoprudny | 树上算法、数据结构 | 维护未标记子节点，势能分析摊还更新；[原文](https://assets.ucup.ac/tutorials/tutorials-2-18.pdf)（文件 p.6） |
| [s2-19-F · When Anton Saw This Task He Reacted With 😩](https://contest.ucup.ac/contest/1487/problem/8133) | S2 Estonia | 多项式与线性代数、数据结构 | 把向量运算转成矩阵乘积，线段树维护结合运算；[原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.9） |
| [s2-20-D · Spacecraft](https://contest.ucup.ac/contest/1499/problem/8168) | S2 Ōokayama | 计算几何、数据结构 | 球面区域化为三维半空间交，DSU 统计连通块；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.3） |
| [s2-20-H · 404 Chotto Found](https://contest.ucup.ac/contest/1499/problem/8172) | S2 Ōokayama | 字符串、数据结构 | 后缀数组与 LCP 排除多串公共子串；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.9） |
| [s2-26-H · Harmonic Operations](https://contest.ucup.ac/contest/1576/problem/8512) | S2 Latin America | 字符串、数据结构 | KMP 提取最小周期，维护旋转和插入的组合摘要；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.9） |
| [s3-0-H · MountainCraft](https://contest.ucup.ac/contest/1695/problem/8775) | S3 America | 数据结构、计算几何 | 线段树维护最低覆盖次数与被覆盖长度；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.16） |
| [s3-0-K · Shadow Line](https://contest.ucup.ac/contest/1695/problem/8778) | S3 America | 计算几何、数据结构 | 扫描投影端点交换事件，维护前缀平衡性；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.22） |
| [s3-1-A · Element-Wise Comparison](https://contest.ucup.ac/contest/1696/problem/8781) | S3 St. Petersburg | 位运算与状态压缩、数据结构 | 比较矩阵 bitset 化，分块前后缀 OR；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.2） |
| [s3-1-C · Cherry Picking](https://contest.ucup.ac/contest/1696/problem/8783) | S3 St. Petersburg | 数据结构 | 分治子段和或 DSU 激活，避免错误二分；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.44） |
| [s3-1-K · Tasks and Bugs](https://contest.ucup.ac/contest/1696/problem/8791) | S3 St. Petersburg | 模拟与基础实现、数据结构 | 映射聚合任务与 bug，按数值顺序输出；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.187） |
| [s3-1-M · Toilets](https://contest.ucup.ac/contest/1696/problem/8793) | S3 St. Petersburg | 数据结构、模拟与基础实现 | 有序集合维护最近候选，事件模拟如厕分配；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.210） |
| [s3-2-B · Roars III](https://contest.ucup.ac/contest/1699/problem/8518) | S3 Zielona Gora | 树上算法、数据结构 | 线段树维护最深 token，换根时撤销局部移动；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.13） |
| [s3-2-F · Waterfall Matrix](https://contest.ucup.ac/contest/1699/problem/8522) | S3 Zielona Gora | 动态规划、数据结构 | 阈值最优边界单调，整体二分配合 multiset；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.76） |
| [s3-2-G · Puzzle II](https://contest.ucup.ac/contest/1699/problem/8523) | S3 Zielona Gora | 构造、数据结构 | 双滑动窗口构造互补区间；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.102） |
| [s3-2-I · Mercenaries](https://contest.ucup.ac/contest/1699/problem/8525) | S3 Zielona Gora | 计算几何、数据结构 | 线段树维护凸包与 Minkowski 和，支持点半平面查询；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.134） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | 凸代价分组，堆处理增量并优化 min-plus 卷积；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-K · Kth Sum](https://contest.ucup.ac/contest/1738/problem/9123) | S3 Hongo | 搜索与二分、数据结构 | 二分第 k 小三元和，堆预处理候选二元和；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.76） |
| [s3-4-O · Optimal Train Operation](https://contest.ucup.ac/contest/1738/problem/9127) | S3 Hongo | 动态规划、数据结构、计算几何 | 转移拆成直线，凸包优化最小代价；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.97） |
| [s3-5-C · Painting Fences](https://contest.ucup.ac/contest/1741/problem/9132) | S3 Moscow | 数据结构、贪心 | 笛卡尔树枚举极大黑矩形，分析倍增扩展；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-K · Train Depot](https://contest.ucup.ac/contest/1741/problem/9140) | S3 Moscow | 树上算法、动态规划、数据结构 | 树上不交路径 DP，DFS 序区间维护贡献；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-6-D · Cycle Game](https://contest.ucup.ac/contest/1762/problem/9170) | S3 Osijek | 数据结构、图论 | 线段树分治与可撤销 DSU 维护八连通关系；[原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-6-G · Touching Grass](https://contest.ucup.ac/contest/1762/problem/9173) | S3 Osijek | 计算几何、数据结构 | 区间凸包查询，离线分治与斜率排序双指针；[原文](https://qoj.ac/blog/jiangly/blogs/948) |
| [s3-7-C · Price Combo](https://contest.ucup.ac/contest/1774/problem/9222) | S3 Warsaw | 动态规划、数据结构 | 交换论证转单调折线，线段树维护转移及奇偶标记；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-F · Train Seats](https://contest.ucup.ac/contest/1804/problem/9440) | S3 Sumiyosi | 动态规划、数据结构 | 区间 DP 利用最优决策单调性优化；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10270) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | 贪心决定分组，DSU 合并配合可撤销背包；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-H · Maximize Array](https://contest.ucup.ac/contest/1812/problem/9483) | S3 Sendai | 贪心、数据结构 | 按同余位置的前缀最大值，依次最大化字典序；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.41） |
| [s3-18-K · Intrusive Donkey](https://contest.ucup.ac/contest/1849/problem/9791) | S3 Southeastern Europe | 数据结构 | 按相同值压成组，线段树倍增组长与第 k 项查询；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.14） |
| [s3-18-L · Ogre Sort](https://contest.ucup.ac/contest/1849/problem/9792) | S3 Southeastern Europe | 贪心、数据结构 | 按必要前移顺序构造，树状数组维护当前位置；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.15） |
| [s3-18-M · Enchanted Lawns Quest](https://contest.ucup.ac/contest/1849/problem/9793) | S3 Southeastern Europe | 树上算法、搜索与二分、数据结构 | 二分树直径，以中心点或中心边统计可增加权值；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.16） |
| [s3-21-C · Segment Tree](https://contest.ucup.ac/contest/1872/problem/9877) | S3 Ōokayama | 数据结构、图论 | 层次图最短路摘要，沿线段树祖先更新；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11291) |
| [s3-21-K · Sum is One](https://contest.ucup.ac/contest/1872/problem/9885) | S3 Ōokayama | 图论、数据结构 | 将共享三元组的等价关系压成线性条边，用 DSU 数分量；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11225) |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | Cartesian 树括号哈希，双向扫描线段树统计不同子树形态；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-24-E · Express Rotations](https://contest.ucup.ac/contest/1890/problem/9963) | S3 Poland | 动态规划、数据结构、图论 | 分阶段最短路，用带偏移的有序表处理负边和长度限制；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.217） |
| [s3-24-J · Just Zeros](https://contest.ucup.ac/contest/1890/problem/9968) | S3 Poland | 位运算与状态压缩、数据结构 | 枚举行翻转掩码，维护各列最优翻转代价；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.94） |
| [s3-27-B · The Best Wife](https://contest.ucup.ac/contest/1901/problem/8612) | S3 London | 数据结构、贪心 | 删包含区间后维护贪心跳转森林，LCT 或持久化线段树；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-C · Cardinality](https://contest.ucup.ac/contest/1901/problem/8613) | S3 London | 概率期望与随机化、位运算与状态压缩、数据结构 | 小集合显式存储，大集合采样 bitset 或 MinHash；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-H · Have You Seen This Subarray?](https://contest.ucup.ac/contest/1901/problem/8618) | S3 London | 数据结构、概率期望与随机化 | 记录相邻数对的出现时间区间，查询时求交；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.2） |
| [s3-27-K · Knapsack](https://contest.ucup.ac/contest/1901/problem/8621) | S3 London | 搜索与二分、概率期望与随机化、数据结构 | Karmarkar-Karp 差分合并，随机重启；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | 贪心消去冗余回文，维护对数个活跃回文；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-31-F · Flats](https://contest.ucup.ac/contest/1924/problem/10119) | S3 Wroclaw | 数据结构、计算几何 | 线段树求矩形下落高度，扫描接触边；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.44） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | 从最小值起安排金字塔两端，区间 DP 合并最少交换；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-32-M · Tree Flip](https://contest.ucup.ac/contest/1939/problem/10226) | S3 Dhaka | 树上算法、数据结构、位运算与状态压缩 | 点分治维护路径异或，支持变根和点修改；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.7） |
| [s3-33-G · Lexicographic Raffle](https://contest.ucup.ac/contest/1954/problem/10271) | S3 India | 字符串、数据结构 | 相邻差异决定字典序，维护关键位置贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.8） |
| [s3-33-H · Majority Graph](https://contest.ucup.ac/contest/1954/problem/10272) | S3 India | 图论、数据结构 | 多数区间隐式建边，差分维护后 BFS 统计分量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.9） |
| [s3-33-I · Majority Voters](https://contest.ucup.ac/contest/1954/problem/10273) | S3 India | 数据结构 | 前缀平衡转线段树最大前缀和查询；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.10） |
| [s3-33-K · P to Q](https://contest.ucup.ac/contest/1954/problem/10275) | S3 India | 构造、数据结构 | 经单位排列中转，保持逆序对不超端点上界；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.12） |
| [s3-33-L · Score Sum](https://contest.ucup.ac/contest/1954/problem/10276) | S3 India | 数据结构 | 按下次出现位置的前缀最大值统计可删长度；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.13） |
| [s3-34-B · Matching Query](https://contest.ucup.ac/contest/1965/problem/10322) | S3 Aobayama | 数据结构、图论 | 匹配转整数规划，线段树维护环上流量约束；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.52） |
| [s3-34-J · Median Operations](https://contest.ucup.ac/contest/1965/problem/10330) | S3 Aobayama | 贪心、数据结构 | 阈值化为 01 串，线段树维护三字符边界摘要；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.68） |
| [s3-35-A · Suspicious Submissions](https://contest.ucup.ac/contest/1993/problem/10701) | S3 Kraków | 字符串、数据结构 | 正反 Trie 建字典序坐标，离线二维或三维数点；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-G · Road Trip](https://contest.ucup.ac/contest/1993/problem/10707) | S3 Kraków | 树上算法、数据结构 | 倍增记录路径最后加油点，LCA 合并两段路径；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.6） |
| [s3-35-I · Random Remainders](https://contest.ucup.ac/contest/1993/problem/10709) | S3 Kraków | 数论、概率期望与随机化、数据结构 | 排序后按整除商分段，前缀幂和计算余数平方；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-35-J · Sumotonic Sequences](https://contest.ucup.ac/contest/1993/problem/10710) | S3 Kraków | 数据结构 | 差分转非负约束，区间维护负值和；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.7） |
| [s3-39-A · Array Similarity](https://contest.ucup.ac/contest/2071/problem/10970) | S3 Tokyo | 数据结构、概率期望与随机化 | 单调后继链，倍增哈希比较区间前缀最大位置；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-G · Guarding Plan](https://contest.ucup.ac/contest/2071/problem/10976) | S3 Tokyo | 计算几何、动态规划、数据结构 | 凸包支配分段，单调队列优化覆盖 DP；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | 前缀平衡分类，笛卡尔树或单调栈优化插入 DP；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-P · Perfect Suika Game on a Tree](https://contest.ucup.ac/contest/2071/problem/10985) | S3 Tokyo | 树上算法、数据结构、位运算与状态压缩 | 持久化线段树合并大二进制数，局部维护可合并条件；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-N · Frequency Function](https://contest.ucup.ac/contest/2135/problem/12163) | S3 Potyczki | 数据结构 | 维护有限层频次变换，按层合并受影响位置更新；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.224） |
| [s4-0-E · Humans vs AI](https://contest.ucup.ac/contest/2041/problem/11360) | S4 America | 数据结构 | 前缀和差分转离线数点，树状数组统计子数组；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.19） |
| [s4-0-G · Most Scenic Cycle](https://contest.ucup.ac/contest/2041/problem/11362) | S4 America | 图论、数据结构 | 利用区域环基结构，队列维护收缩与重边合并；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.25） |
| [s4-1-F · Yet Another MST Problem](https://contest.ucup.ac/contest/2539/problem/14431) | S4 Korolyov | 图论、数据结构 | 按 mex 权值模拟 Kruskal，合并不含当前值的区间；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-1-H · Misread Problem](https://contest.ucup.ac/contest/2539/problem/14433) | S4 Korolyov | 贪心、数据结构 | 凸函数差分斜率集合，slope trick 求固定总和最小代价；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-1-K · Robot Construction](https://contest.ucup.ac/contest/2539/problem/14436) | S4 Korolyov | 数据结构 | 离线右端点扫描，线段树分段赋值、减法和下降查询；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.4） |
| [s4-2-J · JamBrains](https://contest.ucup.ac/contest/2551/problem/14139) | S4 Paris | 数据结构、搜索与二分 | 线段树维护行长和及前缀最小值，二分放置位置；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.5） |
| [s4-2-K · $k$ Operations](https://contest.ucup.ac/contest/2551/problem/14140) | S4 Paris | 贪心、数据结构 | 按值从小到大减少，排序前缀和定位最后一段；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-3-C · Roman Numerals](https://contest.ucup.ac/contest/2559/problem/14417) | S4 Polar | 数据结构、字符串 | 最大值笛卡尔树分解罗马数字区间，离线维护前后缀值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-3-D · Disjoint Set Splitting](https://contest.ucup.ac/contest/2559/problem/14418) | S4 Polar | 数据结构、图论 | 先假定回答求删边时间，逆序加边 DSU 验证；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.3） |
| [s4-3-H · Absolutely Flat](https://contest.ucup.ac/contest/2559/problem/14422) | S4 Polar | 动态规划、数据结构 | 按数值阈值分解 01 问题，利用最优解嵌套性；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.4） |
| [s4-3-J · One Permutation](https://contest.ucup.ac/contest/2559/problem/14424) | S4 Polar | 动态规划、搜索与二分、数据结构 | LCS 路径凹性，参数二分与树状数组 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-B · Beats](https://contest.ucup.ac/contest/2668/problem/15445) | S4 Poland | 贪心、数据结构 | 枚举移走后缀，双端队列维护可保留的递增子序列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.51） |
| [s4-8-E · Enigma](https://contest.ucup.ac/contest/2668/problem/15448) | S4 Poland | 图论、数据结构 | 十万个密码状态，增量 BFS 只松弛变小距离；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.93） |
| [s4-8-L · Linear Averaging](https://contest.ucup.ac/contest/2668/problem/15455) | S4 Poland | 数据结构 | 前缀和与区间最值，求各元素可达到的最小最大平均数；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.113） |
| [s4-10-A · Automatized Mineral Classification](https://contest.ucup.ac/contest/2814/problem/16000) | S4 Wrocław | 交互与信息编码、概率期望与随机化、数据结构 | 随机队列合并同色元素，生日悖论分析询问量；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.45） |
| [s4-10-F · Foxes](https://contest.ucup.ac/contest/2814/problem/16005) | S4 Wrocław | 数据结构、动态规划 | 维护分割指针两侧 LIS，线段树聚合跨侧最优值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.97） |
| [s4-11-F · Language Barrier](https://contest.ucup.ac/contest/2828/problem/16120) | S4 Southeastern Europe | 动态规划、数据结构 | 区间交叠上的 DP，扫描端点维护距离项最小值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.6） |
| [s4-13-A · Depth of Interval](https://contest.ucup.ac/contest/2921/problem/16226) | S4 Ōokayama | 数据结构 | 层状最小次小位置对分解，线段树跳过值域空层；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.1） |
| [s4-13-E · Max Twice Subsequences](https://contest.ucup.ac/contest/2921/problem/16230) | S4 Ōokayama | 数据结构 | 维护 next-occurrence 与双调栈，摊还更新最优两次子序列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.6） |
| [s4-13-I · Subgrid Connected Components](https://contest.ucup.ac/contest/2921/problem/16234) | S4 Ōokayama | 图论、数据结构 | 平面图 Euler 公式，区域代表点前缀和加边界修正；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.15） |
| [s4-13-M · Many Approaches](https://contest.ucup.ac/contest/2921/problem/16238) | S4 Ōokayama | 数据结构 | 相邻人距离恒为零或一，线段树二分与局部更新；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.22） |
| [s4-16-D · Deque Sort](https://contest.ucup.ac/contest/3347/problem/17153) | S4 Warsaw | 数据结构、贪心 | 每阶段拆前缀最大值序列，维护其长度与翻转；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.6） |
| [s4-16-G · Good Permutations](https://contest.ucup.ac/contest/3347/problem/17156) | S4 Warsaw | 数据结构、组合计数 | 下降块由固定值确定，区间最值验证端点兼容；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.9） |
| [s4-17-C · String Workshop](https://contest.ucup.ac/contest/3384/problem/17163) | S4 St. Petersburg | 数据结构、字符串、组合计数 | 稳定排序的必经逆序交叉，离线统计带权贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.2） |
| [s4-17-G · Traffic Lights](https://contest.ucup.ac/contest/3384/problem/17167) | S4 St. Petersburg | 树上算法、数据结构 | Euler 序与 LCA，维护经过指定点的异色端点最短路；[原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.5） |
| [s4-17-I · Wooden Checker](https://contest.ucup.ac/contest/3384/problem/17169) | S4 St. Petersburg | 图论、数据结构 | DSU 检查森林和入度，合并时验证邻接编号连续区间；[原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.8） |
| [s4-18-F · Finite Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17251) | S4 Hongō | 字符串、数据结构 | 左右括号个数相等当且仅当无限，前缀和回答区间；[原文](https://atcoder.jp/contests/utpc2025/editorial/15692) |
| [s4-18-G · Greatest Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17252) | S4 Hongō | 字符串、数据结构、搜索与二分 | 最长合法括号后缀结构，并行二分定位字典序最优；[原文](https://atcoder.jp/contests/utpc2025/editorial/16136) |
| [s4-19-G · Guaranteed Medal](https://contest.ucup.ac/contest/3426/problem/17266) | S4 Belarus | 模拟与基础实现、数据结构 | 按提交顺序模拟判题与罚时，map 维护队伍成绩；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.4） |
| [s4-19-J · Jolly Wheel](https://contest.ucup.ac/contest/3426/problem/17269) | S4 Belarus | 数据结构 | 旋转拆成全圈和两段区间加，扫描线或线段树求覆盖；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.6） |
| [s4-19-K · Kitchen](https://contest.ucup.ac/contest/3426/problem/17270) | S4 Belarus | 模拟与基础实现、数据结构 | 优先队列维护蟑螂吃诱饵事件；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-19-M · May We Answer Your Questions Right?](https://contest.ucup.ac/contest/3426/problem/17272) | S4 Belarus | 数据结构 | 线段树维护幂二因子与截断余项，避免数值无限增长；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-20-C · Score Queries](https://contest.ucup.ac/contest/3516/problem/17408) | S4 India | 数据结构 | 单调栈生成合法左右端点矩形，扫描线统计查询；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.5） |
| [s4-20-D · Merging Maximum](https://contest.ucup.ac/contest/3516/problem/17409) | S4 India | 动态规划、数据结构 | 按最短末段规范去重，单调结构优化奇长最大值划分；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.7） |
| [s4-20-F · Restricted Removals](https://contest.ucup.ac/contest/3516/problem/17411) | S4 India | 动态规划、数据结构 | 分块代价 DP，单调栈合并同最大值转移组；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.9） |
| [s4-20-H · Maximum Difference](https://contest.ucup.ac/contest/3516/problem/17413) | S4 India | 数据结构 | 值域线段树维护有序块与最长缺值间隔；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.12） |
| [s4-20-K · Prefix MEX Equation](https://contest.ucup.ac/contest/3516/problem/17416) | S4 India | 数据结构 | 维护首末出现位置，线段树找最早破坏 mex 条件的值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.18） |
| [s4-21-E · Find "rururutata"](https://contest.ucup.ac/contest/3542/problem/17423) | S4 Kamigō | 字符串、数据结构 | 倍增无碰撞哈希或 LCP，检测三重重复段；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17002) |
| [s4-22-D · Campaign Speech](https://contest.ucup.ac/contest/3575/problem/17716) | S4 Kyoto | 计算几何、数据结构 | 沿多边形边界扫描，集合或坐标排序定位演讲点；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.4） |
| [s4-22-M · Linked VERSE](https://contest.ucup.ac/contest/3575/problem/17725) | S4 Kyoto | 数据结构、计算几何 | small-to-large 合并上凸包，动态维护最优线性函数；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.10） |
| [s4-25-A · Arrow Array](https://contest.ucup.ac/contest/3773/problem/18401) | S4 Zagreb | 贪心、数据结构 | 维护前缀可行上下界，平移约束后线性判定；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.2） |
| [s4-25-B · Big Balls](https://contest.ucup.ac/contest/3773/problem/18402) | S4 Zagreb | 树上算法、数据结构 | 碰撞合并事件建树，区间用边界叶 LCA 定位；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.7） |
| [s4-25-E · Exchange Error](https://contest.ucup.ac/contest/3773/problem/18405) | S4 Zagreb | 数据结构、计算几何 | 分块与前缀和直线凸包，离线双指针查询；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.18） |
| [s4-25-K · Kempt Kale](https://contest.ucup.ac/contest/3773/problem/18411) | S4 Zagreb | 贪心、数据结构、组合计数 | 合法括号位置的拟阵贪心，按收益从大到小选；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.42） |
| [s4-25-M · Maximum Mex](https://contest.ucup.ac/contest/3773/problem/18413) | S4 Zagreb | 树上算法、搜索与二分、数据结构 | 二分 mex，树上分治配合线段树维护路径不同值数；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.49） |
| [s4-Extra-3-D · Electi Lamps](https://contest.ucup.ac/contest/2757/problem/15520) | S4 Osijek | 动态规划、数据结构 | 单调栈预处理覆盖端点，贪心最早有效 DP 转移；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-I · Bobs Rating](https://contest.ucup.ac/contest/2757/problem/15525) | S4 Osijek | 树上算法、数据结构 | Kruskal 重构树，倍增与 LCA 处理评级跨边查询；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s4-Extra-3-J · AND Components](https://contest.ucup.ac/contest/2757/problem/15526) | S4 Osijek | 数据结构、位运算与状态压缩 | 线段树保存各位首次末次出现，合并 AND 连通分量摘要；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-1-C · Cost of Conflicts](https://contest.ucup.ac/contest/4126/problem/20250) | S5 Nizhny Novgorod | 图论、数据结构 | Borůvka 各分量最小出边，扫描线处理冲突矩形加；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.5） |
| [s5-1-F · Fresh Cartridges](https://contest.ucup.ac/contest/4126/problem/20253) | S5 Nizhny Novgorod | 多项式与线性代数、概率期望与随机化、数据结构 | 两独立集并集随机表示成单一线性拟阵，带时间戳基回答区间秩；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.11） |
| [s5-1-H · Hockey Hog](https://contest.ucup.ac/contest/4126/problem/20255) | S5 Nizhny Novgorod | 计算几何、数据结构 | 凸多边形可见性转环形区间，双指针与线段树扫描；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.15） |
| [s5-3-B · Binary Rotations](https://contest.ucup.ac/contest/4565/problem/20730) | S5 Gorkovskaya | 树上算法、数据结构、组合计数 | 二叉树旋转转括号向量支配，折半投影统计；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.2） |
| [s5-3-D · Dynamic Adjustment](https://contest.ucup.ac/contest/4565/problem/20732) | S5 Gorkovskaya | 数据结构、贪心 | 单调回归对偶转期限调度拟阵，动态维护最大收益基；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |
| [s5-3-I · Interval MST](https://contest.ucup.ac/contest/4565/problem/20737) | S5 Gorkovskaya | 图论、数据结构 | 区间 MST 权值公式，树状数组多次离线扫描统计；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.8） |
| [s5-3-K · Keep Colors Apart](https://contest.ucup.ac/contest/4565/problem/20739) | S5 Gorkovskaya | 贪心、数据结构 | 凹 DP 的差分多重集，维护可选收益与时序约束；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.11） |
| [s5-3-M · Matching Substrings](https://contest.ucup.ac/contest/4565/problem/20741) | S5 Gorkovskaya | 字符串、树上算法、数据结构 | SAM endpos 合并，后缀链树 DSU 统计可延伸子串；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.13） |
| [s5-6-B · PerMutation](https://contest.ucup.ac/contest/4617/problem/23670) | S5 Hyakumanben | 数据结构、多项式与线性代数 | 2×2 矩阵前缀积与树状数组第 k 项，交换只改四处比较；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.4） |
| [s5-6-F · Path XOR on MST](https://contest.ucup.ac/contest/4617/problem/23674) | S5 Hyakumanben | 图论、位运算与状态压缩、数据结构 | Kruskal 配异或势能 DSU 和环空间线性基；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.9） |
| [s5-6-H · Please Insert Coin](https://contest.ucup.ac/contest/4617/problem/23676) | S5 Hyakumanben | 动态规划、数据结构 | 仅更新障碍附近 DP，线段树维护移动代价下包络；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.12） |
| [s5-6-I · tatesoto decomposition](https://contest.ucup.ac/contest/4617/problem/23677) | S5 Hyakumanben | 字符串、数据结构 | 正反 Z 算法，扫描有效分割边界并统计分解；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.14） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | 贪心后继指针，倍增汇总区间内字符切换次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |
