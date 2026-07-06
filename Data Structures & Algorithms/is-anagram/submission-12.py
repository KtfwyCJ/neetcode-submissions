class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        elems = {}

        for e in s:
            count = elems.get(e, 0)
            elems[e] = count + 1
        
        for e in t:
            count = elems.get(e, 0)

            if count == 0:
                return False
            elems[e] = count - 1
        
        return True
        