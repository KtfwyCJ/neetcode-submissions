class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        for i in nums:
            if i in seen:
                return True
            seen.set(i)
            
        return False