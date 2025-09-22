from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float('inf')
        for price in prices:
            lowest_price = min(price, lowest_price)
            profit = price - lowest_price
            max_profit = max(profit, max_profit)
        return max_profit
#test case
#[7,1,5,3,6,4]
prices = [7,6,4,3,1]
result = Solution().maxProfit(prices)
print("target is", result)