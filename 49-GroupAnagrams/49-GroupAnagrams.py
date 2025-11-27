# Last updated: 11/26/2025, 8:55:37 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            freq = [0] * 26
            for char in i:
                index = ord(char) - ord('a')
                freq[index] += 1
            freq_tuple = tuple(freq)
            if freq_tuple in group:
                group[freq_tuple].append(i)
            else:
                group[freq_tuple] = [i]
        return [x for x in group.values()]  

