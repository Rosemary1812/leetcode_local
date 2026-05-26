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


def addStrings(num1: str, num2: str) -> str:
    res = ""
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        tmp = n1 + n2 + carry
        carry = tmp // 10
        res = str(tmp % 10) + res
        i, j = i - 1, j - 1
    return "1" + res if carry else res


print(addStrings("11", "124"))
print(addStrings("456", "77"))
print(addStrings("11", "12409087"))
