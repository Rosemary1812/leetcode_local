# ===== 215. 数组中的第K个最大元素 =====
# 难度: 中等
# 英文名: Kth Largest Element in an Array
# 来源: https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
# ---------------------------------------------------------

from random import randint


def partition(nums, left, right):
    i = randint(left, right)
    # randint(left, right) 是从 [left, right]
    #   范围内随机取一个整数，赋给 i，然后用 nums[i] 作为 pivot。
    pivot = nums[i]
    nums[i], nums[left] = nums[left], nums[i]

    i, j = left + 1, right
    while True:
        while i <= j and nums[i] < pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1

        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[left], nums[j] = nums[j], nums[left]
    return j


def findKthLargest(nums, k):
    n = len(nums)
    target_index = n - k
    left, right = 0, n - 1
    while True:
        i = partition(nums, left, right)
        if i == target_index:
            return nums[i]
        if i > target_index:
            right = i - 1
        else:
            left = i + 1


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# ● 215. 数组中的第K个最大元素 — 快速选择算法详解

#   核心思路

#   不需要完整排序，利用快速排序的 partition 特性：每次 partition
#    后，pivot 元素会落在它最终排好序时的正确位置。

#   目标：找第 k 大 = 找从小到大排序后，索引为 n-k 的元素。

#   ---
#   partition 函数逐步解析

#   def partition(nums, left, right):
#       i = randint(left, right)   # 随机选 pivot，避免最坏情况
#   O(n²)
#       pivot = nums[i]
#       nums[i], nums[left] = nums[left], nums[i]  # 把 pivot
#   挪到最左边暂存

#       i, j = left+1, right      # 双指针：i 从左往右，j从右往左
#       while True:
#           while i <= j and nums[i] < pivot:  # i 找第一个 >=
#   pivot 的
#               i += 1
#           while i <= j and nums[j] > pivot:  # j 找第一个 <=pivot 的
#               j -= 1

#           if j >= i:
#               break
#           nums[i], nums[j] = nums[j], nums[i]
#           i += 1
#           j -= 1

#       nums[left], nums[j] = nums[j], nums[left]  # pivot放到最终位置 j
#       return j  # j 就是 pivot 的最终索引

#   ---
#   partition 执行后的状态

#   [小于pivot | pivot | 大于pivot]
#    left...j-1    j    j+1...right

#   pivot 的位置 j 是它在完整排序后的最终正确位置。

#   ---
#   主函数逻辑

#   target_index = n - k   # 第 k 大 = 正序排列第 n-k
#   个（0-indexed）

#   while True:
#       i = partition(nums, left, right)

#       if i == target_index:    # 幸运：pivot 正好是答案
#           return nums[i]
#       if i > target_index:     # pivot 太靠右，答案在左半部分
#           right = i - 1
#       else:                    # pivot 太靠左，答案在右半部分
#           left = i + 1

#   每次排除一侧，不需要递归两侧，这是比快速排序更高效的地方。

#   ---
#   复杂度

#   ┌──────┬────────────────────────────────┬──────┐
#   │      │              时间               │ 空间 │
#   ├──────┼────────────────────────────────┼──────┤
#   │ 平均  │ O(n)                            │ O(1) │
#   ├──────┼────────────────────────────────┼──────┤
#   │ 最坏  │ O(n²)（用随机 pivot 极少触发）    │ O(1) │
#   └──────┴────────────────────────────────┴──────┘

#   ---
#   修复后的正确 partition
