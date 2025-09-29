from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #base case
        if len(nums) == 1:
            return [nums[0]]
        mode = {}
        for num in nums:
            if num in mode:
                mode[num] += 1
            else:
                mode[num] = 1
        f = Counter(mode)
        top_k = f.most_common(k)
        return[num for num, count in top_k] 
