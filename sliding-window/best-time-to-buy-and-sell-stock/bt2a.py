class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for index, price in enumerate(prices):
            lowest = min(lowest, prices[index])
            profit = max(profit, prices[index] - lowest)
        return profit
