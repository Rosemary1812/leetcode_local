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
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverseKGroup(head,k):
    n=0
    cur=head
    while cur:
        n+=1
        cur=cur.next
    
    dummy=ListNode(0,head)
    p0=dummy
    pre=None
    cur=head
    
    while n>=k:
        for _ in range(k):
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        p0.next.next=cur
        nxt=p0.next
        p0.next=pre
        p0=nxt
    return dummy.next

def arrayToList(arr):
    dummy=ListNode()
    cur=dummy
    for var in arr:
        cur.next=ListNode(var)
        cur=cur.next
    return dummy.next

def listToArray(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


print(listToArray(reverseKGroup(arrayToList([1,2,3,4,5]),2)))