from typing import DefaultDict, List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = DefaultDict(int)
        for num in nums:
            counter[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, 0 , -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


nums = [7,7]
k = 1

#Output: [7]

#Output: [2,3]
res = Solution().topKFrequent(nums, k)
print(res)
           
