# 链表题解汇总

## 目录

| # | 题目 | 难度 | 状态 | 标签 |
|---|------|------|------|------|
| 19 | 删除链表的倒数第N个节点 | 中等 | Done | 快慢指针 |
| 21 | 合并两个有序链表 | 简单 | Done | 合并 |
| 23 | 合并K个排序链表 | 困难 | Done | 分治合并 |
| 25 | K个一组翻转链表 | 困难 | Done | 分组反转 |
| 82 | 删除排序链表中的重复元素 II | 中等 | Done | 去重 |
| 92 | 反转链表 II | 中等 | Done | 区间反转 |
| 141 | 环形链表 | 简单 | Done | 快慢指针 |
| 142 | 环形链表 II | 中等 | Done | 快慢指针 |
| 143 | 重排链表 | 中等 | Done | 找中点+反转+合并 |
| 146 | LRU缓存机制 | 中等 | Done | 哈希+双向链表 |
| 160 | 相交链表 | 简单 | Done | 双指针 |
| 206 | 反转链表 | 简单 | Done | 基础反转 |
| 234 | 回文链表 | 简单 | TODO | - |

---

## 一、模板代码

### 1. ListNode 定义

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 2. 数组建链表（dummy 头）

```python
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next
```

### 3. 链表转数组（调试用）

```python
def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
```

### 4. 反转链表（迭代）

```python
def reverse(head):
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre
```

### 5. 找中点（快慢指针）

```python
def find_mid(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # slow 就是中点（偶数个节点时偏左）
```

### 6. 合并两个有序链表

```python
def merge_two(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next
```

---

## 二、题解详解

### 206. 反转链表

**思路：** 三个指针 `pre`、`cur`、`nxt`，每次把 `cur.next` 指向 `pre`，然后三个指针同时往后移。

```python
def reverse(head):
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre
```

---

### 21. 合并两个有序链表

**思路：** dummy 头 + 双指针，每次取较小的节点接到 `cur` 后面，最后把剩余的接上。

```python
def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next
```

---

### 23. 合并K个排序链表

**思路：** 分治法。把 K 个链表两两合并，递归拆成两半，最后合并两个有序链表。时间 O(N log K)。

```python
def merge_k_lists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    def merge(l, r):
        if l == r:
            return lists[l]
        mid = (l + r) // 2
        left = merge(l, mid)
        right = merge(mid + 1, r)
        return merge_two(left, right)
    return merge(0, len(lists) - 1)
```

---

### 25. K个一组翻转链表

**思路：** 先统计长度，然后每 k 个一组做反转。用 `p0` 指向每组的前一个节点，反转后重新连接。

```python
def reverseKGroup(head, k):
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    dummy = ListNode(0, head)
    p0 = dummy
    cur = head
    while n >= k:
        pre = None
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        tail = p0.next
        tail.next = cur
        p0.next = pre
        p0 = tail
        n -= k
    return dummy.next
```

---

### 82. 删除排序链表中的重复元素 II

**思路：** dummy + `pre` 指针。发现 `cur.val == cur.next.val` 时，用 while 循环跳过所有重复值，然后 `pre.next = cur.next`。

```python
def delete_duplicates(head):
    dummy = ListNode(0, head)
    pre = dummy
    cur = head
    while cur:
        if cur.next and cur.val == cur.next.val:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            pre.next = cur.next
        else:
            pre = pre.next
        cur = cur.next
    return dummy.next
```

---

### 92. 反转链表 II

**思路：** 头插法一趟扫描。先走到第 m-1 个节点（pre），然后把后面的节点依次插到 pre 后面。

```python
def reverse_between(head, m, n):
    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(m - 1):
        pre = pre.next
    cur = pre.next
    for _ in range(n - m):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt
    return dummy.next
```

---

### 141. 环形链表

**思路：** 快慢指针。慢走一步、快走两步，如果相遇说明有环。

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

### 142. 环形链表 II

**思路：** 快慢指针找到相遇点后，把一个指针放回头部，两个指针各走一步，再次相遇就是环入口。

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            while slow != head:
                slow = slow.next
                head = head.next
            return slow
    return None
```

---

### 143. 重排链表

**思路：** 三步走：(1) 快慢指针找中点 (2) 反转后半段 (3) 前后两段交替合并。

```python
def reorder_list(head):
    if not head or not head.next:
        return
    # 1. 找中点
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 2. 反转后半段
    pre, cur = None, slow.next
    slow.next = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    # 3. 交替合并
    first, second = head, pre
    while second:
        nxt1, nxt2 = first.next, second.next
        first.next = second
        second.next = nxt1
        first = nxt1
        second = nxt2
```

---

### 146. LRU缓存机制

**思路：** 哈希表 + 双向链表（Python 用 `OrderedDict` 替代）。get/put 时移到头部，容量满时删尾部。

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
```

---

### 160. 相交链表

**思路：** 双指针 a、b 分别从两个头出发，走完自己的链表后跳到对方头部。若有交点一定相遇，否则同时到 None。

```python
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```

---

### 19. 删除链表的倒数第N个节点

**思路：** 快指针先走 n+1 步，然后快慢一起走，快到末尾时慢刚好在目标前一个，直接删除。

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
```

---

## 三、套路总结

### 链表题的三大法宝

| 手法 | 用途 | 代表题 |
|------|------|--------|
| **dummy 头节点** | 统一处理头节点被删/被改的情况 | 19, 21, 25, 82, 92 |
| **快慢指针** | 找中点、找环、找倒数第 k 个 | 19, 141, 142, 143 |
| **反转链表** | 区间反转、整体反转 | 206, 92, 25, 143 |

### 反转链表变形题统一模板

所有反转题都基于同一个核心操作——把 `cur.next` 指向 `pre`：

```python
# 核心反转三行
nxt = cur.next
cur.next = pre
pre = cur
cur = nxt
```

- **206 整体反转：** 直接用这三行走一遍
- **92 区间反转：** 走到 m 位置，用头插法重复这三行 (n-m) 次
- **25 分组反转：** 每 k 个一组做一次整体反转，再重新连接

### 快慢指针变形题统一模板

```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next          # 慢走 1 步
    fast = fast.next.next     # 快走 2 步
    # 在这里判断是否需要 break
```

- **找中点（143）：** `while fast.next and fast.next.next`，循环结束 slow 就是中点
- **判环（141）：** 每步检查 `if slow == fast`，有环必相遇
- **找环入口（142）：** 相遇后把 slow 放回头部，各走一步再相遇就是入口

### 双指针找交点模板（160）

```python
a, b = headA, headB
while a != b:
    a = a.next if a else headB
    b = b.next if b else headA
return a
```

### 常见组合技（143 重排链表）

链表题经常需要**组合多个基础操作**：找中点 + 反转 + 合并，每一步都是独立的模板。
