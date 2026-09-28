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

        const heap = []
        for (const [num, count] of map) {
            heap.push([count, num]);

            heap.sort((a, b) => a[0] - b[0]);

            if (heap.length > k) {
                heap.shift();
            }

        }

        return heap.map(([count, num]) => num)
    }
}
