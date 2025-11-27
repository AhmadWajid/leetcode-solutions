# Last updated: 11/26/2025, 9:12:57 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        anagram_map = {}
4        for word in strs:
5            key = [0] * 26
6            for letter in word:
7                key[ord(letter) - ord('a')] += 1
8            t_key = tuple(key)
9            if t_key in anagram_map:
10                anagram_map[t_key].append(word)
11            else:
12                anagram_map[t_key] = [word]
13        return list(anagram_map.values())