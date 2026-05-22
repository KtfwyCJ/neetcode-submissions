class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # # 只拿数字，不要次数
        # return [num for num, freq in counter.most_common(k)]

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        res = []

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                     return res