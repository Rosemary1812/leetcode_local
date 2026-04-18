# ===== 79. 单词搜索 =====
# 难度: 中等
# 英文名: Word Search
# 来源: https://leetcode.cn/problems/word-search/description/
#
# https://leetcode.com/problems/word-search/
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
# ['A','B','C','E'],
# ['S','F','C','S'],
# ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
# ---------------------------------------------------------


def exist(board, word):
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k + 1 == len(word):
            return True
        board[i][j] = 0
        for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
            if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                return True
        board[i][j] = word[k]
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
)  # True
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
)  # True
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
)  # False
