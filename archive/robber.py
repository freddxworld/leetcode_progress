from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = 0
        for num in nums[1::2]:
            max_money += num
        return max_money
res einserrst= Solution.rob()