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


def minDis(s, t):
    """
    动态规划计算编辑距离（空间优化版）。

    DP 定义：f[i][j] = 将 s[0..i-1] 变成 t[0..j-1] 所需最少操作数
    初始化：
        f[0][j] = j（空串变 t 前 j 字符，需要 j 次插入）
        f[i][0] = i（s 前 i 字符变空串，需要 i 次删除）
    转移（s[i-1] vs t[j-1]）：
        如果相等 → 继承 f[i-1][j-1]
        否则 → min(替换, 删除, 插入) + 1
    本实现用一维数组：f[j] = f[i][j]，pre = f[i-1][j-1]，tem = f[i-1][j+1]
    """
    f = list(range(len(t) + 1))  # f[j] = j，即 f[0][j] = j
    for x in s:
        pre = f[0]  # pre 暂存 f[i-1][0]，即对角线起点
        f[0] += 1
        for j, y in enumerate(t):
            tem = f[j + 1]  # tem 暂存 f[i-1][j+1]，下一轮成为 pre
            if x == y:
                # 字符相同，无操作，继承左上角（pre 就是 f[i-1][j-1]）
                f[j + 1] = pre
            else:
                # 字符不同，三选一：
                #   f[j+1]   = f[i-1][j]   → 删除 s[i-1]
                #   f[j]     = f[i][j-1]   → 插入 t[j-1]
                #   pre      = f[i-1][j-1] → 替换 s[i-1] 为 t[j-1]
                f[j + 1] = min(f[j + 1], f[j], pre) + 1
            pre = tem  # 更新 pre = f[i-1][j+1]，为下一轮对角线准备
    return f[-1]  # f[len(s)][len(t)]


print(minDis("horse", "ros"))
print(minDis("intention", "execution"))
