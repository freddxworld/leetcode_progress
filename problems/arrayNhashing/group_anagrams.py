from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Base Case empty array
        if len(strs) == 0:
            return[[""]]
        elif len(strs) == 1:
            return[[strs[0]]]
