# ===== 94. 二叉树的中序遍历 =====
# 难度: 中等
# 英文名: Binary Tree Inorder Traversal
# 来源: https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# 1
# \
# 2
# /
# 3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
# ---------------------------------------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left


def ino(root):
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)

    ans = []
    dfs(root)
    return ans


def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


print(ino(build_tree([1, None, 2, 3])))
