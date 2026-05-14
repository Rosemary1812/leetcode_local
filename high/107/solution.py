# ===== 107. 二叉树的层序遍历 II =====
# 难度: 中等
# 英文名: Binary Tree Level Order Traversal II
# 来源: https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/
#
# 给你二叉树的根节点 root ，返回其节点值自底向上的层序遍历结果。即按从左到右、从叶到根的顺序，逐层返回每层节点值。
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[15,7],[9,20],[3]]
#
# 示例 2：
# 输入：root = [1]
# 输出：[[1]]
#
# 示例 3：
# 输入：root = []
# 输出：[]
#
# ---------------------------------------------------------
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def level_order(root):
    if not root:
        return []
    res = []

    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res[::-1]


arr = [3, 9, 20, None, None, 15, 7]
root = buildTree(arr)
print(level_order(root))  # [[15, 7], [9, 20], [3]]
