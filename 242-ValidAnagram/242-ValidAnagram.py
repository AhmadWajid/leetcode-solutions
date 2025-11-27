# Last updated: 11/26/2025, 9:33:16 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        for letter in t:
            if letter in counter:
                counter[letter] -= 1
                if counter[letter] == 0:
                    del counter[letter]
        return len(counter) == 0