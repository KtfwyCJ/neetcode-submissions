class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let elems = new Map();

        if (s.length !== t.length) return false;
        
        for (const e of s) {
            elems.set(e, (elems.get(e) || 0) + 1)
        }

        for (const e of t) {
            const nums = elems.get(e) || 0
            if (nums === 0) {
                return false
            }
            elems.set(e, nums - 1)
        }

        return true
    }
}
