# ===== 33. 搜索旋转排序数组 =====
# 难度: 中等
# 英文名: Search in Rotated Sorted Array
# 来源: https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
# 标签: codetop
#
# 给你一个升序排列的整数数组 nums ，和一个整数 target 。
# 
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
# 
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 
# 示例 1：
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 提示：
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4 <= target <= 10^4
#
# ---------------------------------------------------------

# 思路：二分。旋转后数组分为两段有序，每次 mid 将数组分为 [lo, mid] 和 [mid, hi]，
#   其中必有一段是有序的。判断 target 在有序段内则收缩到该段，否则收缩到另一段。
# 时间复杂度：O(log n)
# 空间复杂度：O(1)


def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # 左半段有序
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # 右半段有序
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
