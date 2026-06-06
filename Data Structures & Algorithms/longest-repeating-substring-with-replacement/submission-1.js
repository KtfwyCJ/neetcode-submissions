class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const count = {};

        // 窗口问题， 需要修改次数 =windowSize - maxFreq
        let left = 0
        let maxFreq = 0;
        let maxLength = 0;

        for (let right = 0; right < s.length; right++) {
            const char = s[right];
            // 字符计数
            count[char] = (count[char] || 0) + 1;
            // 最大相同字符数
            maxFreq = Math.max(maxFreq, count[char])

            // 如果窗口大小 - maxFreq > k，说明k不能覆盖，则left指针右移
            while (
                (right - left + 1) - maxFreq > k
            ) {
                count[s[left]]--;
                left++;
            }

            maxLength = Math.max(
                maxLength,
                right - left + 1
            );
        }

        return maxLength

    }
}
