# 交互与信息编码

24 题。主副专题都纳入本页，同题可在多个专题出现。分类是题解归纳，排序不代表难度。

| 题目 | 赛站 | 专题 | 题解依据 |
|---|---|---|---|
| [s1-13-B · Random Interactive Convex Hull Bot](https://contest.ucup.ac/contest/1212/problem/6345) | S1 Iberia | 计算几何、交互与信息编码、概率期望与随机化 | 随机增量维护凸包，方向询问定位插入点；[原文](https://contest.ucup.ac/files/ucup/tutorials/tutorials-1-13.pdf)（文件 p.1） |
| [s2-2-E · Fischer's Chess Guessing Game](https://contest.ucup.ac/contest/1356/problem/7179) | S2 SPb | 交互与信息编码、贪心、搜索与二分 | 枚举猜测点，最小化九类反馈中的最大候选数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.3） |
| [s2-2-L · "Memo" Game With a Hint](https://contest.ucup.ac/contest/1356/problem/7186) | S2 SPb | 交互与信息编码、构造 | 利用提示编码，设计配对翻牌策略；[原文](https://assets.ucup.ac/tutorials/tutorials-2-2.zip)（文件 p.8） |
| [s2-16-H · Eager Sorting](https://contest.ucup.ac/contest/1465/problem/4831) | S2 Run Twice | 交互与信息编码、贪心 | 利用两次运行反馈，快速排序或归并排序；[原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.92） |
| [s2-16-J · Tetra-puzzle](https://contest.ucup.ac/contest/1465/problem/4833) | S2 Run Twice | 搜索与二分、交互与信息编码 | 确定性局面评分与束搜索选择四格骨牌；[原文](https://assets.ucup.ac/tutorials/tutorials-2-16.pdf)（文件 p.136） |
| [s2-21-J · Jumbled Primes](https://contest.ucup.ac/contest/1511/problem/8216) | S2 Delft | 交互与信息编码、数论 | gcd 查询识别素数及素数幂，优化询问次数；[原文](https://assets.ucup.ac/tutorials/tutorials-2-21.pdf)（文件 p.8） |
| [s3-1-D · Dwarfs' Bedtime](https://contest.ucup.ac/contest/1696/problem/8784) | S3 St. Petersburg | 交互与信息编码、搜索与二分 | 根据睡醒周期进行分阶段二分询问；[原文](https://assets.ucup.ac/tutorials/tutorials-3-01-en.pdf)（文件 p.57） |
| [s3-13-I · Colored Complete Graph](https://contest.ucup.ac/contest/1812/problem/9484) | S3 Sendai | 交互与信息编码、图论、构造 | 询问星形边，再逐步合并异色分量找到单色生成树；[原文](https://assets.ucup.ac/tutorials/tutorials-3-13-ja.pdf)（文件 p.44） |
| [s3-21-I · Near Pair](https://contest.ucup.ac/contest/1872/problem/9883) | S3 Ōokayama | 交互与信息编码、搜索与二分 | 区间内近邻对数量差恢复度数，再二分定位端点；[原文](https://atcoder.jp/contests/ttpc2024_1/editorial/11470) |
| [s3-27-E · Equal Strings](https://contest.ucup.ac/contest/1901/problem/8615) | S3 London | 交互与信息编码、概率期望与随机化、字符串 | 按到枢轴字符串的距离分组，递归区分相等串；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.1） |
| [s3-27-I · Interactive Casino](https://contest.ucup.ac/contest/1901/problem/8619) | S3 London | 概率期望与随机化、交互与信息编码 | 按资金比例限制下注，实验选择成功率较高的比例；[原文](https://assets.ucup.ac/tutorials/tutorials-3-27-en.pdf)（文件 p.3） |
| [s3-30-A · Archaeology](https://contest.ucup.ac/contest/1917/problem/10087) | S3 Northern | 交互与信息编码、计算几何、概率期望与随机化 | 半平面交维护候选区域，在凸多边形中心询问；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.1） |
| [s3-30-F · Interactive Primality](https://contest.ucup.ac/contest/1917/problem/10092) | S3 Northern | 交互与信息编码、数论、概率期望与随机化 | 随机加数筛小素数余数，再 CRT 恢复隐藏数；[原文](https://assets.ucup.ac/tutorials/tutorials-3-30-en.pdf)（文件 p.3） |
| [s3-39-F · Fourier Coefficients](https://contest.ucup.ac/contest/2071/problem/10975) | S3 Tokyo | 多项式与线性代数、交互与信息编码 | 几何级数点插值恢复 Fourier 系数；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s3-39-H · Hidden Sequence Rotation](https://contest.ucup.ac/contest/2071/problem/10977) | S3 Tokyo | 字符串、交互与信息编码 | 倍增比较最小子串，利用周期性压缩询问总长；[原文](https://qoj.ac/blog/jiangly/blogs/1261) |
| [s4-0-C · Entrapment](https://contest.ucup.ac/contest/2041/problem/11358) | S4 America | 博弈论、搜索与二分、交互与信息编码 | bitboard 编码局面，记忆化 minimax 决策；[原文](https://assets.ucup.ac/tutorials/tutorials-4-00-en.pdf)（文件 p.16） |
| [s4-8-G · Game of Pipes](https://contest.ucup.ac/contest/2668/problem/15450) | S4 Poland | 交互与信息编码、图论、概率期望与随机化 | 从末层恢复管道自动机，随机前缀与区分后缀定位状态；[原文](https://assets.ucup.ac/tutorials/tutorials-4-08-pl.pdf)（文件 p.136） |
| [s4-10-A · Automatized Mineral Classification](https://contest.ucup.ac/contest/2814/problem/16000) | S4 Wrocław | 交互与信息编码、概率期望与随机化、数据结构 | 随机队列合并同色元素，生日悖论分析询问量；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.45） |
| [s4-10-B · Bit Recovery](https://contest.ucup.ac/contest/2814/problem/16001) | S4 Wrocław | 多项式与线性代数、位运算与状态压缩、交互与信息编码 | 恢复缺一维线性子空间，取交恢复隐藏基向量；[原文](https://assets.ucup.ac/tutorials/tutorials-4-10-en.pdf)（文件 p.104） |
| [s4-19-D · Detecting the Missing Ship](https://contest.ucup.ac/contest/3426/problem/17263) | S4 Belarus | 交互与信息编码、贪心 | 优先打边界格，每次排除最多候选行列；[原文](https://assets.ucup.ac/tutorials/tutorials-4-19-en.pdf)（文件 p.3） |
| [s4-22-H · How to Validate Such a Program](https://contest.ucup.ac/contest/3575/problem/17720) | S4 Kyoto | 多项式与线性代数、交互与信息编码、树上算法 | Newton 恒等式恢复行列式，树距离矩阵公式定位结构；[原文](https://assets.ucup.ac/tutorials/tutorials-4-22-en.pdf)（文件 p.7） |
| [s4-Extra-3-C · Glitch](https://contest.ucup.ac/contest/2757/problem/15519) | S4 Osijek | 搜索与二分、交互与信息编码 | 奇长度区间始终有解，二分缩小候选段；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.1） |
| [s4-Extra-3-K · Hidden Digits](https://contest.ucup.ac/contest/2757/problem/15527) | S4 Osijek | 交互与信息编码 | 大于二的长度答案固定，小规模整串询问；[原文](https://assets.ucup.ac/tutorials/tutorials-4-e3-en.pdf)（文件 p.4） |
| [s5-6-L · Consecutive Pairs](https://contest.ucup.ac/contest/4617/problem/23680) | S5 Hyakumanben | 交互与信息编码、搜索与二分、图论 | 区间边数询问恢复隐藏路径，每个右端点二分找邻居；[原文](https://contest.ucup.ac/download.php?type=attachments&id=4617&r=1)（文件 p.23） |
