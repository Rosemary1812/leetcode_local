# ===== 141. 环形链表 =====
# 难度: 简单
# 英文名: Linked List Cycle
# 来源: https://leetcode.cn/problems/linked-list-cycle/description/
#
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了确定给定链表中没有环，我们使用 pos 表示链表中尾节点的 next 指针指向的索引。如果 pos 是 -1，则链表中没有环。
#
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
# 示例 3：
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
# ---------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_cy_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


print(has_cycle(build_cy_list([3, 2, 0, -4], 1)))
