# ===== 165. 比较版本号 =====
# 难度: 中等
# 英文名: Compare Version Numbers
# 来源: https://leetcode.cn/problems/compare-version-numbers/description/
# 标签: codetop
#
# 给你两个版本号 version1 和 version2，比较它们的大小。
#
# ---------------------------------------------------------

# 思路：按 '.' 分割后逐段比较数值。较短的版本号缺失的段补 0。
# 时间复杂度：O(n)，n 为版本号字符串长度。
# 空间复杂度：O(n)，分割后的列表。


def compare_version(version1, version2):
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))
    for i in range(max(len(v1), len(v2))):
        a = v1[i] if i < len(v1) else 0
        b = v2[i] if i < len(v2) else 0
        if a < b:
            return -1
        if a > b:
            return 1
    return 0


print(compare_version("1.01", "1.001"))
print(compare_version("1.0", "1.0.0"))
print(compare_version("0.1", "1.1"))
print(compare_version("1.0.1", "1"))
print(compare_version("7.5.2.4", "7.5.3"))
