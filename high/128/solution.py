# ===== 128. 最长连续序列 =====
# 难度: 困难
# 英文名: Longest Consecutive Sequence
# 来源: https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# ---------------------------------------------------------
def longest(nums):
    st = set(nums)  # 把 nums 转成哈希集合
    ans = 0
    for x in st:  # 遍历哈希集合
        if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
            continue
        # x 是序列的起点
        y = x + 1
        while y in st:  # 不断查找下一个数是否在哈希集合中
            y += 1
        # 循环结束后，y-1 是最后一个在哈希集合中的数
        ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
    return ans


print(longest([100, 4, 200, 1, 3, 2]))
