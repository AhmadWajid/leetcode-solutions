# Last updated: 11/26/2025, 9:31:44 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        counter = {}
4        freq_array = [[] for i in range(len(nums)+1)]
5        result = []
6        for num in nums:
7            if num in counter:
8                counter[num] += 1
9            else:
10                counter[num] = 1
11        for key, v in counter.items():
12            freq_array[v].append(key)
13        for i in range(len(nums), 0, -1):
14            for num in freq_array[i]:
15                result.append(num)
16                k -= 1
17                if k == 0:
18                    return result
19                
20