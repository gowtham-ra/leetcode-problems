class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
                continue

            diff = price - buy
            max_profit = max(diff, max_profit)


        return max_profit
