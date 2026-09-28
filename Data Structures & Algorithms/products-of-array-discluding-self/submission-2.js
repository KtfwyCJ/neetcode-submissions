class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        const output = new Array(nums.length).fill(1);

        let prefix = 1;

        // Left products
        for (let i = 0; i < nums.length; i++) {
            output[i] = prefix;
            prefix *= nums[i];
        }

        let suffix = 1;

        // Right products
        for (let i = nums.length - 1; i >= 0; i--) {
            output[i] *= suffix;
            suffix *= nums[i];
        }

        return output;

    }
}
