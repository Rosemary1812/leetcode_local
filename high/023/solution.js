// ===== 23. 合并K个排序链表 =====
// 难度: 困难
// 英文名: Merge k Sorted Lists
// 来源: https://leetcode.cn/problems/merge-k-sorted-lists/description/
//
// 合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
//
// 示例:
//
// 输入:
// [
// 1->4->5,
// 1->3->4,
// 2->6
// ]
// 输出: 1->1->2->3->4->4->5->6
//
// ---------------------------------------------------------

function ListNode(val, next) {
  this.vbal = val;
  this.next = next ?? null;
}

function mergeTwoLists(l1, l2) {
  const dummy = new ListNode(0);
  let cur = dummy;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      cur.next = l1;
      l1 = l1.next;
    } else {
      cur.next = l2;
      l2 = l2.next;
    }
    cur = cur.next;
  }
  cur.next = l1 || l2;
  return dummy.next;
}

function mergeK(lists) {
  if (!lists || lists.length === 0) return null;
  if (lists.length === 1) return lists[0];

  const merge = (l, r) => {
    if (l === r) return lists[l];
    const mid = Math.floor((l + r) / 2);
    const l1 = merge(l, mid);
    const l2 = merge(mid + 1, r);
    return mergeTwoLists(l1, l2);
  };
  return merge(0, lists.length - 1);
}

function listToArray(head) {
  const result = [];
  while (head) {
    result.push(head.val);
    head = head.next;
  }
  return result;
}

function buildList(arr) {
  if (!arr || arr.length === 0) return null;
  const dummy = new ListNode(0);
  let cur = dummy;
  for (const val of arr) {
    cur.next = new ListNode(val);
    cur = cur.next;
  }
  return dummy.next;
}

const lists1 = [buildList([1, 4, 5]), buildList([1, 3, 4]), buildList([2, 6])];
console.log(listToArray(mergeKLists(lists1))); // [1,1,2,3,4,4,5,6]
