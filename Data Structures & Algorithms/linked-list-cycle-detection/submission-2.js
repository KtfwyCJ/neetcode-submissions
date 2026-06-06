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
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        // 使用HashSet记录重复元素
        const visited = new Set();

        let curr = head;

        while(curr) {
            if (visited.has(curr)) {
                return true;
            }
            visited.add(curr)
            curr = curr.next
        }

        return false
    }
}
