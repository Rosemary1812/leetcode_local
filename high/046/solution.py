# ===== 46. 全排列 =====
# 难度: 中等
# 英文名: Permutations
# 来源: https://leetcode.cn/problems/permutations/description/
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# [1,2,3],
# [1,3,2],
# [2,1,3],
# [2,3,1],
# [3,1,2],
# [3,2,1]
# ]
#
# ---------------------------------------------------------
def premute(nums):
    res = []
    path = []
    used = [False] * len(nums)

    def back():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            back()
            path.pop()
            used[i] = False

    back()
    return res


print(premute([1, 2, 3]))
print(premute([1, 4, 7]))
