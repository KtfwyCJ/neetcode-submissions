class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let map = new Map();

        for (let i = 0; i < nums.length; i++) {
            const count = map.get(nums[i]) || 0;
            map.set(nums[i], count + 1);
        }
        
        return [...map.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .map(([m]) => m)
        
    }
}
