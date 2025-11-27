# Last updated: 11/26/2025, 9:03:38 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4        for i in range(len(nums)):
5            to_find = target - nums[i]
6            if to_find in seen:
7                return [seen[to_find], i]
8            seen[nums[i]] = i
9