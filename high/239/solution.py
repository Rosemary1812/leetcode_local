# ===== 239. 滑动窗口最大值 =====
# 难度: 困难
# 英文名: Sliding Window Maximum
# 来源: https://leetcode.cn/problems/sliding-window-maximum/description/
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#
#
# 提示：
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
# ---------------------------------------------------------


from collections import deque


def max_window(nums, k):
    ans = [0] * (len(nums) - k + 1)
    q = deque()

    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        left = i - k + 1
        if q[0] < left:
            q.popleft()
        if left >= 0:
            ans[left] = nums[q[0]]
    return ans


print(max_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_window([1], 1))  # [1]
print(max_window([1, -1], 1))  # [1, -1]
print(max_window([9, 11], 2))  # [11]
print(max_window([4, -2], 2))
