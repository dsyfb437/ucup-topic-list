# 字符串

67 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-8-F · Differences](https://contest.ucup.ac/contest/1070/problem/5254) | S1 Slovenia | 字符串 | 多项式哈希表示字符串集合差异；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.9） |
| [s1-8-H · Insertions](https://contest.ucup.ac/contest/1070/problem/5256) | S1 Slovenia | 字符串 | KMP、Z 算法与失配树统计插入后的匹配；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-8.pdf)（文件 p.16） |
| [s1-13-J · Kth Lex Min Min Min Subpalindromes](https://contest.ucup.ac/contest/1212/problem/6353) | S1 Iberia | 字符串、构造、组合计数 | 字符数至少三时避开前两字符，二元情况用六周期构造；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.3） |
| [s1-20-E · Strange Keyboard](https://contest.ucup.ac/contest/1259/problem/6635) | S1 India | 动态规划、字符串 | 字符串前缀 DP，计算一次键盘操作的覆盖代价；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-20.pdf)（文件 p.18） |
| [s2-2-A · Mixed Messages](https://contest.ucup.ac/contest/1356/problem/7175) | S2 SPb | 动态规划、贪心、字符串 | 子序列位置 DP，或枚举中间字符贪心选两侧；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.2） |
| [s2-2-M · Hardcore String Counting](https://contest.ucup.ac/contest/1356/problem/7187) | S2 SPb | 字符串、多项式与线性代数 | 由 border 推出递推，用多项式取模求远项；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.9） |
| [s2-5-K · Text Editor](https://contest.ucup.ac/contest/1388/problem/6556) | S2 Northern | 数据结构、字符串 | 可持久化 Treap，节点存原输入字符串切片；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.49） |
| [s2-5-L · LCSLCSLCS](https://contest.ucup.ac/contest/1388/problem/6557) | S2 Northern | 字符串、动态规划、多项式与线性代数 | 半局部 LCS 与 sticky braids 合成重复串转移；[原文](https://contest.ucup.ac/download.php?type=attachments&id=1388&r=1)（文件 p.54） |
| [s2-6-M · Pattern Search](https://contest.ucup.ac/contest/1398/problem/7618) | S2 Warsaw | 字符串、组合计数 | 枚举周期重复次数，按字符频次约束优化；[原文](https://assets.ucup.ac/tutorials/tutorials-2-6.pdf)（文件 p.5） |
| [s2-19-B · Binary Sequence](https://contest.ucup.ac/contest/1487/problem/8129) | S2 Estonia | 字符串 | 证明隔两项的后缀关系，生成足够长后缀；[原文](https://assets.ucup.ac/tutorials/tutorials-2-19.pdf)（文件 p.6） |
| [s2-20-H · 404 Chotto Found](https://contest.ucup.ac/contest/1499/problem/8172) | S2 Ōokayama | 字符串、数据结构 | 后缀数组与 LCP 排除多串公共子串；[原文](https://assets.ucup.ac/tutorials/tutorials-2-20.pdf)（文件 p.9） |
| [s2-21-E · Enumerating Substrings](https://contest.ucup.ac/contest/1511/problem/8211) | S2 Delft | 字符串、动态规划、组合计数 | 按 border 与周期分解，DP 统计不同字符模式；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.3） |
| [s2-21-G · Graffiti](https://contest.ucup.ac/contest/1511/problem/8213) | S2 Delft | 树上算法、动态规划、字符串 | 记录父子字母做树形 DP，合并长度三路径贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.5） |
| [s2-26-H · Harmonic Operations](https://contest.ucup.ac/contest/1576/problem/8512) | S2 Latin America | 字符串、数据结构 | KMP 提取最小周期，维护旋转和插入的组合摘要；[原文](https://scorelatam.naquadah.com.br/pda24/editorial.pdf)（文件 p.9） |
| [s3-0-B · Champernowne Substring](https://contest.ucup.ac/contest/1695/problem/8769) | S3 America | 字符串、搜索与二分 | 枚举首个数字长度和缺失前缀，处理十进制进位；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.4） |
| [s3-0-I · Not Another Constructive!](https://contest.ucup.ac/contest/1695/problem/8776) | S3 America | 动态规划、字符串 | 记忆化搜索记录 N、NA、NAC 子序列数量；[原文](https://assets.ucup.ac/tutorials/tutorials-3-00-en.pdf)（文件 p.18） |
| [s3-1-I · Spin & Rotate!](https://contest.ucup.ac/contest/1696/problem/8789) | S3 St. Petersburg | 贪心、字符串 | 用等价变换消去可缩短的操作子串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.117） |
| [s3-2-E · Pattern Search II](https://contest.ucup.ac/contest/1699/problem/8521) | S3 Zielona Gora | 字符串、动态规划、贪心 | Fibonacci 单词递归，预处理匹配转移；[原文](https://assets.ucup.ac/tutorials/tutorials-3-02-en.pdf)（文件 p.59） |
| [s3-4-A · Again Make UTPC](https://contest.ucup.ac/contest/1738/problem/9113) | S3 Hongo | 字符串、贪心 | 逆字典序目标保持相对顺序，枚举初始连续块；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.6） |
| [s3-4-D · DRD String](https://contest.ucup.ac/contest/1738/problem/9116) | S3 Hongo | 字符串、动态规划、组合计数 | 按最短 border 分解，前缀和优化计数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.20） |
| [s3-4-N · Number of Abbreviations](https://contest.ucup.ac/contest/1738/problem/9126) | S3 Hongo | 字符串、组合计数 | 按删除长度分组，利用相邻结果相等条件去重；[原文](https://assets.ucup.ac/tutorials/tutorials-3-04-ja.pdf)（文件 p.92） |
| [s3-7-J · Juliet Unifies Ones](https://contest.ucup.ac/contest/1774/problem/9229) | S3 Warsaw | 动态规划、字符串 | 按 0、1、0 三段状态求最少删除；[原文](https://qoj.ac/blog/jiangly/blogs/958) |
| [s3-11-A · Welcome to NPCAPC](https://contest.ucup.ac/contest/1804/problem/9435) | S3 Sumiyosi | 动态规划、多项式与线性代数、字符串 | 记录目标子序列匹配长度，矩阵或递推求大长度计数；[原文](https://atcoder.jp/contests/npcapc_2024/editorial/10269) |
| [s3-13-G · Count Pseudo-Palindromes](https://contest.ucup.ac/contest/1812/problem/9482) | S3 Sendai | 字符串、概率期望与随机化 | 哈希统计偶长伪回文，枚举有限种奇长核心；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.36） |
| [s3-13-N · 0100 Insertion](https://contest.ucup.ac/contest/1812/problem/9489) | S3 Sendai | 动态规划、字符串 | 记录前缀和及其最小值，统计插入可达串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.68） |
| [s3-13-O · Sub Brackets](https://contest.ucup.ac/contest/1812/problem/9490) | S3 Sendai | 图论、字符串 | 不相容区间按左端奇偶建二分图，最大独立集；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.72） |
| [s3-18-G · Shrek's Song of the Swamp](https://contest.ucup.ac/contest/1849/problem/9787) | S3 Southeastern Europe | 动态规划、字符串 | 等字符块只需长度二或三，前缀 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-18-en.pdf)（文件 p.9） |
| [s3-21-B · Self Checkout](https://contest.ucup.ac/contest/1872/problem/9876) | S3 Ōokayama | 组合计数、字符串 | 表达式拆成独立块，反射原理计算路径数；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11403) |
| [s3-21-M · Cartesian Trees](https://contest.ucup.ac/contest/1872/problem/9887) | S3 Ōokayama | 树上算法、字符串、数据结构、概率期望与随机化 | Cartesian 树括号哈希，双向扫描线段树统计不同子树形态；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11194) |
| [s3-24-A · Acronym](https://contest.ucup.ac/contest/1890/problem/9959) | S3 Poland | 字符串、模拟与基础实现 | 记录每个首字母代表词，检查缩写的所有字母；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.2） |
| [s3-24-L · Looping RPS](https://contest.ucup.ac/contest/1890/problem/9970) | S3 Poland | 字符串、概率期望与随机化 | 字符串哈希与 LCP 比较循环石头剪刀布串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-24-pl.pdf)（文件 p.126） |
| [s3-27-E · Equal Strings](https://contest.ucup.ac/contest/1901/problem/8615) | S3 London | 交互与信息编码、概率期望与随机化、字符串 | 按到枢轴字符串的距离分组，递归区分相等串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-30-K · Vortex](https://contest.ucup.ac/contest/1917/problem/10097) | S3 Northern | 树上算法、概率期望与随机化、字符串 | 以重心定根，子树哈希排序得到规范遍历；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.5） |
| [s3-31-A · Anthem](https://contest.ucup.ac/contest/1924/problem/10114) | S3 Wroclaw | 字符串、贪心、数据结构 | 贪心消去冗余回文，维护对数个活跃回文；[原文](https://assets.ucup.ac/tutorials/tutorials-3-31-en.pdf)（文件 p.89） |
| [s3-33-A · AB to C](https://contest.ucup.ac/contest/1954/problem/10265) | S3 India | 贪心、字符串 | 字符数量奇偶不变量，最大化 A 前缀并处理结尾；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.1） |
| [s3-33-G · Lexicographic Raffle](https://contest.ucup.ac/contest/1954/problem/10271) | S3 India | 字符串、数据结构 | 相邻差异决定字典序，维护关键位置贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-3-33-en.pdf)（文件 p.8） |
| [s3-34-E · 010-11 Shorten](https://contest.ucup.ac/contest/1965/problem/10325) | S3 Aobayama | 贪心、字符串 | 按 1 分隔零段，归约为相邻正数共同减一；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.15） |
| [s3-34-M · Divide Digit String](https://contest.ucup.ac/contest/1965/problem/10333) | S3 Aobayama | 字符串、搜索与二分 | 后缀数组排序候选并二分，分 K=1 与更大情况；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.22） |
| [s3-34-N · Palindromic Path](https://contest.ucup.ac/contest/1965/problem/10334) | S3 Aobayama | 图论、字符串 | 回文路径转辅助图，点双与割点分析；[原文](https://assets.ucup.ac/tutorials/tutorials-3-34-ja.pdf)（文件 p.34） |
| [s3-35-A · Suspicious Submissions](https://contest.ucup.ac/contest/1993/problem/10701) | S3 Kraków | 字符串、数据结构 | 正反 Trie 建字典序坐标，离线二维或三维数点；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.1） |
| [s3-35-K · Bitter](https://contest.ucup.ac/contest/1993/problem/10711) | S3 Kraków | 字符串、树上算法、概率期望与随机化 | 表达式子树规范化局部变量，用哈希合并等价类；[原文](https://assets.ucup.ac/tutorials/tutorials-3-35-en.pdf)（文件 p.8） |
| [s3-39-H · Hidden Sequence Rotation](https://contest.ucup.ac/contest/2071/problem/10977) | S3 Tokyo | 字符串、交互与信息编码 | 倍增比较最小子串，利用周期性压缩询问总长；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-I · Insert AB or BA](https://contest.ucup.ac/contest/2071/problem/10978) | S3 Tokyo | 字符串、动态规划、数据结构 | 前缀平衡分类，笛卡尔树或单调栈优化插入 DP；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-40-C · DNA Subsequences](https://contest.ucup.ac/contest/2135/problem/12152) | S3 Potyczki | 动态规划、搜索与二分、字符串 | 分段费用凸性，参数搜索配合线性 DP；[原文](https://assets.ucup.ac/tutorials/tutorials-3-40-pl.pdf)（文件 p.2） |
| [s4-1-D · Sequence Is Not Subsequence](https://contest.ucup.ac/contest/2539/problem/14429) | S4 Korolyov | 字符串、构造 | 按开头字符是否相同递归构造最短非子序列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-01-en.pdf)（文件 p.2） |
| [s4-2-G · Goofy Songs](https://contest.ucup.ac/contest/2551/problem/14136) | S4 Paris | 字符串、模拟与基础实现 | 正则表达式分组与重复短句匹配；[原文](https://assets.ucup.ac/tutorials/tutorials-4-02-en.pdf)（文件 p.4） |
| [s4-3-C · Roman Numerals](https://contest.ucup.ac/contest/2559/problem/14417) | S4 Polar | 数据结构、字符串 | 最大值笛卡尔树分解罗马数字区间，离线维护前后缀值；[原文](https://assets.ucup.ac/tutorials/tutorials-4-03-en.pdf)（文件 p.2） |
| [s4-10-D · DNA](https://contest.ucup.ac/contest/2814/problem/16003) | S4 Wrocław | 字符串、贪心 | 零一字符频次给出三串 LCS 二倍近似；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.20） |
| [s4-10-I · Identical Fences](https://contest.ucup.ac/contest/2814/problem/16008) | S4 Wrocław | 概率期望与随机化、贪心、字符串 | 在线构造两个相同子序列，用随机游走分析剩余长度；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.33） |
| [s4-10-L · Letters on T-shirts](https://contest.ucup.ac/contest/2814/problem/16011) | S4 Wrocław | 字符串、搜索与二分 | 枚举三个短串的排列与非空前缀，检查能否拼成 cerc；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.11） |
| [s4-11-B · AND Reconstruction](https://contest.ucup.ac/contest/2828/problem/16116) | S4 Southeastern Europe | 位运算与状态压缩、字符串 | 按连续零块与最短一块刻画 AND 唯一恢复长度；[原文](https://assets.ucup.ac/tutorials/tutorials-4-11-en.pdf)（文件 p.2） |
| [s4-16-E · Evaluation](https://contest.ucup.ac/contest/3347/problem/17154) | S4 Warsaw | 动态规划、字符串 | 扫描表达式，维护已完成项、未完成乘项和当前因子总和；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.7） |
| [s4-16-I · Palindromes](https://contest.ucup.ac/contest/3347/problem/17158) | S4 Warsaw | 字符串、组合计数 | 回文前缀周期归约，统计自由二进制位；[原文](https://assets.ucup.ac/tutorials/tutorials-4-16-en.pdf)（文件 p.13） |
| [s4-17-C · String Workshop](https://contest.ucup.ac/contest/3384/problem/17163) | S4 St. Petersburg | 数据结构、字符串、组合计数 | 稳定排序的必经逆序交叉，离线统计带权贡献；[原文](https://assets.ucup.ac/tutorials/tutorials-4-17-en.pdf)（文件 p.2） |
| [s4-18-A · Apparently Make UTPC](https://contest.ucup.ac/contest/3420/problem/17246) | S4 Hongō | 字符串、搜索与二分 | 后缀数组和 LCP 枚举重叠，以二分选最小字典序拼接；[原文](https://atcoder.jp/contests/utpc2025/editorial/15605) |
| [s4-18-F · Finite Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17251) | S4 Hongō | 字符串、数据结构 | 左右括号个数相等当且仅当无限，前缀和回答区间；[原文](https://atcoder.jp/contests/utpc2025/editorial/15692) |
| [s4-18-G · Greatest Bracket Sequence](https://contest.ucup.ac/contest/3420/problem/17252) | S4 Hongō | 字符串、数据结构、搜索与二分 | 最长合法括号后缀结构，并行二分定位字典序最优；[原文](https://atcoder.jp/contests/utpc2025/editorial/16136) |
| [s4-19-L · Layered Caesar Salad](https://contest.ucup.ac/contest/3426/problem/17271) | S4 Belarus | 构造、字符串 | 利用缺失首字母标记，Caesar 移位编码两次运行；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.7） |
| [s4-20-E · Optimal Splitting](https://contest.ucup.ac/contest/3516/problem/17410) | S4 India | 动态规划、字符串、贪心 | 两子序列可达状态 DP，逐位贪心最小化最大串；[原文](https://assets.ucup.ac/tutorials/tutorials-4-20-en.pdf)（文件 p.8） |
| [s4-21-E · Find "rururutata"](https://contest.ucup.ac/contest/3542/problem/17423) | S4 Kamigō | 字符串、数据结构 | 倍增无碰撞哈希或 LCP，检测三重重复段；[原文](https://atcoder.jp/contests/pakencamp-2025-day3/editorial/17002) |
| [s4-22-B · Cat Cut](https://contest.ucup.ac/contest/3575/problem/17714) | S4 Kyoto | 字符串、动态规划 | 按最终后缀形态拆分，DP 求最小字典序前缀拼接；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.1） |
| [s4-22-L · Make Many KUPC](https://contest.ucup.ac/contest/3575/problem/17724) | S4 Kyoto | 贪心、字符串 | 从右向左匹配 KUPC，交换论证保证收益不降；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.9） |
| [s4-25-H · Halfway Hawser](https://contest.ucup.ac/contest/3773/problem/18408) | S4 Zagreb | 字符串、贪心 | 比较可生成字符串次序，按排序位置选择中位串；[原文](https://assets.ucup.ac/tutorials/tutorials-4-25-en.pdf)（文件 p.31） |
| [s5-3-M · Matching Substrings](https://contest.ucup.ac/contest/4565/problem/20741) | S5 Gorkovskaya | 字符串、树上算法、数据结构 | SAM endpos 合并，后缀链树 DSU 统计可延伸子串；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4565&r=1)（文件 p.13） |
| [s5-6-I · tatesoto decomposition](https://contest.ucup.ac/contest/4617/problem/23677) | S5 Hyakumanben | 字符串、数据结构 | 正反 Z 算法，扫描有效分割边界并统计分解；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.14） |
| [s5-6-J · Hugest Number](https://contest.ucup.ac/contest/4617/problem/23678) | S5 Hyakumanben | 数论、字符串、多项式与线性代数 | Euclid 型块递归构造最大数，矩阵快速幂处理巨大重复次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.15） |
| [s5-6-N · Delete Sad Faces (Hard)](https://contest.ucup.ac/contest/4617/problem/23682) | S5 Hyakumanben | 字符串、数据结构、贪心 | 贪心后继指针，倍增汇总区间内字符切换次数；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.28） |
