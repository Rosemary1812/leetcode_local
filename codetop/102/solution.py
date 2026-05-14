# ===== 102. 二叉树的层序遍历 =====
# 难度: 中等
# 英文名: Binary Tree Level Order Traversal
# 来源: https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
# 标签: codetop
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# 3
# / \
# 9  20
# /  \
# 15   7
# 返回其层次遍历结果：
#
# [
# [3],
# [9,20],
# [15,7]
# ]
#
# ---------------------------------------------------------

# from collections import deque


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def build_tree(arr):
#     if not arr:
#         return None
#     root = TreeNode(arr[0])
#     q = [root]
#     i = 1
#     while q and i < len(arr):
#         node = q.pop(0)
#         if i < len(arr) and arr[i] is not None:
#             node.left = TreeNode(arr[i])
#             q.append(node.left)
#         i += 1
#         if i < len(arr) and arr[i] is not None:
#             node.right = TreeNode(arr[i])
#             q.append(node.right)
#         i += 1
#     return root


# def level_order(root):
#     if not root:
#         return []
#     res, q = [], deque([root])
#     while q:
#         level = []
#         for _ in range(len(q)):
#             node = q.popleft()
#             level.append(node.val)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         res.append(level)
#     return res

#     return res

# arr = [3, 9, 20, None, None, 15, 7]
# root = build_tree(arr)
# print(level_order(root))


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


def level_order(root):
    if not root:
        return []
    res = []
    cur = [root]
    while cur:
        level = []
        nxt = []
        for node in cur:
            level.append(node.val)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        res.append(level)
        cur = nxt
    return res


arr = [3, 9, 20, None, None, 15, 7]
root = build_tree(arr)
print(level_order(root))
