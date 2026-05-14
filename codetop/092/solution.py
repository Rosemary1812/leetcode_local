# ===== 92. 反转链表 II =====
# 难度: 中等
# 英文名: Reverse Linked List II
# 来源: https://leetcode.cn/problems/reverse-linked-list-ii/description/
# 标签: codetop
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
# ---------------------------------------------------------

# 思路：头插法一趟扫描。先走到第 m-1 个节点（pre），然后将后续 n-m 个节点依次头插到 pre 之后。
#   即 cur.next = pre.next; pre.next = cur.next（经典的区间反转头插法）。
# 时间复杂度：O(n)
# 空间复杂度：O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


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


print_list(reverse_between(build_list([1, 2, 3, 4, 5]), 2, 4))
