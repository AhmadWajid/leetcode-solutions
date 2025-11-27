# Last updated: 11/26/2025, 8:59:15 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        counter = {}
6        for letter in s:
7            if letter in counter:
8                counter[letter] += 1
9            else:
10                counter[letter] = 1
11        for letter in t:
12            if letter in counter:
13                counter[letter] -= 1
14                if counter[letter] == 0:
15                    del counter[letter]
16        return len(counter) == 0