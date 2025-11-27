# Last updated: 11/26/2025, 8:55:25 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums_length = len(nums)
        nums_set = set(nums)
        for i in range(1, nums_length+1):
            if i not in nums_set:
                res.append(i)
        return res