# ===== 25. K 个一组翻转链表 =====
# 难度: 困难
# 英文名: Reverse Nodes in k-Group
# 来源: https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# ---------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def reverseKGroup(head, k):
#     """反转链表每 k 个节点一组"""
#     # 统计链表长度
#     n = 0
#     cur = head
#     while cur:
#         n += 1
#         cur = cur.next

#     dummy = ListNode(0, head)
#     p0 = dummy
#     cur = head

#     while n >= k:
#         pre = None

#         # 反转 k 个节点
#         for _ in range(k):
#             nxt = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nxt

#         # 连接反转后的链表
#         tail = p0.next
#         tail.next = cur
#         p0.next = pre
#         p0 = tail

#         n -= k

#     return dummy.next


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


def arrayToList(arr):
    dummy = ListNode()
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def listToArray(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# 测试
print(listToArray(reverseKGroup(arrayToList([1, 2, 3, 4, 5]), 2)))  # [2, 1, 4, 3, 5]
print(listToArray(reverseKGroup(arrayToList([1, 2, 3, 4, 5]), 3)))  # [3, 2, 1, 4, 5]
print(listToArray(reverseKGroup(arrayToList([1, 2]), 3)))  # [1, 2]
