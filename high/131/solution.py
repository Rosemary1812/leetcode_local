# ===== 131. 分割回文串 =====
# 难度: 中等
# 英文名: Palindromic Partitioning
# 来源: https://leetcode.cn/problems/palindromic-partitioning/description/
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ["aa","b"],
# ["a","a","b"]
# ]
#
# ---------------------------------------------------------
# def partition(s):
#     n, ans, path = len(s), [], []

#     def is_pal(l, r):
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l, r = l + 1, r - 1
#         return True

#     def dfs(start):
#         if start == n:  # 遍历完 → 加答案
#             ans.append(path.copy())
#             return
#         for i in range(start, n):  # 枚举所有子串 s[start..i]
#             if is_pal(start, i):
#                 path.append(s[start : i + 1])
#                 dfs(i + 1)
#                 path.pop()

#     dfs(0)
#     return ans


def par(s):
    n, ans, path = len(s), [], []

    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def dfs(start):
        if start == n:
            ans.append(path.copy())
            return
        for i in range(start, n):
            if is_pal(start, i):
                path.append(s[start : i + 1])
                dfs(i + 1)
                path.pop()

    dfs(0)
    return ans


print(par("aab"))
