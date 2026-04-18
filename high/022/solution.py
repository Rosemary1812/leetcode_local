# ===== 22. 括号生成 =====
# 难度: 中等
# 英文名: Generate Parentheses
# 来源: https://leetcode.cn/problems/generate-parentheses/description/
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# "((()))",
# "(()())",
# "(())()",
# "()(())",
# "()()()"
# ]
#
# ---------------------------------------------------------


def generateParenthesis(n):
    ans = []
    path = []
    def dfs(left, right):
        if right == n:
            ans.append(''.join(path))
            return
        
        if left < n:
            path.append('(')
            dfs(left + 1, right)
            path.pop()
        
        if right < left:
            path.append(')')
            dfs(left, right + 1)
            path.pop()
    
    dfs(0, 0)
    return ans
print(generateParenthesis(1))   # ["()"]
print(generateParenthesis(2))   # ["(())", "()()"]
print(generateParenthesis(3))   # ["((()))", "(()())", "(())()", "()(())", "()()()"]