class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pri = prices[0]
        max_profit = 0
        for price in prices:
            min_pri = min(min_pri, price)
            profit = price - min_pri
            max_profit = max(max_profit, profit)
        return max_profit 
            
        