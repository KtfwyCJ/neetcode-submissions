class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let map = {
            ')' : '(',
            '}' : '{',
            ']' : '[]'
        }

        let arr = [];
        for (let i = 0; i < s.length; i++) {
            if (!map[s[i]]) {
                arr.push(s[i]);
            } else {
                arr.pop();
            }
        }

        return arr.length === 0;
    }
}
