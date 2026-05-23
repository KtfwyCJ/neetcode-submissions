class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 双指针从两端开始，
        # 每次丢掉较短的那一边，
        # 因为短板决定最大可能性

        left = 0
        right = len(heights) - 1

        res = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res