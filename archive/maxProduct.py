from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0] 
        min_product = nums[0]
        result = nums[0]
        for num in nums[1:]:
            options = (num, num * max_product, num * min_product)
            max_product = max(options)
            min_product = min(options)
            result = max(result, max_product)
        return result
#test
nums =[-2,0,-1] 
result = Solution().maxProduct(nums)
print(result)