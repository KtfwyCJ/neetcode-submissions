# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 思路：1. 如何判断子树相同？sameTree 2.如何遍历树？dfs

        # 大树为空
        if not root:
            return False
        
        # 当前节点开始匹配
        if self.isSameTree(root, subRoot):
            return True

        # 去左边找，去右边找
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode] ) -> bool:

        if p == None and q == None:
            return True

        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)