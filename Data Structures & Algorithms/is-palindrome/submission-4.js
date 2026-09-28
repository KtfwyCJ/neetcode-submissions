class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const arr = s.toLowerCase().split('');
        let newArr = []
        let reverseStr = ''
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] !== ' ' && /[a-z0-9]/.test(arr[i])) {
                reverseStr += arr[i]
                newArr.push(arr[i])
            }
        }
        return newArr.reverse().join('') === reverseStr;
    }
}
