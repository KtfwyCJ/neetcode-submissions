class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 题目含义：给你一些数字，让你“无限次使用它们”，拼出所有“刚好加起来等于 target 的方式
        res = []
        nums.sort()

        def dfs(start, remain, path):
            # 成功：刚好凑够
            if remain == 0:
                # path[:]  把当前这个 path 复制一份新的出来
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                #超过了，后面更大不用试了
                if nums[i] > remain:
                    break
                # 选择这个数
                path.append(nums[i])
                # 继续往下选（可以重复用i）
                dfs(i, remain - nums[i], path)
                # 撤销选择
                path.pop()

        dfs(0, target, [])
        return res