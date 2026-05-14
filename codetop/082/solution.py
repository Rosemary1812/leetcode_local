# ===== 82. 删除排序链表中的重复元素 II =====
# 难度: 中等
# 英文名: Remove Duplicates from Sorted List II
# 来源: https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
# 标签: codetop
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复的数字。
#
# ---------------------------------------------------------

# 思路：dummy + 指针扫描。用 dummy 指向 head，pre 指向最后一个确定保留的节点。
#   当 cur.val == cur.next.val 时，跳过所有重复节点。
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


def deleteDuplicate(head):
    cur = dummy = ListNode(next=head)
    while cur.next and cur.next.next:
        val = cur.next.val
        if cur.next.next.val == val:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
        else:
            cur = cur.next
        return dummy.next


# print(deleteDuplicate(build_list([1, 2, 3, 3, 4, 4, 5])))
print_list(deleteDuplicate(build_list([1, 1, 1, 2, 3])))
