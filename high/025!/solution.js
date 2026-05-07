// ===== 25. K 个一组翻转链表 =====
// 难度: 困难
// 英文名: Reverse Nodes in k-Group
// 来源: https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
//
// 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

// k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

// 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

// 示例 1：

// 输入：head = [1,2,3,4,5], k = 2
// 输出：[2,1,4,3,5]
// 示例 2：

// 输入：head = [1,2,3,4,5], k = 3
// 输出：[3,2,1,4,5]

// 提示：
// 链表中的节点数目为 n
// 1 <= k <= n <= 5000
// 0 <= Node.val <= 1000

// 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
// ---------------------------------------------------------

function ListNode(val, next) {
  this.val = val;
  this.next = next ?? null;
}

function reverseKGroup(head, k) {
  let n = 0;
  for (let cur = head; cur; cur = cur.next) n++;

  const dummy = new ListNode(0, head);

  let p0 = dummy;
  let pre = null;
  let cur = head;

  for (; n >= k; n -= k) {
    for (let i = 0; i < k; i++) {
      const next = cur.next;
      cur.next = pre;
      pre = cur;
      cur = next;
    }

    const next = p0.next;
    p0.next.next = cur;
    p0.next = pre;
    p0 = next;
  }
  return dummy.next;
}

function arrayToList(arr) {
  const dummy = new ListNode(0);
  let cur = dummy;
  for (const val of arr) {
    cur.next = new ListNode(val);
    cur = cur.next;
  }
  return dummy.next;
}

function listToArray(head) {
  const result = [];
  while (head) {
    result.push(head.val);
    head = head.next;
  }
  return result;
}

console.log(listToArray(reverseKGroup(arrayToList([1, 2, 3, 4, 5]), 2))); // [2,1,4,3,5]
console.log(listToArray(reverseKGroup(arrayToList([1, 2, 3, 4, 5]), 3))); // [3,2,1,4,5]
