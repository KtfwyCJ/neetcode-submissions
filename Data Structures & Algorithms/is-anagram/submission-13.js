class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // edge case
        if (s.length !== t.length) return false;

        let sMap = new Map();

        for (const val of s) {
            const num = (sMap.get(val) || 0) + 1;
            sMap.set(val, num)
        }

        for (const val of t) {
            const num = sMap.get(val) || 0;
            if (num === 0) return false;
            sMap.set(val, num - 1)
        }

        return true;
        
    }
}
