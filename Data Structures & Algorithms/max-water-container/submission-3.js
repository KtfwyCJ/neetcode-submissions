class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        // result = (height2-height1) * (index2 - index1)

        let maxVolume = 0;
        let left = 0;
        let right = heights.length - 1;

        while (left < right) {
            const width = right - left;
            const height = Math.min(heights[left], heights[right])
            const volume = height * width

            maxVolume = Math.max(volume, maxVolume)

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }


        return maxVolume;
    }
}
