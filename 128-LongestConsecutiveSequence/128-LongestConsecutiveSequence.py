# Last updated: 11/26/2025, 8:55:33 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                temp = 1
                current = num
                while current + 1 in nums:
                    temp += 1
                    current += 1
                longest = max(longest, temp)
        return longest
