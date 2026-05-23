class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 固定一个数，剩下变成 Two Sum
        # 排序：双指针必须依赖“有序”

        nums.sort()

        res = []

        for i in range(len(nums)):
            # 相同数字跳过
            if i > 0 and nums[i] == nums[i -1]:
                continue
            # 左右指针  
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else :
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1


                    # 去重: [-2,0,0,0,2,2]，如果不去重会出现多个[-2,0,2]的结果
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
            



