# ===== 21. 合并两个有序链表 =====
# 难度: 简单
# 英文名: Merge Two Sorted Lists
# 来源: https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# ---------------------------------------------------------


class ListNode:
    def __init__(self,val=0,next=None) :
        self.val=val
        self.next=next


def merge(l1,l2):
    dummy=ListNode(0)
    cur=dummy

    while l1 and l2:
        if l1.val<=l2.val:
            cur.next=l1
            l1=l1.next
        else:
            cur.next=l2
            l2=l2.next
        cur=cur.next
    cur.next=l1 if l1 else l2
    return dummy.next

def buildList(arr):
    dummy=ListNode(0)
    cur=dummy
    for val in arr:
        cur.next=ListNode(val)
        cur=cur.next
    return dummy.next

def ListToArray(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


print(ListToArray(merge(buildList([1,2,4]),buildList([1,3,4]))))
print(ListToArray(merge(buildList([]),buildList([]))))
print(ListToArray(merge(buildList([]),buildList([0]))))
print(ListToArray(merge(buildList([1]),buildList([2]))))
print(ListToArray(merge(buildList([1,1,1]),buildList([1,1,1]))))

