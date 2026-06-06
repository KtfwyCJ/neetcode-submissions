/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    mergeTwoLists(list1, list2) {

        // 创建虚拟头节点(dummy)
        // 这样就不用单独处理第一个节点
        const dummy = new ListNode(0);

        // tail始终指向当前合并链表的最后一个节点
        let tail = dummy;

        // 当两个链表都还有节点时
        while (list1 && list2) {

            // 谁小就接谁
            if (list1.val <= list2.val) {

                // 把list1当前节点接到结果链表后面
                tail.next = list1;

                // list1向后移动
                list1 = list1.next;

            } else {

                // 把list2当前节点接到结果链表后面
                tail.next = list2;

                // list2向后移动
                list2 = list2.next;
            }

            // tail永远跟到新链表的最后面
            tail = tail.next;
        }

        // 循环结束后
        // 一定有一个链表已经为空

        // 直接把剩余部分接上即可
        tail.next = list1 || list2;

        // dummy指向虚拟头
        // 真正头节点是dummy.next
        return dummy.next;
    }
}