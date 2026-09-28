class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        // result = (height2-height1) * (index2 - index1)

        let maxVolume = 0;

        for(let i = 0; i < heights.length; i++) {
            let left = i;
            let right = heights.length - 1;

            while (left < right) {
                const width = right - left;
                const volume = heights[left] < heights[right] ? heights[left] * width : heights[right] * width 
                console.log(left, right)
                console.log(2222, heights[right] - heights[left], heights[left] - heights[right], volume)
                if (volume > maxVolume) {
                    
                    console.log(heights[left], heights[right])
                    maxVolume = volume;
                }
                if (heights[right] > heights[left]) {
                    right--
                } else {
                    left++
                }
            }
        }

        return maxVolume;
    }
}
