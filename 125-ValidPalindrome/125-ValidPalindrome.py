# Last updated: 11/26/2025, 8:55:35 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right  and not s[right].isalnum():
                right -=1
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True