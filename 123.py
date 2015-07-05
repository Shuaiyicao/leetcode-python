class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
            
        sell = {}
        buy = {}
        res = 0
        
        prev_price = 1<<30
        for i in range(n):
            sell[i] = max(0, prices[i] - prev_price)
            prev_price = min(prev_price, prices[i])
            res = max(res, sell[i])
        
        aftr_price = -1<<30
        for i in range(n - 1, -1, -1):
            buy[i] = max(0, aftr_price - prices[i])
            aftr_price = max(aftr_price, prices[i])
        
        for i in range(1, n):
            sell[i] = max(sell[i], sell[i-1])
        
        for i in range(n - 2, -1, -1):
            buy[i] = max(buy[i], buy[i+1])
        
        for i in range(n - 1):
            res = max(res, sell[i] + buy[i+1])
        
        return res
