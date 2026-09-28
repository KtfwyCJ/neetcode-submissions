class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buyPrice = prices[0];

        let maxValue = 0;

        for (let i = 1; i < prices.length; i++) {
            if (prices[i] < buyPrice) {
                buyPrice = prices[i]
            }
            if (prices[i] - buyPrice > maxValue) {
                maxValue = prices[i] - buyPrice;
            }
            
        }

        return maxValue
       
    }
}
