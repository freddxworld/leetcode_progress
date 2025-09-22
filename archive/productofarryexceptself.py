from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        suffix = 1
        for index in range(len(nums)):
            output.append(prefix)
            prefix *= nums[index]
        for index in range(len(nums) - 1, -1, -1):
            output[index] *= suffix
            suffix *= nums[index]
        return output

#test case
nums = [1,2,3,4]
result = Solution().productExceptSelf(nums)
print(result)