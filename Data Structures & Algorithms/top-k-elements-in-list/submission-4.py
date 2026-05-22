class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # bucket[i] = 出现 i 次的所有数字
        bucket = [[] for _ in range(len(nums) + 1)]
        # 填充桶的值
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        res = []
        # 从右到左，因为桶是从小到大排序
        for i in range(len(bucket)-1, -1, -1):
            # 塞数值
            for num in bucket[i]:
                res.append(num)
                # 返回top k
                if len(res) == k:
                     return res