// ===== 3. 无重复字符的最长子串 =====
// 难度: 中等
// 英文名: Longest Substring Without Repeating Characters
// 来源: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
//
// 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
// 
// 示例 1:
// 
// 输入: "abcabcbb"
// 输出: 3
// 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
// 示例 2:
// 
// 输入: "bbbbb"
// 输出: 1
// 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
// 示例 3:
// 
// 输入: "pwwkew"
// 输出: 3
// 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
// 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
//
// ---------------------------------------------------------

function maxStr(str) {
    // TODO: implement
    let left=0;
    let maxLen=0;
    const map=new Map();

    for(let right=0;right<str.length;right++){
        const char=str[right];
        map.set(char,(map.get(char)||0)+1);

        while(map.get(char)>1){
            const leftChar=str[left];   
            map.set(leftChar,map.get(leftChar)-1);
            left++;
        }
        maxLen=Math.max(maxLen,right-left+1);
    }

    return maxLen;
}

console.log(maxStr("abcabcbb"));
console.log(maxStr("bbbbb"));
console.log(maxStr("pwwkew"));



