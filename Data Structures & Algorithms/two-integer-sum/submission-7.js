class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let value = null; // 7-3 = 4
        let map = new Map();
        // <3, index>

        for (let i = 0; i < nums.length; i++) {
            value = target - nums[i];
            if (map.has(value)) {
                return [i, map.get(value)]
            } else {
                map.set(nums[i], i);
            }
        }
    }
}
