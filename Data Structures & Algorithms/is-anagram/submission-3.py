from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            countS[char] = count(char)
        for char in t:
            countT[char] = count(char)

        return countS == countT
        
        