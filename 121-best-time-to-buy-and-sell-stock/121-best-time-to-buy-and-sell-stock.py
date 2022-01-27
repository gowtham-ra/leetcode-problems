import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = math.inf
        max_profit = -math.inf
        
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price-min_val)
        
        return max_profit
        
        
#         buy, sell = prices[0], prices[0]
#         max_profit = 0

#         for price in prices:
#             if price < buy:
#                 buy = price
#                 continue

#             diff = price - buy
#             max_profit = max(diff, max_profit)
            
#         return max_profit
