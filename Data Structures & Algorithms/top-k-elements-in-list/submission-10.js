class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let map = new Map();

        const buckets = Array.from({length: nums.length + 1}, () => [])

        for (let i = 0; i < nums.length; i++) {
            const count = map.get(nums[i]) || 0;

            map.set(nums[i], count + 1)
        }

        for (const [num, count] of map) {
            buckets[count].push(num)
        }

        const results = []
        for (let i = buckets.length - 1; i >=0; i--) {
            for (const num of buckets[i]) {
                results.push(num)

                if (results.length === k) {
                    return results
                }
            }
        }

        
        
    }
}
