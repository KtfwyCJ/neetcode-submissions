class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            # k: 匹配到word的第k个字符

            # 1. 成功，全部匹配完
            if k == len(word):
                return True

            # 2. 越界 or 不匹配
            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != word[k]):
                return False

            # 3. 标记已访问
            temp = board[i][j]
            board[i][j] = "#"

            # 4. 朝4个方向搜索
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1) 
            )

            # 5. 回溯修复
            board[i][j] = temp
            return found

        # 从每个点作为起点尝试
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False