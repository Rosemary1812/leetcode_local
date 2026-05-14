# ===== 124. 二叉树中的最大路径和 =====
# 难度: 困难
# 英文名: Binary Tree Maximum Path Sum
# 来源: https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
# 标签: codetop
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1：
# 
# 输入：[1,2,3]
# 
# 1
# / \
# 2   3
# 
# 输出：6
# 示例 2：
# 
# 输入：[-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出：42
#
# ---------------------------------------------------------

# 思路：后序遍历 DFS。对每个节点，计算经过它的最大路径和：
#   max_gain(node) = node.val + max(左子树贡献, 右子树贡献, 0)
# 其中子树贡献为负则取 0（不选）。在递归中同时用全局变量 ans 更新：
#   ans = max(ans, node.val + left + right)
# 注意 max_gain 返回给父节点时只能选一边（路径不能分叉），但更新 ans 时可以两边都选。
# 时间复杂度：O(n)，每个节点访问一次。
# 空间复杂度：O(h)，递归栈深度等于树高，最坏 O(n)。


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def build_tree(arr):
    if not arr:
        return
    root = TreeNode(arr[0])
    q = [root]
    i = 1
    while q and i < len(arr):
        node = q.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


ans = float("-inf")


def max_gain(node):
    if not node:
        return 0
    left = max(max_gain(node.left), 0)
    right = max(max_gain(node.right), 0)
    global ans
    ans = max(ans, node.val + left + right)
    return node.val + max(left, right)


def max_path_sum(root):
    global ans
    ans = float("-inf")
    max_gain(root)
    return ans


arr = [-10, 9, 20, None, None, 15, 7]
root = build_tree(arr)
print(max_path_sum(root))
