from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            countS[char] = counter(char)
        for char in t:
            countT[char] = counter(char)

        return countS == countT
        
        