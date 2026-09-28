class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let min = prices[0];
        let max = 0;

        for (let i = 0; i < prices.length; i++) {
            if (prices[i] < min) {
                min = prices[i]
            }
            if (prices[i] > max && min != prices[i]) {
                max= prices[i]
            }
        
        }
        if(max <= min) return 0;
        return max - min
    }
}
