# 二叉树题解汇总

## 目录

| # | 题目 | 难度 | 状态 | 标签 |
|---|------|------|------|------|
| 94 | 二叉树的中序遍历 | 中等 | Done | 遍历 |
| 101 | 对称二叉树 | 简单 | Done | 递归 |
| 102 | 二叉树的层序遍历 | 中等 | Done | BFS |
| 103 | 二叉树的锯齿形层次遍历 | 中等 | Done | BFS |
| 105 | 从前序与中序遍历序列构造二叉树 | 中等 | TODO | 构造 |
| 107 | 二叉树的层序遍历 II | 中等 | Done | BFS |
| 124 | 二叉树中的最大路径和 | 困难 | Done | DFS |
| 199 | 二叉树的右视图 | 中等 | Done | BFS |
| 236 | 二叉树的最近公共祖先 | 中等 | Done | DFS |
| 337 | 打家劫舍 III | 中等 | TODO | DFS/DP |
| 437 | 路径总和 III | 中等 | TODO | DFS |

---

## 一、模板代码

### 1. TreeNode 定义

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 2. 递归遍历（前序 / 中序 / 后序）

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### 3. BFS 层序遍历（推荐写法）

```python
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
```

### 4. 最大深度

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 5. 数组建树

```python
from collections import deque

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root
```

---

## 二、题解详解

### 94. 二叉树的中序遍历

**思路：** 递归，左 → 根 → 右。

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

---

### 101. 对称二叉树

**思路：** 递归比较左子树和右子树是否镜像对称。左子树的左孩子 vs 右子树的右孩子，左子树的右孩子 vs 右子树的左孩子。

```python
def isSymmetric(root):
    def compare(left, right):
        if left is None or right is None:
            return left is right
        if left.val != right.val:
            return False
        return compare(left.left, right.right) and compare(left.right, right.left)
    if root is None:
        return True
    return compare(root.left, root.right)
```

---

### 102. 二叉树的层序遍历

**思路：** BFS，用 `cur` 存当前层，`nxt` 存下一层。遍历 `cur` 的同时把子节点加入 `nxt`，最后 `cur = nxt`。

```python
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
```

---

### 103. 二叉树的锯齿形层次遍历

**思路：** 和 102 一样做层序遍历，偶数层翻转即可。

```python
def zigzagLevelOrder(root):
    if not root:
        return []
    res = []
    cur = [root]
    depth = 1
    while cur:
        level = []
        nxt = []
        for node in cur:
            level.append(node.val)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        if depth % 2 == 0:
            level.reverse()
        res.append(level)
        cur = nxt
        depth += 1
    return res
```

---

### 105. 从前序与中序遍历序列构造二叉树

**思路：** 前序第一个是根，在中序中找到根的位置 `mid`，左边 `mid` 个是左子树，右边是右子树。递归构造。

```python
def buildTree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root
```

---

### 107. 二叉树的层序遍历 II

**思路：** 标准层序遍历，最后 `res[::-1]` 翻转，变成从底向上。

```python
def levelOrderBottom(root):
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
    return res[::-1]
```

---

### 124. 二叉树中的最大路径和

**思路：** 后序 DFS。每个节点计算自己能向上贡献的最大收益（只能选一边），同时用全局变量记录经过当前节点的最大路径和（可以走两边）。

```python
ans = float("-inf")

def max_gain(node):
    if not node:
        return 0
    left = max(max_gain(node.left), 0)
    right = max(max_gain(node.right), 0)
    global ans
    ans = max(ans, node.val + left + right)
    return node.val + max(left, right)

def maxPathSum(root):
    global ans
    ans = float("-inf")
    max_gain(root)
    return ans
```

---

### 199. 二叉树的右视图

**思路：** BFS 层序遍历，每层取最后一个节点 `cur[-1].val`。

```python
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
```

---

### 236. 二叉树的最近公共祖先

**思路：** 后序递归。如果当前节点是 p 或 q，返回当前节点。左右子树都有返回值说明 p、q 分布在两侧，当前节点就是 LCA。否则返回非空的那一侧。

```python
def lowestCommonAncestor(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
```

---

## 三、套路总结

### BFS 层序遍历变形题统一模板

所有层序遍历的变形题（102 / 103 / 107 / 199）都用同一个框架，区别只在"怎么处理每一层"：

```python
def solve(root):
    if not root:
        return ...
    res = []
    cur = [root]
    while cur:
        # ===== 在这里对当前层做不同操作 =====
        # 102: 把所有值加入 level
        # 103: 偶数层翻转
        # 107: 最后翻转整个结果
        # 199: 只取 cur[-1].val
        # ==================================
        nxt = []
        for node in cur:
            if node.left:  nxt.append(node.left)
            if node.right: nxt.append(node.right)
        cur = nxt
    return res
```

### DFS 递归变形题统一模板

后序 DFS 适用于需要"先知道子树信息再处理当前节点"的场景：

```python
def dfs(node):
    if not node:
        return 基础值
    left = dfs(node.left)    # 先处理左子树
    right = dfs(node.right)  # 再处理右子树
    # 用 left 和 right 的结果计算当前节点的返回值
    return 当前节点的返回值
```

适用题目：101（对称比较）、124（最大路径和）、236（最近公共祖先）。
