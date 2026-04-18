# ===== 5. 最长回文子串 =====
# 难度: 中等
# 英文名: Longest Palindromic Substring
# 来源: https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设  s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
#
# ---------------------------------------------------------

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longest=""
    def expand(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    for i in range(len(s)):
        odd=expand(i,i)
        even=expand(i,i+1)
        # longest=Math.max(longest,odd,even);
        if(len(odd)>len(longest)):
            longest=odd
        if(len(even)>len(longest)):
            longest=even
    return longest

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))