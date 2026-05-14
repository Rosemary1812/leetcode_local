# ===== 199. 二叉树的右视图 =====
# 难度: 中等
# 英文名: Binary Tree Right Side View
# 来源: https://leetcode.cn/problems/binary-tree-right-side-view/description/
# 标签: codetop
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
# 1            <---
# /   \
# 2     3         <---
# \     \
# 5     4       <---
#
# ---------------------------------------------------------

# 思路：BFS 层序遍历，每层取最后一个节点即可。
# 时间复杂度：O(n)，每个节点访问一次。
# 空间复杂度：O(n)，队列最多存一层节点，最宽层 n/2。

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


# def right_side_view(root):
#     if not root:
#         return []
#     res = []
#     q = deque([root])
#     while q:
#         for _ in range(len(q)):
#             node = q.popleft()
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         res.append(node.val)  # 当前层最后一个节点
#     return res


# arr = [1, 2, 3, None, 5, None, 4]
# root = build_tree(arr)
# print(right_side_view(root))

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr):
    if not arr:
        return
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def rightSideView(root):
    if root is None:
        return []
    ans = []
    cur = [root]
    while cur:
        ans.append(cur[-1].val)
        nxt = []
        for node in cur:
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        cur = nxt
    return ans
