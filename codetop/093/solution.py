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


def restore_ip_addresses(s):
    res = []

    def backtrack(start, parts):
        if len(parts) == 4:
            if start == len(s):
                res.append(".".join(parts))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if len(segment) > 1 and segment[0] == "0":
                break
            if int(segment) > 255:
                break
            backtrack(start + length, parts + [segment])

    backtrack(0, [])
    return res


print(restore_ip_addresses("25525511135"))
print(restore_ip_addresses("0000"))
print(restore_ip_addresses("1111"))
print(restore_ip_addresses("010010"))
