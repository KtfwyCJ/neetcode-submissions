class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        const elems = new Map();

        for (const  e of s)  {
            elems.set(e, (elems.get(e) || 0) + 1)
        }

        for (const e of t) {
            const counts: number = elems.get(e) || 0;

            if (counts === 0) return false;

            elems.set(e, counts - 1);
        }

        return true;


    }
}
