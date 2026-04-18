// ===== 5. 最长回文子串 =====
// 难度: 中等
// 英文名: Longest Palindromic Substring
// 来源: https://leetcode.cn/problems/longest-palindromic-substring/description/
//
// 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设  s 的最大长度为 1000。
// 
// 示例 1：
// 
// 输入: "babad"
// 输出: "bab"
// 注意: "aba" 也是一个有效答案。
// 示例 2：
// 
// 输入: "cbbd"
// 输出: "bb"
//
// ---------------------------------------------------------

function longestPalindrome(s){
    let longest="";
    const expand=(left,right)=>{
        while(left>=0&&right<s.length&&s[left]==s[right]){
            left--;
            right++;
        }
        return s.slice(left+1,right);
    }

    for(let i=0;i<s.length;i++){
        const odd=expand(i,i);
        const even=expand(i,i+1);
        // longest=Math.max(longest,odd,even);
        //!为什么不能Math.max() 因为Math.max()只能比较数字，不能比较字符串
        if(odd.length>longest.length){
            longest=odd;
        }
        if(even.length>longest.length){
            longest=even;
        }
    }
    return longest;
}


console.log(longestPalindrome("babad"));
console.log(longestPalindrome("cbbd"));

//---------------------------------------------------
// Notes:
// 中心扩散 借助expand遍历