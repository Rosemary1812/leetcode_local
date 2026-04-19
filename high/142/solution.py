# ===== 142. 环形链表 II =====
# 难度: 中等
# 英文名: Linked List Cycle II
# 来源: https://leetcode.cn/problems/linked-list-cycle-ii/description/
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
#
# 你是否可以使用 O(1) 空间解决此题？
# 示例 1：

# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：

# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：

# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。

# 提示：
# 链表中节点的数目范围在范围 [0, 104] 内
# -105 <= Node.val <= 105
# pos 的值为 -1 或者链表中的一个有效索引
# ---------------------------------------------------------

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if fast is slow:  # 相遇
#                 while slow is not head:  # 再走 a 步
#                     slow = slow.next
#                     head = head.next
#                 return slow
#         return None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals, pos):
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def detectCycle(head):
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


print(detectCycle(build_list([1, 2], 0)))
print(detectCycle(build_list([1], -1)))
print(detectCycle(build_list([3, 2, 0, -4], 1)))
