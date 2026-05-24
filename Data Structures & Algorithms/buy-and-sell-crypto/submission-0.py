class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        # 一边遍历，一边维护历史最小值
        # “如果我今天卖掉，那我以前最低多少钱买入最划算？””
        for price in prices:
            min_price = min(min_price, price)

            max_profit = max(max_profit, price - min_price)

        return max_profit
            