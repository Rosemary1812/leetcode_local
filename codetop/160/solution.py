# ===== 160. 相交链表 =====
# 难度: 简单
# 英文名: Intersection of Two Linked Lists
# 来源: https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
# 标签: codetop
#
# 找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null。
#
# ---------------------------------------------------------

# 思路：双指针。a 走完 A 链表后转到 B 头部，b 走完 B 链表后转到 A 头部。
#   两人走的总路程相同，若有交点则一定在交点相遇，否则同时到达 None。
# 时间复杂度：O(m+n)
# 空间复杂度：O(1)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def get_intersection_node(headA, headB):
#     a, b = headA, headB
#     while a != b:
#         a = a.next if a else headB
#         b = b.next if b else headA
#     return a
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(haedA, headB):
    a = headA
    b = headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


# 构造相交链表测试
# A: 4 -> 1 -> 8 -> 4 -> 5
# B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
# 交点为节点 8
common = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, common))
headB = ListNode(5, ListNode(6, ListNode(1, common)))
result = get_intersection_node(headA, headB)
print(result.val if result else None)
