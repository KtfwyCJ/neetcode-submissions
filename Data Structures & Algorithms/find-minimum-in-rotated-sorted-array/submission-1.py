class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid > right：说明 mid 在“大区间”，断点在右边 → 去右边找：left = mid + 1
        # mid <= right： 说明右边是有序小区间，断点在左边（包括 mid）：right = mid
        
        left = 0

        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if (nums[mid] > nums[right]):
                left = mid + 1
            else: 
                right = mid
        return nums[left]