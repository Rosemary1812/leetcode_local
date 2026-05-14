# ===== 20. 有效的括号 =====
# 难度: 简单
# 英文名: Valid Parentheses
# 来源: https://leetcode.cn/problems/valid-parentheses/description/
# 标签: codetop
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
#
# ---------------------------------------------------------

# 思路：栈。遇到左括号入栈，遇到右括号检查栈顶是否匹配。
#   最后栈为空则有效。
# 时间复杂度：O(n)
# 空间复杂度：O(n)


def is_valid(s):
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in match:
            if not stack or stack[-1] != match[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return not stack


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
