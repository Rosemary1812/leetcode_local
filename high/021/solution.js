// ===== 21. 合并两个有序链表 =====
// 难度: 简单
// 英文名: Merge Two Sorted Lists
// 来源: https://leetcode.cn/problems/merge-two-sorted-lists/description/
//
// 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
// 
// 示例：
// 
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4
//
// ---------------------------------------------------------

function mergeTwoLists(l1, l2) {
    const dummy = { val: 0, next: null };
    let cur = dummy;

    while (l1 && l2) {
        if (l1.val <= l2.val) {
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

function buildList(arr) {
    const dummy = { val: 0, next: null };
    let cur = dummy;
    for (const val of arr) {
        cur.next = { val, next: null };
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

console.log(listToArray(mergeTwoLists(buildList([1, 2, 4]), buildList([1, 3, 4]))));
console.log(listToArray(mergeTwoLists(buildList([]), buildList([]))));
console.log(listToArray(mergeTwoLists(buildList([]), buildList([0]))));
console.log(listToArray(mergeTwoLists(buildList([1]), buildList([2]))));
console.log(listToArray(mergeTwoLists(buildList([1, 1, 1]), buildList([1, 1, 1]))));