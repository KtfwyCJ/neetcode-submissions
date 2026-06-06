class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {
        // direction: left (num[i-1]), right(num[i+1]), up, down

        // 二维矩阵
        // 从一个点出发
        // 上下左右移动
        // 不能重复访问
        // 找路径
        // 根据以上直接想到dfs+backtrack
        // dfs: 深度优先检索


        const rows = board.length;
        const cols = board[0].length;

        function dfs(r, c, index) {

            // 整个单词匹配完成
            if (index === word.length) {
                return true;
            }

            // 越界
            if (
                r < 0 ||
                r >= rows ||
                c < 0 ||
                c >= cols
            ) {
                return false;
            }

            // 字符不匹配
            if (board[r][c] !== word[index]) {
                return false;
            }

            // 保存原字符
            const temp = board[r][c];

            // 标记访问
            board[r][c] = '#';

            const found =
                dfs(r + 1, c, index + 1) ||
                dfs(r - 1, c, index + 1) ||
                dfs(r, c + 1, index + 1) ||
                dfs(r, c - 1, index + 1);

            // 回溯恢复
            board[r][c] = temp;

            return found;
        }

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {

                if (dfs(r, c, 0)) {
                    return true;
                }
            }
        }

        return false;
    }
}
