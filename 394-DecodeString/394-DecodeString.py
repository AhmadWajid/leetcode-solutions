# Last updated: 11/26/2025, 8:55:26 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            temp = ''
            num = ""
            if i == ']':
                while stack[-1] != '[':
                    temp = stack[-1] + temp
                    stack.pop()
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack[-1] + num
                    stack.pop()
                full = temp * int(num)
                stack.append(full)
            else:
                stack.append(i)
        return ''.join(stack)
