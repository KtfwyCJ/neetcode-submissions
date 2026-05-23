class Solution:
    def isValid(self, s: str) -> bool:
        # 栈Stack: 后进先出（LIFO）

        stack = []

        mapping = {
            ')': '(',
            ']':'[',
            '}':'{'
        }

        for c in s:
            if c in "([{":
                stack.append(c)
            
            else:
                # if not stack 等价于 if len(stack) == 0
                if not stack:
                    return False

                if stack[-1] != mapping[c]:
                    return False

                stack.pop()
        return len(stack) == 0