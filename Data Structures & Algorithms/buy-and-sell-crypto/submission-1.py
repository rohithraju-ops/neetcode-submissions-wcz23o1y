class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpri = prices[0]
        maxpro = 0

        for price in prices:
            minpri = min(minpri, price)
            profit = price - minpri
            maxpro = max(maxpro, profit)
        
        return maxpro
        