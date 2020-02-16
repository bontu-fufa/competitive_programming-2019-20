#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 0: return 0
        
        buy = - prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            profit = max(profit,buy+prices[i] - fee)
            buy = max(buy,profit-prices[i])
        return profit
    
