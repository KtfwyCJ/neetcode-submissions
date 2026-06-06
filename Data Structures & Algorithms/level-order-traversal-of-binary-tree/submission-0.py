# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS（广度优先搜索）+ 队列
        # FIFO(先进先出)：先处理上一层再处理下一层
        # queue 里永远保存“当前层 + 下一层的边界”
        
        if not root:
            return []

        # 结果数组
        result = []

        # 使用队列，初始化放入根节点
        queue = deque([root])

        # 当队列不为空时
        while queue:
            # 1. 当前这一层的节点数量
            level_size = len(queue)

            # 存储当前这一层的值
            level =[]

            # 2. 遍历当前层的所有节点
            for _ in range(level_size):

                # 弹出队首节点（当前层节点）
                node = queue.popleft()

                # 把值加入当前层结果
                level.append(node.val)

                # 3. 把下一层节点加入队列

                if node.left:
                    queue.append(node.left)
                # 如果右孩子还在
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result



        