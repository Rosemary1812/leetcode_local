# ===== 347. 前 K 个高频元素 =====
# 难度: 中等
# 英文名: Top K Frequent Elements
# 来源: https://leetcode.cn/problems/top-k-frequent-elements/description/
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
# 你可以按任意顺序返回答案。
#
# 示例 1：
# 输入：nums = [1,1,1,2,2,3], k = 2
# 输出：[1,2]
#
# 示例 2：
# 输入：nums = [1], k = 1
# 输出：[1]
#
# 进阶：你能用 O(n log k) 时间复杂度和 O(n) 空间复杂度解决吗？
#
# ---------------------------------------------------------
from collections import Counter


def topKFrequent(nums, k):
    cnt = Counter(nums)
    max_cnt = max(cnt.values())

    buckets = [[] for _ in range(max_cnt + 1)]
    for x, c in cnt.items():
        buckets[c].append(x)
    ans = []
    for bucket in reversed(buckets):
        ans += bucket
        if len(ans) >= k:
            return ans


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))


# ● 这是一个用桶排序（Bucket Sort）思路求 Top K 高频元素的算法。

#   核心思想

#   1. 统计频率 — 用 Counter 统计每个数出现的次数
#   2. 按频次入桶 — 创建 max_cnt + 1 个桶，下标 = 出现次数，桶里放所有出现该次数的数
#   3. 逆序遍历桶 — 从高频到低频收集答案

#   图解流程

#   假设 nums = [1,1,1,2,2,3], k = 2

#   Step 1: Counter = {1:3, 2:2, 3:1}
#   Step 2: max_cnt = 3
#           buckets = [[], [], [], []]  # 0,1,2,3

#           1出现3次 → buckets[3] = [1]
#           2出现2次 → buckets[2] = [2]
#           3出现1次 → buckets[1] = [3]

#           buckets = [[], [3], [2], [1]]
#                             ↑   ↑
#                             2   1(最高)

#   Step 3: 逆序遍历: [1] → ans=[1]; [2] → ans=[1,2], len(ans)=2≥k, return

#   复杂度

#   ┌──────┬───────────────────────────────┐
#   │ 指标 │            复杂度             │
#   ├──────┼───────────────────────────────┤
#   │ 时间 │ O(n) — 统计 O(n)，桶排序 O(n) │
#   ├──────┼───────────────────────────────┤
#   │ 空间 │ O(n) — Counter + buckets      │
#   └──────┴───────────────────────────────┘

#   对比

#   相比 HEAP 方法（O(n log k)），桶排序在"频率范围有限"时更快，直接 O(n)。
