class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map()
        let arr = []
        
        for (let e = 0; e < nums.length; e++) {
            const complement = target - nums[e]
            if (map.has(complement)) {
                return [e, map.get(complement)]
            }
                
            map.set(nums[e], e)
        } 
    }
}
