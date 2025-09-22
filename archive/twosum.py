from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_numbers = {}
        for index, num in enumerate (nums):
            complement = target - num
            if complement in unique_numbers:
                return [unique_numbers[complement], index]
            unique_numbers[num] = index
#test  case
target = 6
nums = [3,2,4]
result = Solution().twoSum(nums, target)
print(result)
#Input: nums = [3,2,4], target = 6
# may have only one input and has to return target
# Output: [1,2]