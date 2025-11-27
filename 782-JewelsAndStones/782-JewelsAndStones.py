# Last updated: 11/26/2025, 8:55:23 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel_set = set(jewels)
        for char in stones:
            if char in jewel_set:
                count += 1
        return count