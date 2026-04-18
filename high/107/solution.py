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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    if root is None:
        return []
    ans = []
    cur = [root]
    while cur:
        nxt = []
        val = []
        for node in cur:
            val.append(node.val)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        cur = nxt
        ans.append(val)
    return ans[::-1]


def build_tree(arr):
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


print(levelOrderBottom(build_tree([3, 9, 20, None, None, 15, 7])))
