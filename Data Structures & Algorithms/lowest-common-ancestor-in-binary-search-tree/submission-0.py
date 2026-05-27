# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 核心逻辑: 看 p 和 q 是否在 root 的同一侧
        # BTS保证所有左子树 < root < 所有右子树
        # 如果 p 和 q 都小 → 只能在左边
        # 如果都大 → 只能在右边
        # 否则 → 当前节点就是第一次“分裂点”
        
        # 如果都在左边
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # 如果都在右边
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # 交叉
        return root