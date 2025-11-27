# Last updated: 11/26/2025, 8:55:39 PM
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif stack and bracket_map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack