# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 情况1：两个都为空
        if p == None and q == None:
            return True

        # 情况2：有一个为空
        if p == None or q == None:
            return False

        # 情况3：值不相等
        if p.val != q.val:
            return False

        # 情况4：值相等则继续往下对比
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)