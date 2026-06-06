# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # bst的中序遍历结果一定是从小到大排序的，中序遍历：左 -> 根 -> 右
        # 因此BST 的第 k 小元素 = 中序遍历的第 k 个元素
        # 把中序遍历结果存进数组，最终的结果就是arr[k-1]

        nums = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            nums.append(node.val)

            inorder(node.right)

        # 启动程序
        inorder(root)

        return nums[k-1]

