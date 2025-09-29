from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False

        char_tracker = {}

        for char in s:
            if char in char_tracker:
                char_tracker[char] += 1
            else:
                char_tracker[char] = 1

        for char in t:
            if char not in char_tracker:
                return False
            char_tracker[char] -= 1
            if char_tracker[char] < 0:
                return False

        return True
