// ===== 22. 括号生成 =====
// 难度: 中等
// 英文名: Generate Parentheses
// 来源: https://leetcode.cn/problems/generate-parentheses/description/
//
// 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
//
// 示例：
//
// 输入：n = 3
// 输出：[
// "((()))",
// "(()())",
// "(())()",
// "()(())",
// "()()()"
// ]
//
// ---------------------------------------------------------
function generatePar(n) {
  const ans = [];
  const path = Array(n * 2);

  function dfs(left, right) {
    if (right === n) {
      ans.push(path.join(""));
      return;
    }

    if (left < n) {
      path[left + right] = "(";
      dfs(left + 1, right);
    }
    if (right < left) {
      path[left + right] = ")";
      dfs(left, right + 1);
    }
  }

  dfs(0, 0);
  return ans;
}

console.log(generatePar(3));
