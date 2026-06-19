class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        for i in nums:
            if nums[i] in seen:
                return true

            seen.set(nums[i])
        return false