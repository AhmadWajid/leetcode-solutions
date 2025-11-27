# Last updated: 11/26/2025, 8:55:32 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}
        majority = len(nums)//2
        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1
            if nums_map[i] > majority:
                return i