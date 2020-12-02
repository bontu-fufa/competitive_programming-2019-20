class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2: return 0
        profit = 0
        buy_price = curr_max = prices[0]
        for price in prices:
            if curr_max - buy_price > fee and price < curr_max - fee:
                # print("is profit , price is smaller" ,price)
                profit += curr_max - buy_price - fee
                buy_price = price
                curr_max = price
            elif curr_max - buy_price <= fee and price < buy_price:
                # print("update buy - >less" ,price)

                buy_price = price
                curr_max = price
            elif price > curr_max:
                # print("update max price" ,price)

                curr_max = price
        if curr_max - buy_price > fee:
            print(price)
            profit += curr_max - buy_price - fee
        return profit

    
#     another
    class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 1: return 0
        
        buy = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] > buy + fee:
                profit += prices[i] - buy - fee
                buy = prices[i] - fee
            if prices[i] < buy:
                buy = prices[i]
        return profit
