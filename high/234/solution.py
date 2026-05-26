# ===== 234. 回文链表 =====
# 难度: 简单
# 英文名: Palindrome Linked List
# 来源: https://leetcode.cn/problems/palindrome-linked-list/description/
#
# 给你一个单链表 L，判断它是不是回文的。
#
# 示例 1：
# 输入：head = [1,2,2,1]
# 输出：true
#
# 示例 2：
# 输入：head = [1,2]
# 输出：false
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
# ---------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_list(head):
    cur = head
    pre = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


def is_pali(head):
    mid = middle(head)
    head2 = reverse_list(mid)
    while head2:
        if head.val != head2.val:
            return False
        head = head.next
        head2 = head2.next
    return True


def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


print(is_pali(build_list([1, 2, 2, 1])))
print(is_pali(build_list([1, 2])))
print(is_pali(build_list([1, 2, 3, 2, 1])))
