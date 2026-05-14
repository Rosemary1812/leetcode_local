# ===== 103. 二叉树的锯齿形层次遍历 =====
# 难度: 中等
# 英文名: Binary Tree Zigzag Level Order Traversal
# 来源: https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
# 标签: codetop
#
# 和leetcode 102 基本是一样的，思路是完全一样的。
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# 3
# / \
# 9  20
# /  \
# 15   7
# 返回锯齿形层次遍历如下：
#
# [
# [3],
# [20,9],
# [15,7]
# ]
#
# ---------------------------------------------------------

# from collections import deque


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.right = right
#         self.left = left


# def build_tree(arr):
#     if not arr:
#         return
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


# def zigzag_level_order(root):
#     if not root:
#         return []
#     res = []
#     q = deque([root])
#     depth = 0
#     while q:
#         level = []
#         for _ in range(len(q)):
#             node = q.popleft()
#             level.append(node.val)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         if depth % 2 == 1:
#             level.reverse()
#         res.append(level)
#         depth += 1
#     return res


# arr = [3, 9, 20, None, None, 15, 7]
# root = build_tree(arr)
# print(zigzag_level_order(root))


from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


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


def zigzag_level_tree(root):
    if not root:
        return []
    res = []
    q = deque([root])
    depth = 1
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if depth % 2 == 0:
            level.reverse()
        res.append(level)
        depth += 1
    return res


print(
    zigzag_level_tree(build_tree([3, 9, 20, None, None, 15, 7]))
)  # [[3], [20, 9], [15, 7]]
print(zigzag_level_tree(build_tree([1])))  # [[1]]
print(zigzag_level_tree(build_tree([])))  # []
