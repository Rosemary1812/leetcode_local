# ===== 105. 从前序与中序遍历序列构造二叉树 =====
# 难度: 中等
# 英文名: Construct Binary Tree from Preorder and Inorder Traversal
# 来源: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的前序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
# 示例 1：
# 输入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出：[3,9,20,null,null,15,7]
#
# 示例 2：
# 输入：preorder = [-1], inorder = [-1]
# 输出：[-1]
#

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def buildTree(self, preorder, inorder):
#     if not preorder:
#         return None
#     root_val = preorder[0]
#     root = TreeNode(root_val)
#     mid = inorder.index(root_val)
#     root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#     root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]
#     return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left


def buildTree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root.val)
    # 在这里的作用：找到根节点在中序遍历中的位置，从而确定左子树有多少个节点（mid 个），用来切分前序和中序数组。
    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    # ● 这两行是递归构建左右子树。

    #   以示例为例：
    #   preorder = [3, 9, 20, 15, 7]
    #   inorder  = [9, 3, 15, 20, 7]
    #   root = 3, mid = 1

    #   左子树：
    #   self.buildTree(preorder[1:mid+1], inorder[:mid])
    #   # preorder[1:2] = [9]    ← 前序中，跳过根(1个)，取左子树的(mid个)节点
    #   # inorder[:1]   = [9]    ← 中序中，根左边的就是左子树

    #   右子树：
    #   self.buildTree(preorder[mid+1:], inorder[mid+1:])
    #   # preorder[2:]  = [20, 15, 7]  ← 前序中，剩下的都是右子树
    #   # inorder[2:]   = [15, 20, 7]  ← 中序中，根右边的就是右子树
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(buildTree(preorder, inorder))
