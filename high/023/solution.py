# ===== 23. 合并K个排序链表 =====
# 难度: 困难
# 英文名: Merge k Sorted Lists
# 来源: https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# 合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
# ---------------------------------------------------------
from typing import List, Optional

class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next
  
def merge_two_list(l1,l2):
  dummy=ListNode(0)
  cur=dummy
  while l1 and l2:
    if(l1.val<l2.val):
      cur.next=l1
      l1=l1.next
    else:
      cur.next=l2
      l2=l2.next
    cur=cur.next
  cur.next=l1 if l1 else l2
  return dummy.next


def merge_k_lists(lists):
  if not lists:
    return None
  if len(lists)==1:
    return lists[0]
  
  def merge(l,r):
    if l==r:
      return lists[l]
    mid=(l+r)//2
    left=merge(l,mid)
    right=merge(mid+1,r)
    return merge_two_list(left,right)
  return merge(0,len(lists)-1)
# 递归处理

def build_list(arr):
  if not arr:
    return None
  dummy=ListNode(0)
  cur=dummy
  for val in arr:
    cur.next=ListNode(val)
    cur=cur.next
  return dummy.next

def list_to_array(head):
  arr=[]
  while head:
    arr.append(head.val)
    head=head.next
  return arr


lists1=[build_list([1,4,5]), build_list([1,3,4]), build_list([2,6])]
print(list_to_array(merge_k_lists(lists1)))  # [1,1,2,3,4,4,5,6]

