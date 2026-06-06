class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        // Backtracking
        // 找所有可能
        // 所有组合
        // 所有排列
        // 返回所有结果
        // Combination
        // Permutation
        // Subset

        // []
        // ├── 2
        // │   ├── 2
        // │   │   ├── 2
        // │   │   ├── 5 ✅
        // │   │   ├── 6
        // │   │   └── 9
        // │
        // ├── 5
        // ├── 6
        // └── 9 ✅
        const result = []

        function dfs(index, path, total) {
            if (total === target) {
                result.push([...path])
                return
            }

            if (total > target) {
                return
            }

            for (let i = index; i < nums.length; i++) {
                path.push(nums[i])

                dfs(i, path, total + nums[i])

                path.pop()
            }
        }

        dfs(0, [], 0)

        return result
    }
}
