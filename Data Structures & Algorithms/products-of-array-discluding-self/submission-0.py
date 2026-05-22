class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         
         # 左乘积、右乘积的方法
         # 求除了自己以外所有数的乘积，那就是左边乘积 * 右边乘积

         # 语法糖"重复生成元素"：prefix = [1] * 5 -> [1,1,1,1,1]
         prefix = [1] * n
         postfix = [1] * n
         res = [1] * n

         #prefix
         for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]

         # postfix
         for i in range(n-2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

         # answer
         for i in range(n):
            res[i] = prefix[i] * postfix[i]
        
         return res

        