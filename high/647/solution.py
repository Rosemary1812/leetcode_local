# ## 题目描述

# 给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

# **回文字符串** 是正着读和倒过来读一样的字符串。

# **子字符串** 是字符串中的由连续字符组成的一个序列。

# **示例 1：**

# ```
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# ```

# **示例 2：**

# ```
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# ```

# **提示：**

# - `1 <= s.length <= 1000`
# - `s` 由小写英文字母组成


def countSubstrings(s):
    def expand(l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        return cnt

    return sum(expand(i, j) for i in range(len(s)) for j in (i, i + 1))


print(countSubstrings("abc"))
print(countSubstrings("aaa"))
