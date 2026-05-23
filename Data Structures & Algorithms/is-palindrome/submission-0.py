class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        # isalnum：判断字符是否是字母还是数字，忽略特殊字符
        for c in s:
            if c.isalnum():
                # 忽略大小写
                newStr += c.lower()
        
        # 字符串反转：newStr[::-1] 
        return newStr == newStr[::-1]
        