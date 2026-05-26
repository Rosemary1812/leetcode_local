# ===== 143. 重排链表 =====
# 难度: 中等
# 英文名: Reorder List
# 来源: https://leetcode.cn/problems/reorder-list/description/
# 标签: codetop
#
# 给定链表 1 -> 2 -> 3 -> 4，重排为 1 -> 4 -> 2 -> 3。
#
# ---------------------------------------------------------

# 思路：三步走：1) 找中点（快慢指针）2) 反转后半段 3) 前后两段交替合并。
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


def reorder(head):
    if not head or not head.next:
        return

    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    pre = None
    cur = slow.next
    slow.next = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    first, second = head, pre
    while second:
        nxt1, nxt2 = first.next, second.next
        first.next = second
        second.next = nxt1
        first = nxt1
        second = nxt2


head1 = build_list([1, 2, 3, 4])
reorder(head1)
print_list(head1)  # [1, 4, 2, 3]

head = build_list([1, 2, 3, 4, 5])
reorder(head)
print_list(head)  # [1, 5, 2, 4, 3]
