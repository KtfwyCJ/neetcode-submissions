class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // edge case
        if (strs.length === 1) return [strs]

        let map = new Map();

        for (let i = 0; i < strs.length; i++) {
            // sort element
            let sortedEle = strs[i].split("").sort().join('');
            let arr = map.get(sortedEle) || [];
            map.set(sortedEle, [...arr, strs[i]]);
        }

        return Array.from(map.values())

    }
}
