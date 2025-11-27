# Last updated: 11/26/2025, 8:55:41 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_volume = 0
        while l < r:
            length = r-l
            tall = min(height[l], height[r])
            temp_volume = length * tall
            max_volume = max(temp_volume, max_volume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_volume
