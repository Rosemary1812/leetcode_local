from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


# 递归
# 前序遍历
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


# 中序
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# 后序
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# 层序遍历 BFS
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
    return res


# 最大深度
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
