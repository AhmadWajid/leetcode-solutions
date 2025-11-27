# Last updated: 11/26/2025, 8:54:58 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return not len(set(nums)) == len(nums)