# ===== 70. 爬楼梯 =====
# 难度: 简单
# 英文名: Climbing Stairs
# 来源: https://leetcode.cn/problems/climbing-stairs/description/
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？
#
# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#
# ---------------------------------------------------------
#


def stairs(n):
    pre = 0
    cur = 1
    for _ in range(n):
        pre, cur = cur, pre + cur
    return cur


print(stairs(2))
print(stairs(3))
print(stairs(5))
print(stairs(10))


# 如果写成
# pre=cur
# cur=pre+cur

# ● 有问题。pre = cur 和 cur = pre + cur 不是同时执行的，导致 pre
#   被提前更新了。

#   问题分析：
#   - pre = cur 先执行，pre 变成了 cur 的值
#   - cur = pre + cur 时，pre 已经是新的值了，等于 cur + cur = 2 * cur
#   - 结果是 2 的幂次，不是斐波那契数列

#   当前输出：
#   stairs(2) = 4
#   stairs(3) = 8
#   stairs(5) = 32
#   stairs(10) = 1024

#   修复方法： 使用同时赋值

#   def stairs(n):
#       pre = 0
#       cur = 1
#       for _ in range(n):
#           pre, cur = cur, pre + cur
#       return cur

#   正确输出：
#   stairs(2) = 2
#   stairs(3) = 3
#   stairs(5) = 8
#   stairs(10) = 89
