class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxValue = 1;

        let set = new Set();

        let left = 0;

        for (let right = 0 ; right < s.length; right++) {
            while (set.has(s[right])) {
                set.delete(s[right])
                left++;
            }

            set.add(right);

            maxLength = Math.max(maxLength, right-left+1)

        }

        return maxLength
    }
}
