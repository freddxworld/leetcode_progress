from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            h = min(height[left_pointer], height[right_pointer])
            area = width * h
            max_amount = max(max_amount, area)
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
                

        return max_amount
#test
height = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(height)
print(result)