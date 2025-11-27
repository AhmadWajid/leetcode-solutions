# Last updated: 11/26/2025, 8:55:32 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            value = numbers[left] + numbers[right]
            if value == target:
                return [left+1, right+1]
            if value > target:
                right -= 1
            if value < target:
                left += 1