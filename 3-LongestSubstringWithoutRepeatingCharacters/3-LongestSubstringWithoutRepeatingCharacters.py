# Last updated: 11/26/2025, 8:55:43 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            else:
                seen.add(s[r])
                max_length = max(max_length, r-l+1)
        return max_length