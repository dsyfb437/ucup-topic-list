# 贪心

121 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-4-A · Adjacent Product Sum](https://contest.ucup.ac/contest/1106/problem/5517) | S1 Ukraine | 贪心、构造 | 排序后奇偶交错放置，交换论证；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-4.pdf)（文件 p.1） |
| [s1-8-D · Deforestation](https://contest.ucup.ac/contest/1070/problem/5252) | S1 Slovenia | 贪心、树上算法 | 自叶向根剪枝，保留剩余树桩状态；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.3） |
| [s1-12-E · Five Med Sum](https://contest.ucup.ac/contest/1207/problem/6321) | S1 Ōokayama | 组合计数、贪心 | 五组元素整体排序后统计中位数贡献；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-12.pdf)（文件 p.3） |
| [s1-13-I · SPPPSPSS.](https://contest.ucup.ac/contest/1212/problem/6352) | S1 Iberia | 贪心、搜索与二分 | 前后缀排序交替执行，二分最少操作数；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-16-I · Classical Minimization Problem](https://contest.ucup.ac/contest/1223/problem/6415) | S1 Gomel | 贪心、数据结构 | 优先处理点数最多的横纵线并配对；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.4） |
| [s1-16-J · Classical Scheduling Problem](https://contest.ucup.ac/contest/1223/problem/6416) | S1 Gomel | 贪心、搜索与二分、数据结构 | 二分目标数量，堆维护前后缀最小代价；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-16.pdf)（文件 p.5） |
| [s1-20-B · Minimize Median](https://contest.ucup.ac/contest/1259/problem/6632) | S1 India | 搜索与二分、贪心 | 二分中位数，求降到阈值的最小代价；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.6） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | 子序列位置 DP，或枚举中间字符贪心选两侧；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-2-D · Bishops](https://contest.ucup.ac/contest/1356/problem/7178) | S2 SPb | 贪心、图论 | 对角线建二分图，区间邻接按右端点贪心匹配；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.13） |
| [s2-2-E · Fischer's Chess Guessing Game](https://contest.ucup.ac/contest/1356/problem/7179) | S2 SPb | 交互与信息编码、贪心、搜索与二分 | 枚举猜测点，最小化九类反馈中的最大候选数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.3） |
| [s2-5-A · Greedy Bipartite Matching](https://contest.ucup.ac/contest/1388/problem/6546) | S2 Northern | 图论、贪心 | 按权值逐层保留可扩展的二分图匹配；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.2） |
| [s2-5-B · Banshee](https://contest.ucup.ac/contest/1388/problem/6547) | S2 Northern | 搜索与二分、贪心 | 二分攻击能力，交换论证最少使用次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.19） |
| [s2-5-H · Shared Memory Switch](https://contest.ucup.ac/contest/1388/problem/6553) | S2 Northern | 贪心、数据结构 | 离线预知发送时间，堆淘汰最晚发送的包；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.45） |
| [s2-6-I · Boxes](https://contest.ucup.ac/contest/1398/problem/7614) | S2 Warsaw | 贪心 | 盒子排序后放入最靠左且仍有容量的盒子；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.4） |
| [s2-6-L · Spectacle](https://contest.ucup.ac/contest/1398/problem/7617) | S2 Warsaw | 贪心、数据结构 | 相邻差排序激活，DSU 维护分量可配对数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-7-B · Bins and Balls](https://contest.ucup.ac/contest/1399/problem/7633) | S2 Two Capitals | 贪心 | 排序并分析容量阈值；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.1） |
| [s2-7-G · Lake](https://contest.ucup.ac/contest/1399/problem/7638) | S2 Two Capitals | 贪心 | 按人数比例安排 4+3 或 3+4 的运输；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.6） |
| [s2-7-N · Shoes](https://contest.ucup.ac/contest/1399/problem/7645) | S2 Two Capitals | 动态规划、贪心 | 交换论证后做双端区间 DP，优化访问天数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-7.pdf)（文件 p.9） |
| [s2-14-B · Build Permutation](https://contest.ucup.ac/contest/1452/problem/7933) | S2 Southeastern Europe | 贪心、构造 | 排序后首尾配对，验证固定和；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.2） |
| [s2-14-J · Jackpot](https://contest.ucup.ac/contest/1452/problem/7941) | S2 Southeastern Europe | 贪心 | 排序分高低两半，反向配对达到分差上界；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.11） |
| [s2-14-K · $K$ Subsequences](https://contest.ucup.ac/contest/1452/problem/7942) | S2 Southeastern Europe | 贪心、数据结构 | 正一给当前和最小的序列，负一给最大的；[原文](https://assets.ucup.ac/tutorials/tutorials-2-14.pdf)（文件 p.12） |
| [s2-16-E · Four Plus Four](https://contest.ucup.ac/contest/1465/problem/4828) | S2 Run Twice | 贪心、位运算与状态压缩 | 按字母子集列候选，贪心分配秘密与密钥；[原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.47） |
| [s2-16-H · Eager Sorting](https://contest.ucup.ac/contest/1465/problem/4831) | S2 Run Twice | 交互与信息编码、贪心 | 利用两次运行反馈，快速排序或归并排序；[原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.92） |
| [s2-19-G · LCA Counting](https://contest.ucup.ac/contest/1487/problem/8134) | S2 Estonia | 树上算法、动态规划、贪心 | 树上取两个最大免费子状态，再按增益付费扩展；[原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.11） |
| [s2-19-J · 'Ello, and What Are You After, Then?](https://contest.ucup.ac/contest/1487/problem/8137) | S2 Estonia | 概率期望与随机化、搜索与二分、贪心 | 混合策略可行性转线性分离，双层二分与排序；[原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.16） |
| [s2-20-O · 2D Parentheses](https://contest.ucup.ac/contest/1499/problem/8179) | S2 Ōokayama | 计算几何、贪心、图论 | 扫描线贪心匹配二维括号的左下与右上角；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.18） |
| [s2-26-J · Joys of Trading](https://contest.ucup.ac/contest/1576/problem/8514) | S2 Latin America | 贪心 | 按两村生产耗时比排序，在分界资源处调配；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.13） |
| [s3-0-E · House Deconstruction](https://contest.ucup.ac/contest/1695/problem/8772) | S3 America | 贪心、组合计数 | 无交叉最优匹配，切开圆环后前后缀统计；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.10） |
| [s3-1-G · Unusual Case](https://contest.ucup.ac/contest/1696/problem/8787) | S3 St. Petersburg | 概率期望与随机化、图论、贪心 | 随机贪心游走寻找互不复用的 Hamilton 路；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.102） |
| [s3-1-I · Spin & Rotate!](https://contest.ucup.ac/contest/1696/problem/8789) | S3 St. Petersburg | 贪心、字符串 | 用等价变换消去可缩短的操作子串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.117） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | Fibonacci 单词递归，预处理匹配转移；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-2-H · Weather Forecast](https://contest.ucup.ac/contest/1699/problem/8524) | S3 Zielona Gora | 搜索与二分、贪心 | 二分平均值，减去阈值后检查前缀和划分；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.123） |
| [s3-4-A · Again Make UTPC](https://contest.ucup.ac/contest/1738/problem/9113) | S3 Hongo | 字符串、贪心 | 逆字典序目标保持相对顺序，枚举初始连续块；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.6） |
| [s3-4-G · Graph Weighting](https://contest.ucup.ac/contest/1738/problem/9119) | S3 Hongo | 动态规划、贪心、数据结构 | 凸代价分组，堆处理增量并优化 min-plus 卷积；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.40） |
| [s3-4-J · Japanese Gift Money](https://contest.ucup.ac/contest/1738/problem/9122) | S3 Hongo | 数论、动态规划、贪心 | 贪心货币表示，数位 DP 统计全部偶数张的补集；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.64） |
| [s3-4-L · Largest Triangle](https://contest.ucup.ac/contest/1738/problem/9124) | S3 Hongo | 贪心、计算几何 | 排序枚举连续三边，用海伦公式比较面积；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.82） |
| [s3-5-A · Counting Permutations](https://contest.ucup.ac/contest/1741/problem/9130) | S3 Moscow | 组合计数、贪心 | 按两个余数排序，同类元素阶乘计数；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-C · Painting Fences](https://contest.ucup.ac/contest/1741/problem/9132) | S3 Moscow | 数据结构、贪心 | 笛卡尔树枚举极大黑矩形，分析倍增扩展；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-E · Building a Fence](https://contest.ucup.ac/contest/1741/problem/9134) | S3 Moscow | 贪心 | 按边长与材料长度分类，拼接达到长度下界；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-5-M · Uniting Amoebas](https://contest.ucup.ac/contest/1741/problem/9142) | S3 Moscow | 贪心 | 始终合并全局最大值与相邻元素；[原文](https://qoj.ac/blog/jiangly/blogs/941) |
| [s3-7-B · Missing Boundaries](https://contest.ucup.ac/contest/1774/problem/9221) | S3 Warsaw | 贪心 | 端点约束判相容，计算合法区间数量上下界；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-D · Data Determination](https://contest.ucup.ac/contest/1774/problem/9223) | S3 Warsaw | 贪心、搜索与二分 | 排序后按中位数奇偶分类，枚举紧邻候选对；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-7-M · Mathematics Championships](https://contest.ucup.ac/contest/1774/problem/9232) | S3 Warsaw | 贪心 | 降序前缀和，在二的幂长度处取最优值；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-C · Solve with Friends](https://contest.ucup.ac/contest/1804/problem/9437) | S3 Sumiyosi | 贪心 | 各组排序与前缀和，优化多人协作代价；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10201) |
| [s3-11-M · Admired Person](https://contest.ucup.ac/contest/1804/problem/9447) | S3 Sumiyosi | 动态规划、贪心 | 排序后做保序最小代价匹配 DP；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10177) |
| [s3-11-O · New School Term](https://contest.ucup.ac/contest/1804/problem/9449) | S3 Sumiyosi | 动态规划、数据结构、贪心 | 贪心决定分组，DSU 合并配合可撤销背包；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10178) |
| [s3-13-H · Maximize Array](https://contest.ucup.ac/contest/1812/problem/9483) | S3 Sendai | 贪心、数据结构 | 按同余位置的前缀最大值，依次最大化字典序；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.41） |
| [s3-13-L · Vivid Colors](https://contest.ucup.ac/contest/1812/problem/9487) | S3 Sendai | 计算几何、贪心 | 枚举目标方向，动态维护内积最大的 k 个向量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.58） |
| [s3-18-B · NonZero PrefSuf Sums](https://contest.ucup.ac/contest/1849/problem/9782) | S3 Southeastern Europe | 贪心、数论、构造 | 按正负总和及 gcd 分类，避开零前后缀；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.2） |
| [s3-18-D · Donkey and Puss in Boots](https://contest.ucup.ac/contest/1849/problem/9784) | S3 Southeastern Europe | 博弈论、贪心 | 只需取最大堆，与剩余总数比较胜负；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.5） |
| [s3-18-F · Magical Bags](https://contest.ucup.ac/contest/1849/problem/9786) | S3 Southeastern Europe | 贪心 | 每袋仅保留极值，区间交结构决定保留一件或两件；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.8） |
| [s3-18-H · Shreckless](https://contest.ucup.ac/contest/1849/problem/9788) | S3 Southeastern Europe | 贪心、图论 | 相邻列排序匹配，最大化逆序连接覆盖的行；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.10） |
| [s3-18-J · Make Swamp Great Again](https://contest.ucup.ac/contest/1849/problem/9790) | S3 Southeastern Europe | 贪心 | 检查三个相邻位置能否产生目标中位数，再向外传播；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.13） |
| [s3-18-L · Ogre Sort](https://contest.ucup.ac/contest/1849/problem/9792) | S3 Southeastern Europe | 贪心、数据结构 | 按必要前移顺序构造，树状数组维护当前位置；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.15） |
| [s3-21-A · Don't Detect Cycle](https://contest.ucup.ac/contest/1872/problem/9875) | S3 Ōokayama | 图论、贪心 | 逆序删边，维护端点是否处于环内；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11085) |
| [s3-24-C · Cows](https://contest.ucup.ac/contest/1890/problem/9961) | S3 Poland | 搜索与二分、贪心 | 二分完成时间，按相邻牛的空闲区间贪心互助；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.135） |
| [s3-24-I · Imbalanced Teams](https://contest.ucup.ac/contest/1890/problem/9967) | S3 Poland | 贪心 | 排序后按最强最弱成员分组，求可达能力差；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.19） |
| [s3-27-B · The Best Wife](https://contest.ucup.ac/contest/1901/problem/8612) | S3 London | 数据结构、贪心 | 删包含区间后维护贪心跳转森林，LCT 或持久化线段树；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-J · Jigsaw Puzzle](https://contest.ucup.ac/contest/1901/problem/8620) | S3 London | 计算几何、贪心 | 随机切割使边长唯一，逐片拼接后旋转对齐；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-27-M · Meta](https://contest.ucup.ac/contest/1901/problem/8623) | S3 London | 贪心 | 取每题最短时间，排序后在三百分钟内尽量多做；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.4） |
| [s3-30-D · Preparation for the Exam](https://contest.ucup.ac/contest/1917/problem/10090) | S3 Northern | 贪心、概率期望与随机化 | 交换论证使各部分准备题数尽量均衡；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.2） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | 贪心消去冗余回文，维护对数个活跃回文；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-31-C · CERC Plaques](https://contest.ucup.ac/contest/1924/problem/10116) | S3 Wroclaw | 贪心 | 两序列排序后保序配对；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.11） |
| [s3-31-G · Groceries](https://contest.ucup.ac/contest/1924/problem/10120) | S3 Wroclaw | 搜索与二分、贪心 | 二分最远路程，圆环区间覆盖与跳转；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.69） |
| [s3-31-I · Illuminati](https://contest.ucup.ac/contest/1924/problem/10122) | S3 Wroclaw | 图论、贪心 | 入度出度平衡保证环分解，排序配边求字典序最小；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.29） |
| [s3-32-G · Picturesque Skyline](https://contest.ucup.ac/contest/1939/problem/10220) | S3 Dhaka | 动态规划、贪心、数据结构 | 从最小值起安排金字塔两端，区间 DP 合并最少交换；[原文](https://assets.ucup.ac/tutorials/tutorials-3-32-en.pdf)（文件 p.3） |
| [s3-33-A · AB to C](https://contest.ucup.ac/contest/1954/problem/10265) | S3 India | 贪心、字符串 | 字符数量奇偶不变量，最大化 A 前缀并处理结尾；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.1） |
| [s3-33-B · Bin Packing](https://contest.ucup.ac/contest/1954/problem/10266) | S3 India | 贪心、动态规划 | 优先配满容量十二，剩余四类数量做 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.2） |
| [s3-33-F · Greedy Prices](https://contest.ucup.ac/contest/1954/problem/10270) | S3 India | 贪心、动态规划 | 交换论证确定购买顺序，乘性增长界压缩购买数量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.7） |
| [s3-33-M · Ticket Revenue Maximization](https://contest.ucup.ac/contest/1954/problem/10277) | S3 India | 贪心、动态规划 | 按强弱排序转合法括号选择，优化收入；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.14） |
| [s3-34-D · Swap Counter](https://contest.ucup.ac/contest/1965/problem/10324) | S3 Aobayama | 构造、贪心 | 由交换次数差分恢复排列，贪心最小化字典序；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.43） |
| [s3-34-E · 010-11 Shorten](https://contest.ucup.ac/contest/1965/problem/10325) | S3 Aobayama | 贪心、字符串 | 按 1 分隔零段，归约为相邻正数共同减一；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.15） |
| [s3-34-J · Median Operations](https://contest.ucup.ac/contest/1965/problem/10330) | S3 Aobayama | 贪心、数据结构 | 阈值化为 01 串，线段树维护三字符边界摘要；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.68） |
| [s3-34-K · Shuffle and Max Bracket Score](https://contest.ucup.ac/contest/1965/problem/10331) | S3 Aobayama | 概率期望与随机化、贪心、组合计数 | 堆求最优括号得分，再按随机排列统计贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.72） |
| [s3-39-C · Card Deck](https://contest.ucup.ac/contest/2071/problem/10972) | S3 Tokyo | 贪心、组合计数 | 牌堆贪心可行性，进一步计数可取集合；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-J · Journey through the Fractal](https://contest.ucup.ac/contest/2071/problem/10979) | S3 Tokyo | 贪心、组合计数 | 分形路径层级展开，按倍增次数贪心分配；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-Q · Quadratic Pieces](https://contest.ucup.ac/contest/2071/problem/10986) | S3 Tokyo | 贪心 | 三阶差分为零刻画二次序列，贪心取最长段；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-A · AGI](https://contest.ucup.ac/contest/2135/problem/12150) | S3 Potyczki | 贪心、构造 | 包含区间成对消去，递归构造近半数正确的回答；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.244） |
| [s3-40-I · Santa Claus](https://contest.ucup.ac/contest/2135/problem/12158) | S3 Potyczki | 贪心 | 排序后选极值并保序配对，交换论证乘积最优；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.281） |
| [s4-0-D · Geometry Rush](https://contest.ucup.ac/contest/2041/problem/11359) | S4 America | 计算几何、贪心 | 双指针扫横坐标，维护可通过的纵坐标区间；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.17） |
| [s4-0-H · Ornaments on a Tree](https://contest.ucup.ac/contest/2041/problem/11363) | S4 America | 树上算法、动态规划、贪心 | 自底向上分配权值，保存可向父节点转移的余量；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.32） |
| [s4-0-K · SLA Tomography](https://contest.ucup.ac/contest/2041/problem/11366) | S4 America | 贪心 | 自底向上维护可积液宽度，缩小时加隔墙扩张时加列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.48） |
| [s4-1-H · Misread Problem](https://contest.ucup.ac/contest/2539/problem/14433) | S4 Korolyov | 贪心、数据结构 | 凸函数差分斜率集合，slope trick 求固定总和最小代价；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.3） |
| [s4-2-H · Heure de Rush](https://contest.ucup.ac/contest/2551/problem/14137) | S4 Paris | 贪心 | 保持人相对顺序，只计算各车乘客最终区间两端；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-2-K · $k$ Operations](https://contest.ucup.ac/contest/2551/problem/14140) | S4 Paris | 贪心、数据结构 | 按值从小到大减少，排序前缀和定位最后一段；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.7） |
| [s4-3-I · Two Permutations](https://contest.ucup.ac/contest/2559/problem/14423) | S4 Polar | 构造、贪心 | 固定最小未对齐元素，合法交换逐步恢复目标排列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.5） |
| [s4-8-B · Beats](https://contest.ucup.ac/contest/2668/problem/15445) | S4 Poland | 贪心、数据结构 | 枚举移走后缀，双端队列维护可保留的递增子序列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.51） |
| [s4-8-J · Jury of AMPPZ](https://contest.ucup.ac/contest/2668/problem/15453) | S4 Poland | 搜索与二分、贪心 | 二分综合得分，分别排序几何与非几何题选择；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.18） |
| [s4-8-K · Kids' Blocks](https://contest.ucup.ac/contest/2668/problem/15454) | S4 Poland | 贪心 | 找最高和次高积木，前后缀最大值安排拆分；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.12） |
| [s4-8-M · Market](https://contest.ucup.ac/contest/2668/problem/15456) | S4 Poland | 贪心 | 是否预知次日的收益差排序，选 k 个最大增益；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.145） |
| [s4-10-D · DNA](https://contest.ucup.ac/contest/2814/problem/16003) | S4 Wrocław | 字符串、贪心 | 零一字符频次给出三串 LCS 二倍近似；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.20） |
| [s4-10-E · Easy Tetris](https://contest.ucup.ac/contest/2814/problem/16004) | S4 Wrocław | 搜索与二分、贪心 | 二分可消层数，按列高度模四放置 O 和 I 块；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.126） |
| [s4-10-H · Hiking](https://contest.ucup.ac/contest/2814/problem/16007) | S4 Wrocław | 贪心 | 将相同值分到递增段，安排最大最小值端点；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.38） |
| [s4-10-I · Identical Fences](https://contest.ucup.ac/contest/2814/problem/16008) | S4 Wrocław | 概率期望与随机化、贪心、字符串 | 在线构造两个相同子序列，用随机游走分析剩余长度；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.33） |
| [s4-10-J · Joyful Guided Tour](https://contest.ucup.ac/contest/2814/problem/16009) | S4 Wrocław | 图论、贪心、构造 | 局部重染使同色边数下降，摊还得到合法染色；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.93） |
| [s4-11-G · Intervals from Triplets](https://contest.ucup.ac/contest/2828/problem/16121) | S4 Southeastern Europe | 动态规划、贪心 | 按三元组中点排序，记录最早和最晚结尾两状态；[原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.7） |
| [s4-13-B · Increasing Swaps](https://contest.ucup.ac/contest/2921/problem/16227) | S4 Ōokayama | 贪心、构造 | 逆置换分段右旋，立即拆分可分段最优；[原文](https://assets.ucup.ac/tutorials/tutorials-4-13-en.pdf)（文件 p.1） |
| [s4-16-D · Deque Sort](https://contest.ucup.ac/contest/3347/problem/17153) | S4 Warsaw | 数据结构、贪心 | 每阶段拆前缀最大值序列，维护其长度与翻转；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.6） |
| [s4-18-J · Jelly](https://contest.ucup.ac/contest/3420/problem/17255) | S4 Hongō | 贪心 | 按甜辣差排序，选择交替正负贡献的两端；[原文](https://atcoder.jp/contests/utpc2025/editorial/16128) |
| [s4-18-K · Keep or Gamble](https://contest.ucup.ac/contest/3420/problem/17256) | S4 Hongō | 概率期望与随机化、贪心 | 比较继续抽牌的期望增量，按阈值停止并求期望；[原文](https://atcoder.jp/contests/utpc2025/editorial/15851) |
| [s4-18-M · Max Conference](https://contest.ucup.ac/contest/3420/problem/17258) | S4 Hongō | 贪心、组合计数 | 每种字符非相邻容量，超出最多的一类决定损失；[原文](https://atcoder.jp/contests/utpc2025/editorial/15903) |
| [s4-19-D · Detecting the Missing Ship](https://contest.ucup.ac/contest/3426/problem/17263) | S4 Belarus | 交互与信息编码、贪心 | 优先打边界格，每次排除最多候选行列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | 两子序列可达状态 DP，逐位贪心最小化最大串；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-21-B · Birds-of-Paradise' Card Game](https://contest.ucup.ac/contest/3542/problem/17420) | S4 Kamigō | 贪心、组合计数 | 交换论证排除交错劣形，化简卡牌顺序；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17017) |
| [s4-21-C · Don't be Clockwise](https://contest.ucup.ac/contest/3542/problem/17421) | S4 Kamigō | 计算几何、贪心、构造 | 从最右点开始，每次选转角最小的下一点；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17020) |
| [s4-21-D · Except Ai](https://contest.ucup.ac/contest/3542/problem/17422) | S4 Kamigō | 贪心 | 每段必须缺一个值，从左向右贪心取最长合法段；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17026) |
| [s4-21-H · OR Preference](https://contest.ucup.ac/contest/3542/problem/17426) | S4 Kamigō | 位运算与状态压缩、动态规划、贪心 | 交换论证把 OR 放在 AND 前，前缀掩码 DP；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/18129) |
| [s4-22-C · Partition AND/OR Aggregation](https://contest.ucup.ac/contest/3575/problem/17715) | S4 Kyoto | 位运算与状态压缩、搜索与二分、贪心 | 二分阈值，双指针找合法区间并选互不相交段；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.2） |
| [s4-22-L · Make Many KUPC](https://contest.ucup.ac/contest/3575/problem/17724) | S4 Kyoto | 贪心、字符串 | 从右向左匹配 KUPC，交换论证保证收益不降；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-25-A · Arrow Array](https://contest.ucup.ac/contest/3773/problem/18401) | S4 Zagreb | 贪心、数据结构 | 维护前缀可行上下界，平移约束后线性判定；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.2） |
| [s4-25-H · Halfway Hawser](https://contest.ucup.ac/contest/3773/problem/18408) | S4 Zagreb | 字符串、贪心 | 比较可生成字符串次序，按排序位置选择中位串；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.31） |
| [s4-25-K · Kempt Kale](https://contest.ucup.ac/contest/3773/problem/18411) | S4 Zagreb | 贪心、数据结构、组合计数 | 合法括号位置的拟阵贪心，按收益从大到小选；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.42） |
| [s4-Extra-3-B · Word Generator](https://contest.ucup.ac/contest/2757/problem/15518) | S4 Osijek | 图论、贪心 | Hall 定理保证单词分配，反复二分图匹配构造；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-F · Binary Permutation](https://contest.ucup.ac/contest/2757/problem/15522) | S4 Osijek | 组合计数、贪心 | 正反扫描零一序列，累计可配对元素数量乘积；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.2） |
| [s4-Extra-3-G · Amoeba Tree](https://contest.ucup.ac/contest/2757/problem/15523) | S4 Osijek | 树上算法、贪心 | 按最高占据点深度贪心射击，维护插入后的局部变化；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.3） |
| [s5-1-D · Digesting](https://contest.ucup.ac/contest/4126/problem/20251) | S5 Nizhny Novgorod | 数论、贪心 | 模运算使最大值严格下降，分析能否逐层降到一；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.8） |
| [s5-1-E · Easter Eggs](https://contest.ucup.ac/contest/4126/problem/20252) | S5 Nizhny Novgorod | 概率期望与随机化、贪心 | 按首桶分情况给期望下界，并构造达到下界的策略；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.10） |
| [s5-1-J · Jaded Juice](https://contest.ucup.ac/contest/4126/problem/20257) | S5 Nizhny Novgorod | 贪心、数论 | 不确定区间宽度转确定性增量，排序并枚举重复最大增益次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4126&r=1)（文件 p.19） |
| [s5-3-D · Dynamic Adjustment](https://contest.ucup.ac/contest/4565/problem/20732) | S5 Gorkovskaya | 数据结构、贪心 | 单调回归对偶转期限调度拟阵，动态维护最大收益基；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.3） |
| [s5-3-K · Keep Colors Apart](https://contest.ucup.ac/contest/4565/problem/20739) | S5 Gorkovskaya | 贪心、数据结构 | 凹 DP 的差分多重集，维护可选收益与时序约束；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.11） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | 贪心后继指针，倍增汇总区间内字符切换次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |
