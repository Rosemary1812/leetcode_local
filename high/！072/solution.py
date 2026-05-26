# ===== 72. 编辑距离 =====
# 难度: 困难
# 英文名: Edit Distance
# 来源: https://leetcode.cn/problems/edit-distance/description/
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数。
#
# 你可以对一个单词进行如下操作：
# - 插入一个字符
# - 删除一个字符
# - 替换一个字符
#
# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
#
# ---------------------------------------------------------


# def minDistance(s, t):
#     f = list(range(len(t) + 1))
#     for x in s:
#         pre = f[0]
#         f[0] += 1
#         for j, y in enumerate(t):
#             tmp = f[j + 1]
#             f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
#             pre = tmp
#     return f[-1]


def minDis(s,t):
  n=len(s)
  m=len(t)
  f=[[0]*(m+1)for _ in range(n+1)]
  for i in range(n+1):
    f[i][0]=i
  for j in range(m+1):
    f[0][j]=j
  for i in range(n+1):
    for j in range(m+1):
      if s[i-1]==t[j-1]
        f[i][j]=f[i-1][j-1]
      else:
        f[i][j]=min(f[i-1][j],f[j-1][i],f[i-1][j-1])+1
  return f[n][m]

w1 = "intention"
w2 = "execution"
print(minDis(w1, w2))
