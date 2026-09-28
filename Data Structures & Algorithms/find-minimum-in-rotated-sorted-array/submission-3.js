class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {

        let minVal = 0;

        let left = 0;
        let right = nums.length - 1;

        while (left <= right) {
            const mid = Math.floor((right + left) / 2);

            if (nums[mid] < nums[mid - 1] && nums[mid] < nums[mid+1]) {
                return nums[mid]
            }

            if (nums[right] < nums[left]) {
                left = mid + 1
            }

            if (nums[right] > nums[left]) {
                right = mid - 1
            }

        }
    }
}
