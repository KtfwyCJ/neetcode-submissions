# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 时间复杂度,如果有n个节点：O(n)
        # 空间复杂度，递归会占用函数栈，最坏情况：1->2->3，像链表一样递归深度 O(n)

        # 1. 终止条件
        if not root:
            return None
        
        # 2. 交换左右孩子
        root.left, root.right = root.right, root.left

        # 3. 递归处理左子树
        self.invertTree(root.left)

        # 4. 递归处理右子树
        self.invertTree(root.right)

        # 5. 返回根节点
        return root

        