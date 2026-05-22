class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # 只拿数字，不要次数
        return [num for num, freq in counter.most_common(k)]