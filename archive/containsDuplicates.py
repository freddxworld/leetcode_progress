from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()
        for num in nums:
            if num in unique_numbers:
                return True
            unique_numbers.add(num)
#test case
nums = [1,2,3,1]
result = Solution().containsDuplicate(nums)
print(result)        
#Input: nums = [1,2,3,1]
#Output: true
#Explanatio The element 1 occurs at the indices 0 and 3.