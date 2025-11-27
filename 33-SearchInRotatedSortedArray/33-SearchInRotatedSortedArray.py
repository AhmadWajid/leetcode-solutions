# Last updated: 11/26/2025, 8:55:37 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums) -1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] == target:
                return mid
            if nums[beg] <= nums[mid]:
                if nums[beg] <= target and nums[mid] > target:
                    end = mid -1 
                else:
                    beg = mid + 1
            else:
                if nums[mid] < target <= nums[end]: 
                    beg = mid + 1
                else:  
                    end = mid - 1
        return -1