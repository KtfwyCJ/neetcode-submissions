# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 题目灵魂：max(左子树深度, 右子树深度) + 1
        # 时间复杂度O(n)
        # 空间复杂度，像链表：O(n), 平衡树O(logn)

        # 终止条件
        if not root:
            return 0

        # 2. 求左子树深度
        leftDepth = self.maxDepth(root.left)

        # 3. 求右子树深度
        rightDepth = self.maxDepth(root.right)

        # 4. 返回较大值 + 1
        return max(leftDepth, rightDepth) + 1
        