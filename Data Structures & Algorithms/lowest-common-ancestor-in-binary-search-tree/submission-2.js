/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        // BST: 左 < 根 < 右
        // p,q都小于root
        //     ↓
        // 往左

        // p,q都大于root
        //     ↓
        // 往右

        // 一左一右
        //     ↓
        // 当前root就是LCA

        while (root) {
            if (p.val < root.val && q.val < root.val) {
                root = root.left
            } else if (
                p.val > root.val && q.val > root.val
            ) {
                root = root.right
            } else {
                return root
            }
        }
    }
}
