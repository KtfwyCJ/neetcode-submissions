class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        let stack = []
        for (const char of s) {
            if (char === '(' ||
                char === '{' ||
                char === '[') {
                stack.push(char)
            } else {
                if (
                    stack.length === 0 ||
                    stack.pop() !== map[char]
                ) {
                    return false;
                }
                
            }

        }

        return stack.length === 0;
    }
}
