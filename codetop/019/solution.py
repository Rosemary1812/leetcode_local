# ===== 19. 删除链表的倒数第N个节点 =====
# 难度: 中等
# 英文名: Remove Nth Node From End of List
# 来源: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
# 标签: codetop
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]
#
# ---------------------------------------------------------

# 思路：快慢指针。快指针先走 n 步，然后快慢一起走，快指针到末尾时慢指针正好在倒数第 n 个的前一个。
#   用 dummy 节点处理删除头节点的情况。
# 时间复杂度：O(L)，L 为链表长度。
# 空间复杂度：O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for i in arr:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next


def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


def removeNthFromEnd(head, n):
    left = right = dummy = ListNode(next=head)
    for _ in range(n):
        right = right.next
    while right.next:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next


head1 = build_list([1, 2, 3, 4, 5])
print_list(removeNthFromEnd(head1, 2))

head = build_list([1])
print_list(removeNthFromEnd(head, 1))
