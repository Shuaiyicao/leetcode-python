class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
            
        buy = 1<<30
        res = 0
        for price in prices:
            res = max(res, price - buy)
            buy = min(buy, price)
        return res
            
