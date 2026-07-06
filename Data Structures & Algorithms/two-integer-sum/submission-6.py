class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, e in enumerate(nums):
            complement = target - e

            if complement in map:
                return [map.get(complement), i]
            map[e] = i