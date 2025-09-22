from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        sub_array = nums[0]
        for num in nums:
            sub_array = max(num, sub_array + num)
            largest_sum = max(largest_sum, sub_array)
        return largest_sum

#test case
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = Solution().maxSubArray(nums)
print(result)