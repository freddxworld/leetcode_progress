from typing import DefaultDict, List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = DefaultDict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            keys[tuple(key)].append(word) 
        return list(keys.values())

strs = ["act","pots","tops","cat","stop","hat"]
res = Solution().groupAnagrams(strs)
print(res)
