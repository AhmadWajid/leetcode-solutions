# Last updated: 11/26/2025, 9:33:28 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in seen:
                return [seen[to_find], i]
            seen[nums[i]] = i
