from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            countS[char] = Counter(char)
        for char in t:
            countT[char] = Counter(char)

        return countS == countT
        
        