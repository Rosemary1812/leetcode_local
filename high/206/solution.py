# ===== 206. 反转链表 =====
# 难度: 简单
# 英文名: Reverse Linked List
# 来源: https://leetcode.cn/problems/reverse-linked-list/description/
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def list_to_arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr


def reverse(head):
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


print(list_to_arr(reverse(build_list([1, 2, 3, 4, 5]))))
