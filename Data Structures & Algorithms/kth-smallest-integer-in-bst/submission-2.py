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

        # 优化解法，因为只需要第k小，所以并不需要遍历整个树，所以可以做一个计数器

        # 用栈

        stack = []
        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right
