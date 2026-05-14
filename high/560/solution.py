# ===== 560. 和为 K 的子数组 =====
# 难度: 中等
# 英文名: Subarray Sum Equals K
# 来源: https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
# ---------------------------------------------------------
# from collections import defaultdict


# def subarraySum(nums, k):
#     cnt = defaultdict(int)
#     cnt[0] = 1
#     ans = s = 0

#     for num in nums:
#         s += num
#         ans += cnt[s - k]
#         cnt[s] += 1
#     return ans


# print(subarraySum([1, 1, 1], 2))
# print(subarraySum([2, 2, 2], 3))
# print(subarraySum([3, 4, 7, 2, -3, 1, 4], 7))

from collections import defaultdict


def subarray(nums, k):
    cnt = defaultdict(int)
    cnt[0] = 1
    ans = s = 0
    for num in nums:
        s += num
        ans += cnt[s - k]
        cnt[s] += 1
    return ans


print(subarray([1, 1, 1], 2))


# ● defaultdict 是 Python collections 模块里的字典子类。
#   和普通 dict 的区别
#   普通字典访问不存在的 key 会报 KeyError：
#   d = {}
#   d['a']  # KeyError: 'a'
#   defaultdict 访问不存在的 key 时，会自动创建一个默认值：
#   from collections import defaultdict
#   d = defaultdict(int)   # 默认值是 int() 即 0
#   d['a']                  # 不报错，返回 0
#   d['b'] += 1             # d['b'] 变成 1
#   d2 = defaultdict(list)  # 默认值是 list() 即 []
#   d2['x'].append(1)       # d2['x'] 变成 [1]
#   为什么这题用它
#   代码里 cnt[s - k] 要读取一个可能不存在的 key。用 defaultdict(int) 就不用每次手动判断 key
#   是否存在，不存在时自动返回 0，省了 if s-k in cnt 这种判断，代码更简洁。
