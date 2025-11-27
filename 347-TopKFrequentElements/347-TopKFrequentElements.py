# Last updated: 11/26/2025, 8:55:28 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, num_count in count.items():
            freq[num_count].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res