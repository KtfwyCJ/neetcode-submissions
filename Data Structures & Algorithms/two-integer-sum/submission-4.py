class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {3:0, 4: 1, 5: 2, 6: 3}

        numbers = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numbers:
                return [numbers.get(complement), i]
            else:
                numbers[num] = i
            


        