# ===== 4. 寻找两个正序数组的中位数 =====
# 难度: 困难
# 英文名: Median of Two Sorted Arrays
# 来源: https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
# 标签: codetop
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#
# ---------------------------------------------------------

# 思路：二分查找。在较短的数组上二分，将两个数组各分成左右两部分，
#   使得左半部分长度等于右半部分，且左半部分最大值 <= 右半部分最小值。
#   设 nums1 切在 i，nums2 切在 j = (m+n+1)//2 - i，
#   检查 nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]。
# 时间复杂度：O(log(min(m,n)))
# 空间复杂度：O(1)


def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left1 = nums1[i - 1] if i > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")
        left2 = nums2[j - 1] if j > 0 else float("-inf")
        right2 = nums2[j] if j < n else float("inf")
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            hi = i - 1
        else:
            lo = i + 1


print(find_median_sorted_arrays([1, 3], [2]))
print(find_median_sorted_arrays([1, 2], [3, 4]))
