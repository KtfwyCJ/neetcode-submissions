# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # binary search tree: 左侧所有节点都比右侧小
        # 每个节点都必须落在某个范围内，每个节点都有一个合法区间
        def dfs(node, low, high):
                if not node:
                    return True

                if node.val <= low or node.val >= high:
                    return False

                return (
                    dfs(node.left, low, node.val)
                    and
                    dfs(node.right, node.val, high)
                    )
        # float('-inf')：负无穷大， float('inf')：正无穷大
        return dfs(root, float('-inf'), float('inf'))
        