# ===== 415. 字符串相加 =====
# 难度: 简单
# 英文名: Add Strings
# 来源: https://leetcode.cn/problems/add-strings/description/
# 标签: codetop
#
# 给定两个字符串形式的非负整数 num1 和 num2，计算它们的和并以字符串形式返回。
#
# ---------------------------------------------------------

# 思路：双指针从末尾往前逐位相加，维护进位 carry。
#   注意循环结束后 carry 可能还有值。
# 时间复杂度：O(max(m,n))
# 空间复杂度：O(max(m,n))


def add_strings(num1, num2):
    res = []
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0 or carry:
        a = int(num1[i]) if i >= 0 else 0
        b = int(num2[j]) if j >= 0 else 0
        total = a + b + carry
        res.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(reversed(res))


print(add_strings("11", "123"))
print(add_strings("456", "77"))
print(add_strings("0", "0"))
print(add_strings("999", "1"))
