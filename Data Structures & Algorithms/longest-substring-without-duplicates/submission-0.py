class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # 维护一个永远不重复的窗口, right扩张窗口, left缩小窗口
         charSet = set()
         left = 0
         maxlength = 0

         for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxlength = max(maxlength, right - left + 1)
         return maxlength


            
        
            
        