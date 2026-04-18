# ===== 101. 对称二叉树 =====
# 难度: 简单
# 英文名: Symmetric Tree
# 来源: https://leetcode.cn/problems/symmetric-tree/description/
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# 1
# / \
# 2   2
# / \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# 1
# / \
# 2   2
# \   \
# 3    3
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
# ---------------------------------------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isSy(root):
    def compare(left, right):
        if left is None or right is None:
            return left is right
        if left.val != right.val:
            return False
        return compare(left.left, right.right) and compare(left.right, right.left)

    if root is None:
        return True
    return compare(root.left, root.right)


def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = [root]
    i = 1

    while i < len(arr):
        node = q.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


print(isSy(build_tree([1, 2, 2, 3, 4, 4, 3])))
print(isSy(build_tree([1, 2, 2, None, 3, None, 3])))
print(isSy(build_tree([1])))
