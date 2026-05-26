# ===== 93. 复原IP地址 =====
# 难度: 中等
# 英文名: Restore IP Addresses
# 来源: https://leetcode.cn/problems/restore-ip-addresses/description/
# 标签: codetop
#
# 给定一个只包含数字的字符串 s ，用它来恢复 IP 地址。
#
# ---------------------------------------------------------

# 思路：回溯。IP 地址分 4 段，每段 1~3 位数字，不能有前导零，值不超过 255。
#   每层选择当前段的长度（1/2/3），递归处理剩余部分。
# 时间复杂度：O(1)，最多 3^4 = 81 种组合。
# 空间复杂度：O(1)
# ● 这道题的核心思路是回溯法，逐段构建合法的 IP 地址。

#   IP 地址的约束

#   一个有效 IP 地址由 4 段组成，每段必须满足：
#   - 长度 1~3 位
#   - 不能有前导零（"01" 非法，"0" 合法）
#   - 数值不超过 255

# def restore_ip_addresses(s):
#     res = []

#     def backtrack(start, parts):
#         if len(parts) == 4:
#             if start == len(s):
#                 res.append(".".join(parts))
#             return
#         for length in range(1, 4):
#             if start + length > len(s):
#                 break
#             segment = s[start : start + length]
#             if len(segment) > 1 and segment[0] == "0":
#                 break
#             if int(segment) > 255:
#                 break
#             backtrack(start + length, parts + [segment])

#     backtrack(0, [])
#     return res


def restore_ip(s):
    res = []

    def back(start, parts):
        if len(parts) == 4:
            if start == len(s):
                res.append(".".join(parts))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            segement = s[start : start + length]
            if len(segement) > 1 and segement[0] == "0":
                break
            if len(segement) > 255:
                break
            back(start + length, parts + [segement])

    back(0, [])
    return res


print(restore_ip("25525511135"))
print(restore_ip("0000"))
print(restore_ip("1111"))
print(restore_ip("010010"))


# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：

# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：

# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"
