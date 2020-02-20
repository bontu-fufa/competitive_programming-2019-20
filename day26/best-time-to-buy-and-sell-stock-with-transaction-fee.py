#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        if len(price) == 1: return 0
        
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > buy + fee:
                profit += prices[i] - buy - fee
                buy = prices[i] - fee
            if prices[i] < buy:
                buy = prices[i]
                
                
        return profit
    
