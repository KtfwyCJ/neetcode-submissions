class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxValue = 1;
        const newArr = s.split('');

        if (s.length === 1) return 1;

        let left = 0;
        let right = left + 1;

        let arr = [];

        while(left < right && right < s.length - 1) {
            console.log(arr)
            if (arr.includes(newArr[right])) {
                let index = arr.indexOf(newArr[right]);
                left = index + 1;
            } else {
                arr.push(newArr[right])
            }
            right++
        }

        return arr.length
    }
}
