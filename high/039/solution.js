// ===== 39. 组合总和 =====
// 难度: 中等
// 英文名: Combination Sum
// 来源: https://leetcode.cn/problems/combination-sum/description/
//
// 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
//
// candidates 中的数字可以无限制重复被选取。
//
// 说明：
//
// 所有数字（包括 target）都是正整数。
// 解集不能包含重复的组合。
// 示例 1：
//
// 输入：candidates = [2,3,6,7], target = 7,
// 所求解集为：
// [
// [7],
// [2,2,3]
// ]
// 示例 2：
//
// 输入：candidates = [2,3,5], target = 8,
// 所求解集为：
// [
// [2,2,2,2],
// [2,3,3],
// [3,5]
// ]
//
//
// 提示：
//
// 1 <= candidates.length <= 30
// 1 <= candidates[i] <= 200
// candidate 中的每个元素都是独一无二的。
// 1 <= target <= 500
//
// ---------------------------------------------------------

// 回溯

function comSum(candidates, target) {
  const res = [],
    path = [];
  candidates.sort((a, b) => a - b);
  back(0, 0);
  return res;

  function back(start, sum) {
    if (sum === target) {
      res.push(Array.from(path));
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      const n = candidates[i];
      if (n > target - sum) break;
      path.push(n);
      sum += n;
      back(i, sum);
      path.pop();
      sum -= n;
    }
  }
}

console.log(comSum([2, 3, 6, 7], 7));
console.log(comSum([2, 3, 5], 8));
