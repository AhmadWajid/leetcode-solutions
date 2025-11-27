# Last updated: 11/26/2025, 8:55:29 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        total = [1] * len(nums)
        for i in range(len(total)):
            total[i] = left * total[i]
            left = left * nums[i]
        for i in range(len(total)-1, -1, -1):
            total[i] = total[i] * right
            right = right * nums[i]
        return total